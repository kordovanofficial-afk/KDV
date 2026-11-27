# KORDOVAN Deep CRO Program (Dec 2026 to Feb 2027)
**Status:** L1 draft for the Founder. Nothing in this file has been changed live (no theme, Shopify, Meta or WhatsApp action).
**Written:** 27 Nov 2026 by Claude through the Alex lens (`.claude/agents/alex.md`).
**Companion files:** `ops/marketing/seo/SEO_6MONTH_PLAN_2026-12_to_2027-05.md` (pillar 1 = conversion; this file is the deep version of that pillar and cross-references its rows instead of repeating them) · `ops/marketing/ads/DEC_2026_STRUCTURE_ALEX.md` · `ops/operations/2026-11-21_lost_orders_postmortem_nov.md`.
**Rules this plan obeys:** free tools only · every live change keeps a before-value, gets read back and needs the right approval (theme deploy = L3 one-deploy yes; customer-facing copy = L2) · CQRO check on all copy (no coins, no Karachi, no "our workshop", jackets top-grain, no policy words, no fake urgency or "only X left", only genuine reviews with provenance) · "Blessed Friday", never the other name.

---

## [Alex lens] The verdict up top
1. **The real problem is the last step, not the traffic.** 679 sessions reached checkout in the last 28 days and only 237 finished (35%). Two of every three people who had their wallet out walked away. Jackets are the extreme: 3 paid jacket orders against 23 abandoned jacket checkouts worth Rs 793k in 24 days.
2. **The math:** the site converts 0.98% (28d). Fixing the checkout step alone (35% → 42% completion) is worth about +45 orders a month at today's traffic, before we touch a single ad. Jackets: every extra completed jacket is ~Rs 17k gross profit. Getting jacket completion from ~12% to ~25% is ~3-6 more jackets a month in peak season.
3. **What I'd do first:** fix the things that are broken or untrue (the cart drawer tells jacket buyers "cash on delivery available"; dead buttons; 5 static stars on cards; homepage reviews with no provenance), then make the price of delivery and the payment terms visible BEFORE checkout, then rescue the abandoned checkouts we already have names and phones for.
4. **What I'd stop:** buying jacket traffic into a checkout that fails 88% of the time; judging CRO on Meta numbers; running "tests" our traffic cannot read.
5. **One thing this week:** one theme deploy (Dec 4) with the bug/honesty fixes in Wave 0, and Ahsan calls every abandoned jacket checkout from the last 7 days.

---

## (a) Funnel baseline (read-only pulls, 27 Nov 2026)
Sources: Shopify ShopifyQL `sessions` and `sales` schemas; Admin GraphQL `orders` (Nov 4-27, 200 orders, 8 internal tests removed → 192) and `abandonedCheckouts` (Nov 2-27, 100 rows); Clarity Data Export API (1 day, 26-27 Nov, 788 sessions; thin); Meta ad set read (7d). All numbers include the Blessed Friday period (Nov 21-30), so they flatter bags and hats.

### Sitewide funnel
| Window | Sessions | Add to cart | Reached checkout | Completed | ATC rate | Checkout reach | Checkout completion | CVR |
|---|---|---|---|---|---|---|---|---|
| **28d (Oct 31-Nov 27)** | 24,278 | 954 | 679 | 237 | 3.93% | 2.80% | **34.9%** | **0.98%** |
| 90d (Aug 29-Nov 27) | 86,818 | 2,264 | 1,477 | 530 | 2.61% | 1.70% | 35.9% | 0.61% |

### By device (28d)
| Device | Sessions | Share | ATC | Checkout | Completed | CVR | Completion |
|---|---|---|---|---|---|---|---|
| Mobile | 20,265 | 83.5% | 830 | 564 | 207 | 1.02% | 36.7% |
| Desktop | 3,934 | 16.2% | 124 | 115 | 30 | 0.76% | 26.1% |
Mobile = 87% of completed orders. Every fix is designed and judged on a phone first.

### By source x device (28d)
| Segment | Sessions | ATC | Checkout | Completed | CVR | Completion |
|---|---|---|---|---|---|---|
| Mobile social (Meta) | 8,583 | 378 | 246 | 112 | 1.30% | 45.5% |
| **Mobile search (organic)** | 7,603 | 251 | 143 | **41** | **0.54%** | **28.7%** |
| Mobile direct | 4,001 | 194 | 168 | 51 | 1.27% | 30.4% |
| Desktop search | 2,410 | 68 | 45 | 19 | 0.79% | 42.2% |
| **Desktop direct** | 1,386 | 51 | 63 | **7** | 0.51% | **11.1%** (anomaly: more checkouts than carts → Buy-it-now or staff/test checkouts; investigate, item 24) |

### Top landing pages (28d)
| Landing page | Sessions | ATC | Checkout | Completed | CVR |
|---|---|---|---|---|---|
| / (home) | 2,867 | 153 | 118 | 55 | 1.92% |
| /products/mocha-mate | 2,389 | 146 | 104 | 53 | 2.22% |
| **/collections/mens-leather-jackets** | **2,170** | 36 | 20 | **0** | **0.00%** |
| /products/…gloves-light-brown | 1,653 | 70 | 46 | 27 | 1.63% |
| /collections/mens-leather-wallets | 1,387 | 91 | 46 | 13 | 0.94% |
| **/blogs/jackets/top-10-leather-jacket-brands** | 1,104 | 9 | 7 | **0** | 0.00% |
| /collections/kdv-wallets | 1,002 | 65 | 41 | 14 | 1.40% |
| /products/clifford hat rustic brown | 707 | 26 | 16 | 11 | 1.56% |
| 10 jacket PDPs as landing pages (Maverick, Desert Voyager, Alonzo, Reacher, Iconic, Spy, Apex, Alison, Rebel, black-jackets coll.) | ~1,890 | ~40 | ~25 | **1** | ~0.05% |

