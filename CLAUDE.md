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

## ✅ Working loop
Edit theme → push to draft theme `164277190896` (via Shopify) → review in browser
→ iterate. Keep to the BRAND_MOODBOARD spec at every step.
