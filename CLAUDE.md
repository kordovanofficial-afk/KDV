# Kordovan — Project Memory

Custom Shopify theme for **Kordovan**, a Pakistani full-grain leather brand
(wallets, bags, small leather goods). This file is the persistent context for
every session — read it first.

## 📐 Design source of truth
- **`docs/BRAND_MOODBOARD.md`** — competitor teardown (top 10 global leather
  brands), refined "Quiet Heritage" palette, typography, full UX/SEO rulebook.
  **Always follow this when designing or editing the theme.**
- **`docs/moodboard.html`** — open in a browser to *see* the palette + type specimens.

## 🎨 Active palette — "Quiet Heritage" (Kordovan 2.0)
Refined from the original cognac/gold/off-white/charcoal set (cognac was muddy,
charcoal was too cold for leather):
- Alabaster `#F7F2EA` (bg) · Parchment `#ECE3D4` (surfaces)
- Espresso `#241C16` (text/dark) · Walnut `#4A3528`
- **Cognac `#A0623A`** (primary CTA/links) · Saddle Tan `#C08B5C` (hover) · Antique Brass `#B0894F` (detail)
- Stone `#8B8174` (muted text) · Border `#DDD2C0` · Heritage Olive `#5A5A3C` (sparing accent)
- Fonts: **Fraunces** (headings, replaces Playfair) + **Inter** (body)

> ✅ APPLIED on `shopify-theme-deploy`: `assets/theme.css` `:root` tokens, the
> Fraunces import, hardcoded gradients/shadows, and `config/settings_schema.json`
> defaults are all migrated to Quiet Heritage. Headings = Fraunces 500.

## 🗂 Theme structure & source of truth
**Source of truth = the `shopify-theme-deploy` branch** (this is what Shopify's
GitHub integration deploys). Theme files live at the **repo root** (NOT under
`theme/`): `assets/theme.css` + `theme.js`, `config/`, `layout/`, `locales/`,
`sections/`, `snippets/`, `templates/`.
- Header/footer sections are named **`site-header.liquid` / `site-footer.liquid`**
  (renamed to avoid a Shopify customizer section-group conflict — do not rename back).
- ⚠️ A second, unrelated theme history exists on `claude/vigilant-euler-h81zbc`
  (a from-scratch rebuild nested under `theme/`, sections named `header`/`footer`).
  It is NOT deployable as-is and is NOT the source of truth. Ignore it unless
  explicitly told otherwise.

## 🐎 Brand logo
- Mark: a **black horse-head silhouette** (registered trademark / copyright —
  brand-owned asset, never reproduce/trace it or use it outside this theme).
- Header (`sections/site-header.liquid`) supports it via the `logo` image_picker
  (upload in theme editor → Header → "Logo (dark mark)"). Because the mark is solid black, CSS
  auto-inverts it to cream on the transparent/dark header — one upload suffices.
  Optional `logo_light` slot exists for a custom cream version.
- Logo sizing: 44px header height, shrinks to 34px on scroll (sticky shrink).
- TODO when the file is provided: also set it as favicon + social share image.

## 🚦 Hard constraints (do not violate)
- **Live theme `162105917680` — NEVER touch it.**
- Draft / unpublished theme `164277190896` — the working preview.
- Shopify GitHub integration deploys from the **`shopify-theme-deploy`** branch.
- **Work on `shopify-theme-deploy`** (the source of truth). Pushing it triggers
  the Shopify sync to draft theme `164277190896`. User authorized per-step deploys.
- Do not create PRs unless explicitly asked.

## 🔌 Available integrations (MCP)
Shopify, GitHub, Canva, Figma, Facebook Ads, Higgsfield.
(Playwright is NOT available in this remote env — design is done in code, then
pushed to the draft theme to preview in a browser.)

## 📍 Session state (resume here)
- **Workflow = mockup-first:** build static HTML mockup in `docs/mockups/` →
  user approves → THEN implement in Liquid → deploy once. (User's idea — avoids
  repeated Shopify pushes/sync lag while iterating on design.)
- **Done & deployed** to `shopify-theme-deploy`: Step 1 (Quiet Heritage palette +
  Fraunces + logo support), Step 2 (homepage scroll order, brand story copy,
  testimonial names, eyebrow fix).
- **Homepage mockup** `docs/mockups/homepage-final.html` — APPROVED. **Homepage is
  now FULLY BUILT & deployed** (all kv- sections in `assets/home.css`, loaded
  globally via `layout/theme.liquid`): header → hero → trust marquee → bestsellers
  (Customer Favourites) → brand story → collections grid → testimonials (continuous
  horizontal review marquee, 10 verified reviews, pause-on-hover — user asked for
  "lots of reviews that scroll") → email capture (real Shopify customer form) →
  footer (`site-footer.liquid`, hardcoded content).
