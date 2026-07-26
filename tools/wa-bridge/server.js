/**
 * KORDOVAN WhatsApp BRIDGE  v1.1
 * ============================================================================
 * Runs on a small always-on cloud VM (NOT the office laptop). Holds the
 * WhatsApp session and does two things:
 *   1. POST /send  → sends a text message
 *   2. forwards inbound 1:1 replies to the Cloudflare Worker
 *
 * It deliberately knows NOTHING about Shopify, orders, customers or discounts.
 * No Shopify token lives here. If this box is compromised or the code is shared,
 * no business data goes with it. All logic lives in the Worker.
 *
 * Two browser pages so nobody needs SSH or TeamViewer:
 *   GET /qr?k=ADMIN_KEY      → scan this with the phone to link WhatsApp
 *   GET /status?k=ADMIN_KEY  → live status, queue depth, last error
 *
 * Setup: see README.md
 * ============================================================================
 */

const express = require('express');
const pino = require('pino');
const QR = require('qrcode');
const {
  default: makeWASocket,
  useMultiFileAuthState,
  DisconnectReason,
  fetchLatestBaileysVersion,
} = require('@whiskeysockets/baileys');

// ─── Config (set in .env, never in this file) ────────────────────────────────
const PORT           = process.env.PORT || 8787;
const BRIDGE_SECRET  = process.env.BRIDGE_SECRET || '';   // Worker ⇄ bridge
const ADMIN_KEY      = process.env.ADMIN_KEY || '';       // browser pages only
const WORKER_INBOUND = process.env.WORKER_INBOUND || '';
const AUTH_DIR       = process.env.AUTH_DIR || './auth';
const HOURS_START    = 9;    // 09:00 PKT
const HOURS_END      = 21;   // 21:00 PKT
const JITTER_MIN_MS  = 3000;
const JITTER_MAX_MS  = 10000;

if (!BRIDGE_SECRET || !ADMIN_KEY) {
  console.error('FATAL: BRIDGE_SECRET and ADMIN_KEY must both be set in .env. See README.');
  process.exit(1);
}

let sock = null;
let connected = false;
let currentQR = null;          // data-URL of the pairing QR, null once linked
const stats = { startedAt: Date.now(), sent: 0, failed: 0, lastSent: null, lastError: null, lastInbound: null };

// ─── Helpers ─────────────────────────────────────────────────────────────────

const sleep = ms => new Promise(r => setTimeout(r, ms));
const jitter = () => JITTER_MIN_MS + Math.floor(Math.random() * (JITTER_MAX_MS - JITTER_MIN_MS));
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/** Pakistan phone normalisation → bare 92XXXXXXXXXX. Must match the Worker exactly. */
function normalisePK(raw) {
  let d = String(raw || '').replace(/\D/g, '');
  if (d.startsWith('0092')) d = d.slice(2);
  else if (d.startsWith('00')) d = d.slice(2);
  if (d.startsWith('0')) d = '92' + d.slice(1);
  if (d.length === 10 && d.startsWith('3')) d = '92' + d;
  return /^923\d{9}$/.test(d) ? d : null;
}

/** Hour in PKT regardless of the server's own timezone (cloud VMs default to UTC). */
function pktHour() {
  const now = new Date();
  return new Date(now.getTime() + (300 + now.getTimezoneOffset()) * 60000).getHours();
}
const withinHours = () => { const h = pktHour(); return h >= HOURS_START && h < HOURS_END; };

// ─── Outbound queue ──────────────────────────────────────────────────────────
// Serialised with jitter. Bursts are the strongest ban signal, so messages are
// never sent in parallel and never back to back.

const queue = [];
let draining = false;

async function drain() {
  if (draining) return;
  draining = true;
  while (queue.length) {
    if (!withinHours()) { await sleep(5 * 60 * 1000); continue; }  // hold till morning
    if (!connected) { await sleep(15000); continue; }
    const job = queue.shift();
    try {
      await sleep(jitter());
      await sock.sendMessage(job.jid, { text: job.text });
      stats.sent++; stats.lastSent = { ref: job.ref, at: new Date().toISOString() };
      console.log(`[sent] ${job.ref || ''} → ${job.jid}`);
    } catch (e) {
      stats.failed++; stats.lastError = { ref: job.ref, msg: e.message, at: new Date().toISOString() };
      console.error(`[send-failed] ${job.ref || ''}:`, e.message);
    }
  }
  draining = false;
}

