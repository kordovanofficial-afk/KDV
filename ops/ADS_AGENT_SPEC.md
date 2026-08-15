# Kordovan ads agent — consolidated spec

Synthesised Aug 11 2026 from four independent reviews: a direct-response media
buyer, a systems engineer, a hostile red team, and a quantitative analyst.
Where they disagreed, this document picks a side and says why.

`ADS_AGENT_PLAN.md` holds the original verdict and the Aug 11 fault record.
This is the buildable spec.

---

## 0. The decision, up front

**Build Tier 1. Build Tier 2 in shadow mode only. Never let it act autonomously.**

| | Expected value | Verdict |
|---|---|---|
| Tier 1 — alerting, read-only tokens | **+80k to +120k/yr** | Build this week |
| Tier 2 — recommend-only, human approves | break-even to −50k/yr **unless** all five gates below are in place from day one | Build in shadow mode, act later or never |
| Tier 2 acting autonomously | **−150k to −300k/yr** | Do not build |

The five gates that make Tier 2 non-negative: the evidence gate (§2), delivered
revenue as the only decision metric (§3), the seasonal freeze (§5), the global
sanity layer (§6), and the scorecard (§7). Missing any one of them and Tier 2
is a money-losing random number generator with good prose.

---

## 1. Where the four reviews disagreed, and what I decided

### Conversion floor: 10 or 25?
Media buyer said ≥10 conversions. Red team said ≥25 plus ≥14 days plus a
credible-bound test. **Decided: 25.** At 10 conversions the 95% interval on CPA
is roughly ±46% — wide enough that a "3.0x vs 4.5x" comparison is a coin flip.
The media buyer's *mechanism* is adopted though, and it is the best idea in all
four reviews:

> **The evaluation window is defined by conversion count, not by the calendar.**
> Window = however many trailing days it takes to accumulate 25 conversions,
> floored at 14 days, ceilinged at 28.

At today's ~1 conversion/day/ad set that resolves to the ceiling — 28 days,
i.e. barely ever. In November at 25,000/day it resolves to 2–3 days
automatically. **The same agent runs a testing month and a peak month with no
reconfiguration.** That property is worth more than any individual threshold.

### Should compliance violations be auto-paused?
Media buyer: yes, AUTO-pause on geo violation — pausing is reversible and the
leak is real money. Red team: no, the watcher must hold read-only tokens, full
stop. **Decided: read-only for the first 90 days.**

The media buyer's argument is genuinely strong and I nearly took it. What
settles it is the red team's point that the watcher holding a write token is
what makes every later scope-creep failure possible. A separate, write-capable
Worker for compliance-pause-only can be revisited after 90 clean days — and if
it happens, it is a *different Worker with a different token*, so the thing that
watches is never the thing that writes.

### Silent when passing?
My original plan said "silent when everything passes". **Both the engineer and
the red team said that is wrong, and they are right.** Silence is
indistinguishable from death. `0 checks ran` and `12 checks passed` produce
identical output.

> **Never silent. One line every day, always.**
> `✅ 12/12 green · spend 4,830 · 3 delivered orders · day 34 clean`
> Absence of the message becomes the alarm.

### Is Tier 2 worth building at all?
Media buyer produced a full rule table and wants it. Red team put its EV at
break-even to −50k. **Decided: build it, run it in shadow mode, never wire it
to a write.** Its value is documentation and the scorecard — a written record
of what it *would* have done, scored against what actually happened. If after
three months it does not beat doing nothing, it switches itself off. That
experiment costs nothing and settles the argument with evidence instead of
opinion.

---

## 2. The evidence gate

No Tier-2 output may be emitted unless **all four** hold:

1. ≥ **25** delivered conversions in the window
2. ≥ **14** days elapsed
3. spend ≥ **3x** target CPA
4. the **90% lower credible bound** of delivered ROAS — not the point estimate —
   is on the wrong side of the threshold

