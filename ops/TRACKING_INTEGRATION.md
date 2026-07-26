# Order tracking — current state & the PostEx plan

## Live now (Jul 26 2026)
- Shopify page **Track Your Order**, handle `track-order` (id 163952820464), published.
- Bespoke template `snippets/track-order.liquid`, dispatched by handle in
  `sections/main-page.liquid`. Styling `.kv-track` in `home.css`.
- Footer "Track Your Order" now points at `/pages/track-order`. It previously
  pointed at `routes.account_url`, which bounced logged-out visitors into
  Shopify's login flow — that was the "page keeps loading" bug.

## Configure before this is fully useful
Theme editor → **Theme settings → Order tracking**:
- `courier_name` (default "PostEx")
- `courier_tracking_url` — paste PostEx's PUBLIC tracking URL with `{number}`
  where the tracking number goes, e.g. `https://…/track?cn={number}`.

⚠️ The exact PostEx URL was deliberately NOT hardcoded. Guessing it would ship a
broken link to customers. Until it is set, the form hands off to WhatsApp with
the tracking number pre-filled — a working path, and the channel most Pakistani
customers use anyway.

## Phase 2 — status rendered inline (the user's actual ask)
Goal: customer types a number, our page shows the status, without leaving the site.

FREE stack, mirroring `tools/gsc-mcp-worker/`:
1. **Cloudflare Worker** (free tier) holding the PostEx API token as a secret.
   The token must never reach the browser, so a proxy is mandatory — the theme
   cannot call PostEx directly.
2. Worker exposes `GET /track?cn=<number>` → normalises PostEx's response to
   `{status, updatedAt, city, history[]}`.
3. Restrict by `Origin: https://kordovanleather.com` and rate-limit per IP;
   an open proxy over a courier API is an abuse vector.
4. `snippets/track-order.liquid` swaps `window.open` for a `fetch` to the Worker
   and renders a status timeline. The status table already on the page is the
   intended visual vocabulary.

**Blocked on the user providing:** PostEx API base URL, auth header format, and
a token. Their merchant portal → API//Developer section has these.

## Note on Shopify's own tracking
Shopify order-status URLs are per-order and tokenised, so they cannot be looked
up from a number alone — a courier lookup is the only way to serve guests, and
~all our orders are guest COD.
