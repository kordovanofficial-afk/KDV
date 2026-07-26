# Meta Ads — Wallet Launch (Jul 2026)

Account: **Kordovan 2025 · 995683712074843** (PKR) — the ONLY account in scope.
Pixel/dataset: `1865080707652548`. Budget: **PKR 5,000/day** (~150k/month).

## Structure (both created PAUSED — user adds video creative, then publishes)

| | Campaign ID | Ad Set ID | Budget/day |
|---|---|---|---|
| **Cold — Wallet Launch** | `120254085340610428` | `120254085361120428` | PKR 3,800 |
| **Retarget — Warm** | `120254085373920428` | `120254085374720428` | PKR 1,200 |

Both: OUTCOME_SALES · OFFSITE_CONVERSIONS (Purchase) · WEBSITE · ABO · autobid ·
attribution 7-day click + 1-day view · PK · age 20–55 · Advantage+ audience OFF.

**Cold targeting:** LLA 1% Value `120253661268330428` + LLA 3% Value `120253661269660428`
**Warm targeting:** ATC 180D `120252468021190428`, IC 180D `120252468024210428`,
ViewContent 90D `120252468026250428`, All Visitors 180D `120252468018150428`
**Excluded on BOTH (mandatory rule):** COD Refusers `120253660257910428` +
Purchasers 180D `120252468019140428`

## URL tracking — paste into EVERY ad's "URL parameters" field
```
utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{placement}}&utm_adset={{adset.name}}
```
`{{placement}}` resolves to e.g. `Instagram_Stories`, `Facebook_Mobile_Feed`,
`Instagram_Reels`; `{{site_source_name}}` → `fb` / `ig` / `an` / `msg`.
Read in Shopify Analytics → Sessions by UTM, or GA4 → Traffic acquisition.

## Products in scope (stock-led decision)
Bastion (127 units) + Razor (81, has 18% compare-at = sale angle). Luke (39)
optional 3rd for creative rotation. **Kodo Vertical 2.0 EXCLUDED — 14 units, Black 0.**

## Rules
- Days 0–3: no edits (every change resets learning).
- Day 4: kill ads with 0 ATC after PKR 1,500 spend.
- Day 7: winner gets own ad set; add 2 creative variants.
- Day 10: judge on **delivered vs cancelled in Shopify**, not Meta (Meta counts
  orders placed; ~40% COD refusal inflates it).
- Thresholds: CPA < PKR 800 viable · < 500 scale · ROAS >= 3x placed.
- Never put PAYONLINE10 in ad copy (leaks the prepaid discount — it is delivered
  via WhatsApp order confirmation only).
- Do NOT use the old polluted LLAs (Lifetime Buyers Jun26, Kordovan 2025 Dataset,
  Lifetime Kodo Customers) — seeded on pixel purchasers incl. ~40% refusers.

## Forecast (base case, from Jul 1–23 actuals: CPA 428 blended, AOV 4,525)
Cold CPA will run higher than blended; AOV drops to ~3,000 on 2,450–2,500 wallets.
Expect ~8 placed orders/day → ~5 delivered → ~PKR 450k delivered revenue/month
on 150k spend (~3x on money banked). Margin on the two SKUs decides profitability.
