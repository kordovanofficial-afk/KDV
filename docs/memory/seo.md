# SEO history: GSC, blog, collections, product data, Merchant Center, backlinks

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

## 🗺 SEO MASTER PLAN (user-confirmed Jul 15 2026 — three phases, in order)
1. **Phase 1 — user cleans Shopify catalog** (trash-scrape, manual; see PARKED
   section below for the re-audit checklist when done: counts, kdv- collections,
   redirects for removed URLs, fresh alt audit).
2. **Phase 2 — in-session SEO enrichment of surviving products (together):**
   priority from GSC data — wallets first (mens-leather-wallets pos 10.2 /
   14.5k impr = biggest prize), then cowboy hats (easy #1s), then jackets (fix
   1.9% CTR titles/metas). Per product: title+meta, bulk pattern-based alt-text
   backfill via API, description in brand voice, PDP metafields (subtitle/
   benefits/material/fits/reviews). Per collection: editorial block + JSON-LD.
3. **Phase 3 — automation for FUTURE products (only after 2 proves the pattern):**
   free stack = Shopify custom app (user creates in admin, 5 steps, gives API
   token) + webhook → Cloudflare Worker + Workers AI free tier (~10k neurons/day).
   (a) auto-alt on product create/update (deterministic title/variant pattern +
   vision assist, idempotent, never overwrites existing alts); (b) descriptions
   NEVER auto-published — draft to metafield + `needs-seo-review` tag, human
   approves; (c) nightly self-heal sweep. Worker can query our GSC connector for
   real keywords per product.
- **Alt audit baseline (Jul 15 2026, pre-trim):** 169 live products (192 active,
  357 total), 1,316 images, **630 missing alt (47.9%)** across 80 products;
  worst: Bella Duff 62/63, Diana Cross-body 46/47, TP bags ~26 each. Pattern:
  first images have alts, extra variant/angle shots don't. Detail file
  `alt_audit.jsonl` in scratchpad (session-local; re-export post-trim).

## 🔗 GSC coverage audit + redirect repair (Sep 6 2026 — DONE, do not redo)
Source: user's GSC "All known pages" coverage export (Jun 8 – Sep 4 2026), cross-referenced
against the live catalogue and the live `urlRedirects` list.
- **Indexing is HEALTHY and FLAT — stop worrying about it.** 261 indexed, range 254–277 all
  quarter, no trend. Impressions 2,623/day (Jun) → 2,245 (Aug) → 2,335 (Sep): that is the
  already-closed theme-migration dip recovering. ⚠️ Do NOT re-raise it as a new alarm.
- **1,355 "not indexed" is almost entirely correct behaviour**, not a defect:
  Crawled-not-indexed 341 (tag-filter URLs) · robots.txt 319 (**Shopify defaults — cart,
  checkout, account, sort params; correct, never "fix"**) · 404 256 · alternate-canonical 199
  (**working as designed**) · noindex 124 · has-redirect 99 (**success, not a problem**) ·
  soft-404 1 · dup-no-canonical 1 · discovered 15.
- 🔴 **THE JULY CATALOGUE TRIM DID NOT COST TRAFFIC — measured, settled.** Of 332 URLs with
  impressions in the window, only **25 were dead, totalling 402 impressions and 18 clicks**
  against 251,000 site-wide. Do not re-litigate the trim.
- 🔴 **THE REAL DEFECT, invisible in the coverage report: 22 of the 84 redirects pointed at
  products deleted in the trim** — a redirect into a 404, which is worse than a plain 404
  (crawler takes a hop and dies, link equity lost, customer sees a broken shop).
  ✅ All 22 retargeted, ✅ 25 new redirects added for the dead URLs that still earn
  impressions, ✅ 2 two-hop chains collapsed
  (`kordovan-combo-…-brown` and `natural-milled-premium-laptop-bag-brown`).
  **111 redirects now live, 0 pointing at a dead page, 0 chains** — re-verified after writing.
- ✍️ **Rule for future trims: deleting a product is not finished until you check what
  redirects at it.** Shopify will happily keep a redirect aimed at a deleted handle and the
  coverage report will never tell you.
- ✍️ Redirect to the nearest **equivalent product**; fall back to the category collection only
  when none exists. **Never mass-redirect to the homepage** — Google treats that as a soft 404
  and drops the signal entirely.
- 📌 `/collections/all/<tag>` URLs are LIVE Shopify tag pages, not 404s. 20 of them carry
  traffic (1,614 impressions / 29 clicks). **Do not "tidy" or noindex them without reading
  the next bullet first.**

