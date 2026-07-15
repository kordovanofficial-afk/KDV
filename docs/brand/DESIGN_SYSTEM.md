# Kordovan — Brand Design System

> **Paste this whole file into Claude (or any AI/design tool) as context** before asking it to design anything for Kordovan. It is the single source of truth for look, feel, and components — distilled from the live theme.
>
> **One-line brief:** *Kordovan is a Pakistani full-grain leather house — “heirloom leather, handmade in Pakistan, built to be handed down.”* Every design choice should feel **considered, warm, and permanent** — quiet luxury, never loud or discount-driven.

Design language name: **“Quiet Heritage.”**

---

## 1. Core principles (the feel)

1. **Warm, never clinical.** Cream/parchment canvases — never stark white (#FFFFFF) backgrounds.
2. **Editorial restraint.** Generous whitespace, few elements per view, calm motion.
3. **Leather is the hero.** Big, warm, textural photography; UI stays quiet around it.
4. **Heritage as premium.** “Made in Pakistan” is a mark of pride, not a discount cue.
5. **Trust is structural.** Warranty, reviews, COD, “genuine leather” — shown, not decorated.

**Colour balance per screen (rule of thumb):** ~70% Alabaster/Parchment · ~20% Espresso/Walnut · ~8% Cognac/Tan · ~2% Brass (+ optional Olive).

---

## 2. Colour tokens

Use these exact values. Names map to CSS variables used in the build.

### Core (backgrounds & text)
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--canvas` | Alabaster | `#F7F2EA` | Primary background (warm cream) |
| `--parchment` | Parchment | `#ECE3D4` | Secondary surfaces, alternating sections, cards on dark |
| `--ink` | Espresso | `#241C16` | Primary text + dark sections (warm near-black) |
| `--walnut` | Walnut | `#4A3528` | Secondary text, deep brown panels |

### Signature (the brand accents)
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--cognac` | Cognac | `#A0623A` | **THE brand colour** — primary CTAs, links, key accents |
| `--cognac-dark` | Cognac Dark | `#7E4B2C` | CTA hover / pressed |
| `--tan` | Saddle Tan | `#C08B5C` | Highlights, secondary accents |
| `--brass` | Antique Brass | `#B0894F` | Fine details, dividers, eyebrow labels, stars |
| `--brass-light` | Light Brass | `#D8C39A` | Accents on dark backgrounds (text on espresso) |

### Supporting & feedback
| Token | Name | Hex | Use |
|-------|------|-----|-----|
| `--stone` | Stone/Taupe | `#8B8174` | Muted text, captions, meta |
| `--border` | Border | `#DDD2C0` | Hairline borders, card edges |
| `--olive` | Heritage Olive | `#5A5A3C` | Sparing “thread” accent (≤5% of a screen) |
| `--pine` | Deep Pine | `#2D6A4F` | Success / verified / in-stock |
| `--oxblood` | Oxblood | `#8B2D2D` | Error / sale / sold-out |

**Don’ts:** no pure white backgrounds; no cool greys/blues; brass is for borders & small accents, **not** body text on light.

---

## 3. Typography

**Heading font:** **Fraunces** (variable serif — soft, editorial, heritage). Weights 400, 500, 600 + *italic 400/500*.
**Body / UI font:** **Inter**. Weights 300, 400, 500, 600.
Fallbacks: Fraunces → `Georgia, serif`; Inter → `-apple-system, sans-serif`.

| Role | Font / weight | Size (clamp) | Notes |
|------|---------------|--------------|-------|
| Display / hero H1 | Fraunces 500 | `clamp(40px, 6vw, 76px)` | line-height ~1.0–1.1, letter-spacing −0.02em. Italic for emphasis word. |
| Page title H1 | Fraunces 500 | `clamp(34px, 5vw, 58px)` | |
| Section H2 | Fraunces 500 | `clamp(28px, 3.4vw, 46px)` | letter-spacing −0.01em |
| H3 | Fraunces 500 | 18–24px | |
| Lead paragraph | Fraunces 400 | `clamp(20px, 2.4vw, 27px)` | line-height 1.5; emphasis word in cognac italic |
| Body | Inter 300–400 | 15–17px | line-height 1.7–1.85; color `--walnut` |
| Small / meta | Inter 400 | 12–13px | color `--stone` |
| **Eyebrow** (kicker) | Inter 500–600 | 11px | UPPERCASE, letter-spacing 0.16–0.18em, color `--brass` (or `--cognac` on PDP) |
| Button label | Inter 500–600 | 13–14px | UPPERCASE, letter-spacing 0.04–0.08em |

**Pattern — section header:** small **eyebrow** (brass, uppercase) → **H2** (Fraunces) → optional one-line subhead (walnut). Centered for marketing sections; left-aligned for editorial/PDP.

---

## 4. Spacing, radius, shadow, layout

- **Spacing scale (px):** 4 · 8 · 12 · 16 · 20 · 24 · 30 · 40 · 56 · 72 · 90 · 104. Section vertical padding 90–104px desktop, ~60–68px mobile.
- **Container width:** max 1180–1340px, side padding 40px desktop / 20px mobile.
- **Radius:** small 5–8px (buttons, chips, inputs) · medium 10–14px (cards, images) · pill 99px (filter pills, badges) · circle 50% (icon buttons, swatches).
- **Borders:** 1px `--border` hairlines.
- **Shadows (warm, soft, never grey):**
  - Card: `0 14px 36px rgba(36,28,22,.06)`
  - Raised image: `0 24px 60px rgba(36,28,22,.18)`
  - Header on scroll: `0 1px 14px rgba(36,28,22,.08)`
- **Grids:** product grid 3-col desktop / 2-col mobile; editorial splits 1fr 1fr with 60–80px gap.

---

## 5. Components (specs)

### Buttons
| Variant | Fill | Text | Use |
|---------|------|------|-----|
| **Primary (cognac)** | `--cognac` → hover `--cognac-dark` | #fff | Add to cart, checkout, primary CTA. Full-width on mobile. **Never grey.** |
| **Dark** | `--ink` → hover `--walnut` | `--canvas` | Secondary solid (e.g. on cognac bands) |
| **Ghost** | transparent, 1px border rgba(247,242,234,.55) | `--canvas` | On dark/hero imagery |
| **Outline** | transparent, 1px `--ink` → hover fills ink | `--ink`→cream | Secondary on light |
| **Text link** | underline 1px cognac | `--cognac` | “Read more →”, inline CTAs |

Button shape: padding ~16px 30px, radius 5–7px, uppercase label, 0.2–0.25s transitions.

### Cards
- **Product card:** image in 4:5 rounded container (`--border`, bg #fff); on hover → image scales 1.05 + reveal **Quick Add** (cognac bar). Below: Fraunces name (ink), cognac price, brass ★ rating, optional colour swatch dots + “N colours”. Badges top-left: Bestseller/New (`--ink`/brass-light), Sale (`--oxblood`), Sold Out (`--stone`).
- **Content card:** `--canvas`/#fff, 1px border, radius 12px, 34px padding; optional thin-line cognac icon (42px), Fraunces H3, walnut body.

### Badges & chips
- Eyebrow badge: ink bg, brass-light text, 9–10px uppercase, radius 3px.
- Filter pill: 1px border, radius 99px, hover border stone, active = ink fill + cream text.
- Trust chip: parchment bg, 1px border, pill, cognac line-icon + walnut label.

### Inputs
- 1px `--border`, radius 6–8px, padding ~14–16px, bg #fff (or rgba(247,242,234,.08) on dark); focus border `--cognac`. Inter 15px.

### Header / nav
- Announcement bar: espresso bg, cream text, 11.5px uppercase, brass-light bold.
- Header: cream, sticky; logo (Fraunces, letter-spacing 0.16em, or the horse mark) left; uppercase nav center (12px, 0.12em); search/account/cart icons right (thin-line, 1.4 stroke). Shrinks on scroll.

### Icons
Thin-line, single weight (stroke ~1.4–1.8, no fill), espresso or cognac. No clip-art, no filled glyphs except brand/social marks.

### Motion
- Transitions 0.2–0.35s, ease/cubic-bezier(.25,.46,.45,.94).
- Hover: image scale 1.05–1.06; CTA bg shift; link arrow nudges 4px.
- Continuous marquees (trust bar, reviews) at slow linear speed, **pause on hover**.
- Keep it calm — no bounce, no fast/flashy.

---

## 6. Imagery direction

- **Warm, textural, real.** Full-grain leather with visible grain & hand-stitching, on wood/linen/stone.
- **Colour temperature ~5000K** (warm-neutral); true cognac/brown tones; never cool/blue, no heavy filters.
- **Catalog backgrounds:** seamless Alabaster `#F7F2EA` or Parchment `#ECE3D4` — not pure white.
- **Lighting:** soft key from upper-left, gentle fill, soft contact shadow.
- **Product shot order:** 1) flat-lay/front · 2) in-hand for scale · 3) open/inside · 4) texture macro · 5) lifestyle.
- **Hero:** full-bleed real leather/workshop photo, dark scrim on the text side, one headline + one primary + one soft CTA.

