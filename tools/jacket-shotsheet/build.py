#!/usr/bin/env python3
"""Build docs/images/JACKETS_SHOT_SHEET.html from jackets.py.

Every prompt is emitted fully self-contained — the model spec, the palette, the
framing rule and the protect-list are written into each one, so the user never
has to scroll back to a preamble. 30 jackets x 5 shots = 150 prompts.

    python3 tools/jacket-shotsheet/build.py
"""
import html
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from jackets import JACKETS  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parents[2] / "docs/images/JACKETS_SHOT_SHEET.html"

# ---------------------------------------------------------------- locked specs

MODEL_M = (
    "Pakistani man, 32 years old, 183 cm, lean athletic build, 40-inch chest, "
    "broad shoulders but not bulky. Short black hair with a natural side part, "
    "neatly trimmed full black beard, warm medium-brown skin, dark brown eyes. "
    "Calm neutral expression — mouth closed, not smiling, not posing, looking "
    "slightly off camera. Underneath the jacket: a plain charcoal crew-neck "
    "cotton t-shirt, dark indigo straight-leg denim, dark brown leather boots. "
    "No watch, no rings, no jewellery, no visible branding on any garment. "
    "This exact man appears in every Kordovan men's jacket photograph — keep "
    "him identical every time."
)

MODEL_W = (
    "Pakistani woman, 28 years old, 170 cm, slim build. Long straight "
    "dark-brown hair worn loose past the shoulders with a centre part, warm "
    "light-brown skin, minimal natural makeup. Calm neutral expression — mouth "
    "closed, not smiling, not posing, looking slightly off camera. Underneath "
    "the jacket: a plain cream fine-knit crew-neck top, dark indigo "
    "straight-leg denim, flat black leather ankle boots. No jewellery, no "
    "visible branding on any garment. This exact woman appears in every "
    "Kordovan women's jacket photograph — keep her identical every time."
)

PALETTE = (
    "PALETTE: Quiet Heritage only — Alabaster #F7F2EA, Parchment #ECE3D4, "
    "Espresso #241C16, Walnut #4A3528, Cognac #A0623A. Warm neutral tones "
    "throughout, never a cool or blue cast."
)

NEVER = (
    "NEVER: no text, no captions, no watermarks, no added branding. Do not add, "
    "remove, redraw or alter the embossed Kordovan horse-head mark. No glossy or "
    "plastic sheen on the leather. No blue or cool colour cast. No props beyond "
    "those named above. No readable brand names on any other garment. Do not "
    "crop any part of the jacket out of frame."
)

FIXED = (
    "THE GARMENT IS FIXED. Keep its cut, proportions, panel seams, colour, "
    "leather grain, stitching, hardware, lining and every last detail 100% "
    "identical to the uploaded photo. Do not restyle it, do not redesign it, "
    "do not tidy it up, do not swap the hardware."
)


def model_for(j):
    return MODEL_M if j["sex"] == "m" else MODEL_W


def slug(j):
    return j["handle"].replace("mens-", "").replace("-leather-jacket", "")[:40]


# --------------------------------------------------------------------- prompts

def shot1(j):
    return f"""Using the UPLOADED photo of this exact leather jacket — {j['name']}, a {j['colour']} {j['style']} jacket by Kordovan — produce the CATALOGUE HERO shot.

{FIXED}

PROTECT THESE DETAILS ABOVE ALL: {j['lock']}.

IF THE UPLOAD SHOWS A PERSON WEARING IT: remove the person completely and present the jacket as a ghost mannequin — filled out to a natural worn shape, hollow neck opening, hollow cuffs, no body, no head, no hands, no mannequin visible anywhere.

FRAMING: straight-on front view, jacket upright and centred. THE WHOLE GARMENT IN FRAME — top of the collar to the bottom of the hem, both cuffs included, with an even margin of about 10% all round. Sleeves hanging naturally. Nothing cropped, no part of the jacket touching the edge of the frame.

BACKGROUND: seamless warm Alabaster #F7F2EA studio sweep — warm cream, never pure white.
LIGHT: large soft key from the upper left, gentle fill from the right, soft diffused contact shadow beneath the hem. 5000K, low-to-medium contrast, true-to-life leather tone.
CAMERA: 85mm look, deep focus, sharp throughout.
{PALETTE}
OUTPUT: 4:5 portrait, 2048 x 2560 px, sRGB, photorealistic, high detail.

{NEVER}"""


