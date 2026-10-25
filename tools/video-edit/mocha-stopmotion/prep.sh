#!/usr/bin/env bash
# Stop-motion shots for the Mocha Mate ad: 8fps held frames + per-frame jitter, warm grade, square 1080, silent, no metadata.
set -euo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)/mm/raw"; A="$(cd "$(dirname "$0")" && pwd)/proj/assets"
GRADE="eq=contrast=1.1:saturation=1.05:gamma=0.98,colorbalance=rs=0.05:bs=-0.05:rm=0.03:bm=-0.04"
STOP="fps=8,crop=iw*0.94:ih*0.94:(iw-ow)/2+(random(0)-0.5)*24:(ih-oh)/2+(random(0)-0.5)*24,scale=1080:1080,fps=30"
cut () { # name clip start dur [extra]
  ffmpeg -nostdin -loglevel error -y -ss "$3" -i "$R/Img_$2.mp4" -t "$4" -an -map_metadata -1 \
   -vf "${5:-}$STOP,$GRADE,format=yuv420p" -c:v libx264 -preset slow -crf 17 -movflags +faststart "$A/$1.mp4"; echo "$1"; }
cut hook   1488 8.4  1.3
cut closed 1488 0.2  1.1
cut snap   1488 3.0  1.1
cut inside 1487 6.0  1.1
cut keys   1485 11.0 1.6
cut close  1488 10.4 1.1
cut hold   1483 8.0  1.1
cut pair   1481 1.0  1.1
# rewind: 1488 9.5s->0s played backwards in 0.5s
ffmpeg -nostdin -loglevel error -y -i "$R/Img_1488.mp4" -t 9.5 -an -map_metadata -1 \
  -vf "reverse,setpts=PTS/19,fps=30,scale=1080:1080,$GRADE,format=yuv420p" -c:v libx264 -crf 18 "$A/rewind.mp4"; echo rewind
