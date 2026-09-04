# Kordovan — Project Memory

> 💰 **HARD RULE (user, permanent): FREE options ONLY.** Never recommend or set up
> anything paid — no paid apps, connectors, tools, or subscriptions. Always find the
> zero-cost path (free tiers, native Shopify, export-CSV-and-share, self-hosted/open-source).

Custom Shopify theme for **Kordovan**, a Pakistani full-grain leather brand
(wallets, bags, small leather goods). This file is the persistent context for
every session — read it first.

## 📐 Design source of truth
- **`docs/brand/BRAND_MOODBOARD.md`** — competitor teardown (top 10 global leather
  brands), refined "Quiet Heritage" palette, typography, full UX/SEO rulebook.
  **Always follow this when designing or editing the theme.**
- **`docs/brand/moodboard.html`** — open in a browser to *see* the palette + type specimens.

## 🎨 Active palette — "Quiet Heritage" (Kordovan 2.0)
Refined from the original cognac/gold/off-white/charcoal set (cognac was muddy,
charcoal was too cold for leather):
- Alabaster `#F7F2EA` (bg) · Parchment `#ECE3D4` (surfaces)
- Espresso `#241C16` (text/dark) · Walnut `#4A3528`
- **Cognac `#A0623A`** (primary CTA/links) · Saddle Tan `#C08B5C` (hover) · Antique Brass `#B0894F` (detail)
- Stone `#8B8174` (muted text) · Border `#DDD2C0` · Heritage Olive `#5A5A3C` (sparing accent)
- Fonts: **Fraunces** (headings, replaces Playfair) + **Inter** (body)

> ✅ APPLIED on `kordovan`: `assets/theme.css` `:root` tokens, the
> Fraunces import, hardcoded gradients/shadows, and `config/settings_schema.json`
> defaults are all migrated to Quiet Heritage. Headings = Fraunces 500.

## 🗂 Repo structure & source of truth
**Single source of truth = the `kordovan` branch.** Everything (theme, docs,
tools, ops) lives here — one streamlined trunk for the brand rebuild.
```
kordovan  (trunk)
├── assets/ config/ layout/ locales/     ← THEME — MUST stay at repo root
├── sections/ snippets/ templates/       ←   (Shopify GitHub sync = branch root)
├── docs/
│   ├── brand/   (BRAND_MOODBOARD, DESIGN_SYSTEM, moodboard.html)
│   ├── seo/     (SEO_ARCHITECTURE, SEO_AUDIT_TRACKER)
│   ├── email/   (EMAIL_MIGRATION.html)
│   ├── images/  (IMAGE_BRIEF.md)
│   └── mockups/ (static HTML mockups — mockup-first workflow)
├── .claude/skills/                       ← 7 vendored SEO skills (MIT, see its README;
│                                            use during Phase-2 SEO pass; paid-API steps omitted)
├── tools/gsc-mcp-worker/                 ← FREE GSC connector (Cloudflare Worker)
├── ops/                                  ← agent/session playbooks & working notes
└── CLAUDE.md                             ← this file (read first every session)
```
- ⚠️ **Theme must NOT be nested under `theme/`.** Shopify's GitHub integration
  deploys from the *branch root* only — a `theme/` folder breaks the draft sync.
  Grouping is for everything *around* the theme (docs/tools/ops), never the theme.
- ✅ **MIGRATION DONE (Jul 15 2026):** `shopify-theme-deploy` → `kordovan`.
  `kordovan` is the GitHub **default branch** and Shopify is connected to it via a
  **NEW draft theme `165057069296` "KDV/kordovan"** (the old draft `164277190896`
  was deleted by the user — all references to the old draft ID are obsolete; any
  direct `themeFilesUpsert` pushes now target `165057069296`). Live theme
  `162105917680` untouched. Sole leftover: stale remote branch
  `shopify-theme-deploy` — the session git proxy refuses deletion pushes, so the
  user deletes it once on GitHub (repo → Branches → 🗑). It has no unique commits.
