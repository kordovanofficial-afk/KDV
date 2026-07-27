/**
 * KORDOVAN × POSTEX SYNC WORKER v6.0
 *
 * v6.0 (Jul 27 2026) — WhatsApp order confirmation + delivery updates.
 *   POST /shopify-order?s=WEBHOOK_TOKEN Shopify orders/create webhook
 *   POST /wa-inbound                    replies forwarded by the bridge
 *   GET  /wa-status?s=SYNC_SECRET       queue depth + bridge reachability
 *
 * Messages are QUEUED IN KV, never sent inline, and drained on the hourly cron.
 * The bridge lives on a small VM that can reboot or lose network; queueing means
 * nothing is lost when it does.
 * Requires env: BRIDGE_URL, BRIDGE_SECRET, WEBHOOK_TOKEN.
 *
 * v5.0
 *
 * v5.0 (Jul 26 2026) — adds a PUBLIC tracking endpoint for the storefront:
 *   GET /track?cn=<trackingNumber>
 * so the Track Your Order page can show live status in a popup without the
 * PostEx token ever reaching the browser.
 *
 * ⚠️ SECURITY — DO NOT MAKE /track A PASSTHROUGH ⚠️
 * /track is public and keyed only by a tracking number, and PostEx numbers are
 * guessable. The PostEx `dist` payload contains customer name, phone, delivery
 * address and the COD amount. Returning it raw would let anyone enumerate
 * numbers and harvest the customer base. Only the allowlist in sanitiseTrack()
 * may leave this Worker. Never `return Response.json(dist)`.
 *
 * v4.0 behaviour is unchanged:
 * - Individual PostEx track calls instead of bulk (bulk misses Delivered status)
 * - KV token renewal fixed — always refreshes before expiry
 * - note_attributes tracking extraction added (hxs_courier_tracking)
 * - Webhook + hourly cron both fully operational
 */

const POSTEX_BASE  = 'https://api.postex.pk/services/integration/api/order/v1';
const SHOPIFY_API  = '2024-01';

const DELIVERED_STATUS = 'Delivered';
const RTO_STATUSES     = ['Returned', 'Out For Return'];
const OUT_FOR_DELIVERY = 'out for delivery';   // matched lowercase; PostEx casing varies

// ─── WhatsApp ───────────────────────────────────────────────────────────────
// Quiet hours apply to MARKETING only (kind: 'mktg'). Transactional messages —
// order confirmations, delivery updates — go out 24/7: an order placed at 2am
// needs its confirm/cancel window immediately, and the customer is expecting to
// hear from us because they just checked out. Unsolicited offers at 2am are the
// thing that earns spam reports, so those still wait for morning.
const WA_HOURS_START = 9;      // 09:00 PKT — marketing only
const WA_HOURS_END   = 21;
const WA_MAX_TRIES   = 24;     // ~24h of hourly retries, then give up
const WA_QUEUE_CAP   = 12;     // max drained per cron tick
const STORE_URL      = 'https://kordovanleather.com';

// Storefront origins allowed to call the public /track endpoint.
const TRACK_ALLOWED_ORIGINS = [
  'https://kordovanleather.com',
  'https://www.kordovanleather.com',
];

// ─── Entry Point ──────────────────────────────────────────────────────────────

