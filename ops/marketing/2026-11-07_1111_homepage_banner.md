# 11.11 homepage banner: brief and final prompt (Omar / CEO, Nov 7 2026)

## Why it is built this way
- The homepage hero (`sections/hero-banner.liquid`) puts its own text on top of the image, on the **left side**: the headline
  "Built to Last. Made to Age.", plus the eyebrow, subheading, buttons and trust line. A darkening scrim sits behind it.
  So the image must keep the **left ~45% dark and empty**, or the two layers of text will clash.
- The image is shown with `object-fit: cover; object-position: center right`. On phones the left side is cropped away and the
  **right side stays visible**, so the sale text goes on the right.
- AI image tools often misspell long text. Keep the text in the image short and large. The details (dates, "no code needed",
  the link) go into the hero's own text boxes, which stay sharp on every screen.

## Final AI prompt (2560 × 1440, 16:9)
```
Wide 16:9 premium e-commerce hero banner for a Pakistani full-grain leather brand, photographic and editorial,
"quiet luxury" mood. Deep espresso-brown background (#241C16) with soft warm light. LEFT 45% of the frame: plain,
dark, completely empty (no objects, no text) so a website headline can sit there. RIGHT side: two full-grain
leather bifold wallets, one rich brown and one tan, resting on a dark walnut surface, lit by low golden side
light, visible stitching, realistic leather grain, shallow depth of field. Above the wallets on the right, large
elegant serif typography (like Fraunces), perfectly spelled, exactly these words and nothing else:
line 1, very large, cream colour (#F7F2EA): "11.11"
line 2, large, warm cognac-gold (#C08B5C): "25% OFF"
line 3, small spaced capitals, cream: "EVERY WALLET"
Clean, centred within the right half, generous margins, no other words, no logos, no watermark, no borders,
no badges, no people, no hands. Photoreal, high detail, 2560x1440.
```
Check before uploading: "11.11", "25% OFF" and "EVERY WALLET" are spelled exactly right, with no extra letters or words, and
the left side is empty. If the text comes out wrong, regenerate. Don't fix it by hand.

## Theme editor text (Online Store → Customize → Home → Hero)
| Field | Text |
|---|---|
| Hero image | the new banner, uploaded to Files |
| Eyebrow | 11.11 SALE · 8–12 NOVEMBER |
| Subheading | 25% off every wallet. 15% off everything else. No code needed. |
| Button 1 | Shop the sale → `/collections/kdv-wallets` |
| Button 2 | Shop everything → `/collections/all` |
The headline "Built to Last. Made to Age." is fixed in the code and stays as it is.

## Timing
- Go live just before midnight on **Nov 7**, so the banner and the sale prices land together.
- Put it back after **Nov 12, 11:59 PM**: restore the old hero image (`files/hero.png`) and clear or restore the four text fields.
