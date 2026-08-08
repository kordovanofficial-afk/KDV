# August 2026 — testing month. Everything gets marked.

**Decision (user, Aug 9):** 1M is not reachable in August at a profit — see
`ADS_PLAN_AUG26.md` and the modelling below. So August stops being a revenue
push and becomes a **structured learning month**, so that September and
especially **November** (1,727,910 last year, wedding season) can be scaled
with evidence instead of guesses.

Budgets set Aug 9. **Do not change them mid-test** — a budget change resets
learning and invalidates the comparison.

---

## 1. Locked baseline — measure everything against this

Aug 1–8, before any of the changes below.

| Ad set | Spend | Purch | CPA | Meta ROAS | CPM | Freq |
|---|---|---|---|---|---|---|
| **TOF-A Mocha Mate** | 11,996 | **17** | **518**¹ | 4.86x | 350–627 | 1.37 |
| TOF-B Razor (old video) | 11,994 | 3 | 3,998 | 0.68x | 568–892 | 1.31 |
| DPA Catalogue | 7,970 | 6 | 1,328 | 4.58x | ~320 | **3.90** |
| Retarget | 11,975 | 11 | 1,089 | 3.86x | ~298 | **3.07** |

¹ TOF-A post-city-change (Aug 4–8). Its Aug 1–3 country-wide CPA was 1,315.

**Store-side, Aug 1–9:** 48 orders · 7 cancelled (14.6%) · PKR 138,122 net
placed · ~5.3 orders/day · AOV ~3,900 placed / ~2,900 realised.

### 🔴 Real ROAS is about half what Meta reports
Meta claimed 37 purchases in 8 days; the store took ~43 orders *in total*,
including SEO and direct. Meta is claiming ~86% of everything. Backing that
out puts true ad ROAS at **1.7–2.0x**, not 4.86x. **Every scaling decision uses
1.8x, not the dashboard number.**

## 2. Already proven — do not re-test these

| Finding | Evidence |
|---|---|
| **City targeting works** | TOF-A CPA 1,315 → 518 across the Aug 3 cut. CPM also fell ~490 → ~390–430. Post-change region spend is Punjab/Sindh/ICT only — zero leakage. |
| **The old Razor video does not work** | 11,994 spent, 3 purchases, 0.68x. Killed Aug 9. |
| **Mocha Mate is the winning product** | Also the account's best-ever ad set: CPA 393 at 25 conversions (2025). |
| **Refuser exclusion + WhatsApp are working** | Cancellations 32–36% → 14.6%. |
| Placements | FB Reels 4.69x / 595 purchases lifetime; IG Stories retained. Settled Aug 1 — do not re-cut on small samples. |
| Age / gender | 18–65 all genders. 55–64 = 4.48x lifetime; women cost 38% more but AOV is 7,066 vs 3,351. Settled Aug 1. |

## 3. Budgets as of Aug 9

| Ad set | Daily | Role |
|---|---|---|
| TOF-A Mocha Mate | **1,500** | **control** — the benchmark. Do not touch all month. |
| TOF-B Razor (new video) | 1,000 | creative re-test, capped |
| DPA Catalogue | 1,000 | saturating (freq 3.9) — hold |
| Retarget | 1,000 | saturating (freq 3.1) — hold. ⚠️ campaign-level budget (CBO) |
| **TOF-C test slot** | **1,000** | rotates one variable every 5 days |

Total 5,500/day — same as before, but 1,000 now buys answers.

⚠️ **Every budget or targeting edit force-pauses the entity**
(`status_forced_to_paused`). It has happened on every single edit this month.
Always re-activate and then re-read the status. Never assume.

## 4. The test slot — one variable at a time, 5 days each

Everything else stays identical to TOF-A: same 9 cities, same exclusions,
same placements, 18–65, `advantage_audience: 0`.

| # | Test | Question it answers | Days |
|---|---|---|---|
| 1 | **Broad (no audience) vs TOF-A's LLA** | Is the lookalike earning its keep, or would Meta's algorithm do better unaided? Decides the whole September audience strategy. | Aug 10–14 |
| 2 | **Second product** (Bastion or Kodo 2.0) on the winning audience | Is Mocha Mate special, or is the audience the thing? Decides what to scale in November. | Aug 15–19 |
| 3 | **Karachi-only vs Punjab-only** split | Which geography actually converts — Meta can't break conversions down by region, so it has to be tested as separate ad sets. | Aug 20–24 |
| 4 | **Static image vs video** | Cheapest creative format to produce at volume for the Prestige launch. | Aug 25–29 |

**Stop rule for each:** if an arm is over 2,500 CPA after 5 days *and* has
spent 4,000+, it loses. If both arms are under 1,000, keep the cheaper and note
the second as a viable backup.

**Power warning, stated honestly:** at 1,000/day and ~500–800 CPA that is 6–10
conversions per test. That is enough to spot a large difference (2x) and **not**
enough to resolve a small one (20%). Treat a close result as "no difference
found", never as a winner.

## 5. Measuring cities — use Shopify, not Meta

Meta returns `Not available` for conversions broken down by region, so
city-level CPA cannot be read from the ad platform at all.

**Shopify carries the shipping city on every order — that is ground truth.**
Pull orders by city weekly and track *delivered*, not placed.

### Aug 1–9 by city (orders placed, cancellations excluded)
| City | Orders | In target list? |
|---|---|---|
| Lahore | 12 | ✅ |
| Karachi | 10 | ✅ |
| Rawalpindi | 4 | ✅ |
| Islamabad | 3 | ✅ |
| Multan | 2 | ✅ |
| Hyderabad | 1 | ✅ |
| **Peshawar, Sargodha, Okara, Rahim Yar Khan, Kasur, Bannu, Mangla, Mian Channu, Jamshoro** | **9 combined** | ❌ **not targeted — and none cancelled** |

⚠️ **Those 9 non-targeted cities all delivered without cancelling.** They came
from organic/SEO/direct or from Retarget (still country-wide). That is real
evidence the 9-city list may be **too tight** — Peshawar, Sargodha, Okara and
Rahim Yar Khan look deliverable.

**Do not widen the list on this yet** — most are still PENDING, so RTO is
unknown. Re-check at month end once they have either delivered or failed. If
they delivered, add them for November.

## 6. Open items carried into the tests

- **DPA is missing Karachi** and Multan carries a 40 km radius (flagged Aug 3,
  unconfirmed as fixed). Karachi is the second-biggest market — this is
  suppressing DPA performance and distorting any DPA reading.
- **Retarget is still `countries: ["PK"]`** — the likely source of the
  Akhtrabad and Karak village cancellations.
- `location_types` is still `home, recent` on all ad sets. The `recent` half
  serves people passing through.

## 7. What the answer has to be by Sept 1

Fill this in as the tests land. **This table is the September/November plan.**

| Question | Answer | Evidence |
|---|---|---|
| Broad or lookalike? | | test 1 |
| Which product leads? | | test 2 |
| Which cities scale? | | test 3 + Shopify delivery data |
| Video or static? | | test 4 |
| What CPA holds at 2x budget? | | needs a deliberate scale test late Aug |
| True ad ROAS (not Meta's) | | store revenue ÷ ad spend, monthly |

⚠️ **The one thing these tests will NOT answer: what happens at scale.**
Every test above runs at 1,000/day. Marginal CPA at 5,000/day is a different
number and the only way to learn it is to spend it. **Budget one deliberate
scale test on the winner in the last week of August** — take TOF-A to 3,000 for
5 days and record what CPA does. Without that, November scaling is still a
guess, just a better-informed one.
