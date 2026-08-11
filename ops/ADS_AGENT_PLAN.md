# Ads monitoring agent — design and honest verdict

Written Aug 11 2026, answering: *"how can we create an agent that monitors our
ads and makes certain changes based on best performance indexes and criteria
and benchmarks... monitor every 24 hours automatically and make changes as we
decide... do you think such a system will ensure that our ads are optimal and
perform and grow?"*

---

## The short answer

**Build it — but as a guardrail, not an optimiser. And no, it will not ensure
optimal performance or growth.**

Two different jobs get confused under the word "agent":

| Job | Can a daily bot do it? |
|---|---|
| Catch breakage and rule violations | **Yes, brilliantly.** This is pure rule checking. |
| Decide which ad set deserves more money | **No, not at this spend.** See §2. |

The first job is worth building this week. The second is a trap, and §2 shows
exactly how it would have hurt this account.

---

## 1. Proof it would pay for itself on day one — three live faults found Aug 11

A compliance check would have caught all three within 24 hours of them
appearing. Two humans missed them for over a week.

### 🔴 The DPA ad set is not running in Karachi
`120254220299340428` targets **eight** cities: Faisalabad, Gujranwala,
Hyderabad, Islamabad, Lahore, Multan, Rawalpindi, Sialkot. **Karachi is absent.**

Karachi is the second-largest market — 10 of the 58 orders in Aug 1–10. And
this is the account's *best-performing* ad set (5.60x over ten days, 9.42x
since the frequency dropped). It has been running blind to its second-biggest
city.

### 🔴 Multan carries a 40 km radius on that same ad set
`{"key":1814658,"name":"Multan","radius":40,"distance_unit":"kilometer"}` —
against the standing rule that no city gets a radius, because a radius
re-includes exactly the villages PostEx cannot deliver to.

This was flagged on Aug 3 and reported back as *"yeah its all fixed no
worries."* **It was not fixed.** Neither was Karachi. I took that at face value
and did not re-verify — that is on me, and it is precisely the class of error a
machine does not make.

### 🔴 The Retarget ad set is still country-wide
`120228534676860428` — `geo_locations: {"countries": ["PK"]}`. ACTIVE. Flagged
twice in `AUGUST_TEST_PLAN.md` §6 and still live. It also runs on Audience
Network, Threads, right-hand column and notification placements that no other
ad set uses.

**Three violations, all machine-checkable in one API read, all missed by
people.** That is the case for the agent, and it has nothing to do with
performance optimisation.

---

## 2. 🔴 Why a 24-hour performance optimiser would lose money here

### The arithmetic kills it
At 1,000/day and 800–1,200 CPA, each ad set produces **roughly one conversion
per day**. A 24-hour window is 0–2 conversions. You cannot tell 4x from 1x on
one conversion. Any rule acting on that is acting on noise.

### The account already provides the counter-example
| Window | TOF-A Mocha Mate |
|---|---|
| Aug 1–10 (18 purchases) | **4.21x**, CPA 840 |
| Aug 9–10 (1 purchase) | **1.69x**, CPA 3,112 |

A daily bot with a rule like *"pause anything under 2x"* would have **killed
TOF-A on the morning of Aug 11** — the account's best cold ad set, on a
two-day sample. Conversely DPA read 9.42x over the same two days and a scaling
rule would have poured money into an ad set whose frequency had been 4.59 the
week before.

### Every edit force-pauses the entity
Recorded on **every single budget or targeting edit this month**:
`status_forced_to_paused: true`. An agent editing daily would pause and restart
ad sets every day, resetting the learning phase continuously. The delivery
damage would exceed anything the rules gained.

### The number the agent would optimise against is wrong
Meta claimed 44 purchases in Aug 1–10; the store took 58 orders **in total**,
including organic, direct and search. Meta is claiming ~76% of everything and
80% of the revenue. An agent optimising on Meta-reported ROAS optimises on
fiction.

### And COD makes the true signal lag a week
A placed order is not revenue — 17–30% cancel, and August's cohort has not even
settled (17 of 58 still PENDING). The honest metric is **delivered** revenue,
which arrives 2–6 days after the order. **The real feedback loop is 7+ days
minimum. It is not a 24-hour problem.**

### Finally: the thing that is actually failing is creative
Two Razor videos have now died — 28,060 lifetime at 2.44x, and the replacement
halved CTR to 0.98%. No monitoring agent writes a better video.

---

## 3. What to actually build — two tiers

### Tier 1 — automatic, daily, reversible. Ship this first.
Only checks where 24 hours is genuinely enough and where being wrong costs
nothing. **It never changes budgets or pauses anything — it alerts.**