### 🔎 The tag pages are BRAND SITELINKS, not category rankings (measured Sep 6 2026)
⚠️ **Correction to an earlier read in this same session.** `/collections/all/genuine-leather-products`
(1,157 impr) looked like an untapped category page worth optimising. It is not. Pulling the
`["page","query"]` breakdown shows **100% of its impressions are brand searches** — "kordovan
leather" 898, "kordovan" 215, "kordovan leather pakistan" 41 — **all at position 1.0**.
Across all 20 tag URLs, **86% of traffic is brand**. Lesson: never judge a page from
impressions alone; pull the query breakdown before calling something an opportunity.
- **What is really happening:** Google shows the homepage plus ~6 SITELINKS for "kordovan
  leather" (7,804 impr / 977 clicks a quarter). Each sitelink logs its own impression at
  position 1. Current slots: `/` (68% CTR, 822 clicks) · `/collections/women` ·
  `mens-leather-jackets` · `leather-bags` · `mens-leather-wallets` ·
  **`/collections/all/genuine-leather-products`** · `womens-leather-handbags` · `/collections/men`.
- 🚫 **Low sitelink CTR is NORMAL — it is not lost traffic.** The main result takes the clicks
  (homepage 68%); sitelinks run 0.3–5.9%. Do not "fix" a sitelink's CTR.
- **The actual cost is a wasted shelf slot**: one of six sitelinks pointed at a tag dump whose
  title rendered as `Products – tagged "genuine-leather-products"` — a raw slug in the brand SERP.
- ⚠️ **Sitelinks cannot be set or demoted.** Google retired the demotion tool in 2016. You only
  influence them through site structure, internal linking and how the page presents.
- ✅ **FIXED Sep 6 2026 in the theme, not by building a new collection.** `layout/theme.liquid`
  and `sections/main-collection.liquid` now derive a human `tag_label` from `current_tags`
  (`genuine-leather-products` → `Genuine Leather Products`) and use it for `<title>`, meta
  description, og:title/description, breadcrumb, H1, the editorial H2 and the JSON-LD `name`.
  JSON-LD `url` switched from `collection.url` (which drops the tag) to `request.path`.
  **One change fixes all 20 tag URLs at once, adds no new pages and cannot break a working one.**
  ⚠️ `tag_label` is captured separately in each file on purpose — Shopify sections have
  isolated scope, so a layout variable is not visible inside a section.
- 📌 The tag is real: `genuine-leather-products` covers **54 of 175 active products**, and it is
  **not linked from any nav menu or from the theme** — an orphan URL Google latched onto.
- 🔮 If the slot is ever wanted for something better, the lever is internal linking (give the
  target collection more prominent links), not a redirect — a 301 off a sitelink usually makes
  Google drop the slot rather than move it.
- Working data: scratchpad `gsc/` (session-local — rebuild from a fresh coverage export plus
  `gsc_query` on `["page"]`, diffed against live product/collection/page/article handles).

## ✍️ BLOG / CONTENT SEO (audited + 4 articles published Sep 6 2026)
🔴 **ONE ARTICLE WAS 98.6% OF ALL BLOG TRAFFIC.** `top-10-leather-jacket-brands-in-pakistan`
= 10,235 impr / 463 clicks in Jun 8–Sep 4. **Eight of the other nine articles earned ZERO
clicks** in the same quarter. Nothing had been published since 24 Sep 2024.
- **THE PATTERN THAT WORKS — copy it, do not invent a new one:** *"Top 10 / Best [category]
  Brands in Pakistan"*, with prices, **kept updated** (the winner is dated 2024 but titled
  "(2026)" because it was refreshed). It pulls **458 distinct queries** and ranks #1.9–2.2 for
  its exact title while sitting page-2 on the head terms.
- 🚫 **"How to choose…" guides DO NOT rank for this site.** Two exist; 3 impressions combined.
  Stop writing them. Seasonal sale posts (Azadi/Defence Day 2024) are dead weight — unpublish.
- 🔴 **The killer signal:** Google was serving the *jacket* article at **pos 1.0–2.0 for WALLET
  queries** ("best leather wallets in pakistan" 303 impr pos 2.0) because nothing better existed
  on the site. Wallets are the biggest non-brand category at **30,036 impressions**.
- ✅ **PUBLISHED Sep 6 2026 — 4 new articles, all live, all following the proven structure**
  (JSON-LD `@graph` BlogPosting + FAQPage · "we are on this list" disclosure box · comparison
  table · **price-floor section** · how-to-check-it-yourself · ranked brands each with a
  "Watch out for" · own brand last with an honest "where we are the wrong choice" · FAQ
  matching the schema · bottom line · CTA):
  | `/blogs/wallets/top-10-leather-wallet-brands-in-pakistan` | 598914957552 |
  | `/blogs/jackets/best-winter-jackets-in-pakistan` | 598914990320 |
  | `/blogs/news/top-leather-brands-in-pakistan` | 598915023088 (the HUB — links to all) |
  | `/blogs/bags/best-leather-laptop-and-office-bags-in-pakistan` | 598915055856 |
  - New blog created: **`bags`** `gid://shopify/Blog/108932333808`.
  - Blog IDs: news `50629607613` · sale `94658658544` · wallets `94807032048` ·
    jackets `95231803632` · handbags `95392792816` · shoes `95393775856` · bags `108932333808`.
