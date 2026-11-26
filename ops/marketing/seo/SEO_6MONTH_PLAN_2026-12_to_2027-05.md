# KORDOVAN SEO + Organic Growth Plan: 1 Dec 2026 to 31 May 2027 (182 days, one task a day)

**Status:** L1 DRAFT for the Founder. Nothing in this plan has been changed live. **Written:** 26 Nov 2026 (Claude as CEO, through the Alex lens `.claude/agents/alex.md`).
**Source data:** GSC via the `kdv-seo-mcp` connector (`siteUrl https://kordovanleather.com/`, pulled 26 Nov 2026, data to 24 Nov) and Shopify analytics (ShopifyQL, last 90 days to 26 Nov 2026). The figures are read-only pulls; the numbers we could not get are marked "baseline Dec 3".
**Rules this plan obeys:** free tools only · no Karachi, coins, policy words (the exotic-skin and tobacco families) in any new copy · jackets are top-grain sheepskin, never full-grain · supplier-made ("handcrafted in Pakistan", never "our workshop") · genuine reviews with provenance only · "Blessed Friday", never "Black Friday" · no fake urgency or "only X left" · every live change has a before-value, a read-back and the right approval (L2 customer-facing = Founder yes; L3 theme push / money = Founder yes every time) · `seo:` is a full replace · a fact change sweeps every surface (descriptionHtml, seo.description, metafields, collection `custom.editorial`).

---

## [Alex lens] The verdict up top

1. **The real problem is conversion, not traffic.** Google already sends 25,009 sessions in 90 days. They convert at **0.57%**. The jackets collection got **3,420 organic sessions and 0 completed checkouts**; the top-10 jacket blog got 3,115 sessions and 4. More traffic into a leaky bucket is just more leaking.
2. **The math:** organic = 140 orders / PKR 582k net in 90 days (AOV ~4,950). Take CVR from 0.57% to 1.0% on the same traffic and that's roughly **+105 orders and ~+PKR 520k over the next 6 months for zero ad spend**. No new article comes close.
3. **Second lever: CTR on pages that already rank.** "wallet for men" shows us 16,799 times at position 7.4 and gets 0.4% CTR. The Spy and Alison jacket pages have ~21,700 impressions each at ~0.4%. We are on page one and nobody clicks. Fix the snippet before we write anything new.
4. **What I would NOT do:** buy links or "guest posts" (paid and risky), use paid SEO tools, mass-produce AI blog posts, chase the head term "leather" (2,569 impressions at 0.9% CTR, wrong intent), add Pinterest/YouTube/TikTok SEO before the money pages convert, rename URLs again after the Dec 2 cleanup, or judge anything on impressions. Blog posts convert at ~0.1%: they are for authority and links into collections, not the main sales engine.
5. **One thing this week (Dec 1-7):** jacket collection teardown plus snippet fixes for "wallet for men" and the two jacket PDPs. More, then better, then new: in that order.

---

## 1. Baseline (month 0)

### Google Search Console (web search)
| Window | Clicks | Impressions | CTR | Avg position (impression-weighted) |
|---|---|---|---|---|
| 90 days (26 Aug-24 Nov 2026) | **21,650** | **441,660** | **4.90%** | **7.5** |
| 28 days (28 Oct-24 Nov 2026) | **8,495** | **192,209** | **4.42%** | **6.9** |
| Device split, 90d | Mobile 16,758 clicks (CTR 5.1%, pos 6.7) · Desktop 4,763 (4.2%, pos 9.7) · Tablet 129 | | | |

- **Trend:** daily clicks went from ~110 (late Aug) to ~300-365 (November). Impressions ~2,000/day to ~7,400/day. CTR slid from ~5.5% to ~3.9% in mid-November: most of the new impressions are broad jacket terms that land on PDPs.
- **Brand:** queries containing "kordovan" (top 300) = 2,444 clicks / 3,326 impressions in 90 days (~11% of clicks). Brand demand is small, so non-brand SEO is the growth engine.

### Top 10 pages (90 days)
| Page | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| / (home) | 4,072 | 39,985 | 10.2% | 6.8 |
| /blogs/jackets/top-10-leather-jacket-brands-in-pakistan | 3,156 | 61,956 | 5.1% | 8.6 |
| /collections/mens-leather-jackets | 3,010 | 117,711 | 2.6% | 6.5 |
| /collections/mens-leather-wallets | 2,647 | 68,737 | 3.9% | 8.1 |
| /collections/cowboy-hats | 977 | 7,526 | 13.0% | 4.1 |
| /collections/leather-bags | 649 | 11,484 | 5.7% | 6.6 |
| /blogs/wallets/top-10-leather-wallet-brands-in-pakistan | 596 | 9,148 | 6.5% | 5.8 |
| /collections/smart-wallets | 547 | 8,460 | 6.5% | 8.3 |
| /collections/leather-gloves | 479 | 4,211 | 11.4% | 8.4 |
| /collections/leather-caps | 430 | 4,097 | 10.5% | 5.3 |
| *Leaks:* /products/alison-…biker-jacket 88 clicks / 21,763 impr (0.40%) · /products/mens-spy-… 88 / 21,673 (0.41%) · /products/iconic-… 92 / 13,357 (0.69%) · /collections/laptop-bags pos 14.5 · /collections/mens-leather-shoes pos 25 | | | | |

### Top 10 queries (90 days)
| Query | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| kordovan leather | 1,304 | 1,645 | 79.3% | 1.1 |
| kordovan | 771 | 1,196 | 64.5% | 1.8 |
| leather jacket pakistan | 348 | 7,083 | 4.9% | 7.2 |
| top 10 leather jacket brands in pakistan | 309 | 1,806 | 17.1% | 2.3 |
| leather jackets in pakistan | 288 | 5,720 | 5.0% | 7.6 |
| leather jacket men | 251 | 11,589 | 2.2% | 6.8 |
| kordovan wallet | 227 | 278 | 81.7% | 1.0 |
| leather wallet for men | 200 | 4,303 | 4.6% | 5.9 |
| cowboy hat | 167 | 1,789 | 9.3% | 3.8 |
| leather jackets pakistan | 155 | 2,597 | 6.0% | 8.3 |

### Quick-win band (position 4-20, high impressions, low CTR): the first targets
| Query | Impr | CTR | Pos | Page fix |
|---|---|---|---|---|
| wallet for men | 16,799 | 0.4% | 7.4 | wallets collection title/meta + image |
| leather jacket men | 11,589 | 2.2% | 6.8 | jackets collection snippet + PDP → collection link |
| jackets for men in pakistan | 5,234 | 0.5% | 6.9 | lands on Spy PDP; push to collection |
| leather bags | 3,990 | 1.2% | 6.0 | leather-bags collection snippet |
| leather jacket price in pakistan | 3,951 | 2.7% | 6.8 | Nov 13 price test, read Dec 11 |
| smart wallet for men | 2,698 | 1.9% | 10.0 | smart-wallets editorial |
| wallets for men | 2,549 | 0.5% | 10.2 | wallets collection |
| men jackets pakistan / mens jackets pakistan | 2,723 | 0.8% | ~9.9 | collection |
| winter jackets brands in pakistan (+ "with price") | 3,060 | 2.4% | 4-6 | winter-jackets blog refresh |
| oxford shoes price in pakistan | 1,125 | 0.7% | 4.1 | Oxford snippet |
| briefcase | 1,108 | 1.3% | 9.1 | office-bags collection |

