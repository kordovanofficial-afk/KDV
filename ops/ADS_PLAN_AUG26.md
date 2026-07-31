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
