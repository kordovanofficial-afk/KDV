# Order tracking — live PostEx status on the storefront

## Confirmed URLs (verified in the Cloudflare dashboard, Jul 26 2026)
Worker host: **`kordovan-postex-sync.kordovan-official.workers.dev`**
(workers.dev route ENABLED, visibility Public, no custom domains.)

- Health:    `https://kordovan-postex-sync.kordovan-official.workers.dev/health`
- Tracking:  `https://kordovan-postex-sync.kordovan-official.workers.dev/track`
- Theme setting *Live tracking API* takes the **/track** URL above.

⚠️ The ROOT url returns `{"error":"Not found"}` — that is correct, not a fault.
The dashboard's blue **Visit** button opens the root, so it always looks broken.
Only /health, /track, /track-debug, /webhook/postex, /sync and /stats respond.

## What exists already
`kordovan-postex-sync` (Cloudflare Worker, created Jun 26 2026) polls PostEx
hourly + takes webhooks, marks Delivered COD orders as **paid** in Shopify, and
notes RTOs. **It already holds `POSTEX_TOKEN`**, so no new credential is needed.

Confirmed PostEx contract, read from that Worker's source:
- Base: `https://api.postex.pk/services/integration/api/order/v1`
- `GET /track-order/{trackingNumber}`, auth header **`token: <POSTEX_TOKEN>`**
- Returns `{ statusCode, statusMessage, dist: {...} }`; `dist.transactionStatus`
  carries the status. `statusCode '404'` / `RECORD NOT FOUND` for unknown numbers.

## What was added (Jul 26 2026)
- `tools/postex-worker/track-endpoint.js` — a **public** `GET /track?cn=` endpoint
  to paste into the existing Worker.
- `snippets/track-order.liquid` — fetches it and renders a status modal with a
  timeline. Falls back to the courier URL, then WhatsApp, so it is never a dead end.

## 🔴 Security — the reason this is not a passthrough
The endpoint is public and keyed only by a tracking number, and PostEx numbers
are guessable. `dist` contains **customer name, phone, delivery address and the
COD amount**. Returning it raw would let anyone enumerate numbers and harvest the
customer base — worse than any bug on the site.

So `sanitiseTrack()` is a strict **allowlist**: only `status`, `city`,
`updatedAt` and a status/timestamp `history` are emitted. Never add a field
without asking whether a stranger holding a guessed number should see it.
Also in place: origin restricted to kordovanleather.com, tracking-number format
validation before any upstream call, and a 120s edge cache so repeat/enumeration
hits cost PostEx nothing.

⚠️ **Still recommended:** add a Cloudflare **Rate Limiting** rule on `/track`
(e.g. 20 req/min per IP). The free tier includes one rule. The edge cache blunts
repeats but does not stop a wide sweep across many distinct numbers.

## Deploy steps — copy the WHOLE file, nothing to merge
`tools/postex-worker/worker.js` is the **complete** Worker: the existing v4 sync
plus the new endpoints. Nothing has to be pasted "in the right place".

1. Cloudflare → Workers & Pages → **kordovan-postex-sync** → **Edit code**.
2. Click in the code area, **Ctrl+A** (select all), **Delete**.
3. Paste the entire contents of `tools/postex-worker/worker.js`.
4. Click **Deploy** (top right).
   ⚠️ **Saving is NOT deploying.** Traffic serves the last *deployed* version.
   This exact trap cost 3 days on the GSC worker — see CLAUDE.md.
5. Nothing else changes: no new variables, no new secrets. It reuses the
   POSTEX_TOKEN, SHOPIFY_* and SYNC_KV bindings already on the Worker.
6. Check it still works: open `https://<worker-host>/health` → `{"status":"ok"}`.
7. Then Shopify → Online Store → Themes → Customize → **Theme settings →
   Order tracking** → paste `https://<worker-host>/track` into
   **Live tracking API**. Save.

Verify before trusting it: open `https://<worker-host>/track?cn=<a real number>`
in a browser. It must show status/city/history and **no customer name, phone
or address**. If PII appears, unset the theme setting immediately and tell me.

## Fallback order in the theme
1. `tracking_api_url` set → live status modal
2. else `courier_tracking_url` → opens courier page in a new tab
3. else → WhatsApp with the tracking number pre-filled
