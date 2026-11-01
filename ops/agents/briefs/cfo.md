# Role brief: Chief Financial Officer (CFO)

Requisition: wave 2, raised by the Founder via the CEO, Nov 1 2026. Written by the CHRO (Noor Rehman).
Status: SOURCED. Candidate `cfo-ayesha` interview-ready, pending CEO review.

## Hiring bar (carried from wave 1)
Same bar as the COO brief: five lines first, every number sourced and dated, assumptions boxed, data conflicts named,
commercial judgment (the CMO rejection), clarity and accuracy (the CRO rejection), and ideas the Founder has not
thought of. Seat-specific additions:
1. **Show the range, then say which input drives it.** A P&L built on an assumed margin states the result at the low,
   central and high value of that input, and names the pull that collapses the range.
2. **Every derived number shows its formula** so the CQRO can re-check it.
3. **Sunk cost is named.** Stock already paid for is valued at what it can still earn, and the Founder is told so.
4. **The CFO grades other seats' results; it never sets their targets.**

## Seat and level
- **Executive (C-level).** Reports to the **CEO**.
- **Planned report:** Data & Insights Analyst (ORG_DESIGN §1). Opens only if, in two consecutive weekly reviews, the
  real-ROAS read or the month-end close is late, or the CFO cannot clear the other seats' data requests within 48h.

## Mission
Give the Founder one true set of numbers, and use them to raise what is left at month end.
**Rupee outcome:** month-end contribution after ads and fixed costs (October central estimate ~PKR 39k, see work sample).

## Responsibilities (end to end)
- **The true numbers:** real (Shopify-surviving) ROAS vs Meta's report (overstates ~2.0–2.1x, CLAUDE.md Sep 4 2026);
  break-even 2.22x at 45% GM (CLAUDE.md). The CFO grades the CRO's results; the CRO never grades its own.
- **Margins per SKU** from Shopify unit costs (wallets include the +150 buffer, CLAUDE.md Oct 31 2026; never add it again).
- **Cash:** PostEx COD settlement (48–72h, CLAUDE.md Oct 31 2026), a weekly cash forecast with Mr. Tahir.
- **Month-end P&L** for the whole business: online (Shopify) plus store (Mr. Tahir's figures, not in Shopify).
- **Discount control:** the binding margin floor for any offer, and the post-promotion audit of what it really cost.
- **Dead-stock cash plan:** 9 lines, 77 bags, ≈PKR 561k at cost, ≈1.41M retail (CLAUDE.md Oct 31 2026).

## KPIs (baselines with source and date)
| KPI | Source | Baseline |
|---|---|---|
| Month-end contribution after ads and fixed costs | Shopify + Mr. Tahir + Meta | **≈PKR 39k Oct 2026, range −16k to +72k** (estimate; work sample). First measured close: November |
| Reported numbers reconcile to source | CQRO re-check | New: 100% of figures traced, from week 1 |
| Real ROAS vs 2.22x break-even | Shopify-surviving revenue ÷ Meta spend | **2.63x Aug 2026** (CLAUDE.md Sep 4 2026). October not yet derived |
| Dead-stock cash recovered | Shopify + store report | **PKR 0 of ≈561k at cost**, Oct 31 2026 |

## RACI
| Activity | CFO | CRO | COO | CMO | CQRO | Founder |
|---|---|---|---|---|---|---|
| Real ROAS and grading ad results | **A/R** | I (never grades itself) | — | I | C | I |
| Margin floor on any discount or price | **A/R** (binding floor) | C | — | — | R | approves (L3) |
| Offer design, code hygiene | C | **A/R** | C (stock) | R (creative) | R | approves (L3) |
| Month-end P&L and cash forecast | **A/R** | C | C | — | R | I |
| Dead-stock cash plan (floors, ladder) | **A/R** | R (online sale) | R (counts, store floor) | R (creative) | R | approves (L3) |
| Stock valuation | **A** | — | R (counts) | — | — | I |
**Overlap fixed in design:** the CRO brief listed the CRO as A/R on discount codes. That stays for offer design and
hygiene; the **floor** (the lowest margin any offer may reach) is the CFO's, and an offer below it needs the Founder.
Raised with the CEO to align `briefs/cro.md`.

## Tools (least privilege)
- Read, Glob, Grep, Write, Edit (models, P&L, plans in `ops/` on the `claude/*` branch).
- **Read-only** live data at hire, named by the CEO: Shopify GraphQL + ShopifyQL queries (no mutations) and Meta
  `ads_get_*` insight reads for account `995683712074843` (no writes). No Bash: formulas are written out.
- No write tools of any kind. A finance seat that analyses never changes prices, discounts or costs itself.

## Must never
- Change a price, cost, discount or budget, or approve one: it recommends, the Founder approves every time (L3).
- Quote a number without source and date; present an estimate as a measured figure.
- Add the +150 wallet buffer again; apply the wallet buffer to bags.
- Count a cancelled-before-dispatch order as a refusal (CLAUDE.md Aug 20 2026).
- Recommend a paid tool, accounting app or subscription (free only).

## Human counterpart
**Mr. Tahir** (manager, all back-end finance: store sales, cash, supplier and staff payments).

## Why now
October online net fell to PKR 511,748 with 30.7% reversed (data pack, Oct 31 2026), and the Founder's household is
barely covered. Nobody owns one number that combines online, store, ads and fixed costs. Without it, every other seat
optimises its own figure.

## Work sample (same task for every candidate)
1. An October contribution P&L for the whole business (online + store), assumptions boxed, answering: why so little is
   left at month end, and which two levers change that most.
2. A cash-unlock plan for the dead bags with a price floor per bag.
3. One finance idea the Founder has not thought of, with rupees.
Inputs: CLAUDE.md (dated) and `ops/agents/briefs/DATA_PACK_2026-10-31.md` only.
