#!/usr/bin/env bash
# Luxury cut: tight macro crops, 0.6x optical-flow slow motion, crushed-shadow warm grade, vignette, film grain. Square 1080, silent, no metadata.
set -euo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)/mm/raw"; A="$(cd "$(dirname "$0")" && pwd)/proj/assets"
GRADE="curves=r='0/0 0.3/0.26 0.75/0.82 1/0.97':g='0/0 0.3/0.24 0.75/0.76 1/0.93':b='0/0 0.3/0.2 0.75/0.67 1/0.86',eq=saturation=0.8:contrast=1.08,vignette=angle=PI/4.2,noise=alls=6:allf=t"
cut () { # name clip start srcdur crop(w:h:x:y)
  ffmpeg -nostdin -loglevel error -y -ss "$3" -t "$4" -i "$R/Img_$2.mp4" -an -map_metadata -1 \
   -vf "crop=$5,scale=1080:1080:flags=lanczos,minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts=PTS/0.6,fps=30,$GRADE,format=yuv420p" \
   -c:v libx264 -preset slow -crf 17 -movflags +faststart "$A/$1.mp4"; echo "$1 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A/$1.mp4")"; }
cut patina 1487 12.3 1.7 720:720:300:200
cut snap   1488 4.0  1.6 600:600:300:200
cut open   1487 4.3  1.6 760:760:220:60
cut pair   1483 8.0  1.6 820:820:180:140
cut hero   1488 12.2 1.6 780:780:180:270