export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil((async () => {
      await runPollSync(env);
      await waDrain(env);        // retry anything the bridge could not take earlier
    })());
  },

  async fetch(request, env, ctx) {
    const url  = new URL(request.url);
    const cors = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, X-Sync-Secret',
    };

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors });

    if (url.pathname === '/health')
      return Response.json({ status: 'ok', ts: new Date().toISOString() }, { headers: cors });

    // ─── PUBLIC: storefront tracking lookup ───────────────────────────────────
    if (url.pathname === '/track') {
      return handlePublicTrack(request, env, ctx);
    }

    // One-off diagnostic: returns ONLY the key names PostEx sends, never the
    // values, so the sanitiseTrack allowlist can be checked against reality
    // without leaking customer data. Safe to leave in place (secret-protected).
    if (url.pathname === '/track-debug') {
      if (request.headers.get('X-Sync-Secret') !== env.SYNC_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      const cn = url.searchParams.get('cn');
      try {
        const dist = await trackSinglePostEx(cn, env.POSTEX_TOKEN);
        const historyKeys = Array.isArray(dist.transactionStatusHistory) && dist.transactionStatusHistory[0]
          ? Object.keys(dist.transactionStatusHistory[0]) : null;
        return Response.json({ keys: Object.keys(dist), historyItemKeys: historyKeys }, { headers: cors });
      } catch (e) {
        return Response.json({ error: e.message }, { status: 404, headers: cors });
      }
    }

    if (url.pathname === '/webhook/postex') {
      ctx.waitUntil(handleWebhook(request, env));
      return new Response('OK', { status: 200 });
    }

    if (url.pathname === '/sync') {
      if (request.headers.get('X-Sync-Secret') !== env.SYNC_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      const result = await runPollSync(env);
      return Response.json(result, { headers: cors });
    }

    if (url.pathname === '/stats') {
      if (request.headers.get('X-Sync-Secret') !== env.SYNC_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      return Response.json(await getStats(env), { headers: cors });
    }

    // ─── WhatsApp ─────────────────────────────────────────────────────────────
    // Authenticated with its OWN token, not SYNC_SECRET. The URL is stored in
    // Shopify admin and echoed in delivery logs, so it must not carry the secret
    // that also unlocks /sync, /stats and /wa-drain. SYNC_SECRET is still
    // accepted so an already-registered webhook keeps working.
    if (url.pathname === '/shopify-order') {
      const s = url.searchParams.get('s');
      const authed = Boolean(s) && (s === env.WEBHOOK_TOKEN || s === env.SYNC_SECRET);

      // ?probe=1 → read the breadcrumb trail instead of processing an order.
      if (authed && url.searchParams.get('probe') === '1')
        return Response.json(await getWebhookHits(env), { headers: cors });

      // Record EVERY hit, accepted or rejected, BEFORE the auth check. Without
      // this there is no way to distinguish "Shopify never called" from
      // "Shopify called and we turned it away" — and those need opposite fixes.
      ctx.waitUntil(recordWebhookHit(env, request, s, authed));

      if (!authed) return Response.json(waAuthDiagnosis(s, env), { status: 401, headers: cors });
      ctx.waitUntil(handleNewOrder(request, env));
      return new Response('OK', { status: 200 });   // ack fast; Shopify retries on slow
    }

    if (url.pathname === '/wa-inbound') {
      if (request.headers.get('X-Bridge-Secret') !== env.BRIDGE_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      ctx.waitUntil(handleInbound(request, env));
      return new Response('OK', { status: 200 });
    }

    if (url.pathname === '/wa-status') {
      if (url.searchParams.get('s') !== env.SYNC_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      return Response.json(await waStatus(env), { headers: cors });
    }

    if (url.pathname === '/wa-drain') {
      if (url.searchParams.get('s') !== env.SYNC_SECRET)
        return Response.json({ error: 'Unauthorized' }, { status: 401, headers: cors });
      return Response.json(await waDrain(env), { headers: cors });
    }

    return Response.json({ error: 'Not found' }, { status: 404, headers: cors });
  }
};

// ─── PUBLIC TRACKING ──────────────────────────────────────────────────────────

async function handlePublicTrack(request, env, ctx) {
  const url    = new URL(request.url);
  const origin = request.headers.get('Origin') || '';
  const allow  = TRACK_ALLOWED_ORIGINS.includes(origin) ? origin : TRACK_ALLOWED_ORIGINS[0];

  const headers = {
    'Access-Control-Allow-Origin': allow,
    'Content-Type': 'application/json',
    'Cache-Control': 'public, max-age=60',
  };

  // Reject implausible input before spending a PostEx call on it.
  const cn = (url.searchParams.get('cn') || '').trim();
  if (!/^[A-Za-z0-9-]{6,30}$/.test(cn)) {
    return Response.json(
      { ok: false, error: 'invalid_number', message: 'That does not look like a tracking number.' },
      { status: 400, headers }
    );
  }

  // Edge cache: a customer refreshing, or someone sweeping numbers, costs
  // PostEx nothing for 2 minutes.
  const cacheKey = new Request(`https://track.internal/${cn}`, { method: 'GET' });
  const cache    = caches.default;
  const hit      = await cache.match(cacheKey);
  if (hit) {
    const cached = await hit.json();
    return Response.json(cached, { headers });
  }

  let dist;
  try {
    dist = await trackSinglePostEx(cn, env.POSTEX_TOKEN);
  } catch (e) {
    const notFound = e.message.includes('RECORD NOT FOUND');
    return Response.json(
      {
        ok: false,
        error: notFound ? 'not_found' : 'upstream_error',
        message: notFound
          ? "We can't find that tracking number yet. Newly dispatched orders can take a few hours to appear."
          : 'Tracking is temporarily unavailable. Please try again shortly, or message us on WhatsApp.',
      },
      { status: notFound ? 404 : 502, headers }
    );
  }

  const payload = sanitiseTrack(dist, cn);

  ctx.waitUntil(
    cache.put(
      cacheKey,
      new Response(JSON.stringify(payload), {
        headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=120' },
      })
    )
  );

  return Response.json(payload, { headers });
}

/**
 * Allowlist. Anything not named here is dropped.
 *
 * DELIBERATELY EXCLUDED — do not add:
 *   customerName / consigneeName / customerPhone / phone → PII
 *   deliveryAddress / address                            → PII
 *   invoicePayment / codAmount                           → reveals order value
 *   orderRefNumber                                       → maps to a Shopify order
 */
function sanitiseTrack(dist, cn) {
  const pick = (...keys) => {
    for (const k of keys) {
      if (dist[k] !== undefined && dist[k] !== null && dist[k] !== '') return dist[k];
    }
    return null;
  };

  const rawHistory =
    pick('transactionStatusHistory', 'statusHistory', 'trackingHistory', 'history') || [];

  const history = (Array.isArray(rawHistory) ? rawHistory : [])
    .map(h => ({
      status: h.transactionStatusMessage || h.transactionStatus || h.status || h.statusMessage || null,
      at:     h.updatedAt || h.transactionDate || h.modifiedDatetime || h.date || null,
    }))
    .filter(h => h.status)
    .slice(-12);

  return {
    ok: true,
    trackingNumber: cn,
    status: pick('transactionStatus', 'orderStatus', 'status'),
    city:   pick('cityName', 'destinationCity', 'city'),
    updatedAt: pick('transactionDate', 'updatedAt', 'modifiedDatetime', 'orderDate'),
    history,
  };
}


// ═══════════════════════════════════════════════════════════════════════════
// WHATSAPP  —  queue, messaging, order state
//
// Nothing is sent inline. Everything is queued in KV and drained on the hourly
// cron (plus one immediate attempt). The bridge runs on a small VM that can
// reboot, lose network or be rate-limited; queueing means a customer message is
// never silently lost because the box happened to be down.
// ═══════════════════════════════════════════════════════════════════════════

/** Pakistan phone normalisation → bare 923XXXXXXXXX. MUST match the bridge. */
function normalisePK(raw) {
  let d = String(raw || '').replace(/\D/g, '');
  if (d.startsWith('0092')) d = d.slice(2);
  else if (d.startsWith('00')) d = d.slice(2);
  if (d.startsWith('0')) d = '92' + d.slice(1);
  if (d.length === 10 && d.startsWith('3')) d = '92' + d;
  return /^923\d{9}$/.test(d) ? d : null;
}

function pktHour() {
  const now = new Date();
  return new Date(now.getTime() + (300 + now.getTimezoneOffset()) * 60000).getHours();
}
const waWithinHours = () => { const h = pktHour(); return h >= WA_HOURS_START && h < WA_HOURS_END; };

/**
 * Queue a message. `ref` makes the send idempotent across cron re-runs.
 * `kind` is 'txn' (default, sends at any hour) or 'mktg' (holds for 09–21 PKT).
 */
async function waEnqueue(env, { to, text, ref, kind }) {
  if (!env.SYNC_KV) return { ok: false, error: 'no_kv' };
  const phone = normalisePK(to);
  if (!phone || !text) return { ok: false, error: 'bad_input' };

  // Never message someone who asked us to stop. Permanent, no expiry.
  if (await env.SYNC_KV.get(`waopt:${phone}`)) return { ok: false, error: 'opted_out' };
  // Already sent this exact thing — the cron re-runs, duplicates get you blocked.
  if (await env.SYNC_KV.get(`wasent:${ref}`)) return { ok: false, error: 'already_sent' };

  const key = `waq:${Date.now()}:${Math.random().toString(36).slice(2, 8)}`;
  await env.SYNC_KV.put(key, JSON.stringify({
    to: phone, text, ref, tries: 0, firstAt: Date.now(),
    kind: kind === 'mktg' ? 'mktg' : 'txn',
  }), { expirationTtl: 60 * 60 * 30 });
  return { ok: true, queued: key };
}

/** Hand one message to the bridge. Returns the bridge's own verdict. */
async function waSendViaBridge(env, to, text, ref, kind) {
  if (!env.BRIDGE_URL || !env.BRIDGE_SECRET) return { ok: false, error: 'bridge_not_configured' };
  const res = await fetch(`${env.BRIDGE_URL.replace(/\/+$/, '')}/send`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-Bridge-Secret': env.BRIDGE_SECRET },
    body: JSON.stringify({ to, text, ref, kind: kind === 'mktg' ? 'mktg' : 'txn' }),
  });
  return res.json();
}

/**
 * Drain the queue. Leaves anything it cannot deliver in place for the next tick.
 * After WA_MAX_TRIES (~24h) it gives up and flags the order for a phone call —
 * silence is worse than a wrong channel.
 */
async function waDrain(env) {
  const out = { drained: 0, sent: 0, noWhatsapp: 0, retry: 0, gaveUp: 0, heldMarketing: 0 };
  if (!env.SYNC_KV) return out;
  const hoursOpen = waWithinHours();

  const list = await env.SYNC_KV.list({ prefix: 'waq:', limit: WA_QUEUE_CAP });
  for (const k of list.keys) {
    const raw = await env.SYNC_KV.get(k.name);
    if (!raw) continue;
    let job; try { job = JSON.parse(raw); } catch { await env.SYNC_KV.delete(k.name); continue; }

    // Marketing waits for daylight. Transactional never does — leave the job
    // untouched (no `tries` increment, so holding overnight cannot burn through
    // the retry budget and give up on it).
    if (job.kind === 'mktg' && !hoursOpen) { out.heldMarketing++; continue; }
    out.drained++;

    let r;
    try { r = await waSendViaBridge(env, job.to, job.text, job.ref, job.kind); }
    catch (e) { r = { ok: false, error: e.message }; }

    if (r.ok && r.sent) {
      out.sent++;
      await env.SYNC_KV.put(`wasent:${job.ref}`, '1', { expirationTtl: 60 * 60 * 24 * 30 });
      await env.SYNC_KV.delete(k.name);

    } else if (r.ok && r.sent === false && r.reason === 'not_on_whatsapp') {
      // Not a failure — actionable information. Tell the team to phone them.
      out.noWhatsapp++;
      await env.SYNC_KV.delete(k.name);
      const orderId = (job.ref || '').split(':')[0];
      if (orderId) await tagOrderSafe(env, orderId, ['📞 NO WHATSAPP — CALL']);

    } else {
      job.tries = (job.tries || 0) + 1;
      if (job.tries >= WA_MAX_TRIES) {
        out.gaveUp++;
        await env.SYNC_KV.delete(k.name);
        const orderId = (job.ref || '').split(':')[0];
        if (orderId) await tagOrderSafe(env, orderId, ['📞 NO WHATSAPP — CALL']);
      } else {
        out.retry++;
        await env.SYNC_KV.put(k.name, JSON.stringify(job), { expirationTtl: 60 * 60 * 30 });
      }
    }
  }
  return out;
}

async function waStatus(env) {
  const q = env.SYNC_KV ? await env.SYNC_KV.list({ prefix: 'waq:', limit: 1000 }) : { keys: [] };
  let bridge = 'unknown';
  try {
    const r = await fetch(`${(env.BRIDGE_URL || '').replace(/\/+$/, '')}/health`);
    bridge = r.ok ? await r.json() : `http_${r.status}`;
  } catch (e) { bridge = `unreachable: ${e.message}`; }
  return {
    queued: q.keys.length,
    transactionalSending: '24/7',
    marketingWindowOpen: waWithinHours(),   // 09–21 PKT, marketing only
    pktHour: pktHour(),
    bridgeConfigured: Boolean(env.BRIDGE_URL && env.BRIDGE_SECRET),
    bridge,
  };
}

// ─── Shopify GraphQL (the REST helper above stays for the payment path) ──────

async function shopifyGQL(query, variables, token, env) {
  const res = await fetch(`https://${env.SHOPIFY_STORE}/admin/api/${SHOPIFY_API}/graphql.json`, {
    method: 'POST',
    headers: { 'X-Shopify-Access-Token': token, 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables }),
  });
  const d = await res.json();
  if (d.errors) throw new Error(JSON.stringify(d.errors).slice(0, 200));
  return d.data;
}

/**
 * Tag an order. Never throws — a tagging failure must not break a send.
 * Returns null on success, or the error message, so callers can record why a
 * tag never appeared instead of the failure vanishing into the console.
 */
async function tagOrderSafe(env, orderIdNum, tags) {
  try {
    const token = await getShopifyToken(env);
    const d = await shopifyGQL(
      `mutation($id: ID!, $tags: [String!]!) {
         tagsAdd(id: $id, tags: $tags) { userErrors { message } } }`,
      { id: `gid://shopify/Order/${orderIdNum}`, tags }, token, env);
    const errs = d?.tagsAdd?.userErrors || [];
    if (errs.length) return errs.map(e => e.message).join('; ');
    return null;
  } catch (e) { console.error('tagOrderSafe:', e.message); return e.message; }
}

// ─── Message copy ────────────────────────────────────────────────────────────

const waFirstName = o =>
  (o?.customer?.first_name || o?.shipping_address?.first_name || '').trim().split(' ')[0] || 'there';

const waMoney = v => `PKR ${Math.round(Number(v || 0)).toLocaleString('en-PK')}`;

function msgOrderPlaced(order) {
  const items = (order.line_items || [])
    .map(li => `• ${li.title}${li.quantity > 1 ? ` ×${li.quantity}` : ''}`).join('\n');
  const city = order.shipping_address?.city || '';
  return `Assalam o Alaikum ${waFirstName(order)} 👋

Thank you for your Kordovan order *${order.name}*:
${items}

Total: *${waMoney(order.total_price)}* (Cash on Delivery)${city ? `\nDelivery to: ${city}` : ''}

Please reply *CONFIRM* to lock your order, or *CANCEL* if you have changed your mind.

— Kordovan
_Reply STOP to stop updates._`;
}

function msgOutForDelivery(order) {
  return `${waFirstName(order)}, your Kordovan order *${order.name}* is out for delivery today 🛵

Please keep *${waMoney(order.total_price)}* ready and stay reachable — the rider will call before arriving.

Track it: ${STORE_URL}/pages/track-order
_Reply STOP to stop updates._`;
}

function msgDelivered(order) {
  return `Shukriya ${waFirstName(order)} 🙏

Your Kordovan order *${order.name}* has been delivered. Good leather only gets better with use — if anything is not right, just reply here and we will sort it.

${STORE_URL}
_Reply STOP to stop updates._`;
}

/**
 * Breadcrumb trail for /shopify-order. Keeps the last 8 hits so a silent
 * failure can be told apart from a rejected one. Shopify stamps its own
 * headers on every webhook, so their presence proves the caller was Shopify
 * and not something else knocking.
 */
async function recordWebhookHit(env, request, supplied, authed) {
  if (!env.SYNC_KV) return;
  try {
    const hit = {
      at: new Date().toISOString(),
      authed,
      method: request.method,
      suppliedLength: supplied ? supplied.length : 0,
      shopifyTopic:  request.headers.get('X-Shopify-Topic')       || null,
      shopifyDomain: request.headers.get('X-Shopify-Shop-Domain') || null,
    };
    const raw  = await env.SYNC_KV.get('wahook:hits');
    const hits = raw ? JSON.parse(raw) : [];
    hits.unshift(hit);
    await env.SYNC_KV.put('wahook:hits', JSON.stringify(hits.slice(0, 8)),
      { expirationTtl: 60 * 60 * 24 * 7 });
  } catch (e) { console.error('recordWebhookHit:', e.message); }
}

async function getWebhookHits(env) {
  const raw  = env.SYNC_KV ? await env.SYNC_KV.get('wahook:hits') : null;
  const hits = raw ? JSON.parse(raw) : [];
  const lastRaw = env.SYNC_KV ? await env.SYNC_KV.get('wahook:lastorder') : null;
  return {
    now: new Date().toISOString(),
    lastOrderProcessing: lastRaw ? JSON.parse(lastRaw) : null,
    whatsapp: await waStatus(env),
    totalRecorded: hits.length,
    verdict: hits.length === 0
      ? 'Nothing has EVER called /shopify-order. Shopify is not sending — the webhook is missing, points somewhere else, or is on the wrong event.'
      : (hits.some(h => h.authed && h.shopifyTopic)
          ? 'Shopify has reached this Worker successfully. If orders are still untagged, the problem is after the webhook.'
          : 'Something called, but was rejected or was not Shopify. Check the entries below.'),
    hits,
  };
}

/**
 * Why a 401 happened, without leaking the secret.
 *
 * A bare "Unauthorized" cannot distinguish "the variable never reached the
 * Worker" from "the token in the URL is wrong" — and those need opposite fixes.
 * This reports SHAPES only: binding names, lengths, and whether the two would
 * match after trimming. No part of either token is ever echoed back, so this is
 * safe to leave on a public route.
 */
function waAuthDiagnosis(supplied, env) {
  const cfg = env.WEBHOOK_TOKEN;
  let diagnosis;
  if (!cfg)           diagnosis = 'WEBHOOK_TOKEN is NOT set on this Worker. The variable did not reach the deployed version — add it, then Deploy.';
  else if (!supplied) diagnosis = 'The URL has no ?s= value at all.';
  else if (supplied.trim() === cfg.trim())
                      diagnosis = 'They match except for whitespace — one of them has a stray space or newline. Re-add the variable, taking care not to copy a trailing space.';
  else if (supplied.startsWith(cfg))
                      diagnosis = 'The correct token is there, with extra characters stuck on the end. See unexpectedSuffix below — delete exactly that from the URL.';
  else if (cfg.startsWith(supplied))
                      diagnosis = 'The token in the URL is cut short. Re-paste the full URL into the webhook.';
  else                diagnosis = 'The token in the URL is a different value from WEBHOOK_TOKEN.';

  const out = {
    error: 'Unauthorized',
    diagnosis,
    suppliedLength:   supplied ? supplied.length : 0,
    configuredLength: cfg ? cfg.length : 0,
    expectedLength:   36,
    bindings: Object.keys(env).sort(),   // names only — never values
  };

  // Safe to echo: this is the junk AFTER a full correct token, so it is by
  // definition not part of the secret. It is the only way to see what got
  // picked up during the copy — invisible characters included.
  if (supplied && cfg && supplied.startsWith(cfg) && supplied !== cfg) {
    const extra = supplied.slice(cfg.length);
    out.unexpectedSuffix = extra;
    out.unexpectedSuffixCodes = [...extra].map(c => c.charCodeAt(0));
  }
  return out;
}

// ─── New order → confirmation ask ────────────────────────────────────────────

/**
 * This runs inside ctx.waitUntil, AFTER the 200 has gone back to Shopify, so a
 * throw in here is invisible from every angle — Shopify sees success, the order
 * gets no tag, no message is sent, and nothing surfaces anywhere. The trace
 * below is written whatever happens (note the `finally`) and is readable via
 * ?probe=1, so a silent failure always leaves evidence.
 */
async function handleNewOrder(request, env) {
  const trace = { at: new Date().toISOString(), stage: 'start' };
  try {
    let order;
    try { order = await request.json(); } catch { trace.stage = 'bad_json'; return; }
    if (!order?.id) { trace.stage = 'no_order_id'; return; }

    trace.orderId         = order.id;
    trace.orderName       = order.name;
    trace.financialStatus = order.financial_status || null;
    trace.lineItemCount   = (order.line_items || []).length;

    const phone = normalisePK(
      order.phone || order.shipping_address?.phone || order.billing_address?.phone || order.customer?.phone);
    trace.phoneNormalised = Boolean(phone);
    trace.phoneTail = phone ? `…${phone.slice(-4)}` : null;

    if (!phone) {
      trace.stage = 'no_usable_phone';
      trace.tagError = await tagOrderSafe(env, order.id, ['📞 NO WHATSAPP — CALL']);
      return;
    }

    // Prepaid orders do not need a COD confirmation.
    if (order.financial_status && order.financial_status !== 'pending') {
      trace.stage = 'skipped_not_cod';
      return;
    }

    // Remember who this phone belongs to so a bare "CONFIRM" can be matched back.
    if (env.SYNC_KV) {
      await env.SYNC_KV.put(`wapend:${phone}`, JSON.stringify({
        orderId: order.id, name: order.name, total: order.total_price, at: Date.now(),
      }), { expirationTtl: 60 * 60 * 48 });
    }

    trace.stage = 'composing';
    const text = msgOrderPlaced(order);
    trace.messageLength = text.length;

    trace.stage = 'enqueueing';
    const r = await waEnqueue(env, { to: phone, text, ref: `${order.id}:placed` });
    trace.enqueue = r;

    if (r.ok) {
      trace.stage = 'tagging';
      trace.tagError = await tagOrderSafe(env, order.id, ['⏳ WA SENT']);
      trace.stage = 'draining';
      trace.drain = await waDrain(env);   // try immediately; the queue is the safety net
      trace.stage = 'done';
    } else {
      trace.stage = 'enqueue_refused';
    }
  } catch (e) {
    trace.stage = trace.stage + '_THREW';
    trace.error = e.message;
    trace.stack = String(e.stack || '').split('\n').slice(0, 3).join(' | ');
  } finally {
    if (env.SYNC_KV) {
      await env.SYNC_KV.put('wahook:lastorder', JSON.stringify(trace),
        { expirationTtl: 60 * 60 * 24 * 7 }).catch(() => {});
    }
  }
}

// ─── Customer replies ────────────────────────────────────────────────────────

async function handleInbound(request, env) {
  let body; try { body = await request.json(); } catch { return; }
  const phone = normalisePK(body?.from);
  const text  = String(body?.text || '').trim();
  if (!phone || !text) return;

  const norm = text.toLowerCase().replace(/[^a-z؀-ۿ]/g, '');

  // Opt-out is honoured for anyone, order or not, permanently.
  if (norm === 'stop' || norm === 'unsubscribe') {
    if (env.SYNC_KV) await env.SYNC_KV.put(`waopt:${phone}`, '1');
    return;
  }

  if (!env.SYNC_KV) return;
  const pendRaw = await env.SYNC_KV.get(`wapend:${phone}`);
  if (!pendRaw) return;   // not awaiting anything from this number — stay silent
  let pend; try { pend = JSON.parse(pendRaw); } catch { return; }

  const isConfirm = ['confirm', 'confirmed', 'yes', 'ok', 'okay', 'haan', 'han', 'jee', 'ji', 'theek'].includes(norm);
  const isCancel  = ['cancel', 'cancelled', 'cancelorder', 'no'].includes(norm);

  if (isConfirm) {
    await tagOrderSafe(env, pend.orderId, ['✅ WA CONFIRMED']);
    await env.SYNC_KV.delete(`wapend:${phone}`);
    await waEnqueue(env, {
      to: phone,
      text: `Shukriya! Your order *${pend.name}* is confirmed ✅\n\nWe will dispatch it shortly and send you the tracking details.\n\n— Kordovan`,
      ref: `${pend.orderId}:confirmack`,
    });
    await waDrain(env);
    return;
  }

  if (isCancel) {
    await handleCancelRequest(env, phone, pend, text);
    return;
  }

  // Anything else is a real conversation — leave it for the team's phone.
}

/**
 * Cancellation. orderCancel is IRREVERSIBLE, so every guardrail below is
 * mandatory and anything ambiguous is handed to a human instead of guessed.
 */
async function handleCancelRequest(env, phone, pend, rawText) {
  const token = await getShopifyToken(env);

  const data = await shopifyGQL(
    `query($id: ID!) { order(id: $id) {
        id name displayFinancialStatus displayFulfillmentStatus cancelledAt
        phone shippingAddress { phone }
      } }`,
    { id: `gid://shopify/Order/${pend.orderId}` }, token, env);

  const o = data?.order;
  if (!o || o.cancelledAt) { await env.SYNC_KV.delete(`wapend:${phone}`); return; }

  // 1. IDENTITY — the sender must be the phone on the order. This is the check
  //    that makes auto-cancel safe rather than reckless.
  const orderPhone = normalisePK(o.phone || o.shippingAddress?.phone);
  if (!orderPhone || orderPhone !== phone) {
    await tagOrderSafe(env, pend.orderId, ['⚠️ WA CANCEL — VERIFY']);
    return;
  }

  // 2. Already dispatched → too late to cancel; this is an RTO decision.
  if (o.displayFulfillmentStatus === 'FULFILLED') {
    await tagOrderSafe(env, pend.orderId, ['↩️ WA CANCEL AFTER DISPATCH']);
    await env.SYNC_KV.delete(`wapend:${phone}`);
    await waEnqueue(env, {
      to: phone,
      text: `Your order *${pend.name}* has already been dispatched, so we cannot cancel it automatically.\n\nOur team will call you shortly to sort this out.\n\n— Kordovan`,
      ref: `${pend.orderId}:cancellate`,
    });
    await waDrain(env);
    return;
  }

  // 3. COD only. Anything paid involves a refund — that goes to a human.
  if (o.displayFinancialStatus !== 'PENDING') {
    await tagOrderSafe(env, pend.orderId, ['⚠️ WA CANCEL — VERIFY']);
    return;
  }

  const res = await shopifyGQL(
    `mutation($id: ID!) {
       orderCancel(orderId: $id, reason: CUSTOMER, refund: false,
                   restock: true, notifyCustomer: false) {
         userErrors { message } } }`,
    { id: `gid://shopify/Order/${pend.orderId}` }, token, env);

  const errs = res?.orderCancel?.userErrors || [];
  if (errs.length) {
    console.error('orderCancel:', JSON.stringify(errs));
    await tagOrderSafe(env, pend.orderId, ['⚠️ WA CANCEL — VERIFY']);
    return;
  }

  await tagOrderSafe(env, pend.orderId, ['🚫 WA CANCELLED']);
  await addOrderNote(pend.orderId,
    `🚫 Cancelled on customer request via WhatsApp\nFrom: ${phone}\nMessage: "${rawText}"\nAt: ${new Date().toLocaleString('en-PK', { timeZone: 'Asia/Karachi' })}`,
    token, env);
  await env.SYNC_KV.delete(`wapend:${phone}`);

  await waEnqueue(env, {
    to: phone,
    text: `Your order *${pend.name}* has been cancelled as requested.\n\nIf that was a mistake, just reply here and we will help you reorder.\n\n— Kordovan`,
    ref: `${pend.orderId}:cancelack`,
  });
  await waDrain(env);
}

// ─── Token Management ─────────────────────────────────────────────────────────
// Always fetches a fresh token. Caches in KV for 22 hours.
// Falls back to SHOPIFY_TOKEN env var if refresh fails.

async function getShopifyToken(env) {
  // Try KV cache first
  if (env.SYNC_KV) {
    try {
      const raw = await env.SYNC_KV.get('shopify_token');
      if (raw) {
        const cached = JSON.parse(raw);
        const expiresAt = new Date(cached.expiresAt).getTime();
        // Use cached token if it has more than 2 hours left
        if (expiresAt > Date.now() + 2 * 60 * 60 * 1000) {
          console.log(`Using cached token, expires ${cached.expiresAt}`);
          return cached.token;
        }
      }
    } catch (e) {
      console.log('KV read failed:', e.message);
    }
  }

  // Fetch fresh token
  console.log('Fetching fresh Shopify token...');
  try {
    const res = await fetch(`https://${env.SHOPIFY_STORE}/admin/oauth/access_token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        client_id: env.SHOPIFY_CLIENT_ID,
        client_secret: env.SHOPIFY_CLIENT_SECRET,
        grant_type: 'client_credentials'
      })
    });

    if (!res.ok) throw new Error(`Token endpoint ${res.status}`);

    const data      = await res.json();
    const token     = data.access_token;
    const expiresIn = data.expires_in || 86399;
    const expiresAt = new Date(Date.now() + expiresIn * 1000).toISOString();

    console.log(`Fresh token obtained, expires ${expiresAt}`);

    // Cache in KV for 22 hours
    if (env.SYNC_KV) {
      await env.SYNC_KV.put(
        'shopify_token',
        JSON.stringify({ token, expiresAt }),
        { expirationTtl: 22 * 60 * 60 }
      ).catch(e => console.log('KV write failed:', e.message));
    }

    return token;

  } catch (e) {
    console.log(`Token refresh failed: ${e.message} — falling back to env token`);
    // Fallback to manually set token
    if (env.SHOPIFY_TOKEN) return env.SHOPIFY_TOKEN;
    throw new Error('No valid Shopify token available');
  }
}

// ─── Webhook Handler ──────────────────────────────────────────────────────────

async function handleWebhook(request, env) {
  let payload;
  try { payload = await request.json(); }
  catch (e) { console.error('Webhook parse failed:', e.message); return; }

  console.log('Webhook received:', JSON.stringify(payload));

  const status      = payload.transactionStatus || payload.orderStatus || '';
  const orderRef    = payload.orderRefNumber || payload.orderRef || '';
  const trackingNum = payload.trackingNumber || '';
  const amount      = payload.invoicePayment || payload.amount || null;

  if (!orderRef && !trackingNum) {
    console.log('Webhook: no ref or tracking — skipping');
    return;
  }

  let token;
  try { token = await getShopifyToken(env); }
  catch (e) { console.error('Webhook: token failed:', e.message); return; }

  let order = null;
  if (orderRef) order = await findOrderByRef(orderRef, token, env);
  if (!order && trackingNum) order = await findOrderByTracking(trackingNum, token, env);

  if (!order) {
    console.log(`Webhook: no order found ref=${orderRef} tracking=${trackingNum}`);
    return;
  }

  const now = new Date().toLocaleString('en-PK', { timeZone: 'Asia/Karachi' });

  if (status === DELIVERED_STATUS) {
    if (order.financial_status === 'paid') {
      console.log(`Order ${order.order_number} already paid`);
      return;
    }
    try {
      await markOrderPaid(order.id, amount || order.total_price, trackingNum, orderRef, token, env);
      console.log(`Webhook: ✅ Order ${order.order_number} marked paid`);
      await incrementStat(env, 'webhookPaid');
    } catch (e) {
      console.error(`Webhook mark paid failed:`, e.message);
    }
  } else if (RTO_STATUSES.includes(status)) {
    try {
      await addOrderNote(order.id,
        `⚠️ RTO — PostEx: "${status}"\nTracking: ${trackingNum}\nRef: ${orderRef}\nUpdated: ${now}\nSource: PostEx webhook`,
        token, env);
      await incrementStat(env, 'webhookRTO');
    } catch (e) {
      console.error(`Webhook RTO note failed:`, e.message);
    }
  }
}

// ─── Poll Sync ────────────────────────────────────────────────────────────────
// Checks each order individually against PostEx track API.
// Individual calls return full delivery detail — bulk track does not.

async function runPollSync(env) {
  const start = Date.now();
  const result = {
    trigger: 'poll', startedAt: new Date().toISOString(),
    ordersChecked: 0, markedPaid: 0, rtoFlagged: 0,
    errors: 0, skipped: 0, log: []
  };

  const log = msg => {
    console.log(msg);
    result.log.push({ ts: new Date().toISOString(), msg });
  };

  try {
    let token;
    try {
      token = await getShopifyToken(env);
      log('Shopify token ready');
    } catch (e) {
      log(`FATAL: Token failed — ${e.message}`);
      result.errors++;
      return finalize(result, start, env);
    }

    log('Fetching open COD orders from Shopify...');
    const orders = await getOpenCODOrders(token, env);
    log(`Found ${orders.length} open fulfilled+pending orders`);
    result.ordersChecked = orders.length;

    if (!orders.length) return finalize(result, start, env);

    // Extract tracking numbers — check fulfillments AND note_attributes
    const withTracking = [];
    for (const o of orders) {
      const tn = getTrackingNumber(o);
      if (tn) {
        withTracking.push({ order: o, tracking: tn });
      } else {
        result.skipped++;
      }
    }

    log(`${withTracking.length} have tracking | ${result.skipped} skipped (no tracking)`);

    if (!withTracking.length) return finalize(result, start, env);

    log(`Checking ${withTracking.length} orders against PostEx individually...`);

    // Check individually — more reliable than bulk for delivery status
    for (const item of withTracking) {
      const o  = item.order;
      const tn = item.tracking;
      const now = new Date().toLocaleString('en-PK', { timeZone: 'Asia/Karachi' });

      try {
        const postexData = await trackSinglePostEx(tn, env.POSTEX_TOKEN);
        const status     = postexData.transactionStatus || '';
        const amount     = postexData.invoicePayment || o.total_price;

        if (status === DELIVERED_STATUS) {
          if (o.financial_status === 'paid') {
            log(`Order #${o.order_number} already paid — skipping`);
            result.skipped++;
            continue;
          }
          log(`Order #${o.order_number} [${tn}] — DELIVERED → marking paid`);
          try {
            await markOrderPaid(o.id, String(amount), tn, o.name, token, env);
            result.markedPaid++;
            log(`Order #${o.order_number} ✅ marked paid (PKR ${amount})`);
            // Delivered → thank-you. ref keeps it to exactly one per order.
            const phD = normalisePK(o.phone || o.shipping_address?.phone || o.customer?.phone);
            if (phD) await waEnqueue(env, { to: phD, text: msgDelivered(o), ref: `${o.id}:delivered` });
          } catch (e) {
            log(`Order #${o.order_number} mark paid ERROR: ${e.message}`);
            result.errors++;
          }
        } else if (String(status).toLowerCase() === OUT_FOR_DELIVERY) {
          const phO = normalisePK(o.phone || o.shipping_address?.phone || o.customer?.phone);
          if (phO) await waEnqueue(env, { to: phO, text: msgOutForDelivery(o), ref: `${o.id}:ofd` });
          result.skipped++;
        } else if (RTO_STATUSES.includes(status)) {
          try {
            await addOrderNote(o.id,
              `⚠️ RTO — PostEx: "${status}" | Tracking: ${tn} | ${now} | Via hourly sync`,
              token, env);
            result.rtoFlagged++;
            log(`Order #${o.order_number} ↩️ RTO noted (${status})`);
          } catch (e) {
            log(`Order #${o.order_number} RTO note ERROR: ${e.message}`);
            result.errors++;
          }
        } else {
          result.skipped++;
        }

        await sleep(150); // Respect PostEx rate limits

      } catch (e) {
        // PostEx not found or error — skip silently
        if (!e.message.includes('RECORD NOT FOUND')) {
          log(`Order #${o.order_number} PostEx error: ${e.message}`);
          result.errors++;
        } else {
          result.skipped++;
        }
      }
    }

  } catch (e) {
    log(`FATAL: ${e.message}`);
    result.errors++;
  }

  return finalize(result, start, env);
}

