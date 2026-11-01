# Stock truth: where Shopify stock is wrong (Nov 1 2026)

From: Zain Haider, COO · To: CEO, then CQRO, then the Founder (L2: the corrections change live stock)
Scope: all **173 ACTIVE products / 597 variants**, one location ("G4 Falcon Street Malir Cantt").
Source for every stock figure: Shopify Admin GraphQL `products(query:"status:active")`, read **Nov 1 2026**.
Sales figures: ShopifyQL `FROM sales SHOW net_items_sold ... SINCE -90d`, run Nov 1 2026 (online and Shopify channels
only; walk-in store sales are not in Shopify).
**Read-only. Nothing in Shopify was changed.**

## Five lines
- **Decision:** Approve the 3 data-only fixes now (section 6, part A). Have Mr. Tahir count 34 variants on the shelf by
  **Sun Nov 8**, before the 11.11 sale starts Nov 10: the 15 lines at or around a negative, the Cabin and Branson
  colours, and the 17 sale lines most likely to be oversold. Apply the counts as one batch on Nov 8–9, with the
  POS sync switched off first.
- **Rupee impact:** **PKR 285,250** of stock is negative (20 units over 9 variants). Those lines show as sold out, so any
  real shelf stock on them cannot sell online. **PKR 1,251,062** of wallet, hat, cap and glove stock goes on sale at
  11.11 prices (534 units) with no shelf check behind it. **11 variants on 5 non-MTO products are untracked**, so they
  can be ordered without limit. **PKR 15.26M at cost** of jacket stock that does not exist sits in Shopify's inventory value.
- **Confidence:** High on every Shopify figure (read live today). Medium on *why* each line is negative: I cannot see
  adjustment history with my tools (A2). Low on how many sale units are phantom. Only a count settles that.
- **Risk:** If the counts are written while the POS sync is still running, the sync can overwrite them (two writers).
  If no count happens before Nov 10, a 25%-off wallet that is not on the shelf gets sold and then cancelled.
- **I need:** **Founder:** (1) yes to part A; (2) the date the POS sync goes off (must be before the Nov 8 batch);
  (3) yes to publishing 4 photographed products (section 7). **Mr. Tahir by Nov 8:** a dated, per-variant count of
  the 34 lines in section 6B, signed with his name; Cabin and Branson colour splits; and a yes/no on whether the
  5 untracked products are made to order.

| # | Finding | Variants | Rupees (source: Shopify, Nov 1) | Needs |
|---|---|---|---|---|
| 1 | Negative stock, non-MTO | 9 | 20 units · PKR 285,250 retail | Shelf count |
| 2 | Negative stock, MTO footwear | 17 | 19 units · harmless (CONTINUE) | Nothing (optional tidy) |
| 3 | Jacket placeholders, untracked | 162 (27 products) | Harmless | Nothing |
| 4 | Jacket placeholders, **tracked** | 18 (3 products) | 1,795 phantom units · **PKR 15,258,000 at cost** | Policy fix (no count) |
| 5 | Non-MTO **untracked** (unlimited sell) | 11 (5 products) | One phantom order = PKR 3,740–35,700 | Tahir: MTO or count |
| 6 | Cabin Trolley: store 11 vs Shopify 8 | 3 | +3 units · PKR 126,000 not listed | Colour split |
| 7 | Branson: store 2 vs Shopify 4 | 3 | −2 units · PKR 76,000 phantom (unpublished) | Colour split |
| 8 | Active, stock > 0, not on Online Store | 10 products | 52 units · PKR 579,200 retail | Founder (publish 4) |
| 9 | 11.11 oversell exposure (wallets/hats/caps/gloves) | 60 | 534 units · PKR 1,251,062 at sale price | 17-line count |

## Assumptions
- **A1. Publication `44250300605` is the Online Store.** Every product with an `onlineStoreUrl` carries it, and no product
  without one does. `67510304957` is the Facebook catalogue (its title says so). `67510894781` is assumed to be Google.
  *Replace:* Founder opens Settings → Apps and sales channels.
- **A2. A negative on a DENY variant came from outside online checkout.** Shopify will not sell a DENY variant past 0 online,
  and `committed` is 0 on all 9 lines, so no open order is waiting on them. That leaves the POS sync, an order edit or a manual
  adjustment as the cause. *Replace:* Founder opens Admin → Products → the variant → Inventory → **Adjustment history** (free,
  native). Its "Reason / app" column names the writer.
