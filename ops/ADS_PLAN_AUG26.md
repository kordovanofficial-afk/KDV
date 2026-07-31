# Kordovan — Ad campaign map, August 2026

Built Jul 31 2026 from the account's own data. Read `ADS_PLAYBOOK_PK.md` first —
the COD economics and per-product refusal rates there govern every number below.

Account in scope: **`995683712074843` (Kordovan 2025, PKR)** — only.

---

## 1. What is actually running today

| Campaign | What it really is | Spend/day | Verdict |
|---|---|---|---|
| KV \| Cold \| Wallet Launch | LLA 1%+3% value, 2 ads in ONE ad set | 3,300 | Restructure |
| **Retarget** | **NOT retargeting** — broad PK 18–65, Advantage+ Audience ON, no inclusion audience | 2,050 | Rename, trim, prove |
| KV \| Retarget \| Warm 30-180D | true warm audiences | PAUSED Jul 28 | Rebuild as MOF |

**There is no BOF (past-buyer) campaign and no working MOF.** The funnel is a
cold lookalike and a broad campaign wearing a retargeting label.

### The mislabelled campaign matters
`Retarget` (`120228534676850428` / ad set `120228534676860428`) has **no
`custom_audiences` at all** and `advantage_audience: 1`. Its excellent surface
metrics — CTR 4.18%, CPC 5.40, cost/LPV 7.56 — are what broad Advantage+ looks
like on a mature pixel: it buys the cheapest engaged users, many of whom were
going to convert anyway. Meta claimed 8 purchases in Jul 28–30; Shopify
first-click attributed **4**. Treat its ROAS as unproven until measured
incrementally, and do not scale it further on Meta's numbers alone.

---

## 2. 🔴 One ad per ad set — adopted as a rule

**Evidence, not theory.** In the cold ad set, Jul 28–31:

| Ad | Spend | Share | CTR |
|---|---|---|---|
| AD_Bastion_Cold_PatinaAngle | PKR 13,079 | **99.0%** | 2.30% |
| AD_Razor_Cold_RFIDHook | PKR 137 | **1.0%** | **3.62%** |

Razor has the **better CTR** and received **1% of the budget** — and its numbers
have not moved at all since Jul 30, meaning delivery stopped entirely. Meta
picked a winner on two days of conversion data and never revisited. There was
never a fair comparison.

**Rule: one ad per ad set. Test creative by swapping the ad, never by adding a
second ad alongside it.**

### The honest cost of this rule
Splitting ad sets splits conversions, and Meta wants ~50 per ad set per week to
exit learning. At ~PKR 2,000 CPA and ~5,900/day total, the whole account
produces roughly 3 conversions a day. **We cannot have many ad sets.**

**Therefore: hard cap of 5 active ad sets.** Accept that cold lives in extended
learning permanently — that is a real cost, paid deliberately, in exchange for
being able to tell which creative and which product actually works.

---

## 3. Proposed structure

### TOF — prospecting (smart wallets only)
Brand position: first smart-wallet brand in Pakistan. Cold traffic sells the
category, not the catalogue.

| Ad set | Product | Audience | Budget/day |
|---|---|---|---|
| TOF-A | **Mocha Mate** (3,200) | LLA 1% + 3% Value (All Delivered) | 1,500 |
| TOF-B | **Razor** (2,450) | same | 1,000 |

- Exclude on both: `KV — COD Refusers EXCLUDE`, `KV — All Delivered Buyers SEED`
  (never prospect an existing customer)
