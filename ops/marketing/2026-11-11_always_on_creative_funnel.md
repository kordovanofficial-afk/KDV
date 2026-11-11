# Always-on Meta creative funnel: Dec 1 2026 to Feb 28 2027 (90 days)
**Owner:** Omar (CMO), covering Sana's (CRO) part: structure, budget and measurement · **Drafted:** Nov 11 2026
**Status:** L1 DRAFT, going to CQRO (Hamna), then CEO, then the Founder. Budget and pausing are L3. **Nothing is live and nothing was changed.**
**Inputs read:** `CLAUDE.md`, `ops/marketing/CREATIVE_PLAYBOOK.md`, `docs/brand/BRAND_MOODBOARD.md`, `downloads/Blessed_Friday_R1_R3_Prompts.md`,
`downloads/Our_Mistake_and_Ordered_vs_Arrived_Prompts.md`, the returns page (`snippets/returns.liquid`), live Shopify (prices, compare-at, stock,
unit cost and metafields, read Nov 11 2026) and live Meta creatives H1 (`1789159075513560`) and W01 (`1808182100454013`), read Nov 11 2026.
**Companion files:** `downloads/Always_On_December_Prompts.md` (Founder, GPT prompts plus Meta copy) · `downloads/Ahsan_Filming_List_December.md` (Ahsan).

---
## (a) Summary
From Dec 1 Kordovan runs one always-on Meta campaign that does not depend on a sale. It has three parts:
- **New customers (60%):** one ad set holding only formats that have already sold for us: the Comparison (H1 Mocha Mate, W01 gloves, plus one fresh static for each) and a best-sellers carousel.
- **Warm (30%):** the proven catalogue retargeting, plus a small trust ad set (Ordered vs Arrived, the FAQ carousel, and the W-RT1 winter kit). This part goes after the 25.3% lost-order rate.
- **Weekly test (10%):** one new format each week. A test ad graduates only on Shopify-confirmed orders.

The products ranked by expected margin are:

| Product | Regular price | GP at regular price | Units in stock |
|---|---|---|---|
| Mocha Mate | Rs 3,200 | Rs 2,250 | 29 |
| Executive belt | Rs 3,300 | Rs 2,200 | 28 |
| KODO RFID | Rs 2,300 | Rs 1,750 | 17 (Black 13) |
| Sheep-leather gloves (black and brown) | Rs 1,950 | Rs 1,300 | 71 |
| Cap | Rs 1,950 | Rs 1,300 | 15 (black and brown) |

All of these are ready-to-ship, so cash on delivery is available on every one. Jackets stay out.

**Recommendation: run the 8,000/day table from Dec 1, with a fixed step-down to the 5,000/day table at the Dec 14 read if the trigger in (b) is hit.**
At November's measured efficiency, December's first orders roughly break even on featured-line margins, so the step-down trigger is part of the plan. It is not an afterthought.
**Every ad is judged on Shopify orders by `utm_content` and on its own lost-order rate, never on Meta's count.**

---
## (b) Structure and budget

### Structure (one always-on campaign plus the existing Retarget)
| Slot | Ad set | Audience | Ads at Dec 1 | Judged on |
|---|---|---|---|---|
| NEW (60%) | `AON-NEW` (new, Sales/Purchase) | 9 cities, no radius, Advantage+ audience, **exclude** Purchasers 180D `120252468019140428` + COD Refusers `120253660257910428` | 5 (see calendar) | Shopify CPA vs the category ceiling, plus lost-order rate |
| WARM (20%) | existing Retarget catalogue `120228534676860428` | unchanged (warm + buyers, catalogue) | catalogue | Shopify CPA ≤ 1,300 blended |
| WARM (10%) | `AON-WARM` (new) | All Visitors 180D `120252468018150428`, 9 cities, exclude Purchasers 180D + COD Refusers | 3 trust ads | Shopify CPA, plus **lost-order rate vs the account** |
| TEST (10%) | `AON-TEST` (new) | same as AON-NEW | 1 new format per week | graduation rule (f) |

