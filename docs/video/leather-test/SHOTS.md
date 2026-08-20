# SHOTS — `leather-test`

**22.0 seconds · 8 shots · 7 FILM / 1 GENERATE · 9:16**

Clips land in `./raw/` named `shot01.mp4` … `shot08.mp4`. Over-record every filmed shot
by ~2 seconds; `assemble.sh` trims from the head to the exact duration below. If a
duration changes here it must change in `captions.srt` **and** in the `DURS` array in
`assemble.sh`, or the captions drift.

---

## Shot 01 — the thumb press · FILM

| | |
|---|---|
| In / out | `00:00.0 → 00:03.2` |
| Duration | **3.2s** |
| Type | **FILM (evidentiary)** |

A dry thumb presses into the chest panel of the Iconic. The leather dishes under the
pressure and fine creases fan out from the contact point. The thumb lifts. The creases
relax and the surface comes back.

**Caption:** `Press it. Real leather springs back.`

**Phone note:** Jacket flat on a table beside a north-facing window, phone 20 cm away on
1x with focus and exposure locked by long-press on the panel, press with a dry thumb and
lift cleanly — hold 6 seconds, shoot 3 takes, daylight only, no lamp.

---

## Shot 02 — the same press, on plastic · FILM

| | |
|---|---|
| In / out | `00:03.2 → 00:05.8` |
| Duration | **2.6s** |
| Type | **FILM (evidentiary)** |

Identical press on a coated-PU swatch. It dents rather than dishes, and when the thumb
lifts the mark stays sitting there.

**Caption:** `Coated plastic keeps the crease.`

**Phone note:** Same table, same 20 cm distance, same locked exposure, swap in an
unbranded PU offcut with no logo, tag or stitching in frame — press and lift, hold 6
seconds.

---

## Shot 03 — the pore structure · FILM

| | |
|---|---|
| In / out | `00:05.8 → 00:08.8` |
| Duration | **3.0s** |
| Type | **FILM (evidentiary)** |

Macro drift across the grain. Pores scatter — different sizes, different spacing, a
faint healed scar running through. Nothing about it is regular.

**Caption:** `Look at the pores. No two are alike.`

**Phone note:** Turn the panel to about 30° from the window so the light rakes across and
the pores throw micro-shadows, then drift the phone 10 cm sideways in one slow continuous
move over 6 seconds — do not stop and restart.

---

## Shot 04 — the printed repeat · FILM

| | |
|---|---|
| In / out | `00:08.8 → 00:11.0` |
| Duration | **2.2s** |
| Type | **FILM (evidentiary)** |

Same drift on the PU swatch. The "grain" is a tile. Once the eye finds the repeat it
cannot unsee it.

**Caption:** `A printed grain repeats itself.`

**Phone note:** Identical setup to shot 03 — same 30° angle, same 10 cm drift, same 6
seconds — so the cut reads as a fair comparison and not a lighting trick.

---

## Shot 05 — inside the pocket · FILM

| | |
|---|---|
| In / out | `00:11.0 → 00:14.0` |
| Duration | **3.0s** |
| Type | **FILM (evidentiary)** |

The pocket turned out. The underside of real hide is fibrous, fuzzy, directionless
suede. Beside it, the PU swatch's back: a flat woven fabric mesh with a visible weave.

**Caption:** `Inside the pocket: fibre, not mesh.`

**Phone note:** Pocket turned out under the window with the PU swatch laid beside it,
phone close, tilt slowly from the fibrous suede across to the woven backing in one move
— hold 6 seconds.

---

## Shot 06 — the jacket · FILM

| | |
|---|---|
| In / out | `00:14.0 → 00:16.0` |
| Duration | **2.0s** |
| Type | **FILM (product)** |

The Iconic, worn and closed. Slow tilt up the front. Black, plain, uninterrupted — the
surface we have just spent fourteen seconds examining, now at full scale.

**Caption:** `Full-grain sheepskin.`

