import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import ADS, VIDEOS
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"); os.makedirs(OUT, exist_ok=True)
INK=HexColor("#241C16"); BG=HexColor("#F7F2EA"); STONE=HexColor("#8B8174"); TERRA=HexColor("#A0623A")
W,H=A4; M=42
def wrap(t,f,s,w): return simpleSplit(t,f,s,w)
def fresh(c): c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0); c.setFillColor(INK)
def cover(c,title,lines):
    fresh(c); c.setFont("DVB",19); y=H-70
    for ln in wrap(title,"DVB",19,W-2*M): c.drawString(M,y,ln); y-=25
    y-=6; c.setFont("DV",10)
    for l0 in lines:
        for ln in wrap(l0,"DV",10,W-2*M):
            if y<60: c.showPage(); fresh(c); c.setFont("DV",10); y=H-60
            c.drawString(M,y,ln); y-=13.5
        y-=3
    c.showPage()
def prompt_page(c,head,meta,prompt):
    fresh(c); c.setFont("DVB",14); y=H-54
    for ln in wrap(head,"DVB",14,W-2*M): c.drawString(M,y,ln); y-=18
    c.setFont("DV",8.5)
    for m0 in meta:
        for ln in wrap(m0,"DV",8.5,W-2*M): c.drawString(M,y,ln); y-=11.5
    y-=6; lines=wrap(prompt,"DV",9,W-2*M-24); h=len(lines)*12.2+24
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#DDD2C0")); c.roundRect(M,y-h,W-2*M,h,6,fill=1,stroke=1)
    c.setFillColor(INK); c.setFont("DV",9); yy=y-18
    for ln in lines: c.drawString(M+12,yy,ln); yy-=12.2
    c.showPage()
def video_page(c,v):
    fresh(c); c.setFont("DVB",14); y=H-54
    for ln in wrap(f"{v['n']} · {v['title']}","DVB",14,W-2*M): c.drawString(M,y,ln); y-=18
    c.setFont("DV",9); c.setFillColor(STONE); c.drawString(M,y,f"LENGTH: {v['length']} · SAVE AS: {v['file']}"); y-=18
    c.setFillColor(INK); c.setFont("DV",10)
    for st in v["steps"]:
        for i,ln in enumerate(wrap(st,"DV",10,W-2*M-14)):
            c.drawString(M+(0 if i==0 else 14),y,("• " if i==0 else "")+ln if i==0 else ln); y-=14
        y-=5
    c.showPage()