- ✍️ **RULES FOLLOWED — keep them on any future article:**
  - 🚫 **NEVER publish exact competitor prices.** Use bands (Entry / Mid / Premium) and say why:
    "they change weekly and a stale number is worse than none." Protects accuracy and ages well.
  - 🚫 **No invented reviews, ratings or testimonials** (standing rule).
  - Competitor notes stay to **verifiable, neutral observations** (range breadth, retail
    footprint, price positioning) — never quality accusations we cannot support.
  - Brands were **verified by web search first**, not recalled: Jafferjees, Hub, Jild Craft,
    House of Leather, Blackbird Leathers, Uniworth, Karar, Eligo, Outfitters, Breakout, Cougar,
    Bonanza Satrangi, Diners, Charcoal, English Boot House, Servis/ECS.
  - Real catalogue prices used, not guesses: wallets **Rs 1,499–6,500** (23 products), laptop
    bags **Rs 8,500–42,000** (19), jackets Rs 22,000–35,000.
  - Images are **real Shopify CDN product photos** + the existing `blog-jackets-*` set.
- 📌 **HIGHEST-VALUE REMAINING ACTION (not yet done):** add internal links **from** the jacket
  article **to** the four new ones. It holds all the blog's authority and currently links to
  none of them. ⚠️ Requires re-sending its full ~23KB body via `articleUpdate` — Shopify has no
  partial body update — so do it carefully and verify afterwards; it is the page that earns
  98.6% of blog clicks.
- 📌 Second-highest: the winner sits at **pos 10.1 / 10.7** on "leather jackets in pakistan"
  (1,068 impr) and "leather jacket pakistan" (1,025). Pushing those to page 1 is likely worth
  more than another new article. **Refresh the winner before writing more.**
- ✅ **Internal links DONE Sep 6 2026.** The jacket article now links to all four new guides
  (a box near the top + a footer line, each URL x2), and `dateModified` bumped to 2026-09-06.
  🛡️ **Technique worth reusing for any large body edit — Shopify has no partial body update:**
  query the live body so it auto-saves to a tool-result file → apply insertions in Python with
  exact-match assertions → assert **0 lines removed** → publish → re-query and diff the live
  result against the intended file. Live differed by 6 lines, all Shopify's sanitiser adding a
  newline after `<li>`; all 18 structural markers matched. Backup kept at
  scratchpad `blog/jacket_ORIGINAL.html`.
- 📅 **Indexing requested in GSC for all 5 URLs on Sep 6 2026** (4 new + the updated jacket
  article). **That is the clock start.** Expect a first crawl within days, a first read on
  rankings in 2–4 weeks, meaningful movement in 6–12.
- Blog was **9.1% of site impressions / 6.4% of clicks** before this pass — the baseline to
  measure against. Re-pull `["page"]` and `["page","query"]` in early October and compare.

## 🔍 ORGANIC CHECK (Oct 26 2026, GSC Sep 27–Oct 24 vs prior 4 wks) — report `https://claude.ai/artifact/9rPzA2tK9PpB1MjvzfVg8i`
- Google search = **34 orders / Rs 158,794 in 30d** (beats FB+IG's 42 / 122,446, at zero cost). Non-brand clicks **+49%**
  (2,139→3,187), impressions +59%. Brand flat (~840 clicks).
- Search-landing conversion: wallets **1.36%**, caps **1.79%** (earners) · jackets collection 1,047 visits / **0 orders** ·
  4 bag collections ~600 visits / **0 orders** (on-page trust problem, not ranking).
- **#1 prize: "wallet for men" 7,028 impr @ pos 7.1, CTR 0.36%** → mens-leather-wallets. Proposed (humanized, NOT yet
  applied, needs user OK) new SEO title/desc for wallets, leather-bags (desc is NULL), mens-leather-shoes, homepage meta.
- Jacket blog article out-ranks the jacket collection on "leather jacket pakistan" (4,215 impr) → add shop CTA in article,
  but only after jacket checkout is fixed.

## 👛 WALLETS → 15/DAY FROM SEO (started Oct 26 2026, user goal)
- **Baseline (30d):** wallets sell ~2.2/day ALL channels (≈67 units); **Google search = 20 wallet orders/30d ≈ 0.7/day.**
  Wallet collection funnel (search+all, ~220 sessions/wk → ~12 ATC → ~9 checkout → ~3.5 orders); checkout completion
  ~38%, unchanged before/after the Sep 15 COD fee (store-wide completion drop 60%→32% is mostly jackets, not wallets).
- **Demand ceiling (GSC, 4 wks):** all non-brand wallet queries = **21,906 impr / 667 clicks** across 1,229 queries.
  Even #1 everywhere (~25% CTR) ≈ 5,500 clicks → 75 orders/mo at 1.36% CR (2.5/day), ~165/mo at 3% CR (5.5/day).
  ➡️ **15/day is NOT reachable from wallet web search alone** — needs Google Shopping free listings + AI Overviews +
  gift intent on top. Said so to the user; do not promise 15/day from rankings.
