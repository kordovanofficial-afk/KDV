# Operations: PostEx Worker, email, customers, COD fee, shipping threshold, tooling

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

## 🛡 Security + browser tooling (Oct 26 2026)
- **Playwright CLI 1.56.1 + Chromium are pre-installed** — never `playwright install`. ⚠️ It can only reach
  hosts in the environment's network allowlist; `kordovanleather.com` is NOT on it (Oct 26: CONNECT 403), so
  live-site checks need the user to add `kordovanleather.com` (+ `kordovan-official.workers.dev` hosts) under
  Network access → Allowed domains.
- Install cards offered: **claude-security** (deep code scan + verified patches), **Security Guidance**
  (edit/commit-time review hooks), **playwright** MCP. Use claude-security / the built-in `security-review`
  skill on the theme, `tools/postex-worker/worker.js` and `tools/gsc-mcp-worker/` before any deploy.
- 🚫 **OpenSEO (every-app/open-seo) NOT installed:** the software is free/MIT, but every data call runs on a
  paid DataForSEO key — violates the FREE-only rule. Our free stack: GSC Worker + vendored SEO skills + Apify free tier.

## 🔌 Available integrations (MCP)
Shopify, GitHub, Canva, Figma, Facebook Ads, Higgsfield, Cloudflare.
(Playwright is NOT available in this remote env — design is done in code, then
pushed to the draft theme to preview in a browser.)
- **Kordovan GSC (custom connector, FREE, LIVE-ish):** self-hosted Cloudflare Worker
  MCP server in `tools/gsc-mcp-worker/` gives read access to Google Search Console.
  Worker URL `kdv-seo-mcp.kordovan-official.workers.dev`, connector path `/mcp/<MCP_SECRET>`.
  Tools: `gsc_list_sites`, `gsc_query`, `gsc_list_sitemaps`, `gsc_inspect_url`.
  Service acct = **`kdv-gsc@kordovan-seo.iam.gserviceaccount.com`** (fresh SA,
  Jul 15 2026; old `kdv-seo-reader@…` is a dead ghost — never reuse it). Key
  rotated; old keys deleted.
  **STATUS Jul 15 2026 — ✅ FULLY LIVE, DATA FLOWING.** Root cause of the 3-day
  `invalid_grant "account not found"`: the `GOOGLE_SA_EMAIL` var sat in a SAVED-
  BUT-NEVER-DEPLOYED config version (Cloudflare Settings page shows latest saved
  config, while traffic serves the last DEPLOYED version — editing vars without
  hitting Deploy does nothing; deploying from the code editor carries the OLD
  bindings too). Fixed by delete+re-add of the var to force the deploy flow.
  Worker now has a **`gsc_debug` tool + `?debug` GET param** (safe diagnostics:
  env binding names, email as-stored, key shape, live token test — never leaks
  secrets). Use it FIRST whenever the connector misbehaves.
  ⚠️ **Property gotcha:** SA has access to the URL-prefix property
  `https://kordovanleather.com/` (siteFullUser), NOT `sc-domain:…` — pass
  `siteUrl: "https://kordovanleather.com/"` on every `gsc_query` (env `GSC_SITE`
  still says `sc-domain:…`; either update the var in Cloudflare or keep
  overriding). First data pull done (28d): brand queries dominate (pos ~1),
  top money page = /collections/mens-leather-wallets (833 clicks, pos 10.2 =
  page 2 — big headroom), cowboy-hats niche strong (CTR 13.8%, pos 4.8),
  jackets high-impressions/low-CTR. Bing/GA4 can be added to the same Worker later.

## 📦 PostEx / COD automation (Cloudflare Worker)
- **`kordovan-postex-sync`** — host `kordovan-postex-sync.kordovan-official.workers.dev`
  (workers.dev route enabled + Public; no custom domain). Hourly cron + PostEx
  webhook: marks Delivered COD orders **paid** in Shopify, notes RTOs. Holds
  `POSTEX_TOKEN`, `SHOPIFY_*`, `SYNC_KV`, `SYNC_SECRET`.
- PostEx API: `https://api.postex.pk/services/integration/api/order/v1`,
  `GET /track-order/{cn}`, auth header **`token:`**, status in `dist.transactionStatus`.
