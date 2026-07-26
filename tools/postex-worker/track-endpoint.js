/**
 * PUBLIC TRACKING ENDPOINT — add to `kordovan-postex-sync`
 * ============================================================================
 * Adds GET /track?cn=<trackingNumber> so the storefront Track Your Order page
 * can show live PostEx status in a modal, without shipping the PostEx token to
 * the browser.
 *
 * ⚠️ SECURITY — READ BEFORE EDITING ⚠️
 * This endpoint is PUBLIC and keyed only by a tracking number. PostEx tracking
 * numbers are guessable/sequential, so anyone can enumerate them. The PostEx
 * `dist` payload contains customer PII (name, phone, delivery address) and the
 * COD amount. Returning it raw would be a customer-data breach.
 *
 * Therefore: NEVER `return Response.json(dist)`. Only the explicit allowlist in
 * sanitiseTrack() may leave this Worker. If you add a field, ask first whether
 * a stranger holding a guessed number should be able to see it.
 * ============================================================================
 *
 * INSTALL — paste these three functions into worker.js, then add the two routes
 * shown in ROUTES below into the existing fetch() handler, above the final 404.
 */

// ─── ROUTES (add inside fetch(), before the trailing 404 return) ─────────────
//
//    if (url.pathname === '/track') {
//      return handlePublicTrack(request, env, ctx);
//    }
//
//    // One-off: shows only the KEY NAMES PostEx returns, never the values, so
//    // the allowlist below can be verified against reality without leaking data.
//    if (url.pathname === '/track-debug') {
//      if (request.headers.get('X-Sync-Secret') !== env.SYNC_SECRET)
//        return Response.json({ error: 'Unauthorized' }, { status: 401 });
//      const cn = new URL(request.url).searchParams.get('cn');
//      try {
//        const dist = await trackSinglePostEx(cn, env.POSTEX_TOKEN);
//        return Response.json({ keys: Object.keys(dist) });
//      } catch (e) { return Response.json({ error: e.message }, { status: 404 }); }
//    }
//
// ─────────────────────────────────────────────────────────────────────────────

const TRACK_ALLOWED_ORIGINS = [
  'https://kordovanleather.com',
  'https://www.kordovanleather.com',
];

async function handlePublicTrack(request, env, ctx) {
  const url    = new URL(request.url);
  const origin = request.headers.get('Origin') || '';
  const allow  = TRACK_ALLOWED_ORIGINS.includes(origin) ? origin : TRACK_ALLOWED_ORIGINS[0];

  const headers = {
    'Access-Control-Allow-Origin': allow,
    'Content-Type': 'application/json',
    'Cache-Control': 'public, max-age=60',
  };

  // Reject anything that is not a plausible tracking number before spending a
  // PostEx call on it. Also blocks path/param injection.
  const cn = (url.searchParams.get('cn') || '').trim();
  if (!/^[A-Za-z0-9-]{6,30}$/.test(cn)) {
    return Response.json(
      { ok: false, error: 'invalid_number', message: 'That does not look like a tracking number.' },
      { status: 400, headers }
    );
  }

  // Edge cache: repeated lookups of the same number (customer refreshing, or an
  // enumeration attempt) cost PostEx nothing and return instantly.
  const cacheKey = new Request(`https://track.internal/${cn}`, { method: 'GET' });
  const cache    = caches.default;
  const hit      = await cache.match(cacheKey);
  if (hit) {
    const body = await hit.json();
    return Response.json(body, { headers });
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
          : "Tracking is temporarily unavailable. Please try again shortly, or message us on WhatsApp.",
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
 * Allowlist. Everything not named here is dropped.
 * Deliberately EXCLUDED — do not add:
 *   customerName / customerPhone / consigneeName / phone  → PII
 *   deliveryAddress / address                             → PII
 *   invoicePayment / codAmount                            → reveals order value
 *   orderRefNumber                                        → maps to a Shopify order
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
