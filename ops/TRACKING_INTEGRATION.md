# Order tracking — live PostEx status on the storefront

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

## Deploy steps (user)
1. Cloudflare → Workers → `kordovan-postex-sync` → **Edit code**.
2. Paste the three functions from `tools/postex-worker/track-endpoint.js`, and add
   the two routes (commented at the top of that file) into `fetch()` above the
   final 404.
3. **Click Deploy.** ⚠️ Saving is not deploying — this exact trap cost 3 days on
   the GSC worker (see CLAUDE.md). Traffic serves the last *deployed* version.
4. Verify: `curl "https://<worker-host>/track?cn=<a real tracking number>"`
   → should return `{ok:true,status:...}` and **no** name/phone/address.
5. Shopify → Theme settings → **Order tracking** → set
   **Live tracking API** to `https://<worker-host>/track`.

Optional one-off: `/track-debug?cn=…` with the `X-Sync-Secret` header returns
only the *key names* PostEx sends (never values), so the allowlist can be checked
against the real payload safely. Remove the route afterwards.

## Fallback order in the theme
1. `tracking_api_url` set → live status modal
2. else `courier_tracking_url` → opens courier page in a new tab
3. else → WhatsApp with the tracking number pre-filled
