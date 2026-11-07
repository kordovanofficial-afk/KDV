// Kordovan WhatsApp Front Desk — Cloudflare Worker (free plan)
// Receives Kapso webhooks for the team WhatsApp number and does the routine work instantly,
// with zero AI cost:
//   1. "STORE SALES ..." reports  -> subtract each line from Shopify stock, reply with the result
//   2. "STOCK <name>"             -> reply with current stock for matching products
//   3. anything else from the team-> quick acknowledgement, saved for Claude's nightly run
//   4. strangers                  -> one polite redirect per day to the public order line
// Everything that happens is recorded per day in KV, read by Claude at 23:30 PKT via GET /day.
//
// Bindings (Cloudflare → Worker → Settings → Variables and Secrets / Bindings):
//   DESK_KV            KV namespace
//   KAPSO_API_KEY      secret  (Kapso → API keys)
//   WEBHOOK_SECRET     secret  (same value you give Kapso as the webhook secret)
//   DESK_SECRET        secret  (any long random string; Claude uses it to read /day)
//   SHOPIFY_STORE      var     e.g. kordovan.myshopify.com
//   SHOPIFY_CLIENT_ID / SHOPIFY_CLIENT_SECRET  secrets (same app as the PostEx worker)  — or SHOPIFY_TOKEN
//   PHONE_NUMBER_ID    var     1352393681300763
//   ALLOWLIST          var     923005555968,923002042352,923042528729
//   LOCATION_ID        var     gid://shopify/Location/36710940861

const VERSION = 'desk-1.1';
const SHOPIFY_API = '2026-01';
const KAPSO_BASE = 'https://api.kapso.ai/meta/whatsapp/v24.0';
const PUBLIC_LINE = '0333 2601161';
const ACK_COOLDOWN_S = 10 * 60;       // at most one "got it" per sender per 10 min (never silent for long)
const STRANGER_COOLDOWN_S = 24 * 3600;
const CATALOG_TTL_S = 6 * 3600;
const DAY_TTL_S = 14 * 24 * 3600;

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    if (req.method === 'GET' && url.pathname === '/health') {
      return json({ status: 'ok', version: VERSION, ts: new Date().toISOString() });
    }
    if (req.method === 'GET' && url.pathname === '/day') {
      if (!authed(req, env)) return json({ error: 'unauthorized' }, 401);
      const day = url.searchParams.get('d') || pktDay();
      return json(await getDay(env, day));
    }
    if (req.method === 'GET' && url.pathname === '/selftest') {
      // public on purpose: returns only yes/no checks, never a secret or customer data
      return json(await selftest(env));
    }
    if (req.method === 'POST' && url.pathname === '/webhook') {
      const raw = await req.text();
      if (!(await validSignature(raw, req.headers.get('x-webhook-signature'), env.WEBHOOK_SECRET))) {
        return json({ error: 'bad signature' }, 401);
      }
      const event = req.headers.get('x-webhook-event') || '';
      const idem = req.headers.get('x-idempotency-key') || '';
      if (event !== 'whatsapp.message.received') return json({ ok: true, ignored: event });
      if (idem) {
        if (await env.DESK_KV.get('idem:' + idem)) return json({ ok: true, duplicate: true });
        await env.DESK_KV.put('idem:' + idem, '1', { expirationTtl: 3600 });
      }
      let body;
      try { body = JSON.parse(raw); } catch { return json({ error: 'bad json' }, 400); }
      const payloads = body && body.batch === true && Array.isArray(body.data) ? body.data : [body];
      // Kapso needs 200 within 10s: do the work in the background.
      ctx.waitUntil(Promise.all(payloads.map(p => handleMessage(p, env).catch(e => logError(env, e)))));
      return json({ ok: true });
    }
    return json({ error: 'Not found' }, 404);
  },
};

// ─── message routing ─────────────────────────────────────────────────────────

