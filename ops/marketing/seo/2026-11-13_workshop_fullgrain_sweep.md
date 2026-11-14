# Live-site wording sweep: "our workshop" + jacket "full-grain" (Nov 13–14 2026)

**Approvals:** Founder Nov 12 "yes do the sweep" (a SUPPLIER makes our products, so no "our workshop" / "our artisans" / "in-house" claims) and Founder Nov 9 (jackets are TOP-GRAIN sheepskin, never "full-grain").
**Store:** kordovan.myshopify.com (confirmed). Scope: 168 ACTIVE products, 64 collections, 16 blog articles. Prices, stock, tags, handles untouched.
**Replacement wording used:** "in Pakistan", "made in Pakistan", "by skilled leather artisans in Pakistan" (where "Pakistan" already appeared in the same SEO line, "by skilled leather artisans"). No city added. Malir Cantt references to the *workshop* were removed with the phrase; no new city named.

## Counts (all writes returned 0 userErrors)

| Surface | Field | Items changed |
|---|---|---|
| Products (30 jackets) | descriptionHtml | 30 |
| Products (other) | descriptionHtml | 6 (croc belt, snake belt, gentleman's duffle, city backpack rustic red, bull rider belt, Tuxedo shoe) |
| Products | seo.description (title resent unchanged) | 36 (24 footwear + 12 belts/bags/accessories) |
| Products | custom.benefits | 109 |
| Products | custom.subtitle / fits_text / material | 0 (no hits; all jacket materials already top-grain) |
| Collections | descriptionHtml | 11 (incl. mens-leather-wallets, also removed dead kv2-gifting sentence) |
| Collections | seo.description (title resent) | 7 |
| Collections | custom.editorial | 5 (laptop-bags, leather-bags, biker, bomber, black jackets) |
| Articles | body (+ summary where hit) | 7 articles (3 summaries) |
| Articles | SEO description (global.description_tag) | 0 (no hits) |
| **Total live field writes** | | **≈ 212** |

**Read-back (Nov 14):** every changed field re-read live and diffed against the intended value: **0 mismatches**. Re-ran the grep over all 168 active products, 64 collections, 16 articles (body, summary, SEO, metafields): **0 remaining** "workshop / our artisans / our craftsmen / in-house / hand-cut by us" claims, **0** "full-grain" on any jacket product field. Only remaining "full-grain" on a jacket surface is the generic grade explainer in `mens-leather-jackets` editorial ("Full-grain keeps the whole outer surface; top-grain is lightly corrected…"), which correctly says the jackets are top-grain.

## Deliberately left (with reason)
- **"winter is our busiest season and the bench is full"** (30 jacket PDPs, jacket collection editorials, winter-jackets article): reason-pairing copy required by the MTO rule; "the bench" does not say whose. Flag for Founder if he wants it softened.
- **"Kordovan makes leather jackets / wallets / bags"**, "we make one kind of jacket", "See what we make": brand-level product-line wording, not a manufacturing-location claim. Left. Changed only "We make in batches" (→ "Stock arrives in batches").
- **"We repair these under warranty… from the repair bench"** (laptop-bags article): warranty-service claim, not a making claim.
- **"stitched by skilled artisans" / "handcrafted by skilled artisans" / "passionate craftsmen"** (Regal Weaver copy, Cindy, Stella, Saloon, Zulfiqar, Natural Grain belt): do not say *our*; already true wording.
- **"Hand-cut, hand-stitched, backed for life"** (Bronco wallet benefits) and "Hand-cut in Pakistan" (lanyard SEO): no ownership claim.
- **Generic grade advice** in jacket articles ("check for genuine, full grain or sheepskin", competitor "blend rather than full grain"): about buying in general, not a claim about our jackets.
- **Image file names** `blog-jackets-workshop.png` (CDN URLs) cannot be renamed via API; their ALT text was fixed. Note CLAUDE.md says no workshop footage exists, so these images are probably AI; worth reviewing.
- **"We have a single store in Malir Cantt"** (jacket article): store location, not a workshop claim; pre-existing; not touched (but Malir Cantt is in Karachi, check against the Karachi rule).
- **"It is also the jacket our customers have been most consistently happy with"** (Desert Voyager PDP): review-like claim, outside this sweep; check provenance.
- Pre-existing data issues noticed, not touched: Cindy Tote description is truncated mid-word ("Genuine top g"); discover-kordovan article summary starts with broken markup ("/strong&gt;").
- Shipping/Privacy policies: excluded (Founder edits those).

## Theme files: edited on `claude/hopeful-mccarthy-grntwn`, NOT deployed (needs Founder yes)
Commit `cd94b8e` "Theme: remove 'our workshop' claims (NOT deployed; needs Founder yes)". No JS touched.
- `snippets/our-craft.liquid`: hero alt (no "Kordovan workbench"), "doesn't leave our workshop" → "doesn't carry our name", "every decision in our workshop" → "every decision we make", "We work exclusively with full-grain…" → "We choose full-grain, top-grain and vegetable-tanned leathers", artisan image alt → "in Pakistan", "Decades of skill, in one workshop." → "Decades of skill, by hand.", "Our artisans…it's a workshop" → "The skilled leather artisans in Pakistan who make our pieces…it's handwork". (The page's 5-step process copy still describes hand process in first person-neutral terms; left.)
- `snippets/our-story.liquid`: hero alt → "Artisan hand-stitching leather in Pakistan"; "We work full-grain and vegetable-tanned hides — the highest grade" → "We choose full-grain, top-grain and vegetable-tanned hides — the highest grades".
- `snippets/pdp-main.liquid`: MTO shipping accordion "the workshop cuts and stitches it for you" → "skilled leather artisans in Pakistan cut and stitch it for you"; fallback bullet (only when no benefits metafield) "Full-grain leather…" → "Genuine leather…".
- `sections/main-search.liquid`: "Every result is genuine full-grain leather, hand-stitched in our own workshop" → "Every result is handcrafted in Pakistan".
- `layout/theme.liquid`: tag-page meta description "genuine full-grain leather, cut and hand-stitched in our own workshop" → "genuine leather, cut and hand-stitched in Pakistan".

## Change table (surface | field | before | after)

| Surface | Field | Before | After |
|---|---|---|---|
| product rebel-mens-brown-cafe-racer-sheepskin-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product hawkeye-mens-brown-double-breasted-vintage-coat-s012 | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product mens-urban-rider-brown-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product iconic-mens-black-sheepskin-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product mens-legender-black-black-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product mens-apex-black-plain-suede-bomber-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product mens-ace-black-leather-bomber-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product cobalt-mens-blue-leather-bomber-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product allaric-alley-distressed-brown-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product mens-spy-brown-leather-bomber-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product alison-black-womens-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product bliss-maroon-leather-bomber-women-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product stryker-mens-black-zippered-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product reacher-mens-black-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product wayne-mens-sheepskin-black-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product rockafella-mens-black-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product durham-waxed-mens-black-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product maverick-mens-brown-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product alveraz-mens-black-sheepskin-biker-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product rodriguez-mens-quilted-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product ralph-mens-dark-brown-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product bohemia-mens-vintage-brown-sheepskin-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product alonzo-mens-brown-sheepskin-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product vanguard-mens-black-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product marc-ed-mens-black-leather-biker-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product sheppard-mens-cafe-racer-black-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product waxed-rider-mens-brown-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product desert-voyager-mens-brown-sheepskin-leather-bomber-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product nightfall-mens-diamond-quilted-black-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product shadow-rider-mens-black-cafe-racer-leather-jacket | descriptionHtml | Every Kordovan jacket is cut and stitched after you order, in our own workshop. | …after you order, by skilled leather artisans in Pakistan. |
| product croc-textured-shaded-belt | descriptionHtml | Hand-cut and finished in our own workshop. | Hand-cut and finished by skilled leather artisans in Pakistan. |
| product snake-leather-belt | descriptionHtml | Hand-cut and finished in our workshop from a single strip of hide. | Hand-cut from a single strip of hide and finished by skilled leather artisans in Pakistan. |
| product tp-the-gentlemans-duffle | descriptionHtml | Hand-stitched in our own workshop. | Hand-stitched by skilled leather artisans in Pakistan. |
| product the-city-backpack-by-kordovan-rustic-red | descriptionHtml | Hand-cut and stitched in our own workshop, and covered by… | Hand-cut and stitched by skilled leather artisans in Pakistan, and covered by… |
| product bull-rider-calf-leather-belt | descriptionHtml | Hand-cut and finished in our workshop, with a lifetime… | Hand-cut and finished by skilled leather artisans in Pakistan, with a lifetime… |
| product the-tuxedo-premium-leather-shoe | descriptionHtml | Our in-house shoemakers can add one of the best leather soles… | The skilled shoemakers in Pakistan who make it can add one of the best leather soles… |
| product the-tuxedo-premium-leather-shoe | seo.description (title resent unchanged) | The Tuxedo handcrafted leather shoes for men, Rs 32,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Tuxedo handcrafted leather shoes for men, Rs 32,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-stallion-premium-leather-boot | seo.description (title resent unchanged) | The Stallion boot in croc-textured cow leather, Rs 24,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Stallion boot in croc-textured cow leather, Rs 24,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product tri-fold-premium-durable-belt | seo.description (title resent unchanged) | Genuine leather tri-fold belt for men, Rs 4,000. Hand-finished in our own workshop with a lifetime craftsmanship warranty. Cash on delivery available. | Genuine leather tri-fold belt for men, Rs 4,000. Hand-finished in Pakistan with a lifetime craftsmanship warranty. Cash on delivery available. |
| product copy-of-cardinal-blue-premium-oxford-brogue-wingtip-suede-genuine-leather-shoes | seo.description (title resent unchanged) | Premium Oxford leather shoes for men in brown, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Premium Oxford leather shoes for men in brown, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-regal-weaver | seo.description (title resent unchanged) | The Regal Weaver genuine leather dress shoes, Rs 24,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Regal Weaver genuine leather dress shoes, Rs 24,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-the-regal-weaver | seo.description (title resent unchanged) | The Aristocratic Strider genuine leather shoes, Rs 24,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Aristocratic Strider genuine leather shoes, Rs 24,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product executive-comfort-oxford | seo.description (title resent unchanged) | Executive Comfort Oxford genuine leather shoes, Rs 24,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Executive Comfort Oxford genuine leather shoes, Rs 24,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-executive-comfort-oxford | seo.description (title resent unchanged) | Enigma Burnished genuine leather loafers, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Enigma Burnished genuine leather loafers, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-enigma-burnished-loafers | seo.description (title resent unchanged) | The Luxe Tassel natural milled leather loafers, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Luxe Tassel natural milled leather loafers, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-saachi | seo.description (title resent unchanged) | The Saachi top-grain leather shoes, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Saachi top-grain leather shoes, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product soleil-oxfords | seo.description (title resent unchanged) | Soleil genuine leather Oxford shoes, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Soleil genuine leather Oxford shoes, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product imperial-moccasin | seo.description (title resent unchanged) | Imperial genuine leather moccasins, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Imperial genuine leather moccasins, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product slip-on-kordovan-oxford | seo.description (title resent unchanged) | Slip-On genuine leather Oxford shoes, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Slip-On genuine leather Oxford shoes, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product legacy-wholecut-wingtip | seo.description (title resent unchanged) | Legacy Wholecut Wingtip genuine leather dress shoes, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | Legacy Wholecut Wingtip genuine leather dress shoes, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-mock-croc-leather-dress-belt-black | seo.description (title resent unchanged) | The Saffire croc-textured genuine leather dress belt, Rs 4,400. Hand-finished in our workshop with a lifetime craftsmanship warranty. | The Saffire croc-textured genuine leather dress belt, Rs 4,400. Hand-finished in Pakistan with a lifetime craftsmanship warranty. |
| product copy-of-oxford-brogue-patent-black-limited-trot-series | seo.description (title resent unchanged) | The Salemanco Brogue in black, genuine leather, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Salemanco Brogue in black, genuine leather, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-salemanco-brogue-tan | seo.description (title resent unchanged) | The Salemanco Brogue in tan, genuine leather, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Salemanco Brogue in tan, genuine leather, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-salemanco-brogue-burnished-brown | seo.description (title resent unchanged) | The Salemanco Brogue in burnished brown, genuine leather, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Salemanco Brogue in burnished brown, genuine leather, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-the-salemanco-brogue-burnished-brown | seo.description (title resent unchanged) | The Salemanco Oxford, genuine leather, Rs 22,500. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Salemanco Oxford, genuine leather, Rs 22,500. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product the-tassel-shoe | seo.description (title resent unchanged) | The Tassel genuine leather shoes, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Tassel genuine leather shoes, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product copy-of-the-tassel-shoe | seo.description (title resent unchanged) | The Diplomat genuine leather dress shoes, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery. | The Diplomat genuine leather dress shoes, Rs 21,000. Made to order in Pakistan — about 3 weeks to your door. Free delivery. |
| product omega-ruboff-loafers | seo.description (title resent unchanged) | Omega Ruboff genuine leather loafers for men, Rs 11,400. Made to order in our own workshop — about 3 weeks from checkout to your door. | Omega Ruboff genuine leather loafers for men, Rs 11,400. Made to order in Pakistan — about 3 weeks from checkout to your door. |
| product lionel-loafer-mocassin | seo.description (title resent unchanged) | LIONEL black leather loafer moccasins, Rs 21,400. Made to order in our own workshop — about 3 weeks from checkout to your door. | LIONEL black leather loafer moccasins, Rs 21,400. Made to order in Pakistan — about 3 weeks from checkout to your door. |
| product croc-textured-shaded-belt | seo.description (title resent unchanged) | Croc-textured shaded genuine leather belt, Rs 3,500. Hand-finished in our workshop. Free delivery over Rs 5,500, cash on delivery available. | Croc-textured shaded genuine leather belt, Rs 3,500. Hand-finished in Pakistan. Free delivery over Rs 5,500, cash on delivery available. |
| product snake-leather-belt | seo.description (title resent unchanged) | Snake-textured genuine leather belt for men, Rs 3,500. Hand-finished in our own workshop with a lifetime craftsmanship warranty. | Snake-textured genuine leather belt for men, Rs 3,500. Hand-finished in Pakistan with a lifetime craftsmanship warranty. |
| product tp-dblp-laptop-bag | seo.description (title resent unchanged) | DBLP genuine leather laptop bag with a padded sleeve, Rs 18,500. Hand-stitched in our own workshop. Free delivery over Rs 5,500. | DBLP genuine leather laptop bag with a padded sleeve, Rs 18,500. Hand-stitched in Pakistan. Free delivery over Rs 5,500. |
| product buffalo-bob-leather-belt | seo.description (title resent unchanged) | Buffalo Bob genuine leather belt, Rs 2,800. Thick full-grain hide, hand-finished in our own workshop. Cash on delivery available. | Buffalo Bob genuine leather belt, Rs 2,800. Thick full-grain hide, hand-finished in Pakistan. Cash on delivery available. |
| product the-stella-tote-bag | seo.description (title resent unchanged) | The Stella genuine leather tote bag, Rs 19,500. Structured, roomy and hand-stitched in our own workshop. Free delivery over Rs 5,500. | The Stella genuine leather tote bag, Rs 19,500. Structured, roomy and hand-stitched in Pakistan. Free delivery over Rs 5,500. |
| product bull-rider-calf-leather-belt | seo.description (title resent unchanged) | Bull Rider calf leather belt, Rs 2,800. Hand-finished in our workshop with a lifetime craftsmanship warranty. Cash on delivery available. | Bull Rider calf leather belt, Rs 2,800. Hand-finished in Pakistan with a lifetime craftsmanship warranty. Cash on delivery available. |
| product the-vibe-lite-by-kordovan-vegan | seo.description (title resent unchanged) | The Vibe LITE vegan leather handbag, Rs 6,000. Animal-free construction, made in our own workshop. Free delivery over Rs 5,500. | The Vibe LITE vegan leather handbag, Rs 6,000. Animal-free construction, made in Pakistan. Free delivery over Rs 5,500. |
| product tp-the-city-backpack | seo.description (title resent unchanged) | The City genuine leather backpack, Rs 15,500. Padded laptop section, hand-stitched in our own workshop. Free delivery over Rs 5,500. | The City genuine leather backpack, Rs 15,500. Padded laptop section, hand-stitched in Pakistan. Free delivery over Rs 5,500. |
| product tp-natural-milled-leather-dopp-kit | seo.description (title resent unchanged) | Natural milled leather dopp kit, Rs 6,600. Wipe-clean lining, hand-stitched in our own workshop. Free delivery over Rs 5,500. | Natural milled leather dopp kit, Rs 6,600. Wipe-clean lining, hand-stitched in Pakistan. Free delivery over Rs 5,500. |
| product a4-handle-folio-bali | seo.description (title resent unchanged) | A4 leather folio with a carry handle, Rs 7,500. Holds documents flat, hand-stitched in our own workshop. | A4 leather folio with a carry handle, Rs 7,500. Holds documents flat, hand-stitched in Pakistan. |
| product zimmer-leather-keychain | seo.description (title resent unchanged) | Zimmer genuine leather keychain, Rs 500. Hand-cut in our own workshop — a small gift that lasts. | Zimmer genuine leather keychain, Rs 500. Hand-cut in Pakistan — a small gift that lasts. |
| product tp-voyager-suitcase-trolley-bag-1 | seo.description (title resent unchanged) | Voyager leather suitcase trolley bag, Rs 48,000. Built for repeat travel, hand-stitched in our own workshop. | Voyager leather suitcase trolley bag, Rs 48,000. Built for repeat travel, hand-stitched in Pakistan. |
| product bl-textured-backpack-black | seo.description (title resent unchanged) | Textured black genuine leather backpack, Rs 19,800. Padded laptop compartment, hand-stitched in our own workshop. | Textured black genuine leather backpack, Rs 19,800. Padded laptop compartment, hand-stitched in Pakistan. |
| product the-tuxedo-premium-leather-shoe | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-stallion-premium-leather-boot | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product premium-leather-lipstick-case-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product genuine-sheep-leather-adjustable-baseball-cap-unisex | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product double-pocket-extendable-travel-laptop-bag-natural-milld-leather-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-case-by-kordovan-vintage-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product natural-milled-leather-slim-laptop-bag-by-kordovan-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-kordovans-crushable-premium-genuine-leather-western-cowboy-hat-s012 | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product durable-mens-leather-gloves-black-kordovan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product durable-mens-leather-gloves-light-brown-kordovan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product durable-womens-leather-gloves-dark-red-kordovan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product mini-leather-folio-note-pad-organizer | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tri-fold-premium-durable-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product genuine-sheep-leather-flat-cap-newsboy-unisex | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-womens-casual-cap-newsboy-cap-beret-for-girl-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-diva-tote | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product natural-grain-double-stich-leather-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product premium-nappa-leather-reversible-belt-black-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-millennial-sleek-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product mens-solid-one-piece-leather-dress-casual-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-ripper-case-by-kordovan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product mini-crossbody-bag-small-messenger-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-executive-leather-briefcase-office-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-documate-office-bag-briefcase-with-code-lock | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovans-suede-premium-genuine-leather-western-cowboy-hat-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-executive-ceo-office-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product leather-tray-organizer | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-natural-oil-tanned-leather-casual-belt-rustic-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovans-premium-crazy-horse-leather-western-cowboy-hat | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-travel-mate-trolley-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-mens-leather-fanny-pack | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-the-travel-mate-trolley-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product mini-watch-cufflink-box | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-executive-leather-briefcase-office-bag-with-laptop-compartment-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-cardinal-blue-premium-oxford-brogue-wingtip-suede-genuine-leather-shoes | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovans-premium-oxford-leather-shoes-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product leather-key-chain-with-belt-loop | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-regal-weaver | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-the-regal-weaver | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product executive-comfort-oxford | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-executive-comfort-oxford | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-enigma-burnished-loafers | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-saachi | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product soleil-oxfords | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product imperial-moccasin | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product slip-on-kordovan-oxford | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product legacy-wholecut-wingtip | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovan-sleek-laptop-sleeves-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-kordovan-sleek-laptop-sleeves-tan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovan-sleek-laptop-sleeves-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-expedition-leather-passport-cover | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-beyond-backpack-unisex | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product leather-tissue-box-1 | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-mock-croc-leather-dress-belt-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-travel-mate-trolley-bag-brown-1 | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-maverik-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-oxford-brogue-patent-black-limited-trot-series | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-salemanco-brogue-tan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-salemanco-brogue-burnished-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-the-salemanco-brogue-burnished-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-tassel-shoe | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-the-tassel-shoe | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product vouge-jewellery-case | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product imperial-keychain | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product copy-of-kordovans-premium-leather-western-cowboy-hat-rustic-maroon | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovans-clifford-cowboy-hat-rustic-brown | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product breathable-sheep-leather-adjustable-baseball-cap-unisex | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-elite-passport-holder | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product omega-ruboff-loafers | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product linker-moccassin | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product lionel-loafer-mocassin | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product lionel-loafer-moccasin-tan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product kordovans-affordable-cowboy-hat | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product croc-textured-shaded-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product snake-leather-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-the-gentlemans-duffle | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-dblp-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-elite-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product sheffield-backpack-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-millard-office-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product buffalo-bob-leather-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product diana-cross-body-bag-pebbled-leather | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product diana-cross-body-bag-crazy-horse-leather | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product pinto-hair-on-duffle-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product bella-duff-mini-duffle-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-cindy-tote-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-stella-tote-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product hilford-backpack | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-city-backpack-by-kordovan-rustic-red | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product bull-rider-calf-leather-belt | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-vibe-lite-by-kordovan-vegan | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-forester-backpack-duffle-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-the-city-backpack | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-the-corporate-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-venture-pack | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-natural-milled-leather-dopp-kit | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-traveler-multi-function-crazy-horse-leather-duffle-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product a4-handle-folio-bali | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product gridle-crossbody | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-saloon-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product zulfiqar-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product zimmer-leather-keychain | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-executive-a4-folder | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-voyager-suitcase-trolley-bag-1 | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product rl-the-hilford-backpack | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product bl-textured-backpack-black | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product leather-lanyard | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product the-masters-leather-laptop-bag | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| product tp-branson-briefcase-business-attache | custom.benefits | Hand-cut and stitched in our own workshop | Hand-cut and stitched in Pakistan |
| collection smart-wallets | seo.description (title resent) | …eather card holders and pop-up wallets. Handmade in our own workshop, cash on delivery a | Handmade by skilled leather artisans |
| collection womens-leather-jackets | descriptionHtml | …<p>Leather jackets for women, made to order in our own workshop from semi-aniline sheep | made to order in Pakistan from |
| collection mens-leather-wallets | descriptionHtml | …l-grain, nappa and crazy horse leather, cut and stitched in our own workshop in Pakistan. Cash on delivery i | cut and stitched in Pakistan |
| collection womens-leather-handbags | descriptionHtml | …led, crazy horse and semi-aniline hide, hand-stitched in our own workshop.</p> | hand-stitched in Pakistan |
| collection womens-leather-handbags | seo.description (title resent) | …an. Totes, cross-body bags and clutches hand-stitched in our own workshop. Free delivery over | hand-stitched by skilled leather artisans |
| collection office-bags | seo.description (title resent) | …Pakistan. Structured, laptop-ready and hand-stitched in our own workshop. Free delivery over | hand-stitched by skilled leather artisans |
| collection laptop-bags | descriptionHtml | …d 15.6" — with padded sleeves, cut from full-grain hide in our own workshop.</p> | full-grain hide in Pakistan |
| collection laptop-bags | seo.description (title resent) | …stan, padded for 13-15.6 inch machines. Hand-stitched in our own workshop. Free delivery over | Hand-stitched by skilled leather artisans |
| collection laptop-bags | custom.editorial | …that price.</p>  <p>Full-grain leather, hand-stitched in our own workshop, with a lifetime cr | hand-stitched in Pakistan |
| collection travel-bags | descriptionHtml | …cabin trolleys, cut from full-grain and crazy horse hide in our own workshop — built for repeat | crazy horse hide in Pakistan |
| collection travel-bags | seo.description (title resent) | …duffles and cabin trolleys in Pakistan. Hand-stitched in our own workshop, lifetime warranty. | Hand-stitched by skilled leather artisans |
| collection leather-caps | descriptionHtml | …d flat newsboy caps in black and brown, made in our own workshop.</p> | made in Pakistan |
| collection leather-caps | seo.description (title resent) | …le baseball caps and flat newsboy caps, hand-finished in our own workshop. Cash on delivery a | hand-finished by skilled leather artisans |
| collection leather-bags | custom.editorial | …up. Everything on this page is cut and hand-stitched in our own workshop from full-grain and craz | hand-stitched in Pakistan from |
| collection cowboy-hats | descriptionHtml | …<p>Genuine leather cowboy hats, cut and shaped by hand in our own workshop. Crushable, suede a | shaped by hand in Pakistan |
| collection cowboy-hats | seo.description (title resent) | …enuine leather cowboy hats in Pakistan, handcrafted in our own workshop. Crushable, suede a | handcrafted by skilled leather artisans |
| collection mens-biker-leather-jackets | descriptionHtml | …ackets in genuine full-grain sheepskin, cut and hand-stitched to order in our own workshop. Asymmetric zip, be | genuine top-grain sheepskin, cut and hand-stitched to order in Pakistan |
| collection mens-biker-leather-jackets | custom.editorial | …y biker jacket here is made to order in genuine full-grain sheepskin, and <strong>paid i | genuine top-grain sheepskin |
| collection mens-bomber-leather-jackets | descriptionHtml | …>Leather bomber jackets in genuine full-grain sheepskin, made to order in our own workshop. Ribbed collar, cuf | genuine top-grain sheepskin, made to order in Pakistan |
| collection mens-bomber-leather-jackets | custom.editorial | …r jackets</a>.</p>  <p>Made to order in genuine full-grain sheepskin and <strong>paid in | genuine top-grain sheepskin |
| collection mens-black-leather-jackets | descriptionHtml | …for men, made to order in Pakistan from genuine full-grain sheepskin. Biker, bomber and | genuine top-grain sheepskin |
| collection mens-black-leather-jackets | custom.editorial | …y as it stretches. Every jacket here is genuine full-grain sheepskin, and our <a href="/ | genuine top-grain sheepskin |
| collection mens-leather-wallets | descriptionHtml (hidden FAQ) | For something boxed and ready to give, see our leather gift sets (/collections/kv2-gifting). | sentence removed (dead link; gift sets discontinued) |
| article news/discover-kordovan-leather-redefining-luxury-at-an-affordable-price | body | Our artisans employ traditional techniques | Skilled leather artisans in Pakistan use traditional techniques |
| article news/discover-kordovan-leather-redefining-luxury-at-an-affordable-price | summary | Our artisans employ traditional techniques | Skilled leather artisans in Pakistan use traditional techniques |
| article jackets/top-10-leather-jacket-brands-in-pakistan | body | Written by the Kordovan workshop team, where we have been cutting and stitching leather since 2019. | Written by the Kordovan team. |
| article jackets/top-10-leather-jacket-brands-in-pakistan | body | cut and stitched by hand in our workshop | cut and stitched by hand in Pakistan |
| article jackets/top-10-leather-jacket-brands-in-pakistan | body | cut and stitched to order in our own workshop. | cut and stitched to order in Pakistan. |
| article jackets/top-10-leather-jacket-brands-in-pakistan | body | <strong>made to order</strong> in our own workshop — we do not hold | <strong>made to order</strong> in Pakistan — we do not hold |
| article jackets/top-10-leather-jacket-brands-in-pakistan | body | You pay before we cut. | You pay before your jacket is cut. |
| article jackets/top-10-leather-jacket-brands-in-pakistan | summary | Written by a Pakistani leather workshop that is on the list, and says so. | Written by a Pakistani leather brand that is on the list, and says so. |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | Written by the Kordovan workshop team, where we cut and hand-stitch leather every day. | Written by the Kordovan team. |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | We cut and stitch every wallet in our own workshop in Malir Cantt, in | Every wallet is cut and stitched in Pakistan, in |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | no importer and no middle layer between the bench and the box | no importer between the maker and you |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | the most expensive thing we make is | the most expensive one we sell is |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | workshop pricing | direct pricing |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body (x2) | at a workshop price | at a direct price |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body (x2) | hand-stitched in our own workshop from Rs 1,499 | hand-stitched in Pakistan from Rs 1,499 |
| article wallets/top-10-leather-wallet-brands-in-pakistan | body | We make in batches. | Stock arrives in batches. |
| article wallets/top-10-leather-wallet-brands-in-pakistan | summary | Written by a Pakistani leather workshop that is on the list, and says so. | Written by a Pakistani leather brand that is on the list, and says so. |
| article jackets/best-winter-jackets-in-pakistan | body | Written by the Kordovan workshop team. | Written by the Kordovan team. |
| article jackets/best-winter-jackets-in-pakistan | body | made to order in our own workshop, from | made to order in Pakistan, from |
| article news/top-leather-brands-in-pakistan | body | Written by the Kordovan workshop team. | Written by the Kordovan team. |
| article news/top-leather-brands-in-pakistan | body | cut and hand-stitched in our workshop | cut and hand-stitched in Pakistan |
| article news/top-leather-brands-in-pakistan | body | Kordovan cuts and stitches in our own workshop in Malir Cantt. | Kordovan's pieces are cut and stitched in Pakistan. |
| article news/top-leather-brands-in-pakistan | body | Kordovan, ours, makes wallets and made-to-order jackets from our own workshop. | Kordovan, ours, offers wallets and made-to-order jackets, all made in Pakistan. |
| article news/top-leather-brands-in-pakistan | body | Kordovan — ours — makes wallets, bags and made-to-order jackets from our own workshop. | Kordovan — ours — offers wallets, bags and made-to-order jackets, all made in Pakistan. |
| article news/top-leather-brands-in-pakistan | body | all cut and stitched in our own workshop. | all cut and stitched in Pakistan. |
| article bags/best-leather-laptop-and-office-bags-in-pakistan | body | Written by the Kordovan workshop team, where we make these. | Written by the Kordovan team. |
| article bags/best-leather-laptop-and-office-bags-in-pakistan | body | We make these in our own workshop in Malir Cantt, in | These are made in Pakistan, in |
| article bags/best-leather-laptop-and-office-bags-in-pakistan | body (x2) | made in our own workshop from Rs 8,500 | made in Pakistan from Rs 8,500 |
| article news/real-vs-fake-leather-how-to-check | body | Written by the Kordovan workshop team. | Written by the Kordovan team. |
| article news/real-vs-fake-leather-how-to-check | body | cut and stitched to order in our own workshop. | cut and stitched to order in Pakistan. |
| article news/discover-kordovan-leather-redefining-luxury-at-an-affordable-price | body + summary | where we are dedicated to crafting high-quality leather products | where we are dedicated to offering high-quality leather products |
## Nov 14 follow-up (Founder: "yes, deploy and fix all four")
- Theme deployed: kordovan `f0b5cd1` (cherry-pick of cd94b8e; tags balanced, no "our workshop" left in the 5 files).
- DONE Nov 14 after reconnect (all 4 written, userErrors empty, read back live):
  1. Jacket article: "We have a single store in Malir Cantt." → "We have a single store." (Karachi rule)
  2. Desert Voyager bomber descriptionHtml: delete "It is also the jacket our customers have been most consistently happy with."
  3. Cindy Tote (gid://shopify/Product/8919014080752): repair truncated descriptionHtml.
  4. "Discover Kordovan Leather" (gid://shopify/Article/589424460016): fix broken markup at start of summary.

  Notes: jacket article now "We have a single store." (only Malir/Karachi mention across all 16 articles; verified). Cindy rebuilt as HTML from its own facts; the unverifiable "ethically sourced" claim dropped. Discover summary replaced with a one-line clean summary.
