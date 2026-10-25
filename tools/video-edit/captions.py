"""Word-pop captions (ASS) from transcribe.py JSON. Usage: captions.py <words.json> <out.ass>"""
import sys, json, re
FIX = {"scenic": "CNIC", "mocha": "Mocha", "mate": "Mate", "cordovan": "Kordovan", "kordovan": "Kordovan"}
words = json.load(open(sys.argv[1]))["words"]
def fix(w):
    core = re.sub(r"[^\w]", "", w).lower()
    return re.sub(r"[\w']+", FIX[core], w, count=1) if core in FIX else w
def t(s):
    h, s = divmod(s, 3600); m, s = divmod(s, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"
# group into 3-word chunks, break early at punctuation
chunks, cur = [], []
for w in words:
    cur.append(w)
    if len(cur) == 3 or w[2][-1:] in ".,?!":
        chunks.append(cur); cur = []
if cur: chunks.append(cur)
head = """[Script Info]
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,78,&H00EAF2F7,&H00EAF2F7,&H00161C24,&H64161C24,1,0,0,0,100,100,0,0,1,6,2,2,80,80,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
lines = []
# active word = Cognac #A0623A (ASS BGR: &H3A62A0&), others Alabaster
for c in chunks:
    for i, w in enumerate(c):
        end = c[i + 1][0] if i + 1 < len(c) else w[1]
        txt = " ".join(("{\\c&H3A62A0&\\fscx108\\fscy108}" + fix(x[2]).upper() + "{\\c&HEAF2F7&\\fscx100\\fscy100}") if j == i else fix(x[2]).upper() for j, x in enumerate(c))
        pop = "{\\fad(60,0)}" if i == 0 else ""
        lines.append(f"Dialogue: 0,{t(w[0])},{t(end)},Cap,,0,0,0,,{pop}{txt}")
open(sys.argv[2], "w").write(head + "\n".join(lines) + "\n")
print(len(chunks), "caption chunks,", len(lines), "events")