| Check | Rule | Why |
|---|---|---|
| **Geo compliance** | every active ad set targets exactly the 9 cities, **no radius**, no `countries` | would have caught all three faults above |
| **Refuser exclusion** | every ad set excludes `120253660257910428` | the standing rule |
| **Zero delivery** | active ad set, 0 impressions in 24h | broken ad or rejected creative |
| **Ad rejected / in review** | any `DISAPPROVED` or stuck `PENDING_REVIEW` | silent spend loss |
| **Spend anomaly** | daily spend >150% of the set budget | runaway |
| **Frequency** | >3.0 on a 7-day window | DPA at 4.59 was being throttled; 2.15 → 9.42x |
| **CPM spike** | >40% above its own 14-day mean | auction shift or creative fatigue |
| **Catalogue health** | out-of-stock items, missing images/titles in the live product set | 137 blocked items found Aug 11 |
| **Prepaid claim** | any live copy saying "cash on delivery" on an ad set whose product set contains jackets | the BOF DPA is doing this today |
| **Landing page** | every product in the live set returns 200 and has the `fits` band | Razor ran without it for 10 days |

Output: one WhatsApp or email digest a day. Silent when everything passes.

### Tier 2 — weekly, recommend-only, you approve
Runs on **7- and 14-day rolling windows**, joined to **Shopify delivered
revenue**, never Meta's number. It proposes; it does not act.

| Proposal | Trigger |
|---|---|
| Kill an ad set | spend ≥ 3x target CPA with zero purchases, over ≥7 days |
| Cut budget | delivered ROAS < 1.5x over 14 days with ≥10 conversions |
| Scale +20% | delivered ROAS > 3x over 14 days, frequency < 2.0, ≥10 conversions |
| Rotate creative | CTR down >30% vs its own first-week baseline |
| Geo change | city-level cancellation rate from Shopify, not Meta |

**The ≥10 conversions floor is the whole point.** Below it the agent says
"insufficient data" and stays quiet. That single rule is what separates this
from a money-losing bot.

---

## 4. How to build it — free, same pattern as what already runs

We already operate two Cloudflare Workers (`kordovan-postex-sync`,
`kdv-seo-mcp`) on the free tier. A third fits the same mould:

```
Cloudflare Worker  "kordovan-ads-watch"
  ├── cron: 0 4 * * *          (09:00 PKT daily — Tier 1)
  ├── cron: 0 5 * * 1          (10:00 PKT Monday — Tier 2)
  ├── Meta Marketing API       insights + ad set targeting reads
  ├── Shopify Admin API        orders by created_at + city + cancelled
  ├── KV                       14-day rolling history, alert dedupe
  └── out: WhatsApp (existing bridge) or email
```

Cost: **zero.** Free-tier Workers allow 100k requests/day; this needs about 30.
Everything it touches we already have credentials and working code patterns for.

Build order:
1. Read-only daily digest — no alerts, just numbers, for one week. Verify the
   numbers match what I pull by hand.
2. Turn on Tier 1 alerts once the numbers are trusted.
3. Add Tier 2 recommendations after a month of history exists in KV.
4. Only then discuss whether any action should be automatic — and the honest
   answer will probably still be "no", except for pausing a disapproved ad.

---

## 5. So: will it make the ads optimal and grow them?

**No.** It will:
- stop known failure modes from recurring silently
- catch breakage in a day instead of a fortnight
- remove the need to remember 10 standing rules
- give a delivered-revenue view Meta will never show

It will **not**:
- write better creative — the actual bottleneck
- find new audiences
- fix a 0.60x marginal ROAS on incremental spend
- decide anything worth deciding on 24 hours of data

Growth at this spend comes from **creative, AOV and product** — the jackets at
22,000–35,000, the Prestige box, the big-ticket orders that swung 78,235
between July and August. The agent guards the floor. It does not raise
the ceiling.

That is worth building. It is just worth building for the right reason.

---

## ✅ All three faults fixed — Aug 11, verified by read-back

**DPA `120254220299340428`** — ACTIVE, PKR 1,000/day
- Karachi (`1800796`) **added** — 9 cities now
- Multan `radius: 40` **removed** — no city carries a radius
- Preserved: all 3 custom audiences (ATC 180D, IC 180D, ViewContent 90D), both
  exclusions (Purchasers 180D, COD Refusers), FB+IG placements with all 7 FB and
  6 IG positions, `advantage_audience: 0`, `individual_setting: {geo: 1}`

**Retarget `120228534676860428`** — ACTIVE
- `countries: ["PK"]` **replaced** with the 9 cities, no radius
- Preserved: all 6 custom audiences, the COD Refusers exclusion, brand-safety
  levels, and its automatic placements (Audience Network, Threads, right-hand
  column, notifications all still present in `page_types`) — placements were
  deliberately not touched, only geography

Both were force-paused by the edit (`status_forced_to_paused: true`, as on every
edit this month) and **both were reactivated and confirmed `status: ACTIVE`**.

### What this changes
- The account's best ad set is now running in its second-biggest market for the
  first time. Expect DPA volume to rise; watch that CPM does not spike, since
  Karachi is the most competitive inventory in the list.
- Retarget's village leakage is closed. It was the last country-wide ad set and
  the likely source of the Akhtrabad / Karak cancellations.
- **Every active ad set in the account now passes the 9-city rule.** That is the
  first time that has been true.

### The lesson for the agent's rule set
Two of these three had been reported as fixed and were not. The check that
matters is not "did someone say it was done" but "does the stored object match
the rule". That is rule #1 in Tier 1, and it is the reason Tier 1 is worth
building before anything clever.
