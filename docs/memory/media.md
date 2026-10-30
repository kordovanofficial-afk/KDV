# Video and image generation: video book pointers, music, Higgsfield, Flow

> Moved verbatim from CLAUDE.md on Oct 30 2026 to cut per-session token load. Read on demand.

## 🎬 Video source of truth
- **`docs/video/VIDEO_BOOK.md`** — the core file for EVERY video (ads, Reels, films). Competitor map
  (Bellroy / Ridge / Ekster / Saddleback), the 5 pillars, shot vocabulary, light/surface rules, type,
  sound, 9 formats (F2 "It wears in" patina proof = flagship, our answer to Ridge's anti-leather ads),
  hook bank, jacket rules, shoot kit, edit rules, testing metrics, claims, QC. **Read it before any
  video work.** Rule #1 (Oct 26 2026, after a failed "Prada" film): editing cannot rescue footage —
  never edit from footage not shot for the video; AI voice / synthetic music are drafts only.
- **§15–18 (Oct 26 2026): the signature system.** 8 constants that never change at any product size,
  named zooms Z1–Z6, an approved/banned transition list, scale tiers S/M/L, sound licence verdicts, and
  viral mechanics done our way. Enforced by **`tools/video-edit/kv-kit/`** — 15 HyperFrames registry
  blocks + `kv-brand.css` (maps registry tokens → Quiet Heritage). Shareable page:
  `https://claude.ai/artifact/CcrQwqjptbK5YQJKDu9XiH` (copy at `docs/video/video-book.html`).
- 🔊 **Sound sources:** Openverse is built into `media-use resolve --type sfx` (CC0/CC BY only) — **ads
  use CC0 only** — ✅ user allowed `api.openverse.org` Oct 26 2026 — search works (slow, ~8 s/query). ⚠️ the audio files
  live on `cdn.freesound.org` + `upload.wikimedia.org`, STILL BLOCKED → downloads fail until those are allowed too.
  CC0 foley shortlist (12 cues, blocklisted junk) + downloader: `tools/video-edit/sound-kit/openverse/`.
  🔴 **Oct 26: user allowed cdn.freesound.org + upload.wikimedia.org — downloads STILL fail.** Freesound's CDN returns
  its OWN HTTP 403 to this cloud server's IP (the tunnel opens; referer/UA don't help); Wikimedia returns 429. Not
  fixable from network settings → the team downloads picks from SHORTLIST.md links and uploads them.
- 🎵 **MUSIC SOURCE THAT WORKS (Oct 26 2026): Hugging Face dataset `SoundSafari/Public-Domain-Music` (cc0-1.0,
  ~5,180 human-made instrumentals).** Download via `huggingface.co/datasets/SoundSafari/Public-Domain-Music/resolve/main/<file>`.
  Wikimedia (429, IP rate-limit), Freesound (403) and Jamendo (proxy-blocked, and CC BY anyway) do NOT work.
  I can't listen, so I pick by measured tempo, beat strength, brightness and spectrogram, then snap cuts to the beat grid.
  User expects music on every video ("dude, wheres the music") — never ship a brand video without it again.
- 🎙 **DIVISION OF LABOUR (user, Oct 26 2026):** user supplies ONLY footage + the voiceover recorded in that footage.
  **Claude does ALL transitions, zooms, text/captions, animations, titles, end cards, logo motion, grade, SFX, mix.**
  🔴 **Earshot is NOT cleared for ads**: only unofficial re-uploads exist, one marked CC BY-NC-ND.
  "Real SFX" not identified — need the URL. Owned foley kit list: `tools/video-edit/sound-kit/README.md`
  (`snap_brass_01` = the sonic logo on every end card).

## 🖼 HIGGSFIELD (connected Oct 29 2026) — free plan, 10 credits, ALL SPENT (0 left)
- Free plan blocks GPT Image 2.5 + Seedream 5.0 Pro ("Requires basic plan or higher"); only `marketing_studio_image`
  works (~2 credits per 1k image), and only 1 job at a time. Do not buy credits (FREE-only rule).
- 5 Mocha Mate ad stills made from the REAL Shopify product photos (job ids): 4:5 front `c8c97d86…` · 9:16 story
  `5c956a69…` · 1:1 gift box `2d28aa5c…` · 1:1 back/coin pocket `43d78264…` · 4:5 open `878cf57f…`.
  User OK'd the first one. The model can redraw details: every still must be checked against the real wallet before use.
- 🛑 **User (Oct 29–30): "dont add anything or create any ads with them" → use them as Instagram posts, NOT ads.** Approved stills = 1, 2, 3, 5, but NO ads were
  created and none should be without a new explicit request. Copies sit in Shopify Files only:
  `mm-ad-still-1-front-4x5.png`, `-2-story-9x16`, `-3-gift-1x1`, `-5-open-4x5` (not attached to any product).
- 📌 Oct 30: balance still 0 a day after spending, no reset offer → the free plan's 10 credits did NOT refill daily.

## 🎞 GOOGLE FLOW (Veo, free tier, used by hand) — tested Oct 30 2026
- No API/MCP for Flow; Google Cloud (Veo API trial) rejected every Pakistani card the user tried. Flow is manual only.
- Free credits: a Veo clip costs 20; the user had ~50 and spent 40 on 2 clips. Check whether it refills daily before planning.
- **Method that works:** upload the real product photo as the START frame, Agent OFF, Video 8 s 9:16 x1, and keep the
  background the same as the photo (asking for a different background makes Veo morph the product).
- Test 1 (Mocha Mate light sweep): shape, brass stud, stitching held, but colour drifted dark chocolate → copper
  (centre RGB 42→102) and the horse mark got redrawn. Test 2 added "stays the same dark chocolate brown… no extra shine,
  horse mark unchanged and no sharper": colour held (RGB 61→66), mark stable. ✅ PASS →
  `docs/video/flow-tests/mocha-mate-lightsweep-v2-PASS.mp4` (720p, usable as a beauty shot). Hands test not run yet.
