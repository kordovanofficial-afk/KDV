#!/usr/bin/env bash
# Cut, rotate, crop and warm-grade the b-roll for the Kordovan teaser (1080x1920, 30 fps, silent, no GPS metadata).
set -euo pipefail
T="$(cd "$(dirname "$0")" && pwd)"
S="$T/.."
A="$T/proj/assets"
mkdir -p "$A/fonts"
cp "$S/fonts/Fraunces.ttf" "$S/fonts/Inter.ttf" "$A/fonts/"
# warm Quiet-Heritage grade: lift shadows toward espresso, gentle contrast, slightly desaturated
GRADE="eq=contrast=1.08:saturation=0.92:gamma=0.97,colorbalance=rs=0.05:gs=0.01:bs=-0.05:rm=0.03:bm=-0.04:rh=0.02:bh=-0.03"
cut () { # name src start dur crop
  ffmpeg -nostdin -loglevel error -y -ss "$3" -i "$T/src/IMG_$2.MOV" -t "$4" -an -map_metadata -1 \
    -vf "$5scale=1080:1920:flags=lanczos,fps=30,$GRADE,format=yuv420p" \
    -c:v libx264 -preset slow -crf 16 -movflags +faststart "$A/$1.mp4"
  echo "$1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A/$1.mp4")"
}
# 1481: desk, new vs six-month wallet; crop in on the pair (source is auto-rotated to 1080x1920)
cut pair 1481 1.0 3.2 "crop=720:1280:130:560,"
# 1485: hand opens the wallet
cut open 1485 4.1 2.8 ""
# 1485: keys go into the hidden back pocket
cut keys 1485 11.15 3.0 ""
ls -la "$A" "$A/fonts"