how=[
'WHY THESE ANGLES (read from our own ads, Nov 1-27): (1) The cold winner format is a loud split-screen COMPARISON with a clear question headline, two labelled halves, a 3-point benefit row, a price pill and a Shop Now button (gloves W01, 1,157 per order; Mocha H1, 1,173). (2) The warm winner format is a cinematic WORLD scene + a provocative statement headline + the price (Clifford "Not for everyone. That\'s the point." 744 per order; the bag ad "Leather bags are too expensive." Fair.). (3) A local, emotional scene works warm (chai dhaba, 1,002). (4) What lost: plain studio shots, close-ups alone, trust-only images with no reason to buy, multi-product bundles without a price, founder talking. The first pack I sent followed none of this; this one does.',
'PRODUCT ANGLES IN THIS PACK: Clifford = status / identity (2 tests). Gloves = comparison (cold) and cold-evening warmth (warm). Executive belt = buy it once. Gift = thoughtful. Jacket = made for you (held). ARMOUR, THOMAS and SHELBY: send me the benefits list and I add their prompts in the same two proven formats (comparison for cold, status/scene for warm), written only from facts you confirm.',
"HOW TO USE (images): open ChatGPT (GPT image), upload the product photo(s) and the Kordovan horse-head logo PNG named on each page, paste the WHOLE box (it is one self-contained prompt: size, product, scene, camera, light, every text line, logo, mood, do-nots), generate, check the text spelling and that the product is exactly as in the uploaded photo, then save as JPG with the name shown. Send the files back and Claude builds the ads (copy, UTM, placements) as PAUSED drafts for your yes.",
"SIZES: every ad image is 1080 x 1350 px, 4:5. Keep 4:5 only for now. All text sits 90+ px from the edges (Reels crop).",
"PRICES: honest full prices after Dec 1 (Clifford Rs 10,500, belt Rs 3,300, gloves Rs 1,950, cap Rs 1,950, jacket Rs 32,000). If a website price changed, tell me before you generate. CHECK every output: the product must match the uploaded photo exactly, the text spelled exactly as written, the logo the real one. Regenerate if anything is off.",
"RULES BAKED IN: handcrafted in Pakistan (never 'our workshop'); no coins; no city names; no faces; no invented customers, reviews or crafting scenes; jackets are top-grain sheepskin, made to order, about 3 weeks, paid online; cash on delivery only on in-stock items; no fake urgency; real proof (patina, used wallet) is filmed for real, never generated.",
"VIDEO RULES (apply to every clip): phone vertical (9:16 or 4:5), 1080p, 30 fps; window daylight, no lamps, no flash; plain desk (wood or linen); hands only, no face; no brand logos on watch/clothes/phone; steady (stack books or use a small tripod); the RESULT appears in the first 3 seconds (that is the hook); no talking, no music (Claude adds sound and text); 3 takes of the opening shot; send the files unedited and uncompressed (via Drive/WeTransfer, not WhatsApp).",
"ARMOUR, THOMAS and SHELBY: after you have gone through every benefit and feature, send me the list in writing (or voice-to-text). I will write the ad angles ONLY from facts you confirm and the product page, then add their image prompts to this pack. Until then I will not claim anything about them. Notes: Armour has 41 in stock at Rs 5,850; Shelby shows -2 and Thomas 0 (stock not real yet).",
]
def build():
    path=os.path.join(OUT,"Kordovan_Dec2026_AD_Creative_Pack.pdf"); c=canvas.Canvas(path,pagesize=A4)
    rows=[f"Ad {a['n']} · {a['utm']} · due {a['due']} · {a['title']}" for a in ADS]+[f"{v['n']} · {v['title']}" for v in VIDEOS]
    cover(c,"Kordovan: December 2026 AD creative pack v2 (7 image prompts + 6 video directions)",["Based on Alex's ads study (ops/marketing/ads/ADS_STUDY_NOV2026_AND_DEC_PLAN.md). One prompt per page, everything inside the box.",*how,"CONTENTS:",*rows])
    for a in ADS:
        meta=[f"ANGLE: {a['angle']}",f"UPLOAD: {a['upload']}",f"SAVE AS: AD{a['n']:02d}_{a['utm']}.jpg · DUE: {a['due']}",f"USED FOR: {a['where']}",f"UTM content tag: {a['utm']} (Claude adds the rest; every ad gets utm_term={{{{placement}}}})"]
        prompt_page(c,f"Ad {a['n']} · {a['title']}",meta,a["p"])
    for v in VIDEOS: video_page(c,v)
    c.save(); return path
if __name__=="__main__":
    print(build())
    dump="\n".join(a["p"] for a in ADS)+"\n"+"\n".join(" ".join(v["steps"]) for v in VIDEOS)
    banned=re.compile(r"croc|snake|ostrich|exotic|\bfur\b|cigar|smok|tobacco|karachi|lahore|islamabad|workshop|black friday|\bcoin|full-grain|only \d+ left",re.I)
    scrub=dump.replace("no coins anywhere","").replace("no city names","").replace('no word "workshop"','').replace('no "Black Friday"','').replace("Do NOT mention coins on screen or in the clip.","").replace("(never 'our workshop')","")
    print("BANNED HITS:",sorted(set(m.group(0).lower() for m in banned.finditer(scrub))))
