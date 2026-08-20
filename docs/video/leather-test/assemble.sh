#!/usr/bin/env bash
#
# Kordovan — assemble "leather-test"
# 9:16 Meta ad, 22.0s, 8 shots, captions burned in.
#
# Usage:   ./assemble.sh
# Input:   ./raw/shot01.mp4 … ./raw/shot08.mp4   (over-record; this trims them)
#          ./captions.srt
#          ./audio/bed.m4a                        (optional — silence if absent)
#          ./fonts/                               (optional — Fraunces .ttf files)
# Output:  ./out/leather-test.mp4
#
# Requires: ffmpeg built with --enable-libass and --enable-libx264 (check with
#           `ffmpeg -filters | grep subtitles` — no output means no libass, and
#           the caption burn will fail).

set -euo pipefail
cd "$(dirname "$0")"

SLUG="leather-test"
W=1080          # Meta 9:16
H=1920
FPS=30          # normalise everything: phone clips are 30/60, LTX output is 24

RAW="raw"
WORK="work"
OUT="out/${SLUG}.mp4"

# ---------------------------------------------------------------------------
# Shot order and the exact duration each shot is trimmed to, in seconds.
# These MUST stay in lockstep with SHOTS.md and captions.srt. Change one,
# change all three, or the captions slide off their pictures.
# ---------------------------------------------------------------------------
SHOTS=(shot01 shot02 shot03 shot04 shot05 shot06 shot07 shot08)
DURS=(  3.2     2.6     3.0     2.2     3.0     2.0     2.0     4.0 )
#       FILM    FILM    FILM    FILM    FILM    FILM    GEN     FILM   -> 22.0s

# ---------------------------------------------------------------------------
# Brand colours, in ASS format.
#
# libass writes colours as &HAABBGGRR — byte-REVERSED from CSS hex, with an
# alpha byte in front where 00 = fully opaque. So you read the hex pairs of an
# RGB value backwards. Get this wrong and captions come out the wrong colour:
#
#   Alabaster  #F7F2EA  ->  RR=F7 GG=F2 BB=EA  ->  &H00EAF2F7
#   Espresso   #241C16  ->  RR=24 GG=1C BB=16  ->  &H00161C24
#   Cognac     #A0623A  ->  RR=A0 GG=62 BB=3A  ->  &H003A62A0   (accent, unused below)
# ---------------------------------------------------------------------------
CAP_FILL="&H00EAF2F7"     # Alabaster  — caption fill
CAP_LINE="&H00161C24"     # Espresso   — outline, so text survives a light frame

# Fraunces must be installed system-wide OR present as .ttf in ./fonts/.
# If libass cannot find the family it silently falls back to a default sans and
# the ad stops looking like Kordovan — check the first frame of the output.
FONTSDIR=""
if [[ -d "fonts" ]]; then
  FONTSDIR=":fontsdir=fonts"
else
  echo "note: ./fonts not found — relying on a system-installed Fraunces." >&2
fi

# ---------------------------------------------------------------------------
# Preflight: fail loudly and early rather than half-way through an encode.
# ---------------------------------------------------------------------------
command -v ffmpeg >/dev/null || { echo "error: ffmpeg not on PATH" >&2; exit 1; }
[[ -f captions.srt ]] || { echo "error: captions.srt missing" >&2; exit 1; }

missing=0
for s in "${SHOTS[@]}"; do
  [[ -f "${RAW}/${s}.mp4" ]] || { echo "error: missing ${RAW}/${s}.mp4" >&2; missing=1; }
done
[[ "$missing" -eq 0 ]] || exit 1

rm -rf "$WORK"
mkdir -p "$WORK" out

