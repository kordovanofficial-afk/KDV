"""Mocha Mate master v2: jump cuts + motion + inserts + animated captions + SFX + de-echoed voice.
Usage: build_v2.py  (run from the edit/ dir; needs ../vid-env, ../models, ../fonts, ../bin/deep-filter)"""
import json, os, subprocess, re
import numpy as np

S = os.path.abspath("..")
ORIG = "/home/user/KDV/mocha-mate/originals/IMG_{}.MOV"
FONTS = f"{S}/fonts"
OUT = os.environ.get("V_OUT", "v2")
os.makedirs(f"{OUT}/pieces", exist_ok=True)
GRADE = "eq=contrast=1.06:saturation=1.08:gamma=0.98,colorbalance=rs=0.03:bs=-0.03:rm=0.02:bm=-0.02"
FPS = 30

def run(cmd):
    subprocess.run(cmd, check=True)

def probe_dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)

SEGS = json.load(open(os.environ.get("V_SEGS", "segments.json")))

# ---------- A. speech pieces (jump cuts) ----------
def speech_pieces(clip, a, b, noise="-35dB", minsil=0.30, pad=0.09):
    out = subprocess.run(["ffmpeg", "-nostdin", "-ss", str(a), "-to", str(b), "-i", ORIG.format(clip),
                          "-af", f"silencedetect=noise={noise}:d={minsil}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    sil = list(zip(st, en + [b - a] * (len(st) - len(en))))
    pieces, cur = [], 0.0
    for s0, s1 in sil:
        if s0 - cur > 0.15:
            pieces.append([max(0, cur - pad), min(b - a, s0 + pad)])
        cur = s1
    if (b - a) - cur > 0.15:
        pieces.append([max(0, cur - pad), b - a])
    merged = []
    for p in pieces:
        if merged and p[0] - merged[-1][1] < 0.12:
            merged[-1][1] = p[1]
        else:
            merged.append(p)
    return [[a + p[0], a + p[1]] for p in merged]

timeline, t_acc, k = [], 0.0, 0
for si, s in enumerate(SEGS):
    pcs = speech_pieces(s["clip"], s["in"], s["out"])
    s["t0"] = t_acc
    for pi, (a, b) in enumerate(pcs):
        a, b = round(a * FPS) / FPS, round(b * FPS) / FPS
        n = max(1, round((b - a) * FPS))
        z0 = 1.0 if k % 2 == 0 else 1.12
        if si == 0 and pi == 0:
            z = "1+0.22*max(0,1-on/9)"                      # hook: snap zoom-out in 0.3s
        else:
            z = f"{z0}+0.035*on/{n}"                        # slow push-in
        out = f"{OUT}/pieces/{k:03d}.mp4"
        vf = (f"scale=1080:1920,fps={FPS},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS},"
              f"{GRADE},format=yuv420p")
        run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", f"{a:.4f}", "-i", ORIG.format(s["clip"]), "-t", f"{n / FPS:.4f}",
             "-vf", vf, "-frames:v", str(n), "-af", "aresample=48000,apad", "-ac", "1", "-c:v", "libx264", "-preset", "fast", "-crf", "17",
             "-c:a", "pcm_s16le", "-map_metadata", "-1", out.replace(".mp4", ".mov")])
        d = probe_dur(out.replace(".mp4", ".mov"))
        timeline.append({"k": k, "seg": s["id"], "src": [a, b], "t0": t_acc, "dur": d})
        t_acc += d; k += 1
    s["t1"] = t_acc
    print(s["id"], f"{len(pcs)} pieces", f"{s['t1'] - s['t0']:.2f}s", flush=True)
BODY = t_acc
with open(f"{OUT}/list.txt", "w") as f:
    for p in timeline:
        f.write(f"file 'pieces/{p['k']:03d}.mov'\n")
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
     "-c", "copy", f"{OUT}/body_raw.mov"])

# ---------- E. voice: de-echo (DeepFilterNet) + EQ/compression ----------
os.makedirs(f"{OUT}/df_in", exist_ok=True); os.makedirs(f"{OUT}/df_out", exist_ok=True)
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{OUT}/body_raw.mov", "-vn", "-ac", "1", "-ar", "48000", f"{OUT}/df_in/voice.wav"])
run([f"{S}/bin/deep-filter", "-o", f"{OUT}/df_out", f"{OUT}/df_in/voice.wav"])
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{OUT}/df_out/voice.wav", "-af",
     "highpass=f=90,equalizer=f=250:t=q:w=1:g=-3,equalizer=f=3500:t=q:w=1.2:g=3,"
     "acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2", f"{OUT}/voice_eq.wav"])

# ---------- word timings on the final voice ----------
run([f"{S}/vid-env/bin/python", "-I", "/home/user/KDV/tools/video-edit/transcribe.py",
     f"{OUT}/voice_eq.wav", f"{OUT}/words.json", "hi"])
json.dump({"segs": SEGS, "timeline": timeline, "body": BODY}, open(f"{OUT}/timeline.json", "w"), indent=1)
print("body", round(BODY, 2))
