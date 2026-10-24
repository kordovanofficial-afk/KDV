"""Word-gap jump cuts on the stage-1 body: gaps > MAXGAP between words shrink to KEEP seconds.
Each kept interval alternates a 1.0 / 1.09 punch-in. Rewrites v2/body_raw.mov, voice_eq.wav, words.json, timeline.json."""
import json, os, shutil, subprocess

OUT = os.environ.get("V_OUT", "v2"); MAXGAP = 0.28; KEEP = 0.12
for f in ["body_raw.mov", "voice_eq.wav", "words.json", "timeline.json"]:
    if not os.path.exists(f"{OUT}/untight_{f}"):
        shutil.copy(f"{OUT}/{f}", f"{OUT}/untight_{f}")
words = json.load(open(f"{OUT}/untight_words.json"))
W = words["words"]; TL = json.load(open(f"{OUT}/untight_timeline.json")); BODY = TL["body"]
seg_bounds = [s["t0"] for s in TL["segs"]][1:]          # never cut across a scene boundary's flash point

import re
_o = subprocess.run(["ffmpeg", "-nostdin", "-i", f"{OUT}/untight_voice_eq.wav", "-af", "silencedetect=noise=-40dB:d=0.22",
                     "-f", "null", "-"], capture_output=True, text=True).stderr
_st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", _o)]
_en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", _o)]
keep, start = [], 0.0
for g0, g1 in zip(_st, _en):
    if g0 < 0.05 or g1 > BODY - 0.05:
        continue
    keep.append([start, g0 + KEEP / 2]); start = g1 - KEEP / 2
keep.append([start, BODY])
keep = [[round(a * 30) / 30, round(b * 30) / 30] for a, b in keep]
keep = [k for k in keep if k[1] - k[0] >= 2 / 30]
def remap(t):
    acc = 0.0
    for a, b in keep:
        if t < a: return acc
        if t <= b: return acc + (t - a)
        acc += b - a
    return acc
new_body = sum(b - a for a, b in keep)
print(f"{len(keep)} intervals, {BODY:.2f}s -> {new_body:.2f}s")

os.makedirs(f"{OUT}/tight", exist_ok=True)
with open(f"{OUT}/tight/list.txt", "w") as lst:
    for i, (a, b) in enumerate(keep):
        z = 1.0 if i % 2 == 0 else 1.09
        p = f"{OUT}/tight/{i:03d}.mov"
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-i", f"{OUT}/untight_body_raw.mov", "-frames:v", str(round((b - a) * 30)),
                        "-vf", f"crop=iw/{z}:ih/{z},scale=1080:1920:flags=lanczos,fps=30,format=yuv420p",
                        "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "17", p], check=True)
        lst.write(f"file '{i:03d}.mov'\n")
subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/tight/list.txt",
                "-c", "copy", f"{OUT}/body_raw.mov"], check=True)
_fc = ";".join(f"[0:a]atrim=start={a:.5f}:end={b:.5f},asetpts=PTS-STARTPTS[a{i}]" for i, (a, b) in enumerate(keep))
_fc += ";" + "".join(f"[a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1[out]"
subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{OUT}/untight_voice_eq.wav",
                "-filter_complex", _fc, "-map", "[out]", f"{OUT}/voice_eq.wav"], check=True)
words["words"] = [[remap(w[0]), remap(w[1]), w[2], w[3]] for w in W]
json.dump(words, open(f"{OUT}/words.json", "w"), ensure_ascii=False)
for s in TL["segs"]:
    s["t0"], s["t1"] = remap(s["t0"]), remap(s["t1"])
TL["body"] = new_body
json.dump(TL, open(f"{OUT}/timeline.json", "w"), indent=1)