def shot2(j):
    return f"""Using the UPLOADED photo of this exact leather jacket — {j['name']}, a {j['colour']} {j['style']} jacket by Kordovan — produce the ON-BODY shot.

{FIXED}

PROTECT THESE DETAILS ABOVE ALL: {j['lock']}.

THE MODEL IS FIXED TOO. If the uploaded photo already shows someone wearing the jacket, replace that person entirely with this exact model while keeping the garment untouched:
{model_for(j)}

FRAMING: FULL-LENGTH standing figure, head fully in frame down to the feet. THE ENTIRE JACKET VISIBLE — collar, both sleeves, both cuffs and the full hem. NO half-body crop, NO torso-only crop, nothing cut off at the waist, the elbows or the chin. Model standing square to camera, weight even, arms relaxed at the sides, jacket worn open unless the upload shows it fastened.

SETTING: {j['wear']}. Background kept plain and quiet so the jacket is the only thing being read.
LIGHT: soft directional daylight, 5000K, gentle fill, no harsh shadows across the garment.
CAMERA: 50mm look, f/4, model sharp head to hem, background gently soft.
{PALETTE}
OUTPUT: 4:5 portrait, 2048 x 2560 px, sRGB, photorealistic.

{NEVER}"""


def shot3(j):
    return f"""Using the UPLOADED photo of this exact leather jacket — {j['name']}, a {j['colour']} {j['style']} jacket by Kordovan — produce the OPEN / INSIDE shot.

{FIXED}

PROTECT THESE DETAILS ABOVE ALL: {j['lock']}.

Present the jacket as a ghost mannequin — no person, no head, no hands, no mannequin visible — with the front FULLY OPEN and both front panels held slightly back to reveal the lining, the inner pocket and the inside of the collar. Keep the lining colour, texture and any inner labels exactly as they appear in the upload. If the lining is not visible in the uploaded photo, render it plain and neutral — do NOT invent a pattern, a logo or a contrast colour.

FRAMING: straight-on with a slight 10-degree turn so one open panel reads in depth. THE WHOLE GARMENT IN FRAME, collar to hem, both cuffs included, even margin all round. Nothing cropped.

BACKGROUND: seamless warm Alabaster #F7F2EA sweep.
LIGHT: soft, even, diffused studio light at 5000K so the interior is fully legible into the shadows. Low contrast, soft shadows.
CAMERA: 85mm look, deep focus, sharp throughout.
{PALETTE}
OUTPUT: 4:5 portrait, 2048 x 2560 px, sRGB, photorealistic, high detail.

{NEVER}"""


def shot4(j):
    return f"""Using the UPLOADED photo of this exact leather jacket — {j['name']}, a {j['colour']} {j['style']} jacket by Kordovan — produce the TEXTURE MACRO.

Fill the frame with {j['macro']}.

The colour, grain pattern, thread colour and hardware finish must match the uploaded jacket exactly. Do not invent a different texture, a different leather or a different colour. This is the same physical jacket, photographed close.

PROTECT: {j['lock']}.

LIGHT: raking warm side light at 4900K running across the surface to lift the grain, the pores and the stitching into relief. Deep rich espresso shadows, higher local contrast for tactility. Matte finish — no gloss, no specular hotspot.
CAMERA: 100mm macro look, f/4, very shallow depth of field falling off toward the frame edges.
{PALETTE}
OUTPUT: 4:5 portrait, 2048 x 2560 px, sRGB, photorealistic, extreme detail.

{NEVER}"""