### Orders, payment, loss (Nov 4-27, 192 real orders, Rs 1.085M placed)
| Cut | Orders | Lost (cancelled/refused) | Lost rate | Placed value | Lost value |
|---|---|---|---|---|---|
| All | 192 | 37 | **19%** | 1,085,010 | 152,068 (14%) |
| **COD** | 168 (87.5%) | 36 | **21%** | 825,941 | 149,868 |
| **Paid online (XPay)** | 24 (12.5%) | 1 | **4%** | 259,069 | 2,200 |
| Inside the 9 ad cities | 132 | 18 | 14% | 844,242 | 92,240 |
| **Outside the 9 cities** | 60 | 19 | **32%** | 240,768 | 59,828 |
| Wallets | 103 | 27 | **26%** | 346,025 | 98,958 |
| Gloves | 32 | 4 | 12% | 132,300 | 9,000 |
| Hats | 18 | 2 | 11% | 151,690 | 17,570 |
| Bags | 19 | 1 | 5% | 247,380 | 21,400 |
| Jackets | 3 | 0 | 0% | 134,160 | 0 |
| From Meta (utm/FB/IG) | 96 | 21 | 22% | 423,849 | 94,169 |
| From Google/Bing | 47 | 9 | 19% | 244,333 | 34,489 |
| Direct | 39 | 6 | 15% | 313,635 | 20,660 |
31 COD orders are still pending/in transit, so the final lost rate will move up a little. Cancel reasons: CUSTOMER 25 (Rs 96.8k), FRAUD 7 (staff label for door refusals, see post-mortem), OTHER 3, INVENTORY 2.

### Other baselines
- **AOV (28d):** ~Rs 3,690 net (250 orders / Rs 923k). Free delivery threshold Rs 5,500 = 1.5x AOV.
- **Multi-item orders:** 37 of 200 (18.5%).
- **Returning-customer rate:** Nov 16%, Oct 20%, Sep 16% (May was 28%).
- **Discount codes (28d):** WELCOME10 5 orders, "LAUT AAO" 4 orders (a come-back code; source not confirmed, see item 14), COMEBACK10 1. 240 of 250 orders used no code.
- **Abandoned checkouts with contact details (Nov 2-27):** 100 rows (more pages exist). 23 contain a jacket (Rs 793k; Rs 651k without one 5-jacket bulk cart), ~77 non-jacket (mostly single wallets/gloves at Rs 1.7-4.5k).
- **Clarity, 1 day (26-27 Nov, 688 mobile + 100 desktop sessions; directional only):** mobile average scroll depth **29%** (desktop 38%); **quick-back clicks in 24% of mobile sessions** (wallets collection 46 quick-backs on 64 sessions, jackets collection 35 on 97); dead clicks in 10.6% of mobile sessions (home 29, jackets collection 23, wallets collection 20); **script errors in 8.1% of mobile sessions**; mobile engagement ~47s active.

---

## (b) The leak map: where the money is lost
Monthly figures are per 30 days at current traffic. "Revenue" = placed net revenue; GP ≈ 60-65% of revenue for wallets/gloves/hats, ~61% for jackets (COGS ~11k on ~28k).

| # | Leak | Where | Size (per month) | Evidence | Confidence |
|---|---|---|---|---|---|
| L1 | **Jacket checkout dies at payment** | Jacket PDP → cart drawer → checkout (card/JazzCash only) | **~Rs 650-800k of jacket checkouts abandoned**; 3 completed vs 23 abandoned = ~12% completion | abandonedCheckouts + orders Nov 2-27; jackets collection 0 checkouts on 2,170 sessions | High (size) / Medium (cause: payment wall, surprise, card failures are mixed) |
| L2 | **Non-jacket checkout abandonment** | Checkout shipping/payment step (COD delivery Rs 500 under Rs 5,500 appears only at checkout) | ~77 abandoned carts ≈ **Rs 300k** | abandonedCheckouts; completion 35% sitewide, 28.7% mobile organic | High (size) / Low-Medium (cause) |
| L3 | **COD loss after the order** | Post-purchase (cancel before dispatch, door refusal) | **~Rs 165-190k placed value lost** (19% of orders; wallets 26%; outside-9-cities 32%) | orders Nov 4-27 | High |
| L4 | **Organic mobile traffic does not buy** | Collections, blog, jacket PDPs from Google | Organic CVR 0.54% mobile vs 1.30% Meta mobile; at Meta-like CVR organic would make +~60 orders/month | sessions by source x device | Medium (some organic jacket buyers finish on WhatsApp/direct) |
| L5 | **Collection pages bounce back** | /collections/mens-leather-wallets, kdv-wallets, mens-leather-jackets | wallets collection CVR 0.94% vs Mocha PDP 2.22%; 72% quick-back on wallets collection (1 day) | landing pages + Clarity | Medium |
| L6 | **Mobile buyers never see the proof** | PDP below the fold (reviews, size guide, warranty) | Scroll depth 29% on mobile; proof sits at 60-90% of the page | Clarity + `snippets/pdp-main.liquid` order | Medium |
| L7 | **Small baskets** | Cart drawer / PDP | AOV 3,690 vs free delivery 5,500; 18.5% multi-item | orders | High |
| L8 | **Weak retention** | Post-purchase | Returning 16% (was 28% in May); 13,994 emails barely used | sales by month; briefing | High |
| L9 | **Broken or untrue UI** (trust + dead clicks) | Cart drawer MTO text, order-note link, wishlist heart, card stars, homepage reviews, sticky bar | Not sized; dead clicks 10.6% of mobile sessions, script errors 8.1% | code review + Clarity | High (bugs exist) / Low (rupee size) |