Below the gate, the only permitted output is the literal string
**"insufficient data — no recommendation"**.

Every number the agent prints carries its sample size and interval:
`delivered ROAS 2.3x (n=6, 90% CI 0.9–4.8x)`. A figure without an interval is a
bug.

**The one exception — the zero-conversion barrier.** If an ad set has spent
≥3x its target CPA with **zero** conversions, the probability of that under a
healthy rate is e⁻³ ≈ **5%**. That is the only fast kill that is statistically
honest. On TOF-B it would have fired at ~PKR 1,950 of spend — around day 2,
not day 11 after 13,915 had gone.

---

## 3. Metric discipline

**Meta's value metrics are banned as decision variables.** `purchase_roas`,
`action_values` and `purchase` counts may be *displayed*, always labelled
*"Meta claim — do not act on"*. Evidence: Meta claimed 44 purchases Aug 1–10
while the whole store took 58 orders including organic, direct and search — 76%
of everything, 80% of the revenue.

The only decision metric is **Shopify delivered revenue** (order marked paid
after PostEx delivery), joined per ad set.

Two biases stack multiplicatively and both point the same way: Meta
over-attributes ~1.8–2x, *and* a "purchase" is a COD promise that fails 17–30%
of the time. Combined overstatement ≈ **2.2–2.5x**. A naive "scale above 3x"
rule fires at a true ~1.2x.

**Settlement gate.** Any window in which >20% of orders are still PENDING is
marked *not settled* and is structurally incapable of triggering a proposal.
Mechanically enforced by a `settleComplete` flag on each day record, flipped
true at day+10.

### 🔴 Join coverage — a first-class daily check, and a live risk today
The join depends on UTMs. It is already confirmed that `url_tags` **cannot be
written through this connector** for catalogue ads and must be pasted by hand.

**TOF-C is live-paused right now without its URL parameters pasted.** If it
launches that way, the join returns ~zero delivered orders on real spend, and a
naive agent recommends killing the catalogue-prospecting format that this
account's own history says runs at half the CPA of video.

Rule: measure what fraction of Meta-reported clicks match a Shopify order
carrying the expected `utm_content`. Below **60%**, the agent declares its
delivered numbers unusable and degrades to alerting only. **A zero match is an
instrumentation alert, never a performance verdict.**

---

## 4. Tier 1 — the daily checks

Read-only tokens. Alerts, never writes. This is the part that pays for itself.

| Check | Rule |
|---|---|
| **Geo compliance** | exactly the 9 city keys, **no radius**, no `countries` |
| **Refuser exclusion** | every ad set excludes `120253660257910428` |
| **Join coverage** | ≥60% of Meta clicks match a UTM-tagged Shopify order |
| **URL parameters present** | every active ad carries the expected `utm_*` string |
| **Disapproved / stuck review** | any `DISAPPROVED`, or `PENDING_REVIEW` >48h |
| **Zero delivery** | active ad set, 0 impressions in 24h |
| **Spend anomaly** | daily spend >150% of the entity's budget |
| **Frequency** | >3.0 on a 7-day window |
| **CPM spike** | >40% above that ad set's own 14-day mean, **3 consecutive days** |
| **Catalogue health** | blocked items, missing image/price/availability |
| **Prepaid claim** | "cash on delivery" in copy on an ad set whose product set contains jackets |
| **Landing page** | every product in the live set returns 200 |
| **Expected-state drift** | actual status ≠ expected status for any allowlisted entity |

### Alert budgeting — the rule that keeps this usable
Ten checks × 4–6 ad sets × 365 days ≈ 14,600 evaluations a year. Untuned, that
is 3–8 alerts a day, almost all false, and the thread gets muted by week three.

- **Every rule is backtested against 90 days of history before it ships**, and
  tuned until its historical firing rate is under **once a month per entity**.
  A rule that would have fired more often is wrong and does not ship.
