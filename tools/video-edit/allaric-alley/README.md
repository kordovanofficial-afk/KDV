# The Allaric Alley: 15s from one still (9:16)

This 15s vertical video is built from a single product photo. It follows the book's F6/Tier L tempo, using a "detail tour" format.

## Pipeline
1. **Upscale.** `assets/jacket.jpg` comes from the 1161×1355 source, run 4× through Real-ESRGAN general-x4v3 (BSD, LiteRT on CPU, about 45 s) and then downsized to 3000 px wide. This lets the close-ups go to about 3× without softening.
2. **Virtual camera.** `cam(cx, cy, z)` puts any point of the source photo at a frame position, so each detail is a hard-cut punch-in with a slow push centred on its hotspot.
3. **Shot list:**
   - macro hook "Worn in. On day one." (the only accent word);
   - Z3 reveal to the full jacket;
   - hotspot callouts: notch lapel collar, waist belt, zip pockets, then a match cut on the zip pull to the zip cuffs;
   - leather macro;
   - "Cut for one person." with the made-to-order terms;
   - warm fade-through to the end card.
4. **Sound.** `assets/sfx.wav` uses only the bundled Pixabay effects (whoosh-short, impact-bass-1, click-soft ×5, whoosh, plus a pitched click on the logo), normalised to −18 LUFS. Music is picked from Meta's Sound Collection at upload.

Every claim on screen comes from the product's live Shopify data.

Render with: `HYPERFRAMES_NO_TELEMETRY=1 npx hyperframes@0.8.195 render --quality delivery`