---

## (c) Ranked opportunity list (28 items)
Ranking = expected monthly rupee impact x confidence ÷ effort. Impact ranges are revenue per month at current traffic (GP in brackets where it matters). Levels: L0 analyse · L1 draft · L2 customer-facing (Founder yes) · L3 theme deploy / money / irreversible (Founder yes every time).

### Tier A: do in December (highest impact)

**1. Cart drawer tells jacket buyers "Cash on delivery available" (bug)**
- Hypothesis: the drawer's payment note, "COD available" badge and COD chip are rendered by Liquid at page load. A buyer who lands on a jacket PDP with an empty cart, adds the jacket (AJAX), sees the drawer open with "Cash on delivery available · 7-day returns · COD". Then checkout offers card/JazzCash only. That is the exact surprise the code comments warn about.
- Evidence: `sections/cart-drawer.liquid` lines ~53-88 compute `cart_mto` server-side only; `assets/theme.js` CartDrawer.render() never updates `.cd__fine`, `.cd__trust`, `.cd__pay` (grep: no reference). Jacket completion ~12%.
- Fix: in `CartDrawer.render(cart)`, compute MTO from the cart JSON (pass a per-line flag: add `properties`-free approach = a small `<script id="kv-mto-ids">` list of MTO product IDs rendered from `collections['kdv-jackets']` + footwear, or tag check via `item.product_type` contains "Jacket" plus an MTO ID list) and swap the three blocks. Same message as the Liquid version, with the reason ("each one is cut for a single customer").
- Impact: **Rs 50-110k/month** (2-4 more jackets completed in peak; GP Rs 30-65k). Driver: jacket completion 12% → 18-20%.
- Effort: 2h Claude. Risk: low (copy already approved; logic only). Level: L3 (theme deploy).
- Measure: jacket checkout completion = jacket orders ÷ (jacket orders + jacket abandoned checkouts), weekly. Kill/revert: revert if any non-MTO cart shows the paid-online note (read-back test with a wallet and with a jacket).

**2. Jacket payment rescue path (paid online, more ways to pay, same terms)**
- Hypothesis: jacket buyers want to pay but card/XPay fails or they don't trust a card form; the only methods are card and JazzCash. Full bank transfer / Raast (instant, very common in Pakistan) is a prepaid method but is hidden on MTO carts because it used to carry the dead 50% deposit.
- Evidence: 23 jacket abandons vs 3 completed; 'manual' gateway exists (24 transactions/90d, Rs 453k) = team already closes some orders by hand; October checkouts "died at payment" (archive).
- Fix (three parts, all free): (a) **Founder decision C:** allow "Bank transfer / Raast, full amount" on MTO carts (Shopify manual payment method; Tahir confirms receipt before cutting starts). This is FULL payment, not a deposit; the "50% deposit is dead" rule is untouched. (b) One line under the MTO ship box on the PDP and in the drawer: "Card not going through? WhatsApp us and we'll send a secure payment link or bank details." (`snippets/pdp-main.liquid` MTO block line ~184; drawer MTO note). (c) Shopify checkout: add the same line in the manual payment method's instructions.
- Impact: **Rs 80-170k/month** in Dec-Jan (3-6 jackets; GP Rs 50-105k). Driver: completion 12% → 25%.
- Effort: 1h Claude + Founder setting + Tahir verification SOP. Risk: medium (manual verification load; a paid-but-unverified order must never be cut). Level: L3.
- Measure: jacket orders by gateway; jacket completion rate. Kill/revert: if bank-transfer jacket orders are not paid within 48h in >30% of cases, remove the method (unpaid orders = wasted supplier slots).

**3. Call every abandoned jacket checkout (Ahsan, phone, not WhatsApp)**
- Hypothesis: a Rs 25-34k buyer who typed name + phone into checkout is the hottest lead we have; one human call with "how can I help you finish?" (size, payment link, bank transfer) recovers a share.
- Evidence: 23 jacket abandons in 24 days ≈ 1 per day; cities are mostly real (Rawalpindi, Lahore, Islamabad, Quetta…).
- Fix: daily list (Claude pulls `abandonedCheckouts` with a jacket line from the last 24h → a short file for Ahsan; no PII leaves Shopify/WhatsApp). Script: help first, no discount, no pressure, real lead time ("about 3 weeks"). Kapso number is internal only, so the call comes from the store phone. We never start WhatsApp chats ourselves; if the customer replies on WhatsApp, the 24h window rule applies.
- Impact: **Rs 50-130k/month** (2-5 jackets at 20% recovery). Effort: 15 min/day Ahsan + 5 min Claude. Risk: low (customer gave the number at checkout; keep it courteous, one call, one follow-up). Level: L2 (customer contact; Founder yes once).
- Measure: calls made / reached / recovered order (tag `RECOVERED-CALL`). Kill: stop if recovery <5% after 30 calls.