- **A3. The store does sell wallets, hats and gloves over the counter.** I have no store sales data (POS is not in Shopify).
  *Replace:* the first 7 daily store reports (format in `store_report_card.md`).
- **A4. The 40 card codes are ranked by Shopify data,** using 90-day online units first and stock on hand second, because
  store sales are invisible. *Replace:* Mr. Tahir swaps in any counter best-seller that is missing (one message).
- **A5. Untracked non-MTO products (finding 5) may actually be made on order.** If so, they need the MTO flag and prepaid
  terms, not a count. *Replace:* Mr. Tahir's yes/no.

---

## 1. Negative stock: every active variant below 0

### 1a. Non-MTO (DENY policy, tracked) = **9 variants, 20 units, PKR 285,250 at retail**
`committed` = 0 and `incoming` = 0 on all 9 (inventoryLevel quantities, read Nov 1).

| Product | Colour / size | SKU | Shopify | Price | Retail value | Online sold 90d | On Online Store |
|---|---|---|---|---|---|---|---|
| The Maverik Laptop Bag | Burgundy | SHOPIFY-VAR-46538442834160 | **−7** | 26,500 | 185,500 | 9 | yes |
| Clifford Cowboy Hat // Rustic Brown | M | BCWCHB001-V4 | **−2** | 10,500 | 21,000 | 2 | yes |
| Clifford Cowboy Hat // Rustic Brown | S | BCWCHB001-V5 | **−1** | 10,500 | 10,500 | 2 | yes |
| Black Stripe Leather Cowboy Hat | Large | SHOPIFY-VAR-49839356641520 | **−2** | 4,800 | 9,600 | 2 | yes |
| Black Stripe Leather Cowboy Hat | Extra large | SHOPIFY-VAR-49839356674288 | **−1** | 4,800 | 4,800 | 1 | yes |
| "Four in One" Leather Gift Set | Black | FIOGS200 | **−3** | 9,000 | 27,000 | 0 | **no (no channel)** |
| The Extendable Travel Laptop Bag | Brown | KNMELB011 | **−1** | 21,000 | 21,000 | 1 | yes |
| Imperial Keychain | Chocolate Brown | KIMKD0030 | **−2** | 1,950 | 3,900 | 0 | yes |
| Imperial Keychain | Maroon | KIMKT0020-4 | **−1** | 1,950 | 1,950 | 0 | yes |

The CMO's reading is **confirmed**: Clifford Rustic Brown M −2, S −1 (Shopify, Nov 1).
Total 7+2+1+2+1+3+1+2+1 = **20 units**. Retail 185,500 + 31,500 + 14,400 + 27,000 + 21,000 + 5,850 = **PKR 285,250**.

**What the negatives most likely mean: a missing receipt, not an online oversell.**
- Online checkout cannot push a DENY variant below 0, and none of the 9 has an order waiting (`committed` 0). The units left
  through another writer, most likely the POS sync recording counter sales of stock Shopify never received from the
  workshop (A2).
- So the shelf **did** hold units Shopify did not know about. The negative tells us a receipt was missed. It does not tell
  us what is on the shelf now. The true count could be 0 or more.
- **Maverik Burgundy is the clearest case:** 9 sold online in 90 days (ShopifyQL, Nov 1) and the variant still sits at −7,
  so at least 7 units moved without a receipt. Unit cost is blank in Shopify for every Maverik colour, so the CFO cannot
  value this line.
- **The cost runs the other way from an oversell.** A negative DENY variant shows as **sold out**. If the shelf has
  Clifford hats in M and S, they cannot sell online. Clifford Rustic Brown sold 9 units online in 90 days
  (4 XL + 2 M + 2 S + 1 L) ≈ PKR 94,500, and only XL (1 unit) can be ordered today.
- **Negative is a signal, not a number to write** (operating rule). I am not proposing any figure for these lines. Each one
  gets a shelf count (section 6B).

### 1b. MTO footwear (CONTINUE policy) = 17 variants, 19 units: harmless
Premium Oxford Brown (UK 8 −2, UK 11 −1) · Premium Oxford Black (UK 10, UK 11) · Regal Weaver (UK 9) · Aristocratic
Strider (UK 7 −2, UK 11) · Executive Comfort Oxford (UK 6, 7, 10) · Enigma (UK 8) · Luxe Tussle (UK 9) · Saachi (UK 6, 8) ·
Soleil (UK 9, 11) · Slip-On Oxford (UK 11). Each is −1 unless shown.
These sell at zero by design (CLAUDE.md Sep 4 2026: MTO = CONTINUE), so the negative is just a running count of orders.
**No customer impact.** Optional tidy: set them untracked like the 27 jackets. Low priority, and not part of this batch.

