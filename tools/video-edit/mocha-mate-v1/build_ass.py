"""Build captions + headlines ASS for the Mocha Mate master.
Captions: the founder's own words in Roman Urdu/English, timed to Whisper word timings of the joined
audio (Devanagari words mapped proportionally onto the Roman words within each segment)."""
import json, subprocess

SEG = ["H1", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]
TEXT = {
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
 "H1": "NEW vs. 6 MONTHS", "S1": "Founder · Kordovan", "S2": "The secret back pocket",
 "S3": "CNIC window", "S4": "6–12 cards + cash", "S5": "Real leather ages. It doesn't flake.",
 "S6": "Lifetime craftsmanship warranty", "S7": "4,000+ wallets sold since 2021",
 "S8": "Rs 3,200 · COD or pay online",
}

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)

def t(s):
    h, s = divmod(max(s, 0), 3600); m, s = divmod(s, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"

bounds, acc = {}, 0.0
for sid in SEG:
    d = dur(f"seg/{sid}.mp4"); bounds[sid] = (acc, acc + d); acc += d
TOTAL = acc
words = json.load(open("master_words.json"))["words"]

head = """[Script Info]
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,74,&H00EAF2F7,&H00EAF2F7,&H00161C24,&H64161C24,1,0,0,0,100,100,0,0,1,6,2,2,70,70,430,1
Style: Head,Fraunces,60,&H00EAF2F7,&H00EAF2F7,&H00161C24,&H50161C24,0,0,0,0,100,100,0,0,3,18,0,8,80,80,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
COG, ALB = "&H3A62A0&", "&HEAF2F7&"
for sid in SEG:
    a, b = bounds[sid]
    ev.append(f"Dialogue: 1,{t(a)},{t(b)},Head,,0,0,0,,{{\\fad(150,100)}}{HEAD[sid]}")
    ws = [w for w in words if a - 0.05 <= w[0] < b - 0.05]
    roman = TEXT[sid].split()
    if not ws:
        continue
    n, m = len(roman), len(ws)
    timed = []
    for i, rw in enumerate(roman):
        j0 = min(int(i * m / n), m - 1); j1 = min(int((i + 1) * m / n), m) - 1
        timed.append([ws[j0][0], max(ws[max(j1, j0)][1], ws[j0][0] + 0.12), rw])
    chunks, cur = [], []
    for w in timed:
        cur.append(w)
        if len(cur) == 3 or w[2][-1] in ".,?":
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    for c in chunks:
        for i, w in enumerate(c):
            end = c[i + 1][0] if i + 1 < len(c) else min(w[1] + 0.15, b)
            txt = " ".join((f"{{\\c{COG}\\fscx106\\fscy106}}{x[2].upper()}{{\\c{ALB}\\fscx100\\fscy100}}" if k == i else x[2].upper())
                           for k, x in enumerate(c))
            ev.append(f"Dialogue: 0,{t(w[0])},{t(end)},Cap,,0,0,0,,{txt}")

def secs(x):
    h, m, r = x.split(":"); return int(h) * 3600 + int(m) * 60 + float(r)
caps = sorted([e for e in ev if ",Cap," in e], key=lambda e: secs(e.split(",")[1]))
fixed = []
for i, e in enumerate(caps):
    parts = e.split(",", 9)
    if i + 1 < len(caps):
        nxt = secs(caps[i + 1].split(",")[1])
        if secs(parts[2]) > nxt:
            parts[2] = t(nxt)
    fixed.append(",".join(parts))
ev = [e for e in ev if ",Cap," not in e] + fixed
open("master.ass", "w").write(head + "\n".join(ev) + "\n")
json.dump({"bounds": bounds, "total": TOTAL}, open("bounds.json", "w"), indent=1)
print(f"total {TOTAL:.2f}s, {len(ev)} events")
