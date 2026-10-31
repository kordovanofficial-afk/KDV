# Theme build: repo, palette, logo, storefront state, performance, collections

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

## 📐 Design source of truth
- **`docs/brand/BRAND_MOODBOARD.md`** — competitor teardown (top 10 global leather
  brands), refined "Quiet Heritage" palette, typography, full UX/SEO rulebook.
  **Always follow this when designing or editing the theme.**
- **`docs/brand/moodboard.html`** — open in a browser to *see* the palette + type specimens.

## 🎨 Active palette — "Quiet Heritage" (Kordovan 2.0)
Refined from the original cognac/gold/off-white/charcoal set (cognac was muddy,
charcoal was too cold for leather):
- Alabaster `#F7F2EA` (bg) · Parchment `#ECE3D4` (surfaces)
- Espresso `#241C16` (text/dark) · Walnut `#4A3528`
- **Cognac `#A0623A`** (primary CTA/links) · Saddle Tan `#C08B5C` (hover) · Antique Brass `#B0894F` (detail)
- Stone `#8B8174` (muted text) · Border `#DDD2C0` · Heritage Olive `#5A5A3C` (sparing accent)
- Fonts: **Fraunces** (headings, replaces Playfair) + **Inter** (body)

> ✅ APPLIED on `kordovan`: `assets/theme.css` `:root` tokens, the
> Fraunces import, hardcoded gradients/shadows, and `config/settings_schema.json`
> defaults are all migrated to Quiet Heritage. Headings = Fraunces 500.

## 🗂 Repo structure & source of truth
**Single source of truth = the `kordovan` branch.** Everything (theme, docs,
tools, ops) lives here — one streamlined trunk for the brand rebuild.
```
kordovan  (trunk)
├── assets/ config/ layout/ locales/     ← THEME — MUST stay at repo root
├── sections/ snippets/ templates/       ←   (Shopify GitHub sync = branch root)
├── docs/
│   ├── brand/   (BRAND_MOODBOARD, DESIGN_SYSTEM, moodboard.html)
│   ├── seo/     (SEO_ARCHITECTURE, SEO_AUDIT_TRACKER)
│   ├── email/   (EMAIL_MIGRATION.html)
│   ├── images/  (IMAGE_BRIEF.md)
│   └── mockups/ (static HTML mockups — mockup-first workflow)
├── .claude/skills/                       ← 7 vendored SEO skills (MIT, see its README;
│                                            use during Phase-2 SEO pass; paid-API steps omitted)
├── tools/gsc-mcp-worker/                 ← FREE GSC connector (Cloudflare Worker)
├── ops/                                  ← agent/session playbooks & working notes
└── CLAUDE.md                             ← this file (read first every session)
```
- ⚠️ **Theme must NOT be nested under `theme/`.** Shopify's GitHub integration
  deploys from the *branch root* only — a `theme/` folder breaks the draft sync.
  Grouping is for everything *around* the theme (docs/tools/ops), never the theme.
- ✅ **MIGRATION DONE (Jul 15 2026):** `shopify-theme-deploy` → `kordovan`.
  `kordovan` is the GitHub **default branch** and Shopify is connected to it via a
  **NEW draft theme `165057069296` "KDV/kordovan"** (the old draft `164277190896`
  was deleted by the user — all references to the old draft ID are obsolete; any
  direct `themeFilesUpsert` pushes now target `165057069296`). Live theme
  `162105917680` untouched. Sole leftover: stale remote branch
  `shopify-theme-deploy` — the session git proxy refuses deletion pushes, so the
  user deletes it once on GitHub (repo → Branches → 🗑). It has no unique commits.
- Theme files live at the **repo root** (NOT under `theme/`): `assets/theme.css` +
  `theme.js`, `config/`, `layout/`, `locales/`, `sections/`, `snippets/`, `templates/`.
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

## 📍 Session state (resume here)
- **Workflow = mockup-first:** build static HTML mockup in `docs/mockups/` →
  user approves → THEN implement in Liquid → deploy once. (User's idea — avoids
  repeated Shopify pushes/sync lag while iterating on design.)
- ⚠️ **GOTCHA — class-name collisions:** homepage collection-grid TILE class
  `.kv-coll` (display:flex) collided with the collection-PAGE wrapper `.kv-coll`,
  forcing the page into 3 columns. FIXED by scoping all homepage tile rules under
  `.kv-colls .kv-coll`. Lesson: namespace page wrappers distinctly.
- ⚠️ **GOTCHA — GitHub sync got stuck on `sections/main-product.liquid`** (draft
  kept serving the legacy `.product-page` template; new file `pdp-main` section
  also wouldn't sync, and `templates/*.json` are theme-editor-owned so git won't
  overwrite them). FIX: PDP body lives in `snippets/pdp-main.liquid` (snippets DO
  sync); `sections/main-product.liquid` is a thin `{% render 'pdp-main' %}` wrapper
  pushed directly to the DRAFT theme via `themeFilesUpsert` (allowed on unpublished;
  blocked on live). If main-product ever reverts, re-upsert the wrapper.
