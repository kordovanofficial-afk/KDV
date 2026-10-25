# Kordovan teaser v2 (16s, 9:16, with original score)

HyperFrames project (skills in `.claude/skills/hyperframes*`). Footage, fonts, gsap and the score live in `assets/`. They are not committed (~15MB).

Build `assets/`:
1. Put `src/IMG_1481.MOV`, `src/IMG_1483.MOV` and `src/IMG_1485.MOV` next to `prep.sh`. Recover them from git history with `git show <commit>:mocha-mate/originals/IMG_<n>.MOV`.
2. Put the fonts in `../fonts/`.
3. Run `prep.sh`. It makes 5 beat-cut shots: pair, hold, snap, open and keys.
4. Copy `gsap.min.js` into `assets/` (from `npm pack gsap@3.14.2`).
5. Build the score: `python3 audio/score.py raw.wav && ffmpeg -i raw.wav -af "highpass=f=32,loudnorm=I=-14:TP=-1.5" assets/score.wav`

About the score:
- It is synthesised from scratch in numpy: no samples and no licence, so it is safe for paid ads.
- It runs at 120 BPM in D minor. Whooshes land on every cut, a riser builds into the 8.0s "It ages." drop, and a boom plus bells sit under the 11.0s logo draw.

Render with:
`npx hyperframes@0.8.195 render --quality delivery --output Kordovan_Teaser_v2_16s.mp4`

Copy rule: **never mention Karachi** (user, Oct 25 2026).

The logo sting lives in `../logo-sting/`:
- It is 5s at 1080x1080. Its audio is the score from 11.0–16.0s.
- `trace.py` vectorises the logo PNG with potracer.
- For 9:16, pad onto `#241C16` with ffmpeg.