# ---------------------------------------------------------------------------
# Pass 1 — normalise every shot to one identical spec.
#
# The concat demuxer does a stream copy: it will produce a corrupt or
# desynced file if the parts differ in resolution, pixel format, frame rate or
# SAR. So every clip is re-encoded to exactly the same shape first, at CRF 18 —
# one stop better than the delivery CRF so this intermediate does not become
# the quality floor for the final encode.
# ---------------------------------------------------------------------------
i=0
for s in "${SHOTS[@]}"; do
  dur="${DURS[$i]}"
  idx=$(printf "%02d" $((i + 1)))
  echo "  [${idx}/${#SHOTS[@]}] ${s}  ->  ${dur}s"

  # -ss before -i seeks fast on the input; both are 0 here (we take each clip
  # from its head) but it is left explicit so a late start is a one-word change.
  #
  # scale ... force_original_aspect_ratio=increase then crop = fill 1080x1920
  # without letterboxing. LTX output is 704x1280, so shot07 is upscaled here;
  # lanczos is the sharpest of the practical scalers and matters on grain.
  #
  # setsar=1 forces square pixels — some phones tag a non-1 SAR and concat
  # then refuses the file.
  # -an drops audio: the shots carry unusable on-set sound and the bed is
  # added once, at the end.
  ffmpeg -hide_banner -loglevel error -y \
    -ss 0 -i "${RAW}/${s}.mp4" -t "${dur}" \
    -vf "scale=${W}:${H}:force_original_aspect_ratio=increase:flags=lanczos,crop=${W}:${H},fps=${FPS},setsar=1,format=yuv420p" \
    -an \
    -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
    "${WORK}/${idx}.mp4"

  printf "file '%s'\n" "${idx}.mp4" >> "${WORK}/concat.txt"
  i=$((i + 1))
done

# ---------------------------------------------------------------------------
# Audio bed. Optional by design — this ad is built to work muted, and Meta
# still wants a real AAC track rather than no audio stream at all.
# ---------------------------------------------------------------------------
MUSIC="${MUSIC:-audio/bed.m4a}"
if [[ -f "$MUSIC" ]]; then
  echo "  audio: ${MUSIC}"
  AUDIO_IN=(-i "$MUSIC")
else
  echo "  audio: none found — laying down silence"
  AUDIO_IN=(-f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100)
fi

# ---------------------------------------------------------------------------
# Pass 2 — concatenate, burn captions, encode to the Meta delivery spec.
#
#   original_size=1080x1920  tells libass what resolution FontSize and MarginV
#                            are measured against. Without it ffmpeg's SRT
#                            reader can assume a 384x288 canvas and the text
#                            comes out microscopic.
#   Alignment=2              bottom centre (ASS numpad layout).
#   MarginV=320              lifts captions 320px off the bottom edge, keeping
#                            them inside the middle ~80% and clear of the Reels
#                            and Stories chrome.
#   Outline=3, Shadow=0      a hard Espresso rim, no drop shadow — shadows read
#                            as cheap and muddy the warm grade.
#   -shortest                the silence source is infinite; stop at video end.
#   +faststart               moves the moov atom to the front so the ad starts
#                            playing before it has finished downloading.
# ---------------------------------------------------------------------------
STYLE="FontName=Fraunces,FontSize=52,Bold=0,PrimaryColour=${CAP_FILL},OutlineColour=${CAP_LINE},BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=320,MarginL=90,MarginR=90"

echo "  burning captions and encoding…"
ffmpeg -hide_banner -loglevel error -y \
  -f concat -safe 0 -i "${WORK}/concat.txt" \
  "${AUDIO_IN[@]}" \
  -map 0:v:0 -map 1:a:0 \
  -vf "subtitles=captions.srt:original_size=${W}x${H}${FONTSDIR}:force_style='${STYLE}'" \
  -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -profile:v high -level 4.0 \
  -c:a aac -b:a 128k -ar 44100 -ac 2 \
  -shortest -movflags +faststart \
  "$OUT"

echo
echo "done -> $(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")"
ffprobe -v error -show_entries format=duration:stream=width,height,codec_name \
        -of default=noprint_wrappers=1 "$OUT" || true

# ---------------------------------------------------------------------------
# Optional: put the closing price line in Cognac.
#
# force_style applies one style to every cue, so per-cue colour needs a real
# ASS file. Convert once, edit, then burn the .ass instead of the .srt:
#
#   ffmpeg -i captions.srt captions.ass
#   # add a second [V4+ Styles] line named "Price" with
#   #   PrimaryColour=&H003A62A0   (Cognac #A0623A)
#   # then set the Style field of cues 8 and 9 to Price
#   # and swap the -vf above to:  subtitles=captions.ass:fontsdir=fonts
# ---------------------------------------------------------------------------