**4. Show delivery cost and payment terms before checkout (all non-MTO products)**
- Hypothesis: "Shipping calculated at checkout" hides a Rs 500 COD delivery charge on a Rs 2,650 wallet (+19%). People find it at the shipping step and leave. Pay-online delivery is Rs 250, so the honest message also nudges prepaid (loss 4% vs 21%).
- Evidence: checkout completion 35% (mobile organic 28.7%); ~77 non-jacket abandons in 26 days at Rs 1.7-4.5k; COD fee structure in CLAUDE.md (Pay Online 250 or 0 over 5,500; COD 500 or 250 over 5,500).
- Fix: PDP ship line (`snippets/pdp-main.liquid` ~line 186) → "Delivery Rs 250 if you pay online, Rs 500 cash on delivery. Free over Rs 5,500 (Rs 250 COD fee still applies)." Same line in the drawer under the free-delivery bar (`assets/theme.js` renderShip) and in `sections/main-cart.liquid` ("Shipping: calculated at checkout" → the real numbers). Keep the 4 threshold code places in step (CLAUDE.md store rule).
- Impact: **Rs 45-110k/month** (+2 to +5 pts checkout completion on ~600 non-MTO checkout sessions = +12-30 orders) plus fewer COD losses from the prepaid shift. Confidence low-medium: it may also lower ATC slightly; that's why both are measured.
- Effort: 2h. Risk: medium (could cut ATC). Level: L2 copy + L3 deploy.
- Measure: checkout completion (non-MTO) 14d vs prior 14d, guard metric ATC rate; prepaid share. Kill/revert: revert if ATC rate falls >15% relative AND completion doesn't rise ≥3 pts.

**5. Mobile buy box: move proof and terms above the Add to Cart**
- Hypothesis: mobile visitors scroll 29% on average. Reviews, the size guide, warranty and returns sit far below. Bring a compact version into the buy box.
- Evidence: Clarity scroll depth; PDP order in `snippets/pdp-main.liquid` (reviews at line ~411, size guide ~250, guarantee ~455).
- Fix: in the buy box (above variants): (a) real rating line already exists only when reviews exist; add "Read N reviews" jump link; (b) for jackets a "Size guide" link next to the Size label that scrolls to `.kv-size`; (c) under ATC, one 3-icon row that is TRUE per product type (COD/paid online · 7-day returns or lifetime warranty · delivery 2-6 days or about 3 weeks). No new claims.
- Impact: **Rs 40-90k/month** (+5-10% relative ATC on PDP sessions). Confidence low.
- Effort: 3h. Risk: low. Level: L3.
- Measure: PDP-landing ATC rate (Mocha, gloves, Clifford, jacket PDPs) vs control pages (collections) 14d. Kill/revert: revert if PDP ATC rate is not up ≥5% relative after 14 days (and guard: CVR not down).

**6. Jackets: no size pre-selected + "Send us your chest size" next to the selector**
- Hypothesis: `selected_or_first_available_variant` pre-selects the first size, so a jacket can be bought in the wrong size without choosing. On an MTO piece that is a remake (~Rs 11k COGS) or a cancel. A visible "not sure? WhatsApp your chest size" line is the approved SEO-plan test (Founder decision 4, Nov 26).
- Evidence: `snippets/pdp-main.liquid` line 14 + variant buttons with `active` on `option.selected_value`; Clarity rage clicks on jackets collection (3).
- Fix: for `product.type contains 'Jacket'` only: render size buttons without `active`, ATC disabled with "Select your size" until chosen (`assets/theme.js` VariantSelector.updateAvailability). Combine with SEO plan row 6 (size-confidence block).
- Impact: protects GP (each avoided remake ~Rs 11k) + **Rs 20-50k/month** from size-confidence. Effort: 2h. Risk: low. Level: L3.
- Measure: jacket ATC rate; jacket WhatsApp size chats (Ahsan tally); remakes. Revert: if jacket ATC falls >20% and completion doesn't rise.

**7. Abandoned checkout reminder for non-jacket carts (free channel only)**
- Hypothesis: one reminder within 1-4 hours recovers a share of the ~77 small abandons.
- Evidence: 4 orders used "LAUT AAO" in 28d, so some come-back flow already sends a code (source unconfirmed). COMEBACK10 WhatsApp flow is OFF in the PostEx worker.
- Fix: L0 first: find what sends LAUT AAO (Shopify Marketing → Automations). Then **Founder decision D:** Shopify Email "abandoned checkout" automation, ONE message, no discount (WELCOME10 stacks with everything; LAUT AAO must not stack with sale prices). Shopify Email's free allowance is about 10,000 emails/month (verify in admin), so the abandoned flow fits easily. The store-phone WhatsApp bridge stays OFF for this unless the Founder explicitly decides otherwise (it messages people who did not message us).
- Impact: **Rs 15-35k/month** (5-10% of ~Rs 300k). Effort: 1h. Risk: low. Level: L2.
- Measure: orders tagged/attributed to the recovery email; code use. Kill: stop the code if it appears on >30% of recovered orders that would have come back anyway (compare 2 weeks with code vs 2 weeks without).

**8. Homepage "Reviews" marquee has no provenance (honesty P0)**
- Hypothesis: `sections/testimonials.liquid` hardcodes 10 five-star quotes with names (Ahmed Raza, Sara Malik…), cities and "Verified Purchase". The Nov 11 review clean-up removed unsourced product reviews but this homepage section was not covered, and at least one card names a "Full-Grain Bifold Wallet" product we do not sell under that name. If they cannot be traced to a real customer, they break the hard rule and put the Meta account and the brand's "honest ones" position at risk.
- Evidence: file read 27 Nov; `docs/archive` says the marquee was built "per user request, many reviews that scroll"; no source file exists in `ops/marketing/reviews/` for these 10.
- Fix: Founder decision A: (a) if he can name the source of each, keep only those and log provenance; otherwise (b) replace the marquee with up to 10 real reviews pulled from `custom.reviews_verified` (Judge.me verified buyers already on the site), or hide the section until real ones exist. Also fix "Full-Grain" wording on non-jacket cards only if the product really is full-grain.
- Impact: risk removal (Rs 0 direct). Effort: 1h. Risk: none. Level: L2 + L3 deploy.
- Measure: n/a. This is a compliance item: do it in Wave 0.