## 2. Placeholder stock

### Jackets: deliberate and harmless on 27 of 30, wrong on 3
- **27 jackets: `tracked: false`, CONTINUE**, quantities 96–101 (e.g. Stryker 100/100/99/99/98/100). An untracked item
  ignores its number, so these always sell, which is what MTO needs. **Harmless.** The number is a leftover. Small
  bonus: `100 − qty` = sizes sold since the placeholder was set (Desert Voyager XXL at 96 = 4 sold).
- **3 jackets are `tracked: true` + DENY at ~100.** These are **Maverick** (99/99/99/101/99/99 = 596), **Marc Ed** (100 × 6 = 600)
  and **Nightfall** (100/100/100/99/100/100 = 599).
  - Customers do not notice yet: each size stops selling only after about 100 more orders.
  - **Finance does:** 596 × 8,500 + 600 × 9,000 + 599 × 8,000 = **PKR 15,258,000 at cost** of jackets that do not exist sit
    in Shopify's inventory value and sell-through reports. **CFO: exclude these from any stock valuation until fixed.**
  - They also break the MTO rule that every MTO variant is CONTINUE (CLAUDE.md Sep 4 2026).
  - **Fix (no count needed):** match the other 27, i.e. untracked + CONTINUE. Part A of the batch.
- Also at a 10 placeholder, untracked and harmless: Urban Rider, Iconic, Legender, Apex, Ace, Cobalt, Allaric, Spy, Bliss
  (some sizes), plus footwear Tuxedo (5 sizes), Salemanco Brogue Brown, Salemanco Oxford, Tassel, Diplomat (UK 11 each).

### Real non-MTO placeholder risk: 5 products untracked, so they sell without limit
These are not MTO (no `custom.made_to_order`) but are **`tracked: false`**, so Shopify accepts unlimited orders:

| Product | Variants | Shopify qty | Price | One phantom order at 11.11 price (15% off) |
|---|---|---|---|---|
| Premium Leather Western Cowboy Hat // Studs band // Burgundy | M, L, XL | 0 / 0 / 0 | 9,000 | 7,650 |
| The Saffire Belt | Black, Brown, Tan | 0 / 0 / 0 | 4,400 | 3,740 |
| Sheffield Backpack | Black, Brown | 0 / 0 | 26,500 | 22,525 |
| The Staton Premium Cow Leather Office/Laptop Bag | Brown, Black | 0 / 1 | 42,000 | 35,700 |
| The Atlantic Trolley Duffel Bag // Black | Default | 2 | 36,000 | 30,600 |

If any of these is truly made on order, it needs the MTO flag and prepaid terms. If it is stocked, it needs tracking on plus a
count. Either way it is a live oversell risk during the sale. **Mr. Tahir decides which (A5).**

## 3. Known open discrepancies (Founder's store count, CLAUDE.md Oct 31 2026, vs Shopify Nov 1)

| Line | Store count (Founder, Oct 31) | Shopify Nov 1, per colour | Gap | Rupees |
|---|---|---|---|---|
| **Cabin Trolley Bag** | 11 | Brown 2 · Black 4 · Coffee Brown 2 = **8** | **+3 in store** | 3 × 42,000 = PKR 126,000 sellable stock not listed |
| **TP Branson Briefcase** | 2 | Black 1 · Tan 2 · Maroon 1 = **4** | **−2 phantom** | 2 × 38,000 = PKR 76,000 (unpublished, so no live oversell yet) |
| CEO Executive Office Bag | 5 | 0 · 1 · 1 · 3 = 5 | matches | — |
| Master's Laptop Bag | 16 | Croc 0 · Multicolor 16 | matches | — |
| Bella Duff | 13 | 0·2·1·2·8·0·0 = 13 | matches | — |
| Forester | 3 | 0·1·1·1 = 3 | matches | — |
| Gridle | 6 | 6 | matches | — |
| Bellezza Clutch | 12 | Black 7 · Dark Red 5 | matches | — |
| Venture Pack | 9 | 2 · 3 · 4 | matches | — |
| HM The Lord's | 0 | corrected to 0 Oct 31; now DRAFT | done | — |