- **v5.0 (Jul 26 2026)** adds public `GET /track?cn=` for the storefront Track
  Your Order page. ⚠️ It is a strict ALLOWLIST (status/city/timestamps only) —
  never a passthrough: `dist` carries customer name, phone, address and COD
  amount, and tracking numbers are guessable. See `ops/TRACKING_INTEGRATION.md`.
- ⚠️ The Worker ROOT url returns `{"error":"Not found"}` by design. The
  dashboard "Visit" button opens root, so it always looks broken. Use `/health`.
- 💬 **WhatsApp copy is PAYMENT-AWARE as of Sep 4 2026** (`isPrepaid(o)` =
  `financial_status` set and !== `'pending'`). Before this, the order-placed hook
  **silently dropped every prepaid order** (`skipped_not_cod`), so card/JazzCash
  buyers — i.e. ALL jackets and ALL footwear since the MTO change — got no
  WhatsApp at all. They now get their own message: "Paid in full … nothing to pay
  on delivery" + the workshop expectation, and **no CONFIRM ask** (there
  is nothing to confirm, and prompting invites a cancellation on money in hand).
  Prepaid orders also skip the `wapend:` KV write, so they can never be chased for
  a CONFIRM they were never asked for. COD copy is unchanged.
- ✅ **FIXED Sep 5 2026 — `runPrepaidDeliveryPass()`, the notify-only twin of the COD
  sweep.** Prepaid orders used to get no delivered message and no review ask, because
  `msgDelivered` + `rvSchedule` live inside `runPollSync`, which only sees
  `financial_status=pending` non-card orders. The review engine therefore could not
  ask a single jacket buyer. Runs hourly right after `runPollSync`; also on demand at
  **`/prepaid-sync`** (needs `X-Sync-Secret`). Last result → KV `last_prepaid_sync`.
  Design rules, do not break them:
  - **NEVER calls `markOrderPaid`** — the money is already in.
  - **NEVER writes RTO notes** — `runPollSync` owns returns, so an RTO is recorded once.
  - 🔴 **First-run baseline via KV `ppass:init`.** On the very first execution it burns
    `wasent:` + `rvdone:` on everything ALREADY delivered and sends NOTHING. Without
    this, switching it on cold would blast a month of customers who got their order
    weeks ago — the failure mode that gets a WhatsApp number blocked. **If you ever
    need to re-seed, delete `ppass:init`; never delete it casually.**
  - `PP_WINDOW_DAYS = 30`, deliberately ≤ the 30-day `wasent:` TTL so an order ages out
    of the window before its dedup marker expires (otherwise it gets thanked twice).
  - Skips `rvSchedule` when `rvdue:` already exists — `rvSchedule` OVERWRITES `rvdue:`,
    so calling it on an order the COD sweep just scheduled would push the 3-day review
    timer back an hour every hour and the ask would never fire.
  - No gateway filter on purpose: a COD order already marked paid matches too, but its
    refs are burned so it is a no-op — and it acts as a safety net if the COD sweep
    missed one. `msgDelivered` is payment-neutral, so it is correct either way.
  - Verified by running the real function against mocked Shopify/PostEx/KV: cold run
    seeds 2 and sends 0 · next run messages ONLY the new orders and schedules 1 review
    · third run is a full no-op · `markOrderPaid` called 0 times.
- 🟡 **KNOWN DRIFT (user decision Sep 6 2026) — the LIVE Worker still says "4–7 working
  days". The repo copy says "about 3 weeks". Do NOT treat this as a bug to fix on sight.**
  The user declined the redeploy: *"no need for the whatsapp edit as its purely for the
  high season... so it wont be an issue... as only 1 in 10 will be effected by it."*
  Volume-wise that is right — MTO is roughly 10% of orders. ⚠️ But note the exposure is
  **concentrated, not diluted**: the prepaid message fires on 100% of jacket and footwear
  buyers, i.e. the people who paid PKR 22,000–35,000 in full with nothing in hand. They
  are the likeliest to dispute if week two passes in silence. Raised once, user decided,
  do not re-litigate.
  ➡️ **The repo is already correct**, so the drift closes automatically the next time the
  Worker is deployed for any reason. Mention it then; do not deploy just for this.
- ✅ **DEPLOYED Sep 5 2026.** Verified by diffing `workers_get_worker_code` against the
  repo file: identical apart from Cloudflare's multipart envelope, `isPrepaid` present
  at line 927, and `skipped_not_cod` gone from the live script.
  💡 `workers_get_worker_code` is the way to confirm ANY Worker deploy — it exceeds the
  token cap so it auto-saves to a file, which you then `diff` against the repo copy.
