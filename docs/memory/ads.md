# Meta ads history: audits, ad sets, IDs, reads

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

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

## 🧥 TOF-J — the jacket view-builder (🟢 LIVE Sep 5 2026, user-approved)
> ✅ **ACTIVATED Sep 5 2026** (campaign + ad set + ad all ACTIVE) and **BOF DPA
> `120254220299340428` PAUSED the same minute** to fund it — verified live: DPA
> `effective_status: PAUSED`. Account now runs THREE ad sets at PKR 1,000/day each
> (Retarget · TOF-C · TOF-J) = **unchanged PKR 3,000/day total**. Nothing else moved.
> ⏳ The ad enters Meta review on activation; first delivery is usually within a few hours.

Purpose: jackets are structurally starved inside the shared "All Products" set (70 wallets vs
8 jackets served in August). This is the first ad set that can only ever show a jacket. It is a
**pool-builder for October**, not a September revenue play — the season curve is flat until Oct.
- Campaign **`120254923437380428`** "TOF-J | Jackets Catalogue | Sep 2026" · OUTCOME_SALES · ABO.
- Ad set **`120254923438760428`** "TOF-J | Jackets Cold | View Content" · PKR 1,000/day ·
  `OFFSITE_CONVERSIONS` + `custom_event_type: CONTENT_VIEW` (**View Content, NOT Purchase**) ·
  billing IMPRESSIONS · destination WEBSITE · Highest volume.
  🔴 **Why View Content:** at ~PKR 8,450 jacket CPA, Purchase optimisation needs PKR 400k+/week
  to hit 50 conversions and can NEVER exit learning. VC costs ~PKR 30–60, so 1,000/day clears
  the 50/week bar comfortably. **Flip to Purchase in October, not before.**
- Ad **`120254934279270428`** · creative **`1565804588611384`** · Advantage+ catalog carousel.
  🔁 **Swapped Sep 6 2026.** The original ad `120254923440130428` / creative
  `1753964692388815` promised "4–7 working days on the bench, 3–4 to your door" — false
  once the workshop moved to ~15 days of making. **Ad creatives are IMMUTABLE in Meta**, so
  the fix is always: new creative → new ad in the same ad set → pause the old ad. Never try
  to edit copy in place. v2 says "around three weeks to your door" and names peak season as
  the reason. Old ad + creative kept, paused, for the record.
- Product set **`1801176350880581`** "KV — All Leather Jackets (Men's + Women's)" = 30 products
  (186 variant items), OR of Shopify collections `438804021488` + `438804250864`. Dynamic, so
  new jackets join automatically. This is the FIRST jacket-only set — do not point it at
  "All Products" `608788148654460`.
- Targeting mirrors TOF-C exactly: 9 city keys, **no radius**, `location_types [home, recent]`,
  LLA 1% `120254216730060428` + LLA 3% `120254216735280428`, excludes Purchasers 180D
  `120252468019140428` + COD Refusers `120253660257910428` + Delivered Buyers SEED
  `120254215371460428`, `publisher_platforms [facebook, instagram]`, `advantage_audience: 0`.
  ⚠️ **The live LLA IDs above are the [Jul31] versions — they DIFFER from the Jul 8 IDs recorded
  in the Meta Ads section. Always read the live ad set, never copy IDs from memory.**
- ✍️ Copy deliberately **fixes the DPA creative defect**: no "cash on delivery anywhere in the
  country". It states made-to-order + paid online WITH the reason ("cut for one customer and can
  never be resold"), and names the ~3 week timeline instead of a delivery-area claim.
  No `PAYONLINE10`. Advantage+ Creative left OFF so Meta cannot rewrite the brand voice.
- 🔗 `link_url` carries real UTMs incl. `utm_content={{placement}}` — the first ad in the account
  that does. ⚠️ **Verify on the first real click** that `{{placement}}` resolved and did not land
  as a literal string (TOF-A had that failure). If it comes through literal, the fallback is a
  static `utm_content` naming the ad set.
- 💰 **Funded by pausing BOF DPA `120254220299340428`** (PKR 1,000/day): real ROAS 1.33x against
  a 2.22x break-even, −PKR 12,396 August contribution, frequency 8.10 on 11,739 reach, and
  September burning ~3x faster (2.63 freq in 4 days). Retarget (4.32x) and TOF-C (2.81x) are
  untouchable. The fit is exact: **DPA is starving because nothing fresh feeds its pool** — TOF-J
  refills that pool, so October's DPA restart has an audience to retarget.
