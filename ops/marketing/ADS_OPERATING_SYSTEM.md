# KORDOVAN Ads Operating System (v1, Nov 12 2026)
How we run Meta from now on: structure, tags, rules, analysis. Blessed Friday runs *inside* this system.
Companion files: `ops/ADS_PLAYBOOK_PK.md` (economics), `ops/marketing/CREATIVE_PLAYBOOK.md` (what sells, proven/lost).

---
## 1. Structure: 3 tiers by AUDIENCE, every tier optimises for PURCHASE
| Tier | Campaign | Who | Job | Ads in it |
|---|---|---|---|---|
| **TOF** cold | `KDV | TOF | Prospecting` | Advantage+ audience, 9 cities, excluding site visitors 180D, purchasers 180D, COD refusers | Find new buyers | Proven cold winners (Comparison) + up to 3 challengers |
| **TEST** (inside TOF) | `KDV | TOF | Test` ad set | same as TOF | One new idea a week vs the control | 1 challenger + 1 control |
| **MOF** warm | `KDV | MOF | Trust` | IG/FB engagers 90D + video viewers + site visitors 30D who did not add to cart | Remove doubt | Ordered vs Arrived, FAQ, real reviews, workshop, patina |
| **BOF** hot | `KDV | BOF | Close` | Add-to-cart / checkout 14D + product viewers 7D (+ catalogue) | Close the sale | Catalogue retargeting, Comparison, offers |
Rules: max 4 ad sets in total (budget too small to feed more); 3–6 ads per ad set; ABO (budget on ad sets) so each tier keeps its share; if the MOF audience is under ~50k, merge MOF into BOF.

