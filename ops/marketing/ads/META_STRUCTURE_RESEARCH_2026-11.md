# Meta ads structure research (Founder ask Nov 28) — what is proven, what is not
Method: 12 web searches, read from search summaries (NOT the primary pages; flagged where that matters). Evidence grades: A = Meta's own docs/posts; B = respected independent practitioner; C = agency/vendor anecdote (single client, no method shown). Nothing here is "100% proven" — no independent controlled study of ad-set structure exists. Where evidence is thin it says so.

## Why one ad takes all the spend (the Founder's problem)
Meta optimises total results per ad set, not an even split. It commits early on the ad with the best early signal. Loomer: seen 99.9% of budget on one ad. This is by design; forcing equal spend inside a mixed ad set hides which ad can scale (B). Fix = isolate tests, not fight the algorithm.

## 15 cases / data points
| # | Source | Finding | Grade | Link |
|---|---|---|---|---|
| 1 | Meta Oct 2026 peak-season post (via PPC Land / Relevant Audience) | Ad sets under ~50 conversions/week cost ~28% more per purchase; ad sets supportable = weekly budget / (cost per result x 50). Caveat: small ad sets differ in other ways too | A (second-hand) | https://ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase/ |
| 2 | Meta Marketing API split-testing docs | Official test = 2-5 cells, one ad each, equal split, winner = lowest CPA; warns against uneven groups | A | https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/split-testing |
| 3 | Loomer, one ad gets all the budget | 99.9% of spend on one ad; options = isolate new ads in own test | B | https://www.jonloomer.com/one-ad-gets-all-the-budget/ |
| 4 | Loomer, Creative Testing tool | Test takes ~20% of budget (or all of a brand-new ad set's); one-ad-per-ad-set tests have "serious flaws" vs the tool | B | https://www.jonloomer.com/meta-creative-testing/ |
| 5 | Smartmarketer, Clean-eez | 8 campaigns -> 2, reload creative: CPM -20%, CPA -35% in days (one client; warns of phantom new-customer growth) | C | https://smartmarketer.com/meta-andromeda-transformed-facebook-ads/ |
| 6 | Seer Interactive | Account consolidation: CTR +80%, CPC -44% (snippet only, not opened) | C | https://www.seerinteractive.com/insights/meta-ad-account-consolidation |
| 7 | Common Thread (3,014 advertisers, second-hand) | Average ROAS -7% during Andromeda rollout: consolidation is not a free win | C | https://commonthreadco.com/blogs/coachs-corner/meta-andromeda-roas-creative-strategy-2026 |
| 8 | TenTen (B2B SaaS, Medium) | 3 -> 15 ads in one ad set made CPL worse first | C | https://medium.com/@tentenco/meta-ads-strategy-2026-why-andromeda-gem-and-ios-26-broke-the-old-playbook-78cba1ad4820 |
| 9 | RevenueCat creative testing | Spend +74.6%, CAC -40%: 70 statics wk1, 40/60 winners/testing budget, iterate on winners | C | https://www.revenuecat.com/blog/growth/meta-ads-cac-creative-testing |
| 10 | Motion, 6,015 accounts | ~6.6 creatives/wk -> 0.7 winners/month; ~15.9/wk -> 2.0. Association, not proof | B | https://motionapp.com/library/research/creative-benchmarks-2026/volume-vs-winners |
| 11 | Meta/Byltbasics | Advantage+ Sales beat all other campaigns combined on ROAS | A (vendor case) | https://business.instagram.com/success/bylt-basics |
| 12 | Agency split tests | Advantage+ 4.25 vs 3.78 ROAS; soy-candle brand 3.90 vs 2.39 | C | https://guptamedia.com/insights/tested-meta-advantage-shopping |
| 13 | Power Digital citing Meta | Advantage+ Shopping: 17% lower CPA, 32% higher ROAS (Meta); 26%/58% (their accounts). Works when creative is already strong | A/C | https://powerdigitalmarketing.com/blog/how-to-drive-e-commerce-growth-with-metas-new-advantage-shopping-feature/ |
| 14 | ATTN 2026 benchmark via Segwise | Static CPA $34.50 vs video $48.20 in DTC direct response; video wins CTR, static wins CPM | C | https://segwise.ai/blog/static-video-ratio-meta-ads |
| 15 | Motion 2026 via Webtonic | UGC-style beats polished: CTR +27%, CVR +19% (DTC) | C | https://www.webtonic.io/blog/e-commerce-ad-creative-statistics |
COD angle (thin, vendor-only): COD RTO 25-30% in India; judge by delivered-and-kept, exclude defaulters (we already do) — https://www.egrow.com/en/blog/meta-ads-for-cod-products-2026-playbook

## What the evidence agrees on (use these)
1. Fewer, bigger ad sets (Meta, #1; Loomer; #5/#6 though #7/#8 warn of a dip). 
2. Test new creative in its OWN place so the incumbent cannot starve it (#2, #3, #4).
3. Creative diversity beats audience slicing (Meta guidance via Loomer; #9, #10).
4. Static is fine for direct response; mix formats (#14, Meta "static+video +17% lift").
5. Judge on money that survives (COD refusal), not Meta's number.

## Our own math (Shopify, Nov 7-28)
Online orders ~8.8/day (193 in 22 days); social-referred ~3.9/day in the last 14 days. Meta's own formula: 5,000/day x 7 = 35,000/week / (CPA ~1,300 x 50 = 65,000) = 0.5 ad sets. We run 6. We cannot satisfy the 50/week rule on any ad set except H1 Mocha (1,860/day ~ 1.4 orders/day = 10/week; still under). So every ad set is "learning limited": consolidation matters more for us than for most.
25 Meta sales/day needs ~Rs 32,000-40,000/day at our real CPA (1,300-1,600), 6-8x today's 5,000. At 5,000/day expect ~4-6 Meta orders/day. 25 total online orders/day (all channels) needs ~2.5x today's volume: spend + conversion rate + AOV all together. The path = Dec CRO fixes (checkout/jacket/cart), creative winners, then budget scaled only on winners with proven CPA.

## Recommended structure (Alex lens; for Founder yes)
1. Keep proven ad sets untouched (H1, Retarget v2, RT-W): resetting learning costs money.
2. TEST = Meta's official creative test (one ad per cell, equal split) via Ads Manager or API (ads_experiment_abtest_create_test), 2 ads per test max, 7-10 days, cells identical audience. Read at >=1x ceiling spend per ad, verdict 1.5x (Alex). One product per test so the winner is clean.
3. Winners graduate into ONE Prospecting ad set (not new ad sets per ad). Max 3-4 live ads there; pause the loser at 1.5x ceiling.
4. Total live ad sets in Dec: 5 (H1, Prospecting, Hats-warm, Retarget, RT-W) + 1 test. Review budget per set vs 50/week math every Monday.
5. Scale only a winner: +20% per 72h; never duplicate to "scale".
6. Judge on Shopify orders by utm_content and COD refusal rate.
Unknowns we must measure ourselves: (a) does one-ad-per-cell test starve at 250/day? (b) does consolidating RT-W into Retarget help? Test on our own account.