function finalize(result, start, env) {
  result.durationMs  = Date.now() - start;
  result.completedAt = new Date().toISOString();
  console.log(`[DONE] paid=${result.markedPaid} rto=${result.rtoFlagged} err=${result.errors} ${result.durationMs}ms`);

  if (env?.SYNC_KV) {
    env.SYNC_KV.put('last_sync', JSON.stringify(result), { expirationTtl: 86400 * 7 })
      .catch(() => {});
    env.SYNC_KV.get('totals').then(raw => {
      const t = raw ? JSON.parse(raw) : { markedPaid: 0, rtoFlagged: 0, syncsRun: 0, webhookPaid: 0, webhookRTO: 0 };
      t.markedPaid += result.markedPaid;
      t.rtoFlagged += result.rtoFlagged;
      t.syncsRun   += 1;
      return env.SYNC_KV.put('totals', JSON.stringify(t));
    }).catch(() => {});
  }

  return result;
}

async function getStats(env) {
  if (!env?.SYNC_KV) return { error: 'KV not configured' };
  const [a, b] = await Promise.all([env.SYNC_KV.get('last_sync'), env.SYNC_KV.get('totals')]);
  return { lastSync: a ? JSON.parse(a) : null, totals: b ? JSON.parse(b) : {} };
}