export async function handleMessage(payload, env) {
  const m = payload && payload.message;
  if (!m) return;
  const from = String(m.from || '').replace(/\D/g, '');
  const text = (m.text && m.text.body) || (m.kapso && m.kapso.content) || '';
  const allow = String(env.ALLOWLIST || '').split(',').map(s => s.trim()).filter(Boolean);
  const day = pktDay();

  if (!allow.includes(from)) {
    await appendDay(env, day, 'strangers', { from, text: text.slice(0, 500), at: nowIso() });
    if (!(await env.DESK_KV.get('stranger:' + from))) {
      await env.DESK_KV.put('stranger:' + from, '1', { expirationTtl: STRANGER_COOLDOWN_S });
      await sendText(env, from,
        `Assalam o Alaikum! This is Kordovan's internal team line. For orders and help, please WhatsApp us at ${PUBLIC_LINE}. Thank you!`);
    }
    return;
  }

  const trimmed = text.trim();
  if (/^store\s*sales?\b/i.test(trimmed)) return handleSalesReport(trimmed, from, env, day);
  if (/^stock\b/i.test(trimmed)) return handleStockQuery(trimmed.replace(/^stock\b[:\s-]*/i, ''), from, env);
  // Natural questions: "what's the update on the kodo stock", "how many bastion left", "mocha kitne hain"
  if (/\b(stock|inventory|left|available|kitn[aei]|kitne|baqi|bachay?)\b/i.test(trimmed)) {
    const q = stockQueryFromQuestion(trimmed);
    if (q && (await handleStockQuery(q, from, env, true))) return;
  }

  await appendDay(env, day, 'inbox', { from, type: m.type || 'text', text: text.slice(0, 2000), at: nowIso() });
  if (!(await env.DESK_KV.get('ack:' + from))) {
    await env.DESK_KV.put('ack:' + from, '1', { expirationTtl: ACK_COOLDOWN_S });
    await sendText(env, from, "Got it, thank you. I'll get back to you properly tonight by 11:30 PM. - Claude");
  }
}

// ─── STORE SALES ─────────────────────────────────────────────────────────────

export function parseSalesLines(text) {
  const lines = text.split(/\r?\n/).slice(1).map(l => l.trim().replace(/^[-•*·]\s*/, '').replace(/^\d+[.)]\s+/, '').trim()).filter(Boolean);
  // strips bullets and "1." / "1)" numbering, keeps "2 x Razor" quantities
  return lines.map(raw => {
    let name = raw, qty = 1, mm;
    if ((mm = raw.match(/^(.*?)[\s,]*[x×*]\s*(\d+)\s*(pcs?|pieces?)?$/i))) { name = mm[1]; qty = +mm[2]; }
    else if ((mm = raw.match(/^(.*?)[\s,:-]+(\d+)\s*(pcs?|pieces?)?$/i))) { name = mm[1]; qty = +mm[2]; }
    else if ((mm = raw.match(/^(\d+)\s*[x×*]?\s+(.*)$/i))) { qty = +mm[1]; name = mm[2]; }
    return { raw, name: name.trim(), qty };
  }).filter(l => l.name && l.qty > 0 && l.qty < 100);
}

async function handleSalesReport(text, from, env, day) {
  const lines = parseSalesLines(text);
  if (!lines.length) {
    await sendText(env, from, 'I could not read any items. Please send one item per line, e.g.\nSTORE SALES 08-Nov\nMocha Mate Brown x1\nRazor Black x2');
    return;
  }
  const catalog = await getCatalog(env);
  const done = [], unclear = [], failed = [];
  for (const l of lines) {
    const hits = matchVariants(catalog, l.name);
    if (hits.length !== 1) {
      unclear.push({ ...l, options: hits.slice(0, 5).map(h => h.label) });
      continue;
    }
    const v = hits[0];
    try {
      const after = await adjustStock(env, v, -l.qty, `${day}-${from}-${l.raw}`);
      done.push({ ...l, label: v.label, variantId: v.id, after });
    } catch (e) {
      failed.push({ ...l, label: v.label, error: String(e.message || e).slice(0, 200) });
    }
  }
  await appendDay(env, day, 'sales', { from, at: nowIso(), done, unclear, failed });

  let msg = done.length ? `Done: ${done.length} item${done.length > 1 ? 's' : ''} updated on the website.\n` +
    done.map(d => `- ${d.label} -${d.qty} (now ${d.after ?? '?'})`).join('\n') : 'No items were updated.';
  if (unclear.length) {
    msg += '\n\nPlease clarify:\n' + unclear.map(u => u.options.length
      ? `- "${u.name}" matches: ${u.options.join(' / ')}`
      : `- "${u.name}": no matching product found`).join('\n');
    msg += '\nReply with STORE SALES and the exact names for these lines only.';
  }
  if (failed.length) msg += '\n\nCould not update: ' + failed.map(f => f.label).join(', ') + '. Claude will check tonight.';
  await sendText(env, from, msg);
}

// ─── STOCK lookup ────────────────────────────────────────────────────────────

