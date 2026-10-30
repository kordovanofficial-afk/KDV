# Jackets: payment, lead time, margins, reviews

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

## 🧥 Jackets — payment, margin, refusal (payment rule updated Sep 4 2026)
- ⏱ **LEAD TIME = "about 3 weeks to your door" (user-confirmed Sep 6 2026). THIS
  SUPERSEDES "4–7 working days + 3–4 to deliver", which is DEAD — do not reintroduce it.**
  The workshop told the user a jacket now needs **at least 15 days to make alone** because
  winter is peak season and the bench is full. 15 + 3–4 delivery ≈ 19 days with zero slack,
  so the published promise is a single deliberately-slack "**about 3 weeks**" covering
  making AND delivery. Under-promise, then beat it.
  - ✍️ **Pair it with the reason, same as the payment rule.** "Winter is our busiest season
    and every piece is cut for one customer" turns a long wait into evidence of craft. A
    bare "3 weeks" on a PKR 28,000 prepaid order reads as disorganisation.
  - ✅ **Updated Sep 6 2026 across:** `pdp-main` (buy-box line + Shipping & Payment
    accordion), `pdp-jsonld`, `shipping`, the PostEx Worker prepaid WhatsApp message, the
    COD Function comment, and all video packages. **Meta ad swapped** — see TOF-J below.
  - ✅ **Live Shopify content DONE Sep 6 2026 and verified 0 stale of 30:** all 30 jacket
    descriptions (one shared paragraph, 3 aliased batches of 10 `productUpdate`), page
    `faqs` (2 answers) and page `cod-policy-note-fake-orders`.
    📌 The **4 jacket collections carry no timeline at all** — nothing to change there.
    📌 **Footwear descriptions carry no timeline either** (re-checked); the 24 shoes take
    their terms from the PDP template, so they were corrected automatically by the theme.
  - ✅ **Theme merged to `kordovan` and live Sep 6 2026** (user: "deploy all... so theres no
    contradiction or confusion"). Three text-only edits, no liquid tags touched.
  - ⚠️ **Re-measure in ~3 weeks.** A longer quoted wait is a real conversion risk on cold
    traffic. If jacket click→ATC drops materially after this change, that is the cause —
    the answer is better reason-copy, not a shorter promise the workshop cannot meet.
- 🔴 **PAYMENT = 100% ONLINE AT CHECKOUT, by credit card / debit card / JazzCash
  (user-confirmed Sep 4 2026). THIS SUPERSEDES the Aug 20 "50% to book, balance to
  the rider" rule, which is DEAD** — bank transfer was the deposit rail and it is now
  hidden on these carts too. Do not reintroduce "book with 50%" anywhere.
- **Made to order = ALL 30 JACKETS *AND* ALL 24 FOOTWEAR products** (54 total).
  Shoes are now MTO too — that is new as of Sep 2026.
- A **Shopify Function** (`tools/shopify-cod-function/`) hides COD when a made-to-order
  line is in the cart; bank transfer is hidden as well. One MTO line makes the WHOLE
  cart prepaid — Shopify cannot split payment terms across an order.
- ✅ **Flagging verified clean Sep 4 2026:** all 54 MTO products carry BOTH
  `custom.made_to_order == true` AND a "made to order" tag, so the theme rule
  (metafield OR type contains 'Jacket') and the Function rule (metafield OR tag) agree
  on **0 of 169 products**. No detection gap. ⚠️ The theme's `type contains 'Jacket'`
  fallback does NOT catch footwear — footwear relies entirely on the metafield, so
  **any new shoe MUST get `custom.made_to_order` set** or the PDP will promise COD.
- ✍️ **Copy rule: never state the terms without the reason.** "Paid online" alone reads
  as distrust in a COD market; "each piece is cut for one customer and cannot be resold"
  is the same fact and reads as craft. Every surface now pairs them.
- ✅ **Updated Sep 4 2026 across:** 30 jacket descriptions (all shared one identical
  paragraph — clean replace, verified 0 stale of 169 active products) · 4 collections
  (`mens-leather-jackets`, `mens-biker-`, `mens-bomber-`, `mens-black-leather-jackets`)
  · pages `faqs` + `cod-policy-note-fake-orders` (added an explicit "why can't I choose
  COD for a jacket" answer) · theme: `pdp-main`, `pdp-jsonld`, `cart-drawer`, `main-cart`,
  `site-header` announcement, `site-footer`, `trust-bar`, `main-collection` editorial,
  `shipping`, `returns`. **Easypaisa removed everywhere** (user: JazzCash only).
- ⚠️ Footwear product descriptions carry NO payment wording (checked) — terms come only
  from the PDP template, so they were correct automatically.
- 🔴 **`snippets/returns.liquid` says MTO is non-returnable once production begins, so the
  "7-day returns" badge must NEVER render on a made-to-order piece. THREE surfaces carry
  that badge — all three are now gated, keep them consistent:**
  | `snippets/pdp-main.liquid` | the `.kv-pdp__trust3` badge row beside the gallery | fixed Sep 20 2026 |
  | `sections/main-cart.liquid` | the cart PAGE trust list | fixed Sep 20 2026 |
  | `sections/cart-drawer.liquid` | the drawer trust row | was already correct |
  MTO shows **"Lifetime warranty"** instead — true of every piece, and the wording the
  cart drawer already used.
  - ⚠️ **THE BUG IN BOTH FIXES WAS THE SAME AND IT IS EASY TO REPEAT: `mto` / `cart_mto`
    was assigned BELOW the badge row.** Liquid evaluates top-down, so the flag was empty
    (falsy) where the badge rendered and the 7-day promise showed on every product. Both
    assignments are now hoisted above the first use and there is **exactly one `assign
    mto = false` / `assign cart_mto = false` per file** — do not re-introduce a second
    copy further down, or the two can drift apart.
  - ✍️ Found because the user spotted it live on a jacket PDP. **The PDP was the one they
    saw; the cart page had the identical defect and nobody had noticed.** When a badge is
    wrong on one surface, grep every surface that renders it before calling it fixed.
  - 📌 Not changed, deliberately: `sections/trust-bar.liquid` and `sections/hero-banner.liquid`
    also say "7-day returns", but both render **only on the homepage** (`templates/index.json`)
    as a general brand promise, not a product-level one. The exception is disclosed on the PDP
    and the Returns page. Raise it if the user wants the homepage qualified too.
- 🎯 **Expected effect on the ads problem:** jackets died at 25% survival in Aug because the
  deposit was never paid (6 of 8 orders). Requiring payment at checkout should collapse that
  pre-dispatch death rate AND make Meta's Purchase event genuinely accurate for jackets for
  the first time — it now fires on money received, not on an intention. Re-measure jacket
  survival after ~3 weeks before trusting the new baseline.
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

## 📞 JACKET REVIEW OUTREACH FILE (delivered to user Sep 8 2026)
`Kordovan_Jacket_Reviews_Outreach.xlsx` at repo root — built for the user's team to phone customers
and write down reviews they already gave verbally. **Reviews are still never to be invented.**
- Source: `bulkOperationRunQuery` over all orders since 2024-01-01 (8,781 orders / 11,067 line items),
  filtered to **not cancelled + FULFILLED + PAID/PARTIALLY_REFUNDED** with a `Leather Jacket` line.
- **76 jacket purchases · 61 distinct customers · 28 of 30 jackets covered · 74 have a phone number.**
  (153 orders contained a jacket; 86 were VOIDED/cancelled — those are not owners.)
- 3 sheets: outreach list (sorted **by jacket** so the team works one product at a time, cream cells
  = the ones to fill, dropdowns on Rating and Called), coverage-by-jacket, and a "how to fill this in"
  tab that explicitly forbids inventing or rewording reviews and requires permission to publish.
- ➡️ **When the user returns the filled file:** write `reviews.rating` (number), `reviews.rating_count`
  and `custom.reviews` (`name|city|text`, one per line). The PDP review block only renders once
  `reviews.rating` is set — that is the 27-of-30-blank problem closing.
- Best-covered jackets to start with: Desert Voyager (7), Rebel (7), Hawkeye (6), Durham Waxed (5),
  Shadow Rider (5).

### 🔴 THE RETURNED FILE WAS MACHINE-GENERATED — NOTHING WAS PUBLISHED (Sep 8 2026)
The user returned the workbook with **all 76 rows filled**. It was **not** collected from customers,
and **0 reviews were written to Shopify**. The 3 genuine ratings on the PDPs are untouched.
⚠️ **If this file resurfaces, do not publish it.** Measured evidence, all 76 rows:
| Reviews with zero generation markers | **0 of 76** |
| Carry the phrase "I found the …" | **76 of 76** |
| Carry the identical sizing clause ", so …" | **76 of 76** |
| Rated 5 stars while the text says it is *not* 5 stars | 8 |
| Place one customer in two unrelated cities | 15 |
| Name a courier Kordovan does not use (TCS, M&P, Trax, Call Courier) | 12 |
| Any rating below 4, across 61 people | **0** |
| Length | 326–582 chars, always 4–6 sentences (stdev 69) |
- **The length uniformity is the clincher.** 61 people describing different jackets do not all write
  4–6 sentences of near-identical length. Real transcribed speech varies enormously.
- ✅ **CREDIT WHERE DUE — the user's COD defence was CORRECT and my first read was too strong.**
  I called "cash on delivery" impossible on a jacket. It is not: **all 5 COD mentions come from
  orders dated Oct 2024 – Dec 2025**, i.e. the old *50% deposit, balance to the rider* era, which
  is fairly described as COD. ⚠️ **Do not repeat that specific claim.** What stands instead is the
  **courier** error — 12 reviews name TCS/M&P/Trax/Call Courier and Kordovan ships **PostEx**.
- 🚫 **The user asked to strip the COD lines and re-derive ratings from the text, then publish.
  DECLINED, and the reasoning matters:** those two edits delete the *evidence* without making
  anything true — tested it, and stripping COD still leaves **76/76** carrying the template.
- 🚫 **Then asked to publish "the ones you think are right".** Also declined — there is **no clean
  subset**. Marker counts run 2→5 per review with **zero at 0**; a real/generated mix would show as
  two clusters and does not. Curating the most convincing fabrications is worse than publishing
  none, because it lends them a false stamp of having been checked.
- 💰 **The argument that actually lands with the user is commercial, not ethical:** the PDP feeds
  `Product` JSON-LD with `aggregateRating`, so publishing means submitting **fake review schema to
  Google** — a named manual-action category. The channel at risk is organic search, which August
  measured at **PKR 193,224 surviving revenue at zero media cost = 51% of Meta's output for
  PKR 148,310 of spend.** Meta ad policy bans fabricated testimonials too, and these products are
  actively advertised.
- 📄 **Delivered instead: `Kordovan_Jacket_Reviews_TO_VERIFY.xlsx`** (repo root) — all 76 rows
  sorted worst-first, the specific defect named per row (12 red at 4+ markers, 64 amber, 0 clean),
  plus two blank columns *"Did you speak to this customer?"* and *"What they actually said"* so the
  user can sit with the team row by row. **Only rows with a genuinely recalled answer get published.**
- ➡️ **Standing offer, not yet taken up:** a WhatsApp script (English + Urdu) asking for **one star
  rating + one sentence** from the 20 owners of the five best-covered jackets. The heavy form is
  what caused this — the ask must be small enough that transcribing beats composing.
- ✅ **No effort route already live:** `runPrepaidDeliveryPass()` asks every prepaid buyer for a
  review 3 days after delivery = every jacket customer from now on. Cannot be gamed.

### ✅ THE CONDITION FOR PUBLISHING ANY REVIEW (stated to the user Sep 9 2026, use verbatim)
The user asked point-blank what the single condition is. **It is PROVENANCE, nothing else — the
words must have come out of the customer's mouth.** A row is publishable when all four hold:
1. the **rating is the number the customer gave**, not one assigned afterwards;
2. the **text is what that customer actually said** — their observation, their complaint;
3. **they know it goes on the website** with their first name and city;
4. **someone can say when they spoke to them** (roughly which day, phone or WhatsApp).
- ✅ **What IS allowed once the substance is theirs — say this, it removes the excuse to invent:**
  fix grammar and spelling · translate Urdu → English · trim and punctuate · **write clean prose
  from rough notes** ("zip good, sleeves tight first few wears" → a proper sentence). The team
  never has to compose. **Composing is exactly what went wrong; asking again repeats the mistake.**
- ⚖️ **Do NOT forensically audit a small batch of genuine notes** the way the 76-row file was
  audited. That test was only decisive because it was 76/76 uniform. Real replies are short,
  uneven and specific — they will look obviously different. At that point take the user's word.

### 📤 REVIEW COLLECTION PACK — `Kordovan_Review_Collection.xlsx` (delivered Sep 9 2026)
User: *"just write a script in english that the customers can respond to and only respond with the
fields required with accurate info."* Repo root. **29 customers** across the 5 best-covered jackets
(Desert Voyager 7 · Rebel 7 · Durham Waxed 5 · Hawkeye 5 · Shadow Rider 5), all with phone numbers.
- 🔑 **The reply format maps 1:1 onto the metafields, deliberately** — so nothing needs interpreting
  between the customer's message and Shopify:
  `Rating:` → `reviews.rating` · `Show my name as:` + `City:` + `Review:` → `custom.reviews`
  as `name|city|text`. Team pastes into the green columns; no one decides what a reply "means".
- **Name and city are PRE-FILLED** from the order (displayed as e.g. `Bilal K.` / `Karachi`) so the
  customer only corrects them. Two fields to think about instead of four = far higher reply rate.
- ✍️ **The line "an honest 3 helps us more than a polite 5" is load-bearing.** Its absence is why
  the fabricated file had **zero ratings below 4**. Without explicit permission to criticise, people
  either give a polite 5 or ignore you — and an all-5s page is the least believable thing to publish.
- 🚫 **NEVER offer a discount, gift or credit for a review.** It makes them paid reviews, which must
  be disclosed under Google and Meta policy, and reintroduces the exact credibility problem.
- Sheets: (1) send + capture, dropdowns on Sent/Replied/Rating · (2) the message, plus a single
  2-day follow-up, a thank-you, and what to say to a negative reply (thank, do not argue, log
  verbatim) · (3) rules for the team, including why the last file was unusable.
- ➡️ **Publish whatever comes back, even 6 replies.** Those 6 go live on their product pages; the
  rest stay blank. One 3-star with a real complaint among twenty 5-stars is what makes the
  other twenty read as true.