**Budgets**
| Period | TOF | TEST | MOF | BOF | Sale | Total |
|---|---|---|---|---|---|---|
| Nov 16–25 (bridge) | 1,200 | 500 | 500 | 800 | – | **3,000** |
| Nov 26–30 (Blessed Friday) | 1,200 | 500 | 500 | 800 | **+2,000** BF (1,200 warm / 800 cold) | **5,000** |
| From Dec 1 | 2,000 | 500 | 1,000 | 1,500 | – | **5,000** |
Every ad set ≥ PKR 500/day (Meta's minimum ~495).

---
## 2. Every ad is TAGGED, so we can analyse by what is in it, not by its name
**Ad name = utm_content** (one code, so Meta and Shopify join exactly):
`{tier}_{product}_{format}_{hook}_{style}_v{n}`, e.g. `tof_mocha_comparison_value_studio_v1`, `bf_trolley_receipt_saving_lifestyle_v1`.

| Dimension | Allowed values |
|---|---|
| **format** | comparison · carousel · static · video · receipt · objection · orderedvsarrived · faq · closeup · ugc · countdown · ourmistake |
| **hook** (the first idea that stops the scroll) | value (price/worth) · saving (rupees off) · proof (it's real leather) · trust (COD/returns/what arrives) · status (look/identity) · gift · problem (coins, bulky wallet, cold hands) · deadline · craft |
| **style** | lifestyle (dark heritage scene) · studio (plain background) · real (phone photo/UGC) · textled (headline-dominant) |
| **product** | the handle short name (mocha, kodo, gloves, trolley, …) |
Every ad URL carries: `utm_source=facebook&utm_medium=paid&utm_campaign={tier}_{yyyymm}&utm_content={ad name}`.

---
## 3. What we measure, and in what order
| Stage | Metric | Read it for |
|---|---|---|
| Attention | thumb-stop / 3-sec view rate (video), CTR (link) | Is the HOOK working? |
| Interest | cost per landing-page view, add-to-cart rate | Is the PAGE / offer working? |
| Sale | **Shopify orders by utm_content**, real CPA, real revenue | Is the AD making money? |
| Truth (day 14) | **refusal / lost-order rate per ad** | Is it making *real* money? |
Meta's own purchase count is never used alone (it over-reports ~2.05x).

---
## 4. Decision rules: when to stop, when NOT to stop, when to scale
**Break-even (the CPA ceiling) is per PRODUCT, not one flat number:** ceiling = profit per PLACED order (net of COGS, delivery and that product's refusal rate). From `ADS_PLAYBOOK_PK.md` (Jul data, refresh due): Aristocrat ~3,000 · Bronco ~2,900 · Truckkr ~2,100 · Shelby ~1,500 · Plain Bifold ~1,500 · KODO ~1,100 · **Mocha Mate ~990** · Kodo Vertical ~970 · Bastion ~720 · Rigor Lite ~460. Gloves 1,000 (Founder). Bags: computed per line before BF.

| Situation | Action |
|---|---|
| New ad, < 1× its ceiling spent, no sale | **Do NOT stop.** Too early. |
| CTR (cold) < 0.6% after 3,000 impressions | Stop early: the hook failed (no need to wait for sales) |
| Good CTR + add-to-carts, no sale yet | **Do NOT stop** before 2× ceiling spent: the page/offer may need one more look |
| ≥ 1.5× ceiling spent, 0 Shopify orders | **Stop** |
| 7-day Shopify CPA > 1.3× ceiling (≥ 3 orders' worth of spend) | **Stop** (or move to a cheaper tier if it is a trust ad) |
| Winner has 1–2 bad days | **Do NOT stop.** Judge on 7 days, never on 1 |
| 7-day CPA ≤ 0.7× ceiling with ≥ 3 orders | **Scale** +20% budget, then wait 72h |
| Frequency > 3 (cold) / > 6 (warm) AND CTR down ≥ 30% vs week 1 | **Refresh**: new creative, same winning hook |
| Ad's refusal rate > account average + 10 pts (day 14) | **Stop even if CPA looks good** (it sells promises, not orders) |
Always: change at most once per 72h per ad set; batch edits; never pause an ad set without listing its ads (Nov 8 lesson); every pause/scale is L3 → the Founder says yes on the per-ad table.

---
## 5. Analysis cadence
| When | What | Output |
|---|---|---|
| Daily (inside check-ins) | Anomalies only: an ad over 2× ceiling with 0 orders, spend not delivering, bridge down | 1–3 lines |
| **Monday weekly read** | Per-ad 7-day table (Meta + Shopify + CPA vs ceiling) + breakdowns by **placement** (feed/stories/reels), **age/gender**, **city**, **device** + tag roll-ups (which format, hook, style win) | Table + recommendations → the Founder's yes |
| Day 14 per ad | Refusal rate joined to the ad (utm_content → order → PostEx outcome) | Truth column |
| 1st of the month | Scorecard → `CREATIVE_PLAYBOOK.md` (proven / lost); next month's tests chosen from the queue | Playbook update |
"Winning" = a pattern seen in ≥ 2 ads (e.g. "value hook beats status hook on cold for wallets"), not one lucky ad.

---
## 6. Blessed Friday inside the system (Nov 26–30)
- One extra ad set **BF | Warm** (1,200/day: visitors 180D + engagers 90D) with the carousel, R1 receipt, R3 objection, Our Mistake, S2 clutch.
- One extra ad set **BF | Cold** (800/day, TOF exclusions) with the carousel + R1.
- Tagged like everything else (`bf_…`), so the Dec 1–3 read answers: receipt vs objection vs carousel vs our-mistake, warm vs cold, feed vs stories.
- The tiers keep running underneath; BF ends Nov 30 23:59 and its learnings go into the playbook.

---
## 7. Before launch (owner · date)
1. **Refresh the per-product ceilings** with Aug–Oct data (profit per placed order, incl. refusal). CFO Ayesha · Nov 13–15. *Mocha Mate's last ceiling (~990) is BELOW the 1,300 we have been using; H1 at ~980 Meta CPA may be break-even at best. Verify first.*
2. Audience sizes for MOF/BOF (merge if MOF < ~50k). CRO Sana · Nov 15.
3. Build the 3 campaigns as DRAFTS with the naming + UTMs; carry H1 + W01 over by ID (keeps their history) only if their ceiling check passes. CEO · Nov 15.
4. Founder approves the draft (per-ad table) → live **Nov 16** at 3,000/day.
5. BF ad sets built Nov 23, live Nov 26 evening. Dec 1 → 5,000/day.
