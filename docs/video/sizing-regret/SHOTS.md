# SHOTS — `sizing-regret`

**15.0 seconds · 5 shots · 0 FILM / 5 GENERATE · 9:16**

Every shot is generated. Clips land in `./raw/` named `shot01.mp4` … `shot05.mp4`.

**Generate every clip at the same settings:** 704 × 1280, **97 frames @ 24 fps** (4.04s).
Every shot below is shorter than that, so one render size covers the whole ad and
`assemble.sh` trims each clip from its head to the exact duration. Do not try to match
shot length in the generator — LTX wants frame counts of the form `8n + 1`, and fighting
that costs you a render.

If a duration changes here it must change in `captions.srt` **and** in the `DURS` array
in `assemble.sh`, or the captions drift off their pictures.

---

## Shared parameters — apply to all five shots

| | |
|---|---|
| Model | **LTX-2.3** (distilled / fp8 variant — the one that fits a 16GB T4) |
| Resolution | **704 × 1280** — LTX needs both dimensions divisible by 32, so 704 not 720 |
| Frames / fps | **97 @ 24 fps** = 4.04s per clip |
| Steps | **8** (distilled) · use **30** if running the full model |
| Guidance | **1.0** (distilled) · use **3.0** on the full model |
| VRAM | Enable VAE tiling and fp8 weights, or a T4 OOMs at 1280 |
| Wan2GP | Same prompts, resolution 704×1280, frames 97, everything else default |
| Upscale | **Leave at 704×1280.** `assemble.sh` upscales to 1080×1920 with lanczos — upscaling in the generator only burns VRAM |

Seeds are given per shot. They are fixed so a re-render after a copy change reproduces
the same picture instead of a new man in a new jacket.

---

## Shot 01 — September · GENERATE

| | |
|---|---|
| In / out | `00:00.0 → 00:03.0` |
| Duration | **3.0s** · Seed **310901** |

A warm evening. Jacket over a thin t-shirt, zipped, easy. Nothing is wrong yet — that is
the point. The caption is already mid-sentence.

**Caption:** `The jacket that fits you in September`

### Prompt — paste verbatim

```
A man in his early thirties seen from the collarbone down, wearing a plain dark brown
leather jacket zipped closed over a thin cotton t-shirt, standing still and relaxed on a
warm evening street, the camera makes one slow steady push in from waist height, 35mm
framing, vertical, cropped so that his face stays above the top edge of frame, low golden
evening sun raking along the street from frame left with long soft shadows and warm haze
in the air, palette of warm oatmeal, espresso brown, dusty terracotta and faded cream,
fine film grain with warm highlights and soft brown shadows with no blue in them, no
text, no graphics, no watermark, no logo
```

---

## Shot 02 — January · GENERATE

| | |
|---|---|
| In / out | `00:03.0 → 00:05.8` |
| Duration | **2.8s** · Seed **310902** |

Cold morning, breath in the air, a thick sweater underneath now. He pulls the two front
edges toward each other. The sentence completes.

**Caption:** `won't close in January.`

### Prompt — paste verbatim

```
A man seen from the collarbone down on a cold northern street at first light, wearing a
thick charcoal wool sweater underneath a plain unbranded slim dark brown leather jacket,
pulling the two open front edges of the jacket toward each other with both hands, the
camera holds locked off at chest height with no movement, 50mm framing, vertical, his
face cropped above the top edge of frame, flat cold overcast dawn light with no direct
sun and visible breath in the air, palette of muted cream, charcoal wool, espresso brown
leather and pale grey sky, fine film grain with warm brown shadows and no blue cast, no
text, no graphics, no watermark, no logo
```

---

## Shot 03 — the gap · GENERATE

| | |
|---|---|
| In / out | `00:05.8 → 00:08.6` |
| Duration | **2.8s** · Seed **310903** |

Tight on the closure. The two edges are held apart by the bulk of the knit. A hand tugs
once and lets go. That gap is the whole ad.

**Caption:** `One sweater is the whole difference.`

> ⚠️ **The jacket in this shot must stay anonymous** — no Kordovan detailing, no
> distinctive collar, no recognisable hardware. We are naming a category mistake, not
> staging our own product failing. If a render produces something that looks like a
> catalogue jacket, re-roll the seed.

### Prompt — paste verbatim

```
A tight vertical macro on the front closure of a plain unbranded slim leather jacket worn
over a thick ribbed wool sweater, the two front edges held apart by the bulk of the knit
with a clear gap between them, a hand tugging once at the lower edge and letting go, the
camera holds locked off with no movement, 85mm framing, very shallow depth of field, no
face anywhere in frame, soft flat overcast daylight falling from directly in front,
palette of espresso brown leather, charcoal knit wool and muted cream, fine film grain
with warm shadows and no blue in the blacks, no text, no graphics, no watermark, no logo
```