// ─── WhatsApp connection ─────────────────────────────────────────────────────

async function connect() {
  const { state, saveCreds } = await useMultiFileAuthState(AUTH_DIR);
  const { version } = await fetchLatestBaileysVersion();

  sock = makeWASocket({
    version,
    auth: state,
    logger: pino({ level: 'silent' }),
    markOnlineOnConnect: false,   // don't steal "online" from the team's phone
    syncFullHistory: false,
  });

  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('connection.update', async ({ connection, lastDisconnect, qr }) => {
    if (qr) {
      currentQR = await QR.toDataURL(qr, { width: 320, margin: 2 }).catch(() => null);
      console.log('[wa] pairing QR ready — open /qr in a browser to scan');
    }
    if (connection === 'open') {
      connected = true; currentQR = null;
      console.log('[wa] connected');
    }
    if (connection === 'close') {
      connected = false;
      const code = lastDisconnect?.error?.output?.statusCode;
      const loggedOut = code === DisconnectReason.loggedOut;
      console.log(`[wa] disconnected (${code}) — ${loggedOut ? 'LOGGED OUT: delete auth folder and re-scan' : 'reconnecting in 5s'}`);
      if (!loggedOut) setTimeout(connect, 5000);
    }
  });

  // Inbound: forward raw text to the Worker. Never interpret it here.
  sock.ev.on('messages.upsert', async ({ messages, type }) => {
    if (type !== 'notify' || !WORKER_INBOUND) return;
    for (const m of messages) {
      try {
        const jid = m.key?.remoteJid || '';
        if (m.key?.fromMe) continue;                      // our own sends
        if (!jid.endsWith('@s.whatsapp.net')) continue;   // groups, status, channels
        const text = m.message?.conversation
                  || m.message?.extendedTextMessage?.text
                  || m.message?.buttonsResponseMessage?.selectedDisplayText
                  || m.message?.listResponseMessage?.title
                  || '';
        if (!text.trim()) continue;
        const from = normalisePK(jid.split('@')[0]);
        if (!from) continue;

        stats.lastInbound = { from, at: new Date().toISOString() };
        await fetch(WORKER_INBOUND, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Bridge-Secret': BRIDGE_SECRET },
          body: JSON.stringify({ from, text: text.trim(), ts: Date.now() }),
        }).catch(e => console.error('[inbound-forward-failed]', e.message));
        console.log(`[recv] ${from}: ${text.trim().slice(0, 40)}`);
      } catch (e) {
        console.error('[inbound-error]', e.message);   // never let this kill the session
      }
    }
  });
}

// ─── HTTP ────────────────────────────────────────────────────────────────────

const app = express();
app.use(express.json({ limit: '64kb' }));

const admin = (req, res, next) =>
  req.query.k === ADMIN_KEY ? next() : res.status(401).send('Unauthorized');

app.get('/health', (_req, res) =>
  res.json({ ok: true, connected, queued: queue.length, withinHours: withinHours() }));

/** Pairing QR in the browser — no SSH, no TeamViewer. Auto-refreshes. */
app.get('/qr', admin, (_req, res) => {
  res.set('Content-Type', 'text/html').send(`<!doctype html>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Link WhatsApp — Kordovan</title>
<style>body{font-family:system-ui,sans-serif;background:#F7F2EA;color:#241C16;display:flex;
min-height:100vh;align-items:center;justify-content:center;margin:0;padding:20px}
.c{text-align:center;background:#fff;padding:32px;border-radius:14px;box-shadow:0 10px 40px rgba(0,0,0,.08);max-width:420px}
h1{font-size:20px;margin:0 0 6px}p{color:#6b6257;font-size:14px;line-height:1.6}
img{width:300px;height:300px;image-rendering:pixelated}
.ok{color:#1f6e4d;font-weight:600;font-size:17px}</style>
<div class="c">
${connected
  ? `<h1>✅ WhatsApp is linked</h1><p class="ok">Connected and running.</p>
     <p>Nothing to do here. Check <a href="/status?k=${encodeURIComponent(ADMIN_KEY)}">status</a>.</p>`
  : currentQR
    ? `<h1>Scan to link WhatsApp</h1>
       <p>On the business phone: <b>WhatsApp → Settings → Linked devices → Link a device</b>, then scan this.</p>
       <img src="${currentQR}" alt="WhatsApp pairing QR">
       <p>This page refreshes itself. The code rotates every ~20 seconds — that is normal.</p>`
    : `<h1>Starting…</h1><p>Waiting for a pairing code. This page refreshes automatically.</p>`}
</div>
<script>setTimeout(()=>location.reload(),15000)</script>`);
});

