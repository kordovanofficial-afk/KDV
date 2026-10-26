# Kordovan heritage film (15s, 9:16, luxury "fashion house" style, voiceover)

**Voiceover** is generated with Kokoro-82M, run locally through `pip install kokoro-onnx`.
- Kokoro is Apache-2.0, so commercial use is free.
- Voice `bm_george` (deep British male) at 0.82 speed, with a 5% pitch drop and a touch of room echo applied in ffmpeg.
- Lines: "Leather remembers." / "Every road. Every year." / "Cut by hand. Made to be kept." / "Kordovan."
- The engine phonemises Kordovan as /kˈɔːdəvˌan/, stressed on the first syllable.
- Model files come from github.com/thewh1teagle/kokoro-onnx releases (`model-files-v1.0`).

**Footage** is the Mocha Mate hand clips. `prep.sh` makes macro crops with 0.6x optical-flow slow motion (minterpolate), a crushed-shadow warm grade, a vignette and film grain.

**Score** (`audio/score.py`) is synthesised from scratch: a bowed D-minor drone, sparse felt piano, and a sub swell into a low hit on the logo. The voiceover is ducked over it.

Render with `npx hyperframes@0.8.195 render --quality delivery`.

Never mention Karachi in any line.
