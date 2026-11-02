"""11.11 creative v4 — OFFER-FIRST. Free tools only: Pillow + ffmpeg.
Real Shopify product photos only (no card/ID imagery, Razor dropped). No generation, no retouching."""
import subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, "assets")
OUT = "/home/user/KDV/ops/marketing/creative"
os.makedirs(OUT, exist_ok=True)

ALABASTER = (247, 242, 234)
PARCHMENT = (236, 227, 212)
ESPRESSO = (36, 28, 22)
COGNAC = (160, 98, 58)
SADDLE = (192, 139, 92)
BRASS = (176, 137, 79)
STONE = (139, 129, 116)

FR = os.path.join(ROOT, "fonts", "Fraunces-500.ttf")
IN_R = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
IN_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
IN_SB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"

_fc = {}
def font(p, s):
    k = (p, int(s))
    if k not in _fc:
        _fc[k] = ImageFont.truetype(p, int(s))
    return _fc[k]

def img(name):
    return Image.open(os.path.join(A, name + ".png")).convert("RGB")

def tw(d, s, f):
    return d.textlength(s, font=f)

def fit(d, s, path, max_w, max_size):
    size = max_size
    while size > 10 and tw(d, s, font(path, size)) > max_w:
        size -= 2
    return font(path, size)

def tracked(d, xy_center_y, s, f, fill, W, track=0.12):
    """Letter-spaced uppercase line, centred."""
    sp = f.size * track
    widths = [tw(d, ch, f) for ch in s]
    total = sum(widths) + sp * (len(s) - 1)
    x = (W - total) / 2
    for ch, w in zip(s, widths):
        d.text((x, xy_center_y), ch, font=f, fill=fill)
        x += w + sp

def center(d, y, s, f, fill, W, x0=0):
    d.text((x0 + (W - tw(d, s, f)) / 2, y), s, font=f, fill=fill)

def text_h(f, s="25%OFF"):
    b = f.getbbox(s)
    return b[3] - b[1], b[1]

def fit_cover(im, w, h, zoom=1.0, yoff=0.5):
    s = max(w / im.width, h / im.height) * zoom
    nw, nh = int(im.width * s + 0.5), int(im.height * s + 0.5)
    r = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - w) // 2
    y = int((nh - h) * yoff)
    return r.crop((x, y, x + w, y + h))

