/**
 * KORDOVAN WhatsApp BRIDGE
 * ============================================================================
 * Runs on the office laptop. Holds the WhatsApp session and does two things:
 *   1. POST /send      → sends a text message
 *   2. forwards inbound 1:1 replies to the Cloudflare Worker
 *
 * It deliberately knows NOTHING about Shopify, orders, customers or discounts.
 * No Shopify token lives here. If this machine is lost or this file is shared,
 * no business data goes with it. All logic lives in the Worker.
 *
 * Setup: see README.md in this folder.
 * ============================================================================
 */

const express = require('express');
const pino = require('pino');
const qrcode = require('qrcode-terminal');
const {
  default: makeWASocket,
  useMultiFileAuthState,
  DisconnectReason,
  fetchLatestBaileysVersion,
} = require('@whiskeysockets/baileys');

// ─── Config (edit .env, not this file) ───────────────────────────────────────
const PORT          = process.env.PORT || 8787;
const BRIDGE_SECRET = process.env.BRIDGE_SECRET || '';
const WORKER_INBOUND= process.env.WORKER_INBOUND || '';   // …/wa-inbound
const AUTH_DIR      = process.env.AUTH_DIR || './auth';   // keep separate from POS bot
const TZ_OFFSET_MIN = 5 * 60;                             // PKT = UTC+5
const HOURS_START   = 9;   // 09:00 PKT
const HOURS_END     = 21;  // 21:00 PKT
const JITTER_MIN_MS = 3000;
const JITTER_MAX_MS = 10000;

if (!BRIDGE_SECRET) { console.error('FATAL: BRIDGE_SECRET is not set. See README.'); process.exit(1); }

let sock = null;
let connected = false;

// ─── Helpers ─────────────────────────────────────────────────────────────────

const sleep = ms => new Promise(r => setTimeout(r, ms));
const jitter = () => JITTER_MIN_MS + Math.floor(Math.random() * (JITTER_MAX_MS - JITTER_MIN_MS));

/** Pakistan phone normalisation → bare 92XXXXXXXXXX. Must match the Worker. */
function normalisePK(raw) {
  let d = String(raw || '').replace(/\D/g, '');
  if (d.startsWith('0092')) d = d.slice(2);
  else if (d.startsWith('00')) d = d.slice(2);
  if (d.startsWith('0')) d = '92' + d.slice(1);
  if (d.length === 10 && d.startsWith('3')) d = '92' + d;
  return /^923\d{9}$/.test(d) ? d : null;
}

/** Current hour in PKT, regardless of the laptop's own timezone. */
function pktHour() {
  const now = new Date();
  return new Date(now.getTime() + (TZ_OFFSET_MIN + now.getTimezoneOffset()) * 60000).getHours();
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
    if (!withinHours()) {           // hold until morning rather than message at 3am
      await sleep(5 * 60 * 1000);
      continue;
    }
    const job = queue.shift();
    try {
      await sleep(jitter());
      await sock.sendMessage(job.jid, { text: job.text });
      console.log(`[sent] ${job.ref || ''} → ${job.jid}`);
    } catch (e) {
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

  sock.ev.on('connection.update', ({ connection, lastDisconnect, qr }) => {
    if (qr) {
      console.log('\n─── Scan this QR with the WhatsApp you want to link ───\n');
      qrcode.generate(qr, { small: true });
    }
    if (connection === 'open') {
      connected = true;
      console.log('[wa] connected');
    }
    if (connection === 'close') {
      connected = false;
      const code = lastDisconnect?.error?.output?.statusCode;
      const loggedOut = code === DisconnectReason.loggedOut;
      console.log(`[wa] disconnected (${code}) — ${loggedOut ? 'LOGGED OUT, delete auth dir and re-scan' : 'reconnecting in 5s'}`);
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

// ─── HTTP API ────────────────────────────────────────────────────────────────

const app = express();
app.use(express.json({ limit: '64kb' }));

function auth(req, res, next) {
  if (req.get('X-Bridge-Secret') !== BRIDGE_SECRET) return res.status(401).json({ ok: false, error: 'unauthorized' });
  next();
}

app.get('/health', (_req, res) =>
  res.json({ ok: true, connected, queued: queue.length, pktHour: pktHour(), withinHours: withinHours() }));

app.post('/send', auth, async (req, res) => {
  const { to, text, ref } = req.body || {};
  const num = normalisePK(to);
  if (!num || !text) return res.status(400).json({ ok: false, error: 'bad_request' });
  if (!connected || !sock) return res.status(503).json({ ok: false, error: 'session_disconnected' });

  // Never send blind. Messaging numbers that are not on WhatsApp looks like
  // scraping and is a ban signal — and the "not on WhatsApp" answer is exactly
  // what tells the Worker to flag the order for a phone call instead.
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
