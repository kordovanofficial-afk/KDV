"""Render the four 11.11 concepts. Free tools only: Pillow + ffmpeg.
Real Shopify product photos only; no generation, no retouching of the product."""
import subprocess, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
OUT = "/home/user/KDV/ops/marketing/creative"
os.makedirs(OUT, exist_ok=True)

ALABASTER = (247, 242, 234)
PARCHMENT = (236, 227, 212)
ESPRESSO = (36, 28, 22)
COGNAC = (160, 98, 58)
STONE = (139, 129, 116)
BORDER = (221, 210, 192)

FR = os.path.join(ROOT, "fonts", "Fraunces-500.ttf")
IN_R = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
IN_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"

OFFER_1 = "11.11"
OFFER_2 = "25% off every wallet."
OFFER_3 = "15% off everything else."
DATES = "10–12 November"


def font(p, s):
    return ImageFont.truetype(p, s)


def img(name):
    return Image.open(os.path.join(A, name + ".png")).convert("RGB")


def text_c(d, y, s, f, fill, W):
    w = d.textlength(s, font=f)
    d.text(((W - w) / 2, y), s, font=f, fill=fill)


def fit_cover(im, w, h, zoom=1.0, pan=0.5, yoff=0.5):
    """Scale to cover w x h, apply zoom, crop centred (pan shifts horizontally 0..1)."""
    s = max(w / im.width, h / im.height) * zoom
    nw, nh = int(im.width * s + 0.5), int(im.height * s + 0.5)
    r = im.resize((nw, nh), Image.LANCZOS)
    x = int((nw - w) * pan)
    y = int((nh - h) * yoff)
    return r.crop((x, y, x + w, y + h))


# ---------------------------------------------------------------- C1 motion
def c1_frame(scene, t):
    """scene: dict(img, caption, kind), t in 0..1 progress within scene."""
    W, H = 1080, 1920
    fr = Image.new("RGB", (W, H), ALABASTER)
    d = ImageDraw.Draw(fr)
    if scene["kind"] == "end":
        b1, bt = img("B1"), img("BT1")
        pw, ph = 480, 600
        fr.paste(fit_cover(b1, pw, ph), (50, 360))
        fr.paste(fit_cover(bt, pw, ph), (550, 360))
        text_c(d, 1060, OFFER_1, font(FR, 120), ESPRESSO, W)
        text_c(d, 1230, OFFER_2, font(FR, 66), ESPRESSO, W)
        text_c(d, 1320, OFFER_3, font(FR, 66), ESPRESSO, W)
        text_c(d, 1440, DATES, font(IN_M, 44), COGNAC, W)
        text_c(d, 1560, "Hamare apne workshop se. Lifetime craftsmanship warranty.", font(IN_R, 32), STONE, W)
        text_c(d, 1610, "No code needed.", font(IN_R, 32), STONE, W)
        text_c(d, 1760, "KORDOVAN", font(IN_M, 36), ESPRESSO, W)
        return fr
    im = img(scene["img"])
    zoom = 1.0 + 0.06 * (t if scene.get("dir", 1) > 0 else 1 - t)
    pan = 0.5 + (t - 0.5) * 0.25 if scene.get("pan") else 0.5
    ph = 1350
    fr.paste(fit_cover(im, W, ph, zoom, pan), (0, 140))
    text_c(d, 1560, scene["caption"], font(FR, 72), ESPRESSO, W)
    if scene.get("sub"):
        text_c(d, 1665, scene["sub"], font(IN_R, 38), STONE, W)
    text_c(d, 1800, "11.11  ·  25% off every wallet", font(IN_M, 34), COGNAC, W)
    return fr


def render_video(path, scenes, W, H, fps=30, xfade=6):
    """scenes: list of (frames_count, fn(t)->Image). Simple crossfade of `xfade` frames."""
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
           "-shortest", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "128k", path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_last = None
    for n, fn in scenes:
        for i in range(n):
            t = i / max(n - 1, 1)
            f = fn(t)
            if prev_last is not None and i < xfade:
                f = Image.blend(prev_last, f, (i + 1) / (xfade + 1))
            p.stdin.write(f.tobytes())
        prev_last = fn(1.0)
    p.stdin.close()
    p.wait()
    assert p.returncode == 0, path


def c1():
    fps = 30
    sc = [
        dict(img="B1", caption="Paanch wallets.", sub="Bastion · distressed cow leather", kind="p"),
        dict(img="R4", caption="Razor.", sub="RFID smart wallet", kind="p"),
        dict(img="L1", caption="Luke.", sub="Slim, vertical", kind="p"),
        dict(img="K4", caption="KODO.", sub="Crazy Horse leather, RFID", kind="p"),
        dict(img="A3", caption="Aristocrat.", sub="Slim classic", kind="p", dir=-1),
        dict(kind="end"),
    ]
    scenes = [(int(2.5 * fps), (lambda s: (lambda t: c1_frame(s, t)))(s)) for s in sc]
    render_video(os.path.join(OUT, "C1_paanch_wallets_9x16_15s.mp4"), scenes, 1080, 1920, fps)


