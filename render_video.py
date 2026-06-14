"""
Kordovan Leather — thumbstopping product video renderer
1080×1920  |  30 fps  |  15 s  |  450 frames
Pure Pillow → imageio → MP4
"""

import math
import os
import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ── Constants ────────────────────────────────────────────────────────────────
W, H = 1080, 1920
FPS = 30
TOTAL = 450

GOLD   = (201, 168, 76)
CREAM  = (245, 238, 215)
DARK   = (10, 7, 4)
BROWN  = (59, 31, 14)
BLACK  = (0, 0, 0)

OUT = "/home/user/KDV/kordovan-ad.mp4"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ── Easing ───────────────────────────────────────────────────────────────────

def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))

def ease_out(t):
    """Expo ease-out"""
    return 1 - (1 - clamp(t)) ** 3

def ease_in(t):
    return clamp(t) ** 3

def progress(frame, start, end):
    if end == start:
        return 1.0
    return clamp((frame - start) / (end - start))

def lerp(a, b, t):
    return a + (b - a) * t

def alpha_color(col, a):
    """Return RGBA tuple with given alpha 0-255"""
    return (*col, int(a))

# ── Drawing helpers ──────────────────────────────────────────────────────────

def radial_gradient(w, h, cx, cy, inner, outer):
    """Create a radial gradient image (RGB)."""
    img = Image.new("RGB", (w, h))
    arr = np.zeros((h, w, 3), dtype=np.float32)
    ys, xs = np.mgrid[0:h, 0:w]
    dist = np.sqrt(((xs - cx*w) ** 2) + ((ys - cy*h) ** 2))
    max_d = math.sqrt((max(cx, 1-cx)*w)**2 + (max(cy, 1-cy)*h)**2)
    t = np.clip(dist / max_d, 0, 1)
    for c in range(3):
        arr[:, :, c] = inner[c] * (1 - t) + outer[c] * t
    img = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    return img

def paste_rgba(base, layer):
    """Alpha-composite an RGBA layer onto base (RGB)."""
    base.paste(layer, (0, 0), layer)

def draw_text_centered(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)

def draw_text_left(draw, text, x, y, font, fill):
    draw.text((x, y), text, font=font, fill=fill)

def gold_alpha(a_fraction):
    return (*GOLD, int(255 * a_fraction))

def cream_alpha(a_fraction):
    return (*CREAM, int(255 * a_fraction))

def draw_line_h(img, y, x1, x2, col, alpha=255):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r, g, b = col
    d.line([(x1, y), (x2, y)], fill=(r, g, b, alpha), width=2)
    paste_rgba(img, layer)

# ── Particle system ──────────────────────────────────────────────────────────

PARTICLE_DATA = [
    {"x": (i * 137.5) % 100,
     "y": (i * 73.3) % 100,
     "sz": 2 + (i % 4),
     "delay": (i * 7) % 40,
     "speed": 60 + (i % 5) * 20}
    for i in range(20)
]

def draw_particles(img, frame, opacity_scale=0.7):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for p in PARTICLE_DATA:
        spd = p["speed"]
        t = ((frame + p["delay"] * 2) % spd) / spd
        if t < 0.2:
            a = t / 0.2
        elif t < 0.8:
            a = 1.0
        else:
            a = 1 - (t - 0.8) / 0.2
        a *= opacity_scale
        x = int(p["x"] / 100 * W)
        y = int(p["y"] / 100 * H - t * 60)
        sz = p["sz"]
        d.ellipse([x-sz, y-sz, x+sz, y+sz], fill=(*GOLD, int(a * 180)))
    paste_rgba(img, layer)

# ── Gold horizontal bar ──────────────────────────────────────────────────────

def draw_gold_bar(img, y, width, cx=None):
    if width <= 0:
        return
    if cx is None:
        cx = W // 2
    x1 = cx - width // 2
    x2 = cx + width // 2
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # simulate gradient: solid center, fade edges
    for i in range(width):
        t = abs((i / max(width - 1, 1)) - 0.5) * 2  # 0 at center, 1 at edge
        a = int((1 - t ** 1.5) * 255)
        d.line([(x1 + i, y), (x1 + i, y + 2)], fill=(*GOLD, a))
    paste_rgba(img, layer)

# ── Rounded rectangle ────────────────────────────────────────────────────────

def rounded_rect(draw, x1, y1, x2, y2, r, fill=None, outline=None, width=1):
    if fill:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill)
    if outline:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=r, outline=outline, width=width)

# ── Fonts ────────────────────────────────────────────────────────────────────