- One ad each. Mocha Mate leads on demand (69 orders/90d vs Razor's 21); Razor
  has the stock depth (81 vs 33) and an untested creative that out-CTRs Bastion.
- **Dropped from the paid push:** Luke (PKR 623/order, 50% refusal — worst of
  the set) and Kodo Vertical 2.0 (14 units left, demand collapsed from 248
  orders/yr to 19 in 90 days).
- **Bastion moves out of cold.** 405 orders/yr makes it the volume champion, but
  at ~PKR 720 profit per placed order it cannot carry a PKR 2,180 cold CPA.

### MOF — warm non-buyers
The rebuilt version of the paused campaign. **Strictly non-buyers**, so it can
never bid against BOF for the same person.

- Include: All Website Visitors 180D, ATC 180D, IC 180D, ViewContent 90D
- Exclude: `KV — All Delivered Buyers SEED`, `KV — COD Refusers EXCLUDE`
- Product: smart wallet range
- Budget: **800/day**

### BOF — past buyers ← the missing campaign
The new seed audience is also the best bottom-funnel audience the account has
ever had: **9,600–11,300 proven buyers**, value-weighted.

- Include: `KV — All Delivered Buyers SEED value Jul31` (`120254215371460428`)
- Exclude: purchasers in the last 30 days (do not pester a fresh customer)
- Product: **full catalogue, high ticket** — bags, jackets, briefcases
- Budget: **1,200/day**

Why this is the highest-confidence line item: **24% of customers return every
month, reliably, for a year**, and blended AOV is ~PKR 5,300 against a wallet
AOV of 2,500. Returning customers are exactly who buys the expensive things.
This campaign is how the 24% gets monetised deliberately instead of by accident.

### BROAD — the current "Retarget", renamed
- Rename to `KV | Broad | Advantage+ PK` so nobody reads it as retargeting again
- Keep the refuser exclusion; add the buyer exclusion so it stops re-buying
  customers that BOF now owns
- Budget: **1,400/day** (down from 2,050) pending an incrementality read

### Budget summary — same total, properly split

| | Now | Proposed |
|---|---|---|
| TOF Mocha Mate | — | 1,500 |
| TOF Razor | — | 1,000 |
| Cold (Bastion, single ad set) | 3,300 | — |
| MOF warm non-buyers | 0 | 800 |
| **BOF past buyers** | **0** | **1,200** |
| Broad (ex-"Retarget") | 2,050 | 1,400 |
| **Total** | **5,350** | **5,900** |

5 ad sets. At the cap.

---

## 4. Placements — from this account's data

Cold, Jul 28–30, after the first placement cut:

| Placement | Spend | CTR | Cost/LPV | Purch | Action |
|---|---|---|---|---|---|
| Feed | 4,758 | 2.80% | **33.98** | 3 | **Keep** — the workhorse |
| Instagram Reels | 3,859 | 1.53% | 57.60 | 1 | Keep, watch |
| **Instagram Stories** | **733** | 1.84% | **66.62** | **0** | **CUT** |
| Facebook Stories | 159 | **7.26%** | **26.42** | 1 | **Keep** — best rate |
| Instream video | 300 | 5.72% | 33.36 | 0 | Keep |
| Facebook Reels | — | — | — | — | already cut |
| Audience Network | — | — | — | — | already cut |

Instagram Stories absorbed the budget freed by the Reels cut and got worse
doing it (was PKR 285 at 25.92/LPV before, now 733 at 66.62 with no sales).

**Standing placement set for all new ad sets:**
Facebook — feed, profile_feed, marketplace, video_feeds, story, search,
instream_video. Instagram — stream, explore, explore_home, reels, profile_feed,
ig_search. **No Instagram Stories, no Facebook Reels, no Audience Network,
no Messenger.**

⚠️ Threads cannot be set via the API — every value tried for
`threads_positions` is rejected. It had the best cost/LPV of any placement
(9.05) on a tiny sample. Worth revisiting by hand in Ads Manager.

---

## 5. Kill thresholds — per product, not per campaign

Ad spend is incurred per order **placed**; refusal decides whether it ever
becomes revenue. Maximum break-even CPA by product (from `ADS_PLAYBOOK_PK.md` §6):

| Product | Max CPA |
|---|---|
| The Aristocrat | 3,005 |
| Bronco Handcrafted | 2,913 |
| The Truckkr | 2,106 |
| Shelby & Thomas | 1,500 |
| RFID Protected KODO | 1,128 |
| The Razor | 1,029 |
| Mocha Mate | 988 |
| Kodo Vertical 2.0 | 968 |
| Bastion | 720 |
| Rigor Lite | 462 |

**Current cold CPA is PKR 2,180 — above every product in the TOF set.** TOF is
therefore an explicit customer-acquisition loss, justified only by the 24%
repeat rate and the BOF campaign that monetises it. That is a decision, not an
accident, and it must be reviewed monthly against actual repeat behaviour.

The single biggest lever is not targeting. It is **refusal**: the TOF products
average ~41%. If WhatsApp confirm/cancel takes that to 25%, profit per placed
order rises from ~910 to ~1,400 and TOF approaches break-even on the first
order alone.

---

## 6. Measurement — non-negotiable

1. **Judge on delivered orders in Shopify**, never Meta's purchase count.
2. **Weekly first-click check.** `customerJourneySummary.firstVisit.utmParameters`
   vs Meta's claims. Established: cold matches Meta exactly; the broad campaign
   is overstated ~2.6x.
3. **Per-product refusal rate monthly** — Shopify `returns` grouped by product.
4. Review the whole map monthly; refresh the seed audience quarterly.

---

## 7. Launch order (after the user reviews)

1. Swap cold onto the new lookalikes (queued — waiting on population)
2. Cut Instagram Stories from cold
3. Build BOF — highest confidence, lowest risk, currently zero spend
4. Split TOF into Mocha Mate and Razor, one ad each; retire the Bastion cold ad
5. Rebuild MOF
6. Rename and trim Broad

---

## 8. Retarget budget sizing — rule, not a number (set Jul 31 2026)

**Set to PKR 1,500/day** (from 2,100) the day the campaign was narrowed from
broad to warm-only. Not because 2,100 was wrong — it implies a reachable pool of
~21,000, which is plausible — but because every efficiency number we had
described the BROAD version. A week at a conservative level buys a clean
frequency reading on the audience it actually has now.

### The formula
```
daily budget = (reachable warm pool x target weekly frequency x CPM) / 7,000
```
At frequency 2.5/week and the observed CPM of 250-280:

| Reachable pool | Daily budget |
|---|---|
| 15,000 | ~1,500 |
| 20,000 | ~2,000 |
| 25,000 | ~2,500 |
| 30,000 | ~3,000 |

### Scaling rule — measure, do not guess
| Weekly frequency | Action |
|---|---|
| under 2.0 | raise 25% — under-serving the pool |
| 2.0 - 3.0 | correct, hold |
| over 3.5 | cut 25% — fatiguing the same people |
| any level, CPM rising while CTR falls | pool is saturated regardless of frequency |

### 🔴 The pool is CONTRACTING, not building
Store sessions, ignoring the March spike: **16,745 (Apr) → 11,882 (Jul), down
29% in four months.** Unique visitors 13,767 → 9,545.

A retargeting audience is only a memory of top-funnel traffic. Retargeting spend
therefore **cannot** be scaled by decision — its ceiling is set by how many new
people enter the funnel. At ~10,000 new visitors/month this campaign tops out
around **PKR 2,500-3,000/day**; past that you are paying to show the same people
the same catalogue again.

**To spend more on retargeting, fix top-funnel volume first.** That is the whole
argument for the TOF restructure in section 3.

---

## 9. TOF campaign BUILT (paused) — Jul 31 2026

`KV | TOF | Smart Wallets | Aug26` — **`120254219929940428`**

| Ad set | ID | Budget |
|---|---|---|
| TOF-A \| Mocha Mate \| LLA 1%+3% Value (All Delivered) | `120254219931990428` | PKR 1,500/day |
| TOF-B \| Razor \| LLA 1%+3% Value (All Delivered) | `120254219933170428` | PKR 1,500/day |

**ABO, not CBO — deliberate.** No campaign-level budget. Campaign budget
optimisation would let Meta move money between Mocha Mate and Razor, which is
the exact failure that gave Bastion 99% of spend inside one ad set. With ABO the
two budgets are ring-fenced and the comparison is real.

### Every setting, and the evidence for it

| Setting | Value | Why |
|---|---|---|
| Objective | OUTCOME_SALES | matches the account's working campaigns |
| Optimization | OFFSITE_CONVERSIONS + `custom_event_type: PURCHASE` | optimise on purchases, not ATC/IC. Lower volume, but ATC optimisation imports refusers |
| Pixel | `1865080707652548` (Kordovan 2025 Dataset) | EMQ 9.3/10 on Purchase, CAPI live |
| Bid strategy | Highest volume (autobid) | a cost cap at ~1,000 would throttle a new ad set to nothing while cold sits at 2,180. Revisit once CPA stabilises |
| Attribution | 7-day click / 1-day view | Meta default, correct for a considered COD purchase |
| Billing | Impressions | standard |
| **Age** | **18–54** | see below — CHANGED from the old 20–55 |
| **Gender** | **unrestricted** | see below |
| Geo | PK, `location_types: home + recent` | explicit, since omitting it triggers Meta error #1870194 |
| Advantage+ Audience | **0 (off)** | at 1 it treats audiences as a hint and expands — that is what turned "Retarget" into a broad campaign |
| Targeting relaxation | lookalike 0, custom_audience 0 | no creep outside the lookalikes |
| Placements | manual (below) | data-driven, see §4 |
| Pacing | standard | even delivery, no front-loading |

### 🔴 Age changed to 18–54, from 20–55
Account data, last 90 days, by age:

| Age | Spend | CPA | ROAS |
|---|---|---|---|
| **18–24** | 42,233 | **586** | **6.60x** |
| 25–34 | 92,562 | 740 | 4.45x |
| 35–44 | 61,601 | 1,027 | 3.86x |
| 45–54 | 30,347 | 1,084 | 5.65x (AOV **6,122** — the high-ticket buyers) |
| 55–64 | 11,757 | 980 | **2.89x** |
| 65+ | 4,241 | 848 | 3.10x |

The old 20–55 setting **excluded 18–19, inside the best-performing bucket**, and
included 55+, the weakest. Now 18–54.

⚠️ **Caveat, stated honestly:** those ROAS figures are Meta's, counted on orders
PLACED, not delivered. Young COD buyers are the classic refuser profile, so
18–24's apparent efficiency may not fully survive refusal. What makes widening
defensible is that the lookalike is now seeded on **delivered** buyers only —
it already encodes "people like those who actually accepted the parcel". Watch
18–24's refusal rate specifically in the first month.

### 🔴 Gender left unrestricted — women are underweighted
| Gender | Spend share | CTR | CPA | ROAS | AOV |
|---|---|---|---|---|---|
| Male | **93.5%** | 3.54% | 818 | 4.55x | 3,722 |
| **Female** | **6.2%** | **5.55%** | **683** | **6.65x** | **4,540** |

Women click more, convert cheaper and spend more per order — on 6% of budget.
Gift buyers. Never restrict this campaign to men.

### Audiences
**Included:** LLA 1% Value `120254216730060428` + LLA 3% Value `120254216735280428`
**Excluded (3):** COD Refusers `120253660257910428` · All Delivered Buyers SEED
`120254215371460428` · Purchasers 180D `120252468019140428`

Excluding both buyer lists means prospecting never pays to reach an existing
customer — those belong to Retarget.

### Placements
Facebook: feed, profile_feed, marketplace, video_feeds, story, search,
instream_video. Instagram: stream, explore, explore_home, reels, profile_feed,
ig_search.
**Excluded: Instagram Stories (66.62/LPV, 0 purchases), Facebook Reels
(93.06/LPV, 0 purchases), Audience Network (45% CTR = bot traffic), Messenger.**

### Still to do before launch
1. User attaches creatives (Mocha Mate cinematic from IG; Razor RFID hook)
2. Lookalikes must finish populating
3. Activate campaign → both ad sets → both ads (all four levels)
4. Pause the old cold ad set `120254085361120428` at cutover — **not before**,
   or there is a gap in prospecting


---

## 10. 🔴 CORRECTION — placement cuts were wrong (Aug 1 2026)

**Two of the three placement cuts in §4 were reversed.** They were made on 3-5
days of data with single-digit conversions. The user challenged them and was
right. Lifetime data (Mar 2025 - Aug 2026):

| Placement | Spend | Purchases | CPA | ROAS | Verdict |
|---|---|---|---|---|---|
| feed | 980,259 | 1,240 | 791 | 4.69x | keep |
| **facebook_reels** | **465,842** | **595** | **783** | **4.69x** | **RESTORED** |
| instagram_reels | 405,425 | 599 | **677** | **4.91x** | keep |
| **instagram_stories** | **80,741** | **109** | **741** | **3.78x** | **RESTORED** |
| facebook_stories | 18,608 | 28 | 665 | 6.23x | keep |
| search | 10,040 | 24 | **418** | **6.24x** | keep |
| threads_feed | 3,361 | 6 | 560 | **6.91x** | keep (API cannot set it) |
| instagram_explore | 4,265 | 5 | 853 | 7.38x | keep |
| facebook_profile_feed | 2,176 | 8 | 272 | 16.4x | keep |
| marketplace | 5,118 | 5 | 1,024 | 2.62x | keep — too few conversions to cut |
| instream_video | 4,054 | 4 | 1,014 | 2.69x | keep — same |
| **an_classic (Audience Network)** | 16,084 | 6 | **2,681** | **1.54x** | **CUT — stands** |
| **rewarded_video** | 9,946 | 1 | **9,946** | **0.21x** | **CUT — stands** |
| messenger_inbox | 36 | 0 | — | — | cut |

### The statistics, because this is the lesson
- **Facebook Reels:** PKR 2,233 at its true 783 CPA expects **2.9 purchases**.
  Observing 0 has probability e^-2.9 = **5.8%**. Unlucky, not evidence.
- **Instagram Stories:** PKR 733 at its true 741 CPA expects **0.99 purchases**.
  Observing 0 has probability e^-0.99 = **37%**. Completely meaningless.

**Rule adopted: never cut a placement, product or audience on fewer than ~25
expected conversions.** Below that, absence of conversions is noise. Check the
lifetime window before acting on a short one — a placement carrying six figures
of historic spend deserves more than a five-day look.

Audience Network survives the test and stays cut: 6 purchases on PKR 16,084 is
~20 expected at blended CPA, and 1.54x ROAS against a 4.69x account blend is a
real, sufficiently-powered gap.

### Standing placement set (corrected)
Facebook: feed, profile_feed, marketplace, video_feeds, **story**,
search, instream_video, **facebook_reels**
Instagram: stream, **story**, explore, explore_home, reels, profile_feed, ig_search
**Excluded: Audience Network, Messenger only.**

Applied to: TOF-A `120254219931990428`, TOF-B `120254219933170428`,
and the live cold ad set `120254085361120428` (force-paused on edit,
reactivated and verified ACTIVE).


---

## 11. 🔴 CORRECTION 2 — age and gender, checked against lifetime (Aug 1 2026)

Same discipline applied to §9's demographic decisions. Lifetime, Mar 2025 - Aug 2026:

### Age
| Age | Spend | Purchases | CPA | ROAS | 90-day said | Verdict |
|---|---|---|---|---|---|---|
| 18-24 | 241,067 | **383** | **629** | **5.38x** | 6.60x | widening to 18 CONFIRMED |
| 25-34 | 811,489 | **1,185** | 685 | 4.95x | 4.45x | keep |
| 35-44 | 576,131 | **677** | 851 | 4.32x | 3.86x | keep |
| 45-54 | 248,827 | **253** | 984 | **4.07x** | 5.65x | keep (weakest, still fine) |
| 55-64 | 92,831 | **100** | 928 | **4.48x** | **2.89x** | **CUT REVERSED** |
| 65+ | 38,883 | **37** | 1,051 | **4.56x** | **3.10x** | **CUT REVERSED** |

**Every age bucket runs between 4.07x and 5.38x.** None justifies exclusion.
The 90-day read had 12 purchases in 55-64 — its CPA actually matched lifetime
almost exactly, but AOV wobbled on 12 orders and dragged ROAS to 2.89x. Noise.

**Age set to 18-65 on both TOF ad sets.** No upper cap. Restricting on no
evidence is the same error as the placement cuts.

⚠️ Caveat carried forward: lifetime age data is dominated by
retargeting/broad campaigns where older warm buyers convert well. There is not
yet enough cold-specific data to know whether older ages behave the same in
prospecting. Re-check once the TOF ad sets have ~25 conversions each.

### Gender — right conclusion, WRONG reason
| Gender | Purchases | CPA | AOV | ROAS |
|---|---|---|---|---|
| Female | 158 | **1,029** | **7,066** | **6.87x** |
| Male | **2,467** | **745** | 3,351 | 4.50x |

The §9 claim that "women convert cheaper" was wrong — lifetime shows women cost
**38% MORE** per order. They are valuable because AOV is **more than double**,
not because acquisition is cheap. Leaving gender unrestricted remains correct;
the reasoning in §9 does not.

### Not changed: the live cold ad set (`120254085361120428`)
Left at 20-55 deliberately. It has already had learning reset twice tonight by
placement edits, and it gets paused at TOF cutover anyway. Another reset for an
ad set about to be retired is churn, not improvement.


---

## 12. Catalogue / DPA campaign BUILT (paused) — Aug 1 2026

`KV | BOF | Catalogue DPA | Aug26` — **`120254220293930428`**
Ad set `DPA | Product Intent (VC+ATC+IC, no purchase) | All Products` —
**`120254220299340428`**, PKR 1,000/day, ABO.

Product set: **All Products `608788148654460` — 165 products**, the whole store.
Catalogue `1015378560682303`. Live pixel matches at **99.94%**, so dynamic ads
are fully supported.

### Why this is NOT the same as the Retarget campaign
| | Retarget (`120228534676850428`) | DPA (this) |
|---|---|---|
| Ad | ONE creative, same for everyone | auto-generated per viewer |
| What they see | the same video | **the exact product they browsed** |
| Coverage | whatever is in the creative | all 165 products |
| New product | needs a new ad built | appears automatically |

### Retarget's lifetime record — respected, not overwritten
PKR 342,319 spent · **583 purchases** · CPA **587** · ROAS **6.70x** (May 2025 –
Aug 2026). Best CPA of any campaign, and 583 conversions is properly powered.
Two caveats: it earned that as a **broad** campaign, and its Meta ROAS is the
one measured as ~2.6x overstated, so real first-click is likely 2.5-3x. Its
warm-only performance is unproven as of Aug 1.

### Can they run together?
**Yes, with managed overlap.** Both touch warm users, so they compete in the
auction. Mitigated by giving each a different job:
- **DPA** → product-intent only: ViewContent 90D + ATC 180D + IC 180D, all
  "no purchase". Excludes Purchasers 180D and COD Refusers.
- **Retarget** → the broad warm + buyer pool with brand creative.

⚠️ Overlap is **not eliminated** — ViewContent/ATC/IC users are also inside
Retarget's "All Website Visitors 180D". To remove it entirely, exclude those
three audiences from Retarget. **Not done — needs the user's approval**, and it
would strip Retarget of its highest-intent segment, so it is a real trade-off
rather than an obvious win.

The larger risk at this account's scale is **conversion fragmentation**: ~3
conversions/day across what is now 5 ad sets. Each one takes longer to leave
learning. Accepted deliberately.

⚠️ `product_audience_specs` (native DPA product-level retargeting) could not be
set — the API rejects both documented shapes of the `rule` field. The custom-
audience equivalent above achieves the same targeting; Meta still selects each
viewer's products from their own pixel history, so the dynamic behaviour is
unaffected.

### Budget after this addition
| Campaign | PKR/day |
|---|---|
| TOF-A Mocha Mate | 1,500 |
| TOF-B Razor | 1,500 |
| Retarget (warm + buyers) | 1,500 |
| **DPA catalogue** | **1,000** |
| Old cold (retire at cutover) | 3,800 |
| **Total once old cold is paused** | **5,500** |