def shot5(j):
    return f"""Using the UPLOADED photo of this exact leather jacket — {j['name']}, a {j['colour']} {j['style']} jacket by Kordovan — produce the EDITORIAL LIFESTYLE shot.

{FIXED}

PROTECT THESE DETAILS ABOVE ALL: {j['lock']}.

THE MODEL IS FIXED. If the uploaded photo already shows someone wearing the jacket, replace that person entirely with this exact model while keeping the garment untouched:
{model_for(j)}

SCENE: {j['scene']}.

FRAMING: three-quarter to full length. THE ENTIRE JACKET IN FRAME — collar, both sleeves and the full hem. NO half-body crop, nothing cut off at the waist or the elbows. Natural unposed stance, weight on one leg, hands relaxed. Composition on the rule of thirds with calm empty space on the left third for a headline.
LIGHT: soft natural directional light, warm 4800-5200K, medium contrast, deep soft shadows.
CAMERA: 35-50mm look, f/2.8, model sharp, scene gently blurred.
{PALETTE}
OUTPUT: 3:2 landscape, 2400 x 1600 px, sRGB, photorealistic, high detail.

{NEVER}"""


SHOTS = [
    ("1", "Hero — front, ghost mannequin", "hero", shot1),
    ("2", "On-body — full length, locked model", "onbody", shot2),
    ("3", "Open — lining, inner pocket, collar", "open", shot3),
    ("4", "Texture macro — this jacket's signature", "macro", shot4),
    ("5", "Editorial lifestyle — locked model, own scene", "lifestyle", shot5),
]

# ------------------------------------------------------------------ build html

prompts = {}
cards = []

for j in JACKETS:
    pid = j["pid"]
    sex_label = "Men's" if j["sex"] == "m" else "Women's"
    rows = []
    for num, label, fileword, fn in SHOTS:
        prompts[f"{pid}.{num}"] = fn(j)
        fname = f"kordovan-{slug(j)}-{fileword}.jpg"
        rows.append(
            f'<div class="shot" data-shot="{num}">'
            f'<label><input type="checkbox" class="ck" data-k="{pid}.{num}">'
            f'<span class="sn">Shot {num}</span> {html.escape(label)}'
            f'<em>{html.escape(fname)}</em></label>'
            f'<span class="acts"><button class="copy" data-k="{pid}.{num}">Copy prompt</button></span>'
            f"</div>"
        )

    warn = (
        f'<p class="warn">⚠️ {html.escape(j["warn"])}</p>' if j.get("warn") else ""
    )

    cards.append(
        f'<article class="prod" id="p-{pid}" data-sex="{j["sex"]}" data-style="{html.escape(j["style"])}">'
        f"<header><h3>{html.escape(j['name'])}</h3>"
        f'<span class="badge">{sex_label} &middot; {html.escape(j["style"])} &middot; Rs {j["price"]}</span></header>'
        f'<div class="links">'
        f'<a href="https://kordovanleather.com/products/{j["handle"]}" target="_blank" rel="noopener">live page &#8599;</a>'
        f'<a href="https://admin.shopify.com/store/kordovan-leather/products/{pid}" target="_blank" rel="noopener">admin &#8599;</a>'
        f"</div>"
        f"{warn}"
        f'<p class="lock"><b>Protect on every shot:</b> {html.escape(j["lock"])}.</p>'
        f'<div class="shots">{"".join(rows)}</div>'
        f'<textarea class="note" data-k="{pid}.note" placeholder="notes — e.g. shot 2 redone 12 Aug, waiting on the brown&hellip;"></textarea>'
        f"</article>"
    )

