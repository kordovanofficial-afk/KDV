# Kordovan — Brand Mood Board & Design System

> Pakistani full-grain leather house. Wallets, bags, small leather goods.
> This document is the single source of truth for the redesign. It is built
> from a teardown of the top global leather competitors plus 2026 luxury
> direction, then translated into a concrete palette, type system, and UX
> rulebook. Read this first before touching the theme.

Last updated: 2026-06-20

---

## 1. Positioning in one line

**"Heirloom leather, handmade in Pakistan — built to be handed down, not thrown away."**

We sit at the intersection of three proven playbooks:
- **Bellroy's** clarity & conversion engineering (clean, functional, benefit-led)
- **Saddleback's** heirloom storytelling & lifetime-warranty trust
- **Cuyana / Nappa Dori's** quiet-luxury minimalism & heritage craft narrative

We are NOT a fast-fashion accessories store and we are NOT a loud, discount-driven
Shopify dropshipper. Every design decision should feel *considered, warm, and permanent.*

---

## 2. Competitor teardown — the global top 10

For each: what they nail, and the **one lesson we steal.**

| # | Brand | Country | What they do exceptionally well | The lesson we steal |
|---|-------|---------|---------------------------------|---------------------|
| 1 | **Bellroy** | Australia | The gold standard for DTC leather UX. Every product page leads with a *benefit* and a problem solved ("slim profile, no break-in"). Interactive "fits X cards" visualisations. LWG-certified leather messaging. 3–10yr warranty shown on PDP. | Benefit-first product copy + warranty badge above the fold. Show *capacity/function*, not just specs. |
| 2 | **Saddleback Leather** | USA / Mexico | Founder-myth storytelling ("They'll Fight Over It When You're Dead"), 100-year warranty as the entire brand spine. Rugged, full-grain, hide-to-stitch control. | Make the **warranty + origin story** a hero pillar. "Built to outlive you." Heritage as the emotional hook. |
| 3 | **Carl Friedrik** | UK / Scandinavia | Restrained Scandinavian premium. Editorial photography, generous whitespace, muted dark palette, "intelligent design / long-lasting quality" positioning. Press logos as trust. | Editorial whitespace + press/trust logo strip. Premium = restraint, not clutter. |
| 4 | **Cuyana** | USA / Italy | "Fewer, better things." Cream/beige minimalism, sleek type, huge product imagery, sustainability narrative. Calm, feminine luxury. | Warm cream canvas + oversized imagery + a clear brand ethos line. Less product, more presence. |
| 5 | **Nappa Dori** | India | "Indian Minimalism." Proves a South-Asian heritage brand can read globally premium. Named after its materials (nappa leather + dori thread). Travel/wanderlust art direction. | We are the **Pakistani** answer to Nappa Dori. Lean into regional craft heritage as a global-premium asset, not a discount. |
| 6 | **Shinola** | USA (Detroit) | "Made in Detroit" place-as-brand. Iconic named silhouettes (Runwell). Everyday-luxury, built-to-last. | **Name the silhouettes** (the "Kodo Bifold", etc.) and tie the brand to place — "Made in Pakistan" as a badge of pride. |
| 7 | **Tanner Goods** | USA (Portland) | "Worth Holding Onto." Hand-made-with-vintage-tools craft narrative, workshop imagery, small-team authenticity. | Workshop / hands-at-work imagery. Show the maker, not just the product. |
| 8 | **Popov Leather** | Canada | Transparent craft ("100,000+ orders since 2013"), personalisation/monogramming, full-grain education page ("Our Leather"). Strong reviews. | A dedicated **"Our Leather"** education page + monogramming as an upsell. Volume/social proof numbers. |
| 9 | **WP Standard** | USA | Rich, warm, tactile photography; full-grain tan/cognac tones front and centre; lifestyle-on-leather styling. | Photography that makes you *feel the grain* — warm, close, textural. Colour-match the site to the product. |
| 10 | **Hidesign** | India | Scaled artisanal leather across many markets; eco-tanning story; broad but organised catalogue. | Keep the catalogue **navigable and category-led** even as it grows. Don't let range break the clean nav. |

### Patterns common to ALL winners
1. **Warm neutral canvas** (cream/bone), never stark white, never loud colour.
2. **One signature leather tone** that matches their hero product photography.
3. **Benefit-led copy**, specs hidden in collapsible tabs.
4. **Trust is structural**, not decorative: warranty, reviews, press, "made in ___".
5. **Big, textural, real photography.** No stock gradients, no clip-art icons.
6. **Restraint.** Few products per row, lots of whitespace, calm motion.
7. **A story.** Every great leather brand sells heritage + permanence, not a wallet.

