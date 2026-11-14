# Per-product CPA ceilings, refreshed with Aug–Oct 2026 data
CFO (Ayesha Naqvi) · Nov 14 2026 · L0 analysis, read-only. Nothing in the store or the ads was changed.
Pulled Nov 14 2026: Shopify Admin GraphQL (variant `price` + `inventoryItem.unitCost`; orders by SKU Aug 1–Oct 31 with cancel status + `fulfillments.trackingInfo`; all orders Oct 31–Nov 13 with last-visit UTMs), ShopifyQL `sales` by product (Aug 1–Oct 31 and Nov 1 2025–Oct 31 2026, all Online Store), Meta `ads_get_ad_entities` account 995683712074843 (ad level: Nov 13–14, last 7d, last 14d).

## Answer
- **Decision:** Replace the July ceilings with the column "Ceiling (central)" below for the Nov 17 weekly read. **Mocha Mate rises from ~990 to ~1,450** (lower COD loss since WhatsApp confirmation, measured on 105 orders). **No running ad is above 1.3× its new ceiling.** Retarget (BOF, catalogue) sits just above its central ceiling (1,549 vs ~1,500, 1.03×), inside its range, so it is a watch item, not a stop.
- **Rupee impact:** H1 Mocha has ~350 per placed order of headroom (1,100 Shopify CPA vs 1,458). On its 1,300/day that is the difference between "break-even at best" (the July read) and roughly 1,300 ÷ 1,100 × 358 ≈ **PKR 420/day** of margin above break-even, before fixed costs.
- **Confidence:** High on prices and unit costs (live, Nov 14) and on Mocha + gloves loss rates (order-level cohort, refusal test applied). Medium on the other wallets (ShopifyQL unit loss, thin n on several). Low on jackets (placed→paid share) and on delivery/RTO rupee costs (no PostEx statement yet).
- **Risk:** The ceilings are at REGULAR prices. During any sale they fall (Mocha at 2,400 → ~920). Plain Bifold dropped from ~1,500 to ~810 because its Aug–Oct loss rate was 45%: do not run it cold.
- **I need from you:** Mr. Tahir: the PostEx October invoice (forward + return charge per parcel) by **Nov 17**; it replaces A2/A3 and moves every ceiling by up to ±60.

| Product | Price | COGS | GP per kept order | Lost-order rate used (n, window) | **Ceiling (central)** | Range | July |
|---|---|---|---|---|---|---|---|
| Mocha Mate (H1, MOF ads) | 3,200 | 950 | 2,154 | 30.5% (32/105 orders, Aug–Oct; 8.6% doorstep refusals) | **1,460** | 1,200–1,460 | ~990 |
| Gloves (W01) | 1,950 | 650 | 1,242 | 25.0% (9/36 orders, Aug–Oct; 0 refusals) | **930** (Founder rule stays 1,000) | 890–1,180 | 1,000 |
| BOF catalogue mix (Retarget) | ~3,300 basket | 34.6% cost share | 2,059 | 25.3% (October lost-order rate) | **1,500** | 1,340–2,160 | n/a |
| Executive belt | 3,300 | 1,100 | 2,101 | 18.0% (9/50 units, 12m) | **1,700** | 1,540–1,700 | new |
| Jacket (MTO, paid online) | ~28,066 | 11,000 | 16,139 | 52% placed→not kept (13/25 units, Aug–Oct); 0 refusals | **7,750 per placed** · 16,140 per paid | 7,750–16,140 | 7,100 / 17,066 |
| Aristocrat | 4,200 | 1,250 | 2,824 | 12.2% (6/49 units, 12m) | **2,460** | 2,180–2,460 | ~3,000 |
| Bronco | 6,200 | 1,650 | 4,139 | 33.3% (11/33 units, 12m) | **2,720** | 2,720–3,070 | ~2,900 |
| Truckkr | 3,800 | 1,150 | 2,536 | 25.0% (15/60 units, 12m; 0 sold Aug–Oct) | **1,870** | 1,870–1,950 | ~2,100 |
| Shelby & Thomas | 2,800 | 1,000 | 1,716 | 16.7% (11/66 units, 12m) | **1,410** | 1,410–1,450 | ~1,500 |
| Plain Bifold | 2,400 | 750 | 1,578 | 45.0% (9/20 units, Aug–Oct) | **810** | 810–1,140 | ~1,500 |
| KODO | 2,300 | 550 | 1,681 | 35.0% (21/60 units, 12m) | **1,050** | 1,040–1,050 | ~1,100 |
| Kodo Vertical 2.0 (0 in stock) | 2,450 | 600 | 1,777 | 38.9% (7/18 units, Aug–Oct) | **1,040** | 930–1,040 | ~970 |
| Bastion | 2,500 | 950 | 1,475 | 52.0% (13/25 units, Aug–Oct) | **640** | 640–700 | ~720 |
| Rigor Lite | 1,499 | 450 | 1,004 | 45.5% (20/44 units, Aug–Oct) | **490** | 490–530 | ~460 |

