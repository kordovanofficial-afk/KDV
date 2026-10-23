# Mocha Mate master v2 recipe
Run from a scratchpad `edit/` dir with ../vid-env, ../models, ../fonts, ../bin/deep-filter:
`python3 build_v2.py && python3 tighten.py && python3 build_v2b.py`
- Voice de-echo: DeepFilterNet 0.5.6 static binary from the official GitHub release (`deep-filter`), then EQ
  (−3dB @250Hz, +3dB @3.5kHz) + compressor + loudnorm.
- ⚠️ SYNC RULES (learned the hard way): snap every cut to the 1/30s frame grid; pad each piece's audio to its
  video duration before joining; never trust Whisper word gaps for jump cuts (they're contiguous) — use
  silencedetect −40dB on the DE-ECHOED voice (room echo hides pauses in the raw audio).
- Never `pkill -f <script>` from a Bash call whose own command line contains that name — it kills the shell.

## Cutdowns (Oct 24 2026)
`python3 make_cut.py 30s && CUT_OUT=cut_30s CUT_FILE=Mocha_Mate_30s_v2.mp4 python3 build_v2b.py` (same for 15s).
- 30s = H1 → S2 (pocket + key inserts) → S5 (patina + desk insert) → S8 from "sirf aur sirf 3,200" → end card 2.8s = 31.6s
- 15s = H1 → S5 "Real leather kabhi flake nahi karta…" (desk insert) → S8 "sirf aur sirf 3,200 rupay ka." → end card 2.6s = 14.1s
- Mid-scene cuts snap to real pauses (silencedetect −40dB on the de-echoed voice, ±0.45s).
- Loudness ~−16 LUFS integrated (Meta/IG normalise; fine).

## H3 variant + sync fix (Oct 24 2026)
- H3 ("honest review", clip 1490) replaces H1: `V_OUT=v2h3 V_SEGS=segments_h3.json python3 build_v2.py && ./fixaudio.sh v2h3 && V_OUT=v2h3 python3 tighten.py`
  then `CUT_OUT=v2h3 CUT_FILE=Mocha_Mate_Master_H3.mp4 python3 build_v2b.py`, cuts `30s_h3` / `15s_h3` with `CUT_SRC=v2h3`.
- Multi-range scenes use continuation ids (`S2~2`): no flash, headline held, inserts can anchor to them.
- ⚠️ NEVER cut audio with `aselect between(t,…)` — it works per ~21ms audio frame and drifts up to ~80ms over
  20 cuts. Use per-interval `atrim` + `concat` (sample-exact). After the fix: video == voice on all six outputs
  (H1 30s within 1 frame).
- ⚠️ Long hook titles overflow at 124px Fraunces — split onto two lines (`\N`) at ~104px.
- Final set delivered: Master/30s/15s × H1 (v2) and × H3.