- 📌 Kill threshold written BEFORE launch (the Aug process gap): if cost-per-ViewContent is above
  **PKR 90** on day 3, or above PKR 70 on day 7, kill it. Judge on 14-day windows otherwise.

### 📈 TOF-J day-2 read (Sep 5–6 2026) — PASSES the kill test by 58x, one flag
Spend 1,858.69 · impr 16,404 · reach 13,067 · freq 1.26 · **CTR 7.80%** · **CPC PKR 1.45** ·
**CPM PKR 113** · 1,177 link clicks → 1,015 landing-page views → **1,200 ViewContent** → 1 ATC → 0 purchases.
- ✅ **Cost per ViewContent = PKR 1.55 against a PKR 90 kill line.** Not remotely close to killing.
  CTR 7.80% and CPC PKR 1.45 both beat last season's best in the account (Advantage+, 6.43% / 9.75).
- 🔴 **MY PRE-LAUNCH ESTIMATE WAS WRONG BY ~30x AND THE PLAN CHANGES BECAUSE OF IT.** I forecast
  "PKR 30–60 per ViewContent, 500–900 viewers over all of September, right on the 1,000 minimum".
  Actual: PKR 1.55, **1,200 viewers in two days**. The retargeting pool is already big enough.
  ➡️ Consequence: TOF-J does **not** need to run all through October to sustain the pool, and the
  October DPA restart can happen much sooner than planned. Re-plan off measured cost, not the estimate.
- ⚠️ **THE ONE FLAG: click→ATC is 0.078% (1 of 1,280).** TOF-C is 4.98% and Retarget 3.28% on the
  same days. Cheap traffic that does not add to cart is a pool of scrollers, not buyers.
  🚫 **Do NOT conclude from this yet — n=1 add-to-cart.** Jackets are a PKR 28,000 considered
  purchase against TOF-C's mostly PKR 3,000 wallets, so a large gap is expected; the question is
  whether it is *this* large. **Re-read at day 7 (Sep 12) with ~4,000 clicks behind it.**
  ➡️ If click→ATC is still under ~0.5% at day 7, switch the optimisation event from ViewContent
  to **Add to Cart**: cost per event rises a lot, the pool shrinks, but it becomes people who
  actually considered buying. That is the trade the October retarget needs.
- 🚫 **DO NOT TOUCH THE AD SET BEFORE SEP 12.** August lost money to 7 learning resets in 11 days.
- Placements (spend share): FB Feed 50% (CTR 8.56%, CPC 1.20, the only ATC) · FB Reels 25%
  (7.17%, 1.43) · IG Feed 9% · IG Reels 7% · IG Stories 6% (**CTR 14.77%**, highest, small volume) ·
  FB Reels Overlay 3% (1.18% CTR, the weakest). 🚫 Do not exclude Reels Overlay on PKR 47 of
  spend — Breakdown Effect, and the standing rule against cutting placements on average cost.
- ⏳ `utm_content={{placement}}` still UNVERIFIED — needs a real order from TOF-J and there are
  none yet. Check on the first one.
- ⚠️ Both moves (activating TOF-J, pausing BOF DPA) are LIVE money changes → confirm each time.

### 📈 TOF-J day-7/8 read (Sep 5–12 2026, run Sep 13) — HOLD. Do not switch the event yet.
Spend 7,600.32 · impr 108,374 · reach 63,646 · freq 1.70 · **CTR 6.55%** · **CPC PKR 1.07** ·
**CPM PKR 70** · 6,390 link clicks · **6,578 ViewContent** · 20 ATC · **2 purchases** (Sep 9, Sep 11) ·
Meta ROAS 2.22x · cost per purchase 3,800.
- ✅ **Cost per ViewContent = PKR 1.16 against the PKR 70 day-7 kill line — passes by ~60x.**
  The pool-building job is DONE many times over: 6,578 jacket viewers banked for October against a
  ~1,000/week target. First 2 purchases also landed (there were 0 at day 2).
- 🔴 **THE DAY-7 RULE SAID "SWITCH TO ADD TO CART IF click→ATC < 0.5%". IT IS 0.313%, SO THE RULE
  FIRES — AND THE RULE IS WRONG. DO NOT SWITCH. The rule did not do the learning-phase arithmetic.**
  Cost per ATC is **PKR 380**, so at PKR 1,000/day that is **~18 ATC/week against the ~50 Meta needs
  to exit learning**. Switching parks TOF-J permanently in learning — **the exact trap that ruled out
  Purchase optimisation when this ad set was designed**. Sensitivity-checked: even if ATC optimisation
  halved cost-per-event it only reaches ~37/week. Still short.
