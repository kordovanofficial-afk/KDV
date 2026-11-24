import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data import FEED, STORIES
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"); os.makedirs(OUT, exist_ok=True)

REALISM = ("REALISM: it must look like a real photograph taken on a recent flagship phone by a person, not a render: natural depth of field, "
 "very light sensor grain, slightly imperfect framing and horizon, true-to-life colour, believable soft shadows and reflections. Leather shows real grain, "
 "pores, micro-creases and painted edges, never airbrushed or plastic; stitching is individual and slightly uneven like handwork. No HDR glow, no "
 "oversaturation, no symmetrical catalogue perfection, no lens flare, no AI sheen.")
DONT = ("DO NOT: no coins anywhere, no city names, no word \"workshop\", no \"Black Friday\", no \"only X left\", no countdown clocks, no sale bursts, no stars or "
 "review quotes, no faces or heads (hands cropped at the wrist are fine), no visible third-party brand logos on phones, watches, cars or clothes, no extra products "
 "beyond those described, no redesign of the uploaded product, no added patterns or embossing on the leather, no people cooking or crafting, no misspelled or "
 "extra text beyond the exact lines given, no watermark, no borders, no frames.")

def logo_colour(text):
    return "Espresso #241C16" if "Espresso" in text else "Alabaster #F7F2EA"

def feed_prompt(p):
    return (f"Create ONE photorealistic Instagram FEED photo. SIZE: exactly 1080 x 1350 pixels, vertical 4:5 ratio, sRGB, sharp, high resolution JPG, no borders. "
      f"PRODUCT: use the uploaded product photo of {p['prod']} EXACTLY as it is: same shape, proportions, panels, stitching, hardware, logo position and leather colour; do not redesign or recolour it. "
      f"SCENE: {p['scene']}. COMPOSITION: {p['comp']}. CAMERA: {p['cam']}. LIGHT: {p['light']}. COLOUR PALETTE: {p['pal']}. "
      f"IMAGE TONE: {p['tone_i']}. PRODUCT TONE: {p['tone_p']}. "
      f"LOGO: {p['logo']}. TEXT: {p['text']}; use only these exact words and nothing else. {REALISM} {DONT}")

def story_prompt(s):
    lc = logo_colour(s["text"])
    if s.get("real"):
        return (f"REAL PHONE PHOTO (no GPT image needed for this day). SHOOT: {s['real']} Take it vertical on your phone, daylight, no filter, no flash; leave the top 260 px and bottom 420 px of the frame empty. "
                f"Send the photo to Claude and Claude adds the Kordovan logo ({lc}, centred) and the text on top, then schedules it. TEXT TO ADD: {s['text']}. STICKER: {s['sticker']}. "
                f"DO NOT show faces, customer names or addresses, coins, or any other brand's logo.")
    pr = ("PRODUCT: none; this image has no product. " if s.get("noprod") else f"PRODUCT: use the uploaded product photo(s) of {s['prod']} EXACTLY as shown: same shape, proportions, stitching, hardware and leather colour; do not redesign or recolour. ")
    return (f"Create ONE photorealistic Instagram STORY image. SIZE: exactly 1080 x 1920 pixels, vertical 9:16 ratio, sRGB, sharp, high resolution JPG, no borders. "
      f"SAFE ZONES: keep the top 260 px and the bottom 420 px free of any text or important detail (the profile bar sits at the top; the reply bar and sticker sit at the bottom); all text and the product sit between y=260 and y=1500. "
      f"{pr}"
      f"SCENE: {s['scene']}. COMPOSITION: {s['comp']}. CAMERA: {s['cam']}. LIGHT: {s['light']}. COLOUR PALETTE: {s['pal']}. "
      f"IMAGE TONE: {s['tone_i']}. PRODUCT TONE: {s['tone_p']}. "
      f"LOGO: the uploaded Kordovan horse-head logo PNG exactly as supplied (do not redraw), recoloured {lc}, 100 px wide, centred at y=320. "
      f"TEXT: {s['text']}; use only these exact words and nothing else; add a very soft dark gradient behind text only if needed for legibility. "
      f"{REALISM} {DONT}")

def utm(link, medium, camp, content):
    if not link: return ""
    sep = "&" if "?" in link else "?"
    return f"https://kordovanleather.com{link}{sep}utm_source=instagram&utm_medium={medium}&utm_campaign={camp}&utm_content={content}"

TERRA = HexColor("#A0623A"); INK = HexColor("#241C16"); BG = HexColor("#F7F2EA"); STONE = HexColor("#8B8174")

def wrap(text, font, size, width):
    return simpleSplit(text, font, size, width)

def page_prompt(c, head, sub, meta_lines, prompt, extra=None):
    W, H = A4; m = 42
    c.setFillColor(BG); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont("DVB", 15); y = H - 54
    for ln in wrap(head, "DVB", 15, W - 2*m): c.drawString(m, y, ln); y -= 19
    c.setFont("DV", 9); c.setFillColor(STONE)
    for ln in wrap(sub, "DV", 9, W - 2*m): c.drawString(m, y, ln); y -= 12
    c.setFillColor(INK); c.setFont("DV", 8.5); y -= 4
    for ln0 in meta_lines:
        for ln in wrap(ln0, "DV", 8.5, W - 2*m): c.drawString(m, y, ln); y -= 11.5
    y -= 6
    lines = wrap(prompt, "DV", 9.2, W - 2*m - 24)
    h = len(lines) * 12.6 + 24
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#DDD2C0")); c.roundRect(m, y - h, W - 2*m, h, 6, fill=1, stroke=1)
    c.setFillColor(INK); c.setFont("DV", 9.2); yy = y - 18
    for ln in lines: c.drawString(m + 12, yy, ln); yy -= 12.6
    y = y - h - 16
    if extra:
        c.setFont("DVB", 9); c.setFillColor(TERRA); c.drawString(m, y, "CAPTION + HASHTAGS (copy-paste)"); y -= 13
        c.setFont("DV", 9); c.setFillColor(INK)
        for ln0 in extra.split("\n"):
            for ln in wrap(ln0, "DV", 9, W - 2*m): c.drawString(m, y, ln); y -= 12
    c.showPage()

