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
Goal: reflect **Kordovan's actual products** (not generic AI goods). Large flagship
tile = **portrait ~6:7, 1200 × 1400**; the four small tiles = **~square, 1000 × 900**.
Images are cover-cropped, so keep the subject centred with a little breathing room.
**Status: all 5 placed ✅** — `files/coll-wallets|bags|jackets|shoes|belts.png`.

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `coll-wallets` (large) | Wallets (flagship) | "An elegant angled-overhead arrangement of several Kordovan full-grain leather wallets — a slim bifold, a minimalist cardholder, and an RFID elastic-band smart wallet — in cognac, dark brown and black Crazy-Horse leather, fanned on a warm walnut-wood surface with a couple of cards peeking out; soft directional window light raking the grain, deep espresso shadows; vertical composition with calm space at the bottom for a label." | 1200×1400 |
| `coll-bags` | Bags | "A styled still life of Kordovan full-grain leather bags — a structured women's tote beside a men's leather messenger/laptop bag — in tan and chocolate brown on a warm linen-and-wood surface; soft warm light, visible grain and hand-stitching; premium editorial." | 1000×900 |
| `coll-jackets` | Jackets | "A men's leather cafe-racer / biker jacket in rich brown sheepskin on a wooden hanger against a warm, moody workshop wall; soft side light catching the grain, zips and stitching; masculine, heritage, premium." | 1000×900 |
| `coll-shoes` | Shoes | "A pair of Kordovan brown full-grain leather oxford/brogue dress shoes, angled on a warm stone surface, a loafer hinted softly behind; polished grain, soft overhead warm light, deep shadows; refined menswear editorial." | 1000×900 |
| `coll-belts` | Belts | "Two or three Kordovan full-grain leather belts — one coiled, one laid straight — in tan, brown and black with brushed-metal buckles, on warm linen; top-down, soft warm light, crisp grain and double-stitching." | 1000×900 |

---

## Notes
- **Product cards** (bestsellers, collection/product pages) use **real catalogue
  photos** already on Shopify — no generation needed there.
- These generated images are the **designed / styled** slots (hero, mega tiles,
  collection headers, brand story) — the "art-directed" layer.
- Once generated: upload in Shopify (theme editor / Files) or commit to
  `assets/`, then we wire them into the matching slot.