- 📈 **The rate is also climbing on its own as Meta learns** — 0.078% at day 2 → **0.41% over the last
  four days**, approaching the 0.5% line without any intervention:
  | Sep 6 | Sep 7 | Sep 8 | Sep 9 | Sep 10 | Sep 11 | Sep 12 |
  | 0.09% | 0.36% | 0.14% | 0.59% | 0.22% | 0.35% | 0.49% |
- ➡️ **THE DECISION: hold ViewContent at PKR 1,000/day. Make the event change at the OCTOBER RAMP**,
  when the budget rises enough to sustain ATC or Purchase optimisation properly. That also puts the
  unavoidable learning reset BEFORE the season instead of during it. ⚠️ To run ATC at 50 events/week
  at today's PKR 380/ATC would need roughly **PKR 2,700/day** — do not do that in flat season.
- ✍️ **Lesson for any future pre-written threshold: pair the trigger with the arithmetic of what
  happens when it fires.** A kill/switch rule that cannot be executed without breaking learning is
  not a rule, it is a trap. Check events-per-week at the target budget BEFORE writing the threshold.
- Same window, other ad sets: **Retarget** 7,931 / 10 purchases / 5.73x / cost 793 ·
  **TOF-C** 7,854 / 11 purchases / **16.84x** / cost 714 (up from 6.38x the week before).
  ⚠️ **Do NOT get excited about TOF-C's 16.84x on 11 orders** — this ad set has form for one large
  order carrying a whole window (a single PKR 51,450 order was 25% of its August revenue). 14-day
  windows only.
- ⏳ `utm_content={{placement}}` is now CHECKABLE — TOF-J has its first 2 orders. Still unverified.

## 📊 SEP 1–8 vs AUG 1–8 LIKE-FOR-LIKE (measured Sep 9 2026 — the account turned profitable)
User: *"hows our ad perfromance going for all ads running this month against the performance within
same dates last month"*. Both windows reconcile EXACTLY to account totals (25,772.96 / 45,176.22),
so the ad-set splits below are complete — no missing spend.
| | Aug 1–8 | Sep 1–8 | |
|---|---|---|---|
| Spend | 45,176 | **25,773** | −43% |
| Meta-reported revenue | 149,179 | **143,099** | **−4%** |
| Meta ROAS | 3.30x | **5.55x** | +68% |
| Purchases | 37 | 20 | −46% |
| Cost per purchase | 1,221 | 1,289 | +6% |
| Link clicks | 3,211 | 5,202 | +62% |
| CPM | 404 | 240 | −41% |
| Adds to cart | 118 | 88 | −25% |
- 🎯 **THE HEADLINE: spend fell 43% and Meta revenue fell only 4%.** Every other number is a
  consequence of that. Do not read the purchase drop as decay — see the next bullet.
- 🔴 **THE PURCHASE DROP IS ONE DECISION, NOT DECAY. It is TOF-A Mocha Mate being paused Sep 1.**
  In **Aug 1–8 TOF-A did 17 purchases at 4.86x, cost per purchase 706** — it was that week's volume
  engine. TOF-B Razor's 3 (at **0.68x**) also went, correctly. The 20 remaining purchases all come
  from ad sets running 3.49–9.22x. Volume was traded for quality and the money says that was right.
- Per ad set (spend / purchases / Meta ROAS):
  | **Sep 1–8** | Retarget 8,207 / 9 / **9.22x** · TOF-C 8,084 / 7 / 6.38x · DPA 4,536 / 4 / 3.49x |
  | | TOF-J 3,763 / 0 / — · TOF-A 1,182 / 0 (residual, paused Sep 1) |
  | **Aug 1–8** | TOF-B 12,007 / 3 / **0.68x** · TOF-A 12,000 / 17 / 4.86x · Retarget 11,997 / 11 / 3.85x |
  | | DPA 7,975 / 6 / 4.58x · Cold LLA 1,197 / 0 |
