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

---

# Follow-up, Aug 9 — corrections and self-assessment

## 🔴 CORRECTION — the "14 jackets out of stock" warning was wrong

The section above claimed 14 of 30 jackets were out of stock and therefore
invisible to merchant listings and dynamic ads. **That was incorrect.**

`totalInventory: 0` was read as "sold out". On a product with
`tracksInventory: false` it means "there is nothing to count" — Shopify treats
untracked variants as **always available**. The authoritative field is
`variants.availableForSale`, and checking it showed **29 of 30 were already
`true`**. Only one — the duplicate Alison, which was genuinely tracked at zero
— was unavailable.

**This is the second time in this session the same mistake was made:** earlier,
`productByHandle` returning null was read as "the URL 404s", when it only meant
the product was deleted and a redirect was serving the URL fine.

**Rule: never infer a state from a proxy value. Query the field that actually
governs the behaviour** — `availableForSale` for purchasability,
URL Inspection for indexing, not `totalInventory` or a null lookup.

## What was applied

| Change | Count |
|---|---|
| SEO title + meta description rewritten | 30 products, 3 collections |
| `inventoryItem.tracked` → false (made to order, sellable year-round) | 17 products / 97 variants |
| `productType` "Motorcycle Jackets" → "Leather Jacket" | 8 products |
| Empty collection body description filled + internal links | 1 |

Verified after: all 30 are `productType: Leather Jacket`,
`tracksInventory: false`, `availableForSale: true`.

**Not done, deliberately:** style/colour filter tags. They do nothing until
storefront filters are switched on in admin → Search & Discovery. Do both
together or neither.

## Self-assessment against standard e-commerce SEO practice

**Overall: 7/10 — "metadata layer complete, content layer untouched."**

| Area | Score | Reasoning |
|---|---|---|
| Query research | **9** | Used real Nov–Feb seasonal GSC data, not August and not guesses. Correctly identified that the failure was CTR-at-good-position, not ranking, and that price intent was the untapped angle. |
| Factual accuracy | **9** | Caught PREPAID & MADE TO ORDER before writing COD onto 30 pages; verified free delivery was genuinely true at these price points; checked the returns policy before writing return schema. |
| Title tags | **8** | All ≤60 chars (was 25/30 over), brand survives truncation, filler dropped before brand. Formulaic though — 30 near-identical structures. |
| Collection pages | **8** | Head term + price in title, empty body filled, internal links added, cannibalisation with `kdv-jackets` removed. Body copy is thin at 3 paragraphs; competitors run 300–600 words. |
| Meta descriptions | **7** | All ≤155 with price in every one. But template-generated and they read that way — no variation in hook between a Rs 22,000 and a Rs 35,000 jacket. |
| Structured data | **7** | Product JSON-LD carries shipping + returns as of today. No BreadcrumbList, no FAQPage on the collection. |
| **On-page content** | **3** | **Product body descriptions were not touched at all.** They still open with "PREPAID & MADE TO ORDER\nDescription:" — app boilerplate. This is the text Google actually reads for relevance and it matters more than the meta description. |
| **Image alt text** | **2** | Not addressed. The July audit found 47.9% of images site-wide missing alt text. Leather jackets attract meaningful image-search traffic. |
| Technical checks | **5** | Never verified what the PDP and collection render as H1, never checked whether jackets has the same internal-orphan problem that wallets had, handles left as-is (long and messy, but changing them risks redirects). |
| Competitive analysis | **0** | None. No look at who outranks Kordovan for `leather jacket pakistan` or why. |
| Measurement | **6** | Baseline is recorded above, but no explicit re-check date was set. |

### The biggest miss
**The blog post was ignored.** `top-10-leather-jacket-brands-in-pakistan` sits
at **position 1.58 with 15.7% CTR and 852 clicks** — the single best-performing
jacket asset on the site, and one of the few pages that already wins the
"best/top brand" query family, which converts at 14–24% CTR. Refreshing and
extending it for the new season is probably worth more than several of the
product metas rewritten today, and it was not touched.

### Honest summary
The highest-leverage, evidence-based half of the job is done well and is
factually sound. The half that requires writing real content — product body
copy, alt text, expanding the blog — is untouched, and that is the half that
moves rankings rather than click-through.

Expect this work to lift **CTR on existing impressions within days to two
weeks**. It will not move position. Position needs the content layer.

## Next, in priority order
1. Refresh and extend the top-10-brands blog post for the new season
2. Rewrite product body descriptions (strip the boilerplate opener)
3. Alt text across jacket images
4. Resolve the two duplicate product pairs — **needs a decision on which price
   is correct**: Rebel at 33,600 vs 32,000, Alison at 26,000 vs 23,000
5. Enable Search & Discovery filters, then add style/colour tags
6. Re-check GSC around Sept 10 against the baseline above