TPL = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kordovan — Jackets Shot Sheet</title>
<style>
:root{--bg:#F7F2EA;--card:#fff;--ink:#241C16;--mut:#8B8174;--cognac:#A0623A;--tan:#C08B5C;--bor:#DDD2C0;--parch:#ECE3D4}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 Georgia,'Times New Roman',serif}
header.top{position:sticky;top:0;z-index:9;background:var(--ink);color:#F7F2EA;padding:14px 22px}
header.top h1{margin:0;font-size:20px;font-weight:500;letter-spacing:.04em}
.bar{background:#4A3528;border-radius:99px;height:10px;margin-top:10px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--tan);width:0%;transition:width .3s}
.sub{font-size:12.5px;opacity:.85;margin-top:6px}
.filters{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.filters button{background:transparent;border:1px solid #6b5747;color:#F7F2EA;border-radius:99px;padding:4px 14px;font:12.5px Georgia,serif;cursor:pointer}
.filters button.on{background:var(--cognac);border-color:var(--cognac)}
main{max-width:1000px;margin:0 auto;padding:22px}
.intro{background:var(--card);border:1px solid var(--bor);border-radius:12px;padding:18px 20px;margin-bottom:22px}
.intro h2{margin:0 0 10px;font-size:18px;font-weight:600}
.intro h3{margin:18px 0 6px;font-size:15px;font-weight:600}
.intro p{margin:8px 0}
.intro ul{margin:8px 0;padding-left:20px}
.intro li{margin:4px 0}
.spec{background:#FBF8F2;border:1px solid var(--bor);border-radius:8px;padding:12px 14px;margin:10px 0;font-size:13.5px}
.flag{background:#FBEFEA;border:1px solid #E2C3B3;border-left:4px solid #A0402A;border-radius:8px;padding:12px 14px;margin:12px 0;font-size:13.5px}
.prod{background:var(--card);border:1px solid var(--bor);border-radius:12px;padding:16px 18px;margin-bottom:14px}
.prod.done{opacity:.5}
.prod.hide{display:none}
.prod header{display:flex;justify-content:space-between;gap:10px;align-items:baseline;flex-wrap:wrap}
.prod h3{margin:0;font-size:16.5px;font-weight:600}
.badge{font-size:11.5px;border-radius:99px;padding:3px 10px;background:var(--parch);color:var(--mut);white-space:nowrap}
.links{font-size:12.5px;margin:6px 0;display:flex;gap:14px;flex-wrap:wrap}
.links a{color:var(--cognac)}
.warn{background:#FBEFEA;border-left:3px solid #A0402A;border-radius:6px;padding:8px 10px;font-size:12.5px;margin:8px 0}
.lock{font-size:12.5px;color:var(--mut);margin:8px 0;line-height:1.5}
.lock b{color:var(--ink)}
.shot{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 0;border-top:1px dashed var(--bor);flex-wrap:wrap}
.shot label{cursor:pointer;flex:1}
.shot .sn{font-weight:700;color:var(--cognac);margin-right:4px}
.shot em{color:var(--mut);font-size:12px;font-style:italic;display:block;margin-left:22px}
.shot.checked label{color:var(--mut);text-decoration:line-through}
button.copy{background:var(--parch);border:1px solid var(--bor);border-radius:8px;padding:5px 12px;font:12px Georgia,serif;cursor:pointer;color:var(--ink)}
button.copy:hover{background:var(--tan);color:#fff}
button.copy.copied{background:#5A5A3C;color:#fff}
.note{width:100%;border:1px solid var(--bor);border-radius:8px;background:#FBF8F2;font:12.5px Georgia,serif;padding:7px 9px;margin-top:10px;min-height:34px;resize:vertical}
.io{margin:34px 0;text-align:center;font-size:12.5px;color:var(--mut)}
.io button{margin:0 6px;background:none;border:1px solid var(--bor);border-radius:8px;padding:5px 12px;cursor:pointer;font:12.5px Georgia,serif;color:var(--ink)}
footer{color:var(--mut);text-align:center;font-size:12px;padding:20px}
@media(max-width:600px){main{padding:14px}.prod{padding:13px 14px}}
</style></head><body>
<header class="top"><h1>&#128014; KORDOVAN — Jackets Shot Sheet</h1>
<div class="bar"><i id="tbar"></i></div>
<div class="sub" id="tsub"></div>
<div class="filters">
<button class="on" data-f="all">All 30</button>
<button data-f="todo">Unfinished</button>
<button data-f="m">Men's</button>
<button data-f="w">Women's</button>
<button data-f="s:biker">Biker</button>
<button data-f="s:cafe racer">Cafe racer</button>
<button data-f="s:bomber">Bomber</button>
<button data-f="s:coat">Coat</button>
</div></header>
<main>

<div class="intro">
<h2>How to use this</h2>
<p>One card per jacket, five shots each, and <b>every prompt is complete on its own</b> — the model, the framing rule, the palette and the protect-list are written into all 150 of them. You never need to scroll back up to this box. Read it once, then work from the copy buttons.</p>
<p><b>Per shot:</b> open your image tool &rarr; attach the jacket's real Shopify photo &rarr; hit <i>Copy prompt</i> &rarr; paste &rarr; generate &rarr; save with the filename shown under the shot &rarr; tick the box.</p>

<h3>The two rules this sheet exists to enforce</h3>
<ul>
<li><b>One man, one woman, across the whole range.</b> Every men's jacket is worn by the same specified model; every women's jacket by the same woman. The full description is baked into each prompt, so the men's grid reads as one shoot and the women's as another.</li>
<li><b>No half crops. Ever.</b> Every prompt states the whole garment must be in frame — collar, both cuffs, full hem — and explicitly forbids torso-only and waist-up crops. The on-body and lifestyle shots are full-length.</li>
</ul>

<h3>The locked models</h3>
<div class="spec"><b>Men's — used on all 28 men's jackets</b><br>__MODEL_M__</div>
<div class="spec"><b>Women's — used on both women's jackets</b><br>__MODEL_W__</div>
<p style="font-size:13px;color:#8B8174">If a generated face comes out inconsistent between jackets, add this one line to the end of the prompt: <i>"Frame the model from the chin down so the face is out of shot."</i> Do it for <b>every</b> jacket or none — half and half is what breaks a grid.</p>

<h3>What each shot is for</h3>
<ul>
<li><b>Shot 1 · Hero</b> — the PDP main image and the collection card. Ghost mannequin on cream. If your upload has a person in it, the prompt removes them.</li>
<li><b>Shot 2 · On-body</b> — scale and fit. Full-length, locked model, plain setting.</li>
<li><b>Shot 3 · Open</b> — lining, inner pocket, inside of the collar. This is the trust shot; it is the one that answers "is it real leather inside too".</li>
<li><b>Shot 4 · Macro</b> — <b>different for every single jacket</b>. The quilting on the Nightfall, the fur join on the Urban Rider, the wax pooling on the Durham, the rubbed-through elbow on the Allaric Alley.</li>
<li><b>Shot 5 · Lifestyle</b> — the ad and social image. Every jacket gets its own scene, none repeated, so the grid never twins.</li>
</ul>

<div class="flag"><b>Two catalogue defects to settle before shooting</b>
<ul style="margin:6px 0 0;padding-left:18px">
<li><b>Product 8137559245040</b> is titled <i>"Rebel | Men's Brown Cafe Racer Sheepskin Leather Jacket"</i>, but its handle, all three image filenames and every alt text say <b>Hawkeye brown double-breasted vintage coat</b>. A cafe racer and a double-breasted coat are not the same garment, so one of the two is wrong. This sheet treats it as the coat, because the images decide it. It is not a duplicate of the real Rebel (8079155134704) — it is a mis-titled coat.</li>
<li><b>Product 8180219347184</b> — renamed to <i>Sinclair Women's Bomber Jacket</i>. Its SEO title still read <i>"Alison — Black Women's Leather Biker Jacket"</i> and has been corrected to match.</li>
</ul></div>

<div class="flag" style="background:#FBF8F2;border-color:#DDD2C0;border-left-color:#B0894F"><b>Honest note on how these were written.</b> The product photos could not be opened from the session that built this sheet — the network proxy refuses Shopify's CDN. Style, colour and the protect-lists come from each product's title, handle and image alt text, which name the details explicitly. That is why every prompt is built around <i>"keep the uploaded photo 100% identical"</i>: the garment always comes from your real photo, and the protect-list only tells the generator what not to smooth away. If a protect-list gets a detail wrong for a particular jacket, fix that one line in <code>tools/jacket-shotsheet/jackets.py</code> and re-run the builder.</div>
</div>

__CARDS__

<div class="io">
<button id="exp">Export progress</button><button id="imp">Import progress</button><button id="rst">Reset</button>
<p>Progress is saved in this browser only. Export before switching device.</p>
</div>
</main>
<footer>Kordovan &middot; Jackets Shot Sheet &middot; built from live catalogue data, 10 Aug 2026 &middot; regenerate with <code>python3 tools/jacket-shotsheet/build.py</code></footer>
<script>
const PROMPTS = __PROMPTS__;
const KEY = 'kdv-jacket-shots';
let st = {};
try { st = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { st = {}; }
const save = () => localStorage.setItem(KEY, JSON.stringify(st));

function refresh() {
  document.querySelectorAll('.ck').forEach(c => {
    c.checked = !!st[c.dataset.k];
    c.closest('.shot').classList.toggle('checked', c.checked);
  });
  document.querySelectorAll('.note').forEach(n => { n.value = st[n.dataset.k] || ''; });
  let done = 0, total = 0;
  document.querySelectorAll('.prod').forEach(p => {
    const cks = [...p.querySelectorAll('.ck')];
    const d = cks.filter(c => c.checked).length;
    done += d; total += cks.length;
    p.classList.toggle('done', d === cks.length);
  });
  document.getElementById('tbar').style.width = (total ? done / total * 100 : 0) + '%';
  document.getElementById('tsub').textContent =
    done + ' of ' + total + ' shots done · ' +
    document.querySelectorAll('.prod.done').length + ' of ' +
    document.querySelectorAll('.prod').length + ' jackets complete';
}

document.addEventListener('change', e => {
  if (e.target.classList.contains('ck')) { st[e.target.dataset.k] = e.target.checked; save(); refresh(); }
});
document.addEventListener('input', e => {
  if (e.target.classList.contains('note')) { st[e.target.dataset.k] = e.target.value; save(); }
});
document.addEventListener('click', e => {
  const b = e.target.closest('button.copy');
  if (!b) return;
  navigator.clipboard.writeText(PROMPTS[b.dataset.k]).then(() => {
    b.classList.add('copied'); b.textContent = 'Copied ✓';
    setTimeout(() => { b.classList.remove('copied'); b.textContent = 'Copy prompt'; }, 1400);
  });
});

document.querySelectorAll('.filters button').forEach(btn => btn.onclick = () => {
  document.querySelectorAll('.filters button').forEach(x => x.classList.remove('on'));
  btn.classList.add('on');
  const f = btn.dataset.f;
  document.querySelectorAll('.prod').forEach(p => {
    let show = true;
    if (f === 'todo') show = !p.classList.contains('done');
    else if (f === 'm' || f === 'w') show = p.dataset.sex === f;
    else if (f.startsWith('s:')) show = p.dataset.style === f.slice(2);
    p.classList.toggle('hide', !show);
  });
});

document.getElementById('exp').onclick = () => {
  const b = new Blob([JSON.stringify(st, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b);
  a.download = 'kordovan-jacket-shots.json';
  a.click();
};
document.getElementById('imp').onclick = () => {
  const i = document.createElement('input');
  i.type = 'file'; i.accept = 'application/json';
  i.onchange = () => {
    const r = new FileReader();
    r.onload = () => { try { st = JSON.parse(r.result); save(); refresh(); } catch (e) { alert('Could not read that file.'); } };
    r.readAsText(i.files[0]);
  };
  i.click();
};
document.getElementById('rst').onclick = () => {
  if (confirm('Clear all ticks and notes on this device?')) { st = {}; save(); refresh(); }
};

refresh();
</script>
</body></html>
"""

out = (
    TPL.replace("__MODEL_M__", html.escape(MODEL_M))
    .replace("__MODEL_W__", html.escape(MODEL_W))
    .replace("__CARDS__", "\n".join(cards))
    .replace("__PROMPTS__", json.dumps(prompts, ensure_ascii=False))
)

OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT} — {len(JACKETS)} jackets, {len(prompts)} prompts, {len(out):,} bytes")