- 🔴 **TWO ACCOUNT-LEVEL NUMBERS ARE MIX ARTEFACTS — do not act on either.** TOF-J is 57% of all
  link clicks at a CPM of 83, so it drags every account average:
  - **click→ATC "collapsed" 3.67% → 1.69%.** Ex-TOF-J it is **3.68% — identical to August.**
    **Nothing regressed on the PDPs.** Never quote the account-level ATC rate while TOF-J runs.
  - **CTR/CPC "improved" hugely.** The REAL, ex-TOF-J improvement is link CTR 2.87% → **3.58%**
    and cost per link click 14.07 → **9.89 (−30%)** — genuine, and it comes from killing the
    expensive static/video sets (TOF-B CPC 30.95, TOF-A 28.57). Consistent with catalogue ≈4x cheaper.
- 💰 **ESTIMATED REAL PROFITABILITY — the account crossed break-even between these two windows.**
  Applying the standing ~2.05x Meta overstatement: **Aug 1–8 ≈ 1.61x real (BELOW the 2.22x
  break-even at 45% GM) → est. −PKR 12,400. Sep 1–8 ≈ 2.71x → est. +PKR 5,600.** An ~18,000 swing
  in eight days. ⚠️ **Directional only** — the 2.05x factor was measured on MATURE August cohorts
  and the September orders are days old. Re-derive it from Shopify before quoting as fact.
- 🔴 **SEPTEMBER'S SURVIVAL WILL FALL — the cohort is too young to judge, and this trap is easy to
  fall into.** Store-wide Sep 1–8 = 41 orders / 374,369 placed / 8 cancelled so far → 226,819
  surviving. Aug 1–8 = 48 orders / 187,872 placed / **15 cancelled** → 113,993 surviving.
  ✍️ **But at EQUAL AGE (day 8) August had only 7 cancellations** — the other 8 landed as late as
  Aug 22. So the honest read is **8 vs 7 = cancellation behaviour UNCHANGED**, and September's
  apparent 80.5% count-survival will settle nearer August's 68.8%. **Only ~47% of a window's
  eventual cancellations have landed by day 8 — never compare survival across cohorts of
  different ages.**
- ⏳ **TOF-J day-4 (Sep 5–8):** spend 3,763 · CTR **7.31%** · CPC **1.14** · CPM **83** ·
  2,976 clicks · 3,111 ViewContent → **cost per VC PKR 1.21 against the 90 kill line**.
  **click→ATC 0.20% (6 of 2,976)**, up from 0.078% at day 2 but still far under the 0.5% line set
  for the day-7 decision. ➡️ On this trajectory the **switch from ViewContent to Add to Cart
  optimisation is the likely call at the Sep 12 read**. Do not touch it before then.
- 🔮 **TOF-A deserves a retest but NOT yet.** It was the best ad set in this exact window last month
  and decayed later in August (which is why pausing on full-month data was right). ⚠️ **Its hero
  product The Mocha Mate Wallet still has no sellable variant**, so restarting it sends paid traffic
  to something nobody can buy. **Restock first, then retest** — this is the same "23 products
  invisible to catalogue ads" problem, and it is now blocking a proven ad set.

## 🚨 OCT 2026 — JACKET CHECKOUTS ARE DYING AT PAYMENT (measured Oct 21 2026)
The planned October ramp was NEVER executed: all 3 ad sets are still PKR 1,000/day, TOF-J is still on
ViewContent, BOF DPA still paused. Before ramping, the measurement below says DO NOT scale jacket spend yet.
- **Jacket demand is UP:** GSC "jacket" queries ~20 clicks/day (early Sep) → ~50/day (mid-Oct),
  impressions ~700 → ~1,600/day, position ~10 → ~7. TOF-J sent 14,535 jacket clicks Oct 1–20 at PKR 1.39.
