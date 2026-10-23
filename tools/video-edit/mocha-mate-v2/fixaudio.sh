#!/bin/sh
# pad each piece's audio to its video duration, then de-echo + EQ again (keeps lip sync exact)
set -e
D=$1; cd $D; mkdir -p apad; : > apad/list.txt
for p in pieces/*.mov; do b=$(basename $p .mov); vd=$(ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 $p)
  ffmpeg -nostdin -y -loglevel error -i $p -vn -af "apad=whole_dur=$vd,atrim=0:$vd" -ac 1 -ar 48000 apad/$b.wav; echo "file '$b.wav'" >> apad/list.txt; done
ffmpeg -nostdin -y -loglevel error -f concat -safe 0 -i apad/list.txt -c copy df_in/voice.wav
rm -f df_out/voice.wav; /tmp/claude-0/-home-user-KDV/1d3273db-74a5-5b52-a15a-6f186edb19ae/scratchpad/bin/deep-filter -o df_out df_in/voice.wav >/dev/null 2>&1
ffmpeg -nostdin -y -loglevel error -i df_out/voice.wav -af "highpass=f=90,equalizer=f=250:t=q:w=1:g=-3,equalizer=f=3500:t=q:w=1.2:g=3,acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2" voice_eq.wav