def cover(c, title, lines):
    W, H = A4; m = 50
    def fresh():
        c.setFillColor(BG); c.rect(0, 0, W, H, fill=1, stroke=0); c.setFillColor(INK)
    fresh(); c.setFont("DVB", 20); y = H - 80
    for ln in wrap(title, "DVB", 20, W - 2*m): c.drawString(m, y, ln); y -= 26
    y -= 8; c.setFont("DV", 10)
    for ln0 in lines:
        for ln in wrap(ln0, "DV", 10, W - 2*m):
            if y < 60: c.showPage(); fresh(); c.setFont("DV", 10); y = H - 60
            c.drawString(m, y, ln); y -= 14
        y -= 3
    c.showPage()

how = [
 "HOW TO USE: for each page, open ChatGPT (GPT image), upload the product photo(s) named under UPLOAD plus the Kordovan logo PNG, paste the whole box, and generate. Save the result as JPG with the file name shown. Send the finished images back and Claude schedules them (time + link sticker are on each page).",
 "REALISM TIPS: if an image looks too glossy, add 'less polished, more like a phone photo' and regenerate; if the product shape drifts, say 'copy the uploaded product exactly'. Always check text spelling and that the logo is the real one.",
 "RULES BAKED IN: handcrafted in Pakistan (never 'our workshop'); no coins; no city names; no faces; no invented customers, reviews or crafting scenes; jackets are top-grain sheepskin, made to order, about 3 weeks, paid online (no cash on delivery); free delivery over Rs 5,500; cash on delivery on everything except made-to-order jackets and shoes. Days marked REAL PHONE PHOTO use your own phone photo, not GPT (real proof stays real).",
]

def build_feed():
    path = os.path.join(OUT, "Kordovan_Dec2026_FEED_Post_Prompts_12.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    rows = [f"Post {p['n']:>2} · {p['date']} · {p['pillar']} · {p['title']}" for p in FEED]
    cover(c, "Kordovan — December 2026 Instagram Feed: 12 post prompts", ["Posting days: Tue / Thu / Sat, 9:00 pm PKT. Size 1080 x 1350 (4:5).", *how, "THE 12 POSTS:", *rows])
    for p in FEED:
        meta = ([p["real_option"]] if p.get("real_option") else []) + [f"UPLOAD: {p['upload']}", f"POST: {p['date']} at 9:00 pm PKT · pillar: {p['pillar']} · save as: DEC_post{p['n']:02d}.jpg",
                (f"LINK (bio / DM): {utm(p['link'],'organic','dec_2026','post'+str(p['n']))}" if p['link'] else "LINK: none")]
        page_prompt(c, f"Post {p['n']} · {p['date']} · {p['title']}", "Copy the whole box below into GPT with the uploads.", meta, feed_prompt(p), p["cap"] + "\n" + p["tags"])
    c.save(); return path

def build_stories():
    path = os.path.join(OUT, "Kordovan_Dec2026_STORY_Prompts_30.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    rows = [f"Day {s['d']:>2} · {s['wd']} {s['d']} Dec · {s['type']} · {s['title']}" + ("  [REAL PHOTO]" if s.get("real") else "  [GPT]") for s in STORIES]
    cover(c, "Kordovan — December 2026 Instagram Stories: 30 story prompts", ["One story a day, 9:00 pm PKT. Size 1080 x 1920 (9:16). Add the sticker named on each page inside Instagram.", *how, "THE 30 STORIES:", *rows])
    for s in STORIES:
        meta = [("SOURCE: REAL PHONE PHOTO" if s.get("real") else f"UPLOAD: {s['upload']}"), f"POST: {s['wd']} {s['d']} Dec at 9:00 pm PKT · type: {s['type']} · save as: DEC_story{s['d']:02d}.jpg",
                f"STICKER: {s['sticker']}" + (f" -> {utm(s['link'],'story','dec_2026','d'+str(s['d']))}" if s['link'] else "")]
        page_prompt(c, f"Day {s['d']} · {s['wd']} {s['d']} Dec · {s['title']}", "Copy the whole box below into GPT with the uploads.", meta, story_prompt(s))
    c.save(); return path

def dump_md():
    out = ["# Kordovan Dec 2026 organic plan: prompt dump (for review)\n", "## FEED"]
    for p in FEED: out += [f"### Post {p['n']} {p['date']} {p['title']}", feed_prompt(p), f"CAPTION: {p['cap']}\n{p['tags']}\n"]
    out += ["## STORIES"]
    for s in STORIES: out += [f"### Day {s['d']} {s['title']}", story_prompt(s), f"STICKER: {s['sticker']}\n"]
    open(os.path.join(OUT, "prompts_dump.md"), "w").write("\n".join(out))

if __name__ == "__main__":
    print(build_feed()); print(build_stories()); dump_md()
    banned = re.compile(r"croc|snake|ostrich|exotic|\bfur\b|cigarette|smok|tobacco|lighter|karachi|lahore|islamabad|workshop|black friday|\bcoin", re.I)
    txt = open(os.path.join(OUT, "prompts_dump.md")).read()
    scrub = txt.replace('no coins anywhere','').replace('no city names','').replace('no word "workshop"','').replace('no "Black Friday"','')
    print("BANNED HITS:", sorted(set(m.group(0).lower() for m in banned.finditer(scrub))))