- **Why the catalogue retargeting stays separate:** it is a catalogue ad set, and static trust ads cannot sit inside it. That is why warm has two ad sets.
- **Consolidation on Dec 1 (L3, needs the Founder's yes):** create the AON campaign. Carry over the proven creatives as new ads that use their *existing creative IDs*, so their `utm_content` and copy carry over:

  | Carried creative | Creative ID | utm_content |
  |---|---|---|
  | H1 | `1789159075513560` | `h1_comparison` |
  | W01 | `1808182100454013` | `w01_comparison` |
  | W-RT1 | (existing) | (existing) |

  Then pause TOF-M `120255717721520428`/`…21900428`, TOF-W `120255846370500428` and RT-W `120255846373980428`, so nothing double-spends.
  Learning resets once, on Dec 1. After that, the 72-hour rule and Monday-only batch edits apply.
- **Before H1 is carried over, the CQRO checks it.** Its live copy says "6 to 12 cards plus cash" and "Over 4,000 wallets sold since 2021", but the live Mocha Mate page says "5–6 card slots".
  - I found no source for the 4,000 figure.
  - Creatives are immutable, so if either claim fails, H1 has to be rebuilt as a new creative with corrected copy. It then gets new IDs, and its history starts over.
- Retarget does not rely on `product_audience_specs`; it uses website audiences (CLAUDE.md).

### Budget table A: 8,000/day (recommended)
| Ad set | Per day | Share | Ads |
|---|---|---|---|
| AON-NEW | 4,800 | 60% | 5 |
| Retarget catalogue | 1,600 | 20% | catalogue |
| AON-WARM | 800 | 10% | 3 |
| AON-TEST | 800 | 10% | 1 per week |
| **Total** | **8,000** | **100%** | |
Check: 4,800 + 1,600 + 800 + 800 = 8,000. Every ad set is at least 495. Warm = 2,400 = 30%.

### Budget table B: 5,000/day (lean)
| Ad set | Per day | Share | Ads |
|---|---|---|---|
| AON-NEW | 3,000 | 60% | 4 (drop the weaker new static comparison at the first read) |
| Retarget catalogue | 1,000 | 20% | catalogue |
| AON-WARM | 500 | 10% | 2 (Ordered vs Arrived + FAQ; W-RT1 is dropped) |
| AON-TEST | 500 | 10% | 1 per week |
| **Total** | **5,000** | **100%** | |
Check: 3,000 + 1,000 + 500 + 500 = 5,000. Every ad set is at least 495 (AON-WARM and AON-TEST sit just above the minimum). Warm = 1,500 = 30%.

### Forecast (rule: spend × measured orders per rupee × survival; December only)
| | A: 8,000/day | B: 5,000/day |
|---|---|---|
| December spend (31 days) | 248,000 | 155,000 |
| Shopify orders placed (0.713 per 1,000 spend) | ~177 | ~110 |
| Placed revenue (2.33x spend) | ~577,000 | ~361,000 |
| Surviving revenue (× 0.747) | ~431,000 (~132 orders) | ~270,000 (~82 orders) |
| Surviving GP at 65% GM, minus spend | **~ +32,000** | **~ +20,000** |
| Same at the house 45% GM, minus spend | ~ −54,000 | ~ −34,000 |

> **Assumptions (labelled, each with the test that replaces it)**
> 1. 0.713 orders and Rs 2,327 revenue per Rs 1,000 spent come from the Nov 1–8 Meta channel split (34 orders, 111k, 47.7k spend, about 6,000/day).
>    *Replaced by:* the Dec 14 Shopify read by `utm_medium=paid_social`.
>    Scaling to 8,000 is an extrapolation beyond the level we measured.
> 2. Survival of 74.7% comes from October's account-wide 25.3% lost-order rate, not a Meta-only rate.
>    *Replaced by:* day-14 survival of December's paid orders, read Dec 28.
> 3. 65% GM is the regular-price margin of the featured lines (Mocha 70%, KODO 76%, gloves 67%, belt 67%, cap 67%; unit cost from Shopify Nov 11).
>    The catalogue also sells bags at lower margins, so 45% is the floor case.
>    Neither figure includes delivery cost or return freight on refusals.
>    *Replaced by:* per-line Shopify GP in the monthly scorecard.
> 4. **Not counted:** WhatsApp/DM orders without a UTM (DM keywords MOCHA, GLOVES, BELT, KODO are logged by Ahsan and matched weekly), in-store sales prompted by ads, and repeat purchases.

**Step-down trigger (decided now, applied at the Dec 14 Monday read):** switch to table B if either of these is true:
- blended Shopify CPA across AON-NEW + AON-WARM is above 1,300 for Dec 1–13, or
- placed revenue ÷ spend is below 2.0x (≈ break-even on 65% GM after 25% loss).

The switch is one batched edit, sent to the Founder for a yes.

---
## (c) December calendar (week by week)
Weeks run Tuesday to Monday because Dec 1 is a Tuesday. The read is every Monday (Dec 7, 14, 21, 28). Edits happen only after a read, batched, and need the Founder's yes. A test ad launches on Tuesday and runs 7 days.

**Production deadlines:**
- Ahsan starts filming Nov 16.
- GPT statics go to the CQRO by Nov 24.
- The Founder approves by Nov 28.
- Everything is uploaded on Nov 30, with the BF campaign ending at 23:59.

| Week | AON-NEW (60%) | AON-WARM + Retarget (30%) | AON-TEST (10%) | Ads live | Stock check |
|---|---|---|---|---|---|
| **W1 · Dec 1–7** | H1 Mocha Comparison video (control) · W01 gloves Comparison (control) · `aon_comparison_mocha_v1` (new static) · `aon_comparison_gloves_v1` (new static, black) · `aon_carousel_bestsellers_v1` (6 cards) | Retarget catalogue · `aon_ordered_vs_arrived_mocha` (real photo, already made) · `aon_faq_youasked_v1` (5-card carousel) · W-RT1 winter kit | `aon_closeup_kodo_v1` (KODO Black close-up) | 5 + 3 + catalogue + 1 | Mocha ≥ 15 · KODO Black ≥ 8 |
| **W2 · Dec 8–14** | no change (learning) | no change | `aon_workshop_craft_v1` (real Ahsan footage, 15–20s, cropped 4:5). *Fallback if footage is late:* `aon_closeup_belt_v1` | 9 + catalogue | Mon Dec 7 read: kill checks only |
| **W3 · Dec 15–21** | Dec 14 read: apply the step-down trigger; graduate W1's test if it passes; refresh any ad with 7-day frequency > 2.5 | Dec 14 read: frequency check on AON-WARM (refresh FAQ v2 if > 3.0) | `aon_patina_mocha_v1` (real used Mocha Mate beside a new one, Ahsan). *Fallback:* `aon_closeup_belt_v1` | 9–10 + catalogue | gloves sizes M/L brown ≥ 3 each |
| **W4 · Dec 22–28** | graduates join, max 6 ads in AON-NEW (pause the weakest by Shopify CPA, L3) | Dec 28: first day-14 lost-order rate per ad | `aon_commentreply_mocha_v1` (a REAL comment answered on film, see Ahsan list). *Fallback:* rerun the best near-miss with a new angle | 9–10 + catalogue | Dec 25 is a holiday, with slower delivery: no edits Dec 24–27 |
| **W5 · Dec 29–Jan 4** | December scorecard filled in on Jan 4 | | `aon_ordered_vs_arrived_gloves_v1` (Ahsan's real gloves unboxing photo, same template) | 9–10 + catalogue | January plan set from the scorecard |

**Each December content decision, with product, rupees and measurement:**

| Decision | Product | Expected rupees | Measured by |
|---|---|---|---|
| NEW gets 4,800 | Mocha Mate and gloves first (highest GP × stock) | ~60% of table A's ~431k surviving | `utm_content` per ad |
| WARM trust | all ready-to-ship | measured by lower lost-order rate rather than extra orders | day-14 lost-order rate per `utm_content` |
| TEST | rotating | 800/day buys a verdict, not revenue | graduation rule |

**Stock rule:**
- If Mocha Mate falls below 10 units, its static Comparison is paused and the carousel leads with KODO. H1 keeps running only if a restock is dated.
- KODO ads show only the **Black** variant (13 units). Brown has 1 unit, and Black Silver and Brown Gold have 0.

**January and February (outline, set from the scorecard):**
- **January:** graduated real formats (workshop, patina, Ordered vs Arrived) fill AON-NEW. Gloves stay the lead through January.
- **February:** gloves taper from mid-February. Wallets and belts lead into Ramadan (expected to start around Feb 8 2027; verify the date) and the Eid gifting window (around Mar 9–10 2027).
  - A wallet + belt Comparison and a real-photo gifting angle are prepared by Feb 1. There are no gift sets (they are discontinued).
- **Optional later idea, not in this plan:** jackets (top-grain sheepskin, paid online, about 3 weeks to the door because each is cut for one customer). These come back only after jacket checkout completion recovers.

---
## (d) UTM and naming scheme
- **URL parameters on every ad (paid only):**
  `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign=aon_<monYY>&utm_term=<slot>&utm_content=<ad-id>`
  - `{{site_source_name}}` resolves to fb / ig.
  - `<monYY>` = the month the ad launched, e.g. `aon_dec26`. It stays fixed for the life of the ad.
  - `<slot>` = `new` | `warm` | `test`. When a test ad graduates, the copy placed in AON-NEW keeps its `utm_content` and gets `utm_term=new`. One creative therefore has one history, and the slot shows where each order came from.
- **`utm_content` (the ad ID):** `aon_<format>_<product>_v<n>`
  - formats: `comparison`, `carousel`, `faq`, `closeup`, `workshop`, `patina`, `commentreply`, `ordered_vs_arrived`
  - products: `mocha`, `kodo`, `gloves`, `belt`, `cap`, `bestsellers` (multi-product), `all` (brand-wide)
  - `v<n>` increases with every new creative, including a copy fix, because creatives are immutable.
  - Examples: `aon_comparison_mocha_v1`, `aon_faq_youasked_v1` (a named exception: `youasked` is the series), `aon_ordered_vs_arrived_mocha` (the Founder's existing ID, kept as is and treated as v1).
- **Carried-over legacy IDs** (kept so their history continues): `h1_comparison`, `w01_comparison`, W-RT1's existing tag. Each gets a row in the scorecard.
- **Meta ad names** mirror the ID: `AON | NEW | comparison | mocha | v1`.
- **The landing page must match the click:** each single-product ad links to its product page. Before publishing, the CQRO checks that the page says what the ad says (COD, 7-day exchange, materials). The carousel links each card to its own product. The FAQ links to `/pages/returns` only on the returns card; every other card links to the best-sellers collection.

---
## (e) Monthly format scorecard (template; fill on the first Monday of each month, plus Mondays for the running month)
Sources: Meta ad-level (spend, Meta purchases) · Shopify orders by `utm_content` (placed, revenue) · Shopify status at day 14 (cancelled, refused/RTO = lost). Only orders at least 14 days old count in the lost-order rate.

| Ad (`utm_content`) | Slot | Format | Product | Spend | Meta purch. | Shopify orders | Meta ÷ Shopify | Real CPA (spend ÷ Shopify) | Revenue placed | Lost orders (d14) | Lost-order rate | Surviving revenue | Surviving GP | Real ROAS (surv. rev ÷ spend) | Ceiling | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| h1_comparison | new | comparison (video) | mocha | | | | | | | | | | | | 1,300 | |
| w01_comparison | new | comparison | gloves | | | | | | | | | | | | 1,000 | |
| aon_comparison_mocha_v1 | new | comparison | mocha | | | | | | | | | | | | 1,300 | |
| aon_comparison_gloves_v1 | new | comparison | gloves | | | | | | | | | | | | 1,000 | |
| aon_carousel_bestsellers_v1 | new | carousel | multi | | | | | | | | | | | | 1,300 | |
| (retarget catalogue) | warm | catalogue | multi | | | | | | | | | | | | 1,300 | |
| aon_ordered_vs_arrived_mocha | warm | ordered vs arrived | mocha | | | | | | | | | | | | 1,300 | |
| aon_faq_youasked_v1 | warm | faq | all | | | | | | | | | | | | 1,300 | |
| (W-RT1 existing) | warm | winter kit | gloves + cap | | | | | | | | | | | | 1,000 | |
| aon_closeup_kodo_v1 | test | closeup | kodo | | | | | | | | | | | | 1,300 | |
| … one row per test | | | | | | | | | | | | | | | | |
| **Account total** | | | | | | | | | | | **(baseline)** | | | | | |

**Format roll-up (one row per format):** total spend, Shopify orders, real CPA, lost-order rate vs the account, and the playbook status after the read (PROVEN / IN TEST / LOST). The result goes into `ops/marketing/CREATIVE_PLAYBOOK.md` the same day.
**Placement line (Founder, Nov 10):** for each 4:5 ad, Meta purchases split feed vs stories/reels, for information only. We never exclude placements on averages.

---
## (f) Graduation and kill rules (consistent with the playbook and the Nov 7 kill rule)
**Judging basis:**
- Spend ÷ **Shopify-confirmed orders** by `utm_content` (placed), with Meta used only as an early signal.
- Windows are 14 days, plus lifetime.
- No verdict before an ad has spent at least its category ceiling.

| Category | CPA ceiling (Shopify) | Expected surviving GP per placed order (regular price × 74.7%) |
|---|---|---|
| Wallets (Mocha, KODO) | 1,300 | Mocha ~1,680 · KODO ~1,310 |
| Belt | 1,300 | ~1,640 |
| Gloves, cap | 1,000 | ~970 (the ceiling = break-even; the margin comes from add-on baskets, avg subtotal ~2,726 since Nov 8) |
| Carousel / catalogue / FAQ (multi) | 1,300 | blended |

**GRADUATE (test → AON-NEW):** the ad must meet all of these:
- at least 2 Shopify orders,
- real CPA ≤ its ceiling over its 7-day test,
- lost-order rate ≤ the account average once its orders are 14 days old.

Until the lost-order rate is known, graduation is provisional. The move is batched at a Monday read with the Founder's yes. It then becomes **PROVEN** in the playbook.

**KILL (pause; L3, Founder yes; ad level, never the whole ad set):**
1. Spend ≥ ceiling with 0 Shopify orders → pause. Gloves and cap: ≥ 1,000; wallets and belt: ≥ 1,300.
2. Real CPA above the ceiling over 14 days, with at least 2× ceiling spent → pause.
3. **Refusal kill:** ≥ 5 Shopify orders and a lost-order rate more than 10 points above the account rate → pause, even if the CPA passes. An ad that sells but gets refused is a loser.
4. Fatigue: 7-day frequency > 2.5 (new) or > 3.0 (warm), *and* CPA up 30% on its first 14 days → replace it with v(n+1). Don't pause the slot.
5. Under the ceiling with no sale → leave it running.

**STOP list (number behind each):**

| Stop | Why (number) |
|---|---|
| Founder-led wallet ads | H3 lifetime CPA ~987, paused Nov 8 |
| 9:16 story-only creatives | S3: 971 spent, 0 purchases; Founder rule: 4:5 only |
| Gloves W02–W05 and W-RT2 angles (motorbike fog, chai dhaba, snow, commute) | failed the gloves kill rule Nov 8 (W03 1,063 with 0 sales; W-RT2 CPA 1,558) |
| Value-graph / cost-per-year ad | no defensible lifespan numbers (see the prompts file) |
| Product-audience retargeting (`product_audience_specs`) | never delivered |
| Separate top-, middle- and bottom-of-funnel campaigns | the budget can't feed them above the ~495 minimum with enough data (Founder) |

**LOST:** two failed tests of the same format with different angles → LOST in the playbook.

**Lag rule:** a CPA verdict comes on day 7–14; the lost-order verdict comes on day 14 after the last order counted. Read the scorecard with that lag in mind.

---
## (g) Risks
1. **Mocha Mate stock (29) caps the lead product.** At table A, Mocha could sell through in about 2–3 weeks. *Open question for the Founder: the December restock quantity and date.* The stock rule in (c) protects against selling what we don't have.
2. **The Dec 1 consolidation resets learning.** Expect a worse CPA for about 7–10 days. No other edits are made until the Dec 14 read except L3 kills.
3. **One mixed ad set:** Meta may push most of the spend to one ad (often the video), leaving others unjudged. This is acceptable if that ad wins. Ads under their ceiling simply keep running (rule 5).
4. **Gloves economics are at the margin:** the ceiling of 1,000 ≈ surviving GP on a single pair at the regular 1,950. After the 11.11 price revert, CPA may rise. W01's lifetime spend is now 10,561, so it needs about 11 Shopify orders to stay ≤ 1,000. **Recount it against Shopify before the Dec 1 carry-over.**
5. **Claims in the carried creatives:** see the H1 note in (b). W01 says "Cash on delivery all over Pakistan" and "Rs 1,950", which matches the regular price after the Nov 12 revert. The CQRO verifies both pages on Nov 30.
6. **The FAQ must stay true.** The 7-day policy is an **exchange or store credit** on unused items (not a refund). Made-to-order pieces are not returnable once cutting begins. COD costs Rs 250 more than paying online at every basket size, per the delivery profile. If any policy changes, the FAQ is rebuilt (v2).
7. **GPT image risk:** text misspellings and product drift. Each prompt locks the product photo, and the Founder checks side by side. The "synthetic" item in the comparisons is unbranded and generic, never a real competitor.
8. **Untagged sales** (WhatsApp, DM, store) undercount winners. DM keywords and Ahsan's log partly cover them; the forecast does not count them.
9. **Small warm audience at 800/day:** frequency can climb fast. The fatigue rule and the v2 FAQ are ready.
10. **Seasonality:** gloves demand fades by late February. Ramadan and Eid dates must be verified before the February plan.
11. **Real-only formats depend on Ahsan.** Each test week has a GPT fallback, so the test slot never sits empty. A late real clip is never replaced by a generated imitation.

## CQRO check (Nov 11)
Hamna (CQRO). Level: L2 (customer-facing ads), correctly classified. Sources: live Shopify product descriptions, `custom.*` metafields and variant stock (read Nov 11); ShopifyQL net items sold, last 60 days (Nov 11); `docs/legal/refund-policy.html`; CLAUDE.md. No Karachi, no prices and no reviews anywhere in either file.
Direct fixes made in `downloads/Always_On_December_Prompts.md` (mechanical, sourced):
- FAQ card 1 "WE HEAR EVERY DAY" → "WE HEAR OFTEN" (frequency unverified); primary text likewise.
- FAQ card 2 "Our wallets and belts are genuine cow leather" was FALSE as a universal: Rigor Lite, Sheppard and Midtown Lite are sheep leather (live `custom.material`). Rewritten to "mostly cow; a few slim wallets, gloves and caps are sheep".
- FAQ primary text "textured cow leather" → "textured leather" (live material says croc-/snake-textured leather, animal not stated).
- FAQ card 3 "anywhere in Pakistan" → "across Pakistan". Card 4 MTO line → "can't be returned, because each one is cut for you" (policy: MTO non-returnable). Card 5 promise aligned to the policy (manufacturing defect). Exchange lines now say "unused (ready-to-ship)".
- Gloves "sizes S to 2XL" → "S to XL" (Brown 2XL = 0, Black 2XL = 1). Belt "double row along each edge" → "double-stitched edges". Carousel "never cracks" → "rather than cracks".

| # | Prompt | Verdict | Note / fix |
|---|---|---|---|
| 1 | FAQ carousel | APPROVED after fixes above | COD +250 matches the delivery profile; exchange/store credit is narrower than the policy, so safe. |
| 2 | Mocha Mate comparison | APPROVED after fix | Cow leather, outer button coin pocket, ID window all live. No card count used. |
| 3 | Gloves comparison | RETURNED | Live description: "Genuine leather with a **spandex palm**", fleece lining. "Knit lets the wind in. Leather doesn't." and "Keeps the wind out" imply an all-leather glove. Fix (maker to choose): line 1 "Knit lets the wind in." line 2 "Leather on the back doesn't."; right-pair lines "Sheep leather back" / "Fleece lined inside"; primary text "Sheep leather on the back, a stretch palm for grip and a fleece lining inside." Same for carousel card 4 LINE "Keeps the wind out." → "Fleece lined inside." |
| 4 | KODO close-up | APPROVED | Two bonded layers of Crazy Horse cow leather, up to 10 cards, 3 sections, pull-tab, RFID: all live. |
| 5 | Executive belt close-up | APPROVED after fix | Cowhide; colours chocolate brown, black, tan, camel match live variants. |
| 6 | Best-sellers carousel | RETURNED | "Our best-sellers this winter" includes the KODO, which is not in the top 12 online (60 days). Top sellers: Mocha Mate 45, Gloves Brown 32, Rigor Lite 21, Gloves Black 18, Executive belt 14, Baseball cap 13. Fix: swap card 2 to Rigor Lite (sheep leather slim wallet), or change the primary text to "Our winter pieces:". Also inherits the prompt 3 glove fix. |
| — | Ahsan filming list | APPROVED | Real-only, consent and order-number logging for patina, no fake comments, no city named. |

**Live finding for the Founder (not in these files):** the Mocha Mate and KODO pages (where these ads land) still render 6 `custom.reviews` each, with no recorded provenance (archive line 18, raised Oct 25 and still live Nov 11). They also feed the JSON-LD review markup. Sending December traffic to them breaks the no-invented-reviews rule. Recommendation: clear `custom.reviews` on those pages (L2, Founder yes) before Dec 1.
Next check: Nov 30, re-check COD, the 5,500 threshold, glove sizes, and the landing pages for each ad.
