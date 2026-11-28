# Scaling playbook — lowest spend, scale on proof (Founder Nov 28; Alex lens)
Principle: money only moves toward ads that PROVE themselves on Shopify-confirmed orders that survive COD. No indicator, no scaling. Budget moves first FROM losers TO winners (total unchanged); the TOTAL rises only after a green week.

## The 5 indicators (every read, per AD by utm_content)
1. Shopify orders by utm_content (Meta over-reports ~2.05x; never use Meta's purchases to scale).
2. CPA = spend / Shopify orders vs the product CEILING (DEC_2026_STRUCTURE_ALEX.md sec.6; Mocha 1,460, belt 1,700, hats ~1,800 provisional, gloves 1,000, catalogue mix ~1,500).
3. COD refusal / cancel rate of that ad's orders vs account average.
4. Spend vs ceiling (confidence): <1x = no verdict; 1x-1.5x = watch; >=1.5x = verdict.
5. Frequency + CTR trend (fatigue) and sellable stock.

## Decision table (checked every 3 days; judged on rolling 7 days unless noted)
| State | Rule | Action |
|---|---|---|
| Kill | spend >=1.5x ceiling and 0 Shopify orders; OR CPA >1.3x ceiling after >=2 orders and >=2x ceiling spend; OR refusal >1.5x account avg on >=4 orders; OR sellable stock <=3 | PAUSE the AD (never the ad set before listing every ad in it) |
| Fatigue | frequency >3 cold / >6 warm AND CTR down >=30% vs week 1 | new creative, same hook; keep ad running until replacement has data |
| Hold | spend <1x ceiling with no order; or CPA within 1.0-1.3x ceiling | change nothing; max 1 change per ad set per 72h |
| Descale | CPA 1.0-1.3x ceiling for 3 straight reads | budget -20% |
| VERTICAL scale | CPA <=0.8x ceiling, >=3 Shopify orders, refusal <= account avg, stock ok, ad set has had no edit for 72h | budget +20% (never more; never duplicate) |
| HORIZONTAL scale | vertical stalls (CPA >ceiling after two +20% steps) or frequency climbing | in order: (a) new creative variant of the winner into the SAME ad set; (b) same ad to a new audience (LLA 3%); (c) same angle on the next product (attitude angle test); (d) new placement set only after 4-core data |
| Graduate | test ad: >=2 Shopify orders at <=ceiling and refusal <= avg | joins Prospecting; test slot takes next challenger |
| Funding | any winner needs money | take it from killed/descaled ads first |

## Total budget ladder
- Dec stays 5,000/day. Total rises only if the week's blended Shopify CPA <=1,400 AND refusal <= avg AND no stock red: +10% of total per week, max +500/day per step. Two red weeks in a row: -10%.
- Learning protection: Meta's 50/week math says we are over-split (0.5 ad sets supportable at 5,000/day), so: no new ad set unless it replaces one; test = one ad per cell, 2 cells max, one product.
- Scale per product as ceilings allow: Mocha first (proven), hats (stock-gated), belt/gloves only after Prospecting data.

## Guards
Never touch H1 Mocha, Retarget v2, RT-W unless a Kill or stock rule fires. No pauses by ad-SET average (Nov 8 lesson). Every action logged in ALEX_BRIEFING.md + `ops/marketing/ads/SCALING_LOG.md` with before/after values and read-back. No fake urgency copy. Read Meta budgets back after every change; total must equal the cap.
