# Mocha Mate master v2 recipe
Run from a scratchpad `edit/` dir with ../vid-env, ../models, ../fonts, ../bin/deep-filter:
`python3 build_v2.py && python3 tighten.py && python3 build_v2b.py`
- Voice de-echo: DeepFilterNet 0.5.6 static binary from the official GitHub release (`deep-filter`), then EQ
  (−3dB @250Hz, +3dB @3.5kHz) + compressor + loudnorm.
- ⚠️ SYNC RULES (learned the hard way): snap every cut to the 1/30s frame grid; pad each piece's audio to its
  video duration before joining; never trust Whisper word gaps for jump cuts (they're contiguous) — use
  silencedetect −40dB on the DE-ECHOED voice (room echo hides pauses in the raw audio).
- Never `pkill -f <script>` from a Bash call whose own command line contains that name — it kills the shell.
