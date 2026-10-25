# Video edit toolkit (free, local)

Used for founder/UGC video edits. Everything runs in the session container, so no paid tools.

## Setup (fresh container, ~3 min)
```bash
S=<scratchpad>
python3 -m venv $S/vid-env && $S/vid-env/bin/pip install -q faster-whisper
# Fonts (brand): Google Fonts CSS → static TTF (raw.githubusercontent is blocked)
mkdir -p $S/fonts; for spec in "Inter:wght@700" "Fraunces:wght@600"; do
  url=$(curl -sS -A "Mozilla/4.0" "https://fonts.googleapis.com/css2?family=$spec" | grep -o "https://fonts.gstatic.com[^)]*" | head -1)
  curl -sSL -o $S/fonts/$(echo $spec|cut -d: -f1).ttf "$url"; done
```
The Whisper model (large-v3, int8, ~2.9GB) downloads on first use. **Needs `huggingface.co` AND
`*.hf.co` in the environment's allowed domains** (the model bytes come from `us.aws.cdn.hf.co`;
both were added by the user Oct 22 2026).

## Use
```bash
WHISPER_MODELS=$S/models $S/vid-env/bin/python -I transcribe.py clip.mp4 words.json   # word timings
$S/vid-env/bin/python -I captions.py words.json caps.ass                              # word-pop captions
ffmpeg -i clip.mp4 -vf "ass=caps.ass:fontsdir=$S/fonts" ... out.mp4
```
- Captions: Inter Bold 78px, Alabaster with an Espresso outline, **active word in Cognac #A0623A**,
  3 words per chunk, sized for a 1080×1920 canvas.
- `captions.py` FIX map corrects brand words Whisper mishears ("scenic" → CNIC, cordovan → Kordovan).
  Add to it whenever a new mishearing shows up.
- ⚠️ Never `.upper()` a whole ASS line — it capitalises the `{\c&H…}` override tags and
  silently kills the highlight colour. Uppercase the words only.
- Verified Oct 22 2026 end to end with a synthetic voice: transcription took ~1 min per clip on
  4 CPUs, and the highlight renders correctly.