# ---------------------------------------------------------------- C2 static
def c2(W, H, name):
    fr = Image.new("RGB", (W, H), PARCHMENT)
    d = ImageDraw.Draw(fr)
    top = int(H * 0.06) if H / W < 1.5 else int(H * 0.15)
    text_c(d, top, "Bastion.", font(FR, int(W * 0.11)), ESPRESSO, W)
    text_c(d, top + int(W * 0.145), "Distressed cow leather. Brown ya Tan.", font(IN_R, int(W * 0.036)), STONE, W)
    pw = int(W * 0.47)
    ph = int(pw * 1.25)
    y = top + int(W * 0.23)
    fr.paste(fit_cover(img("B1"), pw, ph), (int(W * 0.025), y))
    fr.paste(fit_cover(img("BT1"), pw, ph), (W - pw - int(W * 0.025), y))
    sy = y + ph + int(W * 0.04)
    d.line([(int(W * 0.1), sy), (int(W * 0.9), sy)], fill=BORDER, width=2)
    text_c(d, sy + int(W * 0.03), "11.11  ·  25% off every wallet  ·  10–12 November", font(IN_M, int(W * 0.036)), COGNAC, W)
    text_c(d, sy + int(W * 0.085), "15% off everything else. No code needed.", font(IN_R, int(W * 0.03)), STONE, W)
    text_c(d, H - int(W * 0.08), "kordovanleather.com", font(IN_M, int(W * 0.032)), ESPRESSO, W)
    fr.save(os.path.join(OUT, name), quality=95)


# ---------------------------------------------------------------- C3 carousel
def c3():
    cards = [
        ("L3", "Andar se dekhiye.", "Luke · card stack aur bill slot"),
        ("R4", "Razor", "Premium leather, RFID smart wallet"),
        ("A3", "Aristocrat", "Card aur cash compartments"),
        ("K1", "KODO", "Crazy Horse leather, RFID"),
    ]
    W = H = 1080
    for i, (n, h, s) in enumerate(cards, 1):
        fr = Image.new("RGB", (W, H), ALABASTER)
        # K1 shows third-party bank cards at the top: crop to the wallet body only
        fr.paste(fit_cover(img(n), W, 860, 1.12 if n == "K1" else 1.0, yoff=1.0 if n == "K1" else 0.5), (0, 0))
        d = ImageDraw.Draw(fr)
        d.rectangle([0, 860, W, H], fill=ALABASTER)
        d.text((64, 885), h, font=font(FR, 64), fill=ESPRESSO)
        d.text((64, 975), s, font=font(IN_R, 34), fill=STONE)
        tag = "11.11 · 25% off every wallet"
        tw = d.textlength(tag, font=font(IN_M, 32))
        d.text((W - 64 - tw, 985), tag, font=font(IN_M, 32), fill=COGNAC)
        fr.save(os.path.join(OUT, f"C3_carousel_card{i}_1x1.jpg"), quality=95)
    # card 5: offer card
    fr = Image.new("RGB", (W, H), PARCHMENT)
    d = ImageDraw.Draw(fr)
    fr.paste(fit_cover(img("BT1"), 420, 525), (330, 50))
    text_c(d, 640, OFFER_1, font(FR, 110), ESPRESSO, W)
    text_c(d, 790, OFFER_2, font(FR, 52), ESPRESSO, W)
    text_c(d, 860, OFFER_3, font(FR, 52), ESPRESSO, W)
    text_c(d, 940, DATES + "  ·  hamare apne workshop se", font(IN_M, 32), COGNAC, W)
    text_c(d, 995, "No code needed.", font(IN_R, 30), STONE, W)
    fr.save(os.path.join(OUT, "C3_carousel_card5_1x1.jpg"), quality=95)


# ---------------------------------------------------------------- C4 bumper
def c4(W, H, name):
    fps = 30

    def macro(n, line):
        def f(t):
            fr = Image.new("RGB", (W, H), ESPRESSO)
            fr.paste(fit_cover(img(n), W, H, 1.0 + 0.08 * t), (0, 0))
            if line:
                d = ImageDraw.Draw(fr)
                fz = int(W * 0.085)
                d.rectangle([0, int(H * 0.78), W, int(H * 0.78) + int(fz * 1.9)], fill=(36, 28, 22))
                text_c(d, int(H * 0.78) + int(fz * 0.35), line, font(FR, fz), ALABASTER, W)
            return fr
        return f

    def end(t):
        fr = Image.new("RGB", (W, H), ALABASTER)
        d = ImageDraw.Draw(fr)
        cy = H // 2 - int(W * 0.2)
        text_c(d, cy, OFFER_1, font(FR, int(W * 0.13)), ESPRESSO, W)
        text_c(d, cy + int(W * 0.18), OFFER_2, font(FR, int(W * 0.06)), ESPRESSO, W)
        text_c(d, cy + int(W * 0.26), OFFER_3, font(FR, int(W * 0.06)), ESPRESSO, W)
        text_c(d, cy + int(W * 0.37), DATES + "  ·  Kordovan", font(IN_M, int(W * 0.04)), COGNAC, W)
        text_c(d, cy + int(W * 0.44), "No code needed.", font(IN_R, int(W * 0.032)), STONE, W)
        return fr

    scenes = [(45, macro("L4", None)), (45, macro("K4", "Leather wears in,")),
              (45, macro("A4", "not out.")), (45, end)]
    render_video(os.path.join(OUT, name), scenes, W, H, fps)


if __name__ == "__main__":
    c2(1080, 1350, "C2_bastion_static_4x5.jpg")
    c2(1080, 1920, "C2_bastion_story_9x16.jpg")
    c3()
    c4(1080, 1920, "C4_bumper_9x16_6s.mp4")
    c4(1080, 1350, "C4_bumper_4x5_6s.mp4")
    c1()
    print("done")