**Phone note:** Jacket worn, framed collarbone to hip so no face enters frame, phone at
chest height tilting slowly up the closed front over 6 seconds, north-facing daylight.

---

## Shot 07 — the workshop · GENERATE

| | |
|---|---|
| In / out | `00:16.0 → 00:18.0` |
| Duration | **2.0s** |
| Type | **GENERATE (atmosphere / place)** |

An empty workshop in warm light. Establishes place under the caption. **No people, no
hands, no garment, no leather** — the moment any of those appear the shot becomes
fabricated evidence of craft rather than an establishing shot. See BRIEF.md.

**Caption:** `Made to order in Karachi.`

### Prompt — paste verbatim

```
A quiet empty leather workshop interior in Karachi in the middle of the morning, a
scarred wooden cutting bench in the centre of the room with dust turning slowly in the
air above it, the camera makes one slow steady push in toward the bench, wide 24mm
framing, vertical, deep space back to a plain plaster wall where paper patterns hang on
nails, hard directional daylight from a single high window at frame left falling in a
shaft across the bench and dying into deep shadow at the edges of the room, palette of
warm oatmeal plaster, espresso brown timber, muted cream paper and aged brass, fine film
grain with warm highlights and soft brown shadows with no blue in them, no people, no
hands, no garments, no leather, no text, no graphics, no watermark, no logo
```

### Parameters

| | |
|---|---|
| Model | **LTX-2.3** (distilled / fp8 variant — the one that fits a 16GB T4) |
| Resolution | **704 × 1280** — LTX needs both dimensions divisible by 32, so 704 not 720 |
| Frames / fps | **97 frames @ 24 fps** = 4.04s, trimmed to 2.0s at assembly |
| Steps | **8** (distilled) · use **30** if running the full model |
| Guidance | **1.0** (distilled) · use **3.0** on the full model |
| Seed | **220117** |
| VRAM | Enable VAE tiling and fp8 weights, otherwise a T4 OOMs at 1280 |
| Wan2GP | Same prompt, resolution 704×1280, frames 97, everything else default |

**Upscale to 1080×1920 happens in `assemble.sh`** (lanczos) — do not upscale in the
generator, it wastes VRAM and softens the grain.

---

## Shot 08 — the close · FILM

| | |
|---|---|
| In / out | `00:18.0 → 00:22.0` |
| Duration | **4.0s** |
| Type | **FILM (product / text bed)** |

Locked off. The Iconic on a wooden hanger against a plain warm wall. Nothing moves. This
is the bed the price and payment terms sit on — the only 4 seconds of the film where
either appears.

**Captions:**
- `18.0 → 20.0` — `From Rs 22,000.` / `Book with 50%, pay the rest to the rider.`
- `20.0 → 22.0` — `Free delivery nationwide.` / `Lifetime craftsmanship warranty.`

**Phone note:** Same jacket on a wooden hanger against a plain warm wall, phone locked
off on a stack of books with absolutely no movement, record 8 seconds — keep the lower
third clean and uncluttered because the text lands there.

---

## Timing table

| # | In | Out | Dur | Type |
|---|---|---|---|---|
| 01 | 00.0 | 03.2 | 3.2 | FILM |
| 02 | 03.2 | 05.8 | 2.6 | FILM |
| 03 | 05.8 | 08.8 | 3.0 | FILM |
| 04 | 08.8 | 11.0 | 2.2 | FILM |
| 05 | 11.0 | 14.0 | 3.0 | FILM |
| 06 | 14.0 | 16.0 | 2.0 | FILM |
| 07 | 16.0 | 18.0 | 2.0 | **GENERATE** |
| 08 | 18.0 | 22.0 | 4.0 | FILM |
| | | **Total** | **22.0s** | 7 FILM / 1 GENERATE |

## Sound

Optional. The film is built to work muted — that is what the burned captions are for.
If you want a bed, use room tone from the workshop or the shot-08 setup, no music sting,
no whoosh transitions. Drop it at `./audio/bed.m4a` and `assemble.sh` picks it up
automatically; with no file it lays down silence at the correct AAC spec.