### Shopify (last 90 days to 26 Nov 2026)
| Channel (referrer source) | Sessions | CVR | Orders | Net sales | AOV |
|---|---|---|---|---|---|
| **Search (organic; Google 24,576 sessions, Bing 327)** | **25,009** | **0.57%** | **140** | **PKR 582,057** | 4,947 |
| Social (mostly Meta ads) | 44,648 | 0.47% | 195 | PKR 469,074 | 4,286 |
| Direct | 16,935 | 0.90% | – | – | – |
| Unattributed (incl. POS/store) | – | – | 206 | PKR 1,291,499 | 6,470 |

Organic landing pages (sessions · CVR · completed checkouts): Home 4,096 · 1.05% · 43 | **Jackets collection 3,420 · 0.00% · 0** | Top-10 jackets blog 3,115 · 0.13% · 4 | **Wallets collection 2,816 · 1.46% · 41** | Cowboy hats 984 · 0.61% · 6 | Leather bags 631 · 0% · 0 | Wallet blog 608 · 0.49% · 3 | Smart wallets 577 · 0.69% · 4 | Maverick jacket PDP 519 · 0% · 0 | Gloves 479 · 0.84% · 4 | Laptop bags 423 · 0% | Caps 413 · 1.94% · 8 | Office bags 352 · 0% | Handbags 269 · 0%.
*Assumption:* "organic revenue" = Shopify last-click referrer `search`. That includes free Shopping listings and undercounts buyers who come back by direct or WhatsApp. Jacket buyers often finish on WhatsApp or come back direct (Nov 1-8: organic incl. AI = 23 orders / 170k, avg 7.4k), so jacket "0" is partly attribution. That is still a leak: the online checkout path for jackets is not working.

**Not available from our tools (baseline task Dec 3 + Founder export Dec):** indexed-page count, referring domains (the GSC API has no Links report), Core Web Vitals field data, GA4 (not set up as far as the archive shows).

---

## 2. Strategy pillars, ranked by revenue impact (Alex's call)

| Rank | Pillar | Why here | THE one number it moves | 6-month target |
|---|---|---|---|---|
| **1** | **Organic landing-page conversion (CRO)**: jackets collection + PDPs (size confidence, "why paid online" explained with its reason, WhatsApp order help), homepage tiles, wallets collection filters, proof blocks (real patina / "ordered vs arrived" photos), Microsoft Clarity (free) to see where people get stuck | Same traffic, more orders. Biggest and fastest lever | **Organic CVR** (Shopify, search referrer) | 0.57% → **0.9-1.0%** |
| **2** | **CTR on pages already on page one**: titles/metas (price-in-Pakistan pattern), PDP → collection internal links for broad jacket terms, rich results (breadcrumb, product, FAQ) | Free clicks we already "own" in impressions | **Non-brand CTR** (GSC) | ~4.0% → **5.0-5.5%** |
| **3** | **Commercial collection pages climbing positions 6-15 → top 5**: editorial + FAQ in `custom.editorial` (the only full-HTML surface on collections), internal linking, one canonical shoe page | Money pages rank where the buyers are | **Avg position of the top-25 money queries** | ~7 → **≤5** |
| **4** | **Seasonal gift pages published 3 weeks before demand**: Valentine (Feb 14), Eid ul Fitr (~Mar 10), shaadi season, Father's Day (Jun 20), Eid ul Adha (~May 17); evergreen 11.11 / Blessed Friday URLs reused every year | Pakistan buys leather as gifts; pages need time to index | **Organic revenue in the 2 weeks before each event** | +25-40% vs normal fortnight |
| **5** | **Top-10 / guide content (proven format) + refreshes**: shoes (drafted), bags, belts; refresh jackets/winter/wallet/hub; every article links to 2-3 money collections | Authority + links into collections; low direct CVR | **Blog → product click-through** and blog clicks | +30% blog clicks, 2 new Top-10 pages on page one |
| **6** | **Technical + feed hygiene**: Core Web Vitals, schema validation, sitemap/indexing, Merchant Center feed titles + photos for the 5 no-photo products, 404/redirect audit, sold-out PDPs kept live with "similar in stock", image SEO | Removes ceilings; free-listing clicks | **CWV pass (mobile, 5 key URLs)** + Merchant Center approved items | 4/5 URLs "good" LCP; 0 products without images |
| **7** | **Proof + retention**: genuine reviews with provenance (Google review ask → consent → `custom.reviews_verified`), Shopify Email sign-up (care guide, no discount stacking), monthly care/new-arrivals email | Raises CVR and LTGP; Alex: proof volume beats copy | **Consented reviews added** + email list size | +20-30 reviews; list 0 → 500+ |
| **8** | **Brand, AI-search (GEO) and earned links (free only)**: facts page for AI engines, Bing Webmaster Tools (feeds ChatGPT search), quarterly AI-answer audit, 5 free outreach pitches, AI referral tracking | Slow, compounding; lowest certainty | **Brand-query impressions** + new referring domains | +25-35% brand impressions; +5-10 genuine referring domains |

Tracking that feeds everything: weekly Monday GSC + Shopify read (20 min), monthly report on the 1st working day, quarterly pivot days (26 Feb, 28 May).

---

## 3. Day-by-day calendar (one task a day)

Notes on the calendar:
- **Owner key:** Claude does ~92% of days. Founder has 9 tasks, each 5-20 minutes (mostly "yes/no" on a before/after table, plus 2 GSC exports, Bing setup and outreach). Ahsan has 3 photo tasks. Tahir has 2 data tasks.
- **Batching Founder approvals (proposed):** the "Founder yes" items can be bundled into ONE message on the Monday read instead of interrupting him daily. "Publish after yes" days slip to the next day if the yes hasn't come.
- **Slack days:** Quaid Day (Dec 25), Kashmir Day (Feb 5), Eid ul Fitr (~Mar 10-12), Pakistan Day (Mar 23), Eid ul Adha (~May 17-18). Eid dates depend on the moon, so shift those by ±1 day. There are also 7 month-end BUFFER days.
- **Seasonality built in:** winter jacket peak Dec-Jan (jacket CRO + CTR first); gifting + Ramadan build in Feb (Ramadan starts ~Feb 8, Eid pages live by Feb 10); spring pivot away from jackets in March; summer catalogue in April; Father's Day, Eid ul Adha and 11.11/Blessed Friday 2027 groundwork in May.
- Already scheduled before this plan and kept: Dec 1 BF revert (`trig_01VKvQUEkanNX7cBoyVgdfpN`), Dec 2 URL cleanup (`trig_01BHowarp4eTeyw9xZduj96h`), Dec 7 jackets 2-week read (`trig_01SCnPomaVF9eFyxJq3LU8c3`, folded into the Dec 7 Monday read), Dec 11 price-title CTR check.
- Effort is Claude time unless marked. Sonnet does the default work and Haiku does the data pulls (model policy). Opus is used only for the two pivot days.

