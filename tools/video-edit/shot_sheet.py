"""Printable Mocha Mate founder-video shot sheet. Usage: shot_sheet.py <fontsdir> <out.pdf>"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, PageBreak)

F, OUT = sys.argv[1], sys.argv[2]
pdfmetrics.registerFont(TTFont("Fraunces", f"{F}/Fraunces.ttf"))
pdfmetrics.registerFont(TTFont("Inter", f"{F}/Inter-Regular.ttf"))
pdfmetrics.registerFont(TTFont("InterB", f"{F}/Inter-Bold.ttf"))
from reportlab.lib.fonts import addMapping
addMapping("Inter", 0, 0, "Inter"); addMapping("Inter", 1, 0, "InterB"); addMapping("Inter", 0, 1, "Inter"); addMapping("Inter", 1, 1, "InterB")

ESP, WAL, COG, PARCH, BORDER, STONE = (colors.HexColor(h) for h in
    ("#241C16", "#4A3528", "#A0623A", "#ECE3D4", "#DDD2C0", "#8B8174"))

def st(name, font="Inter", size=9.5, lead=None, color=ESP, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead or size * 1.35, textColor=color, **kw)

H1 = st("h1", "Fraunces", 26, 30)
H2 = st("h2", "Fraunces", 15, 19, spaceBefore=4, spaceAfter=4)
BODY = st("body")
SMALL = st("small", size=8.5, color=STONE)
LBL = st("lbl", "InterB", 7.5, color=STONE)
SAY = st("say", "InterB", 11, 15)
CAP = st("cap", "InterB", 10, 13, color=COG)
CODE = st("code", "Fraunces", 22, 24, color=colors.white)
CODEL = st("codel", "InterB", 7, 9, color=colors.white)
TITLE = st("title", "Fraunces", 14, 17)

# (code, title, purpose, framing, secs, do, say, headline)
HOOKS = [
 ("H1", "New vs. Six Months", "HOOK A: curiosity", "Top-down, both wallets on wood", "3s",
  "New wallet and your 6-month wallet side by side, flat on a wooden table. Window light from the side. "
  "Tap the old one with one finger on the word 'chhe'.",
  "Ek naya hai. Ek chhe mahine se roz meri jeb mein hai. Pehchaan saktay hain kaunsa?",
  "NEW vs. 6 MONTHS. Can you tell?"),
 ("H2", "The Secret Pocket", "HOOK B: pattern break", "Tight close-up, phone near the wallet", "3s",
  "Wallet fills the frame. SNAP the back button open (loud, close to the phone), pull out your real key.",
  "Har wallet mein ek chupi jeb honi chahiye. Meri wali mein yeh rehta hai.",
  "Every wallet needs a secret pocket."),
 ("H3", "Founder Honest Review", "HOOK C: trust", "Mid shot, you to camera, eye level", "3s",
  "Hold the worn wallet up next to your face. Look straight into the lens. Slight smile, no hard sell.",
  "Apne hi brand ka wallet chhe mahine istemal kiya. Ab imaandari se batata / batati hoon kaisa nikla.",
  "I tested my own wallet for 6 months."),
]
BODY_SCENES = [
 ("S1", "Who I Am", "Credibility", "Mid shot, to camera", "4s",
  "Wallet in hand, relaxed. This is YOUR wallet. Say it like a fact, not a pitch.",
  "Main [naam], Kordovan ka founder. Yeh hai Mocha Mate, aur yeh meri apni hai, display wali nahi.",
  "Founder, Kordovan · my own wallet"),
 ("S2", "The Secret Pocket (demo)", "Feature 1: the reason to buy", "Macro close-up", "6s",
  "Snap the button again. Take out what's REALLY in there (key, emergency note). Put it back, snap shut.",
  "Peeche button wali jeb. Meri mein ghar ki spare chaabi rehti hai, aur ek emergency note, jo tab yaad aata hai jab sach mein zaroorat ho.",
  "The pocket for things you can't lose"),
 ("S3", "CNIC Window", "Feature 2: daily-life pain", "Close-up, hands only", "5s",
  "Slide your CNIC halfway out of the window and back, slowly. Then hold the wallet open toward camera.",
  "CNIC is window mein. Naaka ho ya bank, bas dikhao. Nikalne ki zaroorat nahi.",
  "CNIC window: show it, don't dig"),
 ("S4", "Everything Inside", "Capacity without bulk", "Close-up, then pocket shot", "6s",
  "Cards in one by one, notes in, close it, slide into your back jeans pocket. Pat the pocket.",
  "Andar chhe cards tak, notes ki poori jagah, aur phir bhi jeb mein bhaari nahi lagta.",
  "Up to 6 cards · cash pocket · still slim"),
 ("S5", "The Patina Proof", "THE MONEY SHOT", "Top-down, then slow tilt in window light", "7s",
  "Both wallets side by side again. Point to each. Then pick up the old one and tilt it slowly so the light catches the colour.",
  "Yeh naya hai. Yeh chhe mahine purana. Asli leather ghista nahi, rang pakadta hai.",
  "Real leather doesn't wear out. It ages."),
 ("S6", "Stitching + Warranty", "Risk removal", "Macro on the stitching", "5s",
  "Run your thumb slowly along the stitching of the OLD wallet.",
  "Silai abhi tak waisi hai. Aur waise bhi, har silai par lifetime warranty hai.",
  "Lifetime craftsmanship warranty"),
 ("S7", "150+ People", "Social proof", "Mid shot, to camera", "3s",
  "Wallet in hand, to camera.",
  "Pichle saal ek sau pachaas se zyada logon ne yeh wallet liya.",
  "150+ sold this year"),
 ("S8", "The Offer", "Call to action", "Mid shot, wallet held toward lens", "5s",
  "Hold the wallet toward the lens. Clear and calm. Point down at the end ('link neeche').",
  "Teen hazaar do sau rupay. Online pay karein ya cash on delivery. Link neeche.",
  "Rs 3,200 · Cash on delivery · Link below"),
 ("S9", "Your Secret Pocket? (Instagram/Facebook post only)", "Comments = reach", "Mid shot, to camera", "3s",
  "Raise the wallet, a little smile. A question, not a sales line.",
  "Aur batayein, aap ke wallet ki chupi jeb mein kya hai? Comment mein likhein.",
  "What's in YOUR secret pocket? Comment"),
]
BROLL = [
 ("B1", "Button snap", "Macro. Open + snap shut ×3. Phone close so the sound is crisp."),
 ("B2", "Key out of the pocket", "Macro. Key slides out of the back pocket, then back in."),
 ("B3", "CNIC slide", "Close-up. CNIC slides out of the window and back."),
 ("B4", "Side-by-side push-in", "Top-down, both wallets. Move the phone slowly toward them (5s)."),
 ("B5", "Patina in light", "Old wallet tilted slowly in window light (5s)."),
 ("B6", "Pocket in / out", "Wallet going into a back jeans pocket and coming out."),
 ("B7", "Daily life", "Wallet on a car dashboard · next to chai on a café table · grabbed at the door."),
 ("B8", "Workshop (optional)", "Hands stitching or cutting leather, if you can film there."),
]

def scene_card(sc):
    code, title, purpose, framing, secs, do, say, head = sc
    left = Table([[Paragraph(code, CODE)], [Paragraph("SCENE", CODEL)]], colWidths=[20 * mm])
    left.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), COG), ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                              ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 6)]))
    right = [
        [Paragraph(title, TITLE), Paragraph(f"{purpose}<br/>{framing} · ~{secs}", SMALL)],
        [Paragraph("WHAT TO DO", LBL), ""], [Paragraph(do, BODY), ""],
        [Paragraph("SAY (your words become the captions)", LBL), ""], [Paragraph(f"“{say}”", SAY), ""],
        [Paragraph("ON-SCREEN HEADLINE (added in the edit)", LBL), ""], [Paragraph(head, CAP), ""],
        [Paragraph("TAKES:  □ 1    □ 2    □ 3      ★ best take: ____", SMALL), ""],
    ]
    rt = Table(right, colWidths=[95 * mm, 55 * mm])
    rt.setStyle(TableStyle([("SPAN", (0, i), (1, i)) for i in range(1, 8)] +
                           [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    card = Table([[left, rt]], colWidths=[22 * mm, 152 * mm])
    card.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, BORDER), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("BACKGROUND", (1, 0), (1, 0), colors.white), ("LEFTPADDING", (0, 0), (0, 0), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    return KeepTogether([card, Spacer(1, 4 * mm)])

def boxed(rows, widths, head=True):
    t = Table(rows, colWidths=widths)
    style = [("GRID", (0, 0), (-1, -1), 0.5, BORDER), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if head:
        style += [("BACKGROUND", (0, 0), (-1, 0), PARCH)]
    t.setStyle(TableStyle(style))
    return t

def footer(c, d):
    c.saveState(); c.setFont("Inter", 7.5); c.setFillColor(STONE)
    c.drawString(18 * mm, 10 * mm, "KORDOVAN · Mocha Mate founder video · shot sheet")
    c.drawRightString(192 * mm, 10 * mm, f"page {d.page}"); c.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm,
                        bottomMargin=16 * mm, title="Mocha Mate Founder Video: Shot Sheet", author="Kordovan")
P = lambda t, s=BODY: Paragraph(t, s)
story = [
    P("Mocha Mate: Founder Video", H1),
    P("Six months in my pocket. An honest founder review that sells.", st("sub", "Fraunces", 12, 16, COG)),
    Spacer(1, 5 * mm),
    P("The one rule that makes editing easy", H2),
    boxed([[P("<b>Before EVERY take, say the code out loud:</b> “Scene H1, take 1”. Then wait 2 seconds and start. "
              "For silent shots: “B-roll B3”. I find and sort every clip from this. No renaming, no folders.", BODY)]],
          [174 * mm], head=False),
    Spacer(1, 4 * mm),
    P("Why this ad stops the scroll", H2),
    boxed([[P("<b>What happens on screen</b>", BODY), P("<b>Why it works</b>", BODY)],
           [P("Second 0: motion + sound (the button SNAP, or two wallets side by side)", BODY),
            P("The first second decides the scroll. No logo, no intro, no 'hello'.", BODY)],
           [P("A question in the first line (“Pehchaan saktay hain kaunsa?”)", BODY),
            P("The brain wants the answer, so people keep watching.", BODY)],
           [P("Your REAL 6-month wallet next to a new one", BODY),
            P("Proof, not a claim. Nobody else in Pakistan is showing leather that ages.", BODY)],
           [P("CNIC window + checkpoint/bank line", BODY),
            P("Everyone has dug for their CNIC. It's instantly relatable.", BODY)],
           [P("Founder voice, honest tone, no hard sell", BODY),
            P("Trust is what converts in a COD market. Ads that feel like ads get skipped.", BODY)],
           [P("Price + COD + warranty in the last 5 seconds", BODY),
            P("Removes the three objections right before the click.", BODY)]],
          [88 * mm, 86 * mm]),
    Spacer(1, 4 * mm),
    P("Before you press record", H2),
    boxed([[P("□ Phone <b>vertical</b>, 1080p, 30fps   □ Lens wiped   □ Tap and hold to lock focus and exposure<br/>"
              "□ Window light from the <b>side</b>, never behind you   □ Fan / AC off, quiet room<br/>"
              "□ Plain wall or wooden desk   □ Plain dark shirt, no logos   □ Look into the <b>lens</b>, not the screen<br/>"
              "□ Props: your 6-month Mocha Mate · a NEW Mocha Mate · your real key · CNIC · cards · notes<br/>"
              "□ Don't memorise: read the line, look up, say it. 2–3 takes each. 2-second pause before and after.<br/>"
              "□ At the end: <b>10 seconds of silence</b> in the same room (“Room tone”, then quiet).", BODY)]],
          [174 * mm], head=False),
    Spacer(1, 3 * mm),
    P("Honesty rules: only show what's REALLY in your back pocket. The old wallet must be your real 6-month one. "
      "No numbers beyond 150+.", SMALL),
    PageBreak(),
    P("Hooks: film all three", H2),
    P("Each is the first 3 seconds of a different version. Meta tests which one stops the most thumbs, and we put "
      "the budget behind the winner.", SMALL),
    Spacer(1, 3 * mm),
] + [scene_card(s) for s in HOOKS] + [
    PageBreak(), P("The story: film in this order", H2),
    P("Same body for every hook. Scenes S1–S8 = the ad. S9 is for the organic Instagram/Facebook post only.", SMALL),
    Spacer(1, 3 * mm),
] + [scene_card(s) for s in BODY_SCENES] + [
    Spacer(1, 2 * mm), P("B-roll: silent shots (5–10s each)", H2),
    P("Say “B-roll B1” etc. before each. These are what make it feel premium.", SMALL), Spacer(1, 2 * mm),
    boxed([[P("<b>Code</b>", BODY), P("<b>Shot</b>", BODY), P("<b>How</b>", BODY), P("<b>Done</b>", BODY)]] +
          [[P(f"<b>{c}</b>", BODY), P(t, BODY), P(h, BODY), P("□", BODY)] for c, t, h in BROLL],
          [14 * mm, 38 * mm, 108 * mm, 14 * mm]),
    Spacer(1, 5 * mm),
    P("What you get back from the edit", H2),
    boxed([[P("<b>Version</b>", BODY), P("<b>Scenes</b>", BODY), P("<b>Use</b>", BODY)],
           [P("Master ~50s", BODY), P("Hook + S1–S8", BODY), P("Main ad, Facebook feed", BODY)],
           [P("30s", BODY), P("Hook + S2, S3, S5, S8", BODY), P("Reels + Stories ads", BODY)],
           [P("15s", BODY), P("Hook + S5 + S8", BODY), P("Retargeting, Stories", BODY)],
           [P("Organic Reel", BODY), P("Hook A + S1–S9", BODY), P("Instagram/Facebook post (comment question)", BODY)]],
          [40 * mm, 56 * mm, 78 * mm]),
    Spacer(1, 2 * mm),
    P("3 hooks × 3 ad lengths = 9 ad versions from one shoot. Captions are your own words, word by word, the "
      "spoken word highlighted in cognac; the headline is added on top for people watching without sound.", SMALL),
]
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("ok", OUT)
