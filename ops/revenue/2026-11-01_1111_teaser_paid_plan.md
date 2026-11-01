# 11.11 teaser: paid plan (cold, Nov 3–9) and handoff to the sale (Nov 10–12)
CRO (Sana Iqbal), Nov 1 2026. **L3 proposal only. Nothing has been changed in Meta.** Account `995683712074843` only.
Live reads: Meta `ads_get_ad_entities`, ad set and campaign level, Nov 1 2026 (`last_7d` = Oct 25–31, `yesterday` = Oct 31).

**Decision:** Run one new cold ad set optimised for **ThruPlay** (not Purchase) carrying both teaser cuts, at **PKR 1,000/day on top of the current 5,340/day**, Nov 3 00:00 to Nov 9 23:59 PKT. Bank viewers in a new audience **"KV — 11.11 Teaser ThruPlay 30D"**. On Nov 10–12 retarget them in their own small sale ad set (RT-T), not inside Retarget.
**Rupee impact:** Spend **7,000** (1,000 × 7 days). It pays back only if the pool brings **7 extra surviving wallet orders** (7,000 ÷ ~1,000 per order, A3), plus RT-T's own spend. That means the pool must convert at **cost per ThruPlay ÷ 1,000**: 0.37% at 3.73, 0.88% at 8.77. Each surviving sale wallet order returns about 725–1,250 (11.11 plan, Nov 1).
**Confidence:** High on budgets, IDs and benchmarks (read live today). Low on payoff: 3 sale days at roughly 1 order/day is Poisson noise, and incrementality cannot be cleanly isolated.
**Risk:** Cheap attention that never buys. TOF-J bought jacket viewers at PKR 1.16 each and converted clicks to cart at 0.31% (CLAUDE.md, Sep 13 2026). A teaser pool can repeat that pattern.
**I need from you:** (1) Yes/no on **+1,000/day, Nov 3–9, total 7,000** (L3) by **Nov 2, 18:00 PKT** so it can start Nov 3. (2) Yes/no on creating the audience and, on Nov 10, an **RT-T ad set** sized to the pool (≈250–600/day, §4). Its budget comes out of whatever you decide for the open 5,000/day sale question. I am not deciding that here. (3) From the CMO by Nov 2: final cut lengths and 9:16 + 4:5 versions.

| Item | Value | Source, date |
|---|---|---|
| Live total now | **5,340/day** = Retarget 1,000 + TOF-M H1 1,500 + H3 500 + TOF-W 1,500 + RT-W 840 | Meta, Nov 1 2026 |
| TOF-M H1 (cold LLA, video): cost per ThruPlay · CPM | **3.73 · 264.38** (1,981 ThruPlays / 27,918 impr = 7.1%) | Meta last_7d, Nov 1 |
| TOF-M H3 (cold LLA, video): cost per ThruPlay · CPM | **8.77 · 448.78** (776 / 15,165 = 5.1%) | Meta last_7d, Nov 1 |
| Retarget CPM (warm) | **323.79**, freq 2.86 | Meta last_7d, Nov 1 |
| Cold CPM benchmark | 416–492 | ADS_PLAYBOOK_PK.md §2 |
| Teaser budget / days / total | 1,000 · 7 (Nov 3–9) · **7,000** | proposal |
| Pool if ThruPlay cost = H1 … H3 | 7,000 ÷ 3.73 = **1,877** … 7,000 ÷ 8.77 = **798** ThruPlays | derived |
| Kill line (day 3, Nov 6 read) | cost per ThruPlay **> 9** or CPM **> 500** | proposal |