### December 2026 - Harvest winter demand, fix the leak (jacket CRO, CTR, measurement)

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-12-01 | Tue | Verify the Blessed Friday price revert + stock-buffer revert finished (auto task); confirm no sale price left in any seo.description | Claude | Read-back note | Merchant Center accuracy | L0 | 20m |
| 2 | 2026-12-02 | Wed | RUN the approved 30-URL cleanup (`url_cleanup_2026-12/`): pre-checks, productUpdate with redirectNewHandle, read back every 301 | Claude | Read-back log + redirect list | Indexed clean URLs / crawl waste | L3 (approved Nov 22) | 90m |
| 3 | 2026-12-03 | Thu | BASELINE REPORT: freeze the numbers in this plan's scorecard (28d GSC, Shopify organic orders/revenue/CVR by landing page) as month 0 | Claude | `reports/2026-12_baseline.md` | Scorecard | L0 | 45m |
| 4 | 2026-12-04 | Fri | Install Microsoft Clarity (free heatmaps + session replays) via a theme snippet on a session branch; mockup + diff to Founder | Claude | Branch commit + one-deploy ask | Organic CVR (diagnosis) | L3 (theme push) | 45m |
| 5 | 2026-12-05 | Sat | CRO teardown of /collections/mens-leather-jackets (3,420 organic sessions in 90d, 0 completed checkouts): list the top 5 blockers (paid-online only, size doubt, 3-week wait, no proof) with fixes | Claude | `cro/jackets_collection_teardown.md` | Jacket organic CVR | L1 | 60m |
| 6 | 2026-12-06 | Sun | Size-confidence block for jacket PDPs: real size chart (S-XXXL chest ranges from live options) + 'not sure? WhatsApp your chest size' line; mockup | Claude | Mockup in `docs/mockups/` | Jacket add-to-cart rate | L1 | 60m |
| 7 | 2026-12-07 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 8 | 2026-12-08 | Tue | Ask Founder for 3 decisions on the jacket teardown (size block, 'why paid online' explainer, WhatsApp order help on collection) in ONE message | Founder | Yes/no on 3 items | Jacket organic CVR | L2 | 5m (Founder) |
| 9 | 2026-12-09 | Wed | Build the approved jacket CRO changes (custom.editorial + snippet) on a branch; CQRO check | Claude | Branch commit | Jacket organic CVR | L1 | 90m |
| 10 | 2026-12-10 | Thu | Deploy jacket CRO changes (one-deploy yes), read back checksums, note before-values | Claude | Live + read-back | Jacket organic CVR | L3 | 30m |
| 11 | 2026-12-11 | Fri | Price-in-Pakistan CTR check (Nov 13 test): jackets, wallets, Oxford pages; revert any page whose price-query CTR is not up ~1 pt | Claude | Verdict table + revert batch if needed | CTR on price queries | L2 if revert | 45m |
| 12 | 2026-12-12 | Sat | 'wallet for men' fix: 16,799 impr, CTR 0.4%, pos 7.4. Check which URL ranks, rewrite title/meta of /collections/mens-leather-wallets to win the click (price band, COD, free delivery over 5,500 online) | Claude | Draft title/meta + before-value | CTR 'wallet for men' | L2 | 45m |
| 13 | 2026-12-13 | Sun | Jacket PDP CTR fix: Spy (21.7k impr, 0.41%) and Alison (21.8k impr, 0.40%) rank for broad 'jackets for men' terms. Add a 'See all men's jackets' internal link high on the PDP and test title wording | Claude | Draft + mockup | Jacket PDP CTR / collection clicks | L2 | 60m |
| 14 | 2026-12-14 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 15 | 2026-12-15 | Tue | Founder yes on wallet + jacket PDP title/meta batch (one message, before/after table) | Founder | Yes/no | CTR | L2 | 5m (Founder) |
| 16 | 2026-12-16 | Wed | Publish the CTR batch (seo title + description together), read back every value | Claude | Live + read-back | CTR | L2 | 30m |
| 17 | 2026-12-17 | Thu | Technical baseline: PageSpeed Insights (free) mobile on home, jackets collection, wallets collection, 1 PDP, top-10 blog; record LCP/INP/CLS | Claude | `tech/cwv_baseline.md` | Core Web Vitals | L0 | 45m |
| 18 | 2026-12-18 | Fri | GSC Page-indexing + Links report export (2 screenshots/CSV, 5 minutes) so we have indexed pages + referring domains baseline (our API can't read these) | Founder | 2 files | Indexed pages, referring domains | L0 | 5m (Founder) |
| 19 | 2026-12-19 | Sat | Sitemap + robots check with gsc_list_sitemaps and gsc_inspect_url on 10 top URLs (incl. the 30 renamed ones) - submitted vs indexed | Claude | `tech/index_check_dec.md` | Indexed pages | L0 | 45m |
| 20 | 2026-12-20 | Sun | Merchant Center health read: disapproved/limited items, missing images (5 no-photo products), price mismatches after the BF revert; fix list | Claude | `tech/gmc_dec.md` | Free-listing clicks | L0 | 45m |
| 21 | 2026-12-21 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 22 | 2026-12-22 | Tue | Ahsan: photograph the 5 live no-photo products (City Backpack, A4 Folder, Voyager, Lanyard, Master's) + measure dimensions; send on WhatsApp | Ahsan | Photos + dimensions | Shopping eligibility, PDP CVR | L1 | 2h (Ahsan) |
| 23 | 2026-12-23 | Wed | Upload Ahsan's photos with alt text + add real dimensions to those 5 descriptions (before-values kept) | Claude | Live + read-back | Shopping eligibility | L2 (pre-approved photo pass) | 60m |
| 24 | 2026-12-24 | Thu | Jackets winter cluster: refresh 'best-winter-jackets-in-pakistan' (8,496 impr, CTR 2.8%, pos 5.9): new intro answering the query in 2 lines, price table, link to collection | Claude | Draft body + SEO | Blog CTR + collection clicks | L2 | 90m |
| 25 | 2026-12-25 | Fri | SLACK (Quaid Day / Christmas): no task. Catch up anything slipped this week | Claude | - | - | - | 0 |
| 26 | 2026-12-26 | Sat | Founder yes + publish winter-jackets refresh; read back | Claude | Live | Blog CTR | L2 | 20m |
| 27 | 2026-12-27 | Sun | Top-10 jackets blog (3,156 clicks, 4 checkouts): add a 'Shop by style' product strip + 'how to order a made-to-order jacket' box to turn readers into buyers | Claude | Draft + before-value | Blog -> product click-through | L2 | 60m |
| 28 | 2026-12-28 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 29 | 2026-12-29 | Tue | Publish top-10 jackets conversion box after Founder yes; read back | Claude | Live | Blog -> product CTR | L2 | 20m |
| 30 | 2026-12-30 | Wed | Gloves winter push: /collections/leather-gloves (CTR 11.4%, pos 8.4) - add 150-word editorial + FAQ (sizes, care) in custom.editorial to climb into top 5 | Claude | Draft | Gloves position | L2 | 60m |
| 31 | 2026-12-31 | Thu | Publish gloves editorial after yes; read back | Claude | Live | Gloves position | L2 | 20m |

### January 2027 - Convert the traffic we already have (collections, homepage, schema, Valentine prep)

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 32 | 2027-01-01 | Fri | Internal-link audit: map every page linking to the 6 money collections (jackets, wallets, bags, gloves, caps, cowboy hats); list orphan or weakly linked products | Claude | `links/internal_map_dec.md` | Collection positions | L0 | 60m |
| 33 | 2027-01-02 | Sat | Read Clarity on jackets + wallets collections (2 weeks of data): top 3 dead clicks / rage clicks / scroll depth; one fix each | Claude | `cro/clarity_read_jan.md` | Organic CVR | L0 | 60m |
| 34 | 2027-01-03 | Sun | Homepage (4,096 organic sessions, CVR 1.05%): above-the-fold test plan - category tiles for jackets/wallets/bags + proof line; mockup | Claude | Mockup | Homepage CVR | L1 | 90m |
| 35 | 2027-01-04 | Mon | MONTHLY REPORT #1 (Dec) + Monday read: scorecard vs target, what moved, what didn't, the ONE fix for January | Claude | `reports/2027-01_monthly.md` + 1-page PDF for the Founder | Scorecard | L0 | 60m |
| 36 | 2027-01-05 | Tue | Founder yes on homepage tile mockup | Founder | Yes/no | Homepage CVR | L2 | 5m (Founder) |
| 37 | 2027-01-06 | Wed | Deploy homepage tiles (one-deploy yes), read back | Claude | Live | Homepage CVR | L3 | 30m |
| 38 | 2027-01-07 | Thu | Wallets collection CRO: filter by type (bifold/card/long), best-seller first sort, price band chips; mockup from Clarity read | Claude | Mockup | Wallet CVR | L1 | 90m |
| 39 | 2027-01-08 | Fri | Deploy wallets collection CRO after yes; read back | Claude | Live | Wallet CVR | L3 | 30m |
| 40 | 2027-01-09 | Sat | Wallet cluster gap list: GSC queries containing 'wallet' at pos 8-30 (smart, card holder, long, women) - pick 3 pages to strengthen | Claude | `content/wallet_gaps.md` | Wallet clicks | L0 | 45m |
| 41 | 2027-01-10 | Sun | Strengthen /collections/smart-wallets (2,698 impr 'smart wallet for men', pos 10): editorial + FAQ + title | Claude | Draft | Smart wallet position | L2 | 60m |
| 42 | 2027-01-11 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 43 | 2027-01-12 | Tue | Publish smart-wallets editorial after yes | Claude | Live | Smart wallet position | L2 | 20m |
| 44 | 2027-01-13 | Wed | /collections/womens-leather-wallets (pos 11.3): editorial + gift angle + title | Claude | Draft | Position | L2 | 60m |
| 45 | 2027-01-14 | Thu | Publish women's wallets after yes | Claude | Live | Position | L2 | 20m |
| 46 | 2027-01-15 | Fri | Laptop bags collection (pos 14.5, 5,277 impr): editorial + FAQ (sizes fit 14/15.6 in from real specs), title with price band | Claude | Draft | Laptop bag position | L2 | 60m |
| 47 | 2027-01-16 | Sat | Publish laptop bags editorial after yes | Claude | Live | Position | L2 | 20m |
| 48 | 2027-01-17 | Sun | Leather shoes: /collections/mens-leather-shoes sits at pos 25 while kdv-shoes ranks 9.6 - pick ONE canonical shoe page, fix links/canonical so they stop splitting | Claude | Proposal | Shoe position | L2 | 60m |
| 49 | 2027-01-18 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 50 | 2027-01-19 | Tue | Apply shoe canonical/links fix after yes; read back | Claude | Live | Shoe position | L2 / L3 if theme | 45m |
| 51 | 2027-01-20 | Wed | Publish the drafted Top 10 Leather Shoe Brands in Pakistan article (CQRO re-check, prices refreshed) | Claude | Live article | Shoe cluster clicks | L2 | 60m |
| 52 | 2027-01-21 | Thu | Schema check: Rich Results Test on 5 PDPs, 3 collections, 3 articles (Product, BreadcrumbList, FAQ, Article); fix list | Claude | `tech/schema_jan.md` | Rich results | L0 | 45m |
| 53 | 2027-01-22 | Fri | Fix schema errors found (theme branch) | Claude | Branch commit | Rich results | L3 (theme) | 60m |
| 54 | 2027-01-23 | Sat | Ahsan: 10 real 'in use' photos of best-sellers (Mocha Mate, Executive belt, gloves, Diva Tote) on a plain desk, phone is fine | Ahsan | 10 photos | Image search + PDP CVR | L1 | 1h (Ahsan) |
| 55 | 2027-01-24 | Sun | Image SEO pass: add Ahsan's photos as 2nd image on those PDPs with descriptive file names + alt text | Claude | Live | Image clicks, PDP CVR | L2 | 60m |
| 56 | 2027-01-25 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 57 | 2027-01-26 | Tue | Reviews with provenance: list delivered orders from Dec (via PostEx worker data) whose customers left a Google review; ask Ahsan to get written OK to quote on site | Claude | Ask list | Review count | L2 | 45m |
| 58 | 2027-01-27 | Wed | Add consented reviews to custom.reviews_verified (provenance logged: who, when, how) | Claude | Live | PDP CVR | L2 | 45m |
| 59 | 2027-01-28 | Thu | Valentine's gift page prep: GSC/known demand for 'gift for husband/boyfriend' - draft /pages or collection 'Leather Gifts for Him' (wallet+belt+gloves) with real prices | Claude | Draft | Gift query clicks | L2 | 90m |
| 60 | 2027-01-29 | Fri | Publish Valentine gift page (needs ~3 weeks to index) after yes; link from homepage + wallets | Claude | Live | Gift query clicks | L2 | 30m |
| 61 | 2027-01-30 | Sat | Bing Webmaster Tools: import from GSC (free, 5 minutes) - Bing feeds ChatGPT search | Founder | Verified site | AI/Bing visibility | L1 | 5m (Founder) |
| 62 | 2027-01-31 | Sun | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |

### February 2027 - Gifting + Ramadan/Eid build (pages live 3 weeks before demand), first authority work

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 63 | 2027-02-01 | Mon | MONTHLY REPORT #2 (Jan) + Monday read | Claude | `reports/2027-02_monthly.md` | Scorecard | L0 | 60m |
| 64 | 2027-02-02 | Tue | Eid gift guide draft: 'Eid gifts for men in Pakistan' (wallets, belts, shoes, gloves off-season excluded) with price bands; publish by Feb 10 so it indexes before the last-10-days peak | Claude | Draft | Eid query clicks | L2 | 90m |
| 65 | 2027-02-03 | Wed | Publish Eid gift guide after yes; internal links from hub + wallets + belts | Claude | Live | Eid clicks | L2 | 30m |
| 66 | 2027-02-04 | Thu | Belts collection: editorial + FAQ (sizing by waist, buckle types) + title with price band | Claude | Draft | Belt position | L2 | 60m |
| 67 | 2027-02-05 | Fri | SLACK (Kashmir Day) | Claude | - | - | - | 0 |
| 68 | 2027-02-06 | Sat | Publish belts editorial after yes | Claude | Live | Belt position | L2 | 20m |
| 69 | 2027-02-07 | Sun | Ramadan/Eid homepage + announcement copy (Eid delivery cut-off date from PostEx reality, no fake urgency) | Claude | Mockup | Homepage CVR | L2 | 45m |
| 70 | 2027-02-08 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 71 | 2027-02-09 | Tue | Tahir: confirm the real Eid delivery cut-off date with PostEx + which best-sellers have stock for Eid | Tahir | Date + stock list | Honest cut-off, fewer refusals | L1 | 20m (Tahir) |
| 72 | 2027-02-10 | Wed | Deploy Eid homepage block (time-locked, same pattern as 11.11) after yes | Claude | Live | Homepage CVR | L3 | 45m |
| 73 | 2027-02-11 | Thu | Jacket season taper: switch jackets collection meta from 'winter' to evergreen (biker/bomber all year) - prevent CTR crash in spring | Claude | Draft | Jacket CTR off-season | L2 | 30m |
| 74 | 2027-02-12 | Fri | Publish jacket evergreen metas after yes | Claude | Live | Jacket CTR | L2 | 20m |
| 75 | 2027-02-13 | Sat | Top-10 wallet blog refresh (596 clicks, pos 5.8): 'Updated Feb 2027', price bands, link to Eid guide + smart wallets | Claude | Draft | Blog CTR | L2 | 60m |
| 76 | 2027-02-14 | Sun | Publish wallet blog refresh after yes | Claude | Live | Blog CTR | L2 | 20m |
| 77 | 2027-02-15 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 78 | 2027-02-16 | Tue | Hub page refresh (/blogs/news/top-leather-brands-in-pakistan, 2,902 impr, CTR 3.2%): answer-first intro, links to every Top 10 | Claude | Draft | Hub CTR | L2 | 60m |
| 79 | 2027-02-17 | Wed | Publish hub refresh after yes | Claude | Live | Hub CTR | L2 | 20m |
| 80 | 2027-02-18 | Thu | GEO check: ask ChatGPT/Perplexity/Gemini/Google AI Mode 15 buyer questions ('best leather wallet brand in Pakistan', etc.); log who gets cited | Claude | `geo/ai_audit_feb.md` | AI-search mentions | L0 | 60m |
| 81 | 2027-02-19 | Fri | Add an /llms.txt-style 'About Kordovan' facts page (who, what, materials, delivery, warranty, COD) linked from footer - one citable source for AI engines | Claude | Draft page | AI-search mentions | L2 | 60m |
| 82 | 2027-02-20 | Sat | Publish facts page after yes | Claude | Live | AI-search mentions | L2 | 20m |
| 83 | 2027-02-21 | Sun | Earned-links list (free): 20 Pakistani fashion/gift bloggers, 'best of' lists that already rank, student/menswear forums; what each would want | Claude | `links/outreach_list.md` | Referring domains | L0 | 90m |
| 84 | 2027-02-22 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 85 | 2027-02-23 | Tue | Founder picks 5 of the 20 to approach + OK on the pitch wording (no paid placements) | Founder | 5 names + yes | Referring domains | L2 | 10m (Founder) |
| 86 | 2027-02-24 | Wed | Wedding/shaadi angle article: 'What to gift the groom: leather wallet, belt, shoes' - real prices, no Karachi | Claude | Draft | Long-tail clicks | L2 | 90m |
| 87 | 2027-02-25 | Thu | Publish shaadi gift article after yes | Claude | Live | Long-tail clicks | L2 | 20m |
| 88 | 2027-02-26 | Fri | QUARTERLY PIVOT DAY #1 (week 13): apply the kill/pivot rules to every pillar; Alex verdict; move effort from the worst pillar to the best for Mar-May | Claude | `reports/2027-Q1_pivot.md` -> Founder | All pillars | L2 (Founder reads) | 90m |
| 89 | 2027-02-27 | Sat | Mid-quarter CTR re-read: every page changed since Dec 1 - keep / revert (quality guard #4) | Claude | Verdict table | CTR | L2 if revert | 60m |
| 90 | 2027-02-28 | Sun | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |

### March 2027 - Eid peak, then spring pivot away from jackets (bags, hats, shoes)

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 91 | 2027-03-01 | Mon | MONTHLY REPORT #3 (Feb) + Monday read | Claude | `reports/2027-03_monthly.md` | Scorecard | L0 | 60m |
| 92 | 2027-03-02 | Tue | Eid last-10-days watch: daily GSC on gift pages; fix any title not getting clicks (one change only) | Claude | Note | Eid clicks | L2 | 30m |
| 93 | 2027-03-03 | Wed | Eid post-mortem: gift guide clicks, orders by landing page, refusal rate on organic COD orders | Claude | `reports/eid_2027.md` | Organic revenue | L0 | 60m |
| 94 | 2027-03-04 | Thu | Spring pivot plan: which non-jacket pages get the jacket internal-link slots on home + menu for Apr-Sep (data from Q1) | Claude | Proposal | Non-jacket clicks | L2 | 45m |
| 95 | 2027-03-05 | Fri | Apply spring menu/home link swap after yes (theme) | Claude | Live | Non-jacket clicks | L3 | 45m |
| 96 | 2027-03-06 | Sat | Office/laptop bags blog refresh (2,884 impr, pos 8.7) + new real dimensions | Claude | Draft | Blog clicks | L2 | 60m |
| 97 | 2027-03-07 | Sun | Publish office bags refresh after yes | Claude | Live | Blog clicks | L2 | 20m |
| 98 | 2027-03-08 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 99 | 2027-03-09 | Tue | Women's handbags collection (6,510 impr, CTR 3.5%, pos 9.3): editorial, vegan items labelled honestly, title | Claude | Draft | Handbag position | L2 | 60m |
| 100 | 2027-03-10 | Wed | SLACK (Eid ul Fitr, expected ~Mar 10, moon-dependent): no task | Claude | - | - | - | 0 |
| 101 | 2027-03-11 | Thu | SLACK (Eid holidays) | Claude | - | - | - | 0 |
| 102 | 2027-03-12 | Fri | SLACK (Eid holidays) | Claude | - | - | - | 0 |
| 103 | 2027-03-13 | Sat | Publish handbags editorial after yes | Claude | Live | Position | L2 | 20m |
| 104 | 2027-03-14 | Sun | New article: 'Top 10 leather bag brands in Pakistan' (proven format, price bands only) | Claude | Draft | Bag cluster clicks | L2 | 2h |
| 105 | 2027-03-15 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 106 | 2027-03-16 | Tue | Publish bag Top 10 after CQRO + yes | Claude | Live | Bag clicks | L2 | 30m |
| 107 | 2027-03-17 | Wed | Cowboy hats (CTR 13%, pos 4.1, the best-CTR money page): add FAQ + sizing to push into top 3 | Claude | Draft | Hat position | L2 | 45m |
| 108 | 2027-03-18 | Thu | Publish cowboy hats FAQ after yes | Claude | Live | Hat position | L2 | 20m |
| 109 | 2027-03-19 | Fri | Core Web Vitals re-read on the same 5 URLs; one fix for the worst (image weight, font, JS) | Claude | `tech/cwv_mar.md` | CWV | L0 | 45m |
| 110 | 2027-03-20 | Sat | Ship the CWV fix on a branch -> deploy after yes | Claude | Live | CWV pass rate | L3 | 60m |
| 111 | 2027-03-21 | Sun | Outreach: send pitches to the 5 approved targets (Founder's account or the brand email, free) | Founder | 5 sent | Referring domains | L2 | 20m (Founder) |
| 112 | 2027-03-22 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 113 | 2027-03-23 | Tue | SLACK (Pakistan Day) | Claude | - | - | - | 0 |
| 114 | 2027-03-24 | Wed | Sold-out audit: sold-out PDPs still getting clicks - add 'similar in stock' links (keep pages live for SEO) | Claude | Draft list | Lost-click recovery | L2 | 45m |
| 115 | 2027-03-25 | Thu | Apply sold-out 'similar' links after yes | Claude | Live | Recovery | L2 | 45m |
| 116 | 2027-03-26 | Fri | Review round 2 (provenance): Feb-Mar delivered buyers who replied to the Google review ask | Claude | Ask list | Review count | L2 | 30m |
| 117 | 2027-03-27 | Sat | Add consented reviews round 2 | Claude | Live | PDP CVR | L2 | 30m |
| 118 | 2027-03-28 | Sun | Shopify Email sign-up block on blog posts + footer: free care-guide PDF (no discount stacking); mockup -> yes -> live | Claude | Live | Email list size | L2 | 60m |
| 119 | 2027-03-29 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 120 | 2027-03-30 | Tue | Email: first monthly 'care + new arrivals' Shopify Email to opted-in list (free tier) | Claude | Draft -> Founder | Returning-customer rate | L2 | 60m |
| 121 | 2027-03-31 | Wed | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |

### April 2027 - Summer catalogue + proof + feed quality

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 122 | 2027-04-01 | Thu | MONTHLY REPORT #4 (Mar, incl. Eid read: gift pages vs last 2 weeks of Ramadan) | Claude | `reports/2027-04_monthly.md` | Scorecard | L0 | 60m |
| 123 | 2027-04-02 | Fri | Shoes cluster: Oxford price page (1,125 impr 'oxford shoes price in pakistan', CTR 0.7%) - title/meta + editorial | Claude | Draft | Shoe CTR | L2 | 45m |
| 124 | 2027-04-03 | Sat | Publish Oxford/shoe CTR fix after yes | Claude | Live | Shoe CTR | L2 | 20m |
| 125 | 2027-04-04 | Sun | Summer article: 'How to care for leather in Pakistani summer heat' (real care advice, links to products) | Claude | Draft | Long-tail + email signups | L2 | 90m |
| 126 | 2027-04-05 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 127 | 2027-04-06 | Tue | Publish summer care article after yes | Claude | Live | Long-tail clicks | L2 | 20m |
| 128 | 2027-04-07 | Wed | Travel bags collection (CTR 7.2%, pos 9.1): editorial + FAQ (cabin size from real specs) | Claude | Draft | Position | L2 | 60m |
| 129 | 2027-04-08 | Thu | Publish travel bags after yes | Claude | Live | Position | L2 | 20m |
| 130 | 2027-04-09 | Fri | Ahsan: patina photo set (Founder's own used wallet vs new) + 3 'ordered vs arrived' photos for proof blocks | Ahsan | Photos | PDP CVR | L1 | 45m (Ahsan) |
| 131 | 2027-04-10 | Sat | Patina proof block on wallet PDPs (real photos only) | Claude | Mockup -> yes | Wallet PDP CVR | L2 | 60m |
| 132 | 2027-04-11 | Sun | Deploy patina block after yes | Claude | Live | Wallet CVR | L3 | 30m |
| 133 | 2027-04-12 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 134 | 2027-04-13 | Tue | Internal-link round 2: every blog post links to 2-3 money collections with descriptive anchors; fix any broken link | Claude | Batch | Collection positions | L2 | 90m |
| 135 | 2027-04-14 | Wed | GEO re-audit (same 15 questions as Feb) - did the facts page / outreach change citations? | Claude | `geo/ai_audit_apr.md` | AI mentions | L0 | 45m |
| 136 | 2027-04-15 | Thu | Belt cluster article: 'Top 10 leather belt brands in Pakistan' | Claude | Draft | Belt clicks | L2 | 2h |
| 137 | 2027-04-16 | Fri | Publish belt Top 10 after yes | Claude | Live | Belt clicks | L2 | 30m |
| 138 | 2027-04-17 | Sat | Merchant Center re-read: product titles in feed (lead with product type + colour), missing GTIN/brand flags | Claude | `tech/gmc_apr.md` | Free-listing clicks | L0 | 45m |
| 139 | 2027-04-18 | Sun | Fix top 20 feed titles via seo/title changes (sweep every surface) | Claude | Live | Free-listing CTR | L2 | 60m |
| 140 | 2027-04-19 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 141 | 2027-04-20 | Tue | Caps collection (CTR 10.5%, pos 5.3): summer caps editorial + FAQ | Claude | Draft | Caps position | L2 | 45m |
| 142 | 2027-04-21 | Wed | Publish caps editorial after yes | Claude | Live | Position | L2 | 20m |
| 143 | 2027-04-22 | Thu | Tahir: list of new products arriving Apr-Jun (so new PDPs launch with full SEO from day 1) | Tahir | List | New-page indexing speed | L1 | 15m (Tahir) |
| 144 | 2027-04-23 | Fri | SEO launch template for new products (title, meta, 200-word description, alt, metafields, collection links) - checklist file | Claude | `seo/NEW_PRODUCT_CHECKLIST.md` | Time-to-rank | L0 | 45m |
| 145 | 2027-04-24 | Sat | GSC image-search read (searchType image): which product images get impressions; rename/alt the top 20 losers | Claude | Batch | Image clicks | L2 | 60m |
| 146 | 2027-04-25 | Sun | /collections/women ranks pos 2.9 with CTR 2.2% - wrong-intent title? rewrite title/meta to match the queries it shows for | Claude | Draft -> yes -> live | Women's CTR | L2 | 45m |
| 147 | 2027-04-26 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 148 | 2027-04-27 | Tue | 404 + redirect audit: GSC not-found URLs (Founder export from Dec/Feb) + old handles; add missing 301s | Claude | Live redirects | Crawl health | L2 | 60m |
| 149 | 2027-04-28 | Wed | Search-term mining in Shopify site search (what people type and don't find) -> content/merch gaps | Claude | Gap list | Site CVR | L0 | 45m |
| 150 | 2027-04-29 | Thu | Search-term fixes: synonyms/redirects for zero-result searches | Claude | Live | Site search CVR | L2 | 45m |
| 151 | 2027-04-30 | Fri | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |

### May 2027 - Scale what worked; Father's Day, Eid ul Adha, 11.11/Blessed Friday 2027 groundwork

| # | Date | Day | Task (one action) | Owner | Deliverable | Metric moved | Level | Effort |
|---|---|---|---|---|---|---|---|---|
| 152 | 2027-05-01 | Sat | Father's Day gift page draft (Jun 20) - publish by May 20 to index | Claude | Draft | Gift clicks | L2 | 60m |
| 153 | 2027-05-02 | Sun | Publish Father's Day page after yes; link from home + wallets | Claude | Live | Gift clicks | L2 | 20m |
| 154 | 2027-05-03 | Mon | MONTHLY REPORT #5 (Apr) + Monday read | Claude | `reports/2027-05_monthly.md` | Scorecard | L0 | 60m |
| 155 | 2027-05-04 | Tue | Evergreen sale URLs: create (draft, unpublished) /collections/sale-1111 and /collections/blessed-friday-sale pages that we REUSE every year so they build authority | Claude | Proposal | Sale-event organic clicks | L2 | 45m |
| 156 | 2027-05-05 | Wed | Founder yes on evergreen sale URLs | Founder | Yes/no | Sale clicks | L2 | 5m (Founder) |
| 157 | 2027-05-06 | Thu | More of what worked: the best-performing Dec-Apr page change - copy the pattern to 5 similar pages | Claude | Batch | Whichever metric won | L2 | 90m |
| 158 | 2027-05-07 | Fri | Publish the 'more of what worked' batch after yes | Claude | Live | Same | L2 | 30m |
| 159 | 2027-05-08 | Sat | Quick-win sweep #2: GSC queries pos 4-15 with >500 impr in last 90d - one title/meta fix each for the top 10 | Claude | Draft batch | CTR | L2 | 90m |
| 160 | 2027-05-09 | Sun | Publish quick-win batch #2 after yes | Claude | Live | CTR | L2 | 30m |
| 161 | 2027-05-10 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 162 | 2027-05-11 | Tue | Jacket pre-season plan (Oct 2027 demand starts ~Sep): what to refresh in Aug, using this winter's data | Claude | `seo/jackets_preseason_2027.md` | Next-winter jacket clicks | L0 | 60m |
| 163 | 2027-05-12 | Wed | Review round 3 (provenance) + update review counts | Claude | Live | PDP CVR | L2 | 45m |
| 164 | 2027-05-13 | Thu | CWV final read on the 5 URLs vs December baseline | Claude | Table | CWV | L0 | 30m |
| 165 | 2027-05-14 | Fri | Referring-domains + indexed pages re-export (GSC Links + Page indexing) | Founder | 2 files | Referring domains, indexed | L0 | 5m (Founder) |
| 166 | 2027-05-15 | Sat | GEO audit #3 (same 15 questions) | Claude | Log | AI mentions | L0 | 45m |
| 167 | 2027-05-16 | Sun | Email: Father's Day + Eid ul Adha send to opted-in list | Claude | Draft -> Founder | Returning rate | L2 | 45m |
| 168 | 2027-05-17 | Mon | SLACK (Eid ul Adha, expected ~May 16-18, moon-dependent) | Claude | - | - | - | 0 |
| 169 | 2027-05-18 | Tue | SLACK (Eid ul Adha holidays) | Claude | - | - | - | 0 |
| 170 | 2027-05-19 | Wed | Thin-content re-scan: any product < 150 words (new arrivals) -> batch rewrite | Claude | Batch | Position | L2 | 90m |
| 171 | 2027-05-20 | Thu | Publish thin-content batch after yes | Claude | Live | Position | L2 | 30m |
| 172 | 2027-05-21 | Fri | Organic COD refusal by landing page (PostEx outcomes x first-visit landing page): drop or fix pages that bring refusing buyers | Claude | `reports/organic_refusals.md` | Real (delivered) organic revenue | L0 | 60m |
| 173 | 2027-05-22 | Sat | AI referral tracking: Shopify sessions from chatgpt.com / perplexity / copilot referrers since Dec; add to scorecard | Claude | Scorecard row | AI-search traffic | L0 | 30m |
| 174 | 2027-05-23 | Sun | Accessories cluster: key chains, card holders, watch box, tray - one editorial for the accessories/gifts collection | Claude | Draft -> yes -> live | Accessory clicks | L2 | 60m |
| 175 | 2027-05-24 | Mon | Weekly read: GSC 7d vs prior 7d (clicks, CTR, top-20 money queries) + Shopify organic sessions/CVR/orders; log to scorecard; flag any page down >20% | Claude | `reports/weekly_YYYY-MM-DD.md` (5 lines) | All (early warning) | L0 | 20m |
| 176 | 2027-05-25 | Tue | Jun-Nov content calendar draft (11.11 + Blessed Friday 2027 landing pages ready by Oct 1) | Claude | Draft | Sale-event organic revenue | L1 | 60m |
| 177 | 2027-05-26 | Wed | Clean the scorecard + archive all before-values into one index file for the H1 review | Claude | `ops/marketing/seo/H1_2027_index.md` | Hygiene | L0 | 45m |
| 178 | 2027-05-27 | Thu | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |
| 179 | 2027-05-28 | Fri | QUARTERLY PIVOT DAY #2 (week 26): full 6-month review vs scorecard; Alex verdict; draft Jun-Nov 2027 plan (11.11 + Blessed Friday 2027 SEO) | Claude | `reports/2027-H1_review.md` -> Founder | All pillars | L2 | 2h |
| 180 | 2027-05-29 | Sat | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |
| 181 | 2027-05-30 | Sun | BUFFER: finish anything slipped; if nothing slipped, pull the next month's first task forward | Claude | - | - | - | 0-60m |
| 182 | 2027-05-31 | Mon | MONTHLY REPORT #6 (May) + hand the Jun-Nov plan to the Founder for a yes | Claude | `reports/2027-06_monthly.md` + next plan | Scorecard | L2 | 60m |

---

## 4. KPI scorecard (monthly targets, realistic ranges)

| Metric (source) | Baseline | Dec 26 | Jan 27 | Feb 27 | Mar 27 | Apr 27 | May 27 |
|---|---|---|---|---|---|---|---|
| GSC clicks / month | 8,495 (28d) | 9,000-10,500 | 9,000-10,500 | 7,500-9,500 | 8,000-9,500 | 8,000-10,000 | 9,000-11,000 |
| GSC impressions / month | 192k (28d) | 200-230k | 200-230k | 170-210k | 170-210k | 180-220k | 190-240k |
| Site CTR | 4.42% | 4.5-5.0% | 4.8-5.3% | 5.0-5.5% | 5.0-5.5% | 5.0-5.6% | 5.2-5.8% |
| Avg position (weighted) | 6.9 | 6.5-7.0 | 6.3-6.8 | 6.2-6.8 | 6.0-6.6 | 5.8-6.4 | 5.6-6.2 |
| Organic orders (Shopify, search) | ~47/mo | 50-60 | 55-65 | 55-65 | 60-75 (Eid) | 55-70 | 65-80 |
| Organic net revenue (PKR) | ~194k/mo | 210-260k | 230-280k | 230-280k | 260-320k | 240-300k | 280-340k |
| Organic CVR | 0.57% | 0.60-0.70% | 0.70-0.80% | 0.75-0.85% | 0.85-0.90% | 0.85-0.95% | 0.90-1.00% |
| Jackets collection organic checkouts | 0 / 90d | ≥3 | ≥5 | n/a (season) | – | – | – |
| Core Web Vitals (5 key URLs, mobile LCP "good") | PSI baseline in Dec | measure | – | – | ≥3/5 | – | ≥4/5 |
| Indexed pages (active products + collections) | Founder export Dec | measure | – | ≥95% | – | – | ≥95% |
| Referring domains (GSC Links) | Founder export Dec | measure | – | – | +2-4 | – | +5-10 total |
| Brand-query impressions ("kordovan…", 90d) | 3,326 | – | – | +10% | – | – | +25-35% |
| Consented reviews added | 0 | – | 5-10 | – | +5-10 | – | +5-10 |
| Email subscribers (organic sign-up) | ~0 | – | 50-100 | 150 | 250 | 350 | 500+ |

**Assumptions:** (1) Jacket queries are a large share of impressions and fall from late February, so total clicks dip in Feb-Mar even if every page improves. Judge spring on **non-jacket non-brand clicks** (baseline Dec 3) and on CVR, not on total clicks. (2) Organic revenue is last-click Shopify `search`; delivered (post-refusal) revenue is ~10-15% lower, checked in the May refusal task. (3) No paid tools, no paid links, the same team, ~1 hour a day of Claude time. (4) We have no prior-year GSC data for these months, so the ranges are wide on purpose. Re-set them at the Feb 26 pivot.

---

## 5. Kill / pivot rules (applied at the 8-week mark and on each pivot day)

| Pillar | Underperforming means (after 8 weeks) | Then we… |
|---|---|---|
| 1 CRO | Organic CVR not up ≥0.1 pt, OR jackets collection still 0 checkouts after the size/WhatsApp changes | Revert the change that hurt (Clarity + before-values), and move jacket effort to a "WhatsApp-to-order" path the team already uses. Don't add more page elements |
| 2 CTR | A rewritten page's CTR is not up ≥0.5 pt at the same position within 3-4 weeks | Revert to the before-value (quality guard #4). Test ONE different angle, and stop after 2 failed angles |
| 3 Collection positions | Target query is not up ≥2 positions in 8 weeks | Stop adding words. Add internal links from the strongest page (top-10 jacket blog / home) instead, then re-read |
| 4 Seasonal pages | Not indexed 10 days after publish, or <50 impressions by the event | Request indexing, link from home, and next year publish 5 weeks early |
| 5 Content | A new article has <300 impressions after 8 weeks | No more new articles in that category. Fold the article into the hub/collection editorial and 301 it |
| 6 Technical | CWV fix doesn't move lab LCP | Revert. Only fix what PageSpeed attributes (images/fonts/JS) |
| 7 Proof/retention | <5 consented reviews in a quarter | Simplify the ask (Ahsan does it by voice on WhatsApp, the customer says yes, we transcribe) |
| 8 Brand/GEO/links | 0 new referring domains after 5 pitches | Stop outreach. Put that time back into pillar 1 |

**Global rule (Alex):** if organic CVR is flat at the **Feb 26 pivot**, the March-May content tasks are cut in half and the freed days go to CRO. Conversion is the constraint until it moves.

---

## 6. Risks

1. **Seasonality masks progress.** Jacket demand collapses in spring. Mitigation: judge spring on non-jacket clicks and CVR.
2. **Approval bottleneck.** About 70 L2 "after yes" days. If the Founder is slow, the calendar slips. Mitigation: one weekly bundled yes.
3. **Theme pushes deploy LIVE** (L3 every time). Every push goes on a branch with a mockup, a `node --check`, tag balance and checksum read-back.
4. **Policy and brand words creeping back** (Karachi, coins, exotic/tobacco words, full-grain on jackets, workshop). Mitigation: CQRO check on every customer-facing draft (Sonnet/Haiku output).
5. **Attribution blind spots.** WhatsApp and direct jacket orders are invisible to the "search" channel. Mitigation: ask Ahsan "how did you find us?" on WhatsApp jacket orders (logged in the nightly run).
6. **Algorithm updates / AI Overviews** eating clicks on informational queries (blog). Mitigation: commercial pages are pillar 1-3, and the facts page + GEO audit cover this.
7. **Microsoft Clarity is a third-party script.** It needs one line in the Privacy policy (the Founder edits policies) and must not hurt LCP (load async; check with the CWV re-read).
8. **Stock-outs.** Ranking pages for sold-out items waste clicks. The sold-out "similar in stock" task covers this. Tahir's arrivals list keeps new PDPs SEO-ready.
9. **Eid dates move with the moon.** Gift pages are published early, so a ±1 day shift doesn't matter.
10. **The GSC connector ignores `dimensionFilterGroups`.** Always filter locally; run `gsc_debug` if numbers look odd.

---

## 7. Decisions needed from the Founder

1. **Approve the pillar order** (conversion first, CTR second, content later), Alex's call.
2. **Microsoft Clarity** (free heatmaps/replays): OK to build it on a branch for a one-deploy yes in December? Needs one Privacy-policy line that you add.
3. **Weekly bundled approvals:** OK to send all L2 before/after tables once a week (Monday) instead of day by day?
4. **Jacket direction:** OK to test a "not sure of size? WhatsApp us your chest size" line + a short "why jackets are paid online" explainer (with the reason: cut for one customer, can't be resold) on the jackets collection and PDPs?
