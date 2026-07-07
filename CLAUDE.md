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

## 📧 ACTIVE — Hosting/email cost migration (backend cleanup before SEO)
Goal: kill TMDHosting "Starter" Linux hosting ($180/yr, renews in ~9 mo from Jul 2026)
→ total ~$20/yr. Site is 100% on Shopify; hosting only serves DNS + cPanel email.
- Domain .com at TMD $19.99/yr — **renews ~Aug 2026, RENEW IT** (transfer to
  Cloudflare Registrar ~$10/yr only NEXT year, never near expiry).
- **DECIDED (user-confirmed): Zoho Mail Forever Free, webmail + Zoho app only**
  (user accepts no IMAP → Thunderbird demoted to local ARCHIVE of old mail).
  5 seats: `admin@`, `asadj@`, `umair@`, `contact@`, `corporate@`.
  Aliases: `sales@` + `daraz@` → admin ONLY. User DELETED `customercare.usa@`,
  `shahid.butt@us.`, `marketing@`, `social@` (verified unused: not on site/
  Shopify/customers; socials are under user's personal Meta email). `kordovan`
  system catch-all — emptied (pure spam); NO catch-all in Zoho.
- **Guide = `docs/EMAIL_MIGRATION.html`** (baby-steps, 8 phases + troubleshooting,
  delivered). User executing solo; reports back after the Phase 6 test checklist.
  Catch-all mailbox already emptied (was pure spam).
- **STATUS Jul 4 2026 — MIGRATION EXECUTED ✅:** Zoho org live (5 users + sales@/
  daraz@ aliases on admin, all green: MX/SPF/DKIM verified). DNS moved to
  Cloudflare Free (nameservers brady/lucy.ns.cloudflare.com set at TMD). Final
  CF zone = 15 records, ALL grey-cloud/DNS-only: A@→23.227.38.65, CNAME www/
  account→shops.myshopify.com, 4× Shopify email CNAMEs (s9k/s9k2/s9k3._domainkey
  →dkim1-3.e2b7bcdd21fe.p531.email.myshopify.com + mailers9k), 3× Zoho MX,
  TXT: zoho SPF, zmail._domainkey DKIM, _dmarc (p=none+rua), zoho-verification,
  facebook-domain-verification (Meta ads — NEVER delete). Klaviyo NS+TXT deleted
  (user confirmed unused). Old mail archived in Thunderbird Local Folders.
  User tested all 7 addresses — working. **PENDING:** (1) observation window →
  ~Jul 18: disable TMD Starter auto-renew (hosting only, NOT domain!);
  (2) domain renewal ~Aug 2026 $19.99 — PAY IT; (3) optional: SPF/DKIM/DMARC
  "show original" check + COD test-order email check.
- **Site emails:** gmail address PURGED from theme (commit ff8aeb3) — public
  contact = `contact@kordovanleather.com` (footer + story/care/shipping/returns
  snippets); `admin@` remains in Shopify PAGE content (FAQs/Contact/Corporate/
  policies) + store sender. Optional pending: Corporate page quote email →
  `corporate@` (live page content — needs explicit OK).

## 🧹 DONE — Customer-base cleanup (Jul 5 2026, pre-SEO backend hygiene)
From 27,193 → ~26,000 profiles. Executed via Shopify MCP GraphQL (user granted
approval; `customerDelete` works, `customerMerge` BLOCKED — connector token
lacks `write_customer_merge` scope, no workaround; direct API egress blocked).
- Alias/duplicate analysis from customer CSV export (scratchpad, session-local):
  892 clusters → 185 zero-order duplicates API-deleted · 23 priority merges
  (dup ≥2 orders) done MANUALLY by user in admin (Spring '26 has native
  "Mergeable" column + Merge button) · 446 one-order-dup merges + 86
  consent-hold merges SKIPPED as cosmetic (list = manual_merge_list.csv,
  delivered) · 6 junk test profiles deleted (placeholder phones 0300-0000000/
  1234567, "Test/Abc Def" names); 9 junk-with-orders remain (undeletable).
- BIG PURGE: 985 deleted (zero orders + no email/SMS/WhatsApp consent + no
  tags/notes + created ≤Dec 26 2025 via ID↔date probing; 520 recent spared;
  2 refused by API order-guard). Audit logs delivered to user.
- **SERIAL COD REFUSERS tagged (Jul 7 2026):** bulk-exported ALL 5,203 cancelled
  orders (bulkOperationRunQuery → storage.googleapis.com URL IS fetchable through
  proxy; cdn.shopify.com is NOT). Refuser = 2+ cancels with reason CUSTOMER/FRAUD/
  OTHER (excluded INVENTORY/STAFF/DECLINED = our-side). 425 serial refusers found;
  **API-tagged `FRAUD RISK` on 323** (the "never completed a single order" set),
  9 batches of tagsAdd, zero errors. Skipped 4 internal/team (Asad Janjua/Umair
  Khan/biz phone 3332601161·3009120000) + 71 MEDIUM (2 cancels but did complete) +
  27 other HIGH (3+ cancels but completed ≥1 — OFFERED to tag, user hasn't said yes).
  `customerDelete` CANNOT remove them (Shopify blocks delete of any customer with
  orders, incl. cancelled). List = serial_cod_refusers.csv (delivered).
- **Shopify Flow LIVE (user built, on):** Order created → IF customer tags Includes
  "FRAUD RISK" → Add order tag `⛔ FRAUD RISK`. Auto-flags every new order from a
  refuser at top of order. (Order tags are grey chips, not red text — Shopify has no
  native tag colouring w/o a paid app; ⛔ emoji is the visibility hack.)
- **OPEN:** 56 REVIEW clusters (different names sharing phone/address — family
  vs COD-refuser) await user's CANCELLED-ORDERS export → then tag via API (tags
  work). User's own profiles: business phone 3332601161 cluster.

## 📣 Meta Ads (SCOPED — Kordovan 2025 ONLY)
- **ONLY account to ever touch/reference: `995683712074843` ("Kordovan 2025", PKR,
  ACTIVE).** User locked scope Jul 7 2026. IGNORE all others (Kordovan Leather
  337…255 = DISABLED/flagged; Kordovan 2.0 492…061 = closed; Corporate 136…323;
  UAE 589…560; + unrelated DEW/Vertix/Ivy Laine/Oakn'Moss).
- **KEY INSIGHT (parallels COD finding):** lookalike seeds = Pixel "Purchase"
  (order PLACED) → ~40% are COD refusers, so LLAs teach Meta to find refusers.
  FIX PLAN: (1) reseed value-based LLA from DELIVERED/PREPAID buyers (clean seed
  buildable from bulk order export); (2) build REFUSER EXCLUSION audience (323
  FRAUD RISK + all cancelled-order customers) → exclude from prospecting;
  (3) feed delivered/paid back as conversion signal (offline conv/CAPI); (4) prune
  ~25 audience sprawl. Old inactive "Lifetime Fulfilled Customers" LLA had the
  right idea (fulfilled=delivered) but is off.
- Uploading customer PII (hashed) to Meta needs explicit user OK each time.
- Pixel EMQ check pending (tool needed approval). Data export files in scratchpad:
  cancelled_orders.jsonl (5203), orders_12mo.jsonl (3468), serial_cod_refusers.csv.
- **Prepaid discount LIVE on store:** code `PAYONLINE10` (10% off, active, unlimited).
  Deploy via WhatsApp order-confirmation reward (leak-proof, no app). Full enforce
  + COD fee + OTP later via PostEx XPay integration (user exploring) — PARKED.

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
