"""Kordovan 11.11 teasers (T1 "Something is being made", T2 "Mark the date").

Free tools only: Pillow + numpy for every frame, ffmpeg (libx264) for the MP4s.
Real Shopify product photographs only, used unretouched: crop, scale, a slow
push-in, a warm grade and a moving light. Nothing is generated.

    python3 teaser.py                          # all four MP4s + 12 review frames
    python3 teaser.py --dateline "Starts tomorrow"   # re-version T2's date line

Rules baked in (see TEASERS.md): no discount %, no rupee price, no Karachi,
no Razor photos, no card/ID imagery, no exclamation marks, "11.11" + the date
on screen by 2 s and again at the end, text inside the middle ~80% vertically.
"""
import argparse, os, subprocess, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("KDV_TEASER_SRC", os.path.join(ROOT, "_src"))   # photo cache (git-ignored)
FRAMES = os.path.join(ROOT, "frames")
FR = os.path.join(ROOT, "fonts", "Fraunces-500.ttf")                 # Fraunces Medium, OFL
IN_R = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
IN_M = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
FPS = 30

# Quiet Heritage
ALABASTER = (247, 242, 234)
PARCHMENT = (236, 227, 212)
ESPRESSO = (36, 28, 22)
WALNUT = (74, 53, 40)
COGNAC = (160, 98, 58)
SADDLE = (192, 139, 92)
BRASS = (176, 137, 79)
STONE = (139, 129, 116)

# Source photos: same Shopify Files URLs as ops/marketing/2026-11_1111_ad_creative.md §2.
# Deliberately NOT used: every Razor shot (R1/R3/R4/RAB), and anything showing a card
# or ID (B2, B3, BT2, L2, L3, K1, K2, A3).
URLS = {
    "L4": "https://cdn.shopify.com/s/files/1/0267/9164/1277/files/LUKE_4.png?v=1784650360",
    "A4": "https://cdn.shopify.com/s/files/1/0267/9164/1277/files/AristocratBrown4.png?v=1784571309",
    "K4": "https://cdn.shopify.com/s/files/1/0267/9164/1277/files/RFIDProtectedKODOSmartWalletBlack4.png?v=1784533454",
    "BT1": "https://cdn.shopify.com/s/files/1/0267/9164/1277/files/Bastiontan1_a59beb11-dc8e-494d-a67d-1c3d3a5aa764.png?v=1784817045",
}

_cache = {}


def photo(name):
    if name not in _cache:
        os.makedirs(SRC, exist_ok=True)
        p = os.path.join(SRC, name + ".png")
        if not os.path.exists(p):
            urllib.request.urlretrieve(URLS[name], p)
        _cache[name] = Image.open(p).convert("RGB")
    return _cache[name]


def font(p, s):
    return ImageFont.truetype(p, int(s))


def ease(t):
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


def ramp(t, a, b):
    """0 before a, 1 after b, smooth in between (times in seconds)."""
    return ease((t - a) / (b - a)) if b > a else float(t >= a)


# ---------------------------------------------------------------- grade + light
def espresso_grade(im, darken=0.78, gamma=1.12):
    """Warm, darker, and shadows lifted to Espresso instead of black (no blue cast)."""
    a = np.asarray(im).astype(np.float32) / 255.0
    a = (a ** gamma) * darken
    a *= np.array([1.04, 1.0, 0.90], np.float32)               # pull blue down, warm up
    e = np.array(ESPRESSO, np.float32)
    out = e + np.clip(a, 0, 1) * (255.0 - e)                    # black point -> Espresso
    return Image.fromarray(out.astype(np.uint8))


_grid = {}


def diag(W, H):
    """0..1 coordinate running diagonally top-left -> bottom-right, for light sweeps."""
    if (W, H) not in _grid:
        y, x = np.mgrid[0:H, 0:W].astype(np.float32)
        _grid[(W, H)] = (x + 0.55 * y) / (W + 0.55 * H)
    return _grid[(W, H)]