- **Content pages DONE:** `sections/main-page.liquid` rebuilt into on-brand editorial
  layout (`.kv-page` / `.kv-rte` in home.css); leading h1/h2 in page bodies is
  CSS-suppressed (hero band shows the title). Pages already exist in the store w/
  real content — footer/CTA links repointed to the REAL handles:
  `about-kordovan` (Our Story), `our-craft` (hero "See the Craft"), `shipping`,
  `leather-care-guide`, `returns`. (Don't use `/pages/about` or `/pages/leather-care`.)
- ⚠️ **Editor strips SETTINGS too (not just blocks):** the theme editor removed
  newly-added section settings (`aggregate`, `percent`, `count`, hero `heading`)
  from `index.json` on sync — harmless ONLY because every kv- section supplies
  `| default:` fallbacks in liquid. Keep hardcoded defaults on all section settings.
- **Content-page designs DONE & deployed:** Our Story (`about-kordovan`), Our Craft
  (`our-craft`), Shipping (`shipping`), Leather Care (`leather-care-guide`), Returns
  (`returns`) — bespoke layouts rendered via `snippets/*` dispatched by handle in
  `sections/main-page.liquid` (theme-local; NO template-suffix change → live theme
  untouched). Shared `.kv-cp` component CSS in home.css. Images uploaded to Files
  (`about-*`, `craft-*`, `care-patina`, `returns-pillar-bg`).
- **PRODUCT PAGE (PDP) DONE & deployed:** `sections/main-product.liquid` +
  `related-products.liquid` restyled to the approved `docs/mockups/product.html`
  (`.kv-pdp` CSS). Reuses ALL `theme.js` hooks (`.product-gallery`, `.product-form`,
  `.variant-btn`, `.product-atc__*`, `.product-info__price-*`, `[data-product-variants]`)
  so gallery/variants/AJAX add-to-cart/cart-drawer work untouched. Structure:
  gallery + sticky benefit buy-box (price+shipping transparency, full-width cognac
  ATC, 3 trust icons) → 4 brand features → capacity "fits" (metafield) → description
  + Care/Shipping/Warranty accordion → reviews (metafield) → guarantee → related →
  sticky mobile ATC.
- ⚠️ **SEO-PHASE TODOs (user-confirmed, remember):** (1) NO review app — author
  reviews ourselves per product via metafields: `reviews.rating` (number),
  `reviews.rating_count`, `custom.reviews` (one per line `name|city|text`). PDP shows
  the reviews block + star rating ONLY when `reviews.rating` is set (hidden until then).
  (2) Go product-by-product so EVERY active product matches this PDP's depth — fill
  `custom.subtitle`, `custom.benefits` (one per line), `custom.material`, capacity
  `custom.fits` (`value|label` per line) + `custom.fits_title`/`fits_text`, full image
  gallery. Until filled, brand-universal fallbacks render.
- **Known follow-up:** site header cart link (`.kv-cart`) navigates to /cart; it does
  NOT open the cart drawer (theme.js binds drawer-open to legacy `.header__cart-btn`).
  Wire `.kv-cart` to open the drawer when we polish cart.
- **COLLECTION / CATEGORY PAGE DONE & deployed:** `sections/main-collection.liquid`
  + new `snippets/card-product.liquid` restyled to `docs/mockups/collection.html`
  (`.kv-coll` / `.kv-pc` CSS). Compact hero, sticky toolbar (native sort +
  storefront filter pills/drawer + active chips), 3/2-col grid, hover 2nd-image +
  Quick Add (reuses theme.js `.product-card__quick-add[data-variant-id]`) + colour
  swatches + Sold-Out/Sale/New badges + wishlist, JS **Load More** (appends next
  paginated page), editorial SEO block + `CollectionPage`/`ItemList` JSON-LD.
  Serves EVERY category. `collection.json` keeps email_signup below.
  ⚠️ **Filter pills/drawer populate only when storefront filters are enabled** in
  admin → Search & Discovery → Filters. Until then: just "All" + sort (graceful).
  Optional `collection.metafields.custom.editorial` overrides the SEO block.
- **OPEN / next up (user picks):** cart drawer polish — restyle to Quiet Heritage
  + wire `.kv-cart` header icon to open the drawer (recommended next) · search
  results (reuse `.kv-coll`/`card-product`) · SEO pass (per-product enrichment,
  self-authored reviews, titles/meta/alt, enable storefront filters).
- Logo: user is uploading manually (Header → "Logo (dark mark)"); needs a
  TRANSPARENT-bg black PNG (their source had a white bg). Favicon/social TODO.

## 🖼 Image workflow (protocol)
- **Every designed image slot = an image brief:** product/subject + ready-to-paste
  GPT-image prompt + exact px size & aspect. Tracked in **`docs/IMAGE_BRIEF.md`**.
- Give new briefs inline whenever a new image slot is introduced.
- **Label/copy on a tile must match the image in it** (no mismatched product names).
- Product cards use real Shopify catalogue photos; hero/mega/collection/brand-story
  use the generated "art-directed" images.

## 🗃 Site collections (kdv- set — controlled, for this theme)
Created as **smart collections** (auto-populate by tag), published to Online Store,
sorted **Best Selling**. Referenced by hardcoded handle in Liquid (NOT via JSON
template settings — Shopify's editor strips collection/handle settings from
`templates/index.json` on sync, which is why block-based references render empty).
- `kdv-wallets` (≈55) · `kdv-bags` (≈68) · `kdv-jackets` (≈36) · `kdv-shoes` (≈24)
  · `kdv-belts` (≈13) · `kdv-accessories` (≈28)
- Header nav + Bestsellers (#1 per category) reference these. New Arrivals →
  `/collections/all?sort_by=created-descending`; Sale → `/collections/all` (no
  kdv-sale yet). Women's sub-links still use existing womens-* collections.

## ✅ Working loop
Edit theme → push to draft theme `164277190896` (via Shopify) → review in browser
→ iterate. Keep to the BRAND_MOODBOARD spec at every step.