def get_font(size, bold=False):
    # Try common system fonts; fall back to default
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def get_sans(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


# Pre-load fonts
f_title   = get_font(90, bold=True)
f_title2  = get_font(72, bold=True)
f_sub     = get_font(42, bold=False)
f_eyebrow = get_sans(28, bold=False)
f_body    = get_sans(34, bold=False)
f_btn     = get_sans(38, bold=True)
f_url     = get_sans(30, bold=False)
f_mono    = get_font(130, bold=True)
f_feature = get_sans(40, bold=False)
f_label   = get_sans(26, bold=False)

# ── Wipe overlay ─────────────────────────────────────────────────────────────

def draw_wipe(img, t):
    """Gold wipe from left; t=0 hidden, t=1 full screen."""
    px = int(W * ease_out(t))
    if px <= 0:
        return
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rectangle([0, 0, px, H], fill=(*GOLD, 255))
    paste_rgba(img, layer)

# ── Vignette ─────────────────────────────────────────────────────────────────

_VIGNETTE = None
def get_vignette():
    global _VIGNETTE
    if _VIGNETTE is None:
        v = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(v)
        for i in range(400):
            t = i / 400
            r = int(t ** 1.5 * 200)
            shrink_x = int(W * t / 2)
            shrink_y = int(H * t / 2)
            d.rectangle([shrink_x, shrink_y, W - shrink_x, H - shrink_y],
                        outline=(0, 0, 0, r))
        _VIGNETTE = v
    return _VIGNETTE

# ── Scene 1 — Brand Reveal (0–130) ───────────────────────────────────────────

def render_scene1(frame):
    t_bg = ease_out(progress(frame, 0, 120))
    bg_scale = lerp(1.08, 1.0, t_bg)

    # background
    img = radial_gradient(W, H, 0.3, 0.4, BROWN, DARK)

    # subtle diagonal lines overlay
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(-H, W + H, 60):
        d.line([(i, 0), (i + H, H)], fill=(*GOLD, 8), width=1)
    paste_rgba(img, layer)

    # vignette
    v_alpha = ease_out(progress(frame, 0, 40))
    vign = get_vignette().copy()
    vign.putalpha(Image.fromarray(
        np.array(vign.getchannel("A")) * v_alpha, "L"
    ))
    paste_rgba(img, vign)

    draw_particles(img, frame)

    d = ImageDraw.Draw(img)

    # top & bottom gold lines
    line_a = ease_out(progress(frame, 48, 70))
    top_y = int(H * 0.12)
    bot_y = int(H * 0.88)
    draw_gold_bar(img, top_y, int(W * 0.75 * line_a), W // 2)
    draw_gold_bar(img, bot_y, int(W * 0.75 * line_a), W // 2)

    # K monogram circle
    logo_a = ease_out(progress(frame, 20, 60))
    logo_y_off = int(lerp(40, 0, ease_out(progress(frame, 20, 60))))
    center_y = H // 2 - 200

    circle_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(circle_layer)
    cx, cy = W // 2, center_y + logo_y_off
    r = 90
    cd.ellipse([cx-r, cy-r, cx+r, cy+r],
               outline=(*GOLD, int(logo_a * 255)), width=3)
    # K letter
    bbox = cd.textbbox((0, 0), "K", font=f_mono)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    cd.text((cx - tw//2, cy - th//2 - 8), "K", font=f_mono,
            fill=(*GOLD, int(logo_a * 255)))
    paste_rgba(img, circle_layer)

    # KORDOVAN brand name
    name_y = center_y + logo_y_off + 110
    name_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    nd = ImageDraw.Draw(name_layer)
    draw_text_centered(nd, "KORDOVAN", name_y, f_title,
                       (*CREAM, int(logo_a * 255)))
    paste_rgba(img, name_layer)

    # LEATHER subtitle + gold line
    tag_a = ease_out(progress(frame, 55, 90))
    tag_y_off = int(lerp(30, 0, ease_out(progress(frame, 55, 90))))

    bar_w = int(240 * ease_out(progress(frame, 55, 78)))
    draw_gold_bar(img, name_y + 115 + tag_y_off, bar_w)

    sub_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sub_layer)
    draw_text_centered(sd, "LEATHER", name_y + 130 + tag_y_off, f_sub,
                       (*GOLD, int(tag_a * 255)))
    draw_text_centered(sd, "Crafted to Last a Lifetime",
                       name_y + 210 + tag_y_off, f_eyebrow,
                       (*CREAM, int(tag_a * 180)))
    paste_rgba(img, sub_layer)

    return img

# ── Scene 2 — Product Focus (0–140 relative) ──────────────────────────────────

def render_scene2(frame):
    img = Image.new("RGB", (W, H), DARK)
    d_bg = ImageDraw.Draw(img)

    # diagonal pattern
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(-H, W + H, 30):
        d.line([(i, 0), (i + H, H)], fill=(*GOLD, 6), width=1)
    paste_rgba(img, layer)

    # Left gold bar
    bar_w = int(ease_out(progress(frame, 0, 30)) * 6)
    if bar_w > 0:
        layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d2 = ImageDraw.Draw(layer2)
        for y in range(H):
            t = abs(y / H - 0.5) * 2
            a = int((1 - t) * 200)
            d2.line([(0, y), (bar_w, y)], fill=(*GOLD, a))
        paste_rgba(img, layer2)

    slide_t = ease_out(progress(frame, 0, 35))
    card_y_off = int(lerp(60, 0, slide_t))
    card_a = int(slide_t * 255)

    # Product card
    pad = 86
    card_top = int(H * 0.09) + card_y_off
    card_bot = int(H * 0.60) + card_y_off
    card_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card_layer)
    rounded_rect(cd, pad, card_top, W - pad, card_bot, 24,
                 fill=(*BROWN, card_a),
                 outline=(*GOLD, int(card_a * 0.2)), width=2)

    # shimmer
    shimmer_x = int(lerp(-200, W + 200, progress(frame, 0, 140)))
    sh_w = 180
    for i in range(sh_w):
        t = abs((i / sh_w) - 0.5) * 2
        a = int((1 - t) * 40)
        x = shimmer_x - sh_w // 2 + i
        if 0 <= x < W:
            cd.line([(x, card_top), (x, card_bot)], fill=(*GOLD, a))

    paste_rgba(img, card_layer)

    # Wallet illustration
    wallet_cx = W // 2
    wallet_cy = (card_top + card_bot) // 2 - 30
    ww, wh = 400, 240

    wall_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wall_layer)

    # wallet body
    wx1 = wallet_cx - ww // 2
    wy1 = wallet_cy - wh // 2
    wx2 = wallet_cx + ww // 2
    wy2 = wallet_cy + wh // 2
    rounded_rect(wd, wx1, wy1, wx2, wy2, 26,
                 fill=(92, 51, 23, card_a),
                 outline=(*GOLD, int(card_a * 0.4)), width=2)

    # center fold
    wd.line([(wallet_cx, wy1 + 10), (wallet_cx, wy2 - 10)],
            fill=(*GOLD, int(card_a * 0.25)), width=1)

    # card slots
    for i in range(3):
        sx1 = wx1 + 20 + i * 5
        sy1 = wy1 + 25 + i * 8
        wd.rounded_rectangle([sx1, sy1, sx1 + 150, sy1 + 80],
                             radius=8, fill=(*GOLD, int(card_a * (4 + i) * 10)),
                             outline=(*GOLD, int(card_a * 0.1)), width=1)

    # K monogram
    kb = wd.textbbox((0, 0), "K", font=f_title2)
    kw, kh = kb[2]-kb[0], kb[3]-kb[1]
    wd.text((wx2 - kw - 32, wy2 - kh - 22), "K", font=f_title2,
            fill=(*GOLD, int(card_a * 0.5)))

    # label under wallet
    lbl = "Full-Grain Leather Wallet"
    lb = wd.textbbox((0, 0), lbl, font=f_label)
    lw = lb[2] - lb[0]
    wd.text((wallet_cx - lw//2, wy2 + 20), lbl, font=f_label,
            fill=(*GOLD, int(card_a * 0.5)))

    paste_rgba(img, wall_layer)

    draw_particles(img, frame)

    # Text content bottom
    content_a = ease_out(progress(frame, 20, 55))
    content_y_off = int(lerp(40, 0, ease_out(progress(frame, 20, 55))))

    text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = ImageDraw.Draw(text_layer)

    base_y = int(H * 0.63) + content_y_off
    draw_text_left(td, "NEW ARRIVAL", pad, base_y, f_label,
                   (*GOLD, int(content_a * 255)))
    draw_text_left(td, "Full-Grain", pad, base_y + 44, f_title2,
                   (*CREAM, int(content_a * 255)))
    draw_text_left(td, "Leather Wallet", pad, base_y + 148, f_title2,
                   (*CREAM, int(content_a * 255)))

    line_w = int(260 * ease_out(progress(frame, 30, 58)))
    paste_rgba(img, text_layer)
    if line_w > 0:
        lline = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lline)
        for i in range(line_w):
            t = abs((i / max(line_w-1,1)) - 0.5)*2
            a = int((1-t**1.2)*255)
            ld.line([(pad+i, base_y+265), (pad+i, base_y+267)], fill=(*GOLD, a))
        paste_rgba(img, lline)

    body_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(body_layer)
    draw_text_left(bd, "Handcrafted in Pakistan.", pad, base_y + 285, f_body,
                   (*CREAM, int(content_a * 190)))
    draw_text_left(bd, "Built to age beautifully.", pad, base_y + 340, f_body,
                   (*CREAM, int(content_a * 190)))
    paste_rgba(img, body_layer)

    return img

# ── Scene 3 — Feature Pills (0–110 relative) ──────────────────────────────────

FEATURES = [
    ("◆", "Full-Grain Leather"),
    ("◇", "Handstitched"),
    ("◈", "150+ Years of Craft"),
    ("✦", "Ethically Sourced"),
]

def render_scene3(frame):
    img = Image.new("RGB", (W, H), (17, 9, 5))
    d = ImageDraw.Draw(img)

    # diagonal lines
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for i in range(-H, W + H, 50):
        ld.line([(i, 0), (i - H, H)], fill=(*GOLD, 10), width=1)
    paste_rgba(img, layer)

    draw_particles(img, frame)

    title_a = ease_out(progress(frame, 10, 45))
    title_y = int(lerp(30, 0, ease_out(progress(frame, 10, 45))))

    tl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = ImageDraw.Draw(tl)
    draw_text_centered(td, "WHY KORDOVAN", title_y + 200, f_label,
                       (*GOLD, int(title_a * 255)))
    draw_text_centered(td, "The Difference", title_y + 255, f_title2,
                       (*CREAM, int(title_a * 255)))
    draw_text_centered(td, "is in the Details", title_y + 360, f_title2,
                       (*CREAM, int(title_a * 255)))
    paste_rgba(img, tl)

    # gold dot under title
    dot_w = int(80 * ease_out(progress(frame, 30, 50)))
    draw_gold_bar(img, title_y + 475, dot_w)

    # Feature cards
    card_x = 80
    card_w = W - 160
    card_h = 110
    card_start_y = title_y + 520

    for i, (icon, label) in enumerate(FEATURES):
        card_a = ease_out(progress(frame, 35 + i * 18, 65 + i * 18))
        card_x_off = int(lerp(-80, 0, ease_out(progress(frame, 35 + i*18, 65+i*18))))
        cy_pos = card_start_y + i * (card_h + 22)

        cl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cd = ImageDraw.Draw(cl)
        rounded_rect(cd, card_x + card_x_off, cy_pos,
                     card_x + card_w + card_x_off, cy_pos + card_h, 18,
                     fill=(*GOLD, int(card_a * 22)),
                     outline=(*GOLD, int(card_a * 45)), width=2)

        # icon
        icon_b = cd.textbbox((0, 0), icon, font=f_feature)
        ih = icon_b[3] - icon_b[1]
        cd.text((card_x + card_x_off + 32, cy_pos + card_h//2 - ih//2 - 5),
                icon, font=f_feature, fill=(*GOLD, int(card_a * 255)))

        # label
        lb = cd.textbbox((0, 0), label, font=f_feature)
        lh = lb[3] - lb[1]
        cd.text((card_x + card_x_off + 100, cy_pos + card_h//2 - lh//2 - 5),
                label, font=f_feature, fill=(*CREAM, int(card_a * 255)))

        paste_rgba(img, cl)

    return img

# ── Scene 4 — CTA (0–92 relative) ────────────────────────────────────────────

def render_scene4(frame):
    img = radial_gradient(W, H, 0.6, 0.5, BROWN, DARK)

    draw_particles(img, frame)

    # corner accents
    for i, (cx, cy, deg) in enumerate([(80,80,0),(W-80,80,90),(W-80,H-80,180),(80,H-80,270)]):
        ca = ease_out(progress(frame, 15 + i * 8, 40 + i * 8))
        if ca <= 0:
            continue
        cl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        cd = ImageDraw.Draw(cl)
        sz = 50
        # draw corner L-shape
        if deg == 0:
            cd.line([(cx, cy), (cx+sz, cy)], fill=(*GOLD, int(ca*255)), width=2)
            cd.line([(cx, cy), (cx, cy+sz)], fill=(*GOLD, int(ca*255)), width=2)
        elif deg == 90:
            cd.line([(cx, cy), (cx-sz, cy)], fill=(*GOLD, int(ca*255)), width=2)
            cd.line([(cx, cy), (cx, cy+sz)], fill=(*GOLD, int(ca*255)), width=2)
        elif deg == 180:
            cd.line([(cx, cy), (cx-sz, cy)], fill=(*GOLD, int(ca*255)), width=2)
            cd.line([(cx, cy), (cx, cy-sz)], fill=(*GOLD, int(ca*255)), width=2)
        elif deg == 270:
            cd.line([(cx, cy), (cx+sz, cy)], fill=(*GOLD, int(ca*255)), width=2)
            cd.line([(cx, cy), (cx, cy-sz)], fill=(*GOLD, int(ca*255)), width=2)
        paste_rgba(img, cl)

    content_a = ease_out(progress(frame, 20, 55))
    content_y = int(lerp(20, 0, ease_out(progress(frame, 20, 55))))

    tl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td = ImageDraw.Draw(tl)

    draw_text_centered(td, "OWN THE TIMELESS", content_y + 500, f_label,
                       (*GOLD, int(content_a * 255)))
    draw_text_centered(td, "Genuine.", content_y + 580, f_title,
                       (*CREAM, int(content_a * 255)))
    draw_text_centered(td, "Handcrafted.", content_y + 690, f_title,
                       (*GOLD, int(content_a * 255)))
    draw_text_centered(td, "Forever.", content_y + 800, f_title,
                       (*CREAM, int(content_a * 255)))
    paste_rgba(img, tl)

    # gold line
    line_w = int(320 * ease_out(progress(frame, 30, 60)))
    draw_gold_bar(img, content_y + 940, line_w)

    # CTA button
    cta_a = ease_out(progress(frame, 45, 75))
    cta_y = int(lerp(30, 0, ease_out(progress(frame, 45, 75))))

    if cta_a > 0:
        btn_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        bd = ImageDraw.Draw(btn_layer)

        btn_y = content_y + cta_y + 990
        btn_w, btn_h = 480, 100
        bx1 = W//2 - btn_w//2
        bx2 = W//2 + btn_w//2

        # Glow
        pulse = 0.3 + 0.2 * math.sin(frame / 30 * math.pi * 2)
        for g in range(30, 0, -1):
            ga = int(pulse * (30-g) / 30 * 40)
            rounded_rect(bd, bx1-g, btn_y-g, bx2+g, btn_y+btn_h+g, 10,
                         fill=(*GOLD, ga))

        rounded_rect(bd, bx1, btn_y, bx2, btn_y+btn_h, 10,
                     fill=(*GOLD, int(cta_a * 255)))
        bb = bd.textbbox((0,0), "SHOP NOW", font=f_btn)
        bw, bh = bb[2]-bb[0], bb[3]-bb[1]
        bd.text((W//2 - bw//2, btn_y + btn_h//2 - bh//2 - 3), "SHOP NOW",
                font=f_btn, fill=(*DARK, int(cta_a * 255)))
        paste_rgba(img, btn_layer)

        # URL
        url_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ud = ImageDraw.Draw(url_layer)
        draw_text_centered(ud, "kordovanleather.com",
                           content_y + cta_y + 1120, f_url,
                           (*CREAM, int(cta_a * 160)))
        paste_rgba(img, url_layer)

    return img

# ── Main render loop ──────────────────────────────────────────────────────────

def render_frame(frame):
    # Scene transitions:
    # Scene 1: 0–130   (wipe out 118–136)
    # Scene 2: 128–268 (wipe out 250–268)
    # Scene 3: 258–368 (wipe out 350–368)
    # Scene 4: 358–450

    if frame < 148:
        img = render_scene1(frame)
    elif frame < 268:
        img = render_scene2(frame - 128)
    elif frame < 368:
        img = render_scene3(frame - 258)
    else:
        img = render_scene4(frame - 358)

    # Wipe transitions
    if 118 <= frame < 136:
        wt = progress(frame, 118, 136)
        draw_wipe(img, wt)
    elif 136 <= frame < 148:
        draw_wipe(img, 1.0)

    if 250 <= frame < 268:
        wt = progress(frame, 250, 268)
        draw_wipe(img, wt)
    elif 268 <= frame < 270:
        draw_wipe(img, 1.0)

    if 350 <= frame < 368:
        wt = progress(frame, 350, 368)
        draw_wipe(img, wt)
    elif 368 <= frame < 370:
        draw_wipe(img, 1.0)

    return np.array(img.convert("RGB"))


print("Rendering Kordovan Leather Ad…")
writer = imageio.get_writer(OUT, fps=FPS, quality=9, codec="libx264",
                            pixelformat="yuv420p",
                            macro_block_size=None)

for f in range(TOTAL):
    if f % 30 == 0:
        print(f"  frame {f}/{TOTAL}  ({f//30}s)")
    frame_arr = render_frame(f)
    writer.append_data(frame_arr)

writer.close()
print(f"\nDone! → {OUT}")