---

## 7. Logo & marks

- **Mark:** black horse-head silhouette (registered trademark — brand-owned; never re-trace or reuse outside Kordovan).
- Solid black mark auto-inverts to cream over dark/hero headers (CSS filter). Needs a **transparent-background** PNG.
- Wordmark: “KORDOVAN” in Fraunces 600, uppercase, letter-spacing ~0.16em.

---

## 8. Voice & tone

- **Confident, warm, understated.** Heritage + permanence, not hype.
- Benefit-first, plain language; specs in tabs, not walls of text.
- Recurring lines: *“Built to Last. Made to Age.”* · *“Leather, built to be handed down.”* · *“Genuine leather guaranteed.”*
- Avoid: exclamation-heavy hype, “cheap”, aggressive discount language, emoji clutter (a single 🐎/🇵🇰 is fine sparingly).

---

## 9. Quick copy-paste tokens (CSS)

```css
:root{
  --canvas:#F7F2EA; --parchment:#ECE3D4; --ink:#241C16; --walnut:#4A3528;
  --cognac:#A0623A; --cognac-dark:#7E4B2C; --tan:#C08B5C; --brass:#B0894F;
  --brass-light:#D8C39A; --stone:#8B8174; --border:#DDD2C0;
  --olive:#5A5A3C; --pine:#2D6A4F; --oxblood:#8B2D2D;
  --font-heading:'Fraunces',Georgia,serif;
  --font-body:'Inter',-apple-system,sans-serif;
}
```
Google Fonts: `Fraunces:ital,opsz,wght@0,9..144,400;0,..,500;0,..,600;1,..,400;1,..,500` + `Inter:wght@300;400;500;600`.

---

*Kordovan · Est. 2020 · Handcrafted in Pakistan. Keep it quiet, warm, and built to last.*
