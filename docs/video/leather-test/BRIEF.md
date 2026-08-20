# BRIEF — `leather-test`

**Kordovan · September 2026 jacket campaign · hero ad**

---

## Objective

Cold prospecting. Take a man who has been burned by a "genuine leather" jacket that
peeled, and hand him a test he can run with his own thumb. The test is the ad. The
jacket is the payoff.

Landing page: `https://kordovanleather.com/collections/mens-leather-jackets`

## The one thing the viewer should feel

*"I can check this myself — and they already know I'm going to."*

Not desire. Not urgency. **Relief that someone is inviting the inspection instead of
dodging it.** In a market where PU is sold as leather at Rs 22,000, the seller who
teaches you the test is the seller who passes it. Every creative decision below serves
that single feeling.

## Product on screen

**The Iconic — Black Sheepskin** · `iconic-mens-black-sheepskin-leather-jacket` ·
**Rs 22,000** — the floor of the men's range.

This is a deliberate choice, not a default. The closing caption says *"From Rs 22,000"*,
so under the **label-matches-subject rule** the jacket in frame must be the Rs 22,000
jacket. Shooting the Rs 35,000 Urban Rider against a "from Rs 22,000" card would be a
bait line. The Iconic is also the plainest jacket in the range — clean uninterrupted
panels, no studs, no quilting — which is exactly what you want when the whole film is
macro shots of grain. Nothing competes with the surface.

## Claims used, and where each is verified

| Claim in the film | Source |
|---|---|
| Full-grain sheepskin | Product handle + description, `The Iconic` |
| Made to order in Karachi | CLAUDE.md jacket facts; catalogue "made to order" |
| From Rs 22,000 | Verified floor price, men's jacket range (`ops/SEO_JACKET_ROLE_SPLIT.md`) |
| Book with 50%, pay the rest to the rider | CLAUDE.md, user-confirmed 20 Aug 2026 |
| Free delivery nationwide | Every jacket is Rs 22,000+, far over the Rs 5,500 threshold |
| Lifetime craftsmanship warranty | Site-wide, on every Kordovan piece |

**Not used, deliberately:** no discount code (`PAYONLINE10` never appears in creative),
no cash-on-delivery badge, no "hand-stitched" or "saddle-stitched" — those belong to
specific wallets, not to the jacket range.

> ⚠️ **Payment-line flag for the account owner.** CLAUDE.md (20 Aug 2026) sets the jacket
> term as *50% to book, balance to the rider*. But the product-level catalogue copy and
> `snippets/pdp-jsonld.liquid` still say **"prepaid"** — that correction landed on the 4
> jacket collections and the brands article, not on the 30 product descriptions or the
> JSON-LD fallback. This ad uses the corrected term. **The landing page must agree with
> the ad before this runs**, or the click lands on a page that contradicts the creative.

---

## FILM / GENERATE split

**7 shots FILM · 1 shot GENERATE · 22.0 seconds**

This is an almost entirely filmed package. That is the correct answer to this brief, not
a failure to use the tools.

### Why the demonstration is filmed — all of it

The integrity rule is not a style preference here; it is the entire premise of the ad.
Shots 1–5 exist for one purpose: **to prove a claim about the physical product.** A
generated thumb-press does not show leather springing back — it shows a model's guess at
what leather springing back looks like. A generated pore structure is, by construction, a
*printed repeating pattern of pixels* — the exact thing shot 4 accuses the fakes of. An
ad that synthesises the fibrous suede underside is doing precisely what it condemns, and
one frame of it surfacing later would be terminal for a brand whose only real moat is
being the honest seller.

So: every shot that carries evidentiary weight is filmed on a phone with the real jacket.

Shot 6 (the finished jacket, worn) is **also filmed**, and this is the judgement call
worth explaining. Wardrobe-on-body is normally fair to generate. But this film spends
fourteen seconds establishing that you can trust your eyes on this surface. Cutting from
five real macros to a synthetic hero jacket would retroactively put every preceding frame
in question, and the caption over it names the material. It is filmed. It also costs
nothing extra — the jacket is already on the table for shots 1–5.

Shot 8 (the closing hold) is filmed for the same reason and from the same setup.

### The one generated shot, and its boundary

**Shot 7 — the Karachi workshop, 2.0s.** Establishing atmosphere: a shaft of daylight, a
scarred cutting bench, dust turning. It sets place under the caption *"Made to order in
Karachi."*

The boundary is drawn hard and it is written into the prompt's negative clause:
**no people, no hands, no garment, no leather in frame.** The moment a generated hand is
shown working leather, the shot stops being an establishing shot and becomes fabricated
evidence of craft — testimony that a specific person made a specific thing. An empty room
in warm light says *this is where it happens*; it does not testify about the making.

**Recommended upgrade:** if the workshop is accessible, film 6 seconds of the real bench
and drop the generated clip. It is strictly better and it takes one visit. The generated
version exists so the ad can ship this week without one. If you film it, the package
becomes 8/8 FILM and `self_ai_disclosure` flips to `OPT_OUT` — see COPY.md.

### The PU comparison shots (2 and 4)

Shots 2 and 4 show a coated-PU swatch failing the same tests. Direction is strict:
**an unbranded offcut, no label, no tag, no logo, no recognisable garment.** We are
demonstrating a material category, not attacking a named competitor. Same table, same
distance, same light, same camera move as the real-leather shot it cuts against — if the
comparison is not shot fairly, it is not a demonstration, it is a trick, and a viewer
who has held both will notice.

---

## Format spec

| | |
|---|---|
| Aspect / resolution | 9:16, **1080×1920** |
| Codec | H.264, `yuv420p`, CRF 20, `+faststart` |
| Audio | AAC 128k, 44.1kHz stereo |
| Frame rate | 30 fps (all sources normalised) |
| Runtime | **22.0s** |
| Captions | **Burned in.** Fraunces 500, Alabaster `#F7F2EA` on Espresso `#241C16` outline |
| Safe area | Captions at `MarginV=320` — inside the middle ~80%, clear of Reels chrome |
| First 2 seconds | Macro thumb-press. **No logo, no price, no brand card.** |
| Price / payment | On screen only from **18.0s to 22.0s** — the final 4 seconds |

## Grade

Warm throughout. Espresso shadows, never black, never blue. Shoot everything on
**overcast north daylight** — one light source across the whole film means the cuts
between real leather and PU read as a fair comparison rather than a lighting trick.
No lamps, no mixed colour temperature.

## Generation target

LTX-2.3 (Apache 2.0) on a free Colab T4 or via Wan2GP. One clip, 704×1280, 97 frames at
24fps (4.04s), trimmed to 2.0s and upscaled to 1080×1920 at assembly. Free-tier runnable
with a single generation.

## Media notes

- Ad set: cold prospecting, **Karachi · Lahore · Islamabad · Rawalpindi only**, city keys
  from CLAUDE.md, **no `radius`** on any of them.
- **Exclude `KV — COD Refusers EXCLUDE` `120253660257910428`** — no exceptions.
- This is the ad that runs in **Karachi**. The leather-authenticity angle is
  season-independent, which matters in a city with no winter. `sizing-regret` is the
  northern companion.
- Jackets refuse at **57%** vs ~38% all-products, and jacket order counts overstate
  demand ~2x. **Forecast on delivered only.** The 50% deposit is load-bearing — do not
  relax it to lift conversion.
- At ~PKR 8,450 jacket CPA, a Purchase-optimised ad set at PKR 1,000/day will never exit
  learning. **Optimise on View Content** at this budget, one broad consolidated ad set.
