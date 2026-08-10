# Cowboy hats SEO — Aug 10 2026

Second SEO pass after jackets. **Different problem, different fix**: hats
already rank well. Jackets had a CTR problem at page-two positions; hats have
good CTR at position 5 and need depth to climb, plus a stock problem that
outweighs everything on this page.

## 1. The data — 12 months, queries containing "hat"

| Query | Impressions | Position | CTR | Clicks |
|---|---|---|---|---|
| **cowboy hat** | **5,423** | 5.55 | **6.69%** | 363 |
| cowboy hat pakistan | 1,478 | 4.61 | **23.3%** | 345 |
| **cow boy hat** *(misspelling)* | **914** | 5.65 | **5.69%** | 52 |
| cowboy hats | 814 | 5.62 | 8.48% | 69 |
| cowboy hat price in pakistan | 790 | 2.93 | 21.5% | 170 |
| leather hats | 579 | 7.67 | 5.01% | 29 |
| **leather hat** | 551 | **3.80** | **5.81%** | 32 |
| cowboy hats pakistan | 523 | 3.86 | **29.1%** | 152 |
| hat price in pakistan | 186 | **3.56** | **1.08%** | 2 |

~13,500 impressions and ~1,450 clicks a year.

### The pattern
**Pakistan-qualified queries convert brilliantly (23–29% CTR). Generic ones do
not (5–7%).** For `cowboy hat` the SERP is full of international retailers, so
a Pakistani shop earns fewer clicks at the same position — that part is
structural and not fixable with a title.

But two are genuinely underperforming for their position and are fixable:
- `leather hat` — **position 3.80, 5.81% CTR.** Should be 10–12%.
- `hat price in pakistan` — **position 3.56, 1.08% CTR.** Should be ~10%.

`cow boy hat` at 914 impressions is a misspelling worth keeping in mind — it
cannot go in a title without looking illiterate, but Google matches it to the
correct spelling anyway.

## 2. What was wrong

| Defect | Count |
|---|---|
| **Products with NO SEO title or description at all** | **4 of 6** |
| Product body descriptions **identical, word for word** | **6 of 6** |
| `productType` inconsistent (`Hats` ×5, empty ×1) | 1 |
| Collection SEO title over 60 chars (truncated) | 1 |
| Collection body carried `&amp;nbsp;` artifacts and an empty `<!---->` | 1 |

Six products sharing one description verbatim is duplicate content inside a
single collection — the weakest possible signal for a category that is trying
to rank first.

## 3. What was applied

**Collection** — new title `Leather Cowboy Hats in Pakistan — From Rs 4,800 |
Kordovan` (57 chars, carries the price the highest-intent queries ask for), new
meta, and a rewritten body covering:
- **How to size a hat** (measure above the ears, size up between sizes) — the
  single most useful thing on a hat page and the reason people abandon
- Style guide: crushable / suede / studded / Clifford
- What a leather hat should cost in Pakistan, and what under Rs 2,500 means
- Care — crown-down storage, drying, conditioning
- **Karachi shop mention** for `cowboy hats near me` and `cowboy hat karachi`
- Internal links to leather caps and accessories

**All 6 products** — unique SEO title, unique meta with price, and a genuinely
different body per product written around what actually distinguishes it
(crushable vs suede nap vs crazy-horse patina vs the heavier Clifford build).
`productType` normalised to `Hats`.

⚠️ **Free delivery is only claimed on the two Rs 10,500 Clifford hats.** The
threshold is Rs 5,500, so the Rs 4,800 and Rs 9,000 hats do not qualify and
their copy says cash on delivery only. Hats are **not** prepaid-only — that
restriction applies to jackets, so COD is stated correctly here.

## 4. 🔴 The stock problem outweighs all of the above

| Product | Price | Total inventory | First variant buyable |
|---|---|---|---|
| Crushable Western Cowboy Hat | 4,800 | 15 | ❌ **no** |
| Suede Western Cowboy Hat, Brown | 4,800 | **0** | ❌ **no** |
| Studded Band, Burgundy | 9,000 | **0** | ❌ **no** |
| Clifford Faded Black | 10,500 | 1 | ✅ |
| Clifford Rustic Brown | 10,500 | 3 | ✅ |
| Black Stripe Cowboy Hat | 4,800 | 1 | ❌ **no** |

**Four of six are unbuyable. Two are at literal zero. Total stock across the
category is about 20 units.**

These are `tracksInventory: true` with real zeros — unlike the jackets, where
zero meant "untracked, always available". This is genuine sold-out.

The category pulls **2,027 impressions a month at position 5 with 13.2% CTR**,
and most of that traffic lands on something it cannot buy.

**Question for the user: are hats made to order like the jackets, or real
stock?**
- If made to order → untrack inventory as we did for jackets and all six
  become buyable immediately.
- If real stock → the category needs restocking before any ranking gain is
  worth having.

## 5. Honest ceiling on "rank #1"

The on-page work is done to standard. It does not guarantee position 1, and it
would be dishonest to claim it does:

- `cowboy hat` at position 5.55 is competing with international retailers who
  have far more domain authority. On-page work can realistically move this to
  3–4, not 1.
- `cowboy hat pakistan` at 4.61 and `cowboy hats pakistan` at 3.86 are
  genuinely winnable — the intent is local and the competition is thinner.