- **Done & deployed** to `kordovan`: Step 1 (Quiet Heritage palette +
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
- **CART DRAWER DONE & deployed:** `sections/cart-drawer.liquid` restyled to
  `docs/mockups/cart-drawer.html` (`.cart-drawer` in home.css). `theme.js
  CartDrawer.render` now outputs the **free-shipping progress bar** (threshold
  PKR 2,500 = `250000` minor units in `renderShip()` — change there if free-ship
  amount changes), kv line items with inline qty + **Remove**, subtotal; shows/
  hides ship+cross-sell on empty. **Header cart `.kv-cart` now opens the drawer**
  (fixed the earlier gap). `KDV.updateCartCount()` updates both legacy + `.kv-cart i`
  badges. Cross-sell = server-rendered from `cart-drawer` section setting
  `upsell_collection` (default `kdv-accessories`), one-click via the quick-add hook.
- **SEARCH DONE & deployed:** full-screen overlay `snippets/search-overlay.liquid`
  (opens from `.kv-search` desktop + mobile-menu link; popular searches + category
  empty state; debounced live results) backed by `sections/predictive-search.liquid`
  (server-rendered suggestions/collections/products via `/search/suggest?section_id=
  predictive-search`). `sections/main-search.liquid` restyled to `.kv-coll` grid +
  `card-product` + Load More + friendly no-results. `.kv-srch` CSS in home.css.
- **STOREFRONT BUILD COMPLETE** (homepage, content pages, PDP, collection, cart
  drawer, search). **OPEN = SEO PASS + polish:** (1) per-product enrichment +
  self-authored reviews via metafields; (2) titles/meta/alt text + PDP Product
  JSON-LD; (3) enable storefront filters (Search & Discovery); (4) logo upload +
  favicon + social share image; (5) optional polish: /cart PAGE, 404 & account
  pages still on legacy theme styling; wishlist heart is decorative (no backend).
- Logo: user is uploading manually (Header → "Logo (dark mark)"); needs a
  TRANSPARENT-bg black PNG (their source had a white bg). Favicon/social TODO.

## ⚡ Performance rules (Jul 26 2026 pass — do not regress)
- **Fonts must stay a `<link>` in `layout/theme.liquid`.** Never put the Google
  Fonts call back as `@import` in `theme.css` — that forced a 3-deep serial chain
  (css → googleapis → gstatic) before first paint.
- **Hero is a real `<img>`, not a CSS background.** Backgrounds are invisible to
  the browser's preload scanner and can't be responsive; the hero is the homepage
  LCP element. `object-fit:cover` + `object-position:center right` reproduce the
  old framing.
- **Every new `<img>` needs `srcset` + `sizes` + `width`/`height` + `loading`.**
  A bare `image_url: width: 600` ships a desktop file to a 180px phone slot.
  Above-fold → `loading="eager" fetchpriority="high"`; everything else → `lazy`.
- **Gallery swaps decode before painting** (`assets/theme.js` `goTo`/`preload`).
  Never reintroduce a fixed `setTimeout` fade — it shows a blank frame while the
  file downloads. Anything that changes the main image must set **`srcset` as well
  as `src`**, or the browser keeps painting the old one.
- ⚠️ `theme.css` holds the `:root` design tokens that `home.css` depends on —
  it cannot be dropped even though it is largely legacy styling.
- Verify before pushing: `node --check assets/theme.js` + div/liquid tag balance.
  The site cannot be loaded from this environment (proxy denies
  `kordovanleather.com`), so static checks are the only safety net.

## 🖼 Image workflow (protocol)
- **Every designed image slot = an image brief:** product/subject + ready-to-paste
  GPT-image prompt + exact px size & aspect. Tracked in **`docs/images/IMAGE_BRIEF.md`**.
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
Edit theme → push to draft theme `165057069296` (via Shopify) → review in browser
→ iterate. Keep to the BRAND_MOODBOARD spec at every step.


## Header nav: Winter link (Oct 31 2026)
- `sections/site-header.liquid`: "Winter" → `/collections/winter-collection` sits directly above Sale in the desktop `kv-nav` and the mobile `kv-mmenu`. Pushed to `kordovan` (c36afe6, user-requested), live theme file updated 2026-10-31T06:18Z. Collection `493073760496`, 4 products (brown + black men's gloves, women's dark red gloves, flat cap).

## Homepage hero: Winter banner (LIVE Oct 31 2026, kordovan 41f61e1)
- `sections/hero-banner.liquid` shows a Winter Collection banner when the "Winter banner" checkbox is on or missing (editor strips settings, so missing = on). Untick it in the theme editor to restore the brand hero.
- Art: desktop `Dusk_Market_Portrait_in_Warm_Leather.png` (1672x941), phone `Cinematic_Historic_Street_Portrait.png` (1122x1402) via <picture> at 749px. Phone layout in `home.css` (.kv-hero--winter): text at the bottom, face clear.
- Copy: WINTER COLLECTION / Ready for the cold. / Flat caps and sheep leather gloves, for him and for her. / Shop the Winter Collection → /collections/winter-collection / Cash on delivery · Free delivery over Rs 5,500 · Genuine leather.
- Live theme checksums matched the repo files at 06:39Z.