## Assumptions
- **A1. The teaser's ThruPlay cost will be no worse than TOF-M's.** TOF-M optimises for Purchase, so its 3.73–8.77 is only a ceiling benchmark. *Replace with:* the teaser's own day-3 read (Nov 6).
- **A2. ThruPlays ≈ people.** The audience counts people. One person can be counted more than once in ThruPlays, so the real pool is **≤ 798–1,877**. *Replace with:* audience size in Ads Manager on Nov 9.
- **A3. Each surviving sale wallet order is worth ~1,000.** The middle of the 25%-off table: Bastion 725 · KODO/Luke/Plain/Shelby 850–1,000 · Razor 988 · Mocha Mate 1,250 (after cost + 200 delivery, 11.11 plan Nov 1). Non-wallet lines at 15% off are worth more per order. *Replace with:* RT-T's actual order mix on Nov 26.
- **A4. A ThruPlay ad under the Engagement objective can carry a website link and CTA.** *Test:* check during the build. If it cannot, use Awareness with a ThruPlay goal and accept fewer site visits.
- **A5. Excluding Audience Network** lowers accidental views. This is a general platform pattern, not measured in this account. *Test:* none needed. The cost of excluding it is small.

## Detail
### 1. Objective and event: ThruPlay
- **Why not Purchase:** there is nothing at the sale price to buy until Nov 10, so a Purchase-optimised teaser would chase full-price buyers, which is TOF-M's job. Purchase also needs ~50 results a week to exit learning (playbook §5). At 1,000/day it never would.
- **Why ThruPlay rather than Reach or 2s views:** Reach buys exposures, not attention. A 2s view is a scroll. ThruPlay (15s, or the whole video if shorter) is the cheapest signal that a person watched, and it makes a good retarget seed.
- **Learning arithmetic:** at the 9 kill line, 1,000 ÷ 9 = 111 ThruPlays/day = 777/week, far above 50. It exits learning in about a day, so the day-3 read is a fair one.
- **Build:** campaign "TEASE | 11.11 Teaser | ThruPlay | Nov 2026", objective **Engagement** (video views), ABO, **one ad set, both cuts as 2 ads**. Meta picks the winner, and one larger ad set is better than two small ones (playbook §5). Not OUTCOME_SALES. If any sales objective is used, clear the injected catalogue (`promoted_object:{}`) and read it back (CLAUDE.md, Oct 24).
- Link → `/collections/kdv-wallets`, UTMs `utm_source=facebook&utm_medium=paid_social&utm_campaign=tease_1111_nov26&utm_content={{placement}}`. **No discount code and no "% off"** in creative (design choice: the offer is not live until Nov 10; not a CLAUDE.md hard rule, CQRO fix Nov 1). No Karachi. No COD claim (jackets and footwear are in the 15%).

### 2. Budget
- **1,000/day, Nov 3 00:00 PKT (Nov 2 19:00Z) → Nov 9 23:59 PKT (Nov 9 18:59Z), total 7,000.** Each day the creative is late cuts 1,000 and about a day of pool. Do not extend into Nov 10: on Nov 10 the creative is wrong.
- **On top, not replacing.** Account goes 5,340 → **6,340/day** for 7 days. Why not trim:
  - TOF-W and RT-W went live Oct 31 (spend 270 / 158 on Oct 31 only). Touching them before Nov 3 breaks the 72h rule.
  - Retarget is the best ad set in the account (4.32x real, Aug audit).
  - TOF-M H1 is the cheapest cold video in the account (3.73 per ThruPlay, 9 Meta purchases in 7 days). The Mocha Mate stock trim is moot: the Founder said a restock lands in a few days (CLAUDE.md, Nov 1).
- The **5,000/day sale-window question stays open.** This plan ends Nov 9, so it does not overlap with it.

### 3. Audience and placements
- **9 cities by key, no radius**, `location_types [home, recent]`. Age 18–65. Advantage+ audience OFF.
- **Include:** LLA 1% `120254216730060428` + LLA 3% `120254216735280428` (Value, All Delivered [Jul31]). These are the live cold audiences on TOF-M and TOF-W. I recommend them over broad because the pool's job is to buy on Nov 10, and the seed is delivered buyers. Note: they overlap with TOF-M and TOF-W in the auction.
- **Exclude:** COD Refusers `120253660257910428` · Purchasers 180D `120252468019140428` · Delivered SEED `120254215371460428` · **All Website Visitors 180D `120252468018150428`**. Retarget already reaches every one of these groups, so the teaser pays only for **new** people.
- **Placements:** Facebook + Instagram, all positions including FB Reels (do not exclude it, CLAUDE.md Aug audit). **No Audience Network or Threads** (A5). Retarget currently serves on both, for comparison.