---

## Shot 04 — the resolve · GENERATE

| | |
|---|---|
| In / out | `00:08.6 → 00:11.4` |
| Duration | **2.8s** · Seed **310904** |

A well-cut jacket closed over a thick sweater, walking, comfortable. No strain at the
front.

**Caption:** `Made to order in Karachi.` / `Tell us there's a sweater under it.`

> 🔴 **Two binding constraints — see BRIEF.md.**
> 1. **No measurement beat.** No tape measure, no on-screen figures, no before/after
>    split, no "look, it closes" gesture. A staged proof would be fabricated evidence and
>    would have to be filmed instead. This is a man walking, and that is all it is.
> 2. **The caption is an offer the workshop must honour.** Confirm with the owner that a
>    chest-allowance request will actually be actioned at order time, and that whoever
>    answers WhatsApp knows to ask. If not, the caption drops to `Made to order in
>    Karachi.` alone.

### Prompt — paste verbatim

```
A man seen from the collarbone down walking slowly toward the camera on a cold pine-lined
northern road, wearing a well-cut warm brown leather jacket closed cleanly over a thick
cream wool sweater with no strain at the front, the camera tracks backward at a steady
walking pace at chest height, 35mm framing, vertical, his face out of frame above the top
edge, pale winter morning sun coming from behind him through mist and rim-lighting his
shoulders, palette of warm brown leather, cream wool, muted olive pine and soft grey
mist, fine film grain with warm highlights and espresso shadows with no blue in them, no
text, no graphics, no watermark, no logo
```

---

## Shot 05 — the close · GENERATE

| | |
|---|---|
| In / out | `00:11.4 → 00:15.0` |
| Duration | **3.6s** · Seed **310905** |

Wide, still, cold, quiet. He walks away into the mist and the jacket is the only warm
thing in the frame. The price and payment terms sit over the road in the lower third.

**Captions:**
- `11.4 → 13.2` — `From Rs 22,000.` / `Book with 50%, pay the rest to the rider.`
- `13.2 → 15.0` — `Free delivery nationwide.` / `Lifetime craftsmanship warranty.`

### Prompt — paste verbatim

```
An empty cold northern hill road in early morning mist with pine trees receding into grey
depth, a small back-turned figure in a warm brown leather jacket walking slowly away from
the camera into the haze, the camera holds locked off and lets him grow smaller, 24mm
wide framing, vertical, deep space with the figure small and centred and never turning
around, flat diffused mist light with a weak sun somewhere behind the trees, palette of
soft grey mist, muted olive pine, espresso brown and warm cream road dust, fine film
grain with warm shadows and no blue cast, no text, no graphics, no watermark, no logo
```

> The lower third of this frame is empty road. That is deliberate — it is the bed the
> closing text sits on, and it is the only part of the film where price appears.

---

## Timing table

| # | In | Out | Dur | Type | Seed |
|---|---|---|---|---|---|
| 01 | 00.0 | 03.0 | 3.0 | GENERATE | 310901 |
| 02 | 03.0 | 05.8 | 2.8 | GENERATE | 310902 |
| 03 | 05.8 | 08.6 | 2.8 | GENERATE | 310903 |
| 04 | 08.6 | 11.4 | 2.8 | GENERATE | 310904 |
| 05 | 11.4 | 15.0 | 3.6 | GENERATE | 310905 |
| | | **Total** | **15.0s** | 0 FILM / 5 GENERATE | |

Total generation load: **5 clips × 4.04s at 704×1280**. On a free Colab T4 with the
distilled model at 8 steps that is roughly 3–5 minutes a clip — the whole ad renders
inside one free session with room to re-roll a seed or two.

## Sound

Optional; the film is built to work muted. If you want a bed, use wind and distant birds
at low level — no music sting, no whoosh on the cuts. Drop it at `./audio/bed.m4a` and
`assemble.sh` picks it up; with no file it lays down silence at the correct AAC spec.

## Re-roll guidance

Generators fail in predictable ways here. Re-roll the seed rather than rewriting the
prompt when you see:

- **A face creeping into frame** at the top edge — the crop is the whole identity
  strategy. Push the framing tighter and re-roll.
- **Shot 03's jacket looking designed** — collar shapes, contrast zips, visible hardware.
  It must stay anonymous.
- **Blue shadows** in shots 02, 03 or 05. Cold weather tempts the model into a cool
  grade. Grey mist, warm shadows. Re-roll, and if it persists add "warm white balance"
  after the palette clause.
- **Hands with the wrong number of fingers** in shots 02 and 03 — the two shots that show
  hands. If two re-rolls do not fix it, tighten the framing until only the cuff and the
  jacket edge are in shot; the tug reads fine without the whole hand.