- ⚠️ Deploying the Worker is MANUAL: paste `tools/postex-worker/worker.js` whole
  into the Cloudflare editor, then **Deploy**. A git push does NOT ship it.
  ⚠️ `/health` returns only `{status, ts}` — no version marker, so it CANNOT confirm a
  deploy. Consider adding one if this gets deployed often.
- Full source of truth for the Worker: `tools/postex-worker/worker.js` (paste
  whole file into the Cloudflare editor, then **Deploy** — saving ≠ deploying).

## 📧 ACTIVE — Hosting/email cost migration (backend cleanup before SEO)
Goal: kill TMDHosting "Starter" Linux hosting ($180/yr, renews in ~9 mo from Jul 2026)
→ total ~$20/yr. Site is 100% on Shopify; hosting only serves DNS + cPanel email.
- Domain .com at TMD $19.99/yr — **renews ~Aug 2026, RENEW IT** (transfer to
  Cloudflare Registrar ~$10/yr only NEXT year, never near expiry).
- **DECIDED (user-confirmed): Zoho Mail Forever Free, webmail + Zoho app only**
  (user accepts no IMAP → Thunderbird demoted to local ARCHIVE of old mail).
  5 seats: `admin@`, `asadj@`, `umair@`, `contact@`, `corporate@`.
  Aliases: `sales@` + `daraz@` → admin ONLY. User DELETED `customercare.usa@`,
  `shahid.butt@us.`, `marketing@`, `social@` (verified unused: not on site/
  Shopify/customers; socials are under user's personal Meta email). `kordovan`
  system catch-all — emptied (pure spam); NO catch-all in Zoho.
- **Guide = `docs/email/EMAIL_MIGRATION.html`** (baby-steps, 8 phases + troubleshooting,
  delivered). User executing solo; reports back after the Phase 6 test checklist.
  Catch-all mailbox already emptied (was pure spam).
- **STATUS Jul 4 2026 — MIGRATION EXECUTED ✅:** Zoho org live (5 users + sales@/
  daraz@ aliases on admin, all green: MX/SPF/DKIM verified). DNS moved to
  Cloudflare Free (nameservers brady/lucy.ns.cloudflare.com set at TMD). Final
  CF zone = 15 records, ALL grey-cloud/DNS-only: A@→23.227.38.65, CNAME www/
  account→shops.myshopify.com, 4× Shopify email CNAMEs (s9k/s9k2/s9k3._domainkey
  →dkim1-3.e2b7bcdd21fe.p531.email.myshopify.com + mailers9k), 3× Zoho MX,
  TXT: zoho SPF, zmail._domainkey DKIM, _dmarc (p=none+rua), zoho-verification,
  facebook-domain-verification (Meta ads — NEVER delete). Klaviyo NS+TXT deleted
  (user confirmed unused). Old mail archived in Thunderbird Local Folders.
  User tested all 7 addresses — working. **PENDING:** (1) observation window →
  ~Jul 18: disable TMD Starter auto-renew (hosting only, NOT domain!);
  (2) domain renewal ~Aug 2026 $19.99 — PAY IT; (3) optional: SPF/DKIM/DMARC
  "show original" check + COD test-order email check.
- **Site emails:** gmail address PURGED from theme (commit ff8aeb3) — public
  contact = `contact@kordovanleather.com` (footer + story/care/shipping/returns
  snippets); `admin@` remains in Shopify PAGE content (FAQs/Contact/Corporate/
  policies) + store sender. Optional pending: Corporate page quote email →
  `corporate@` (live page content — needs explicit OK).

## 🧹 DONE — Customer-base cleanup (Jul 5 2026, pre-SEO backend hygiene)
From 27,193 → ~26,000 profiles. Executed via Shopify MCP GraphQL (user granted
approval; `customerDelete` works, `customerMerge` BLOCKED — connector token
lacks `write_customer_merge` scope, no workaround; direct API egress blocked).
- Alias/duplicate analysis from customer CSV export (scratchpad, session-local):
  892 clusters → 185 zero-order duplicates API-deleted · 23 priority merges
  (dup ≥2 orders) done MANUALLY by user in admin (Spring '26 has native
  "Mergeable" column + Merge button) · 446 one-order-dup merges + 86
  consent-hold merges SKIPPED as cosmetic (list = manual_merge_list.csv,
  delivered) · 6 junk test profiles deleted (placeholder phones 0300-0000000/
  1234567, "Test/Abc Def" names); 9 junk-with-orders remain (undeletable).
- BIG PURGE: 985 deleted (zero orders + no email/SMS/WhatsApp consent + no
  tags/notes + created ≤Dec 26 2025 via ID↔date probing; 520 recent spared;
  2 refused by API order-guard). Audit logs delivered to user.
- **SERIAL COD REFUSERS tagged (Jul 7 2026):** bulk-exported ALL 5,203 cancelled
  orders (bulkOperationRunQuery → storage.googleapis.com URL IS fetchable through
  proxy; cdn.shopify.com is NOT). Refuser = 2+ cancels with reason CUSTOMER/FRAUD/
  OTHER (excluded INVENTORY/STAFF/DECLINED = our-side). 425 serial refusers found;
  **API-tagged `FRAUD RISK` on 323** (the "never completed a single order" set),
  9 batches of tagsAdd, zero errors. Skipped 4 internal/team (Asad Janjua/Umair
  Khan/biz phone 3332601161·3009120000) + 71 MEDIUM (2 cancels but did complete) +
  27 other HIGH (3+ cancels but completed ≥1 — OFFERED to tag, user hasn't said yes).
  `customerDelete` CANNOT remove them (Shopify blocks delete of any customer with
  orders, incl. cancelled). List = serial_cod_refusers.csv (delivered).
- **Shopify Flow LIVE (user built, on):** Order created → IF customer tags Includes
  "FRAUD RISK" → Add order tag `⛔ FRAUD RISK`. Auto-flags every new order from a
  refuser at top of order. (Order tags are grey chips, not red text — Shopify has no
  native tag colouring w/o a paid app; ⛔ emoji is the visibility hack.)
- **OPEN:** 56 REVIEW clusters (different names sharing phone/address — family
  vs COD-refuser) await user's CANCELLED-ORDERS export → then tag via API (tags
  work). User's own profiles: business phone 3332601161 cluster.

## ✅ FREE-SHIPPING THRESHOLD UNIFIED AT PKR 5,500 (Sep 8 2026 — deployed live, done)
The cart PAGE contradicted every other surface: it promised free delivery at PKR 3,000 while
the drawer, header, trust bar, PDP, shipping page and JSON-LD all said 5,500. A customer could
be told two different numbers in one session, and the cart page is the last thing they read.
- ✅ `sections/main-cart.liquid:75,77,79` — `300000` → **`550000`** (threshold test, the
  "add X more" figure, and the progress-bar width divisor; all three must move together).
- ✅ `sections/announcement-bar.liquid:39,48` — schema default + preset text → **PKR 5,500**.
- 📌 **`assets/theme.js` `renderShip()` was ALREADY correct at `550000`.** An older note in this
  file claimed 250000 (PKR 2,500) for the cart drawer — that was **stale and is now corrected**.
  Do not "fix" the drawer; it is right. ⚠️ Lesson: re-grep before trusting a threshold recorded here.
- ✍️ **The threshold now lives in exactly 2 code places**: `theme.js:550` (drawer) and
  `main-cart.liquid` (cart page), plus `pdp-jsonld.liquid:19` (`jl_free_ship_min = 550000`) for
  structured data. **Change all three together** or the site disagrees with itself again.
- 🔎 Verified after the edit: **0 occurrences** of `300000`/`250000`/"PKR 3,000"/"PKR 2,500"
  remain anywhere in `assets/ sections/ snippets/ layout/ templates/ config/`.
- ⚠️ The announcement bar values are **schema defaults/presets**, so a bar already configured in
  the theme editor keeps its saved text — the editor's stored setting wins over the default.
  **Check Theme editor → Announcement Bar and retype it if it still shows 3,000.**

## 💳 PREPAID INCENTIVE = A COD FEE AT THE SHIPPING STEP (LIVE Sep 15 2026, user-approved)
User wanted *"auto discount when someone used online payment"*. 🔴 **THAT IS IMPOSSIBLE IN SHOPIFY
ON ANY PLAN — do not go looking for a way.** The order total must be final before the payment is
authorised, and payment method is chosen last, so no discount (code, automatic, or Function) can
react to it. Every "COD fee" app on the app store works around this the same way we now do: at the
**shipping step**, which the customer chooses BEFORE payment.
- ✅ **LIVE on the default delivery profile, Domestic zone. COD costs exactly PKR 250 more in both
  price bands** (user set the fee: *"yes the fee is 250"*):
  | Cart | Pay online | Cash on delivery |
  | Under 5,500 | `Standard Delivery — Pay Online` **250** | `Cash on Delivery` **500** |
  | 5,500+ | `Free Delivery — Pay Online` **0** | `Cash on Delivery` **250** |
  `EXPRESS NEXT DAY DELIVERY (KARACHI ONLY)` 1,000 — untouched, no conditions.
  ⚠️ **COD orders over 5,500 therefore LOSE free delivery.** Deliberate — otherwise the incentive
  vanishes exactly on the highest-value carts. Reverse by setting that rate to 0 if the user objects.
- 🔑 **IDs for any future edit** (re-read them, do not trust this list blindly):
  profile `48076685501` · locationGroup `48194551997` · zone `103282671805` (Domestic).
  Mutation shape: `deliveryProfileUpdate(id, profile:{locationGroupsToUpdate:[{id, zonesToUpdate:
  [{id, methodDefinitionsToCreate | methodDefinitionsToUpdate}]}]})`. Conditions go in
  **`priceConditionsToCreate`** (`{operator, criteria:{amount,currencyCode}}`), NOT `conditionsToCreate`.
- ✍️ **Why a FLAT FEE beats a percentage, and why 10% was wrong.** COD's real cost is roughly fixed
  in rupees (return shipping + the courier's COD handling), so a flat 250 tracks it almost exactly.
  A percentage overpays wildly at the top: 10% of a 28,000 jacket is 2,800 to change a behaviour
  that costs the same 250 as a wallet does. Measured cost of COD ≈ **2.5–3.5% of cart**; the old
  `PAYONLINE10` at 10% was ~3x that.
- ✅ **It costs NOTHING on the 54 made-to-order products** — they already cannot be paid COD, so
  those buyers only ever see the prepaid rate. The "don't waste the discount on MTO" problem solves
  itself; no collection scoping needed.
- ✅ **No code means nothing to leak.** This is the whole `ASAD90` class of problem designed out.
- 🔴 **TWO GAPS STILL OPEN — neither is fixed, do not assume they are:**
  1. **A customer can pick a prepaid rate and still choose COD at payment.** Nothing enforces the
     pairing. Cheapest fix uses infrastructure that already exists: the PostEx Worker sees every
     order's `financial_status` and shipping line, so a mismatch is trivially detectable and its
     WhatsApp message can carry a payment link instead of a COD confirmation. The clean fix is a
     payment-customization Function change, but **it is UNVERIFIED whether that Function's input
     can read the SELECTED delivery option** — test before promising it.
  2. **An MTO cart still SHOWS the COD shipping rate**, then COD is absent at payment — a potential
     dead end on the highest-value products right before jacket season. Mitigated only by the rate
     description ("Not available on made-to-order pieces, which are prepaid only"). **The real fix
     is a delivery-customization Function hiding the COD rate when the cart has an MTO line.**
- 📌 `PAYONLINE10` (10%, all products, uncapped, no expiry) is **still ACTIVE with 0 redemptions in
  2 months**. It is now redundant and should be retired — not yet done, user has not been asked.
- 🔴 **DISCOUNT-CODE SPRAWL — audited Sep 9, mostly NOT cleaned up.** 16 active codes, only ONE with
  an expiry date. Four had no per-customer limit. **`ASAD90` — 90% off everything, uncapped, no
  expiry, already used once — the user REMOVED it Sep 15 (verified: `codeDiscountNodeByCode` returns
  null).** Still live and uncapped-ish: `BDAY25` 25% · `USM25` 25% · `KORDOVAN20` 20% ·
  `UMAIR109` 20% (no per-customer cap) · `WCM10` 10% (185 uses) · `WELCOME10` 10% — and WELCOME10 is
  **the only code that combines with order + product + shipping discounts**, a landmine under any
  future sale. User chose "audit and report first"; the report was delivered, the cleanup was not
  actioned. ⚠️ Raise it before running any promotion.