- **Live SERP (mobile, PK, Oct 26 via Apify):** HUB #1 on all 4 head terms (title just "Men Leather Wallet"); Jafferjees,
  Daraz, Metro, Waldor, Borjan, Zellbury, Sage, Uniworth fill the rest. Kordovan #4 "leather wallet", #6 "leather wallet
  for men", not top-8 for "wallet for men"/"wallets for men". **Google showed our HERO `descriptionHtml` as the snippet,
  not the SEO description.** Kordovan is ABSENT from both AI Overviews (they cite HUB, Jafferjees, Karar, Uniworth, Sage,
  Zellbury, Outfitters, Logo).
- ✅ **APPLIED LIVE Oct 26:** `mens-leather-wallets` SEO title "Wallets for Men in Pakistan: Genuine Leather from Rs 1,499 |
  Kordovan", new SEO description, new hero `descriptionHtml` (price + COD + warranty, query-led), **sortOrder
  CREATED_DESC → BEST_SELLING**. Wallet blog article already links to the collection 3x (no change needed).
- ✅ **26 WALLET PRODUCT TITLES RENAMED LIVE Oct 26 (user-approved)** to the jacket pattern `Name | Men's <material>
  <type> Wallet` (22 in mens-leather-wallets + Razor, Kodo Vertical 2.0, KODO, Illusion). 0 userErrors. Handles and SEO
  titles unchanged → no URL breaks. Facts only from `custom.material` / existing SEO titles. Feeds Google Shopping + Meta
  catalogue on their next daily sync. Theme has no title-dependent logic (only a testimonial label "Mocha Mate Wallet").
  User declined adding fit details (notes/CNIC/card counts) — do not re-ask.
- 🤖 **AI Overviews (Oct 26 SERP check):** Kordovan IS cited on brand-list queries — #1 in "top 10 wallet brands in
  pakistan", #2 "best wallet brands…", #3 "best leather wallet brands…", #4 "original leather wallet in pakistan" (links
  the collection). The AIO even cites our wallet blog article as its source for other brands. ABSENT on purchase queries
  ("leather wallet for men", "wallets for men"), where AIO lists named models + prices (HUB, Jafferjees, Karar).
  AIO still says "workshop in Karachi" from cached old text — will age out.
- 🔴 **Stock gaps on the page:** SOLD OUT = Elite Card Holder (5.0★, 38 reviews), Armour, Kingsman, Truckkr, Crazy Horse
  Long; Midtown Lite 3 units + Sheppard 2 (the Rs 1,499 entry wallets). Gator is DRAFT.

## 🛒 PAGE-2 COLLECTION PASS (Sep 8 2026 — 13 collections rewritten LIVE, done)
User: *"yes lets do the page 2 collections"*. Target = the collection pages sitting at
position 6–20 on non-brand queries, i.e. **33,721 trapped impressions** across the top 12 pages.
All changes are **live Shopify content, NOT theme** — no push was needed and none was made.
- **Trapped demand (non-brand, pos 6–20, Jun 8–Sep 4):** `mens-leather-wallets` 15,460 impr ·
  `/` 4,890 (ranks for "leather bags" 3,023 @ 7.1) · `mens-leather-jackets` 4,394 ·
  `smart-wallets` 1,874 · `leather-bags` 1,416 · `travel-bags` 1,404 ·
  `womens-leather-handbags` 940 · `leather-caps` 690 · `laptop-bags` 447 · `office-bags` 358.
- 🔴 **FIVE COLLECTIONS HAD COMPLETELY EMPTY `descriptionHtml` AND NO EDITORIAL** — they were
  rendering the theme's generic fallback and had no unique content at all: `travel-bags`,
  `womens-leather-handbags`, `leather-caps`, `laptop-bags`, `office-bags`. All five now have
  a unique description, a query-led SEO title and a full `custom.editorial` block.
  **`womens-leather-jackets` was empty too** and got the same treatment.
- 🔴 **LIVE CONTRADICTION FOUND AND FIXED: all 4 jacket collections' `custom.editorial`
  metafields still said "book with 50%, and pay the balance to the rider"** — the DEAD Aug 20
  rule — while the `descriptionHtml` on the same page said "paid in full online at checkout".
  ⚠️ **Why the Sep 4 pass missed it: it updated `descriptionHtml` only.** The editorial block
  is a SEPARATE metafield that renders below the product grid, so the page argued with itself.
  ✍️ **Rule: a collection has TWO content surfaces — `descriptionHtml` (hero) and
  `custom.editorial` (below the grid). Changing terms means changing BOTH.** Both now also
  carry the "about three weeks" lead time, which they previously lacked entirely.
- 📌 `custom.editorial` on Collection is **`multi_line_text_field`** (HTML stored as a string).
  Other COLLECTION `custom` defs: `banner_image`/`mobile_banner_image` (file_reference),
  `description` (rich_text_field).
- 🎯 **THE BIG UNSERVED INTENT: "price in pakistan" queries, ~2,500 impressions, answered by
  nothing on the site.** "leather wallet price in pakistan" 561 @ 5.7 · "briefcase price in
  pakistan" 491 @ 8.5 · "leather jacket price in pakistan" 534 @ 6.3 · "original leather jacket
  price…" 303 @ 3.7 · "genuine leather wallet price…" 333 · plus long tail. **Added an honest
  price-band section** (PU / split / full-grain / imported) to wallets, jackets, office bags,
  laptop bags and smart wallets, using REAL catalogue floors and ceilings:
  | wallets **1,499–6,500** (23) · smart wallets **1,800–3,200** (6) · caps **1,950–2,550** (4) |
  | jackets **22,000–35,000** (28) · handbags **6,000–19,500** (7) · laptop **12,000–42,000** (19) |
  | office **17,600–42,000** (6) · travel **29,000–45,000** (6) |
  🚫 Still no exact competitor prices — bands only, per the standing blog rule.