(Table is 14 rows because the brief asked for all 14 lines; the first 5 are the ones ads run on now.)

**Sources and dates:** Price and COGS = live Shopify `price` / `unitCost`, read Nov 14 2026 (no compare-at on any of these, so 11.11 is reverted). Wallet costs already include the +150 buffer (not added again); belt, gloves and jacket costs carry none. Jacket price = mean of 28 men's jackets and COGS 11,000 (archive, Aug 20 2026; Shopify shows 7,500–10,000 by style, so 11,000 is conservative). Loss rates: Mocha and gloves from order-level GraphQL (Nov 14 pull); others from ShopifyQL `quantity_returned ÷ quantity_ordered` (Nov 14 pull). BOF basket = Meta last-visit orders Nov 1–8 (CLAUDE.md) and the 10 kept Retarget orders Oct 31–Nov 13 (avg 3,185, partly at 11.11 prices); cost share 34.6% = October measured (`2026-11-01_margin_and_cash.md`).

## Assumptions
- **A1. Formula.** Ceiling = (1 − L) × GP − L × 28% × RTO cost, where GP = 0.97 × price − COGS (− 225 if price ≥ 5,500), L = lost-order rate (placed → not kept, pre-dispatch cancels included because the ad already paid for them), 28% = share of lost orders that were dispatched (Mocha cohort 9/32; Aug store-wide 20/84 = 24%). One unit per order (measured 1.00–1.06 for wallets; gloves 1.15, shown in its range). *Replaces it:* per-product order-level pull for every line, same as Mocha.
- **A2. Delivery.** Below 5,500 the customer pays 250 (online) or 500 (COD), which covers our PostEx charge, so 0 net (conservative: COD leaves ~+275). At ≥ 5,500 we pay ~225. *Pull:* PostEx October invoice.
- **A3. RTO cost** 450 per refused parcel, forward + return (range 250–500; `ops/WHATSAPP_PLAN.md` 400–500, July playbook 250). The product comes back to stock and is resold. *Pull:* PostEx invoice.
- **A4. Payment cost** 3% of price (COD 2.5–3.5%, card 2–3.5%; Nov 1 margin note A4). *Pull:* XPay statement.
- **A5. Window rule.** Aug–Oct used where the product had ≥ 15 units ordered; otherwise 12 months (Nov 2025–Oct 2026), with the other window as the range end. ShopifyQL books returns on the return date, so a few July orders' returns sit in August and some late-October returns are missing; this roughly nets out.
- **A6. Jackets.** Paid 100% online, so no refusals. "Not kept" = unpaid/expired or cancelled; Aug–Oct still includes the deposit era (before Sep 4). *Pull:* Nov 1–30 jacket orders placed vs paid; if ≥ 80% now pay, the per-placed ceiling rises to ~12,900.
- **A7. Cohort age.** Every Aug–Oct order is ≥ 14 days old on Nov 14, past the ~day 8 point where ~47% of cancellations land. KDV#22936 (Mocha, fulfilled, still PENDING) is counted as kept.