**9. Product cards: show real ratings, the true terms, and the one fact that sells**
- Hypothesis: cards show "★★★★★" whenever `reviews.rating` exists, whatever the real average (misleading), and give no reason to pick one wallet over another, so people open, bounce back (72% quick-back on the wallets collection), repeat.
- Evidence: `snippets/card-product.liquid` line ~66; Clarity quick-backs; wallets collection CVR 0.94% vs Mocha PDP 2.22%.
- Fix: stars = real avg from `custom.reviews_verified` + count "(12)" or nothing; one line from `custom.subtitle` (already written per product in the SEO pass) under the title; a small chip "Made to order · paid online" on MTO cards, "Cash on delivery" on others.
- Impact: **Rs 15-40k/month** (+10-20% collection CVR on ~4,500 collection sessions). Effort: 2h. Risk: low. Level: L3.
- Measure: collection-landing CVR and quick-back rate (Clarity). Revert: if collection CVR down >15% relative over 14 days.

**10. Jackets collection header strip (fold into SEO rows 5, 8-10)**
- Hypothesis: 2,170 sessions, 36 ATC, 0 orders. The terms (made to order, about 3 weeks, paid online, why) appear only on the PDP. Put them where the shopper decides to click.
- Fix: one strip under the H1 on `sections/main-collection.liquid` when the collection is a jacket collection (handles: mens-leather-jackets, mens-black-leather-jackets, kdv-jackets, winter-collection if jacket-led): "Made to order for you · about 3 weeks to your door · paid online by card, JazzCash or bank transfer · not sure of your size? WhatsApp your chest size". Content = SEO plan row 5 teardown; build/deploy = rows 9-10.
- Impact: counted inside items 1-3 and 6 (jacket completion). Level: L3.

### Tier B: December/January (solid, smaller)

**11. Prepaid nudge (honest, no new discount)**
- Fix: in drawer + PDP "Pay online: delivery Rs 250 instead of Rs 500, and your order ships first" (only if Tahir confirms prepaid orders really are dispatched first; otherwise drop the second half). No discount (L3 money stays untouched).
- Impact: shift prepaid share 12.5% → 18-20%; saves ~2-4 lost orders/month + return freight: **Rs 10-25k/month**. Level: L2/L3. Measure: prepaid share; lost rate. Kill: if prepaid share doesn't move ≥3 pts in 28 days, remove the line (keeps the page short).

**12. Wallet refusal guard: "What arrives" proof on the 5 best-selling wallet PDPs**
- Hypothesis: wallets lose 26% of orders (Rs 99k in 24 days). Impulse buys from ads that don't match expectations get refused. A real phone photo of the wallet in a hand (size reality) + exact dimensions + card count cut the "not what I expected" refusals.
- Fix: Ahsan photos (SEO plan row 54 is Jan 23; pull the Mocha/Elite/Bastion/Plain Bifold/Aristocrat ones forward to Dec 8); add dimensions to `custom.fits`. CQRO: real photo labelled honestly, no "unedited" claims unless true.
- Impact: wallet lost rate 26% → 20% ≈ 6 orders/month ≈ **Rs 20k/month placed + ~Rs 3k freight**. Level: L2. Measure: wallet lost rate at day 14 per product. Revert: n/a (photos stay).

**13. Order confirmation reply rate (ops, feeds CRO)**
- Hypothesis: only ~18% reply to the WhatsApp confirmation; confirmed orders refuse 4%, unconfirmed 7% (post-mortem). Make the reply one keystroke: "Reply 1 to confirm, 2 to change something" in the PostEx worker's confirmation template (next worker version; manual paste deploy).
- Impact: **Rs 10-25k/month** (fewer refusals + earlier cancels = no wasted freight). Effort: 1h + Founder paste. Level: L3 (worker deploy). Measure: reply rate; refusal rate confirmed vs unconfirmed. Revert: previous worker version.

**14. Find and tame the discount sprawl before December**
- L0: list every active code (WELCOME10 combines with everything; LAUT AAO source unknown; PAYONLINE10 redundant). Then one Founder decision: which codes live in December and whether they combine with full prices only. Homepage email block promises "10% off just for saying hello", which is fine at full price but must never stack.
- Impact: margin protection; Level: L0 → L3.

**15. Fix dead clicks and small breakages (Wave 0)**
- Wishlist heart on every card has no JavaScript (dead click) → remove it (or build a free localStorage wishlist later). "+ Add order note / gift message" in the drawer has no handler (dead click) → make it open a textarea that writes `cart.note` via `/cart/update.js` (useful for December gifting) or remove. Duplicate `.cart-drawer-overlay` (layout + section) → remove one.
- Impact: dead clicks 10.6% → <6% of mobile sessions; gift notes help Dec/Eid. **Rs 5-15k/month**. Level: L3.

**16. Sticky mobile ATC bar fixes**
- `kv-pdp__mbar` (z-index 60, bottom 0) sits on top of the WhatsApp float (z-index 50, bottom 24px), so on mobile PDPs the WhatsApp button is mostly hidden (verify on a phone). The bar price never updates on variant change and still says "Add to Cart" on sold-out PDPs.
- Fix: lift the WhatsApp float above the bar on PDPs (`bottom: 84px` when `.kv-pdp__mbar` is shown), update `.mp` in `VariantSelector.updatePrice`, mirror disabled/"Sold out" state. Level: L3. Impact: WhatsApp chats from PDPs (count via `wa.me` click tally in Clarity) + fewer confused taps.