- ✅ **`leather-bags` had NO SEO title at all** (fell back to "All Bags") while ranking 6.8 for
  "leather laptop bags" (871 impr) and 6.5 for "office bag" (584). Now titled and rebuilt as a
  **hub** linking down to laptop / office / travel / women's with price ranges — leather-bags
  outranks the specific collections for their own queries, so the fix is structure, not a fight.
- ✅ `smart-wallets` title now leads with the actual query ("Smart Wallet for Men in Pakistan")
  — it ranks 15.5 for that term (974 impr) and the old title buried it behind "RFID Leather".
- ✅ **Fixed a factual error live:** `leather-bags` SEO description said "Free delivery over
  PKR 3,000". Real threshold is **PKR 5,500**. Every page written in this pass states 5,500.
- ⚠️ **GOTCHA — GraphQL block strings (`"""`) take backslashes LITERALLY.** Writing `15.6\"`
  inside one stored a literal backslash and it rendered on the page. Use plain `"` (fine unless
  three in a row) or reword ("15.6-inch"). Caught on `laptop-bags` and rewritten; **always
  re-query a block-string write and read the value back.**
- ⚠️ **`gsc_query`'s `dimensionFilterGroups` is IGNORED by our Worker** — a page-filtered query
  returns site-wide rows. Pull `["page","query"]` unfiltered and filter locally instead.
- 📌 Collections are THIN and that caps the ceiling: caps 4 products · office 6 · travel 6 ·
  smart 6 · handbags 7. Content is now good; **breadth is the next lever there**, not more words.
- 📅 Written Sep 8 2026. Google needs 2–6 weeks. Re-pull `["page","query"]` in mid-October and
  compare position on: "leather wallet for men" (6.74), "smart wallet for men" (15.5),
  "briefcase price in pakistan" (8.54), "leather bags for women" (16.4), "travel bag" (11.1).

## 🧱 PRODUCT-DATA COMPLETION PASS (Sep 8 2026 — catalogue-wide, DONE, do not redo)
User instruction: *"do the alt text backfill first, then the SEO Desctiption then the subtitile/
benefits and material thing, fix the product taxonomy."* All done and verified on 175 active products.
| Field | Before | After |
|---|---|---|
| Image alt text | **545 of 1,282 missing (42.5%)** | **0 missing (100%)** |
| SEO title | 47 missing | **0** |
| SEO description | 48 missing | **0** |
| `custom.subtitle` | 115 missing | **0** |
| `custom.benefits` | 115 missing | **0** |
| `custom.material` | 115 missing | **0** |
| Blank `productType` | 22 | **0** (43 distinct → 33) |
- **ALT TEXT — the method that worked, reuse it.** Shopify image **filenames carry real signal**
  (`Baseball_cap_by_kordovan_white_front.jpg` → colour *white* + angle *front*). Parse the filename
  (strip UUIDs/hex first), match colour and angle word-lists, and fall back to
  `"{title} — genuine {category} by Kordovan, view N"` so **every alt is unique** (545/545 unique).
  Write with **`fileUpdate(files:[{id, alt}])`** — up to ~110 per call, 6 calls did the lot.
  ⚠️ Anchor every regex with `\b` — an unanchored `croc` matched inside other words.
- 🔴 **ACCURACY RULES LEARNED HERE — apply to any future bulk copy job:**
  - ⚠️ **`The Diva Tote // Vegan` and `The Vibe // LITE // Vegan` are VEGAN, not leather.** Never let
    a template call them "genuine leather". Check `vegan|faux|synthetic` in the title first.
  - ⚠️ **Never assert a feature you cannot verify** (a mirror, a lining, a buckle metal, a locking
    handle). Benefits are now **brand-universal facts + one category-entailed line only**.
  - ⚠️ **`The Stallion // Premium Leather Boot`'s own description says "1 YEAR WARRANTY"**, so its
    benefits deliberately carry **no warranty line** — everything else says lifetime. Do not "fix".
  - Material was **extracted from each product's own description**, never invented; 49 distinct
    values. Where the description gave no signal, the honest fallback is plain `Genuine leather`.
- 🔴 **GOTCHA — `seo:` is a FULL REPLACE, not a merge.** Passing `seo:{description:...}` with no
  `title` **wiped that product's existing SEO title** (caught on `mini-crossbody-bag-small-messenger-bag`
  and repaired). **Always send title AND description together.**
