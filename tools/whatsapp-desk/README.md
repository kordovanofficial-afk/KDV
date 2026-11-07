# Kordovan WhatsApp Front Desk (Cloudflare Worker, free)

It answers the team WhatsApp number (+1 202-474-5597, Kapso) instantly, with zero Claude credits:

| Message from the team | What happens |
|---|---|
| `STORE SALES 08-Nov` + one item per line (`Mocha Mate x1`, `KODO Black x2`) | Each line is subtracted from Shopify stock and the result is replied. Unclear lines are asked back, never guessed. |
| `STOCK mocha` | Reply with the current website stock for matching products. |
| anything else | "Got it, I'll reply by 11:30 PM" (once per 2h); saved for Claude's nightly run. |
| anyone NOT on the allowlist | One polite redirect per day to the public order line 0333 2601161. Nothing is changed. |

Claude reads the day's activity at 23:30 PKT from the Kapso message history (and `GET /day` with header `X-Desk-Secret`).

Endpoints: `GET /health` · `GET /selftest` (yes/no checks only) · `GET /day?d=YYYY-MM-DD` (needs `X-Desk-Secret`) · `POST /webhook` (Kapso, HMAC-signed).

## Settings (Cloudflare → worker → Settings)
- Bindings: KV namespace `DESK_KV`.
- Variables (text): `SHOPIFY_STORE=kordovan.myshopify.com` · `PHONE_NUMBER_ID=1352393681300763` ·
  `ALLOWLIST=923005555968,923002042352,923042528729` · `LOCATION_ID=gid://shopify/Location/36710940861`.
- Secrets: `KAPSO_API_KEY` · `WEBHOOK_SECRET` · `DESK_SECRET` · `SHOPIFY_CLIENT_ID` + `SHOPIFY_CLIENT_SECRET`
  (same Shopify app as the PostEx worker; it needs `write_inventory` + `read_products`). `SHOPIFY_TOKEN` also works.

Deploying is manual: paste `worker.js` into the Cloudflare editor, then click **Deploy**. Verify with `/health` (version) and `/selftest`.
Tested locally against the real catalogue with mocked Shopify/Kapso: sales parsing, variant tie-break
(`KODO Black` ≠ `Black Gold`), ambiguous lines asked back, stranger redirect once a day, signature reject, dedupe.