export function stockQueryFromQuestion(t) {
  const FILL = new Set(['what','whats','what s','is','are','the','on','of','for','about','update','latest','any','news',
    'stock','inventory','left','available','how','many','much','do','we','have','our','still','in','please','pls','plz',
    'kitna','kitni','kitne','hain','hai','he','ka','ki','ke','baqi','bacha','bachay','bache','abhi','website','online',
    'wallet','wallets','check','tell','me','give','current','status','count','qty','quantity','units','pieces','pcs']);
  return norm(t.replace(/[’'`]/g, '')).split(' ').filter(w => w.length >= 2 && !FILL.has(w)).join(' ');
}

async function handleStockQuery(q, from, env, quiet = false) {
  const catalog = await getCatalog(env);
  let hits = matchVariants(catalog, q);
  if (!hits.length && q.includes(' ')) {
    // be forgiving: try each word alone and keep the first word that matches something
    for (const w of q.split(' ').filter(x => x.length >= 3)) { hits = matchVariants(catalog, w); if (hits.length) break; }
  }
  hits = hits.slice(0, 12);
  if (!hits.length) {
    if (quiet) return false;
    await sendText(env, from, `No product found for "${q}". Try a shorter name, e.g. STOCK mocha mate`); return false;
  }
  const fresh = await freshQuantities(env, hits.map(h => h.id));
  await sendText(env, from, 'Website stock:\n' + hits.map(h =>
    `- ${h.label}: ${fresh[h.id] === null ? 'not tracked (made to order / always available)' : fresh[h.id]}`).join('\n'));
  return true;
}

// ─── matching ────────────────────────────────────────────────────────────────

const norm = s => String(s || '').toLowerCase().replace(/kordovan|\/\/|[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
const STOP = new Set(['the', 'a', 'an', 'of', 'and', 'by', 'leather', 'genuine', 'pc', 'pcs']);

export function matchVariants(catalog, query) {
  const toks = norm(query).split(' ').filter(t => t && !STOP.has(t));
  if (!toks.length) return [];
  const hits = catalog.filter(v => {
    const words = v.norm.split(' ');
    return toks.every(t => words.some(w => w === t || (t.length >= 3 && w.startsWith(t))));
  });
  if (hits.length <= 1) return hits;
  // Tie-break: "KODO Black" should pick "— Black", not "— Black Gold". Keep hits whose whole
  // variant title is named in the query.
  const exact = hits.filter(v => v.vt && v.vt.split(' ').every(w => toks.includes(w)));
  return exact.length === 1 ? exact : hits;
}

async function getCatalog(env) {
  const cached = await env.DESK_KV.get('catalog', 'json');
  if (cached) return cached;
  const out = [];
  let after = null;
  for (let page = 0; page < 10; page++) {
    const d = await shopify(env, `query($after:String){ products(first:100, after:$after, query:"-status:archived"){
      pageInfo{hasNextPage endCursor}
      nodes{ title variants(first:100){ nodes{ id title inventoryItem{ id tracked } } } } } }`, { after });
    for (const p of d.products.nodes) {
      for (const v of p.variants.nodes) {
        const label = v.title && v.title !== 'Default Title' ? `${p.title} — ${v.title}` : p.title;
        out.push({ id: v.id, item: v.inventoryItem.id, tracked: v.inventoryItem.tracked, label, norm: norm(label),
          vt: v.title && v.title !== 'Default Title' ? norm(v.title) : '' });
      }
    }
    if (!d.products.pageInfo.hasNextPage) break;
    after = d.products.pageInfo.endCursor;
  }
  await env.DESK_KV.put('catalog', JSON.stringify(out), { expirationTtl: CATALOG_TTL_S });
  return out;
}

async function freshQuantities(env, ids) {
  const d = await shopify(env, `query($ids:[ID!]!){ nodes(ids:$ids){ ... on ProductVariant{ id inventoryQuantity inventoryItem{ tracked } } } }`, { ids });
  const out = {};
  for (const n of d.nodes) if (n) out[n.id] = n.inventoryItem.tracked ? n.inventoryQuantity : null;
  return out;
}

async function adjustStock(env, v, delta, keySeed) {
  if (!v.tracked) throw new Error('stock not tracked for this item');
  const key = await sha256hex(keySeed);
  const d = await shopify(env, `mutation($input:InventoryAdjustQuantitiesInput!){
    inventoryAdjustQuantities(input:$input) @idempotent(key:"${key}") { userErrors{ field message } } }`,
    { input: { reason: 'correction', name: 'available', referenceDocumentUri: 'kordovan://store-sales',
      changes: [{ inventoryItemId: v.item, locationId: env.LOCATION_ID, delta }] } });
  const errs = d.inventoryAdjustQuantities.userErrors;
  if (errs && errs.length) throw new Error(errs.map(e => e.message).join('; '));
  const q = await freshQuantities(env, [v.id]);
  return q[v.id];
}

// ─── Shopify ─────────────────────────────────────────────────────────────────

async function shopifyToken(env) {
  if (env.SHOPIFY_CLIENT_ID && env.SHOPIFY_CLIENT_SECRET) {
    const c = await env.DESK_KV.get('shopify_token', 'json');
    if (c && c.token) return c.token;
    const r = await fetch(`https://${env.SHOPIFY_STORE}/admin/oauth/access_token`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ client_id: env.SHOPIFY_CLIENT_ID, client_secret: env.SHOPIFY_CLIENT_SECRET, grant_type: 'client_credentials' }),
    });
    if (r.ok) {
      const j = await r.json();
      await env.DESK_KV.put('shopify_token', JSON.stringify({ token: j.access_token }), { expirationTtl: 20 * 3600 });
      return j.access_token;
    }
  }
  if (env.SHOPIFY_TOKEN) return env.SHOPIFY_TOKEN;
  throw new Error('no Shopify credentials');
}

async function shopify(env, query, variables) {
  const r = await fetch(`https://${env.SHOPIFY_STORE}/admin/api/${SHOPIFY_API}/graphql.json`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': await shopifyToken(env) },
    body: JSON.stringify({ query, variables }),
  });
  const j = await r.json();
  if (!r.ok || j.errors) throw new Error('Shopify: ' + JSON.stringify(j.errors || r.status).slice(0, 300));
  return j.data;
}

// ─── Kapso ───────────────────────────────────────────────────────────────────

export async function sendText(env, to, body) {
  const r = await fetch(`${KAPSO_BASE}/${env.PHONE_NUMBER_ID}/messages`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-API-Key': env.KAPSO_API_KEY },
    body: JSON.stringify({ messaging_product: 'whatsapp', to, type: 'text', text: { body: body.slice(0, 4000) } }),
  });
  if (!r.ok) await logError(env, new Error(`send ${r.status}: ${(await r.text()).slice(0, 300)}`));
}