def brass_sweep(fr, c, k=0.22, width=0.09):
    """Screen-blend a soft Antique Brass band centred at diagonal position c."""
    if k <= 0 or c < -0.3 or c > 1.3:
        return fr
    band = np.exp(-((diag(*fr.size) - c) / width) ** 2)[..., None] * k
    a = np.asarray(fr).astype(np.float32)
    lit = 255.0 - (255.0 - a) * (255.0 - np.array(BRASS, np.float32) * band) / 255.0
    return Image.fromarray(np.clip(lit, 0, 255).astype(np.uint8))


def vignette(W, H, strength=0.55, cy=0.5):
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H * cy) / (H / 2)) ** 2)
    return np.clip((r - 0.35) / 0.9, 0, 1) ** 1.4 * strength


def apply_mask_to_espresso(fr, m):
    """Blend frame toward Espresso by mask m (H x W, 0..1)."""
    a = np.asarray(fr).astype(np.float32)
    e = np.array(ESPRESSO, np.float32)
    return Image.fromarray((a * (1 - m[..., None]) + e * m[..., None]).astype(np.uint8))


def push(im, W, H, cx, cy, w0, w1, t):
    """Smooth sub-pixel push-in: crop box width w0 -> w1 around (cx, cy), output W x H."""
    w = w0 + (w1 - w0) * ease(t)
    h = w * H / W
    if h > im.height:
        h = im.height; w = h * W / H
    x0 = min(max(cx - w / 2, 0), im.width - w)
    y0 = min(max(cy - h / 2, 0), im.height - h)
    return im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + w, y0 + h))


# ---------------------------------------------------------------- type
def fit(d, s, path, size, maxw):
    f = font(path, size)
    while d.textlength(s, font=f) > maxw and size > 10:
        size *= 0.96
        f = font(path, size)
    return f


def text_layer(W, H, items):
    """items: (text, font_path, size, colour, y_centre_px). Returns RGBA, centred lines."""
    L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    for s, p, size, col, yc in items:
        f = fit(d, s, p, size, W * 0.86)
        x0, y0, x1, y1 = d.textbbox((0, 0), s, font=f)
        d.text(((W - (x1 - x0)) / 2 - x0, yc - (y1 - y0) / 2 - y0), s, font=f, fill=col + (255,))
    return L


def over(fr, layer, a):
    if a <= 0:
        return fr
    top = fr.convert("RGBA")
    top.alpha_composite(layer)
    return Image.blend(fr, top.convert("RGB"), min(a, 1.0))