- 🔴 **TAXONOMY — two collections filter on `productType`, so normalising it is NOT free:**
  `leather-backpacks` (TYPE = **`backpack`**, lowercase) and `crossbody-messenger-bags`
  (TYPE = **`Crossbody Bag`**). Both were left EXACTLY as-is. **`Leather Jacket` is also protected** —
  the theme's MTO rule is `type contains 'Jacket'`. Verified after the change: backpacks 6→**8**
  (two blanks correctly joined it), crossbody 6→6, jackets 28→28, shoes 24→24. **Nothing dropped.**
  ✍️ Before touching `productType` again, re-read `collections{ruleSet{rules{column}}}` for `TYPE` rules.
- ⚠️ **~29 aliased `productUpdate` calls per request is the safe ceiling** — 72 aliases returned a
  transient `upstream_error`; 36 and 29 both succeeded. Split and retry rather than assuming failure.
- ✅ **BODY DESCRIPTIONS CLOSED Sep 9 2026 — 0 of 175 active products now have an empty or stub
  description** (verified: no product with images has a description under 50 chars). The last 5
  were `croc-textured-shaded-belt`, `snake-leather-belt`, `tp-the-gentlemans-duffle`,
  `the-city-backpack-by-kordovan-rustic-red`, `bull-rider-calf-leather-belt`.
  - ⚠️ **The croc and snake belts are TEXTURED, not exotic skin.** The pattern is embossed into
    genuine hide. The copy says so explicitly — never let a future pass imply real crocodile or
    snake, which would be a false material claim on a product page and in the Google feed.
  - ✍️ **Only verifiable facts were used:** the material already in `custom.material`, the real
    colour options (duffle Tan/Brown, Bull Rider Black/Brown), real prices, and the two
    brand-universal facts already rendered site-wide in `layout/theme.liquid:23` — **"Karachi
    workshop"** and **"lifetime craftsmanship warranty"**. Check that line before asserting either.
  - 📌 **These 5 are NOT made-to-order** (only the 30 jackets + 24 footwear are), so the copy
    correctly says **cash on delivery is available**. Do not blanket-apply the jacket payment rule.
  - 📌 The three belts (2,800 / 3,500) sit BELOW the Rs 5,500 free-delivery threshold, so they
    state the threshold as policy rather than promising free delivery. Do not "simplify" that.
- 📌 **12 active products have NO IMAGES AT ALL** (invisible in search, ads and catalogue):
  `tp-the-city-backpack`, `zimmer-leather-keychain`, `tp-executive-a4-folder`,
  `tp-voyager-suitcase-trolley-bag-1`, `leather-lanyard`, `the-masters-leather-laptop-bag`,
  `the-braided-belt`, `four-in-one-leather-gift-set`, `tp-branson-briefcase-business-attache`,
  `gift-box-4-pieces-set`, `mini-card-cash-carry`, `luxe-card-lite`. **Photography is the fix.**

