# October margin measured, PostEx cash anomaly, margin floor (applied to the decided 11.11 offer)
CFO (Ayesha Naqvi) · Nov 1 2026 · L0 analysis, read-only. Nothing in the store, ads, prices or discounts was changed.
Pulled Nov 1 2026: Shopify Admin GraphQL `orders` (Oct 1–31 PKT, 137 orders, 3 pages, line items + current `inventoryItem.unitCost`), `orders{transactions events}` for the 6 anomaly orders, `products status:active` (173 products, live price + unitCost + stock); Meta `ads_get_ad_entities` account 995683712074843, Oct 1–31 spend. Code read: `tools/postex-worker/worker.js`.
Working files (session-local): `/tmp/claude-0/-home-user-KDV/f5fcf710-68f4-5237-b745-1abc96a75843/scratchpad/fin/`.

---

## Answer
- **Decision:** Retire the 45% planning margin. October's measured all-in online margin is **64.2%** (range 59.7–68.0%), so October left about **PKR 170k** after ads and fixed costs, not 39k. Adopt the margin floor below as binding. Under it, the decided 11.11 offer breaches on **4 sellable lines by %** and **14 sellable lines by rupees when bought alone**; 23 sellable lines have **no unit cost** and cannot be tested.
- **Rupee impact:** October contribution 169,705 (range 82,689 to 249,135). 11.11 margin given away on normal volume ≈ **PKR 9,100** for the 3 days (up to ~22,000 if 3 jackets sell inside the window); break-even needs **1.59x** wallet volume and **1.32x** other volume. PostEx Sync has recorded **PKR 86,616 of cash that was never received** on 6 orders.
- **Confidence:** High on revenue, unit costs and the PostEx diagnosis (every order and transaction read). Medium on delivery/COD/card costs (estimated, no PostEx or XPay statement yet). Low on the store (Mr. Tahir's figure still missing), which is now the widest input.
- **Risk:** The PostEx bug double-records cash on every edited or part-prepaid order and will keep doing it through 11.11. Shopify "paid" status on those orders can hide real money still owed, and the excess makes Shopify cash look 86k richer than the bank.
- **I need from you:** (1) Approve the floor (L3) by **Nov 4**. (2) Decide by **Nov 6** what to do with the breaching lines in section 3 (exclude, add a minimum order, or accept with eyes open). (3) Mr. Tahir: October store sales, the PostEx October settlement statement and the XPay statement by **Nov 4**. (4) Costs for the 23 no-cost lines (list in 3d), or exclude them, by **Nov 6**.

| October 2026 (orders placed Oct 1–31, not cancelled) | PKR | Source |
|---|---|---|
| Product revenue after discounts (116 orders, excl. 2 expired jackets) | 484,047 | GraphQL line items |
| COGS (Shopify unitCost; 49,400 of revenue has no cost, filled at 35%) | −167,490 | GraphQL unitCost |
| **Product gross margin** | **316,557 (65.4%)** | derived |
| Shipping paid by customers | +39,250 | GraphQL shipping lines |
| PostEx delivery, COD cost, card fees, open-cohort haircut | −45,016 | estimates A2–A5 |
| **Online contribution before ads** | **310,791 (64.2%)** | derived |
| Store contribution (300,000 × 60%) | +180,000 | estimate A6 |
| Meta spend October | −96,086 | Meta, measured |
| Fixed costs | −225,000 | CLAUDE.md Oct 31 |
| **Left at month end** | **169,705** (82,689 to 249,135) | derived |

## Assumptions
- **A1. Unit cost = current Shopify `unitCost`.** Wallets include the +150 buffer (written Oct 31), bags carry none. This is today's cost applied to October lines, which is conservative for wallets. Non-wallet, non-bag costs (hats, caps, gloves, belts, jackets 10,000, shoes) were not confirmed by the Founder; jackets show 7,500–10,000 in Shopify by style (11 at 10,000, 18 at 7,500–9,500, Alison blank) against a flat 11,000 in CLAUDE.md *(CQRO fix Nov 1, live unitCost read)*. *Pull:* Mr. Tahir confirms the 10 biggest non-wallet costs.
- **A2. 49,400 of revenue has no cost** (Rastov Backpack 30,800 · Dopp Kit 6,600 · Roxanne Clutch Tan + Red 8,800 as custom lines · Mini Folio 3,200). Filled at 35% cost (range 25–50%). The 3,500 "TCS charges" custom line is treated as a delivery pass-through, not product.
- **A3. Delivery** we pay PostEx: 225 per dispatched order (range 150–300) × 114 dispatched = 25,650. *Pull:* PostEx October invoice.
- **A4. COD cost** 3% of COD cash (range 2.5–3.5%, CLAUDE.md Sep 15 "measured cost of COD ≈ 2.5–3.5% of cart") × 343,630 = 10,309. **Card/XPay fee** 2.5% (range 2–3.5%) × 179,667 = 4,492. *Pull:* XPay statement.
- **A5. Open cohort:** 17 COD orders (64,650 product revenue) not yet delivered. Haircut at the 9.9% after-dispatch refusal rate (CLAUDE.md Aug 20): margin lost + return leg = 4,565 (range 2,242–7,107). *Test:* re-pull Nov 15.
- **A6. Store:** 300,000 (250–350k, CLAUDE.md Oct 31) at 60% margin (range 50–66%): same list prices, no delivery or COD cost, haircut for in-store bargaining. *Pull:* Mr. Tahir's October total.
- **A7. Not in this P&L:** packaging, Shopify plan and apps, phones, the Founder's household draw, tax.

## Detail

### 1. Measured October margin (formulas)
- Base: 137 orders placed Oct 1–31 PKT → 119 not cancelled → minus 2 EXPIRED unpaid jackets (KDV#22830, 22839, 52,200) and 1 fully refunded (KDV#22857, 0 current qty) → **116 orders**.
- Line revenue = Σ currentQuantity × discountedUnitPriceAfterAllDiscounts = **487,547**; minus the 3,500 TCS line = **484,047**. It equals current subtotals on every order (checked, 0 mismatches).
- Reconciles to ShopifyQL (CRO, Nov 1): net 514,947.9 − 52,200 expired + 27,199.1 Sep reversals booked in October = 489,947; mine is 487,547. The 2,400 gap is the same 2,400 gap between ShopifyQL gross (748,170) and the CRO's line-item gross (745,770).
- COGS covered: 434,647 of revenue carries a cost; cost 150,200 → cost share 34.6%. Uncovered 49,400 × 35% = 17,290. Total 167,490. Gross margin (484,047 − 167,490) ÷ 484,047 = **65.4%**.
- By category (revenue / cost): Smart Wallet 80,500 / 23,350 · Bifold Wallet 62,420 / 21,300 · Hat 53,490 / 20,500 · Slim Wallet 51,877 / 16,200 · Laptop Bag 51,300 / 22,200 · Cap 31,005 / 10,850 · Belt 30,300 / 9,900 · Gloves 23,205 / 7,800 · Women's Wallet 21,600 / 7,450. **Wallets 230,047 at 31.9% cost share; everything else 245,200 at 37.5%.**
- Contribution = 484,047 − 167,490 + 39,250 − 25,650 − 10,309 − 4,492 − 4,565 = **310,791 = 64.2%**. Low (all costs high) 288,775 = 59.7%; high 329,221 = 68.0%.
- **Why 45% was wrong:** it was a planning number that bundled pre-dispatch cancellations into margin. Measured by cohort, cancelled orders cost almost nothing (87% die before dispatch, CRO D2), so they belong in the lost-order rate (25.3%), not in the margin. Using both 45% and a 30.7% reversal rate double-counted the same loss.

### 2. October P&L redone
- Work sample (45% on 511,748 ShopifyQL net): online 230,287 · store 135,000 · ads −101,000 (estimate) · fixed −225,000 → 39,287.
- Now: online **310,791** (cohort basis, expired jackets out) · store **180,000** · ads **−96,086 (measured)** · fixed **−225,000** → **169,705**.
- Low: 288,775 + 250,000 × 50% − 96,086 − 235,000 = **82,689**. High: 329,221 + 350,000 × 66% − 96,086 − 215,000 = **249,135**.
- The swing input is now **the store** (125,000 to 231,000, a 106k range), not the online margin (40k range). Mr. Tahir's figure closes most of it.
- Real ROAS check (directional only): Meta-paid orders by last visit 174,697 gross, 55,300 cancelled (CRO D2) → 119,397 surviving ÷ 96,086 = **1.24x** on last-click Shopify revenue. Break-even at the measured 64.2% is 1 ÷ 0.642 = **1.56x**. Last-click undercounts Meta, so this is a floor, not the real ROAS; the CRO's ad-set view is the one to grade on.

### 3. PostEx Sync anomaly: it is a sync bug, not real money

| Order | Real money in | Shopify "received" | Phantom | What happened |
|---|---|---|---|---|
| KDV#22898 | 28,600 card − 400 refund = **28,200** | 85,400 | **56,800** | Fully prepaid by Visa. Order edited twice. Sync then captured 56,800 COD that PostEx never collected |
| KDV#22890 | 8,951 bank advance + 8,899 COD = **17,850** | 29,249 | **11,399** | Poll captured 8,899 (correct), webhook captured 20,350 three minutes later |
| KDV#22863 | 4,400 bank advance + 9,100 COD = **13,500** | 22,600 | **9,100** | Poll captured 9,100 (correct), webhook captured 13,500 three minutes later |
| KDV#22906 | **4,570** (current total) | 8,890 | **4,320** | One capture at the pre-edit total |
| KDV#22929 | 1,749 XPay + ~651 COD = **2,400** | 5,898 | **3,498** | Part-prepaid, then edited; webhook captured the full 4,149 |
| KDV#22862 | **1,749** (current total) | 3,248 | **1,499** | One capture at the pre-edit total |
| **Total** | | | **86,616** | = the CRO's figure exactly |

- **Cause (two defects in `worker.js`):**
  1. **Wrong amount.** The webhook path (`handleWebhook`, ~line 1454/1482) uses `payload.invoicePayment || payload.amount || order.total_price`. The PostEx webhook evidently carries no amount, so it falls back to `order.total_price`, which on these orders is the total before staff edits and ignores any card or bank prepayment. The hourly poll (~line 1561) reads `invoicePayment` from PostEx and records the right figure (9,100; 8,899). Tell-tale: webhook notes say `Ref: ` (blank); poll notes say `Ref: KDV#…`.
  2. **Weak "already paid" guard.** Both paths skip only when `financial_status === 'paid'`. After a first partial capture the order is `partially_paid`; a card order with a refund is `partially_refunded`. Both pass the guard, so a second capture lands (22863, 22890), and a fully prepaid card order gets a COD capture (22898).
- **Effect on revenue:** none. Shopify gross and net sales are built from line items, so ShopifyQL sales and my margin are unaffected.
- **Effect on cash:** Shopify's "cash collected" rung is overstated by **86,616 for October**. Real cash on these 6 orders = 68,269. Two bank advances (4,400 + 8,951 = 13,351) never reached Shopify as transactions at all; the bug happens to cover them, which is why it looked like plausible money.
- **Risk:** (a) anyone refunding the "overpayment" on 22898 through XPay could send real money to the customer that was never received from them; (b) "PAID" status can mask a real balance still owed; (c) the pattern repeats on every edited or part-prepaid order, and 11.11 brings more edits.
- **Owner: CTO seat (CEO until hired), L2 deploy.** Fix the amount (use PostEx `invoicePayment`, else call `/track-order`, else do not capture) and the guard (skip when `total_outstanding ≤ 0` or status is paid / partially_refunded / refunded; never capture more than outstanding). Clean-up of the 6 records is a Founder decision (L3: it changes financial records). **Pull for the CTO:** `orders{totalOutstandingSet}` Aug–Oct to size earlier months. **Rule from today:** the cash rung of the revenue ladder comes from the PostEx settlement statement, not Shopify "received".

### 4. The margin floor (proposed, binding once approved)
**Standard floor, every promotion on live stock.** After the discount, each order must keep:
- **contribution ≥ 40% of the discounted price**, and
- **contribution ≥ PKR 1,000 per order**,

where contribution = discounted price − unit cost − 3% payment/COD cost − delivery we pay (225 when the order is free-delivery, i.e. ≥ 5,500; 0 below that, because the customer pays 250–500).

Why these numbers:
- October's measured all-in margin is 64.2%. Ads took 96,086 ÷ 484,047 = **19.9%** of online product revenue. 40% leaves a promoted order paying for its own ads about twice over (break-even real ROAS 1 ÷ 0.40 = 2.5x), with ~20% still going to fixed costs.
- PKR 1,000 is about one Meta purchase at the account's best ad set (Retarget CPA 969, Oct 11–24, CLAUDE.md). An order that keeps less than that loses money if Meta bought it, and 11.11 traffic will be ad-pushed.

**Clearance floor, dead stock only (sunk cost):** discounted price ≥ unit cost + delivery + 3%, i.e. the sale must return at least the cash we paid. This values the stock at what it can still earn, not at what it cost. Below that = a Founder decision, shown both ways.

### 5. Applied to the decided 11.11 offer (25% wallets, 15% everything else, Nov 10–12)
Basis: live price and unitCost (Nov 1), single unit bought alone. "Wallets" = product types containing "Wallet" plus Card Holder (Bellezza and Nova are type Women's Wallet, so they take 25%). ⚠️ The real boundary is whatever collection the automatic discount targets; the CRO/COO must confirm it matches this list.

**5a. Breach the 40% floor (sellable now)**: exclusion candidates
| Product | Price → sale | Cost | Contribution | Stock |
|---|---|---|---|---|
| The Nova // Weaved Leather Wallet & Clutch | 4,200 → 3,150 (−25%) | 1,950 | 1,106 (35.1%) | 5 |
| Elite Laptop Bag | 12,000 → 10,200 (−15%) | 6,000 | 3,669 (36.0%) | 5 |
| The City Backpack by Kordovan // Rustic Red | 15,500 → 13,175 (−15%) | 7,500 | 5,055 (38.4%) | 1 |
| The Executive Leather Briefcase (Black variant) | 28,600 → 24,310 (−15%) | 14,000 | 9,356 (38.5%) | 1 |
Not sellable now (0 stock, DENY), would breach if restocked: The Armour (39.2%), Gift Box 4 Pieces Set (−56, below cost).

**5b. Pass 40% but keep < PKR 1,000 when bought alone (sellable now)**
| Product | Sale price | Cost | Contribution | Stock |
|---|---|---|---|---|
| Midtown Lite wallet | 1,124 | 550 | 541 | 3 |
| Sheppard wallet | 1,124 | 550 | 541 | 1 |
| The Money Clip | 1,463 | 800 | 619 | 18 |
| Rigor Lite | 1,124 | 450 | 641 | 7 |
| Leather Key Chain with Belt Loop | 978 | 250 | 698 | 30 |
| The Seamless card wallet | 1,500 | 700 | 755 | 19 |
| The Bastion | 1,875 | 950 | 869 | 65 |
| Baseball Cap // Unisex | 1,658 | 650 | 958 | 20 |
| Winter Gloves Men's Black / Men's Brown / Women's Dark Red (3 lines) | 1,658 | 650 | 958 | 56 / 45 / 14 |
| Premium Leather Lipstick Case | 1,700 | 675 | 974 | 2 |
| The Ripper Case | 1,785 | 750 | 981 | 17 |
| Plain Bifold | 1,800 | 750 | 996 | 8 |
- Midtown, Sheppard and the keychain are under 1,000 even at **full** price, so they never cover a Meta purchase alone. *(CQRO fix Nov 1: Money Clip removed; at full price 1,950 − 800 − 58.5 = 1,091.5, above 1,000. Live price read Nov 1.)*
- **Free alternative to excluding them:** a minimum order on the automatic discounts. The weakest line keeps 48.1% at sale, so 1,000 ÷ 0.481 = **PKR 2,100 discounted subtotal** clears every row in 5b (two cheap wallets, or one wallet plus gloves). CQRO to test on a draft cart whether Shopify's minimum counts only the discounted items.

**5c. Pass both** (99 of 142 sellable price lines), including every jacket and shoe at 15% (e.g. Iconic 22,000 → 18,700, contribution 7,914 = 42.3%) and the CEO bag (35,700, 14,404 = 40.3%, just over).

**5d. No unit cost, cannot be tested (sellable now, 23 lines).** Supply costs or exclude:
The Saffire Belt · Women's Casual Cap // Newsboy · The Case by Kordovan · Natural Milled Leather Dopp Kit · The Gentlemans' Duffle · Mini Leather Folio · Leather Tissue Box Rectangle · Mini Watch/Cufflink/Jewelry Box · Trinity Jewlery Case · Zimmer Leather Keychain · Leather Lanyard · Natural Milled slim laptop bag (3 of 4 variants) · The Corporate Office laptop bag · The Documate Office Bag · The Maverik Laptop Bag · The Millennial · The Staton office/laptop bag · The Executive Leather Briefcase (Brown, Coffee Brown) · Millard Office Bag · Voyager Suitcase Trolley Bag · The Beyond Backpack · The Rastov Backpack · Alison women's jacket and both Salemanco Brogues (MTO, 0 stock, CONTINUE).
⚠️ **The Maverik Laptop Bag was the #1 product by 90-day net (274,275, data pack Oct 31) and has no cost in Shopify.** Get this one before Nov 10.

**5e. Expected margin given away (Nov 10–12)**
- Normal 3-day volume = October run-rate ÷ 31 × 3: wallets 230,047 → **22,263**; other products 245,200 → **23,729**.
- Given away on normal volume: 22,263 × 25% + 23,729 × 15% = 5,566 + 3,559 = **9,125**.
- Margin per rupee of list: wallets 0.651 full → (0.75 × 0.97) − 0.319 = 0.408 at sale; others 0.595 → 0.449. Break-even lift: 0.651 ÷ 0.408 = **1.59x** wallets; 0.595 ÷ 0.449 = **1.32x** others.
- High case: November jacket season. Each jacket sold at 15% gives away 28,066 × 15% = 4,210; three in the window add 12,630, total about **21,800**.
- Last year's evidence (CRO, Nov 1): wallets sold ~0.98x at constant prices under a ~20% cut; the store total ran 1.36x on jackets and bags. On that pattern, wallets lose about 5,400 of margin and the rest roughly break even (1.36x vs 1.32x needed): **net about −5,000 for the window**. Small, and the decision stands; this is the price of the event.
- Stacking: two automatic discounts set not to combine also block WELCOME10 (CRO B4). Any order showing more than 25% off a wallet means stacking: pause.

### 6. Black Friday dead-bag clearance (77 bags, 560,800 at cost)
| Bag | List | Cost | Units | Cash floor (max off) | Standard floor (max off) | At 40% off: price / contribution |
|---|---|---|---|---|---|---|
| Cabin Trolley | 42,000 | 17,000 | 11 | 17,758 (57.7%) | 30,219 (28.0%) | 25,200 / 7,219 |
| CEO bag | 42,000 | 20,000 | 5 | 20,851 (50.4%) | 35,482 (15.5%) | 25,200 / 4,219 |
| Master's | 10,800 | 4,900 | 16 | 5,052 (53.2%) | 8,991 (16.7%) | 6,480 / 1,161 |
| Bella Duff | 10,500 | 3,500 | 13 | 3,608 (65.6%) | 6,535 (37.8%) | 6,300 / 2,386 |
| Forester | 34,500 | 11,500 | 3 | 12,088 (65.0%) | 20,570 (40.4%) | 20,700 / 8,354 |
| Gridle | 15,500 | 5,000 | 6 | 5,155 (66.7%) | 9,167 (40.9%) | 9,300 / 3,796 |
| Bellezza | 6,500 | 2,350 | 12 | 2,423 (62.7%) | 4,123 (36.6%) | 3,900 / 1,433 |
| Branson | 38,000 | 11,500 | 2 | 12,088 (68.2%) | 20,570 (45.9%) | 22,800 / 10,391 |
| Venture | 8,600 | 3,800 | 9 | 3,918 (54.4%) | 7,061 (17.9%) | 5,160 / 1,205 |
- Formulas: cash floor = (cost + 225) ÷ 0.97 (cost ÷ 0.97 when the price falls under 5,500 and the customer pays delivery). Standard floor = (cost + 225) ÷ (0.97 − 0.40).
- **These bags take the clearance floor, not the standard one.** They are sunk; under the standard floor the CEO bag could not go past 15% off, which keeps 100,000 of cash on a shelf.
- The planned ladder (25% Nov 10–26, 40% Black Friday Nov 27 – Dec 6) stays **above the cash floor on every line**. All 77 sold at 40% off = **845,520 cash**, contribution **246,754** over cost.
- At 11.11 these bags get only 15% (Bellezza 25%, as a Women's Wallet type): all above both floors, and the CEO bag just clears 40% (40.3%).
- Master's (16 units) and Venture (9) keep only ~1,200 each at 40% off, close to the PKR 1,000 order minimum. Do not go deeper on those two without a yes.

---

## One idea nobody asked for: stop 11.11 creating the PostEx bug
Every 11.11 order a staff member edits (size swap, colour swap, an extra item) is a new chance for the webhook to capture the pre-edit total. Until the CTO fix ships, a **free staff rule**: on any edited COD order, Mr. Tahir checks "received" against current total the day after delivery and flags any negative outstanding. In October that would have caught 86,616 of false cash in six checks of under a minute each. It costs nothing and protects the weekly cash forecast.