- **Two figures, side by side:** Cabin is 11 by the store count and 8 in Shopify; Branson is 2 by the store count and 4 in Shopify.
  The store count wins only once it is **per colour, dated and named** (operating rule). The Oct 31 counts are product totals,
  so both lines wait for Mr. Tahir's colour split.
- **Accuracy KPI update:** 8 of 10 counted lines now match Shopify (7 match outright, plus Lord's fixed). Was ≤7/10 (brief, Oct 31).

## 4. ACTIVE products with stock > 0 that are NOT on the Online Store
Ten products, **52 units, PKR 579,200 at retail**. Image counts are from `mediaCount`, Nov 1.

| Product | Units (per colour) | Price | Retail | Channels | Photos |
|---|---|---|---|---|---|
| The Master's Leather Laptop Bag | 16 (Multicolor 16) | 10,800 | 172,800 | none | **0** |
| TP Branson Briefcase | 4 (Black 1, Tan 2, Maroon 1); store says 2 | 38,000 | 152,000 | none | **0** |
| Bellezza Clutch | 12 (Black 7, Dark Red 5), store count matches | 6,500 | 78,000 | none | 6 |
| Voyager Suitcase Trolley Bag | 1 (Brown) | 48,000 | 48,000 | none | **0** |
| The City Backpack | 3 (Black, Brown, Tan 1 each) | 15,500 | 46,500 | Facebook only | **0** |
| The Gentlemans' Duffle | 1 (Tan) | 18,500 | 18,500 | Facebook only | 4 |
| Executive A4 Folder | 2 (Black 1, Brown 1) | 8,800 | 17,600 | none | **0** |
| Bull Rider Calf Leather Belt | 6 (Black 2, Brown 4) | 2,800 | 16,800 | Facebook only | 4 |
| The City Backpack // Rustic Red | 1 | 15,500 | 15,500 | Facebook only | 3 |
| Leather Lanyard | 6 (Black 2, Bodo 3, Tan 1) | 2,250 | 13,500 | none | **0** |

Sum: 172,800 + 152,000 + 78,000 + 48,000 + 46,500 + 18,500 + 17,600 + 16,800 + 15,500 + 13,500 = **PKR 579,200**.
- **6 of 10 have no photos.** These are Master's, Branson, Voyager, City Backpack, A4 Folder and Lanyard, matching the
  no-image list in CLAUDE.md Sep 8. **Photos come before publishing.** Ahsan's photo job, not a stock job.
- **4 have photos and could go live now:** Bellezza, Gentlemans' Duffle, Bull Rider, City Backpack Rustic Red
  (20 units, PKR 129,600). See section 7.
- ⚠️ **4 products are published to the Facebook catalogue but not to the Online Store** (City Backpack, Gentlemans' Duffle,
  Bull Rider, City Backpack Rustic Red). If the "All Products" catalogue set shows them, a paid click lands on a page that
  does not load. **For the CMO to check** in the catalogue (I have no Meta tools).
- Also unpublished, at 0 or negative: Braided Belt, Four in One (−3), Gift Box, Mini Card & Cash Carry, Luxe Card Lite.

## 5. 11.11 sale (Nov 10–12): where Shopify's sellable stock is likely higher than the shelf
**Exposure** = every sellable non-MTO, DENY, Online Store variant with stock > 0, valued at sale price (wallets 25% off,
everything else 15% off): **139 lines, 782 units, PKR 3,003,124**. Of that, wallets, hats, caps and gloves come to
**60 lines, 534 units, PKR 1,251,062**. That is not a loss figure. It is the stock no one has counted. On Oct 31, 3 of 10
counted lines were wrong (CLAUDE.md).

Three signs that a line's Shopify figure runs **above** the shelf:
- **S1. Untracked non-MTO:** sells without limit. These are the 5 products in section 2.
- **S2. Shown in stock with 0 online sales in 90 days.** This is the HM The Lord's pattern: stock sold at the counter while
  Shopify kept the old figure. It covers Luxurious Ladies Clutch White & Brown 18 and Black 10, The Seamless 19, Razor
  Brown Black 15 and Black Brown 13, Executive Belt Camel 5, and Case by Kordovan Vintage Brown 9.
  (ShopifyQL 90d shows 0 for each.)
- **S3. Same product has a negative sibling,** which means the POS sync was writing that product's stock unreliably:
  Clifford Rustic Brown XL 1, Black Stripe Medium 1, Maverik Black 2, Imperial Keychain Tan 1, Extendable Travel Black.

The 17 sale lines I want counted are in section 6B. I picked them by rupees at sale price, ranked highest first.

Mocha Mate, for the record only (Founder: restock in a few days, no escalation): **22 in Shopify Nov 1**, vs 25 on Oct 31 and
43 on Oct 24 (CLAUDE.md). It goes into the sale at 2,400.

## 6. Correction list (PROPOSAL: nothing has been changed)
**Order of work:** (1) Founder switches the POS sync off and names the date. (2) Mr. Tahir counts. (3) CQRO checks the
batch. (4) Founder approves. (5) CEO applies it. (6) I re-read every line and report back the same day.
Counts are written as **absolute sets with `compareQuantity` = the figure I read today**. If anything moved in between
(an online order, for example), the write fails instead of overwriting it.

### Part A: CERTAIN. No shelf count needed; data only.
| # | Change | Why it is certain | Effect |
|---|---|---|---|
| A1 | Maverick, Marc Ed, Nightfall jackets (18 variants): set `tracked: false`, policy CONTINUE | All 30 jackets are MTO (CLAUDE.md Sep 4); the other 27 are already set this way | Removes 1,795 phantom units / PKR 15.26M at cost from inventory value; no customer change |
| A2 | No write on the 8 matched lines (CEO, Master's, Bella Duff, Forester, Gridle, Bellezza, Venture, Lord's) | Store count = Shopify | Recorded as counted Oct 31, so they leave this week's cycle-count list |
| A3 | MTO footwear negatives (17 variants): **no write** | CONTINUE sells at zero by design | None. Optional tidy later |

### Part B: NEEDS MR. TAHIR'S SHELF COUNT (per variant, dated, his name), due **Sun Nov 8**
**B1. Negatives and their siblings (15 lines).** Each one shows sold out or unreliable today:
1. Maverik Laptop Bag: Burgundy (−7), Black (2), Tan (0)
2. Clifford Cowboy Hat Rustic Brown: S (−1), M (−2), L (0), XL (1), XXL (0)
3. Black Stripe Cowboy Hat: S (0), M (1), L (−2), XL (−1)
4. Extendable Travel Laptop Bag: Brown (−1)
5. Imperial Keychain: Chocolate Brown (−2), Maroon (−1). Tan and Black are folded into this one line.
6. Four in One Gift Set: Black (−3). It is on no channel, so count only.

**B2. Colour splits (2 lines).** Cabin Trolley (Brown / Black / Coffee Brown, total should be 11) and Branson
(Black / Tan / Maroon, total should be 2).

**B3. 11.11 pre-sale count (17 lines, ranked by rupees at sale price):**
| # | Line (Shopify qty, Nov 1) | At sale price | Sign |
|---|---|---|---|
| 1 | Luxurious Ladies Clutch White & Brown (18) | 97,200 | S2 |
| 2 | Bastion Brown (43) | 80,625 | top seller |
| 3 | Luxurious Ladies Clutch Chocolate (12) + Black (10) | 118,800 | Black S2 |
| 4 | Luke (30) | 54,000 | top seller |
| 5 | Bastion Tan (22) | 41,250 | top seller |
| 6 | Stallion (8) | 39,000 | — |
| 7 | Clifford Faded Black S (4) + L (3) | 62,475 | hero hat |
| 8 | Bronco Pullup (7) | 32,550 | — |
| 9 | The Seamless (19) | 28,500 | S2 |
| 10 | Razor Brown Black (15) + Black Brown (13) | 51,450 | S2 |
| 11 | Hunter HM (11) | 26,400 | net −1 in 90d |
| 12 | Money Clip (18) | 26,325 | — |
| 13 | Razor All Red (13), Red Black (9), All Black (8), All Brown (9) | 71,663 | — |
| 14 | KODO Black (13), Brown (2), Black Gold (3) | 31,050 | — |
| 15 | Aristocrat Brown (5) + Black (7) | 37,800 | — |
| 16 | Men's Winter Gloves, Black and Brown, all sizes (101) | 167,408 | seasonal |
| 17 | Genuine Sheep Baseball Cap Black (10) + Brown (10) | 33,150 | top seller |

**B4. Untracked non-MTO (5 products, section 2).** Mr. Tahir answers: made on order (then MTO flag + prepaid), or stocked
(then a count + tracking on). **Must be settled before Nov 10.**

Total to count: 15 + 2 + 17 = **34 lines**. Even 3–4 variants each is about an hour with Ahsan.

### What happens to each count
- **Count = Shopify:** no write, logged as counted.
- **Count ≠ Shopify:** absolute set to the count, with `compareQuantity` = the Nov 1 figure (re-read on the day).
- **Count higher than Shopify on a negative line:** set to the count. **No receipts are back-filled.** History stays as it is,
  and the CFO books the difference as an unreceived receipt.
- **Count of 0 on a sale line:** set to 0 before Nov 10, so it shows sold out instead of selling and then cancelling.

## 7. One idea nobody asked for: put four photographed products on sale instead of hiding them
Bellezza Clutch (12, store count matches), Gentlemans' Duffle (1), Bull Rider Belt (6) and City Backpack Rustic Red (1) are
**active, counted or low-risk, have photos, and are on no web channel** (section 4). Publishing them to the Online Store
before Nov 10 puts **20 units / PKR 129,600 at full price** in front of 11.11 traffic at zero media cost. At sale prices:
Bellezza 12 × 4,875 = 58,500 (25% off, still above its 2,350 cost), plus 18,500 + 6 × 2,800 + 15,500 = 50,800 at
15% off = 43,180. Total ≈ **PKR 101,680**.
It is one click per product (Founder, L2). It also fixes the Facebook-catalogue dead-end for three of them.

## Evidence trail
- Live reads Nov 1 2026: products (173), variants (597), inventoryLevels quantities (available / committed / on_hand / incoming)
  for the 9 negatives, `tracked` flags, `mediaCount`, `resourcePublicationsV2`.
- ShopifyQL 90-day `net_items_sold` by product and variant (135 rows).
- Raw pulls kept in the session scratchpad `stock/` (session-local; rebuild with the same queries).

## Appendix: card code → Shopify SKU (for the reconciliation; Ahsan never sees this)
MOCHA MM001 · BAST-BR TBSW0092 · BAST-TN SHOPIFY-VAR-48830732468464 · LUKE TLSW0011 · RAZ-BB TRZRBK0091 ·
RAZ-RB …49494426747120 · RAZ-AB …49494426779888 · RAZ-BRB …49494426812656 · RAZ-ABR …49494426845424 · RAZ-AR …49494426878192 ·
KODO-BK KDWBK0010 · KODO-BR KDWBR0010 · KODO-BG KDWBKG0010 · KV2-BR KV20BK0095 · RIGOR-BK RGWL0100 ·
RIGOR-BR SHOPIFY-VAR-47573513404656 · MIDTOWN MTWL0098 · SHEP SHPW0099 · SHELBY TSBSW002 · PLAIN-BK NLBFW002 ·
PLAIN-TN SHOPIFY-VAR-46256935960816 · ARIS-BR TACBRN0020 · ARIS-BK TACBLK0010 · HUNTER THHW0094 · SEAM SEAMBLK002 ·
CLIP TMC0031 · STALLION SHCW · BRONCO BHWL0020 · ELITE-BR TEMW0020 · ELITE-BK TEMW0021 · CLUTCH-WB TLLCW002 ·
CLUTCH-CH TLLCW003 · CLUTCH-BK TLLCW001 · CLIF-RB-XL BCWCHB001 / -L …-V3 / -M …-V4 / -S …-V5 / -XXL SHOPIFY-VAR-46926101151984 ·
CLIF-FB-XL BCWCHB002 / -L …-V2 / -M …-V3 / -S …-V4 · STRIPE-S/M/L/XL SHOPIFY-VAR-49839356575984 / …608752 / …641520 / …674288 ·
CAP-BK SLBC0020 · CAP-BR SLBC0040 · FLAT-BK SLFC0010 · FLAT-BR SLFC0020 · FLAT-TN SHOPIFY-VAR-48739139617008 ·
GLV-BK-S/M/L/XL/2XL DMLG00112 / DMLG0011 / DMLG0012 / DMLG0013 / SHOPIFY-VAR-48602098729200 ·
GLV-BR-S/M/L/XL DMLG0020 / DMLG0021 / DMLG0022 / DMLG0023 · GLV-W-S/M/L/XL DWLG0030 / DWSLGDR112 / DWSLGDR113 / DWSLGDR114.
(Several Shopify SKUs are auto-generated `SHOPIFY-VAR-…` placeholders. The card codes replace them for the store; real SKUs
can be set later, which is an L2 change.)
