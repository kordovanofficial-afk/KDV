#!/usr/bin/env bash
# v2 shot list: beat-cut b-roll (1080x1920, 30fps, silent, metadata stripped, warm grade)
set -euo pipefail
T="$(cd "$(dirname "$0")" && pwd)"; A="$T/proj/assets"
GRADE="eq=contrast=1.08:saturation=0.92:gamma=0.97,colorbalance=rs=0.05:gs=0.01:bs=-0.05:rm=0.03:bm=-0.04:rh=0.02:bh=-0.03"
cut () { ffmpeg -nostdin -loglevel error -y -ss "$3" -i "$T/src/IMG_$2.MOV" -t "$4" -an -map_metadata -1 \
  -vf "$5scale=1080:1920:flags=lanczos,fps=30,$GRADE,format=yuv420p" -c:v libx264 -preset slow -crf 16 -movflags +faststart "$A/$1.mp4"; echo "$1 ok"; }
cut pair  1481 1.0  1.7 "crop=720:1280:130:560,"
cut hold  1483 8.0  1.7 "crop=800:1422:140:300,"
cut snap  1485 4.1  1.1 ""
cut open  1485 5.5  1.6 ""
cut keys  1485 11.15 2.1 ""