// ─── storage & helpers ───────────────────────────────────────────────────────

async function getDay(env, day) {
  return (await env.DESK_KV.get('day:' + day, 'json')) || { day, sales: [], inbox: [], strangers: [], errors: [] };
}
async function appendDay(env, day, field, entry) {
  const d = await getDay(env, day);
  (d[field] = d[field] || []).push(entry);
  await env.DESK_KV.put('day:' + day, JSON.stringify(d), { expirationTtl: DAY_TTL_S });
}
async function logError(env, e) {
  try { await appendDay(env, pktDay(), 'errors', { at: nowIso(), error: String(e && e.message || e).slice(0, 500) }); } catch {}
}

async function selftest(env) {
  const out = { version: VERSION };
  try {
    const d = await shopify(env, `{ currentAppInstallation{ accessScopes{ handle } } location(id:"${env.LOCATION_ID}"){ name } }`);
    const scopes = d.currentAppInstallation.accessScopes.map(s => s.handle);
    out.shopify = { ok: true, location: d.location && d.location.name,
      read_products: scopes.includes('read_products') || scopes.includes('write_products'),
      write_inventory: scopes.includes('write_inventory') };
  } catch (e) { out.shopify = { ok: false, error: String(e.message) }; }
  out.catalogCached = !!(await env.DESK_KV.get('catalog'));
  out.vars = ['KAPSO_API_KEY', 'WEBHOOK_SECRET', 'PHONE_NUMBER_ID', 'ALLOWLIST', 'LOCATION_ID', 'SHOPIFY_STORE']
    .filter(k => !env[k]);
  out.missing = out.vars; delete out.vars;
  return out;
}

function authed(req, env) {
  return env.DESK_SECRET && req.headers.get('x-desk-secret') === env.DESK_SECRET;
}
async function validSignature(raw, sig, secret) {
  if (!secret || !sig) return false;
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(raw));
  const hex = [...new Uint8Array(mac)].map(b => b.toString(16).padStart(2, '0')).join('');
  if (hex.length !== sig.length) return false;
  let diff = 0;
  for (let i = 0; i < hex.length; i++) diff |= hex.charCodeAt(i) ^ sig.charCodeAt(i);
  return diff === 0;
}
async function sha256hex(s) {
  const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 40);
}
function pktDay() { return new Date(Date.now() + 5 * 3600 * 1000).toISOString().slice(0, 10); }
function nowIso() { return new Date().toISOString(); }
function json(o, status = 200) { return new Response(JSON.stringify(o), { status, headers: { 'Content-Type': 'application/json' } }); }