---

## 3. Refined colour palette — "Quiet Heritage" (Kordovan 2.0)

The previous palette (Cognac `#8B5E3C` / Gold `#C9A96E` / Off-white `#FAF8F5` /
Charcoal `#1C1917`) was solid but had two weaknesses:
- The cognac read slightly **muddy/orange**.
- The dark was a **cold charcoal** — wrong for a warm leather brand.

The refinement (aligned to 2026 quiet-luxury direction — cognac as "the new
neutral", ivory bases, espresso replacing black):

### Core
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--canvas` | **Alabaster** | `#F7F2EA` | Primary background. Warm cream, not white. |
| `--parchment` | **Parchment** | `#ECE3D4` | Secondary surfaces, alternating sections. |
| `--ink` | **Espresso** | `#241C16` | Primary text + dark sections. Warm near-black (replaces cold charcoal). |
| `--walnut` | **Walnut** | `#4A3528` | Secondary dark, deep brown panels. |

### Signature
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--cognac` | **Cognac** | `#A0623A` | THE brand colour. Primary CTA, links, key accents. Richer/redder than before — passes AA with white text. |
| `--tan` | **Saddle Tan** | `#C08B5C` | Hover states, highlights, secondary buttons. |
| `--brass` | **Antique Brass** | `#B0894F` | Fine details, dividers, "gold" accents. Restrained — borders & rules, NOT text on light. |

### Supporting
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--stone` | **Stone/Taupe** | `#8B8174` | Muted/secondary text, captions. |
| `--border` | **Border** | `#DDD2C0` | Hairline borders, card edges. |
| `--olive` | **Heritage Olive** *(optional accent)* | `#5A5A3C` | Sparing "thread" accent — badges, tiny highlights. Our differentiator: every competitor is all-neutral; a single muted olive thread-tone feels heritage + distinctive. Use ≤5% of any screen. |

### Feedback
| Token | Name | Hex |
|-------|------|-----|
| `--success` | Deep Pine | `#2D6A4F` |
| `--error` | Oxblood | `#8B2D2D` |

**Rule of thumb per screen:** ~70% Alabaster/Parchment · ~20% Espresso/Walnut ·
~8% Cognac/Tan · ~2% Brass + (optional) Olive.

---

## 4. Typography

**Recommended upgrade:** replace Playfair Display with **Fraunces** for headings.
Playfair is everywhere and reads generic; Fraunces is a free Google variable serif
with optical sizing — softer, more editorial, more *heritage-luxury*, and
differentiates us instantly. Inter stays for body (clean, neutral, excellent on
mobile).

| Role | Font | Weights | Notes |
|------|------|---------|-------|
| Display / Headings | **Fraunces** (fallback: Playfair Display, Georgia, serif) | 400, 500, 600 + soft italic | Large, generous, tight leading on big sizes. |
| Body / UI | **Inter** (fallback: -apple-system, sans-serif) | 300, 400, 500, 600 | Body 16px min. Letter-spacing 0 on body, slight +tracking on small-caps labels. |
| Eyebrow / labels | Inter, uppercase, `letter-spacing: 0.12em`, `--stone` | 500 | "Bestsellers", "The Craft", section kickers. |

Type scale (keep existing rem scale): xs .75 / sm .875 / base 1 / md 1.125 /
lg 1.25 / xl 1.5 / 2xl 2 / 3xl 2.5 / 4xl 3.5 / 5xl 5rem.
Hero headline: 4xl–5xl, Fraunces 500, max 8 words.

---

## 5. Art direction / imagery

- **Warm, textural, real.** Close grain, hands working leather, leather on warm
  surfaces (wood, linen, stone). Match photo tone to the Cognac/Tan palette.
- **No gradient placeholders, no stock clip-art icons.** Trust icons are thin-line,
  single-weight, espresso.
- **Product photo order (every PDP):** 1) flat lay on clean surface · 2) in hand
  for scale · 3) open/inside · 4) texture macro · 5) lifestyle.
- **Hero:** full-viewport real leather footage/photo. One headline, one primary +
  one soft CTA.
- Always set descriptive `alt` text (see SEO rules below).

---