## Detail
### Mocha Mate (the ad that matters)
- Cohort: 105 orders with SKU MM001 placed Aug 1–Oct 31 PKT. Kept 73. Cancelled 32: 9 dispatched then cancelled (tracking present = refusals: KDV#22473, 22479, 22487, 22495, 22596, 22651, 22652, 22669, 22941) and 23 before dispatch (4 INVENTORY, 1 STAFF cancel 2 hours after booking, KDV#22939, not a refusal).
- GP = 3,200 × 0.97 − 950 = 3,104 − 950 = **2,154**.
- Central: 73/105 = 0.695 × 2,154 = 1,498; minus 9/105 = 0.0857 × 450 = 39 → **1,459**.
- Low (12 months, 118/282 lost = 41.8%): 0.582 × 2,154 = 1,254 − 0.418 × 126 = 53 → **1,201**.
- Why it rose from ~990: the July figure used a 49.2% loss rate (pre-WhatsApp confirmation) and old COGS; Aug–Oct is 30.5%.

### H1 Mocha (ad `120255717749990428` "Comparison") against the new ceiling
| Window | Spend | Meta purchases (Meta CPA) | Shopify placed, utm `h1_comparison` | Shopify CPA | vs 1,459 |
|---|---|---|---|---|---|
| Nov 13–14 | 1,893 | 4 (473) | 2 distinct (KDV#23096, 23100; 23097 was a 1-minute duplicate re-placed as 23098) | 947 (631 if 3 counted) | 0.65× (0.43×) |
| 14 days to Nov 13 | 19,801 | 22 (900) | 18 (2 cancelled pre-dispatch) | **1,100** | **0.75×** |
- **Below the ceiling.** Do not convert with 2.05x: that is a REVENUE overstatement (Meta also claims other products and duplicates). On counts, Meta claimed 22 vs 18 placed in Shopify = 1.22x. Applying 2.05x to the 14-day Meta CPA (900 × 2.05 = 1,845) would wrongly put H1 above the ceiling.
- The ceiling is per PLACED order and already nets out the 30.5% loss, so the Shopify placed CPA is the right comparison. Last-click undercounts Meta slightly, so 1,100 is a cautious figure.
- Caveat: during 11.11 (Nov 8–12) Mocha sold at 2,400, where the ceiling is 0.695 × (2,328 − 950) − 39 = **919**. H1 at ~1,100 was above that for those five days; at the regular 3,200 it is back below.
- Under section 4 rules: 0.75× is between "hold" and the 0.7× scale line. Hold; re-read on the Monday 7-day table.

### Other ads now running
- **Retarget / BOF catalogue** (ad `120228534677040428`): 14 days 17,036 spend; Shopify last-visit `Facebook_UA` orders = 11 placed (1 cancelled) → **1,549**. Central ceiling 3,300 × 0.747 × 0.624 − 40 = **1,498**; low 3,185 × 0.695 × 0.624 − 40 = 1,341; high (October store mix, 3,533 kept revenue per placed order) 3,533 × 0.624 − 45 = 2,160. **1.03× central**: watch, not stop (stop line 1.3×). Meta claims 24 purchases (CPA 710).
- **W01 gloves (new TOF ad `120256055946350428`)**: 905 spent since Nov 13, 0 Meta purchases. Under 1× ceiling: too early. The old W01 drove 11 Shopify orders Oct 31–Nov 13.
- **MOF Mocha trust ad (`120256055946470428`)**: 790 spent, 0 purchases. Under 1× ceiling: too early.

### Gloves
- 36 orders with a glove SKU Aug 1–Oct 31; 9 cancelled, all before dispatch (0 refusals); 27 kept with 31 glove units.
- GP = 1,950 × 0.97 − 650 = **1,242**. Central 0.75 × 1,242 = **931**. With measured 1.15 units per kept order: 1,071. Gloves-only orders (19, 1 cancelled): 0.947 × 1,242 = **1,176**. 12-month ShopifyQL (80/308 = 26%): 0.74 × 1,242 − 33 = **886**.
- The Founder's 1,000 sits inside 886–1,176. Keep it.

### Executive belt
- GP = 3,300 × 0.97 − 1,100 = **2,101**. 12m: 0.82 × 2,101 − 0.18 × 126 = 1,723 − 23 = **1,700**. Aug–Oct (3/12): 0.75 × 2,101 − 32 = 1,544.

### Jacket
- Per paid order: 28,066 − 11,000 − 2.5% card fee (702) − 225 delivery = **16,139**.
- Per placed order: Aug–Oct jacket units 25 ordered, 13 reversed → 48% kept: 0.48 × 16,139 = **7,747**.

### Wallet lines (formula applied)
- Aristocrat: 0.878 × 2,824 − 0.122 × 126 = 2,479 − 15 = **2,464**; Aug–Oct 2/9: 0.78 × 2,824 − 28 = 2,175.
- Bronco (≥ 5,500, −225): 6,014 − 1,650 − 225 = 4,139; 0.667 × 4,139 − 42 = **2,719**; Aug–Oct 1/4: 0.75 × 4,139 − 32 = 3,072.
- Truckkr: 0.75 × 2,536 − 32 = **1,870**; July 22.1%: 0.779 × 2,536 − 28 = 1,948.
- Shelby: 0.833 × 1,716 − 21 = **1,408**; Aug–Oct 2/14: 0.857 × 1,716 − 18 = 1,453.
- Plain Bifold: 0.55 × 1,578 − 57 = **811**; 12m 25.8%: 0.742 × 1,578 − 33 = 1,138.
- KODO: 0.65 × 1,681 − 44 = **1,049**; Aug–Oct 5/14: 0.643 × 1,681 − 45 = 1,036.
- Kodo Vertical: 0.611 × 1,777 − 49 = **1,036**; 12m 44.4%: 0.556 × 1,777 − 56 = 932.
- Bastion: 0.48 × 1,475 − 66 = **642**; 12m 48.4%: 0.516 × 1,475 − 61 = 700.
- Rigor Lite: 0.545 × 1,004 − 57 = **490**; 12m 42.1%: 0.579 × 1,004 − 53 = 528.

## One idea nobody asked for: Truckkr is the best cold wallet we are not advertising
Truckkr has the 4th-highest ceiling (~1,870) and the 2nd-lowest loss rate among volume wallets (25%), **48 units in stock**, and **0 online sales Aug–Oct** (ShopifyQL). That stock holds 48 × 2,536 = **PKR 121,700 of gross profit** doing nothing. A TEST-tier slot at the ~495/day minimum for 7 days (≈ 3,500, under 2× its ceiling, so the section 4 rules cap the loss) would show whether it can sell at H1-like CPAs. At H1's 1,100 it would leave ~770 per placed order above break-even, against ~360 on Mocha. Proposal only: it needs the Founder's yes (L3 spend).
