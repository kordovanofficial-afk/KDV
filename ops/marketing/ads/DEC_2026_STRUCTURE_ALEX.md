# KORDOVAN Meta structure for December 2026 (Alex's recommendation)
**Status:** L3 proposal for the Founder. Nothing changed live. **Written:** 27 Nov 2026 (Claude through the Alex lens).
**Budget decided (Founder, Nov 27):** 5,000/day from Dec 1. **Founder rule:** leave good campaigns as they are.
**Fixed rules:** account `995683712074843` only · every ad set = the 9 cities, location type home, no radius · every ad set excludes COD Refusers `120253660257910428` · `targeting` is a full replace (read and merge) · creatives are immutable (new copy = new creative → new ad → pause old) · judge on Shopify orders by `utm_content` (Meta over-reports ~2.05x) · every pause/scale/budget move is L3 · never duplicate or overlap-test a proven ad (that resets its learning) · max 1 change per ad set per 72h.

---

## [Alex lens] Top line
1. **The constraint in December is not ads, it's stock and checkout.** Mocha Mate (the ad winner) has 11 units and sells ~1.5 a day: it runs out around Dec 4-6 unless the restock lands. Jackets (the winter money) complete checkout ~12% of the time. Buying more traffic into either is burning cash.
2. **The math:** after the two Blessed Friday ad sets end Nov 30 23:59, live spend falls on its own to **~3,160/day** (H1 1,860 · BOF 800 · RT-W 500 · TOF 500 with no ad = 0). We need **+1,840/day** placed on things that have already proven they sell, plus one disciplined weekly test.
3. **What I'd do:** keep H1, Retarget v2 and RT-W untouched. Carry the one BF winner (the Clifford hat ad, ~Rs 776 per Meta purchase over 7 days) into December at full price and half the budget. Give the empty TOF ad set two single-product statics (static beat video and carousel in 11.11). One 500/day test a week. No bags, no jackets in December until their conditions are met.
4. **What I'd stop:** bag ads at full price (3 Meta purchases on Rs 6.0k in BF, Rs 2,013 per purchase *before* the 2x correction); any "sale continues" messaging after Nov 30; feeding a sold-out Mocha ad.
5. **One thing this week:** get the Mocha restock date in writing from Tahir. It decides 37% of the December budget.

---

## 1. What exists today (read live 27 Nov, 7d Meta-reported)
| Ad set | ID | Budget/day | 7d spend | Meta purchases | Meta CPA | Ends | Dec 1 fate |
|---|---|---|---|---|---|---|---|
| TOF-M H1 Comparison (Mocha) | `120255717721520428` | 1,860 | 12,123 | 12 | 1,010 | — | **KEEP as is** (stock guard) |
| BOF Retarget (catalogue; v2 ad `120256265936730428`, set `1166452646327632`) | `120228534676860428` (campaign 800) | 800 | 4,394 | 7 (mostly the old ad before rejection) | 628 | — | **KEEP as is**; judge v2 alone |
| RT-W v2 gloves page viewers 30D | `120256111259690428` (campaign CBO 500) | 500 | 3,479 | 3 | 1,160 | — | **KEEP as is** |
| TOF Cold (A+A, LLA 1-3% signal) | `120256055941820428` | 500 | 0 (no ad) | — | — | — | **Give it 2 ads, 640/day** |
| BF26 HATS ONLY | `120256204345990428` | 1,400 | 9,311 | 12 | 776 | Nov 30 23:59 | **Carry into Dec at 700/day, full-price ad** |
| BF26 BAGS ONLY | `120256242727930428` | 3,300 | 6,039 | 3 | 2,013 | Nov 30 23:59 | **Let it end** |
| MOF trust / Autopilot / Truckkr TEST / old TOF-W / old RT-W | various | paused | — | — | — | — | stay paused |

---

