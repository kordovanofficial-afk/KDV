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

## 5. Optional — email-capture background
The email band currently uses a CSS gradient (looks good as-is). Optionally add a
subtle dark leather texture behind it. Wide full-bleed band.

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `email-leather-bg` *(optional)* ✅ | Dark full-grain leather texture | PLACED in mockup — `files/email-leather-bg.png` (dark overlay on top for legibility). Final decision on shipping it to the theme: TBD. | 2400×1000 |

| ID | Subject | GPT prompt (after preamble) | Size |
|----|---------|------------------------------|------|
| `coll-wallets` (large) | Wallets (flagship) | "An elegant angled-overhead arrangement of several Kordovan full-grain leather wallets — a slim bifold, a minimalist cardholder, and an RFID elastic-band smart wallet — in cognac, dark brown and black Crazy-Horse leather, fanned on a warm walnut-wood surface with a couple of cards peeking out; soft directional window light raking the grain, deep espresso shadows; vertical composition with calm space at the bottom for a label." | 1200×1400 |
| `coll-bags` | Bags | "A styled still life of Kordovan full-grain leather bags — a structured women's tote beside a men's leather messenger/laptop bag — in tan and chocolate brown on a warm linen-and-wood surface; soft warm light, visible grain and hand-stitching; premium editorial." | 1000×900 |
| `coll-jackets` | Jackets | "A men's leather cafe-racer / biker jacket in rich brown sheepskin on a wooden hanger against a warm, moody workshop wall; soft side light catching the grain, zips and stitching; masculine, heritage, premium." | 1000×900 |
| `coll-shoes` | Shoes | "A pair of Kordovan brown full-grain leather oxford/brogue dress shoes, angled on a warm stone surface, a loafer hinted softly behind; polished grain, soft overhead warm light, deep shadows; refined menswear editorial." | 1000×900 |
| `coll-belts` | Belts | "Two or three Kordovan full-grain leather belts — one coiled, one laid straight — in tan, brown and black with brushed-metal buckles, on warm linen; top-down, soft warm light, crisp grain and double-stitching." | 1000×900 |

---

## 6. Content page — Our Story (About) — `page-about.html`
Top-to-bottom image slots. Header = logo only (no image). Stats band, value
cards (line icons) and the cognac CTA band are intentionally image-free.

| ID | Where on page | Prompt (after preamble) | Aspect / Size |
|----|---------------|--------------------------|---------------|
| `about-hero` | Full-bleed hero behind "Built to be handed down." Keep **lower-left third calm/shadowed** for the headline. | "A wide, cinematic view inside a warm Pakistani leather workshop — a craftsman at a worn wooden bench saddle-stitching a cognac full-grain wallet, coils of leather, brass tools and thread spools around him, dust catching low golden window light from the left, deep espresso shadows filling the right and lower-left; documentary heritage mood, photoreal, shallow depth of field." | 16:9 · 2560×1440 |
| `about-origin` | Left image — "It started with a belief." | "A close still life of three well-used full-grain leather wallets in cognac, chocolate and black, fanned on a warm walnut surface, edges softened and surfaces glowing with years of patina, a couple of worn bank cards peeking out; raking warm window light revealing grain and hand-stitching, calm negative space top-left; intimate, nostalgic, premium editorial." | 4:5 · 1200×1500 |
| `about-craft-teaser` | Right image — "From hide to stitch, by hand." | "Over-the-shoulder shot of an artisan's hands finishing a rich brown leather jacket on a workbench — pressing a seam, waxed thread and a stitching pony in frame, soft warm side light, blurred warm workshop behind; tactile, human, heritage-luxury, photoreal, shallow depth of field." | 4:5 · 1200×1500 |
| `about-promise-bg` | Dark background behind the warranty pillar (dark overlay sits on top). May reuse `email-leather-bg` instead. | "A full-frame macro of dark espresso full-grain leather — deep natural grain, subtle scarring, a single line of hand-stitching crossing one corner, dramatic low side light, rich shadows; luxurious, masculine, near-monochrome brown texture suitable as a darkened background." | wide · 2400×1100 |

