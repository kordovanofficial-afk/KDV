"""Stage 2: animated captions/headlines/flashes (ASS), B-roll inserts, SFX, progress bar, end card, final mux."""
import json, os, subprocess
import numpy as np

S = os.path.abspath("..")
FONTS = f"{S}/fonts"
OUT = os.environ.get("CUT_OUT", "v2")
OUTFILE = os.environ.get("CUT_FILE", "Mocha_Mate_Master_v2.mp4")
ORIG = "/home/user/KDV/mocha-mate/originals/IMG_{}.MOV"
GRADE = "eq=contrast=1.06:saturation=1.08:gamma=0.98,colorbalance=rs=0.03:bs=-0.03:rm=0.02:bm=-0.02"
TL = json.load(open(f"{OUT}/timeline.json"))
SEGS = {s["id"]: s for s in TL["segs"]}
ORDER = [s["id"] for s in TL["segs"]]
BODY = TL["body"]
WORDS = json.load(open(f"{OUT}/words.json"))["words"]

def run(cmd):
    subprocess.run(cmd, check=True)

TEXT = {
 "H3": "Pichle 6 mahine se main apne brand ka Mocha Mate wallet use kar raha hoon, aur ab time aa gaya hai ke main ek honest review de sakoon aap sab logon ko ke mujhe ye wallet kaisa hai?",
 "H1": "Ek naya hai. Ek chhe mahine se mere istemaal mein. Aap bata sakte hain kaun sa?",
 "S1": "Mera naam Asad Janjua hai. I am the co-founder of Kordovan Leather.",
 "S2": "Is wallet ki ek special pocket iski back side par hai, jo safe aur secure hai, aur main ismein apni spare keys aur change rakhta hoon.",
 "S3": "This is the CNIC window, jisko checkpost pe ya bank pe nikalne ki zaroorat nahi parti, so it's very convenient.",
 "S4": "Is wallet mein mere 6 se 12 cards hain, aur cash rakhne ke liye bhi ample space hai, aur yeh kabhi bhaari feel nahi hota.",
 "S5": "Ye wallet brand new hai, aur ye mera personal 6 mahine used wallet hai. Real leather kabhi flake nahi karta, sirf colour patina deta hai.",
 "S6": "Stitching iski abhi tak bilkul brand new si hai, aur saath hi aap sabko lifetime guarantee bhi hai.",
 "S7": "Pichle 5 years mein thousands of wallets, especially this Mocha Mate wallet, hum sell kar chuke hain.",
 "S8": "Genuine leather wallet, jiski lifetime guarantee hai, sirf aur sirf 3,200 rupay ka. Order ke liye COD ya online pay karein, link neeche diya hai.",
}
HEAD = {
 "H3": "Founder's honest review",
 "H1": "NEW vs. 6 MONTHS", "S1": "Founder · Kordovan", "S2": "The secret back pocket",
 "S3": "CNIC window", "S4": "6–12 cards + cash", "S5": "Real leather ages",
 "S6": "Lifetime craftsmanship warranty", "S7": "4,000+ wallets sold since 2021", "S8": "Rs 3,200",
}
KEYWORDS = {"naya", "chhe", "pocket", "keys", "cnic", "12", "cards", "patina", "lifetime", "thousands", "3,200", "neeche", "honest", "review"}
# B-roll inserts: (clip, src_in, src_out, anchor) — anchor = (segment, roman word that starts the insert)
INSERTS = [(1485, 6.0, 8.3, ("S2", "special")), (1485, 9.9, 11.6, ("S2", "spare")), (1481, 3.9, 6.9, ("S5", "Ye"))]
END_OVERRIDE = None
if os.path.exists(f"{OUT}/cut.json"):
    _c = json.load(open(f"{OUT}/cut.json"))
    TEXT = {**TEXT, **_c["text"]}
    INSERTS = [(i[0], i[1], i[2], (i[3], i[4])) for i in _c["inserts"]]
    END_OVERRIDE = _c["end"]

