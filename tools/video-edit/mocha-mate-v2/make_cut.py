"""Build a cutdown body from the tightened v2 master body, then stage 2 renders graphics on it.
Usage: make_cut.py <name>   (config inside CUTS). Ranges are (segment, first roman word idx, last roman word idx);
mid-segment cut points snap to the nearest real pause in the de-echoed voice."""
import json, os, re, subprocess, sys

NAME = sys.argv[1]
SRC = "v2"
CUTS = {
 "30s": {"ranges": [("H1", 0, 14), ("S2", 0, 25), ("S5", 0, 24), ("S8", 7, 24)], "end": 2.8,
         "inserts": [[1485, 6.0, 8.3, "S2", "special"], [1485, 9.9, 11.6, "S2", "spare"], [1481, 3.9, 6.9, "S5", "Ye"]]},
 "15s": {"ranges": [("H1", 0, 14), ("S5", 14, 24), ("S8", 7, 12)], "end": 2.6,
         "inserts": [[1481, 4.2, 6.6, "S5", "Real"]]},
}
cfg = CUTS[NAME]
OUT = f"cut_{NAME}"
os.makedirs(f"{OUT}/parts", exist_ok=True)
TL = json.load(open(f"{SRC}/timeline.json")); SEGS = {s["id"]: s for s in TL["segs"]}
WORDS = json.load(open(f"{SRC}/words.json"))["words"]
TEXT = json.load(open("text_master.json"))

def timed(sid):
    a, b = SEGS[sid]["t0"], SEGS[sid]["t1"]
    ws = [w for w in WORDS if a - 0.05 <= w[0] < b - 0.05]
    roman = TEXT[sid].split(); n, m = len(roman), len(ws); out = []
    for i, rw in enumerate(roman):
        j0 = min(int(i * m / n), m - 1); j1 = max(j0, min(int((i + 1) * m / n), m) - 1)
        out.append([ws[j0][0], max(ws[j1][1], ws[j0][0] + 0.12), rw])
    return out

o = subprocess.run(["ffmpeg", "-nostdin", "-i", f"{SRC}/voice_eq.wav", "-af", "silencedetect=noise=-40dB:d=0.08",
                    "-f", "null", "-"], capture_output=True, text=True).stderr
SIL = list(zip([float(x) for x in re.findall(r"silence_start: ([\d.]+)", o)],
               [float(x) for x in re.findall(r"silence_end: ([\d.]+)", o)]))
def snap(t, side):
    best = None
    for s0, s1 in SIL:
        p = (s1 - 0.05) if side == "start" else (s0 + 0.05)
        if abs(p - t) <= 0.45 and (best is None or abs(p - t) < abs(best - t)):
            best = p
    return best if best is not None else t

ranges, text, newsegs, acc = [], {}, [], 0.0
for sid, i0, i1 in cfg["ranges"]:
    tw = timed(sid); roman = TEXT[sid].split()
    a = SEGS[sid]["t0"] if i0 == 0 else snap(tw[i0][0], "start")
    b = SEGS[sid]["t1"] if i1 == len(roman) - 1 else snap(tw[i1][1], "end")
    a, b = round(a * 30) / 30, round(b * 30) / 30
    ranges.append((sid, a, b)); text[sid] = " ".join(roman[i0:i1 + 1])
    newsegs.append({"id": sid, "t0": acc, "t1": acc + (b - a)}); acc += b - a
    print(f"{sid}: {a:.2f}-{b:.2f} ({b - a:.2f}s) «{text[sid][:60]}»")
BODY = acc

with open(f"{OUT}/list.txt", "w") as lst:
    for i, (sid, a, b) in enumerate(ranges):
        p = f"parts/{i:02d}.mov"
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", f"{a:.4f}", "-i", f"{SRC}/body_raw.mov",
                        "-frames:v", str(round((b - a) * 30)), "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "17",
                        f"{OUT}/{p}"], check=True)
        lst.write(f"file '{p}'\n")
subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
                "-c", "copy", f"{OUT}/body_raw.mov"], check=True)
sel = "+".join(f"between(t,{a:.4f},{b:.4f})" for _, a, b in ranges)
subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{SRC}/voice_eq.wav",
                "-af", f"aselect='{sel}',asetpts=N/SR/TB", f"{OUT}/voice_eq.wav"], check=True)
def remap(t):
    acc2 = 0.0
    for _, a, b in ranges:
        if a <= t <= b: return acc2 + (t - a)
        acc2 += b - a
    return None
nw = []
for w in WORDS:
    s, e = remap(w[0]), remap(w[1])
    if s is not None and e is not None: nw.append([s, e, w[2], w[3]])
json.dump({"language": "hi", "words": nw}, open(f"{OUT}/words.json", "w"), ensure_ascii=False)
json.dump({"segs": newsegs, "body": BODY}, open(f"{OUT}/timeline.json", "w"), indent=1)
json.dump({"text": text, "inserts": cfg["inserts"], "end": cfg["end"]}, open(f"{OUT}/cut.json", "w"), indent=1)
print(f"body {BODY:.2f}s + end card {cfg['end']}s = {BODY + cfg['end']:.2f}s")