> Briefs for Our Craft / Shipping / Leather Care / Returns pages: TBD (doing them
> one page at a time per the user's request — About first).

---

## Notes
- **Jackets have their own sheet.** Per-jacket, per-shot prompts for all 30
  jackets live in **`docs/images/JACKETS_SHOT_SHEET.html`** (open it in a
  browser — 150 copy buttons, progress saved locally). It supersedes the generic
  "Jackets & Coats" rows in `shot-sheet.html`, which gave every jacket the same
  category prompt. Regenerate with `python3 tools/jacket-shotsheet/build.py`;
  the per-jacket art direction is editable in `tools/jacket-shotsheet/jackets.py`.
- **Product cards** (bestsellers, collection/product pages) use **real catalogue
  photos** already on Shopify — no generation needed there.
- These generated images are the **designed / styled** slots (hero, mega tiles,
  collection headers, brand story) — the "art-directed" layer.
- Once generated: upload in Shopify (theme editor / Files) or commit to
  `assets/`, then we wire them into the matching slot.

---

## Blog — Top 10 Leather Jacket Brands in Pakistan (2026)
`/blogs/jackets/top-10-leather-jacket-brands-in-pakistan` · briefed Aug 9 2026

Five slots. Shoot or generate, then upload to **Shopify → Content → Files**
using the exact filenames below so they can be pulled and placed automatically.

**House style for all five (Quiet Heritage):** natural daylight, matte finish,
no gloss or specular highlights, muted palette — Alabaster `#F7F2EA`,
Parchment `#ECE3D4`, Espresso `#241C16`, Walnut `#4A3528`, Cognac `#A0623A`.
Editorial, restrained, heritage-menswear magazine. **No text, no logos, no
watermarks.** JPG, sRGB, under 300 KB each after export.

---

### 1 · Header image
**File:** `blog-jackets-hero.jpg` · **1600 × 900** (16:9)
**Placement:** top of article, above the disclosure box
**Alt text:** `Three genuine leather jackets — biker, bomber and cafe racer — laid flat on linen`

> Editorial product photograph, flat overhead composition. Three genuine leather jackets laid slightly overlapping on a warm alabaster linen backdrop: a black sheepskin biker jacket with asymmetric zip, a dark brown bomber with ribbed cuffs, and a deep espresso cafe racer with a band collar. Soft directional daylight from the upper left, long gentle shadows. Matte leather, visible natural grain and stitching detail, no gloss. Muted palette of espresso brown, black and cognac against cream linen. Quiet, premium, understated heritage-menswear editorial styling. No text, no logos, no people. Medium format, 50mm, f/5.6, natural light.

---

### 2 · Leather grain macro
**File:** `blog-jackets-grain-macro.jpg` · **1400 × 900** (14:9)
**Placement:** inside "How to check the leather yourself", after the intro line
**Alt text:** `Close-up of genuine sheepskin leather grain showing irregular natural pores`

> Extreme macro photograph of genuine sheepskin leather surface, filling the frame. Irregular natural grain with visible pores of varying size and spacing, subtle tonal variation across the hide, a soft natural crease running diagonally. Deep walnut brown. Raking side light from the left to bring out the texture in relief. Matte, no sheen. Shallow depth of field falling off toward the edges. Photographic realism, no illustration, no text. 100mm macro lens, f/4.

---

### 3 · The four jacket styles
**File:** `blog-jackets-four-styles.jpg` · **1600 × 900** (16:9)
**Placement:** inside "Which style should you buy?", above the list
**Alt text:** `Four leather jacket styles compared — biker, bomber, cafe racer and vintage distressed`

> Four-panel grid, equal quarters separated by thin cream dividers. Each panel shows one leather jacket photographed straight-on against a plain parchment backdrop, identical lighting and framing across all four: (1) black biker jacket with asymmetric zip and belted waist, (2) brown bomber jacket with ribbed collar, cuffs and hem, (3) black cafe racer with minimal band collar and centre zip, (4) vintage distressed brown jacket with worn, faded finish. Soft even daylight, matte leather, no gloss. Consistent scale and centring so the silhouettes can be compared. No text, no labels, no people, no hangers visible.

---

### 4 · The workshop
**File:** `blog-jackets-workshop.jpg` · **1400 × 900** (14:9)
**Placement:** inside the "1. Kordovan" section, after the first paragraph
**Alt text:** `Leather jacket panels being cut and stitched by hand in a Karachi workshop`
**Why it matters:** this is the credibility image. A real workshop photo of your
own bench beats anything generated — **prefer a real one if you can take it.**

> Documentary photograph of a leather workshop bench. Hands of a craftsman guiding a panel of brown sheepskin leather under an industrial sewing machine, mid-stitch. Cutting patterns, a steel rule, chalk marks and thread spools on a worn wooden surface around it. Warm natural window light from the side, dust visible in the air. Muted, unstyled, honest — a working room rather than a set. Espresso and walnut tones with cream daylight. Face not visible. No text, no logos. 35mm, f/2.8, natural light, slight grain.

---

### 5 · Winter layering
**File:** `blog-jackets-winter-layering.jpg` · **1400 × 900** (14:9)
**Placement:** inside "Buying for a Pakistani winter"
**Alt text:** `Brown leather jacket worn over a knit sweater showing room for winter layering`

> Editorial lifestyle photograph, waist-up, shot from the side and slightly behind so the face is not visible. A man wearing an open dark brown leather jacket over a thick cream wool sweater, collar turned up, on a cold overcast morning. Soft flat winter daylight, muted background of a blurred street with warm stone tones. Focus on how the jacket sits over the knit — room across the chest and shoulders. Matte leather, natural fall of the fabric. Understated, documentary, not a fashion pose. No text, no logos, no visible branding.

---

### After upload
Tell me they are in Files and I will pull the CDN URLs and place all five in
the article with the alt text above, plus add the header image to the
`BlogPosting` schema `image` property (currently omitted because none existed).