### 4. Handoff: the audience and RT-T
- **Create now (free; it fills as views come in):** video engagement audience **"KV — 11.11 Teaser ThruPlay 30D"**. Source = both teaser videos, "people who watched to ThruPlay", 30-day retention. 30 days covers **Black Friday (Nov 27)** too (Nov 3 + 30 = Dec 3).
- **On Nov 10, a new ad set "RT-T | 11.11 Teaser Viewers | Purchase"** with the sale creative. Include the teaser audience. Exclude Website Visitors 180D, Purchasers 180D, Delivered SEED and COD Refusers, so it does not overlap with Retarget. Anyone who clicked through the teaser is already in Retarget's pool.
- **Why not add it inside Retarget or RT-W:** `targeting` is a full replace and a significant edit. It would reset Retarget's learning on day 1 of the sale. It would also make the teaser unmeasurable, because Meta cannot split results by inclusion audience.
- **Size RT-T to the pool, not to a round number:** budget/day = pool × 3 frequency × CPM ÷ 1,000 ÷ 3 days. At Retarget's CPM of 323.79: 1,877 people → **608/day**; 798 → **259/day**. Use the real Nov 9 audience size.

### 5. Kill and measure rules (written before launch)
- **Day 3, read Nov 6 ~10:00 PKT on Nov 3–5 (~3,000 spent): kill if cost per ThruPlay > 9 or CPM > 500.** Why: 9 is just above the worst live cold video (H3, 8.77). 500 is just above the cold CPM benchmark top (492). **If it fires:** stop. The loss is capped at ~3,000, and the ≥333 ThruPlays already banked (3,000 ÷ 9) stay usable for RT-T. Learning is not an issue (777/week at the line). Also note the ThruPlay rate against H1 7.1% and H3 5.1%. Below 5% means the creative is weak, which is a CMO note and not a kill.
- **No edits Nov 3–5** (72h rule). Day 5 (Nov 8): if cost per ThruPlay is still above 9, stop. There is too little time left to fix it.
- **What I read on Nov 10–12 (daily, with the 11.11 checks):** RT-T spend, reach and frequency. Shopify orders tagged with RT-T's UTM and `tease_1111_nov26`, with their cancellations. Teaser-click orders Nov 3–9 (full price) are counted too.
- **The payoff verdict comes at day 14 (Nov 26), not on Nov 12:** surviving contribution of RT-T + teaser-tagged orders ≥ **7,000 + RT-T spend**. Per unit: each surviving wallet order ≈ 1,000 (A3). Only ~47% of cancellations land by day 8 (CLAUDE.md, Sep 9), so a Nov 13 read will flatter it.
- **Rung:** judge on surviving Shopify revenue. Meta-reported purchases are shown alongside, never instead. The ~2.05x overstatement factor is from August and is not re-derived for November.

### 6. Data conflicts and notes for the CEO
- **IDs:** CLAUDE.md (Nov 1) lists TOF-W `120255846370500428` and RT-W `120255846370710428` as ad sets. Live, those are **campaign** IDs. The ad sets are `120255846373560428` (TOF-W; budget 1,500 held at campaign level) and `120255846373980428` (RT-W, 840).
- **Location types:** TOF-M, TOF-W and RT-W run `frequently_in + home + recent`. Retarget and the documented standard are `home + recent` (CLAUDE.md, TOF-J). This plan uses `home + recent`. Whether to align the others is a separate question.
- The 11.11 plan's F2 check 6 says "spend flat at today's 4,000/day". Live spend is 5,340, or 6,340 if this is approved. That line needs updating.
- **Council asks:** CFO, confirm the ~1,000/order wallet contribution floor (A3). CMO, provide cut lengths and both aspect ratios. If both cuts are under 15s, ThruPlay means a full watch. COO: none (no stock is sold Nov 3–9).