## 2. Dec 1 allocation (5,000/day)
| Tier (by audience) | Ad set | Budget/day | Products | Change needed |
|---|---|---|---|---|
| **TOF** cold | TOF-M H1 Comparison `120255717721520428` | **1,860** | Mocha Mate | none |
| **TOF** cold | TOF Cold `120256055941820428` → rename `KDV | TOF | Prospecting Dec` | **640** (+140) | 2 new single-product statics: `tof_gloves_lifestyle_problem_lifestyle_v1` (the chai-dhaba gloves creative that works warm, tried cold) + `tof_executive_static_value_studio_v1` (Executive belt, 10 orders/28d, ceiling ~1,700) | new creatives + ads, budget |
| **TEST** cold | new ad set in the TOF campaign `KDV | TOF | Test Dec` (same targeting as TOF Cold) | **500** | one new format per week (section 5) | new ad set |
| **Warm** (MOF/BOF) | HATS ONLY `120256204345990428` → rename `KDV | WARM | Winter Hats` | **700** (−700) | Clifford Rustic Brown + Faded Black, Crushable | remove end date, budget, swap to a full-price ad (section 4) |
| **BOF** hot | Retarget `120228534676860428` (v2 clean catalogue) | **800** | 72 in-stock ready-to-ship items | none |
| **BOF** warm | RT-W v2 gloves `120256111259690428` | **500** | gloves | none |
| **Total** | | **5,000** | | ✓ every ad set ≥ 500 |

**Split:** new customers 3,000 (60%: H1 1,860 + Prospecting 640 + Test 500) · warm/hot 2,000 (40%). The Boardroom target is 60/30/10; December runs **60/40/0 + test inside the 60** because three of our four proven ads are warm. When the hats ad set is paused (stock or season, ~Dec 20-31), its 700 moves to TOF Prospecting only if a Prospecting ad has ≥2 Shopify orders under its ceiling; that lands us at 60/30/10 for January.
**By product (Dec 1):** wallets ~2,180 (44%: H1 + half Prospecting) · winter (gloves + hats) ~1,520 (30%) · catalogue mix 800 (16%) · test 500 (10%) · jackets 0 · bags 0 (catalogue only).