- **Jacket sales COLLAPSED:** Oct 1–20 = 1 jacket order (KDV#22857, Rs 29,000, card) and it was
  REFUNDED next day — staff event log: *"waiting for customer's reply regarding jacket size and processing
  time"*. **Net jacket sales in October = 0.** (Late Sep: 5 orders / ~159k — so it worked before.)
- 🔴 **~19 jacket checkouts ABANDONED Oct 1–20, ≈ PKR 748,000** (address entered, then left). Many are
  9-city (Rawalpindi ×5, Lahore ×4, Islamabad ×2, Karachi, Hyderabad).
- ✅ **The card gateway is NOT broken** — XPay card/online orders complete daily on wallets, hats,
  laptop bags (incl. a 56,800 laptop-bag order Oct 21). The failure is jacket-specific.
- **Diagnosis (most → least likely):** (1) prepaid 100% + "about 3 weeks" on a Rs 25–35k cold purchase —
  the one paying buyer left over processing time; and every week further into the season the promised
  date slides later; (2) the known dead end — MTO cart still SHOWS the COD shipping rate, then COD is
  absent at payment; (3) TOF-J's cheap cold traffic (click→ATC 0.37% in Oct).
- ➡️ **Do not raise TOF-J / jacket budget until checkout completion recovers.** More traffic into a
  ~0% checkout is pure waste. TOF-J ViewContent pool (≈22k viewers Sep 21–Oct 20) is already huge.

## 🎯 RT-J — jacket retarget (🟢 LIVE Oct 21 2026, user-approved) · TOF-J PAUSED same minute
User: *"pause the TOF J and then retarget them as a purchase intent... follow a proper funnel"*.
TOF-J had banked ~27k jacket ViewContent events (Sep 5–Oct 20) and nothing was harvesting them.
- Ad set **`120255674363190428`** "RT-J | Jacket Viewers + ATC 30D | Purchase", inside the TOF-J campaign
  `120254923437380428`. PKR 1,000/day (TOF-J's budget moved over → account total unchanged at 3,000/day).
  `OFFSITE_CONVERSIONS` + **PURCHASE**, product set `1801176350880581` (30 jackets).
- ~~**Audience = `product_audience_specs`**~~ (REPLACED Oct 22, see below — it never delivered): ViewContent OR
  AddToCart on a jacket in the last 30 days, minus jacket Purchase 30d; also excludes COD Refusers
  `120253660257910428` + Purchasers 180D `120252468019140428`. 9 cities, no radius, FB+IG, A+A off.
- Ad **`120255674366650428`**, creative **`948984301258821`** (catalog carousel, Advantage+ creative OFF).
  ✍️ Copy targets the two objections the one refunded October buyer actually raised — **size** ("WhatsApp us
  on 0333 2601161 before you pay") and **processing time** ("about three weeks… winter is our busiest
  season"). Headline "Made for you. At your door in about 3 weeks." UTMs `utm_campaign=rtj_jackets_oct26`,
  `utm_content={{placement}}`. No COD claim, no discount, no guarantee (not approved yet).
- **TOF-J `120254923438760428` PAUSED** (verified `effective_status: PAUSED`). Restart cold only when RT-J
  frequency climbs above ~4 (pool exhausted) or once jacket checkouts are completing again.
- 🔴 **DAY-1 FAILURE + FIX (Oct 22 2026): RT-J had 0 impressions for ~20h** although campaign, ad set and ad
  were all ACTIVE with no errors and the pixel matched 99.99% (~1,000 jacket ViewContent/day).
  **The `product_audience_specs` (catalogue dynamic retarget) audience never started delivering.**
  ➡️ Replaced with a plain website custom audience, the same pattern the working Retarget ad set uses:
  **`120255689014190428` "KV — Jacket Page Visitors 30D (RT-J)"** = pixel URL i_contains `jacket` OR
  `hawkeye` (29 of 30 jacket handles contain "jacket"; Hawkeye's is `hawkeye-…-vintage-coat-s012`).
  Also catches the jacket collection pages. Prefill on. Ad set re-entered review (IN_PROCESS) Oct 22
  19:46 PKT. ✍️ **Lesson: for retargeting in this account, use a website custom audience,
  not `product_audience_specs`.** The catalogue ad still picks which jackets to show.
  ⚠️ If a jacket is ever added WITHOUT "jacket" in its handle, add it to this audience's rule.
- ✅ **FIX CONFIRMED Oct 23 2026: RT-J is delivering.** First ~day after the audience swap: spend 1,750 ·
  impr 4,991 · reach 3,018 · freq 1.65 · 297 link clicks (CTR ~6%, CPC ~5.9) · CPM 351 · 265 VC · 2 ATC ·
  2 IC · 0 purchases. Audience `120255689014190428` operation status 200 (Normal). Too early to judge.
- ⚠️ Purchase optimisation at 1,000/day will stay in learning — acceptable for a fixed retarget pool.
  **Do not touch it for 72h. Read day 3 (Oct 24) and day 7 (Oct 28).** The win condition is a COMPLETED
  jacket order, not CTR; the 19 October abandons say the bottleneck is checkout, so also watch
  abandoned jacket checkouts in Shopify alongside Meta's numbers.

### 📈 RT-J day-4 read (Oct 23–26 2026, run Oct 26) — ads deliver, checkout still kills jackets
Spend 5,388 · impr 12,788 · 752 link clicks (CTR ~7.5%) · 768 VC · **15 ATC · 9 initiated checkouts · 0 purchases**.
CPM rising 350 → 570 and daily reach falling 3,026 → ~1,300 = the 30-day pool is small and saturating.
- Shopify: **0 jacket orders Oct 11–26.** Abandoned since Oct 21: Rockafella + hat 40,300 (Islamabad) · The Ace
  27,750 (Quetta) · Ralph 24,500 (Sargodha) · Saachi shoe 21,000 (Lahore, also MTO) ≈ **PKR 113k at the payment step**.
- ➡️ Verdict unchanged from Oct 21: **it is a checkout/payment problem, not an ad problem.** Do NOT raise RT-J or restart
  TOF-J. Highest-ROI free fixes: (1) team phones the abandoners same day (size + timing objections); (2) build the
  delivery-customization Function that hides the COD rate on MTO carts (the dead end). Read RT-J again Oct 28.
- Same window: **TOF-M (Mocha Mate founder videos) is converting** — ~8 tagged orders Oct 24–25 incl. a 20,500 basket
  (h3_founder). Day-3 read due Oct 27.

### ⏹ JACKET ADS DROPPED (Oct 26 2026, user: *"just drop the jacket ads altogether, since people who want to buy with
intent will eventaully search for us on google"*). Campaign **`120254923437380428`** (TOF-J + RT-J) **PAUSED**, verified:
only TOF-M, Retarget and the TOF-C campaign (its ad set already paused) remain active. **Account now ~3,000/day**
(Retarget 1,000 · TOF-M H1 1,000 · TOF-M H3 1,000). Jackets still appear inside the Retarget catalogue ad (All Products set).
⚠️ Google search does NOT bypass the problem: ~50 organic jacket clicks/day also produced 0 orders in October — the
checkout/payment step is the blocker for every channel. Freed 1,000/day NOT reallocated (needs user OK).

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

## 🎬 TOF-M — Mocha Mate founder-video test (REBUILT Oct 24 2026, DRAFT — user attaches videos + publishes)
User: *"remove this campagin completely and create a new one step by step… budget should be 1000 per day for each
ad set… put in any dummy video for now as draft"*.
- 🔴 **WHY v1 BROKE (do not repeat):** `ads_create_campaign` silently injects `promoted_object.product_catalog_id`
  (catalogue `1015378560682303`) on OUTCOME_SALES. Ads Manager then applied *"value_defaulting_for_product_catalog_sales"*:
  added product set `608788148654460` to the ad sets, turned the ads into catalogue carousels (only "carousel" offered),
  **dropped the LLA inclusions and the COD-Refusers exclusion**. ➡️ **Fix: right after creating any non-catalogue sales
  campaign, `ads_update_entity` campaign `{"promoted_object":{}}`, then read the draft back** — it shows `promoted_object: []`.
- ✍️ Video ads: build with `ads_create_ad` inline `video_data` (video_id + image_hash thumbnail + title + link_description +
  `call_to_action{type,value{link}}`) and put UTMs in creative `url_tags`. `ads_create_creative` adds `link_title`/
  `link_description` inside the CTA value → Ads Manager error #1815589 (deprecated). Image ads: `image_url` → error 1443051.
- **Economics:** price 3,200 · COGS 950 · delivery 150–200 → GP ≈ 2,050 (64%) · break-even ≈ ~1,300 per Meta purchase.
  Stock checked: `mocha-mate` 43 units, sellable.
- 🔁 **FINAL (Oct 24, 3rd build): user deleted every earlier TOF-M draft and asked for campaign + ad sets ONLY, no ads.**
  Campaign **`120255717719930428`** (catalogue link cleared, `promoted_object: []`) · ad sets **`120255717721520428`** H1
  Comparison + **`120255717721900428`** H3 Founder Voice — same settings as below, verified VALIDATED with 0 errors.
  **User builds both ads in Ads Manager.** All older IDs below are dead.
  🟢 **PUBLISHED Oct 24 2026 by the user.** Ad sets ACTIVE at PKR 1,000/day each. User-built ads: `120255717749990428`
  "Comparison" (creative `1789159075513560`, VIDEO, ACTIVE) · `120255717819950428` "Foudner ad" (creative `1754735512261830`,
  VIDEO, IN_PROCESS = in Meta review at check). **Day-3 read Oct 27, day-5 Oct 29** against the kill rule below.
- Campaign **`120255717556140428`** "TOF-M | Mocha Mate Founder Videos | Oct 2026" · OUTCOME_SALES · ABO · no catalogue.
- Ad sets (each `daily_budget` 100000 minor units = **PKR 1,000/day**, OFFSITE_CONVERSIONS PURCHASE, pixel 1865080707652548,
  9 cities no radius, home+recent, LLA 1% `120254216730060428` + 3% `120254216735280428`, excl Purchasers 180D
  `120252468019140428` + COD Refusers `120253660257910428` + Delivered SEED `120254215371460428`, FB+IG all positions, A+A off):
  `120255717561830428` H1 Comparison · `120255717561920428` H3 Founder Voice.
- 🔁 **Oct 24 (later): user asked to build the ADS themselves.** Both API ads below set to DELETED in the draft;
  campaign + 2 ad sets kept and re-verified unchanged. User builds the ad level in Ads Manager.
  ✍️ Lesson: when the user is editing in Ads Manager, stop at the ad-set level — UI media swaps blanked the Website URL.
- (deleted) Ads: `120255717562610428` H1 (`utm_content=h1_comparison`) · `120255717564000428` H3 (`utm_content=h3_founder`).
  url_tags `utm_source=facebook&utm_medium=paid_social&utm_campaign=tofm_mochamate_oct26&utm_term={{placement}}`.
  Placeholder video on BOTH = account video `1134847245954824` "mocha mate new vs use dperpesctive.mp4" (the 64s master).
  User swaps in `Mocha_Mate_30s_v2.mp4` (H1) / `Mocha_Mate_30s_H3.mp4` (H3). Advantage+ creative features opted out.
- Leftover drafts to DISCARD in Ads Manager: `120255717326670428` "XX DISCARD — TOF-M broken (catalogue)" and
  `120255717554640428` "XX DISCARD — unused v2" (new drafts cannot be API-deleted, only discarded in the UI).
- 📌 Kill rule: per ad set ≥ PKR 2,600 spent with 0 purchases by day 3 → kill; day-5 CPA check vs ~1,300; no edits for 72h.

### 📈 TOF-M day-5 read (Oct 21–28 window, run Oct 28) — PASSES, the first cold winner in months
- Meta: **H1 Comparison** 4,480 spent · 8 purch · CPA **560** · 6.99x · CTR 3.30% · CPM 261 ·
  **H3 Founder** 4,556 · 7 purch · CPA **651** · 8.89x · CTR 3.22% · CPM 438. Both far under the kill line.
- Shopify (UTM tofm_mochamate_oct26 + one Facebook_UA order on the TOF-M campaign id): **~12 live orders,
  1 cancelled (the 20,500 h3 basket)**. ≈ PKR 750 per PLACED order vs Mocha Mate profit/placed ≈ 988
  (49% historical refusal) → profitable but not by much until deliveries confirm. Nearly all are COD (PENDING).
- 🔴 **The prepaid-rate gap is real and visible:** 5 TOF-M orders total 3,450 (= 3,200 + the 250 "Pay Online"
  rate) yet are PENDING COD. Customers pick the cheaper prepaid shipping and then pay cash anyway.
- 🔴 **Mocha Mate stock 29 units (DENY policy) on Oct 28** — at ~3–5/day all channels, ~1 week left.
  Restock BEFORE scaling TOF-M or the PDP sells out and the catalogue ads drop it.
- Retarget (Oct 21–28): 7,996 · 8 purch · CPA 1,000 · 5.21x · freq 2.93. Healthy, keep.

## ⏸ TOF-C PAUSED (Oct 24 2026, user-approved: *"ok pause the TOF-C"*) — verified `effective_status: PAUSED`
Ad set `120254472805020428`. Oct 11–24: spend 13,650 · 5 Meta purchases · CPA 2,730 · Meta 2.42x (≈1.2x real vs 2.22x
break-even) · only 3 UTM-tagged Shopify orders (7,400). Cold prospecting now = TOF-M H1/H3 (2,000/day).
**Account now 4,000/day:** Retarget 1,000 · RT-J 1,000 · TOF-M H1 1,000 · TOF-M H3 1,000.
Same review: Retarget 13,567 / 14 purch / CPA 969 / 3.71x / freq 3.85 (keep) · RT-J 0 jacket orders, read Oct 28 ·
**0 jacket orders store-wide Oct 11–24** · chatgpt.com sent 3 orders (2,200 / 4,700 / 6,600) at zero cost.


## 🧤 TOF-W — Winter Gloves (DRAFT, fixed Oct 31 2026, NOT launched)
- Campaign `120255841687880428` "TOF-W | Winter Gloves | Nov 2026" · CBO PKR 1,500/day · OUTCOME_SALES.
- Ad set `120255841689160428` renamed "TOF-W | Gloves | Cold LLA 1%+3% | Purchase". Fixed to the standard: 9 cities
  (no radius, home/recent/frequently_in), FB+IG only, A+A OFF, 18–65 all genders, LLA 1% `120254216730060428` + 3%
  `120254216735280428`, excl Purchasers 180D + COD Refusers + Delivered SEED, attribution 7-day click only.
- 🔴 The original 5 draft ads (…702210/702250/702280/702320/702390) had LOST their creatives (blank copy, no link,
  "See Details", W04 erroring "link required"), most likely from an Ads Manager UI edit. Creatives are immutable, so
  5 NEW ads were created from the intact creatives: W01 `120255841876800428` · W02 `120255841876850428` ·
  W03 `120255841877210428` · W04 `120255841877280428` · W05 `120255841877340428` (all 0 errors). Broken ones await
  discard (user confirmation required).
- Retarget drafts W-RT1 `120255841702480428` / W-RT2 `120255841702970428` in live Retarget ad set: VALIDATED, intact.
- ⚠️ Found on the LIVE TOF-M H1 ad set `120255717721520428` (Oct 31 read): NO lookalike inclusion and NOT excluding
  COD Refusers or Purchasers 180D (excludes only Kodo customers, Lifetime Fulfilled, Delivered SEED). Breaks the
  standing rule. Not changed (live money edit, needs user OK).
- Live Retarget ad set serves Audience Network + Threads too (all placements). Not changed.
- ✅ Oct 31: broken TOF-W drafts discarded. TOF-M H1 fix PUBLISHED and verified live (LLA 1%+3%, excl COD Refusers +
  Purchasers 180D added; re-review IN_PROCESS).
- 🆕 RT-W (DRAFT, user publishes it): campaign `120255841966670428` "RT-W | Winter Retarget | Nov 2026" (ABO, catalogue
  link cleared) · ad set `120255841974990428` PKR 300/day, Purchase, 9 cities home/recent, FB+IG, A+A off
  (custom-audience only), incl All Visitors 180D + ATC 180D + IC 180D + ViewContent 90D, excl COD Refusers + Purchasers
  180D · ads W-RT1 `120255841975560428`, W-RT2 `120255841975580428`. Old copies in the live Retarget ad set discarded.
  All 9 objects across TOF-W + RT-W read back VALIDATED with 0 errors.
- 🔁 Oct 31 (later): user DISCARDED ALL DRAFTS in Ads Manager (their browser showed a stale copy: old ad set name, no
  ads). Rebuilt from scratch, NOT published (user reviews + publishes):
  TOF-W campaign `120255846370500428` (CBO 1,500/day) · ad set `120255846373560428` · ads W01 `120255846376030428`,
  W02 `…376280428`, W03 `…376700428`, W04 `…376820428`, W05 `…376970428`.
  RT-W campaign `120255846370710428` · ad set `120255846373980428` (300/day) · W-RT1 `…377080428`, W-RT2 `…377130428`.
  All 11 objects VALIDATED, 0 errors; catalogue cleared on both campaigns; links resolve (brown 45, black 56 in stock).
  ⚠️ Lesson: API drafts and an already-open Ads Manager tab can disagree; tell the user to open Ads Manager fresh.
- 🔴 Oct 31: ads built from the placement-customised creatives (creative_id, asset_feed) showed EMPTY in the Ads
  Manager draft editor (no image/headline/description/URL params) and errored there, although the API read was fine.
  ➡️ Rule: for drafts the user reviews in Ads Manager, build ads INLINE (object_story_spec.link_data + image_hash +
  url_tags), never by referencing a PAC/asset_feed creative_id. Rebuilt all 7 inline (4:5 feed image only):
  TOF-W ads W01 `120255846508150428` W02 `…513420428` W03 `…513530428` W04 `…513600428` W05 `…513690428` ·
  RT-W W-RT1 `…513730428` W-RT2 `…513760428`. Old creative_id ads discarded.
- RT-W ad set budget had become 84000 (Rs 840) and custom-audience expansion ON after creation; reset to 30000 and
  expansion 0, re-verified.