## 6. Layout & UX rulebook (locked spec)

### Navigation
- Max 6–7 top-level items. **Categories, not product lines.**
- Mega menu for **Bags** (subcategories + 1 featured product image). Simple
  dropdown for **Men/Women**. **No** dropdown for **Sale**.
- Sticky on scroll, height shrinks **80px → 56px**, logo scales down with it.
- Cart icon shows live count. Search opens a **full-screen overlay** (not a redirect).

### Hero
- One headline, **8 words max** — a benefit, not a description.
- One primary CTA ("Shop Wallets") + one soft CTA ("See the Craft"). **Never three.**
- Full-viewport real leather image/video.
- Trust line under the fold: *"Free delivery · 7-day returns · Genuine leather guaranteed"*.

### Homepage scroll order
1. Hero (emotion/desire)
2. Trust bar (risk removal)
3. Bestsellers — **4 products** (social proof)
4. Brand story, short (emotional "why us")
5. Collections grid (category navigation)
6. Testimonials carousel (real names, real products, verified)
7. Email capture — **offer (10% off)**, not just "subscribe"
8. Footer — clean, no clutter

### Product page (most important page)
- Title: `[Material] [Product Type] — [Key Feature]` → "Full-Grain Leather Bifold Wallet — RFID Blocking".
- Image order as in §5.
- Price prominent, **always above the fold**.
- **Add to Cart** = cognac, full-width on mobile, **never grey**.
- Below ATC: 3 trust icons (Genuine leather · Free delivery · 7-day returns).
- Description: first 2 lines = **benefits**; specs in a collapsible tab.
- "You May Also Like" = **3 products**, not 8.
- Reviews section at bottom with star breakdown.

### Collection page
- Filter bar: by type / price / colour. **Max 3 filters.**
- Default sort: **Bestselling** (not "Featured").
- Grid: **3 cols desktop / 2 mobile. No sidebar.**
- Card: image (hover → second angle), name, price, "Add to Cart" on hover.
- Collection hero: 2-line description + product count. **No big banner.**

### SEO
- Page title: `[Product Name] | Kordovan — Genuine Leather [Category] Pakistan`.
- Meta description: benefit + differentiator + CTA.
- Alt text: descriptive, not keyword-stuffed
  ("Brown leather bifold wallet open showing card slots").
- URL slugs: `/products/kodo-bifold-wallet`, never numeric IDs.

### Conversion-killers to eliminate
- Pop-ups on load → only after 45s or on exit intent.
- Shipping cost hidden till checkout → show it on the PDP.
- No size/care guide → add a **care guide tab** (reduces returns).
- Slow images → Shopify `img_url` with proper sizes (already done).
- Cart redirect → use the cart **drawer** (already done).

---

## 7. "Steal map" — quick reference

- Conversion mechanics & benefit copy → **Bellroy**
- Warranty + heirloom story → **Saddleback**
- Editorial restraint + press trust → **Carl Friedrik**
- Cream canvas + big imagery + ethos line → **Cuyana**
- Heritage-as-premium positioning → **Nappa Dori** (we're the Pakistani one)
- Named silhouettes + "Made in ___" → **Shinola**
- Maker/workshop imagery → **Tanner Goods**
- "Our Leather" education page + monogramming → **Popov**
- Feel-the-grain photography → **WP Standard**
- Navigable category-led catalogue at scale → **Hidesign**

---

## Sources
- [Saddleback Leather](https://saddlebackleather.com/) · ["They'll Fight Over It When You're Dead"](https://saddlebackleather.com/they-will-fight-over-it-when-youre-dead-book/)
- [Bellroy](https://bellroy.com/) · [Slim Sleeve PDP](https://bellroy.com/products/slim-sleeve-wallet)
- [Carl Friedrik](https://www.carlfriedrik.com/) · [Wikipedia](https://en.wikipedia.org/wiki/Carl_Friedrik)
- [Cuyana](https://cuyana.com/)
- [Nappa Dori](https://www.nappadori.com/) · [About](https://www.nappadori.com/pages/about-us)
- [Shinola](https://www.shinola.com/) · [Tanner Goods About](https://www.tannergoods.com/pages/about-us) · [Popov Leather About](https://www.popovleather.com/pages/about)
- [2026 luxury colour trends — Gelato](https://www.gelato.com/blog/trending-colors) · [Luxury brand colours — Zoviz](https://zoviz.com/blog/luxury-brand-colors-meanings)