/** Live status page — "keep checking it when I need to". */
app.get('/status', admin, (_req, res) => {
  const up = Math.floor((Date.now() - stats.startedAt) / 1000);
  const hrs = `${Math.floor(up / 3600)}h ${Math.floor((up % 3600) / 60)}m`;
  const row = (k, v) => `<tr><td>${k}</td><td><b>${v}</b></td></tr>`;
  res.set('Content-Type', 'text/html').send(`<!doctype html>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bridge status — Kordovan</title>
<style>body{font-family:system-ui,sans-serif;background:#F7F2EA;color:#241C16;padding:24px;margin:0}
.c{max-width:560px;margin:0 auto;background:#fff;padding:26px;border-radius:14px;box-shadow:0 10px 40px rgba(0,0,0,.06)}
h1{font-size:19px;margin:0 0 16px}table{width:100%;border-collapse:collapse;font-size:14px}
td{padding:9px 0;border-bottom:1px solid #eee}td:last-child{text-align:right}
.on{color:#1f6e4d}.off{color:#8B2D2D}small{color:#8B8174}</style>
<div class="c"><h1>WhatsApp bridge</h1><table>
${row('WhatsApp', connected ? '<span class="on">connected</span>' : '<span class="off">disconnected</span>')}
${row('Queued right now', queue.length)}
${row('Sending window (09–21 PKT)', withinHours() ? '<span class="on">open</span>' : 'closed — holding')}
${row('Hour in Pakistan', pktHour() + ':00')}
${row('Sent since restart', stats.sent)}
${row('Failed since restart', stats.failed)}
${row('Uptime', hrs)}
${row('Last sent', stats.lastSent ? esc(stats.lastSent.ref) + '<br><small>' + esc(stats.lastSent.at) + '</small>' : '—')}
${row('Last reply in', stats.lastInbound ? esc(stats.lastInbound.from) + '<br><small>' + esc(stats.lastInbound.at) + '</small>' : '—')}
${row('Last error', stats.lastError ? '<span class="off">' + esc(stats.lastError.msg) + '</span><br><small>' + esc(stats.lastError.at) + '</small>' : 'none')}
</table><p><small>Refreshes every 20s. ${connected ? '' : '<a href="/qr?k=' + encodeURIComponent(ADMIN_KEY) + '">Link WhatsApp →</a>'}</small></p></div>
<script>setTimeout(()=>location.reload(),20000)</script>`);
});

app.post('/send', (req, res, next) => {
  if (req.get('X-Bridge-Secret') !== BRIDGE_SECRET) return res.status(401).json({ ok: false, error: 'unauthorized' });
  next();
}, async (req, res) => {
  const { to, text, ref } = req.body || {};
  const num = normalisePK(to);
  if (!num || !text) return res.status(400).json({ ok: false, error: 'bad_request' });
  if (!connected || !sock) return res.status(503).json({ ok: false, error: 'session_disconnected' });

  // Never send blind. Messaging numbers not on WhatsApp looks like scraping and
  // is a ban signal — and the "not on WhatsApp" answer is exactly what tells the
  // Worker to flag the order for a phone call instead.
  try {
    const [found] = await sock.onWhatsApp(num);
    if (!found?.exists) return res.json({ ok: true, sent: false, reason: 'not_on_whatsapp' });
    queue.push({ jid: found.jid, text, ref });
    drain();
    return res.json({ ok: true, sent: true, queued: queue.length });
  } catch (e) {
    return res.status(502).json({ ok: false, error: e.message });
  }
});

app.listen(PORT, () => console.log(`[http] bridge listening on :${PORT}`));
connect().catch(e => { console.error('FATAL', e); process.exit(1); });