**17. Mobile script errors in 8% of sessions (diagnose before guessing)**
- L0: Clarity API gives counts, not stack traces. Ask the Founder or Ahsan for one phone screen-recording on Chrome Android of Mocha PDP → add → checkout, or use the free PageSpeed Insights / Chrome DevTools console on desktop emulation. Likely sources: app embeds in `content_for_header`, the Clarity tag, the `payment_button` script. Impact unknown; if an error blocks ATC on some phones it is the biggest item on this list. Level: L0.

**18. "Wear it with" bundle on PDPs (upsell, Hormozi "you'll need this too")**
- Hypothesis: the drawer add-ons lifted the average cart ~30% (Nov 9 read). Do the same on the PDP for natural pairs: gloves ↔ cap/hat, belt ↔ wallet, wallet ↔ keychain, jacket ↔ gloves. Real prices, no bundle discount at first (L3 if a discount is ever added; margin floor ≥40% GM / ≥Rs 1,000 GP per line).
- Fix: a 2-item row under the ATC, products from a `custom.pairs_with` product-list metafield (free, native); fallback to the drawer pool.
- Impact: multi-item 18.5% → 22-23% ≈ +8 add-on lines × ~Rs 2.5k = **Rs 20-30k/month**. Level: L3. Measure: multi-item share, AOV. Revert: if PDP ATC rate drops >10% relative.

**19. Fortnightly email to the list (retention, free tier)**
- Hypothesis: the list is the cheapest traffic we own. Two emails this month produced an Rs 72,960 jacket order and a Rs 24k order.
- Fix: one email every 2 weeks, segmented to stay inside the free allowance (~10,000/month; the list is 13,994, so send to purchasers + engaged-90-days first). December themes: winter (gloves, hats, jackets with the real lead time and the order-by date for winter), gifting under Rs 5,500 with real prices. No sale language after Nov 30.
- Impact: **Rs 40-120k/month** (low confidence; 2 data points). Level: L2. Measure: email-attributed orders (utm_source=shopify_email). Kill: unsubscribe rate >1% per send → slow to monthly.

**20. Post-purchase care + cross-sell message (continuity)**
- Fix: in the PostEx worker's delivered thank-you (already live) add the Leather Care Guide link and one "pairs well with" link for the product category (UTM `post_purchase`). Day 30 email via Shopify Email automation "customer purchased" (care tips + pairs). No discount.
- Impact: returning rate 16% → 19-20% over 90 days ≈ **Rs 15-30k/month** by February. Level: L2/L3 (worker deploy). Measure: returning-customer rate monthly; utm post_purchase orders.

**21. Honest claims sweep (CQRO)**
- Generic PDP block says "Hand-Stitched: stitched and finished by hand"; the guarantee says "No questions asked" right after a condition ("if it fails because of how it was made"); brand story and tag meta say "We work full-grain leather by hand in Pakistan" / "cut and hand-stitched" (supplier makes our products; jackets are top-grain). Files: `snippets/pdp-main.liquid` lines ~96-97, 199, 458; `sections/brand-story.liquid` + `templates/index.json` brand_story text; `layout/theme.liquid` tag_description; `sections/main-collection.liquid` line ~148.
- Fix: keep only what the supplier and products can prove ("hand-finished" only if true; "repair or replace if it fails because of how it was made" without "no questions asked"; "handcrafted in Pakistan"). Level: L2 + L3. Impact: trust/compliance; feeds CQRO gate.

**22. Hats pre-order transparency**
- The hat PDPs show 10 per size while the batch is still on its way, and the dispatch note was removed (Founder, Nov 26); the team phones buyers after ordering. Alex: this works only while every call happens. Measure weekly: hat cancels before dispatch; if >15% or the vendor date slips, put an honest line back ("dispatched in about 7-10 days") — Founder decision E. Level: L2.

**23. Sold-out hiding leaves short pages**
- Sold-out cards are skipped inside `paginate … by 24`, so a bag page can show e.g. 14 cards then "Load More". Fix: raise `products_per_page` for bag collections or sort available-first. Level: L3. Impact: small (bags Rs 5-10k/month).

**24. Desktop direct checkout anomaly (L0)**
- 63 checkouts vs 51 carts and 7 completions in 28d. Check whether staff/test checkouts (store PC, Founder testing) are polluting the funnel; if so, exclude by tag or note it in the scorecard. Level: L0.

### Tier C: January-March

**25. Homepage above the fold (SEO rows 34-37)** — category tiles + one proof line. Measure homepage CVR (1.92% today). Don't duplicate; this plan only adds the measurement rule (control = Mocha PDP CVR).
**26. Wallets collection filters/sort (SEO rows 38-39)** — add "type" chips, best-seller sort. Measure collection CVR + quick-back.
**27. Speed: 160 KB of CSS on every page (theme.css 72 KB + home.css 90 KB, both render-blocking)** — after the PSI baseline (SEO row 17, pull it forward to Dec 3), split PDP/collection-only CSS. Level: L3. Impact unknown; do only if mobile LCP >2.5s.
**28. Ramadan/Eid gifting (Feb-Mar)** — gift note working (item 15), "gift under Rs 5,500" and "Eid delivery: order by [real PostEx cut-off date]" banner (no fake urgency), pairs bundles for Eid. Eid ul Fitr ~Mar 10 (moon), so live by Feb 20. Cross-ref SEO rows 64-65, 69.

---

