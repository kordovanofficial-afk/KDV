# 11.11 teasers: T1 "Something is being made" · T2 "Mark the date"

**Status: READY FOR CQRO** (L1 creative → CQRO → CEO → Founder; any paid use is L3 via the CRO).
Prepared Nov 1 2026 by the Creative Director for the CMO (Omar). Nothing has been uploaded, posted or spent.
**v2 (Nov 1):** CQRO note applied. T2 beat B no longer says "Once a year. Three days." (it would be false, because a Black Friday sale follows). It now reads **"10–12 November."** I chose this over "Three days only." because it is pure fact and carries no urgency.

## 1. Brief and reading taken
Cold top-of-funnel, about Nov 3–9, building recall of the date before the sale opens Nov 10 00:00 PKT.
- **No discount figure anywhere.** The reveal belongs to the sale creatives (C1–C4).
- **"Our biggest sale of the year" is NOT used.** Last year's WCM20 ran at 20% (CRO report Nov 1), which beats this year's 15% on non-wallets, so "biggest" can be contested for most of the catalogue. Both teasers say **"Our 11.11 sale"**.
- "11.11" **and** a date line are on screen **by 1.3 s** in both videos, and again on the end card.
- No Karachi, no rupees, no "was" price, no exclamation marks. No Razor photos and no card or ID imagery (§5).
- Every frame is a **real Shopify product photograph**: crop, scale, slow push-in, warm grade and a moving brass light only. Nothing generated, nothing retouched. `self_ai_disclosure` = **OPT_OUT**.
- **First 2 s carry no logo:** T1 opens on a crop of the Luke stitch line that keeps the embossed horse out of frame. T2 opens on type only.

## 2. T1 "Something is being made" (14 s)
Workshop mood on Espresso: macro crops of leather grain, stitching and a finished edge, slow push-ins, warm grade with shadows lifted to Espresso (never black), and a soft Antique Brass light sweeping across each shot. Craft first, then the date, then a quiet close.

| Time | Picture | On-screen text |
|---|---|---|
| 0.0–3.0 s | Luke (L4), right-hand stitch line, embossed mark out of frame, push-in | **"11.11"** (Fraunces, brass glint across it) + **"10–12 November"** (in by 1.3 s) |
| 3.0–5.5 | Aristocrat (A4), stitched corner and edge, push-in | "Something is being made." |
| 5.5–8.0 | Luke (L4), lower stitch row and grain | "Slowly, in our own workshop." |
| 8.0–10.6 | KODO (K4), embossed mark in Crazy Horse leather | "Leather. Thread. Time." |
| 10.6–14.0 | End card on Espresso, faint grain behind | **"11.11"** (large, brass glint) · Cognac underline · **"10–12 November"** · "kordovanleather.com" |

## 3. T2 "Mark the date" (12 s)
A bold type piece on Espresso with a Walnut glow. A huge "11.11" in Fraunces with a brass glint passing through the numerals, then one hero wallet (Bastion Tan) revealed by a widening pool of light.

| Time | Picture | On-screen text |
|---|---|---|
| 0.0–3.5 s | Type only | **"11.11"** (huge) · Cognac underline · **"Starts 10 November"** (in by 1.3 s) |
| 3.5–8.0 | Bastion Tan (BT1) revealed in a spotlight, slow push-in, brass sweep | "11.11" (small, top) · **"10–12 November."** · "Starts 10 November" |
| 8.0–12.0 | End card | "Mark the date." · **"11.11"** (huge) · underline · **"Starts 10 November"** · "Our 11.11 sale · kordovanleather.com" |

**Versionable date line:** "Starts 10 November" is true on every day from Nov 3 to Nov 9. To re-version it (for example, a Nov 9 cut), run:
`python3 teaser.py --only T2 --dateline "Starts tomorrow" --suffix _nov9`
⚠️ Stop the teasers by Nov 9 23:59 PKT. On Nov 10, "Starts 10 November" becomes stale.

## 4. Captions (primary text)
**T1 (English):** Something is being made in our own workshop. Our 11.11 sale runs 10–12 November. Mark the date.
**T1 (optional Roman Urdu line):** Hamare apne workshop mein kuch ban raha hai. 11.11 sale, 10 se 12 November.
**T2 (English):** Our 11.11 sale starts 10 November and runs to the 12th. Mark the date.
**T2 (optional Roman Urdu line):** 11.11 sale 10 November se shuru. Date yaad rakhiye.
**Headline (both):** 11.11 · 10–12 November
**Description:** Leather from our own workshop.
**CTA button:** Learn More (to the homepage; nothing is on sale until Nov 10, so not "Shop Now")
None of these carry a discount, a price, a code or urgency.

## 5. Photos used, and those deliberately excluded
Used (Shopify Files, same URLs as `../2026-11_1111_ad_creative.md` §2): **L4** Luke grain + stitching · **A4** Aristocrat grain/edge · **K4** KODO Crazy Horse emboss · **BT1** Bastion Tan front. Product names are never captioned, so the label-matches-image rule cannot be broken.
Excluded: every Razor shot (R1, R3, R4, RAB). Also excluded because they show a card, an ID or annotations: B2, B3, BT2, L2, L3, K1, K2, A3.
Note for the CQRO: K4 shows the word "Kordovan" embossed on the leather (8.0–10.6 s). It is our own product marking, not a third-party brand.

## 6. Music (optional; the videos are silent-safe and carry a silent AAC track)
A slow, low cello or felt-piano bed at about 60–70 BPM, a single soft piano note landing on each "11.11", and faint workshop room tone under T1. Use a licence-clear track from the YouTube Audio Library or Meta Sound Collection only, and record the track name when it is added in the Meta editor. No voiceover.

## 7. Files (`ops/marketing/teasers/`)
| File | Spec |
|---|---|
| `T1_something_is_being_made_9x16_14s.mp4` | 1080×1920, 14.0 s, 30 fps, H.264 yuv420p CRF 18, faststart, silent AAC 128k |
| `T1_something_is_being_made_4x5_14s.mp4` | 1080×1350, same |
| `T2_mark_the_date_9x16_12s.mp4` | 1080×1920, 12.0 s, same |
| `T2_mark_the_date_4x5_12s.mp4` | 1080×1350, same |
| `frames/*_t1.6s.jpg`, `*_t4.6s/6.5s.jpg`, `*_t13.2s/11.2s.jpg` | 3 frames per video, 12 in total, for review without a shell |
| `teaser.py` | rebuilds everything (Pillow + numpy + ffmpeg). Downloads the 4 photos into `_src/` if missing |
| `fonts/Fraunces-500.ttf` + `Fraunces-OFL.txt` | Fraunces Medium, SIL OFL. Inter comes from the system |
| `.gitignore` | ignores `_src/` (the cached product photos) |

## 8. CQRO checklist
- [ ] No % / rupee / "was" price / code in any frame or caption
- [ ] "11.11" and a date are legible on the t1.6s frames (thumbnail test)
- [ ] No Karachi, no exclamation marks, no "biggest"
- [ ] No card, ID, bank or card-network mark in any frame
- [ ] "Starts 10 November" is pulled or re-versioned before Nov 10
- [ ] T2 beat B reads "10–12 November." (CQRO note, v2)
