# Mocha Mate stop-motion ad (15s, 9:16, original upbeat track + SFX)

The source is the Mocha Mate hand footage (`Img_1481/1483/1485/1487/1488.mp4`), which you can recover from git history at `d1f1f95~1:mocha-mate/`.
Do not use the founder clips 1495 and 1501: they show a different black wallet with an ID window, not the Mocha Mate.

Build steps:
1. `prep.sh` makes the 8 fps held-frame shots with per-frame jitter. The montage and the hero still are built separately; their ffmpeg commands are recorded in the session notes.
2. `python3 audio/track.py raw.wav && ffmpeg -i raw.wav -af "highpass=f=35,loudnorm=I=-13:TP=-1.2" assets/track.wav`
3. Copy `gsap.min.js` and the fonts into `assets/`.
4. Render with `npx hyperframes@0.8.195 render --quality delivery`.

The track is 120 BPM in F major and synthesised from scratch (no samples, no licence). It includes these effects: pop, boing, scratch, stamp thud, key jingle, click, ding and cha-ching.
The visual style is stop-motion: footage at 8 fps, a frame that jolts to a new angle on every cut, and stickers that pop on with `steps(3)` easing.
