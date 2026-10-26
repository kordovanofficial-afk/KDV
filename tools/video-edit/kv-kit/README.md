# kv-kit: the Kordovan motion kit

This kit holds the approved HyperFrames blocks, branded through one token file. The rules for when to use each block are in `docs/video/VIDEO_BOOK.md` §15–§16.

## Use it in a new video
1. Copy `kv-brand.css` and the blocks you need from `compositions/` into the new project.
2. Link `kv-brand.css` **after** each block's own styles. Every block reads the shared tokens (`--bg`, `--fg`, `--brand`, `--accent`, `--font-display` …), so colours, fonts and eases become Quiet Heritage automatically.
3. Copy the font files into the project's `assets/fonts/`: Fraunces.woff2, Inter.woff2, and NotoNastaliqUrdu.woff2 for Urdu script only. Never load fonts from the network at render time.
4. Run `npm run check`, then snapshot before rendering.

## Installed blocks (HyperFrames 0.8.195 registry)
| Block | Book code | Allowed in |
|---|---|---|
| `match-cut`, `text-match-cut` | match cut | all tiers |
| `cut-the-curve` | velocity cut | hooks |
| `fade-through` | warm fade-through (espresso wash) | time jumps, end card |
| `organic-light-leak-overlay` | light leak (warm only) | Tier L, max 1 |
| `editorial-flash-overlay` | editorial flash | launches, max 1 |
| `iris-reveal` | inside or pocket reveal | F5 only |
| `beat-freeze-cut` | Z5 speed ramp + freeze | Tier S |
| `camera-dolly-zoom` | Z4 dolly zoom | jackets, once |
| `kinetic-center-build` | headline build | headlines ≤ 5 words |
| `inline-highlight` | cognac underline on the accent word | all |
| `caption-weight-shift`, `caption-editorial-emphasis` | house captions | all |
| `logo-brand-close` | end-card lockup (swap in the horse mark) | all |
| `grain-overlay` | ≤ 3% on type cards and end cards only | all |

Add more blocks with `npx hyperframes@0.8.195 add <name>` (the catalogue is reachable from the cloud session). Never add the glitch, chromatic, pixelate, vortex, VHS or 3D-flip blocks (book §15.2).

## Sound
- Openverse SFX: `npx hyperframes media-use resolve --type sfx --intent "leather creak" --project .` It returns CC0 or CC BY only and writes `assets/sfx/CREDITS.md`. **Ads use CC0 only.** It needs `api.openverse.org` allowed in the environment network settings.
- Our own foley goes in `../sound-kit/` (book §17.1).
