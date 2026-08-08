# Jackets SEO — rewritten Aug 9 2026, ahead of winter

Jackets are the second-largest organic pool on the site and the season is
about to start. All 30 products and 3 collection pages rewritten.

## Why this was worth doing — the seasonal data

Search Console, **Nov 2025 – Feb 2026** (last winter), queries containing
"jacket": roughly **130,000 impressions and 5,800 clicks in four months**,
against ~9,400 impressions/month in August. The season is ~3.5x the traffic.

The problem was never rankings. It was that good rankings were not earning
clicks:

| Query | Impressions | Position | CTR | Expected CTR at that position |
|---|---|---|---|---|
| `black leather jacket price in pakistan` | 1,087 | **1.33** | **4.3%** | 25–30% |
| `black leather jacket` | 4,555 | **4.51** | **0.83%** | ~7% |
| `leather jacket price in pakistan` | 11,344 | **3.26** | **3.09%** | 10–12% |
| `jacket brands in pakistan` | 2,120 | 6.42 | 1.46% | ~5% |
| `leather jacket men` | 20,447 | 6.36 | 3.10% | 5–6% |
| `leather jackets` | 14,421 | 9.03 | 1.36% | ~2.5% |

Position 1.33 earning 4.3% is the clearest signal available that the listing
itself was the problem.

**Note this corrects the Aug 1 reading in `SEO_STATUS_AUG26.md` §2.** In August
jackets sit at position 11.9 where 2.2% CTR is par, so it looked fine. In
season they rank on page one, and there the titles fail badly.

## What was actually wrong

| Defect | Count |
|---|---|
| SEO titles over 60 chars — truncated in the SERP, brand cut off | **25 / 30** |
| SEO titles containing "Pakistan" | **2 / 30** |
| SEO descriptions mentioning price | **5 / 30** |
| **SEO title belonging to a completely different product** | **2** |
| Duplicate products (same title, two IDs) | 2 pairs |

The two wrong titles: a **Rebel** cafe racer jacket carried the SEO title
*"Hawkeye Brown Double Breasted Vintage Coat"* (with "Hakeye" misspelled in the
description), and an **Alison** women's biker jacket carried *"Bliss Women's
Leather Bomber Jacket"*. Both were serving the wrong product to Google.

## The new pattern

**Title** — `{Name} — {Colour} {Style} Leather Jacket | Kordovan`, hard-capped
at 60 characters so the brand survives truncation. Filler words are dropped
before the brand is.

**Description** — `{Name}: {style} for men, handcrafted in Pakistan from
genuine leather. Rs {price} — made to order, prepaid. Free delivery nationwide.`
Under 155 characters, and **the price is in every one** — because
`leather jacket price in pakistan` is 11,344 impressions sitting at position 3.

### 🔴 No "cash on delivery" anywhere in jacket copy
All 30 jacket descriptions carry **"PREPAID & MADE TO ORDER"**. Jackets are not
COD. Writing the usual COD line into these would have been a false promise on
30 pages. The copy says "made to order, prepaid" instead.

Free delivery *is* true — every jacket is Rs 22,000+, well over the Rs 5,500
threshold.

## Collections

| Handle | New title |
|---|---|
| `mens-leather-jackets` (28) | Men's Leather Jackets Pakistan — From Rs 22,000 \| Kordovan |
| `kdv-jackets` (30) | All Leather Jackets — Biker, Bomber & Racer \| Kordovan |
| `womens-leather-jackets` (2) | Women's Leather Jackets in Pakistan \| Kordovan |

`mens-leather-jackets` had an **empty body description** — same fault as
`kdv-wallets`. Filled with editorial copy that links out to the women's
collection and to the top-10-brands blog post (which ranks at position 1.58
with 15.7% CTR and is the single best-performing jacket asset on the site).

`kdv-jackets` was deliberately retitled *away* from "Leather Jackets in
Pakistan" so it stops competing with `mens-leather-jackets` for the head term.

## 🔴 Open — blocks the season, needs the user

1. **14 of 30 jackets show 0 inventory** and are ACTIVE. Out-of-stock products
   are dropped from merchant listings and dynamic ads. If they are made to
   order they should not be showing zero — either set stock or turn inventory
   tracking off for them. **This is the biggest single blocker to selling
   jackets this winter.**
2. **Two duplicate product pairs** — Rebel (Rs 33,600 and Rs 32,000) and Alison
   (Rs 26,000 and Rs 23,000). Two URLs competing for one product. Merge or
   redirect one of each.
3. **Product type is inconsistent** — some "Motorcycle Jackets", some "Leather
   Jacket". Affects catalogue grouping and filters.
4. Images — user is handling separately.

## What to expect

Titles and descriptions are re-crawled faster than rankings move — **days to
about two weeks**, not the 3–6 weeks a position change takes. CTR improvements
land on impressions you already have, so this should show before the season
peaks.

If CTR on the top jacket queries goes from ~3% to ~7% at unchanged positions,
that is roughly **+5,000 clicks across the Nov–Feb season**.