### Mocha stock guard (Founder decision 4)
- Mocha sells ~43 units/28d (1.5/day); 11 left on Nov 27 → about 5-7 days.
- When Mocha sellable stock is **≤3 and there is no restock date in writing**: pause the **H1 ad** (not the ad set; keeps its history), and leave its 1,860/day **unspent** (don't force it onto unproven ads). Reactivate the same ad the day stock lands; no edits, so learning is preserved.
- If the restock date is ≤7 days away, keep H1 running and tell buyers the honest dispatch time on the PDP (L2). Never sell Mocha as "last pieces".

### Jackets (Founder decision 5)
- **No jacket ad spend in December until jacket checkout completion is ≥25% for 7 days** after the CRO Wave 1 deploy (Dec 10; see `ops/marketing/cro/CRO_DEEP_PLAN_2026-11-27.md` items 1-6, 10). Baseline ~12% (3 orders vs 23 abandoned checkouts in 24 days).
- When it passes: the TEST slot runs `bof_jacket_static_trust_studio_v1` to Jacket visitors 30D `120255689014190428` for 7 days at 500/day. Ceiling ~7,750 per placed jacket order (~16,140 per paid). Copy must carry the terms with the reason (made to order, about 3 weeks, paid online because each is cut for one customer). Jackets are top-grain sheepskin.

### Bags
- Let `BF26 | BAGS ONLY` end at Nov 30 23:59 as scheduled. Bags at full price have long consideration and weak cold economics; Retarget v2's catalogue already contains in-stock bags. Write the BF bag read (per card `bf_car_*`, per static `bf_*`, Shopify-confirmed) into the playbook on Dec 1-3. Revisit a bag ad only for a real reason (new bag launch, gifting page in Feb).

---

## 3. Naming and UTM tags (from the Ads Operating System, section 2)
- **Ad name = utm_content:** `{tier}_{product}_{format}_{hook}_{style}_v{n}` (e.g. `tof_gloves_lifestyle_problem_lifestyle_v1`, `warm_clifford_static_status_studio_v2`, `test_mocha_faq_trust_real_v1`).
- **URL tags:** `utm_source=facebook&utm_medium=paid&utm_campaign={tier}_202612&utm_content={ad name}` (`tof_202612`, `test_202612`, `warm_202612`, `bof_202612`).
- **Do NOT rename or re-tag the proven ads** (H1 = `h1_comparison`, Retarget v2 = `bof_clean_v2`, RT-W = `rtw_gloves_chaidhaba_warm_lifestyle_v2`): their history and the Shopify join depend on the current tags.
- Ad set names: `KDV | {TIER} | {audience} | {month}`; campaign budgets stay where they are (BOF and TOF-W are campaign-level budgets today).

## 4. Tier rules (who sees what)
| Tier | Audience | Excludes (always) | Job |
|---|---|---|---|
| TOF / TEST | Advantage+ audience with the LLA 1% `120254216730060428` / 3% `120254216735280428` signal, 9 cities, home | COD refusers `120253660257910428`, Purchasers 180D `120252468019140428`, All Visitors 180D `120252468018150428`, Delivered SEED `120254215371460428`, BF purchasers 30D | find new buyers |
| WARM (hats) | BF bag+hat viewers 180D `120256204324970428` + All Visitors 180D + Purchasers 180D (as today) | COD refusers | sell the hat to people who looked |
| BOF | catalogue retargeting as set up in v2 | COD refusers | close viewers/ATC |
| RT-W | Gloves page viewers 30D `120256104608660428` | COD refusers | close glove viewers |

**Hats ad set on Dec 1:** the BF Clifford ad (`bf_clifford`) was built for the sale. If its creative shows a sale price, a strikethrough or the sale name (to verify on the creative before Nov 30), it must stop at 23:59 Nov 30. Steps (needs the Founder's yes, scheduled for Nov 30 evening): (1) build `warm_clifford_static_status_studio_v2` with the full price and no sale wording, as a paused ad in the same ad set; (2) at ~00:10 PKT Dec 1 (after the 00:05 price revert): remove the ad set end date, set 700/day, pause `bf_clifford`, activate v2. If the creative has no sale wording, simply remove the end date and set 700/day (the ad keeps its learning). Rename the ad set. **Pause the hats ad set** when any best-selling size shows ≤3 sellable, when hat cancels before dispatch pass 15%, or when the vendor's date slips without a new date in writing. Ceiling: CFO to compute the full-price hat ceiling by Dec 2; provisional **~1,800 per placed order**.

**BF audiences after Nov 30:** keep every audience (never delete; they are free retargeting pools). The BF bag+hat viewers 180D audience feeds the hats warm set; BF purchasers go into the TOF exclusion for 30 days; no "sale extended"/"last chance" ads to BF engagers (no fake urgency). BF learnings (static vs carousel, warm vs cold, feed vs stories/reels) go into `CREATIVE_PLAYBOOK.md` on Dec 1-3 from Shopify-confirmed orders.

## 5. Weekly format test (500/day, the TEST ad set)
- One challenger a week against the TOF Prospecting control; never a copy of H1 (no overlap with the proven ad). Read at ≥1x the product's ceiling spend with Shopify orders, verdict at 1.5x.
- Graduate rule (playbook section 6): ≥2 Shopify orders at ≤ ceiling and refusal rate ≤ account average → joins TOF Prospecting. Two failed angles of a format → LOST.

| Week | Dates | Test | Product | Asset source | utm_content |
|---|---|---|---|---|---|
| 1 | Dec 1-7 | FAQ "You asked, we answered" (real leather? COD? returns? delivery cost?) | Gloves (in stock, winter) | GPT static, real facts only | `test_gloves_faq_trust_textled_v1` |
| 2 | Dec 8-14 | Office desk demo (Founder's hands: fit, what fits, flex) | Gloves or Executive belt | Founder clip, Claude edits | `test_gloves_video_proof_real_v1` |
| 3 | Dec 15-21 | Jacket trust static to jacket viewers **only if** the checkout condition passed; else Patina before/after (Founder's own used wallet) | Jacket / wallet | studio static / real photo | `bof_jacket_static_trust_studio_v1` or `test_wallet_patina_proof_real_v1` |
| 4 | Dec 22-31 | Gift under Rs 5,500 (real full prices, no sale wording) | gloves + cap / belt + wallet | GPT static | `test_gift_static_gift_studio_v1` |
Founder produces the week-2 and week-3 real assets by Dec 6 (decision 6).

## 6. Per-product CPA ceilings (Shopify placed CPA; CFO Nov 14, regular prices)
Mocha Mate ~1,460 · Gloves 1,000 (Founder) · BOF catalogue mix ~1,500 · Executive belt ~1,700 · Jacket ~7,750 per placed (~16,140 per paid) · Aristocrat ~2,460 · Bronco ~2,720 · Truckkr ~1,870 · Shelby ~1,410 · Plain Bifold ~810 · KODO ~1,050 · Kodo Vertical ~1,040 · Bastion ~640 · Rigor Lite ~490 · **Hats (full price) provisional ~1,800, CFO by Dec 2** · Bags: no December ad.
⚠️ Ceilings rise again after the Dec 1 price revert (they fell during the sale).

## 7. Scale / kill rules (unchanged from the Ads OS, section 4; per AD, Shopify-confirmed)
| Situation | Action |
|---|---|
| New ad < 1x ceiling spent, no sale | keep running |
| Cold CTR < 0.6% after 3,000 impressions | stop (hook failed) |
| ≥ 1.5x ceiling spent, 0 Shopify orders | stop |
| 7-day Shopify CPA > 1.3x ceiling (≥ 3 orders' worth of spend) | stop |
| 7-day Shopify CPA ≤ 0.7x ceiling with ≥ 3 orders | +20% budget, then wait 72h |
| Frequency > 3 cold / > 6 warm AND CTR down ≥ 30% vs week 1 | refresh creative, same hook |
| Ad refusal rate > account average + 10 pts (day 14) | stop even if CPA looks good |
| Stock: product ≤ 3 sellable without a dated restock | pause that ad (Mocha, hats) |
Before any pause: list every ad in the ad set with lifetime + 14d numbers and Shopify orders by utm_content (Nov 8 lesson). Every pause/scale is L3: per-ad table → Founder yes. Monday weekly read stays the decision point.

## 8. Calendar
| When | What |
|---|---|
| Nov 28-30 | Verify the Clifford creative wording; build the full-price hat ad (paused) and the 2 Prospecting statics + week-1 test ad as drafts; CFO hat ceiling |
| Nov 30 23:59 | BF bags + hats ad sets end automatically |
| **Dec 1 ~00:10 PKT** | After the price revert: hats set → 700/day, no end date, full-price ad; Prospecting 640 with 2 ads; Test set 500 with week-1 ad. Read back every budget (total must equal 5,000) |
| Dec 1-3 | BF read into the playbook (Shopify-confirmed by utm_content, placement breakdown) |
| Dec 4 | 72h check (report only) |
| Dec 7, 14, 21, 28 | Monday weekly read: per-ad table, ceilings, stock, jacket checkout condition, next week's test |
| Dec 10+ | Jacket condition check starts after CRO Wave 1 |

---

## 9. Decisions for the Founder (6)
1. **Dec 1 allocation: 5,000/day as in section 2** (H1 1,860 · Prospecting 640 · Test 500 · Hats 700 · BOF 800 · RT-W 500). *[Alex lens] Yes. Everything proven stays untouched; new money goes only where proof exists. The number: blended Shopify CPA ≤ 1,400.*
2. **Hats into December:** keep the hats ad set at 700/day (half), full-price ad, no sale wording, with the stock/cancel/vendor-date pause rules. *[Alex lens] Yes. It's the best BF ad (~776 per Meta purchase), but at full price it must re-prove itself; half budget is the honest bet.*
3. **Bags:** let the bags ad set end Nov 30; no bag ad set in December (catalogue only). *[Alex lens] Yes. 2,013 per Meta purchase on clearance prices means it would be worse at full price.*
4. **Mocha stock guard:** Tahir gives the restock date in writing by Dec 1; pause the H1 ad at ≤3 sellable without a date; its budget stays unspent. *[Alex lens] Yes. You can't scale what you can't ship. Don't let the winner train on sold-out clicks.*
5. **Jackets:** no jacket ads until jacket checkout completion is ≥25% for 7 days after the Dec 10 CRO fixes; then a 500/day jacket-viewer retarget in the test slot. *[Alex lens] Yes. Fix the bucket, then pour. Jackets make ~Rs 17k GP each, so the fix is worth more than any ad.*
6. **Weekly test calendar (section 5)** and the Founder films the desk demo + patina clip by Dec 6. *[Alex lens] Yes. Volume of real proof beats clever copy; one test a week, judged on Shopify orders.*

## Not verified
- Whether the `bf_clifford` creative shows a sale price or the sale name (check before Nov 30).
- Mocha restock date; gloves and hat sellable stock per size on Dec 1.
- Full-price hat ceiling (CFO). Retarget v2 has too little spend (~Rs 1.1k) to judge; the 7-day ad set numbers above still include the old, now-rejected ad.
- Meta figures are Meta-reported (over-report ~2.05x); Shopify-confirmed per-ad orders come at the Dec 1-3 read.