def product_fit(im, w, h, zoom=1.0, crop_top=0.0):
    """Show the whole product: contain on its own (light) studio background; cover for dark macros."""
    if crop_top:
        im = im.crop((0, int(im.height * crop_top), im.width, im.height))
    corner = im.getpixel((4, 4))
    if sum(corner) < 450:  # dark macro shot -> fill the frame
        return fit_cover(im, w, h, zoom)
    s = min(w / im.width, h / im.height) * zoom
    nw, nh = int(im.width * s), int(im.height * s)
    r = im.resize((nw, nh), Image.LANCZOS)
    x, y = (w - nw) // 2, (h - nh) // 2
    if nh > h:  # zoomed past the frame height: crop centrally (product sits mid-frame in every source)
        r = r.crop((0, (nh - h) // 2, nw, (nh - h) // 2 + h)); y = 0; nh = h
    # seamless surround: solid fill in the photo's own edge colour, photo edges feathered into it
    edge = r.crop((0, 0, 6, nh)).resize((1, 1), Image.BOX).getpixel((0, 0))
    edge2 = r.crop((nw - 6, 0, nw, nh)).resize((1, 1), Image.BOX).getpixel((0, 0))
    fill = tuple((p + q) // 2 for p, q in zip(edge, edge2))
    bg = Image.new("RGB", (w, h), fill)
    mask = Image.new("L", (nw, nh), 255)
    md = ImageDraw.Draw(mask)
    fe = max(1, int(nw * 0.10))
    for i in range(fe):
        v = int(255 * i / fe)
        md.line([(i, 0), (i, nh)], fill=v)
        md.line([(nw - 1 - i, 0), (nw - 1 - i, nh)], fill=v)
    bg.paste(r, (x, y), mask)
    return bg

def zoom_frame(fr, z):
    """Scale whole frame by z (>=1) about centre and crop back to size."""
    if z <= 1.0001:
        return fr
    W, H = fr.size
    r = fr.resize((int(W * z), int(H * z)), Image.LANCZOS)
    x, y = (r.width - W) // 2, (r.height - H) // 2
    return r.crop((x, y, x + W, y + H))

# ------------------------------------------------------------------ building blocks
def offer_block(W, H, bg=ESPRESSO, full=False):
    """The hero offer: 11.11 SALE / 25% OFF / EVERY WALLET (+ secondary lines when full)."""
    fr = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(fr)
    m = int(W * 0.08)
    inner = W - 2 * m
    accent = SADDLE if bg == ESPRESSO else ALABASTER
    num = ALABASTER
    f_eyebrow = font(IN_SB, int(W * 0.034))
    f_1111 = fit(d, "11.11", FR, inner * 0.62, int(H * (0.22 if full else 0.30)))
    f_25 = fit(d, "25% OFF", FR, inner, int(H * (0.20 if full else 0.28)))
    f_ew = font(IN_SB, int(W * (0.045 if full else 0.05)))
    lines = [("eyebrow", "KORDOVAN  ·  11.11 SALE", f_eyebrow, BRASS if bg == ESPRESSO else PARCHMENT),
             ("big", "11.11", f_1111, num),
             ("big", "25% OFF", f_25, accent),
             ("track", "EVERY WALLET", f_ew, num)]
    if full:
        f_15 = fit(d, "15% off everything else.", FR, inner, int(W * 0.075))
        f_meta = font(IN_M, int(W * 0.04))
        lines += [("rule", None, None, None),
                  ("text", "15% off everything else.", f_15, num),
                  ("text", "10–12 November", f_meta, accent),
                  ("text", "No code needed.", font(IN_R, int(W * 0.036)), PARCHMENT if bg == ESPRESSO else ALABASTER)]
    gaps = {"eyebrow": 0.055, "big": 0.035, "track": 0.04, "rule": 0.035, "text": 0.022}
    # measure
    hs = []
    for kind, s, f, c in lines:
        if kind == "rule":
            hs.append(4)
        else:
            h, _ = text_h(f, s)
            hs.append(h)
    total = sum(hs) + sum(gaps[k] * H for k, *_ in lines[1:])
    y = (H - total) / 2
    for i, ((kind, s, f, c), h) in enumerate(zip(lines, hs)):
        if i:
            y += gaps[kind] * H
        if kind == "rule":
            d.line([(W * 0.38, y), (W * 0.62, y)], fill=BRASS, width=3)
        else:
            _, top = text_h(f, s)
            if kind in ("eyebrow", "track"):
                tracked(d, y - top, s, f, c, W, 0.16 if kind == "eyebrow" else 0.12)
            else:
                center(d, y - top, s, f, c, W)
        y += h
    return fr

def offer_band(W, h, bg=ESPRESSO):
    """Persistent badge band: 11.11 | 25% OFF EVERY WALLET, big enough for thumbnails."""
    band = Image.new("RGB", (W, h), bg)
    d = ImageDraw.Draw(band)
    m = int(W * 0.06)
    f_num = fit(d, "11.11", FR, W * 0.34, int(h * 0.62))
    xdiv0 = m + tw(d, "11.11", f_num) + int(W * 0.04)
    room = (W - m) - (xdiv0 + int(W * 0.05))  # right block must clear the divider by >=5% of width
    f_off = fit(d, "25% OFF", FR, min(W * 0.50, room), int(h * 0.50))
    ew_size = max(18, int(h * 0.13))
    while ew_size > 14:
        f_ew = font(IN_SB, ew_size)
        if sum(tw(d, c, f_ew) for c in "EVERY WALLET") + f_ew.size * 0.14 * 11 <= room:
            break
        ew_size -= 1
    nh, ntop = text_h(f_num, "11.11")
    d.text((m, (h - nh) / 2 - ntop), "11.11", font=f_num, fill=ALABASTER)
    # divider
    xdiv = m + tw(d, "11.11", f_num) + int(W * 0.04)
    d.line([(xdiv, h * 0.2), (xdiv, h * 0.8)], fill=BRASS, width=3)
    oh, otop = text_h(f_off, "25% OFF")
    eh, etop = text_h(f_ew, "EVERY WALLET")
    block = oh + h * 0.06 + eh
    y0 = (h - block) / 2
    xr = W - m
    acc = SADDLE if bg == ESPRESSO else ALABASTER
    d.text((xr - tw(d, "25% OFF", f_off), y0 - otop), "25% OFF", font=f_off, fill=acc)
    s = "EVERY WALLET"
    sp = f_ew.size * 0.14
    wtot = sum(tw(d, c, f_ew) for c in s) + sp * (len(s) - 1)
    x = xr - wtot
    for c in s:
        d.text((x, y0 + oh + h * 0.06 - etop), c, font=f_ew, fill=ALABASTER)
        x += tw(d, c, f_ew) + sp
    return band

def caption_strip(W, h, title, sub, bg=ALABASTER):
    s = Image.new("RGB", (W, h), bg)
    d = ImageDraw.Draw(s)
    f1 = font(FR, int(h * 0.36))
    f2 = font(IN_M, int(h * 0.17))
    h1, t1 = text_h(f1, title)
    h2, t2 = text_h(f2, sub)
    y = (h - (h1 + h * 0.1 + h2)) / 2
    center(d, y - t1, title, f1, ESPRESSO, W)
    center(d, y + h1 + h * 0.1 - t2, sub, f2, COGNAC, W)
    return s

# ------------------------------------------------------------------ statics
def c2(W, H, name):
    """Bastion static: offer hero top (~48%), Bastion pair below."""
    fr = Image.new("RGB", (W, H), PARCHMENT)
    oh = int(H * (0.48 if H / W < 1.5 else 0.50))
    fr.paste(offer_block(W, oh, ESPRESSO), (0, 0))
    d = ImageDraw.Draw(fr)
    strip = int(H * (0.12 if H / W < 1.5 else 0.11))
    ph = H - oh - strip
    gap = int(W * 0.03)
    pw = (W - 3 * gap) // 2
    pimg = ph - 2 * gap
    fr.paste(fit_cover(img("B1"), pw, pimg), (gap, oh + gap))
    fr.paste(fit_cover(img("BT1"), pw, pimg), (2 * gap + pw, oh + gap))
    y = H - strip
    d.rectangle([0, y, W, H], fill=ALABASTER)
    f1 = font(FR, int(strip * 0.34))
    f2 = font(IN_M, int(strip * 0.16))
    t1 = "Bastion. Brown ya Tan."
    t2 = "15% off everything else  ·  10–12 November  ·  No code needed"
    t2f = fit(d, t2, IN_M, W * 0.9, int(strip * 0.16))
    h1, o1 = text_h(f1, t1)
    h2, o2 = text_h(t2f, t2)
    yy = y + (strip - (h1 + strip * 0.12 + h2)) / 2
    center(d, yy - o1, t1, f1, ESPRESSO, W)
    center(d, yy + h1 + strip * 0.12 - o2, t2, t2f, COGNAC, W)
    fr.save(os.path.join(OUT, name), quality=95)

def c3():
    W = H = 1080
    # card 1: pure offer card on cognac
    offer_block(W, H, COGNAC, full=True).save(os.path.join(OUT, "C3_carousel_card1_1x1.jpg"), quality=95)
    cards = [
        ("B1", "Bastion", "Distressed cow leather", dict()),
        ("L1", "Luke", "Slim, vertical", dict()),
        ("A3", "Aristocrat", "Slim classic", dict()),
        ("K1", "KODO", "Crazy Horse leather, RFID", dict(crop_top=0.47, zoom=1.0)),  # crop out bank cards
        ("R4", "Razor", "RFID smart wallet", dict()),  # v5: Razor back, leather close-up (no cards)
    ]
    band_h = int(H * 0.36)
    strip_h = int(H * 0.15)
    for i, (n, t, s, kw) in enumerate(cards, 2):
        fr = Image.new("RGB", (W, H), ALABASTER)
        fr.paste(offer_band(W, band_h, ESPRESSO), (0, 0))
        ph = H - band_h - strip_h
        fr.paste(product_fit(img(n), W, ph, kw.get("zoom", 1.3), kw.get("crop_top", 0.0)), (0, band_h))
        fr.paste(caption_strip(W, strip_h, t, s + "  ·  10–12 November  ·  No code needed"), (0, H - strip_h))
        fr.save(os.path.join(OUT, f"C3_carousel_card{i}_1x1.jpg"), quality=95)

# ------------------------------------------------------------------ video
def render_video(path, scenes, W, H, fps=30, xfade=6):
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

def opener(W, H):
    base = offer_block(W, H, ESPRESSO)
    return lambda t: zoom_frame(base, 1.0 + 0.05 * (1 - t))  # settles in, readable from frame 0

def closer(W, H):
    base = offer_block(W, H, COGNAC, full=True)
    return lambda t: zoom_frame(base, 1.0 + 0.03 * t)

def product_scene(W, H, n, title, sub, kw=None):
    kw = kw or {}
    band_h = int(H * (0.24 if H / W > 1.5 else 0.30))
    strip_h = int(H * (0.13 if H / W > 1.5 else 0.15))
    ph = H - band_h - strip_h
    band = offer_band(W, band_h, ESPRESSO)
    strip = caption_strip(W, strip_h, title, sub)
    src = img(n)
    def f(t):
        fr = Image.new("RGB", (W, H), ALABASTER)
        fr.paste(band, (0, 0))
        fr.paste(product_fit(src, W, ph, 0.94 * (1.0 + 0.05 * t), kw.get("crop_top", 0.0)), (0, band_h))
        fr.paste(strip, (0, H - strip_h))
        return fr
    return f

def c1():
    W, H, fps = 1080, 1920, 30
    scenes = [(int(2.5 * fps), opener(W, H))]
    for n, t, s, kw in [("B1", "Bastion", "Distressed cow leather", None),
                        ("L1", "Luke", "Slim, vertical", None),
                        ("K4", "KODO", "Crazy Horse leather, RFID", None),
                        ("A3", "Aristocrat", "Slim classic", None),
                        ("R4", "Razor", "RFID smart wallet", None)]:
        scenes.append((int(1.5 * fps), product_scene(W, H, n, t, s, kw)))
    scenes.append((int(5.0 * fps), closer(W, H)))
    render_video(os.path.join(OUT, "C1_paanch_wallets_9x16_15s.mp4"), scenes, W, H, fps)

def c4(W, H, name):
    fps = 30
    scenes = [(60, opener(W, H)),
              (60, product_scene(W, H, "B1", "Bastion", "Leather wears in, not out.")),
              (60, closer(W, H))]
    render_video(os.path.join(OUT, name), scenes, W, H, fps)

if __name__ == "__main__":
    c2(1080, 1350, "C2_bastion_static_4x5.jpg")
    c2(1080, 1920, "C2_bastion_story_9x16.jpg")
    c3()
    c4(1080, 1920, "C4_bumper_9x16_6s.mp4")
    c4(1080, 1350, "C4_bumper_4x5_6s.mp4")
    c1()
    print("done")
