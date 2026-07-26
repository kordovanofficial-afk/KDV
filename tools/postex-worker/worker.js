/**
 * KORDOVAN × POSTEX SYNC WORKER v5.0
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

// Storefront origins allowed to call the public /track endpoint.
const TRACK_ALLOWED_ORIGINS = [
  'https://kordovanleather.com',
  'https://www.kordovanleather.com',
];

// ─── Entry Point ──────────────────────────────────────────────────────────────

export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil(runPollSync(env));
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
          } catch (e) {
            log(`Order #${o.order_number} mark paid ERROR: ${e.message}`);
            result.errors++;
          }
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
    `/orders.json?status=any&financial_status=pending&fulfillment_status=fulfilled&limit=250&fields=id,order_number,name,financial_status,total_price,payment_gateway,fulfillments,note_attributes`,
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