def lit_numerals(W, H, s, size, yc, c, base=ALABASTER, glint=BRASS):
    """'11.11' in Fraunces with a brass glint travelling through the glyphs (RGBA)."""
    L = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(L)
    f = fit(d, s, FR, size, W * 0.9)
    x0, y0, x1, y1 = d.textbbox((0, 0), s, font=f)
    d.text(((W - (x1 - x0)) / 2 - x0, yc - (y1 - y0) / 2 - y0), s, font=f, fill=255)
    band = np.exp(-((diag(W, H) - c) / 0.07) ** 2)[..., None]
    col = np.array(base, np.float32) * (1 - band) + np.array(glint, np.float32) * band
    rgba = np.dstack([col, np.asarray(L, np.float32)]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA"), (y1 - y0)


def underline(fr, W, yc, half, prog, col=COGNAC, th=4):
    if prog <= 0:
        return fr
    d = ImageDraw.Draw(fr)
    hw = half * ease(prog)
    d.rectangle([W / 2 - hw, yc - th / 2, W / 2 + hw, yc + th / 2], fill=col)
    return fr


# ---------------------------------------------------------------- encoder
def encode(path, W, H, frame_fn, dur, grabs):
    """Pipe raw RGB frames into ffmpeg. Silent stereo AAC track added (Meta prefers a track)."""
    n = int(round(dur * FPS))
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
           "-shortest", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
           "-pix_fmt", "yuv420p",            # plays everywhere incl. older phones
           "-movflags", "+faststart",        # moov atom first so the feed can start instantly
           "-c:a", "aac", "-b:a", "128k", path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    want = {int(round(g * FPS)): g for g in grabs}
    base = os.path.splitext(os.path.basename(path))[0]
    for i in range(n):
        f = frame_fn(i / FPS)
        p.stdin.write(f.tobytes())
        if i in want:
            f.save(os.path.join(FRAMES, f"{base}_t{want[i]:.1f}s.jpg"), quality=90)
    p.stdin.close(); p.wait()
    assert p.returncode == 0, path
    print(path)


# ---------------------------------------------------------------- T1
T1_SCENES = [  # (start, end, photo, cx, cy, w_start, w_end, line)  boxes in source px
    (0.0, 3.0, "L4", 861, 938, 522, 470, None),            # right-hand stitch line, mark out of frame
    (3.0, 5.5, "A4", 860, 900, 560, 500, "Something is being made."),
    (5.5, 8.0, "L4", 330, 1060, 600, 540, "Slowly, in our own workshop."),
    (8.0, 10.6, "K4", 520, 760, 760, 640, "Leather. Thread. Time."),
]
T1_DUR = 14.0
XF = 0.3  # crossfade seconds


def t1_maker(W, H):
    tall = H / W > 1.5
    s = W / 1080
    graded = {n: espresso_grade(photo(n)) for n in {sc[2] for sc in T1_SCENES}}
    vig = vignette(W, H, 0.6)
    yN = H * (0.42 if tall else 0.40)       # opening numerals
    yLine = H * (0.68 if tall else 0.74)    # craft lines
    cache = {}

    def lines(key, items):
        if key not in cache:
            cache[key] = text_layer(W, H, items)
        return cache[key]

    def scene_frame(sc, t):
        a, b, n, cx, cy, w0, w1, line = sc
        fr = push(graded[n], W, H, cx, cy, w0, w1, (t - a) / (b - a + XF))
        fr = apply_mask_to_espresso(fr, vig)
        fr = brass_sweep(fr, -0.2 + 1.5 * (t - a) / (b - a), 0.20)
        if line:
            band = np.zeros((H, W), np.float32)
            yy = np.arange(H, dtype=np.float32)[:, None]
            band += np.exp(-((yy - yLine) / (H * 0.09)) ** 2) * 0.55
            fr = apply_mask_to_espresso(fr, np.broadcast_to(band, (H, W)))
            L = lines(line, [(line, FR, 76 * s, ALABASTER, yLine)])
            fr = over(fr, L, ramp(t, a + 0.25, a + 0.85) * (1 - ramp(t, b - 0.15, b + 0.2)))
        return fr

    def opening_type(fr, t):
        # "11.11" + dates by 1.3 s: the thumbnail-legible stamp the brief requires by 2 s
        a = ramp(t, 0.35, 1.0) * (1 - ramp(t, 2.75, 3.15))
        if a <= 0:
            return fr
        yy = np.arange(H, dtype=np.float32)[:, None]
        halo = np.exp(-((yy - yN) / (H * 0.16)) ** 2) * 0.6 * a
        fr = apply_mask_to_espresso(fr, np.broadcast_to(halo, (H, W)))
        num, nh = lit_numerals(W, H, "11.11", 300 * s, yN, -0.2 + t * 0.45)
        fr = over(fr, num, a)
        d8 = lines("o_date", [("10–12 November", IN_M, 64 * s, PARCHMENT, yN + nh * 0.5 + 80 * s)])
        return over(fr, d8, ramp(t, 0.8, 1.3) * (1 - ramp(t, 2.75, 3.15)))

    def end_card(t):
        a0 = 10.6
        fr = Image.new("RGB", (W, H), ESPRESSO)
        # faint grain of the first shot behind the end card, so it stays leather, not a slide
        g = push(graded["L4"], W, H, 861, 938, 470, 440, (t - a0) / (T1_DUR - a0))
        fr = Image.blend(fr, g, 0.16)
        fr = apply_mask_to_espresso(fr, vig)
        yE = H * (0.44 if tall else 0.45)
        num, nh = lit_numerals(W, H, "11.11", 380 * s, yE, -0.3 + 1.6 * ramp(t, a0 + 0.3, T1_DUR - 0.6))
        fr = over(fr, num, ramp(t, a0 + 0.1, a0 + 0.8))
        fr = underline(fr, W, yE + nh * 0.5 + 55 * s, 150 * s, ramp(t, a0 + 0.6, a0 + 1.3))
        L = lines("e_txt", [
            ("10–12 November", IN_M, 62 * s, SADDLE, yE + nh * 0.5 + 135 * s),
            ("kordovanleather.com", IN_R, 44 * s, STONE, yE + nh * 0.5 + 215 * s),
        ])
        return over(fr, L, ramp(t, a0 + 0.9, a0 + 1.5))

    def frame(t):
        if t >= 10.6:
            f = end_card(t)
            if t < 10.6 + XF:
                prev = scene_frame(T1_SCENES[-1], t)
                f = Image.blend(prev, f, ramp(t, 10.6, 10.6 + XF))
            return f
        for k, sc in enumerate(T1_SCENES):
            if sc[0] <= t < sc[1]:
                f = scene_frame(sc, t)
                if k and t < sc[0] + XF:
                    f = Image.blend(scene_frame(T1_SCENES[k - 1], t), f, ramp(t, sc[0], sc[0] + XF))
                if k == 0:
                    f = Image.blend(Image.new("RGB", (W, H), ESPRESSO), f, ramp(t, 0.0, 0.5))
                return opening_type(f, t)
        return end_card(t)

    return frame


# ---------------------------------------------------------------- T2
T2_DUR = 12.0


def t2_maker(W, H, dateline):
    tall = H / W > 1.5
    s = W / 1080
    ground = Image.new("RGB", (W, H), ESPRESSO)
    # quiet Walnut glow in the centre of the Espresso ground
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    glow = np.exp(-(((x - W / 2) / (W * 0.7)) ** 2 + ((y - H * 0.47) / (H * 0.42)) ** 2))[..., None]
    g = np.array(ESPRESSO, np.float32) * (1 - glow * 0.6) + np.array(WALNUT, np.float32) * glow * 0.6
    ground = Image.fromarray(g.astype(np.uint8))
    wallet = espresso_grade(photo("BT1"), darken=0.95, gamma=1.05)
    cache = {}

    def lines(key, items):
        if key not in cache:
            cache[key] = text_layer(W, H, items)
        return cache[key]

    # layout
    yA = H * (0.42 if tall else 0.40)               # beat A numerals
    yTop = H * (0.205 if tall else 0.14)            # beat B small numerals
    wcy = H * (0.49 if tall else 0.50)              # wallet centre
    wh = int(H * (0.42 if tall else 0.50))          # wallet window height
    ww = int(wh * 0.8)
    yB1 = H * (0.755 if tall else 0.81)
    yB2 = yB1 + 92 * s
    yE = H * (0.45 if tall else 0.46)

    def beat_a(t, fade):
        fr = ground.copy()
        num, nh = lit_numerals(W, H, "11.11", 400 * s, yA, -0.25 + 0.5 * t)
        fr = over(fr, num, ramp(t, 0.15, 0.8) * fade)
        fr = underline(fr, W, yA + nh * 0.5 + 55 * s, 170 * s, ramp(t, 0.6, 1.3) * fade)
        L = lines("a_date", [(dateline, IN_M, 64 * s, SADDLE, yA + nh * 0.5 + 140 * s)])
        return over(fr, L, ramp(t, 0.8, 1.3) * fade)

    def beat_b(t):
        a0 = 3.5
        fr = ground.copy()
        u = (t - a0) / (8.0 - a0)
        win = push(wallet, ww, wh, 561, 700, 1122, 1040, u)
        # spotlight reveal: radial mask grows over 1.6 s, edges melt into the ground
        yy, xx = np.mgrid[0:wh, 0:ww].astype(np.float32)
        r = np.sqrt(((xx - ww / 2) / (ww / 2)) ** 2 + ((yy - wh / 2) / (wh / 2)) ** 2)
        rad = 0.15 + 0.85 * ramp(t, a0 + 0.1, a0 + 1.7)
        m = np.clip((rad - r) / 0.35, 0, 1) ** 1.5
        base = np.asarray(fr.crop((W // 2 - ww // 2, int(wcy - wh / 2),
                                   W // 2 - ww // 2 + ww, int(wcy - wh / 2) + wh))).astype(np.float32)
        mix = base * (1 - m[..., None]) + np.asarray(win).astype(np.float32) * m[..., None]
        fr.paste(Image.fromarray(mix.astype(np.uint8)), (W // 2 - ww // 2, int(wcy - wh / 2)))
        fr = brass_sweep(fr, -0.2 + 1.4 * ramp(t, a0 + 1.2, 8.0), 0.16)
        num, _ = lit_numerals(W, H, "11.11", 170 * s, yTop, -1)
        fr = over(fr, num, ramp(t, a0, a0 + 0.5))
        L1 = lines("b1", [("10–12 November.", FR, 70 * s, ALABASTER, yB1)])
        fr = over(fr, L1, ramp(t, a0 + 0.9, a0 + 1.5))
        L2 = lines("b2", [(dateline, IN_M, 50 * s, SADDLE, yB2)])
        return over(fr, L2, ramp(t, a0 + 2.0, a0 + 2.6))

    def beat_c(t):
        a0 = 8.0
        fr = ground.copy()
        L0 = lines("c0", [("Mark the date.", FR, 72 * s, PARCHMENT, yE - 290 * s)])
        fr = over(fr, L0, ramp(t, a0 + 0.1, a0 + 0.7))
        num, nh = lit_numerals(W, H, "11.11", 400 * s, yE, -0.3 + 1.6 * ramp(t, a0 + 0.4, T2_DUR - 0.5))
        fr = over(fr, num, ramp(t, a0 + 0.2, a0 + 0.9))
        fr = underline(fr, W, yE + nh * 0.5 + 55 * s, 170 * s, ramp(t, a0 + 0.7, a0 + 1.4))
        L = lines("c_txt", [
            (dateline, IN_M, 64 * s, SADDLE, yE + nh * 0.5 + 140 * s),
            ("Our 11.11 sale  ·  kordovanleather.com", IN_R, 42 * s, STONE, yE + nh * 0.5 + 225 * s),
        ])
        return over(fr, L, ramp(t, a0 + 0.9, a0 + 1.5))

    def frame(t):
        if t < 3.5:
            return beat_a(t, 1 - ramp(t, 3.2, 3.6))
        if t < 8.0:
            f = beat_b(t)
            if t < 3.5 + XF:
                f = Image.blend(beat_a(t, 1 - ramp(t, 3.2, 3.6)), f, ramp(t, 3.5, 3.5 + XF))
            return f
        f = beat_c(t)
        if t < 8.0 + XF:
            f = Image.blend(beat_b(t), f, ramp(t, 8.0, 8.0 + XF))
        return f

    return frame


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dateline", default="Starts 10 November",
                    help="T2 date line; keep it true on every day the ad runs")
    ap.add_argument("--only", choices=["T1", "T2"], default=None)
    ap.add_argument("--suffix", default="", help="appended to T2 filenames when re-versioning")
    a = ap.parse_args()
    os.makedirs(FRAMES, exist_ok=True)
    for (W, H, tag) in [(1080, 1920, "9x16"), (1080, 1350, "4x5")]:
        if a.only in (None, "T1"):
            encode(os.path.join(ROOT, f"T1_something_is_being_made_{tag}_14s.mp4"), W, H,
                   t1_maker(W, H), T1_DUR, [1.6, 4.6, 13.2])
        if a.only in (None, "T2"):
            encode(os.path.join(ROOT, f"T2_mark_the_date_{tag}_12s{a.suffix}.mp4"), W, H,
                   t2_maker(W, H, a.dateline), T2_DUR, [1.6, 6.5, 11.2])
    print("done")