## (d) 90-day test roadmap (Dec 1 - Feb 28)
### What our traffic can honestly read (free tools only, no A/B tool)
- ~12,000 sessions per 14 days. With CVR ~1%, a before/after on the whole site can only see a change of **≥ ~25% relative** in completed-checkout rate with reasonable confidence; ATC rate (~3.9%) can see changes of **≥ ~13-15% relative**. A single page (e.g. 2,000 sessions/28d) can only show big swings.
- So: (1) prefer fixes that are obviously right (bugs, honesty, missing information) and ship them without a "test"; (2) judge real tests on the leading metric with more events (ATC rate, checkout completion), with CVR as the guard; (3) use **14-day before/after with a control page** that did not change (difference-in-differences), because December traffic, the Dec 1 price revert and the winter peak move everything; (4) one change per page per 14 days; (5) write the before-value and the revert rule BEFORE the deploy; (6) never conclude anything from Clarity's 1-3 day window alone.
- Guard windows: no CRO deploy on Dec 1 (price revert) or Dec 2 (URL cleanup); keep 72h quiet after each deploy before reading anything.

### Sequence
| Wave | Dates | What ships | Why now | Read on | Control |
|---|---|---|---|---|---|
| **0: broken/untrue** | build Dec 2, deploy **Dec 4** (uses SEO row 4's slot: Clarity is already installed since Nov 26) | #1 drawer MTO note, #8 homepage reviews (per decision A), #9 card stars (real only), #15 dead clicks, #16 sticky bar/WhatsApp, #21 the two worst claims | Trust bugs, no test needed; jackets peak now | Dec 18 | n/a (bug fixes) |
| **1: jacket path + terms** | Dec 5-10 (= SEO rows 5, 6, 8, 9, 10) | #2 payment rescue (decision C), #6 size select, #10 collection strip, #4 delivery cost line, #5 buy-box proof | Winter peak; biggest rupee items | Dec 24 (14d) | Wallet PDPs for jacket changes; jacket pages for #4 |
| 1b: ops (no theme) | from Dec 1 | #3 jacket abandon calls, #7 recovery email (decision D), #14 code clean-up, #24 anomaly | Starts immediately | weekly | n/a |
| **2: basket + retention** | Dec 15-31 | #18 "wear it with", #11 prepaid nudge (if #4 didn't already move prepaid), #12 wallet real photos, #19 email #1 (Dec 8) and #2 (Dec 22) | Gifting weeks | Jan 7 | Collections |
| **3: organic pages** | Jan 1-31 | #25 homepage (rows 34-37), #26 wallets collection (rows 38-39), #13 worker reply prompt, #20 post-purchase, #27 speed if needed | Post-peak, cleaner reads | Jan 31 / Feb 14 | PDPs |
| **4: Ramadan/Eid** | Feb 1-28 | #28 gift notes/bundles/cut-off banner; jackets wind-down (stop jacket pushes ~Feb 15) | Ramadan starts ~Feb 8, Eid ~Mar 10 | Mar 14 | last Eid fortnight |
| Pivot | Feb 26 (SEO plan quarterly pivot day) | Keep/kill review of every item vs its revert rule | | | |

---

## (e) Weekly CRO scorecard (Monday, inside the SEO Monday read and the ads weekly read; 15 minutes, Haiku can pull it)
| Metric | Source | Baseline (28d to Nov 27) | Target Jan 31 | Target Feb 28 | Red flag |
|---|---|---|---|---|---|
| Sitewide CVR (completed ÷ sessions) | ShopifyQL sessions | 0.98% | 1.15% | 1.25% | < 0.85% two weeks running |
| ATC rate | ShopifyQL | 3.93% | 4.4% | 4.6% | −15% w/w |
| **Checkout completion** (completed ÷ reached) | ShopifyQL | 34.9% | 40% | 42% | < 32% |
| **Jacket checkout completion** (jacket orders ÷ (orders + abandoned)) | Admin orders + abandonedCheckouts | ~12% | 25% | 30% | < 15% after Wave 1 |
| Organic (search) CVR, mobile | ShopifyQL | 0.54% | 0.75% | 0.85% | below baseline |
| Lost-order rate (day-14) | Admin orders | 19% | 16% | ≤ 15% | > 22% |
| Wallet lost rate | Admin orders | 26% | 21% | 20% | > 28% |
| Prepaid share of orders | Admin orders | 12.5% | 17% | 20% | — |
| AOV / multi-item share | ShopifyQL sales / orders | 3,690 / 18.5% | 4,000 / 21% | 4,200 / 23% | AOV < 3,400 |
| Returning-customer rate (month) | ShopifyQL | 16% | 18% | 20% | < 15% |
| Mobile scroll depth / quick-back / dead-click / script-error sessions | Clarity API (1 call, 3 days) | 29% / 24% / 10.6% / 8.1% | 35% / 20% / 6% / 3% | — | script errors > 10% |
| Abandoned jacket checkouts called / recovered | Ahsan tally | 0 / 0 | ≥ 80% called / ≥ 15% recovered | | |
Rule: a metric moves only on Shopify data; Clarity explains "why", never "how much".

---

## (f) What Alex would NOT do
1. **No paid CRO, A/B, review, upsell or popup apps.** Free rule, and our traffic can't read an A/B test anyway.
2. **No fake urgency or scarcity:** no countdown timers outside real end dates, no "only X left", no "X people viewing". Hats pre-order stock must never be sold as "last pieces".
3. **No invented proof:** no review widgets padded with unsourced quotes, no "Verified Purchase" without an order behind it (see item 8).
4. **No discount as the conversion fix.** Discounts are the weakest lever; no new code to "save" abandoned carts, no stacking WELCOME10/LAUT AAO on sale prices. Value and clarity first.
5. **No 50% deposit, no COD on made-to-order.** The fix for jackets is more ways to pay in full plus a human, not weaker terms.
6. **No lowering the Rs 5,500 free-delivery line** to lift CVR; it is the AOV engine (add-ons +30%).
7. **No buying more jacket traffic** (ads) until jacket checkout completion is ≥25% for 7 days.
8. **No exit-intent popups or forced account creation** on mobile.
9. **No redesign.** Quiet Heritage stays; we move information, fix bugs and add proof.
10. **No reading of tests before 14 days, and no more than one change per page per 14 days.**
11. **No unpublishing sold-out PDPs** (SEO), no URL renames beyond the approved Dec 2 batch.
12. **No cold WhatsApp messages** from the Kapso number (internal only) and no template sends; recovery runs on phone calls and free email.

---

## (g) First 10 days (Dec 1-10), merged with the SEO calendar (row numbers = SEO plan rows; add, don't duplicate)
| Date | SEO row (unchanged) | CRO add-on (this plan) | Owner | Level |
|---|---|---|---|---|
| Tue Dec 1 | Row 1: BF price/stock revert check | Start #3: first abandoned-jacket list (last 7 days) to Ahsan via Founder yes; L0 #14 list all live discount codes + find the LAUT AAO sender | Claude, Ahsan | L2 / L0 |
| Wed Dec 2 | Row 2: URL cleanup (no theme deploy today) | Build Wave 0 on the session branch: #1, #9, #15, #16 + #8 option (b) ready; `node --check assets/theme.js`, tag balance; mockup screenshots | Claude | L1 |
| Thu Dec 3 | Row 3: baseline report | Add this file's scorecard (section e) to `reports/2026-12_baseline.md` as the CRO block; pull SEO row 17 (PageSpeed baseline) forward to today for #27; L0 #17 script-error check + #24 desktop anomaly | Claude | L0 |
| Fri Dec 4 | Row 4: Clarity install is ALREADY DONE (deployed Nov 26) → slot freed | **Wave 0 deploy** after the Founder's one-deploy yes (decision A + F); before-values (file checksums) + read-back on a wallet cart and a jacket cart | Claude, Founder | L3 |
| Sat Dec 5 | Row 5: jackets collection teardown | Add the checkout data to the teardown: 23 abandons, 3 orders, gateway split, cities; draft #2 copy + #10 strip copy for CQRO | Claude | L1 |
| Sun Dec 6 | Row 6: jacket size block mockup | Add #6 (no pre-selected size, "Select your size") and #5 buy-box proof row to the same mockup | Claude | L1 |
| Mon Dec 7 | Row 7: weekly read (+ Dec 7 jackets read) | CRO scorecard week 1 (section e) + ads weekly read; Founder brief | Claude | L0 |
| Tue Dec 8 | Row 8: Founder yes on jacket teardown (3 items) | Same ONE message adds CRO decisions B (delivery-cost line), C (bank transfer/Raast full payment on MTO), D (recovery email, no code), E (hats line if cancels >15%); send email #1 (#19) if approved | Founder | L2/L3 |
| Wed Dec 9 | Row 9: build jacket CRO on a branch | Build Wave 1 in the same branch: #2 rescue line, #4 delivery-cost line (4 threshold places stay in step), #5, #6, #10; CQRO check | Claude | L1 |
| Thu Dec 10 | Row 10: deploy jacket CRO (one-deploy yes) | Same deploy carries Wave 1; before-values + read-back; set the Dec 24 read (14d) with the control pages named in section d | Claude, Founder | L3 |

---

## Decisions for the Founder (CRO; bundle into the Dec 8 message, A and F earlier)
- **A. Homepage reviews marquee:** keep only reviews you can source, otherwise replace with real verified reviews from the PDPs. *[Alex lens] Replace now; proof we can't back up is a liability, not an asset.*
- **B. Show delivery costs before checkout** (Rs 250 online / Rs 500 COD, free over Rs 5,500). *[Alex lens] Yes. Surprise costs kill the checkout; the honest line also nudges prepaid, which loses 4% of orders instead of 21%.*
- **C. Made-to-order: add bank transfer / Raast as a FULL payment method** (Tahir verifies before cutting), plus the "card not going through? WhatsApp us" line. *[Alex lens] Yes. Same terms, more doors. The number: jacket completion 12% → 25%.*
- **D. Abandoned checkouts:** Ahsan calls jacket abandons daily; one free Shopify Email reminder for the rest, no discount code. *[Alex lens] Yes. These are the warmest leads we will ever have; a call costs nothing.*
- **E. Hats:** if hat cancels before dispatch pass 15% or the vendor date slips, the honest dispatch line goes back on the page. *[Alex lens] Agree with your call for now; the team call is the control.*
- **F. One theme deploy on Dec 4 for Wave 0** (bug + honesty fixes). *[Alex lens] Yes; these are broken, not experiments.*

## Not verified (say so before quoting)
- The cause split of jacket abandonment (card failure vs payment-method refusal vs price/lead-time) — Shopify gives no gateway error per abandoned checkout. Ahsan's calls (#3) will tell us.
- Whether the WhatsApp float is actually hidden behind the sticky bar on real phones (code says yes; the live site can't be fetched from here).
- What sends the "LAUT AAO" code; whether Shopify's abandoned-checkout automation is on; the current Shopify Email free allowance.
- Clarity is 1 day of data (788 sessions); treat all Clarity numbers as directional.
- Provenance of the 10 homepage reviews (none found in the repo; the Founder may know).
- 31 COD orders still in transit: the 19% lost rate will rise a little.