def t(s):
    h, s = divmod(max(s, 0), 3600); m, s = divmod(s, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"

# ---- map Roman words onto Whisper word timings per segment ----
timed_by_seg = {}
for sid in ORDER:
    a, b = SEGS[sid]["t0"], SEGS[sid]["t1"]
    ws = [w for w in WORDS if a - 0.05 <= w[0] < b - 0.05]
    roman = TEXT[sid].split()
    n, m = len(roman), len(ws)
    out = []
    for i, rw in enumerate(roman):
        if not ws:
            st = a + (b - a) * i / n; en = a + (b - a) * (i + 1) / n
        else:
            j0 = min(int(i * m / n), m - 1); j1 = max(j0, min(int((i + 1) * m / n), m) - 1)
            st, en = ws[j0][0], max(ws[j1][1], ws[j0][0] + 0.12)
        out.append([st, en, rw])
    timed_by_seg[sid] = out

ASS = """[Script Info]
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,96,&H00EAF2F7,&H00EAF2F7,&H00161C24,&H78000000,1,0,0,0,100,100,0,0,1,7,3,2,60,60,470,1
Style: Head,Fraunces,62,&H00EAF2F7,&H00EAF2F7,&H00241C16,&H40241C16,0,0,0,0,100,100,0,0,3,20,0,7,0,0,0,1
Style: Hook,Fraunces,124,&H00EAF2F7,&H00EAF2F7,&H00241C16,&H00241C16,1,0,0,0,100,100,0,0,1,8,4,8,60,60,300,1
Style: Fx,Inter,10,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev, pops, whooshes = [], [], []
COG, ALB = "&H3A62A0&", "&HEAF2F7&"
FLASH = r"{\an7\pos(0,0)\p1\c&HEAF2F7&\alpha&HFF&\t(0,50,\alpha&H70&)\t(50,200,\alpha&HFF&)}m 0 0 l 1080 0 1080 1920 0 1920{\p0}"

for i, sid in enumerate(ORDER):
    a, b = SEGS[sid]["t0"], SEGS[sid]["t1"]
    if i > 0 and "~" not in sid:
        ev.append(f"Dialogue: 5,{t(a)},{t(a + 0.22)},Fx,,0,0,0,,{FLASH}")
        whooshes.append(a - 0.12)
    base = sid.split("~")[0]
    HOOKS = {"H1": ("NEW vs. 6 MONTHS", "Can you tell?"), "H3": (r"{\fs104}6 MONTHS WITH\N{\fs104}MY OWN WALLET", "Honest review")}
    if "~" in sid:
        continue_seg = True
    else:
        continue_seg = False
    if base in HOOKS and i == 0:
        h1, h2 = HOOKS[base]
        ev.append(f"Dialogue: 3,{t(a)},{t(min(b, a + 2.6))},Hook,,0,0,0,,"
                  r"{\fscx60\fscy60\t(0,180,\fscx100\fscy100)\fad(0,200)}" + h1 + r"\N{\fs84\c&H5C8BC0&}" + h2)
        ev.append(f"Dialogue: 2,{t(a + 2.6)},{t(b)},Head,,0,0,0,,"
                  rf"{{\move(-700,250,70,250,0,260)\fad(0,150)}}{HEAD[base]}")
    elif continue_seg:
        ev.append(f"Dialogue: 2,{t(a)},{t(b)},Head,,0,0,0,,{{\\pos(70,250)}}{HEAD[base]}")
    else:
        ev.append(f"Dialogue: 2,{t(a + 0.05)},{t(b)},Head,,0,0,0,,"
                  rf"{{\move(-700,250,70,250,0,260)\fad(0,150)}}{HEAD[base]}")
    # captions: 2-word chunks, pop-in, active word cognac, keyword emphasis
    words = timed_by_seg[sid]
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 2 or w[2][-1] in ".,?":
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    for ci, c in enumerate(chunks):
        c_end = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else min(c[-1][1] + 0.2, b)
        is_key = any(x[2].strip(".,?").lower() in KEYWORDS for x in c)
        for wi, w in enumerate(c):
            st = w[0]
            en = c[wi + 1][0] if wi + 1 < len(c) else c_end
            if en <= st: continue
            parts = []
            for k, x in enumerate(c):
                word = x[2].upper()
                kw = x[2].strip(".,?").lower() in KEYWORDS
                if k == wi:
                    parts.append(f"{{\\c{COG}}}{word}{{\\c{ALB}}}")
                elif kw:
                    parts.append(f"{{\\c&H5C8BC0&}}{word}{{\\c{ALB}}}")
                else:
                    parts.append(word)
            size = r"\fs122" if is_key else ""
            intro = r"\fscx72\fscy72\t(0,90,\fscx100\fscy100)" if wi == 0 else ""
            ev.append(f"Dialogue: 1,{t(st)},{t(en)},Cap,,0,0,0,,{{{size}{intro}}}" + " ".join(parts))
        if is_key:
            pops.append(c[0][0])

open(f"{OUT}/captions.ass", "w").write(ASS + "\n".join(ev) + "\n")

# ---- B-roll inserts ----
ins_specs = []
for n, (clip, si, so, (sid, word)) in enumerate(INSERTS):
    tw = [w for w in timed_by_seg[sid] if w[2].strip(".,?").lower() == word.lower()]
    T = tw[0][0] if tw else SEGS[sid]["t0"] + 0.5
    d = so - si
    p = f"{OUT}/ins_{n}.mov"
    run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", str(si), "-to", str(so), "-i", ORIG.format(clip),
         "-vf", f"scale=1080:1920,fps=30,zoompan=z='1.04+0.06*on/{int(d*30)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,{GRADE},format=yuv420p",
         "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "17", p])
    ins_specs.append((p, T, d))
    whooshes.append(T - 0.1)
    print("insert", n, sid, word, f"at {T:.2f}s for {d:.1f}s")

# ---- SFX track (self-generated: whoosh + pop) ----
SR = 48000
rng = np.random.default_rng(7)
def whoosh():
    n = int(0.42 * SR); x = rng.standard_normal(n)
    x = np.convolve(x, np.ones(18) / 18, mode="same")                 # soften
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    sweep = np.sin(2 * np.pi * np.cumsum(np.linspace(300, 2400, n)) / SR) * 0.3 + 0.7
    return x * env * sweep * 0.18
def pop():
    n = int(0.09 * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * (520 + 900 * tt) * tt) * np.exp(-55 * tt) * 0.22
END = END_OVERRIDE or 3.4
total = BODY + END
sfx = np.zeros(int((total + 1) * SR))
def place(sig, at):
    i = int(max(0, at) * SR); sfx[i:i + len(sig)] += sig[: len(sfx) - i]
for w in whooshes: place(whoosh(), w)
for p in pops: place(pop(), p)
place(whoosh(), BODY - 0.1); place(pop(), BODY + 0.45); place(pop(), BODY + 1.2)
import wave
with wave.open(f"{OUT}/sfx.wav", "wb") as f:
    f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes((np.clip(sfx, -1, 1) * 32767).astype(np.int16).tobytes())

# ---- end card (animated) ----
last = f"{OUT}/last.png"
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-sseof", "-0.1", "-i", f"{OUT}/body_raw.mov", "-frames:v", "1", "-update", "1", last])
end_ass = ASS + "\n".join([
    r"Dialogue: 1,0:00:00.00,0:00:03.40,Hook,,0,0,0,,{\an5\pos(540,690)\fad(250,0)\move(540,740,540,690,0,300)}The Mocha Mate",
    r"Dialogue: 1,0:00:00.40,0:00:03.40,Hook,,0,0,0,,{\an5\pos(540,840)\fs160\c&H5C8BC0&\fscx40\fscy40\t(0,160,\fscx112\fscy112)\t(160,260,\fscx100\fscy100)}Rs 3,200",
    r"Dialogue: 1,0:00:00.80,0:00:03.40,Cap,,0,0,0,,{\an5\pos(540,985)\fs50\b0\fad(200,0)}Cash on delivery  ·  Lifetime warranty",
    r"Dialogue: 1,0:00:01.10,0:00:03.40,Cap,,0,0,0,,{\an5\pos(540,1075)\fs56\fad(200,0)}kordovanleather.com",
    r"Dialogue: 1,0:00:01.40,0:00:01.90,Cap,,0,0,0,,{\an5\move(540,1230,540,1265)\fs60\c&H5C8BC0&}LINK NEECHE ↓",
    r"Dialogue: 1,0:00:01.90,0:00:02.40,Cap,,0,0,0,,{\an5\move(540,1265,540,1230)\fs60\c&H5C8BC0&}LINK NEECHE ↓",
    r"Dialogue: 1,0:00:02.40,0:00:02.90,Cap,,0,0,0,,{\an5\move(540,1230,540,1265)\fs60\c&H5C8BC0&}LINK NEECHE ↓",
    r"Dialogue: 1,0:00:02.90,0:00:03.40,Cap,,0,0,0,,{\an5\move(540,1265,540,1230)\fs60\c&H5C8BC0&}LINK NEECHE ↓",
]) + "\n"
open(f"{OUT}/end.ass", "w").write(end_ass)
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-loop", "1", "-t", str(END), "-i", last,
     "-vf", f"gblur=sigma=30,eq=brightness=-0.24:saturation=0.75,ass={OUT}/end.ass:fontsdir={FONTS},fade=t=in:st=0:d=0.3,fps=30,format=yuv420p",
     "-c:v", "libx264", "-preset", "fast", "-crf", "17", f"{OUT}/end.mov"])

# ---- composite body: inserts -> captions -> progress bar ----
inputs = ["-i", f"{OUT}/body_raw.mov"]
fc, last_lbl = [], "0:v"
for n, (p, T, d) in enumerate(ins_specs):
    inputs += ["-i", p]
    fc.append(f"[{n + 1}:v]setpts=PTS-STARTPTS+{T:.3f}/TB[i{n}]")
    fc.append(f"[{last_lbl}][i{n}]overlay=eof_action=pass:enable='between(t,{T:.3f},{T + d:.3f})'[o{n}]")
    last_lbl = f"o{n}"
fc.append(f"[{last_lbl}]ass={OUT}/captions.ass:fontsdir={FONTS},"
          f"drawbox=x=0:y=0:w='iw*t/{BODY + END:.3f}':h=10:color=0xA0623A@0.95:t=fill[v]")
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fc), "-map", "[v]", "-an",
     "-c:v", "libx264", "-preset", "medium", "-crf", "18", f"{OUT}/body_v.mov"])
with open(f"{OUT}/vlist.txt", "w") as f:
    f.write("file 'body_v.mov'\nfile 'end.mov'\n")
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/vlist.txt", "-c", "copy", f"{OUT}/video.mov"])

# ---- audio: voice + SFX, loudness ----
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{OUT}/voice_eq.wav", "-i", f"{OUT}/sfx.wav", "-filter_complex",
     f"[0:a]apad=pad_dur={END}[vo];[vo][1:a]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000",
     "-ac", "2", "-c:a", "aac", "-b:a", "192k", f"{OUT}/audio.m4a"])
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{OUT}/video.mov", "-i", f"{OUT}/audio.m4a", "-map", "0:v", "-map", "1:a",
     "-c:v", "copy", "-c:a", "copy", "-shortest", "-map_metadata", "-1", "-movflags", "+faststart", OUTFILE])
print("done", round(BODY + END, 2), "s")