async function incrementStat(env, key) {
  if (!env?.SYNC_KV) return;
  try {
    const raw = await env.SYNC_KV.get('totals');
    const t   = raw ? JSON.parse(raw) : { markedPaid: 0, rtoFlagged: 0, syncsRun: 0, webhookPaid: 0, webhookRTO: 0 };
    t[key]    = (t[key] || 0) + 1;
    await env.SYNC_KV.put('totals', JSON.stringify(t));
  } catch (e) {}
}

// ─── Shopify Helpers ──────────────────────────────────────────────────────────

async function shopifyFetch(path, token, env, options = {}) {
  const url = `https://${env.SHOPIFY_STORE}/admin/api/${SHOPIFY_API}${path}`;
  const res = await fetch(url, {
    ...options,
    headers: {
      'X-Shopify-Access-Token': token,
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Shopify ${res.status}: ${text.slice(0, 200)}`);
  }
  return res.json();
}

async function getOpenCODOrders(token, env) {
  const data = await shopifyFetch(
    `/orders.json?status=any&financial_status=pending&fulfillment_status=fulfilled&limit=250&fields=id,order_number,name,financial_status,total_price,payment_gateway,fulfillments,note_attributes,phone,customer,shipping_address,line_items`,
    token, env
  );
  return (data.orders || []).filter(o => {
    const gw = (o.payment_gateway || '').toLowerCase();
    return !['stripe','paypal','jazzcash','easypaisa','credit_card','debit_card','shopify_payments'].some(g => gw.includes(g));
  });
}

function getTrackingNumber(order) {
  // Check fulfillments first
  for (const f of (order.fulfillments || [])) {
    if (f.tracking_number) return f.tracking_number;
    if (f.tracking_numbers?.length) return f.tracking_numbers[0];
  }
  // Check note_attributes — PostEx Shopify app stores tracking here as hxs_courier_tracking
  const trackingKeys = ['tracking_number', 'hxs_courier_tracking', 'tracking', 'postex_tracking'];
  for (const a of (order.note_attributes || [])) {
    if (trackingKeys.includes((a.name || '').toLowerCase()) && a.value) {
      return a.value;
    }
  }
  return null;
}

async function findOrderByRef(orderRef, token, env) {
  const clean = orderRef.replace(/[^0-9a-zA-Z#]/g, '');
  try {
    const d = await shopifyFetch(
      `/orders.json?name=${encodeURIComponent(clean)}&status=any&fields=id,order_number,name,financial_status,total_price,fulfillments,note_attributes`,
      token, env
    );
    if (d.orders?.length) return d.orders[0];
    const num = clean.replace(/[^0-9]/g, '');
    if (num) {
      const d2 = await shopifyFetch(
        `/orders.json?name=${encodeURIComponent('#'+num)}&status=any&fields=id,order_number,name,financial_status,total_price,fulfillments,note_attributes`,
        token, env
      );
      if (d2.orders?.length) return d2.orders[0];
    }
  } catch (e) { console.error('findOrderByRef:', e.message); }
  return null;
}

async function findOrderByTracking(trackingNumber, token, env) {
  try {
    const d = await shopifyFetch(
      `/orders.json?status=any&fulfillment_status=fulfilled&limit=250&fields=id,order_number,name,financial_status,total_price,fulfillments,note_attributes`,
      token, env
    );
    for (const o of (d.orders || []))
      if (getTrackingNumber(o) === String(trackingNumber)) return o;
  } catch (e) { console.error('findOrderByTracking:', e.message); }
  return null;
}

async function markOrderPaid(orderId, amount, trackingNumber, orderRef, token, env) {
  const now = new Date().toLocaleString('en-PK', { timeZone: 'Asia/Karachi' });
  await shopifyFetch(`/orders/${orderId}/transactions.json`, token, env, {
    method: 'POST',
    body: JSON.stringify({
      transaction: {
        kind: 'capture', status: 'success', amount,
        gateway: 'cash on delivery', source: 'external',
        message: `COD collected — PostEx Delivered | Tracking: ${trackingNumber} | Ref: ${orderRef}`
      }
    })
  });
  await addOrderNote(orderId,
    `✅ Delivered & marked paid via PostEx Sync\nTracking: ${trackingNumber}\nRef: ${orderRef}\nUpdated: ${now}\nSource: Automated sync`,
    token, env);
}

async function addOrderNote(orderId, note, token, env) {
  try {
    const d        = await shopifyFetch(`/orders/${orderId}.json?fields=note`, token, env);
    const existing = d.order?.note || '';
    await shopifyFetch(`/orders/${orderId}.json`, token, env, {
      method: 'PUT',
      body: JSON.stringify({
        order: { id: orderId, note: existing ? `${existing}\n\n---\n${note}` : note }
      })
    });
  } catch (e) { console.error('addOrderNote:', e.message); }
}

// ─── PostEx API ───────────────────────────────────────────────────────────────

async function trackSinglePostEx(trackingNumber, postexToken) {
  const res = await fetch(
    `${POSTEX_BASE}/track-order/${encodeURIComponent(trackingNumber)}`,
    { headers: { 'token': postexToken, 'Content-Type': 'application/json' } }
  );
  if (!res.ok) throw new Error(`PostEx ${res.status}`);
  const data = await res.json();
  if (data.statusCode === '404' || data.statusMessage === 'RECORD NOT FOUND')
    throw new Error('RECORD NOT FOUND');
  if (data.statusCode !== '200') throw new Error(`PostEx: ${data.statusMessage}`);
  return data.dist || {};
}

// ─── Utils ────────────────────────────────────────────────────────────────────

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