- `leather hat` at 3.80 with 5.81% CTR should improve on CTR alone.

**And ranking first while four of six products are sold out would make things
worse, not better** — higher impressions against an out-of-stock page trains
Google that the result disappoints.

Remaining gaps not addressed here: no image alt-text audit on hat images, no
FAQ schema on the collection (the theme has no collection FAQ block), and the
messy handle `copy-of-kordovans-crushable-...` which is not worth the redirect
risk to change.

---

# 🔴 Aug 10 — the collection copy was not rendering. Fixed.

User reported the editorial block on `/collections/cowboy-hats` was not
showing what the wallets collection shows. It wasn't, and the cause is in
`sections/main-collection.liquid`:

| Where | What it renders |
|---|---|
| Hero, line 20 | `collection.description \| strip_html \| truncatewords: 40` |
| Editorial block, line 129 | `collection.metafields.custom.editorial`, **else** a hardcoded generic fallback |

**The collection body description is never rendered in full anywhere on the
page.** The hero shows the first 40 words with all HTML stripped, and the block
below the grid reads a *metafield*, not the body.

So the ~500-word cowboy-hats body written on Aug 10 — sizing guide, style
guide, price context, care, the Karachi shop mention — was invisible to both
readers and Google. Only its first 40 words appeared, as one flat paragraph.
Meanwhile the editorial block was still serving the old two-paragraph metafield
from before the rewrite.

Wallets looked correct by luck: `mens-leather-wallets` has a 35-word body that
survives the truncation intact, and a populated `custom.editorial` metafield.

## The fix — no theme change

Split the copy the way the template expects:

- `collection.description` → a 36-word summary, sized to survive `truncatewords: 40`
- `custom.editorial` → the full long-form copy, which renders below the grid

Links and lists carry **inline styles**, because `.kv-coll__editin` in
`assets/home.css` has rules for `h2`, `h3` and `p` only — and `theme.css` sets a
global `a { color: inherit; text-decoration: none }`, so an unstyled link in
this block is invisible as a link. Inline styles avoid a live-theme push.

## Same defect on other collections

| Collection | Body | `custom.editorial` | Renders below grid |
|---|---|---|---|
| `cowboy-hats` | 36-word summary | full copy | ✅ fixed Aug 10 |
| `mens-leather-wallets` | 35 words | set | ✅ fine |
| `mens-leather-jackets` | ~90 words, **truncated to 40** | old generic copy | ⚠️ Aug 9 body is half-invisible |
| `kdv-jackets` | **empty** | none | generic fallback |
| `womens-leather-jackets` | **empty** | none | generic fallback |
| `kdv-wallets` | ~70 words, **truncated** | none | generic fallback |

## Optional theme polish (needs a live push, not done)

Add to `assets/home.css` under `.kv-coll__editin` — `ul/ol/li` spacing, `li::marker`
in brass, and `a` in cognac with an underline, mirroring the existing `.kv-rte`
rules. Would let the metafield copy drop the inline styles.

---

# Aug 10 — the PDP "fits" band. The real question.

The block the user was pointing at is the PDP capacity band in
`snippets/pdp-main.liquid` (line 155) — eyebrow, headline, paragraph, three
stat tiles, and a wide image on the left. It is gated on one metafield:

```liquid
{%- if product.metafields.custom.fits != blank -%}
```

No `custom.fits`, no band. The image is not "image 5" by rule — the snippet
walks `product.images` and takes the **first one with `aspect_ratio > 1.2`**,
falling back to `product.media[1]`. On the hats that happens to be image 5,
because all six carry four portrait shots (1122x1402) then one landscape
lifestyle shot (1536x1024).

## Coverage across the live catalogue

**20 of 170 active products have `custom.fits`. All 20 are wallets.**

Zero on jackets, hats, bags, shoes, belts, caps, gloves — and 11 wallets are
missing it too, including **The Razor**, which is one of the two products
carrying live paid traffic.

| Category | Active | Has the band |
|---|---|---|
| Wallets (all sub-types) | ~31 | 20 |
| Leather Jacket | 30 | 0 |
| Hats | 6 | 0 → **6 (fixed Aug 10)** |
| Bags / laptop / backpack / duffle | ~35 | 0 |
| Shoes | ~22 | 0 |
| Belts | ~11 | 0 |
| Caps, gloves, cases, misc | ~35 | 0 |

## Applied — all six hats

`fits`, `fits_title` and `fits_text` written per hat. Size ranges are taken
from the real variant options and differ per product — Clifford Faded Black is
XL only, Clifford Rustic Brown is XL–XXL, the Studded Band is M–XL, the rest
S–XL. No theme change was needed; the landscape image was already there.

## ⚠️ One hardcoded string does not survive the move off wallets

Line 172 is `<span class="eyebrow">Holds What Matters</span>` — wallet language.
It reads wrong above a hat, and will read wrong above a jacket, a belt and a
pair of shoes. Fix is one line:

```liquid
<span class="eyebrow">{{ product.metafields.custom.fits_eyebrow | default: "Holds What Matters" }}</span>
```

Additive, defaulted, changes nothing on any page that does not set the new
metafield. **Needs the user's approval — pushing `kordovan` deploys live.**