- Hard cap **3 alerts/day** plus the digest. The agent ranks and drops, and
  reports what it dropped.
- Statistical rules need **3 consecutive days** out of band, never one.
- Severity routing: P0 (compliance, disapproved, zero-delivery >12h) → immediate.
  P1 → daily digest. P2 → weekly only.

### `NOT CHECKED` is a valid result, `PASS` is not always available
Any check that cannot be performed completely reports **`NOT CHECKED`**, never
`PASS`. A false green is worse than no check — it consumes the attention that
would have found the fault. The digest prints how many checks *ran*, not just
how many passed.

---

## 5. Seasonality and outliers

**Five orders swung 78,235 between two 10-day windows — larger than the entire
revenue gap of 50,811.** November 2025 did 1,727,910 against ~465k in a normal
month. Outliers and seasons dominate this business.

- **Winsorise everything.** Every ROAS/CPA figure is computed twice — once raw,
  once excluding orders ≥ PKR 10,000. **No proposal fires unless both agree on
  the direction.**
- **Never compare to "previous period."** Compare to same-period-last-year, or
  print *"no seasonal baseline — do not infer a trend"*.
- **Hardcoded seasonal freeze: no Tier-2 cut or kill proposals between Oct 1
  and Jan 15.** The eight highest-stakes weeks of the year are a human decision
  made with a human's memory of last year.
- No underperformance verdict on any jacket-carrying ad set before it has 21
  in-season days. Jacket CPMs, CTRs and conversion rates will not resemble
  wallet ones, and jackets are prepaid-only in a COD market — expect worse
  checkout conversion and a much higher tolerable CPA.

---

## 6. The global sanity layer

Runs **before** any per-entity logic. Checks: store-wide conversion rate inside
its normal band, PostEx settling at normal rate and lag, total order count
normal, pixel event rate normal.

**If any global input is anomalous, every per-entity proposal is suppressed and
the agent emits one line: "global anomaly detected — no recommendations."**

This exists because of a specific, plausible scenario: PostEx has a five-day
delivery backlog; the delivered-revenue join — correctly ignoring Meta's
inflated number, exactly as designed — shows every ad set under 1.0x; the agent
writes a calm, well-evidenced recommendation to halve the account, containing
no false numbers and one catastrophic conclusion. Every safeguard would have
worked as designed, all the way into the wall.

Related rule: every finding must list its **top two alternative explanations**,
and if it cannot distinguish them it may not propose an action.

---

## 7. The scorecard — the highest-leverage safeguard, and it is free

Every Tier-2 proposal carries a **falsifiable 14-day prediction**:
*"cutting X to 500/day will raise account delivered ROAS from 1.9x to ≥2.2x."*

Monthly, the agent reports its own hit rate — including for proposals that were
rejected, where the counterfactual is observable.

> **If over three months the hit rate does not beat a do-nothing baseline,
> Tier 2 switches itself off.**

Without this, trust accumulates from fluency rather than accuracy, and six
months in nobody has any evidence either way.

---

## 8. What must never be automated

1. Pausing or killing on performance
2. Any budget increase
3. Any targeting write — full-replace semantics, and the object at risk is the
   COD refuser exclusion, the most valuable configuration in the account
4. Audience create / delete / upload (PII consent, hand-built seed)
5. Anything touching creative
6. Any write to Shopify — enforced by a **read-only token**, not by restraint
7. Reactivating anything the agent did not itself pause in the same run
8. Any message to a customer
9. Discounts, and anything that could put `PAYONLINE10` into ad copy
10. Its own configuration — thresholds, rules, allowlists, autonomy level. All
    in source, all in git. **A system that can widen its own remit does not
    have a remit.**
11. Anything about November
12. Interpreting a global anomaly

**Entity allowlist in source code.** A read list and a strictly smaller write
list. Never resolve an entity by name — the account has 100+ dead campaigns
with country-wide targeting and no exclusions, one bad ID away from live.