- Theme files live at the **repo root** (NOT under `theme/`): `assets/theme.css` +
  `theme.js`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/`, `templates/`.
- Header/footer sections are named **`site-header.liquid` / `site-footer.liquid`**
  (renamed to avoid a Shopify customizer section-group conflict — do not rename back).
- ⚠️ A second, unrelated theme history exists on `claude/vigilant-euler-h81zbc`
  (a from-scratch rebuild nested under `theme/`, sections named `header`/`footer`).
  It is NOT deployable as-is and is NOT the source of truth. Ignore it unless
  explicitly told otherwise.

## 🐎 Brand logo
- Mark: a **black horse-head silhouette** (registered trademark / copyright —
  brand-owned asset, never reproduce/trace it or use it outside this theme).
- Header (`sections/site-header.liquid`) supports it via the `logo` image_picker
  (upload in theme editor → Header → "Logo (dark mark)"). Because the mark is solid black, CSS
  auto-inverts it to cream on the transparent/dark header — one upload suffices.
  Optional `logo_light` slot exists for a custom cream version.
- Logo sizing: 44px header height, shrinks to 34px on scroll (sticky shrink).
- TODO when the file is provided: also set it as favicon + social share image.

## 🚦 Hard constraints (do not violate)
- ⚠️ **ROLES FLIPPED Jul 25 2026 — `165057069296 "KDV/kordovan"` IS NOW THE LIVE
  `MAIN` THEME.** The user published it (theme record shows role MAIN, updated
  2026-07-25T02:45Z); the old live theme `162105917680` is now UNPUBLISHED and is
  the fallback/rollback copy. The old "never touch 162105917680" rule is obsolete
  — that ID is no longer serving customers.
- 🔴 **Consequence: pushing `kordovan` now deploys STRAIGHT TO THE LIVE STORE.**
  There is no draft buffer any more. Every theme commit is a production release
  during paid-ads spend. Review carefully; prefer a mockup or a duplicate theme
  for anything structural.
- Shopify GitHub integration deploys from the **`kordovan`** branch.
- **Work on `kordovan`** (the source of truth).
- 🛑 **ASK BEFORE EVERY PUSH TO `kordovan` (user, Aug 19 2026 — supersedes the old
  "user authorized per-step deploys" rule).** Each push is a live release while ads
  are running, so confirm every time; a yes on one deploy is NOT standing permission
  for the next. Build on the session's `claude/*` branch, then ask to merge.
- ⚠️ **Sessions are often scoped to a `claude/*` branch while Shopify deploys only
  from `kordovan`** — so work is INVISIBLE on the store until that merge. Say so
  when handing off, or the user checks the site and sees the old version.
- Do not create PRs unless explicitly asked.

## 🧥 Jackets — payment, margin, refusal (user-confirmed Aug 20 2026)
- **Payment = 50% of retail to BOOK, balance paid to the rider on delivery.**
  ⚠️ NOT "prepaid only" — the old rule was wrong and was live on the site. Corrected
  across the 4 jacket collections + the brands article. Never write "no cash on
  delivery" for jackets again; half of it *is* paid at the door.
- **COGS PKR 10,000–12,000** (use 11,000). Mean selling price across the 28 men's
  jackets = **PKR 28,066** → gross profit ~**PKR 17,066/jacket (61%)**. That is
  ~5.7x the best wallet (Aristocrat, 3,005) and ~24x the Bastion (720).
  **Break-even CPA ≈ PKR 15,300.** Cold CPA of ~1,979 returns ~7.7x here — jackets
  are the ONE product that makes cold prospecting viable in this account.
- **No production ceiling** (user, Aug 20 2026) — budget is the only constraint.
- ✅ **Jackets have ZERO doorstep refusals. 0 of 134 orders in 24 months were
  dispatched and then cancelled** (checked via fulfillments + trackingInfo, Aug 20
  2026). Once a jacket ships it is delivered, every time — the 50% deposit filters
  before anything leaves the workshop, so jackets carry **no RTO cost at all**.
  ⚠️ **Never count VOIDED/cancelled as a refusal.** A cancelled order with no
  tracking number was never dispatched. Test = `fulfillments.trackingInfo.number`
  present, or `displayFulfillmentStatus` FULFILLED/RESTOCKED.
- **The real jacket problem is BOOKING conversion, not delivery.** 75 of 134 jacket
  orders were cancelled pre-dispatch: 25 CUSTOMER · 24 OTHER · 22 FRAUD · 2
  INVENTORY · 2 DECLINED — i.e. the deposit was never paid. Only **56 became paid
  (42%)**. Costs nothing in shipping, but it means **Meta's Purchase event (fires at
  order placement) is ~58% noise on jackets** — the same structural trap as the COD
  refuser problem. Feed the PAID/confirmed event back, not order-placed.
- **Break-even CPA ≈ PKR 7,100 per PLACED order** (17,066 × 42%), or ~8,500 ignoring
  the 22 fraud orders; the full **17,066 per PAID jacket**, since nothing ships unpaid.
  Still 3.6–4.3x the PKR 1,979 cold CPA.
- 📌 **Store-wide RTO is 9.9%, not ~40%.** Of 6,482 orders (24m): 4,699 not cancelled,
  1,144 cancelled BEFORE dispatch, **639 cancelled AFTER dispatch = 9.9% real RTO**
  (555 of those tagged FRAUD). The playbook's "~40% never deliver" conflates
  pre-dispatch cancellations with genuine refusals — re-measure before quoting it.
- **Cities (delivered orders, 12m all-products, n=2,512):** Lahore 331 · Karachi 232
  · Islamabad 169 · Rawalpindi 101 — **those four = 84% of 9-city delivered volume**.
  Outside the 9 cities delivery is 49.9% vs 67.9% inside (28.1% for jackets) —
  independent re-validation of the 9-city rule. Karachi has the highest jacket AOV
  (39,316) despite the mildest winter → sell Karachi *style*, sell the north *layering*.
  ⚠️ Jacket-level city data is thin (2–26 orders/city) — direction only, never ranking.
- **Season curve (PK jacket impressions):** Aug 13.6k · Sep 13.6k (FLAT — do not
  spend) · Oct 35k · Nov 78.6k · Dec 78.5k · Jan 46.8k · Feb 11.4k. Ramp in OCTOBER.
- ✅ **The "Aug 2026 is 64% below Aug 2025" alarm was a MEASUREMENT ARTEFACT — diagnosed
  and closed Aug 20 2026. Do not re-raise it.** Daily series (PK jacket impressions):
  June ~430/day @ pos 14.8 · 1–26 Jul ~390/day · **27 Jul–10 Aug ~215/day @ pos 19.0**
  · **11–18 Aug ~300/day @ pos 12.2**. The break is 27 Jul, two days after the new
  theme went live 25 Jul — a recrawl-cycle lag. It is a **theme-migration dip already
  recovering**; last-8-day position (12.2) is BETTER than June (14.8).
  **June 2026 (~430/day) ≈ Aug 2025 (~438/day), so there is no underlying YoY decline.**
  The original alarm came from measuring 1–18 Aug, which straddled the trough.
- 🔬 Two hypotheses were tested and **falsified** — record so they are not retried:
  (1) *Catalogue trim removed indexed URLs* — checked all 47 product URLs with pre-trim
  traffic against surviving handles: only 5 are dead (~219 clicks total). Not the cause.
  (2) *Core update / permanent ranking loss* — positions fell site-wide but recovered
  within ~2 weeks, which a core update does not do.
  ⚠️ Small real finds worth fixing anyway: dead URLs `durable-mens-leather-gloves-light-
  brown-kordovan-1` (125 clicks/5,394 impr), `copy-of-the-access-minimal-wallet`,
  `four-in-one-leather-gift-set`, `the-seamless-stitch-less-wallet`, `the-hunter-crazy-
  horse-belt`; plus **`the-braded-belt` is DRAFT** (429 impr) so it 404s on the storefront.
- 📌 **Catalogue is now 172 products (170 active, 2 draft, 0 archived)** vs 357 in Jul —
  ~185 hard-deleted. 84 URL redirects exist, mostly legacy. Deletion did NOT hurt
  rankings measurably, but build redirects for the 5 URLs above.
- **Learning phase:** at ~PKR 8,450 jacket CPA, 50 conversions/week = PKR 400k+/wk,
  so a jacket campaign optimising for Purchase will NEVER exit learning. Optimise on
  View Content at small budgets; keep ONE broad consolidated ad set (Advantage+ did
  6.43% CTR / PKR 9.75 per click last season — best in the account).

## 📊 AUGUST 2026 AD AUDIT (measured Sep 4 2026 — full month, Shopify-reconciled)
✅ **Ad-level insights + `publisher_platform`/`platform_position` breakdowns WORK via the MCP.**
The Aug 20 session concluded they were blocked; they are not — retry before ever telling the
user placement data is unavailable.
- **Spend PKR 148,310. Meta reported 5.40x. Real (surviving Shopify revenue) = 2.63x.**
  Ladder: Meta 800,401 → matched to real orders 709,469 (130) → **surviving 390,328 (85)**
  → cash collected 292,679 (71). **Standing correction factor for this account ≈ 2.0–2.1x**
  (matches the playbook's ~2x note; now measured twice).
- Contribution at 45% GM = **+PKR 19,712 only.** Break-even = 2.22x (1.82x at 55% GM).
  August was *marginally* profitable. Do not scale a thin margin.
- Per ad set (spend / Meta ROAS / REAL ROAS / contribution @45%):
  | Retarget Warm+Buyers | 35,064 | 6.92x | **4.32x** | +33,056 ✅ best in account |
  | TOF-C Catalogue Cold | 20,177 | 8.31x | **2.81x** | +5,338 ✅ only 20 days live |
  | TOF-A Mocha Mate | 46,489 | 3.89x | **2.42x** | +4,135 ⚠️ paused Sep 1 |
  | Bastion Cold | 1,173 | — | **7.54x** | +2,809 ✅ tiny n, retest |
  | BOF DPA Product Intent | 30,913 | 6.50x | **1.33x** | −12,396 ❌ freq **8.10** on 11,739 reach |
  | TOF-B Razor (killed Aug 11) | 14,469 | 0.56x | **0.19x** | −13,231 ❌ |
- 🔴 **TOF-C Catalogue Cold is the big discovery: CPC PKR 6.96 / CTR 4.17% on COLD traffic**,
  vs the playbook's cold benchmark of PKR 32–52. Catalogue/DPA-format cold creative beats
  static+video cold creative by ~5x on click cost. Under-tested — only 20 days live.
- **Kill discipline is the process gap.** TOF-B was correctly killed but 7 days late
  (PKR 9,207 wasted). Signal was clear by day 3. Rule to apply: write the kill threshold in
  rupees BEFORE launch (≈2x break-even CPA, ~PKR 5,500 for a wallet), check day 3 and day 5.
- ⚠️ **7 learning-phase resets in 11 days** (status flips, re-reviews, a 6-minute pause/unpause,
  TOF-C flipped 5x in 21 min). Batch edits; leave ad sets alone 72h.
- **Placement quality (Shopify-verified survival, NOT Meta's ROAS):** IG Stories 100% (n=3) ·
  IG Feed 89% · IG Reels 72% (biggest surviving revenue, 48,700) · FB Feed 62% · **FB Reels 52%**.
  🚫 **Do NOT exclude FB Reels** — Breakdown Effect; it is also the cheapest CPM (255–314 vs 473).
  It is a *signal* problem: fix by feeding paid/delivered back to Meta, not by cutting placement.
- 🔴 **UTM blind spot: 57 of 127 paid-Meta orders (45%) carry no usable placement tag** because
  `Retarget` and `TOF-C` hardcode `utm_content=Facebook_UA` / adset-ID. 3 more carry literal
  unresolved `{{site_source_name}}` / `{{placement}}` macros on TOF-A. Fix with dynamic macros.
- **Store-wide Aug:** 223 orders / 1,259,046 placed → 139 surviving / 726,660 (62%).
  Real RTO 20 = **9.0%** (matches the 9.9% baseline). Pre-dispatch kills 64 = 28.7%.
  Channel: Meta 402,078 surviving (cost 148,310) · **Organic search 193,224 at ZERO cost**
  · Direct 118,808. Organic = 51% of Meta's output for 0% of the spend → keep funding SEO.
- 🔴 **JACKETS AUG: 8 orders placed (334,700) → only 2 survived (128,150) = 25% survival**,
  vs 62% store-wide. Zero doorstep refusals — all 6 died pre-dispatch on the unpaid 50% deposit.
  Worse than the 42% historical baseline. **Fix the deposit flow before October spend lands.**
- 9-city rule re-validated again: inside 70% survival vs outside 47%.
- Full report artifact: `https://claude.ai/code/artifact/0c0cee26-25af-4c81-adc2-677245832118`
  Working data + scripts: scratchpad `aug-audit/` (session-local; rebuild via bulk export).

## 🎯 THE THREE LIVE CATALOGUE ADS (analysed Sep 4 2026, daily series Aug 1–Sep 3)
All three currently-running ads ARE catalogue/DPA ads, all at **PKR 1,000/day**, and all point at
the **SAME product set `608788148654460` "All Products" (164 items)** in catalogue
`1015378560682303`. No segmentation between cold / intent / warm.
- ✅ **Catalogue format confirmed ~4x cheaper than static+video:** catalogue CTR 4.07–4.30% /
  CPC 6.96–8.14 / cost-per-LPV 9.30–10.94, vs Mocha Mate + Razor at CTR 1.64–1.74% /
  CPC 29.69–31.66 / LPV 49.28. Keeping only catalogue ads live was correct.
- 🔴 **THE BLANK DAYS ARE POISSON NOISE, NOT A PERFORMANCE PROBLEM. Do not "diagnose" them.**
  Each ad buys ~1 order/day (spend ≈ CPA ≈ 1,000), so e^−λ predicts the blanks almost exactly:
  Retarget λ=1.47 → 23% predicted vs **21% observed** · DPA λ=1.00 → 37% vs **32%** ·
  TOF-C λ=0.96 → 38% vs **42%**. Sale-days vs blank-days differ by <6% on CTR/CPC/impr/freq.
  **Fix = raise λ, not "optimise".** Pooling the SAME PKR 3,000/day into ONE campaign turns three
  1/day lotteries into one 3/day process → blank days fall ~11/month to <2. Costs nothing.
  ⚠️ Judge these ads on **14-day windows**; a 3-day read is one order.
- **Revenue concentration is extreme:** TOF-C top-3 days = 58% of its revenue (a single
  PKR 51,450 order on Aug 12 = 25%); DPA top-3 = 55%; Retarget top-3 = 34% (healthiest).
- **Per-ad state:**
  | Retarget Warm+Buyers | 4.32x real | freq **4.86** | blank 21% | IMPROVING (5.73x→10.20x H1→H2) |
  | BOF DPA Product Intent | 1.33x real | freq **8.10** | blank 32% | DEGRADING (blank 4/17→7/17, pur 21→13) |
  | TOF-C Catalogue Cold | 2.81x real | freq **1.14** | blank 42% | COOLING (11.95x→5.98x, blank 3/12→7/12) |
  ⚠️ DPA Sept burn is WORSE: freq 2.63 in Sep 1–4 alone on reach 4,165 (~3x August's daily rate).
- 🔴 **CREATIVE DEFECT (live, fix first): the DPA body says "cash on delivery anywhere in the
  country — you pay when it reaches your door."** Violates the 9-city rule AND misstates jacket
  terms (50% to book, balance to rider). The set includes all 30 jackets → likely a direct
  contributor to jackets dying at the deposit stage.
- ⚠️ **The Retarget creative dates from 2025-05-21 — 16 months old, never refreshed**, names
  "KODO 2.0", and is off-brand (emoji bullets, "Built tough. Priced right." = discount voice vs
  Quiet Heritage). It is winning on audience quality DESPITE the creative. **Never edit it in
  place** (resets 16 months of learning) — run a new on-brand ad alongside it.
- 📌 **Catalogue coverage: 107 of 590 variants (18%) cannot be served.** Meta's 107
  PRODUCT_OUT_OF_STOCK items map EXACTLY onto Shopify's 107 variants that are
  `inventoryQuantity<=0 AND inventoryPolicy=DENY` (= `availableForSale:false`).
  ✅ **The feed is ACCURATE — this is not a sync fault.** Shopify→Meta sync `connected`,
  last success 2026-09-03. Jackets are NOT suppressed (all 33 zero-stock jacket variants are
  CONTINUE, so they reach Meta as in stock). 131 CONTINUE-at-zero variants sync fine.
  ⚠️ `has_webhooks_registered: false` → catalogue updates are a once-daily batch, not realtime.
- 🔴 **23 products are 100% invisible to every catalogue ad** (no sellable variant), incl.
  **The Mocha Mate Wallet** (the hero of the paused TOF-A cinematic ad!), both cowboy hats
  (a category ranking pos 4.8 / CTR 13.8% in GSC), The Casual Belt, ILLUSION Magic Wallet,
  The Truckkr, Crazy Horse Long Wallet, 4 laptop bags. A further 38 lose part of their range
  (Documate 4 of 6 hidden, Diana Pebbled 4 of 5). **Restocking widens the shelf at zero media cost.**
- 🔴 **The real ceiling is click→ATC of 2.4–3.4%** (Retarget 3.4 · DPA 3.1 · TOF-C 2.4).
  ATC→order is HEALTHY at 26–32%. ~11,600 of ~12,000 paid clicks left without adding anything.
  Lifting click→ATC 3%→4.5% = +50% orders on all three ads at once = same as +PKR 1,500/day free.
  **That is a PDP problem (27 of 30 jacket PDPs still show no rating/review), not an ads problem.**
- Full diagnosis artifact: `https://claude.ai/code/artifact/4b45ff0c-623f-4acb-bda8-1ccffa5ca7f1`

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

## 📣 Meta Ads (SCOPED — Kordovan 2025 ONLY)
> 🔴 **STANDING RULE (user, Aug 3 2026): EVERY ad set targets these 9 CITIES ONLY.
> Never `countries: ["PK"]` again.** PostEx delivers to cities, not villages —
> country-wide targeting sent ~40% of orders to small towns and most were
> cancelled, while still firing Purchase events that teach Meta to find more of
> them (same failure mode as the COD refusers).
> Meta city keys (verified live, use these directly in `geo_locations.cities`):
> ```
> Karachi 1800796 · Lahore 1807162 · Islamabad 1796084 · Rawalpindi 1822222
> Faisalabad 1784775 · Multan 1814658 · Sialkot 1827865
> Gujranwala 1792796 · Hyderabad 1795700
> ```
> ⚠️ **NO `radius`** on any of them — a radius re-includes the villages. Omitting
> the key entirely = "current city only", which is what we want.
> ⚠️ `targeting` is a FULL REPLACE via the API — fetch the ad set's existing
> targeting and merge, or you will wipe the audiences and exclusions.
> 📕 **READ `ops/ADS_PLAYBOOK_PK.md` FIRST for any ads work.** Real PKR benchmarks,
> COD unit economics (cold is currently under water, retargeting is very
> profitable), the ~2x Meta attribution overstatement, and the delivery mechanics
> that bite us. It overrides every number in the vendored ad skills.
- **ONLY account to ever touch/reference: `995683712074843` ("Kordovan 2025", PKR,
  ACTIVE).** User locked scope Jul 7 2026. IGNORE all others (Kordovan Leather
  337…255 = DISABLED/flagged; Kordovan 2.0 492…061 = closed; Corporate 136…323;
  UAE 589…560; + unrelated DEW/Vertix/Ivy Laine/Oakn'Moss).
- **KEY INSIGHT (parallels COD finding):** lookalike seeds = Pixel "Purchase"
  (order PLACED) → ~40% are COD refusers, so LLAs teach Meta to find refusers.
  FIX PLAN: (1) reseed value-based LLA from DELIVERED/PREPAID buyers (clean seed
  buildable from bulk order export); (2) build REFUSER EXCLUSION audience (323
  FRAUD RISK + all cancelled-order customers) → exclude from prospecting;
  (3) feed delivered/paid back as conversion signal (offline conv/CAPI); (4) prune
  ~25 audience sprawl. Old inactive "Lifetime Fulfilled Customers" LLA had the
  right idea (fulfilled=delivered) but is off.
- Uploading customer PII (hashed) to Meta needs explicit user OK each time.
- **Pixel EMQ (dataset 1865080707652548 "Kordovan 2025 Dataset", CAPI live):**
  Purchase 9.3/10 (email/phone/name 100%) — HEALTHY, not the problem. Funnel
  events 6.3–6.9. The issue is SEMANTIC: great data on wrong event (order placed
  incl. 40% refusers). Second pixel "…(DO NOT USE)" 652254084055676 = dead.
- **AUDIENCE BUILD (Jul 8 2026) — DONE (except exclusion upload):** ToS accepted.
  SEED `120253659969900428` "KV — Delivered Repeat Buyers (SEED, value-based)"
  POPULATED (~1,050 matched, value-based, ACTIVE) via native CSV upload.
  Value-based LLAs created off it: 1% `120253661268330428`, 3% `120253661269660428`,
  5% `120253661272010428` (populating ~few hrs). EXCLUSION
  `120253660257910428` "KV — COD Refusers EXCLUDE (never delivered)" POPULATED
  (3,891 uploaded 100%). BOTH audiences done. Full seed of all 14,122 delivered buyers
  available (seed_all.tsv) if we ever want a broader seed. Old polluted LLAs
  ("Purchase 180"/"Pixel Purchasers") → PAUSE once new LLAs ready.
- **STRICT AD RULE (locked):** EVERY ad set EXCLUDES "KV — COD Refusers EXCLUDE".
  COLD = value-based LLA 1–3% of Delivered Repeat Buyers seed (+exclude existing
  buyers). WARM = website/ATC/IC visitors (+exclude refusers +recent purchasers).
  PAUSE old "Purchase 180"/"Pixel Purchasers" LLAs (polluted w/ refusers).
- Data export files in scratchpad: cancelled_orders.jsonl (5203), orders_12mo.jsonl
  (3468), serial_cod_refusers.csv, META_*.csv.
- **Prepaid discount LIVE on store:** code `PAYONLINE10` (10% off, active, unlimited).
  Deploy via WhatsApp order-confirmation reward (leak-proof, no app). Full enforce
  + COD fee + OTP later via PostEx XPay integration (user exploring) — PARKED.

## 🗺 SEO MASTER PLAN (user-confirmed Jul 15 2026 — three phases, in order)
1. **Phase 1 — user cleans Shopify catalog** (trash-scrape, manual; see PARKED
   section below for the re-audit checklist when done: counts, kdv- collections,
   redirects for removed URLs, fresh alt audit).
2. **Phase 2 — in-session SEO enrichment of surviving products (together):**
   priority from GSC data — wallets first (mens-leather-wallets pos 10.2 /
   14.5k impr = biggest prize), then cowboy hats (easy #1s), then jackets (fix
   1.9% CTR titles/metas). Per product: title+meta, bulk pattern-based alt-text
   backfill via API, description in brand voice, PDP metafields (subtitle/
   benefits/material/fits/reviews). Per collection: editorial block + JSON-LD.
3. **Phase 3 — automation for FUTURE products (only after 2 proves the pattern):**
   free stack = Shopify custom app (user creates in admin, 5 steps, gives API
   token) + webhook → Cloudflare Worker + Workers AI free tier (~10k neurons/day).
   (a) auto-alt on product create/update (deterministic title/variant pattern +
   vision assist, idempotent, never overwrites existing alts); (b) descriptions
   NEVER auto-published — draft to metafield + `needs-seo-review` tag, human
   approves; (c) nightly self-heal sweep. Worker can query our GSC connector for
   real keywords per product.
- **Alt audit baseline (Jul 15 2026, pre-trim):** 169 live products (192 active,
  357 total), 1,316 images, **630 missing alt (47.9%)** across 80 products;
  worst: Bella Duff 62/63, Diana Cross-body 46/47, TP bags ~26 each. Pattern:
  first images have alts, extra variant/angle shots don't. Detail file
  `alt_audit.jsonl` in scratchpad (session-local; re-export post-trim).

## 🧾 Jacket SEO audit (measured Aug 20 2026, all 30 `Leather Jacket` products)
⚠️ **Do NOT assume product SEO is incomplete — titles/descriptions/alt are DONE.** The
Aug 2026 pass covered them; a fresh session wasted effort re-checking. Measured state:

| Field | Coverage |
|---|---|
| SEO title | **30/30** |
| SEO description | **30/30** |
| Image alt text | **179/179 (100%)** — jackets are the one clean category vs 47.9% missing store-wide |
| `custom.fits` | **30/30** |
| `custom.subtitle` | **30/30** ✅ filled Aug 20 2026 |
| `custom.benefits` | **30/30** ✅ filled Aug 20 2026 |
| `custom.material` | **30/30** ✅ filled Aug 20 2026 |
| `reviews.rating` | **3/30** (mens-spy 3.0, shadow-rider 5.0, stryker 1.0 — each count 1) |
| `custom.reviews` | **0/30** |

- subtitle/benefits/material were written per product from each one's own spec list
  (`material` renders inline in the PDP eyebrow so it must stay short — e.g.
  `Top-grain sheep leather`, `Top-grain sheep suede` for Apex, `Semi-aniline sheep
  leather` for the two women's).
- 🚫 **Reviews are NOT to be invented.** The 3 existing ratings are real customer ones
  (nobody self-authors a 1-star). Fabricating customer names/cities/testimonials next to
  genuine ratings is deceptive and undercuts the whole "we're the honest ones" position.
  **Collect real ones instead:** 56 delivered jacket buyers exist, 54 contactable,
  covering 29 of the 30 jackets. Outreach list built Aug 20 2026
  (`jacket_review_outreach.csv`, session-local — rebuild from a bulk export of
  `financial_status:paid` orders with jacket line items). Start with Durham Waxed and
  Desert Voyager, 5 owners each.
- ⚠️ **Stryker shows 1.0 stars from a single text-less review, live.** An unexplained
  one-star is worse than no rating — it is the only social proof on that page. Three of
  its owners are on the outreach list.

- Titles are correctly front-loaded (`Men's Black Biker Leather Jacket Pakistan — Iconic
  | Kordovan`). 22 of 30 exceed 60 chars but what truncates is `| Kordovan` — **leave
  them alone**, this is not a defect.
- 🔴 **The live gap is PDP depth, not metadata.** `snippets/pdp-main.liquid` renders the
  review block + star rating ONLY when `reviews.rating` is set, so **27 of 30 jacket PDPs
  currently show no rating and no social proof**. That sits directly on the conversion
  bottleneck (jacket site CR ~0.115%, cheap clicks at PKR 9.75) heading into the season.
  Filling subtitle/benefits/material/reviews is worth more than any targeting change.

## 🏬 PARKED — Catalog trim before SEO (user doing manually)
User moved to own POS software (synced w/ Shopify). Is removing store-only / bogus /
irrelevant products from the ONLINE store so the online catalog = only what's sold
online. Cautions given: (1) UNPUBLISH from Online Store channel vs DELETE — deleting
may break POS sync / remove POS record; only hard-delete truly-dead SKUs. (2) Removed
products leave 404s → need URL redirects (build a bulk redirect list after). When user
returns: re-audit trimmed catalog (count remaining online products, verify 6 kdv-
smart collections still populate by tag, flag empty collections, set up redirects),
THEN start SEO enrichment on the clean set.

## 📍 Session state (resume here)
- **Workflow = mockup-first:** build static HTML mockup in `docs/mockups/` →
  user approves → THEN implement in Liquid → deploy once. (User's idea — avoids
  repeated Shopify pushes/sync lag while iterating on design.)
- ⚠️ **GOTCHA — class-name collisions:** homepage collection-grid TILE class
  `.kv-coll` (display:flex) collided with the collection-PAGE wrapper `.kv-coll`,
  forcing the page into 3 columns. FIXED by scoping all homepage tile rules under
  `.kv-colls .kv-coll`. Lesson: namespace page wrappers distinctly.
- ⚠️ **GOTCHA — GitHub sync got stuck on `sections/main-product.liquid`** (draft
  kept serving the legacy `.product-page` template; new file `pdp-main` section
  also wouldn't sync, and `templates/*.json` are theme-editor-owned so git won't
  overwrite them). FIX: PDP body lives in `snippets/pdp-main.liquid` (snippets DO
  sync); `sections/main-product.liquid` is a thin `{% render 'pdp-main' %}` wrapper
  pushed directly to the DRAFT theme via `themeFilesUpsert` (allowed on unpublished;
  blocked on live). If main-product ever reverts, re-upsert the wrapper.
- **Done & deployed** to `kordovan`: Step 1 (Quiet Heritage palette +
  Fraunces + logo support), Step 2 (homepage scroll order, brand story copy,
  testimonial names, eyebrow fix).
- **Homepage mockup** `docs/mockups/homepage-final.html` — APPROVED. **Homepage is
  now FULLY BUILT & deployed** (all kv- sections in `assets/home.css`, loaded
  globally via `layout/theme.liquid`): header → hero → trust marquee → bestsellers
  (Customer Favourites) → brand story → collections grid → testimonials (continuous
  horizontal review marquee, 10 verified reviews, pause-on-hover — user asked for
  "lots of reviews that scroll") → email capture (real Shopify customer form) →
  footer (`site-footer.liquid`, hardcoded content).
- **Content pages DONE:** `sections/main-page.liquid` rebuilt into on-brand editorial
  layout (`.kv-page` / `.kv-rte` in home.css); leading h1/h2 in page bodies is
  CSS-suppressed (hero band shows the title). Pages already exist in the store w/
  real content — footer/CTA links repointed to the REAL handles:
  `about-kordovan` (Our Story), `our-craft` (hero "See the Craft"), `shipping`,
  `leather-care-guide`, `returns`. (Don't use `/pages/about` or `/pages/leather-care`.)
- ⚠️ **Editor strips SETTINGS too (not just blocks):** the theme editor removed
  newly-added section settings (`aggregate`, `percent`, `count`, hero `heading`)
  from `index.json` on sync — harmless ONLY because every kv- section supplies
  `| default:` fallbacks in liquid. Keep hardcoded defaults on all section settings.
- **Content-page designs DONE & deployed:** Our Story (`about-kordovan`), Our Craft
  (`our-craft`), Shipping (`shipping`), Leather Care (`leather-care-guide`), Returns
  (`returns`) — bespoke layouts rendered via `snippets/*` dispatched by handle in
  `sections/main-page.liquid` (theme-local; NO template-suffix change → live theme
  untouched). Shared `.kv-cp` component CSS in home.css. Images uploaded to Files
  (`about-*`, `craft-*`, `care-patina`, `returns-pillar-bg`).
- **PRODUCT PAGE (PDP) DONE & deployed:** `sections/main-product.liquid` +
  `related-products.liquid` restyled to the approved `docs/mockups/product.html`
  (`.kv-pdp` CSS). Reuses ALL `theme.js` hooks (`.product-gallery`, `.product-form`,
  `.variant-btn`, `.product-atc__*`, `.product-info__price-*`, `[data-product-variants]`)
  so gallery/variants/AJAX add-to-cart/cart-drawer work untouched. Structure:
  gallery + sticky benefit buy-box (price+shipping transparency, full-width cognac
  ATC, 3 trust icons) → 4 brand features → capacity "fits" (metafield) → description
  + Care/Shipping/Warranty accordion → reviews (metafield) → guarantee → related →
  sticky mobile ATC.
- ⚠️ **SEO-PHASE TODOs (user-confirmed, remember):** (1) NO review app — author
  reviews ourselves per product via metafields: `reviews.rating` (number),
  `reviews.rating_count`, `custom.reviews` (one per line `name|city|text`). PDP shows
  the reviews block + star rating ONLY when `reviews.rating` is set (hidden until then).
  (2) Go product-by-product so EVERY active product matches this PDP's depth — fill
  `custom.subtitle`, `custom.benefits` (one per line), `custom.material`, capacity
  `custom.fits` (`value|label` per line) + `custom.fits_title`/`fits_text`, full image
  gallery. Until filled, brand-universal fallbacks render.
- **Known follow-up:** site header cart link (`.kv-cart`) navigates to /cart; it does
  NOT open the cart drawer (theme.js binds drawer-open to legacy `.header__cart-btn`).
  Wire `.kv-cart` to open the drawer when we polish cart.
- **COLLECTION / CATEGORY PAGE DONE & deployed:** `sections/main-collection.liquid`
  + new `snippets/card-product.liquid` restyled to `docs/mockups/collection.html`
  (`.kv-coll` / `.kv-pc` CSS). Compact hero, sticky toolbar (native sort +
  storefront filter pills/drawer + active chips), 3/2-col grid, hover 2nd-image +
  Quick Add (reuses theme.js `.product-card__quick-add[data-variant-id]`) + colour
  swatches + Sold-Out/Sale/New badges + wishlist, JS **Load More** (appends next
  paginated page), editorial SEO block + `CollectionPage`/`ItemList` JSON-LD.
  Serves EVERY category. `collection.json` keeps email_signup below.
  ⚠️ **Filter pills/drawer populate only when storefront filters are enabled** in
  admin → Search & Discovery → Filters. Until then: just "All" + sort (graceful).
  Optional `collection.metafields.custom.editorial` overrides the SEO block.
- **CART DRAWER DONE & deployed:** `sections/cart-drawer.liquid` restyled to
  `docs/mockups/cart-drawer.html` (`.cart-drawer` in home.css). `theme.js
  CartDrawer.render` now outputs the **free-shipping progress bar** (threshold
  PKR 2,500 = `250000` minor units in `renderShip()` — change there if free-ship
  amount changes), kv line items with inline qty + **Remove**, subtotal; shows/
  hides ship+cross-sell on empty. **Header cart `.kv-cart` now opens the drawer**
  (fixed the earlier gap). `KDV.updateCartCount()` updates both legacy + `.kv-cart i`
  badges. Cross-sell = server-rendered from `cart-drawer` section setting
  `upsell_collection` (default `kdv-accessories`), one-click via the quick-add hook.
- **SEARCH DONE & deployed:** full-screen overlay `snippets/search-overlay.liquid`
  (opens from `.kv-search` desktop + mobile-menu link; popular searches + category
  empty state; debounced live results) backed by `sections/predictive-search.liquid`
  (server-rendered suggestions/collections/products via `/search/suggest?section_id=
  predictive-search`). `sections/main-search.liquid` restyled to `.kv-coll` grid +
  `card-product` + Load More + friendly no-results. `.kv-srch` CSS in home.css.
- **STOREFRONT BUILD COMPLETE** (homepage, content pages, PDP, collection, cart
  drawer, search). **OPEN = SEO PASS + polish:** (1) per-product enrichment +
  self-authored reviews via metafields; (2) titles/meta/alt text + PDP Product
  JSON-LD; (3) enable storefront filters (Search & Discovery); (4) logo upload +
  favicon + social share image; (5) optional polish: /cart PAGE, 404 & account
  pages still on legacy theme styling; wishlist heart is decorative (no backend).
- Logo: user is uploading manually (Header → "Logo (dark mark)"); needs a
  TRANSPARENT-bg black PNG (their source had a white bg). Favicon/social TODO.

## ⚡ Performance rules (Jul 26 2026 pass — do not regress)
- **Fonts must stay a `<link>` in `layout/theme.liquid`.** Never put the Google
  Fonts call back as `@import` in `theme.css` — that forced a 3-deep serial chain
  (css → googleapis → gstatic) before first paint.
- **Hero is a real `<img>`, not a CSS background.** Backgrounds are invisible to
  the browser's preload scanner and can't be responsive; the hero is the homepage
  LCP element. `object-fit:cover` + `object-position:center right` reproduce the
  old framing.
- **Every new `<img>` needs `srcset` + `sizes` + `width`/`height` + `loading`.**
  A bare `image_url: width: 600` ships a desktop file to a 180px phone slot.
  Above-fold → `loading="eager" fetchpriority="high"`; everything else → `lazy`.
- **Gallery swaps decode before painting** (`assets/theme.js` `goTo`/`preload`).
  Never reintroduce a fixed `setTimeout` fade — it shows a blank frame while the
  file downloads. Anything that changes the main image must set **`srcset` as well
  as `src`**, or the browser keeps painting the old one.
- ⚠️ `theme.css` holds the `:root` design tokens that `home.css` depends on —
  it cannot be dropped even though it is largely legacy styling.
- Verify before pushing: `node --check assets/theme.js` + div/liquid tag balance.
  The site cannot be loaded from this environment (proxy denies
  `kordovanleather.com`), so static checks are the only safety net.

## 🖼 Image workflow (protocol)
- **Every designed image slot = an image brief:** product/subject + ready-to-paste
  GPT-image prompt + exact px size & aspect. Tracked in **`docs/images/IMAGE_BRIEF.md`**.
- Give new briefs inline whenever a new image slot is introduced.
- **Label/copy on a tile must match the image in it** (no mismatched product names).
- Product cards use real Shopify catalogue photos; hero/mega/collection/brand-story
  use the generated "art-directed" images.

## 🗃 Site collections (kdv- set — controlled, for this theme)
Created as **smart collections** (auto-populate by tag), published to Online Store,
sorted **Best Selling**. Referenced by hardcoded handle in Liquid (NOT via JSON
template settings — Shopify's editor strips collection/handle settings from
`templates/index.json` on sync, which is why block-based references render empty).
- `kdv-wallets` (≈55) · `kdv-bags` (≈68) · `kdv-jackets` (≈36) · `kdv-shoes` (≈24)
  · `kdv-belts` (≈13) · `kdv-accessories` (≈28)
- Header nav + Bestsellers (#1 per category) reference these. New Arrivals →
  `/collections/all?sort_by=created-descending`; Sale → `/collections/all` (no
  kdv-sale yet). Women's sub-links still use existing womens-* collections.

## ✅ Working loop
Edit theme → push to draft theme `165057069296` (via Shopify) → review in browser
→ iterate. Keep to the BRAND_MOODBOARD spec at every step.
