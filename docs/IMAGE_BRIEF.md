# Kordovan — Image Brief / Asset Manifest

Running list of every **designed** image the theme needs. For each slot:
**product/subject · GPT-image prompt · exact size (px) + aspect · where it goes · status.**
When an image is generated, drop it in and tick the status. Label/copy on a tile
must always match the image in it.

> **STYLE PREAMBLE — prepend to every prompt below:**
> *"Premium editorial product photography, Kordovan leather brand. Quiet Heritage
> palette: warm espresso & walnut browns, cognac, antique brass, alabaster cream.
> Full-grain leather with visible natural grain and hand-stitching. Soft warm
> directional light, deep rich shadows, shallow depth of field, heritage-luxury
> mood. No text, no logos, no brand marks, no watermarks."*

Generate at the listed pixel size (already 2× for retina). Save as `.jpg` (photos)
or `.png` (cutouts). Filenames: `slot-id.jpg` (e.g. `mega-wallets.jpg`).

---

## 1. Header — mega menu featured tiles
Display ~360×270; generated at 2×. Aspect **5:4**, size **1000 × 800 px**.

| ID | Product / subject | GPT prompt (after preamble) | Size |
|----|-------------------|------------------------------|------|
| `mega-wallets` ✅ | KODO RFID Smart Wallet (flagship) | DONE — `files/KODO.png` (embossed horse mark + local bank cards). | 1000×800 |
| `mega-jackets` ✅ | Men's leather jacket | DONE — `files/Jacket.png` (workshop, warm window light). | 1000×800 |
| `mega-bags` | Men's leather laptop/messenger bag | "A tan-brown full-grain leather messenger/laptop bag resting on a worn wooden bench beside a coiled strap; warm side light, espresso background, editorial still life." | 1000×800 |
| `mega-shoes` | Men's leather dress shoe | "A pair of dark-brown full-grain leather oxford dress shoes on a warm stone surface, one slightly forward, soft overhead warm light, polished grain, luxury editorial." | 1000×800 |
| `mega-accessories` | Small leather goods grouping | "An overhead arrangement of small leather goods — a belt coil, a cardholder, leather gloves and a cigarette case — in cognac and espresso tones on warm linen; tidy editorial flat-lay." | 1000×800 |

## 2. Homepage — hero background
Full-bleed. Aspect **16:9**, size **2560 × 1440 px**. Keep the **left third clear**
(negative space) for the headline.

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `hero-home` ✅ | Pakistani artisan hand-stitching leather | DONE — `files/hero.png`. (Prompt: warm Pakistani leather workshop, artisan saddle-stitching cognac Crazy-Horse full-grain leather, traditional tools, left third dark for headline, 16:9.) | 2560×1440 |

## 3. Homepage — brand story
Aspect **3:4** portrait, size **1000 × 1300 px**.

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `story-craft` ✅ | Artisan burnishing leather | DONE — `files/story-craft.png`. | 1000×1300 |

## 4. Homepage — collections grid
Large tile = **4:5** portrait **1200 × 1500**; medium tiles = **4:3** **1200 × 900**.

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `coll-wallets` (large) | Wallets category | "An arrangement of premium leather wallets in cognac and espresso tones standing and stacked on a warm stone surface; soft overhead warm light; full-grain texture; empty space at the bottom for a label." | 1200×1500 |
| `coll-bags` (med) | Bags category | "A full-grain leather messenger bag on a wooden bench in warm directional light, espresso background, editorial." | 1200×900 |
| `coll-belts` (med) | Belts category | "Several coiled full-grain leather belts in brown and tan tones arranged on warm linen, top-down, soft warm light." | 1200×900 |

---

## Notes
- **Product cards** (bestsellers, collection/product pages) use **real catalogue
  photos** already on Shopify — no generation needed there.
- These generated images are the **designed / styled** slots (hero, mega tiles,
  collection headers, brand story) — the "art-directed" layer.
- Once generated: upload in Shopify (theme editor / Files) or commit to
  `assets/`, then we wire them into the matching slot.