---

## 9. Build order

| Phase | Build | Shippable | Effort |
|---|---|---|---|
| **0** | Worker, KV, secrets, `BUILD_ID`, `/health`, `/debug`, daily cron writing metrics. **No checks, no alerts, no writes.** | A week of history you can diff by hand against Ads Manager | 1 session |
| **1** | The Tier-1 checks, alert state machine, dedupe, WhatsApp digest, daily heartbeat | **The whole reason to build this.** All three Aug 11 faults caught within 24h | 2 sessions |
| **2** | Shopify delivered-revenue backfill, settlement flags, rolling baselines, join coverage | A delivered-revenue view Meta will never show | 1 session |
| **3** | Tier 2 in **shadow mode** — proposals computed, logged, scored, never sent for approval | The scorecard experiment running | 2 sessions |
| **4** | Hardening: external dead-man's switch, rate-limit backoff, flaky-error retry, replay | Production-grade | 1 session |

**Phases 0–1 (3 sessions) deliver most of the value.** There is no phase that
enables writes; that is a separate decision, taken later, with the scorecard in
hand.

### Key engineering decisions
- **Meta is the lock, not KV.** Every write is conditional on freshly-read
  remote state. KV is eventually consistent and is never a mutex for money.
- **Desired-state reconciler, not a retry.** Because every edit force-pauses,
  "reactivate after write" as a linear step eventually fails at the worst
  moment. A `restore:<id>` key swept every 15 minutes converts an unbounded
  silent outage into a bounded, visible, self-healing one.
- **`BUILD_ID` bumped on every paste**, echoed by `/health`. That is the
  mechanical defence against Cloudflare's Save-is-not-Deploy trap, which has
  already cost three days once.
- **`/health` is public and carries no business data**, so the external monitor
  needs no credentials.
- Separate Worker from `kordovan-postex-sync`. An ads bug must never be able to
  stop COD orders being marked paid.

---

## 10. 🔴 Two things that matter more than the agent

### The margin number is missing, and it changes every threshold
The media-buyer review computed that at ~73% gross margin, **a Meta-reported
ROAS of 3.5x is break-even** — which would make TOF-A (4.21x) and Retarget
(4.15x) thin rather than good, and DPA (5.60x) the only genuinely profitable
line in the account.

**That 73% is an assumption, not a measured figure.** I have not verified it.
If real margin is materially different, every CPA ceiling moves. Jacket COGS is
missing entirely, and the provisional PKR 4,000 jacket CPA ceiling assumes ~50%
margin — if it is 65%, the true ceiling is ~7,900 and we are badly under-spending
on the highest-leverage line of the year.

**Getting real COGS is the highest-value missing input in the account, and it
is worth more than the agent.** Needed before Oct 1.

### Consolidation buys statistical power for free
The binding constraint on every decision is conversions per window, not rupees.
To act responsibly you need ~25–30 conversions per ad set per 14 days ≈ 2.1–2.5
conversions/day/ad set ≈ **PKR 2,500–3,000/day per ad set**.

**Two ad sets at 2,500/day clear that bar at today's total spend. Four at 1,250
do not.** Fewer, larger ad sets is the cheapest available upgrade to decision
quality — and it also helps the learning phase, which every ad set in this
account currently sits at roughly 14% of.

That is a strategy change, not a software project, and it is available now.

---

## 11. The honest closing line

At ~5,000/day the highest-EV automation in this business is not ad optimisation.
Site conversion rate ran 1.02% in August against 1.42% in July; lifting it back
would halve cold CPA — an effect no budget rule can produce. Two Razor videos
have now died, and creative is a 2x CPA lever in this account's own history that
sits entirely outside the agent's field of view.

**The agent guards the floor. It does not raise the ceiling, and it will quietly
convince you that it does.** Build it for the floor and it is clearly worth
having.