### 🔴 ALL 30 JACKETS CARRIED THE DEAD "4–7 DAYS" LEAD TIME (found + fixed Sep 8 2026)
`custom.fits` on every one of the 30 jackets still read
`S–3XL|Every size, made to order / 4–7 days|Cut and stitched for you / 3–4 days|Delivered to your door`
— and that block **renders on the PDP**, contradicting the "about 3 weeks" promise the Sep 6 pass put
everywhere else. Now reads `S–3XL|… / About 3 weeks|From checkout to your door / Paid online|Card,
debit card or JazzCash`. Verified **0 of 30 stale**.
- ✍️ **This is the SECOND surface the Sep 6 lead-time pass missed** (the first was the four jacket
  collections' `custom.editorial`, fixed Sep 8 too). **A product has many content surfaces:
  `descriptionHtml`, `seo`, and EACH metafield. Changing a fact means sweeping all of them** —
  grep the live values, do not trust a previous "done" note.

### 🔴 THIRD SURFACE — ALL 30 JACKET **SEO DESCRIPTIONS** STILL SAID "4–7 DAYS" (fixed Sep 15 2026)
Found while acting on a Google Merchant Center recommendation. **`seo.description` was never touched
by the Sep 6 lead-time pass or the Sep 8 sweeps** — both looked at `descriptionHtml` and metafields.
All **30 of 30** read `… Ready in 4–7 days, delivered in 3–4.` Now `… About 3 weeks to your door.`
- 🔴 **WHY THIS ONE WAS THE WORST: `seo.description` IS THE FIELD GOOGLE MERCHANT CENTER PUBLISHES.**
  Proven, not assumed — the description text in the user's Merchant Center screenshot matches
  `seo.description` verbatim ("The Ace: black bomber jacket in p…"), NOT `descriptionHtml`. So the
  dead 4–7 day promise was live in Google Shopping on 30 made-to-order items at Rs 22,000–35,000,
  paid 100% up front, entering peak season. ⚠️ **Any future fact change must sweep `seo.description`
  — it is the highest-exposure surface on the store, not a minor metadata field.**
- ✅ **Verified after writing: 0 of 175 active products carry `4–7 days` anywhere in SEO title or
  description; 30/30 jackets say "About 3 weeks"; 0 jackets lost their SEO title.** Also confirmed
  0 occurrences of the dead "50% deposit" wording catalogue-wide.
- ⚙️ Method: generated the 30 rewrites in Python by regex-replacing only the lead-time sentence,
  asserting each result still contains the colour word and is ≤165 chars, then emitted the GraphQL.
  **Never hand-retype 30 descriptions** — 2 batches of 15 aliased `productUpdate`, 0 userErrors.
  🔴 `seo:` is a FULL REPLACE — every call sent `title` AND `description`. Verified no title wiped.

### 🛍 WHAT MERCHANT CENTER'S "ADD COLOR / PATTERN" RECOMMENDATION ACTUALLY MEANS
User sent the "Update product descriptions to include details customers are looking for" report
(Men's Coats & Jackets): Key details = *Material*, Add to description = *Color, Pattern*.
- 🚫 **It is NOT asking for more words. Do not stuff colour into the prose — it is already there.**
  Every one of the 30 jacket SEO descriptions already names its colour, and all 30 name the material.
  The gap is **structured feed attributes**, not text.
- 📌 **Measured state of the Shopify taxonomy metafields (namespace `shopify`) on jackets:**
  `color-pattern` set on **28 of 30** — missing only on `alison-black-womens-biker-jacket` and
  `bliss-maroon-leather-bomber-women-jacket`. Also set: `size`, `fabric`, `age-group`,
  `target-gender`, `neckline`, `sleeve-length-type`, `care-instructions`,
  `outerwear-clothing-features`. **There is NO `pattern` key** — the taxonomy category
  (`Bomber Jackets`, `Motorcycle Outerwear`, `Sport Jackets`, `Coats & Jackets`) does not expose one.
  All values are `list.metaobject_reference`, so writing them needs the metaobject GID, not a string.
- ⚠️ **THE REPORT IS READING STALE FEED DATA — check the date before acting on it again.** Proof:
  it showed `cobalt-mens-blue-leather-bomber-jacket` with description "Shop Kordovan's Cobalt blue
  leath…", copy that no longer exists in Shopify. The feed syncs ~once daily. Since all 30 SEO
  descriptions changed on Sep 15, **wait 48h and re-pull Diagnostics before any further attribute
  work** — part of this recommendation may simply clear itself.
- 🚫 **DO NOT label these jackets "quilted" pattern.** "Quilted" appears in all 30 bodies but refers
  to the **lining** ("Quilted viscose lining"). Only two are genuinely quilted on the outside, and
  both say so in their titles: `rodriguez-…-quilted-…` (claret) and `nightfall-…-diamond-quilted-…`.
  A naive keyword match would have mislabelled 28 products.

### ✅ SHIPPING CLAIMS + FOOTWEAR DISCLOSURE FIXED IN SEO DESCRIPTIONS (Sep 15 2026, user: *"yes fix both"*)
Same session, immediately after the jacket lead-time fix. **72 products rewritten** (65 + 7 length trims).
- 🔴 **THE PROBLEM: 65 of 175 active products advertised unconditional free shipping to Google.**
  Phrasings found: `Free shipping nationwide.` ×41 · `Free shipping nationwide, lifetime warranty.` ×9
  · `Free shipping.` ×8 · `Free delivery.` ×3 · plus 4 one-offs. **Wrong twice over** — free delivery
  starts at **Rs 5,500**, and since Sep 15 **COD costs Rs 250 more**. All now read
  **"Free delivery over Rs 5,500"** (a policy statement, true at any cart value, so it is safe to
  apply uniformly without checking each product's price).
- 🔴 **AND 20 of the 24 footwear SEO descriptions disclosed neither made-to-order nor the lead time**,
  despite all 24 shoes being MTO — the same exposure the jackets had. All 24 now carry
  **"Made to order in our Karachi workshop — about 3 weeks to your door. Free delivery."**
  (every shoe is Rs 21,000+, comfortably over the threshold, so "Free delivery" is literally true).
- ✅ **Verified catalogue-wide after writing:** 0 unqualified free-shipping claims · 24/24 footwear
  disclose made-to-order AND "about 3 weeks" · 0 SEO titles or descriptions lost · 0 `4–7 days`
  anywhere · 0 descriptions over 165 chars.
- ⚠️ **`The Stallion // Premium Leather Boot` CONTRADICTS ITSELF ON MATERIAL — unresolved.**
  `custom.material` says **Croc-textured leather**; its old SEO description said **full-grain cowhide**.
  Both cannot be right. Its new SEO description deliberately asserts **neither material nor a warranty**
  (the warranty omission is the standing rule — its own body copy says "1 YEAR WARRANTY" while
  everything else says lifetime). **Ask the user which material is correct before writing either.**
- 📌 **14 products still say "nationwide" and that is CORRECT — do not "fix" them.** Nine say
  *"ships nationwide"* (true, PostEx delivers nationwide) and five say *"Cash on delivery nationwide"*
  (also true — those are cowboy hats and wallets, not made-to-order, so COD is genuinely available).
  ⚠️ Those five do not mention the new Rs 250 COD fee. Not false, but tighten if the fee is promoted.
- ✍️ **Length rule learned here: keep `seo.description` ≤ ~160 chars.** Swapping in the longer
  "Free delivery over Rs 5,500" pushed 7 products to 166–172, which Google would have truncated —
  cutting off the very shipping line the pass existed to correct. Trimmed by dropping filler
  ("by Kordovan", "Available in multiple colors"), never by dropping the shipping fact.

## 🛍 GOOGLE MERCHANT CENTER — LIVE, and free listings are already producing (Sep 8 2026)
⚠️ **DO NOT tell the user Merchant Center "needs setting up" — it exists and is working.**
Confirmed from the user's own dashboard screenshot.
- **Merchant Center ID `5365730451`**, account name "Kordovan", Comparison Shopping Service =
  **Google Shopping (google.com/shopping)**. Free listings active.
- **28-day performance: 4.27K total clicks (−6.5%), and Google's own summary says ORGANIC
  PRODUCT CLICKS are +15.9%.** The two move opposite ways because **all Google Ads campaigns
  are paused/removed**, so paid clicks are draining out of the total while organic grows.
- 🔴 **THE UNRESOLVED QUESTION — how big is this really?** Search Console shows only ~2,400
  web-search organic clicks/month. If a large share of that 4.27K is **free Shopping listings**,
  Shopping is one of the biggest organic channels in the business and **it has never appeared in
  any of our analysis, because GSC does not report Shopping surfaces.** ➡️ Get the free-vs-paid
  split from the "Click trend" / "View more" control on the Overview performance card before
  treating 4.27K as organic. Do not quote it as organic until that split is seen.
- 📌 **Open items visible on the dashboard:** (1) **1 notification**; (2) a banner (partly hidden)
  reading *"To finish your M… policy for your online store"* — almost certainly the **returns
  policy**, which Merchant Center requires and which can suppress free listings; (3) Google
  recommends adding a **business profile**. All three are free.
- ➡️ **Next diagnostic to request from the user: Products → Diagnostics** (item-level issues —
  missing GTIN/brand, image problems, price mismatches). With free listings already producing at
  this volume, anything suppressed there is direct lost revenue.
- 🔗 **The Sep 8 product-data pass feeds this directly.** Merchant Center categorises from the
  feed, and `product_type` is an input: it went from **22 blanks / 43 inconsistent labels → 0
  blanks / 33 clean types**, plus SEO title+description on all 175. Shopify pushes the feed
  roughly **once daily**, so expect Diagnostics to shift over 24–48h, not instantly.
- 💰 Consistent with the FREE-only rule: free listings cost nothing. Paid Shopping stays parked
  until October per the jacket season curve.

## 🏬 PARKED — Catalog trim before SEO (user doing manually)
User moved to own POS software (synced w/ Shopify). Is removing store-only / bogus /
irrelevant products from the ONLINE store so the online catalog = only what's sold
online. Cautions given: (1) UNPUBLISH from Online Store channel vs DELETE — deleting
may break POS sync / remove POS record; only hard-delete truly-dead SKUs. (2) Removed
products leave 404s → need URL redirects (build a bulk redirect list after). When user
returns: re-audit trimmed catalog (count remaining online products, verify 6 kdv-
smart collections still populate by tag, flag empty collections, set up redirects),
THEN start SEO enrichment on the clean set.

## 🔗 BACKLINK OUTREACH (Oct 29 2026) — `Kordovan_Backlink_Prospects.xlsx` (repo root)
- 🚫 No automated/paid link schemes (Google link-spam policy; organic search = 34 orders/Rs 1.59 lakh in 30d at zero cost).
- 🚫 OpenSEO (every-app/open-seo) declined: needs a paid DataForSEO key ($1 trial, $50 minimum top-up). User said leave it.
- Finding: few neutral "best leather brands in Pakistan" lists exist; our own 3 guide articles rank #1–2 and feed the AI
  Overview. Competitor lists (Karar, House of Leather, Trendevoker, Footlib) rank themselves #1.
- Priority 1: Karar's wallet comparison names Kordovan with WRONG facts (1-yr warranty, Rs 3,000–8,000, COD "some"),
  no link (draft D1) · ProPakistani 2022 jacket list (D2) · claim b2c.com.pk + peekaboo.guru listings (no website link).
- ✅ User confirmed Oct 29: Etsy "KordovanLeatherUS" (still LIVE), Amazon.ae and Daraz ("Kordvan") listings are OURS;
  Amazon + Daraz inactive. Not impersonation — do not re-raise.
- Skip: hutch.pk (sells "mirror copy" designer wallets), competitor lists, Reddit self-promo.
- ✅ **Oct 29: "Real vs Fake Leather: 8 Ways to Check" PUBLISHED** — `/blogs/news/real-vs-fake-leather-how-to-check`
  (article `599524737264`, blog news). Header = user's AI image `Leather_vs._Worn_Faux-Leather_Wallets.png` (stand-in;
  swap for a real shoot photo per `docs/images/IMAGE_BRIEF.md`). Source `docs/seo/blog/real-vs-fake-leather.html`.
  Request indexing in GSC; read rankings for "how to check real leather" / "rexine vs leather" in 4–8 weeks.

