#!/usr/bin/env bash
# Assembles the seven clips into the finished 9:16 ad.
#
#   raw/shot01.mp4 … raw/shot07.mp4   generated clips, any size, 9:16-ish
#   audio/vo.wav                      recorded voiceover (optional but intended)
#   captions.srt                      burned in, brand type and colours
#
# Usage: ./assemble.sh
set -euo pipefail
cd "$(dirname "$0")"

OUT="jacket_film_v1.mp4"
DURS=(4 4 4 5 3 3 4)          # seconds per shot; must match captions.srt
FONT="${FONT:-Fraunces}"       # falls back to any serif if not installed

# --- preflight: fail loudly here rather than mid-encode -----------------------
command -v ffmpeg >/dev/null || { echo "ffmpeg not installed"; exit 1; }
for i in $(seq -w 1 7); do
  [ -f "raw/shot$i.mp4" ] || { echo "missing raw/shot$i.mp4"; exit 1; }
done
[ -f captions.srt ] || { echo "missing captions.srt"; exit 1; }

mkdir -p build
rm -f build/*.mp4 build/list.txt

# --- 1. trim each clip to its exact duration, normalise to 1080x1920 ----------
# scale+crop rather than pad: generated clips vary slightly in aspect and a
# letterbox would show as black bars inside a full-bleed Reels placement.
for n in $(seq 1 7); do
  i=$(printf "%02d" "$n"); d=${DURS[$((n-1))]}
  ffmpeg -y -loglevel error -i "raw/shot$i.mp4" -t "$d" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=24,setsar=1" \
    -an -c:v libx264 -crf 18 -pix_fmt yuv420p "build/clip$i.mp4"
  echo "file 'clip$i.mp4'" >> build/list.txt
done

# --- 2. concatenate -----------------------------------------------------------
ffmpeg -y -loglevel error -f concat -safe 0 -i build/list.txt -c copy build/joined.mp4

# --- 3. burn captions ---------------------------------------------------------
# ASS colours are &HBBGGRR — byte-reversed from hex RGB. Get this wrong and the
# captions come out the wrong colour but still render, so it fails silently.
#   Alabaster #F7F2EA -> &H00EAF2F7   (fill)
#   Espresso  #241C16 -> &H00161C24   (outline)
# MarginV keeps captions clear of the Reels UI chrome at the bottom.
ffmpeg -y -loglevel error -i build/joined.mp4 \
  -vf "subtitles=captions.srt:force_style='FontName=${FONT},FontSize=52,PrimaryColour=&H00EAF2F7,OutlineColour=&H00161C24,BorderStyle=3,Outline=2,Shadow=0,Alignment=2,MarginV=260'" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p build/captioned.mp4

# --- 4. audio -----------------------------------------------------------------
# Generated clips often carry music we did not ask for. Their audio is discarded
# entirely and the recorded voiceover becomes the only track. loudnorm targets
# -14 LUFS, which is where social platforms normalise to.
if [ -f audio/vo.wav ]; then
  ffmpeg -y -loglevel error -i build/captioned.mp4 -i audio/vo.wav \
    -filter_complex "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st=26.5:d=0.5[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest "$OUT"
else
  echo "note: audio/vo.wav not found — writing silent track at spec"
  ffmpeg -y -loglevel error -i build/captioned.mp4 \
    -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
    -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k -shortest "$OUT"
fi

echo "done -> $(pwd)/$OUT"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$OUT"
