# COPY — `sizing-regret`

**Ad name:** `AD_Jackets_Cold_SizingRegret_Sep26`
**Account:** `995683712074843` (Kordovan 2025, PKR) — the only account in scope
**Destination:** `https://kordovanleather.com/collections/mens-leather-jackets`

---

## Primary text

> The jacket that fits you perfectly in September is being tried on over a t-shirt.
>
> In January there is a sweater under it, and a slim fit that looked right in autumn will not close over a wool layer. Most men find this out in the first cold week, months after the money is gone.
>
> Ours are made to order in Karachi. Tell us you'll be wearing something under it and the chest is cut with that in mind, without the jacket losing its line.
>
> From Rs 22,000. Book with 50% and pay the balance to the rider. Free delivery nationwide, lifetime craftsmanship warranty.

The first sentence is 81 characters — it clears the mobile truncation point whole, so the
premise lands before anyone taps "See more".

### Alternates for testing

**B — the direct question**
> Try this before you buy a leather jacket this month: put a sweater on, then try the jacket over it. If it will not close, it is an autumn jacket and you are about to pay winter money for it. Kordovan jackets are made to order in Karachi — tell us there's a layer going underneath and it is cut for one. From Rs 22,000, book with 50% and pay the balance to the rider.

**C — the northern frame**
> Islamabad in January is not Karachi in January. A slim leather jacket that sits perfectly over a t-shirt will not close over a wool sweater, and by the time you find out, the season is half over. Ours are made to order — the chest can allow for the layer without ruining the line. From Rs 22,000. Free delivery nationwide.

Variant C leans hardest into the geography and is the one to test first if the ad set is
northern-only. Test one at a time — do not split PKR 1,000/day three ways.

---

## Headline

> **Cut to close over a sweater**

27 characters — under the 40-character feed truncation point.

*Alternates:* `An autumn fit is not a winter fit` (33) · `Made to order in Karachi` (24)

## Description

> **Made to order in Karachi**

24 characters — safe under the 30-character link-description limit.

## Call to action

> **`SHOP_NOW`**

`LEARN_MORE` is the variant worth testing here — this creative teaches something before
it sells, and at PKR 1,000/day in September the useful output is a cheap read on whether
the angle holds, not immediate orders. Judge either on delivered orders in Shopify.

---

## AI disclosure

> ### `self_ai_disclosure` = **`OPT_IN`**

All five shots are generated with LTX-2.3. This is the fully synthetic package, and the
disclosure is not a grey area.

It is worth being clear about why this ad is allowed to be fully synthetic while
`leather-test` is not: **nothing here functions as evidence.** Every frame is mood,
weather, environment and wardrobe-on-body. The one commercial claim — made to order, cut
for the layer — is carried in the caption as a stated fact underwritten by how the
business actually works, not proved by a picture. The moment this ad tried to *show* a
measurement or stage a proof, the same rule that filmed seven shots of `leather-test`
would apply here too.

---

## Compliance checklist — confirm every line before publishing

- [ ] 🔴 **The workshop has agreed to honour the chest-allowance request.** The caption
      *"Tell us there's a sweater under it"* is a promise, not a slogan. Confirm the
      workshop will action it at order time and that whoever answers WhatsApp knows to
      ask. **If not, cut that caption line back to `Made to order in Karachi.`** — the ad
      still works.
- [ ] **No discount code in the creative.** `PAYONLINE10` goes out only in the WhatsApp
      order confirmation.
- [ ] **No cash-on-delivery badge.** Jackets are not COD. The line is *"Book with 50%,
      pay the balance to the rider"* — and half of it genuinely is paid at the door, so
      never write "no cash on delivery" either.
- [ ] **Landing page agrees with the ad.** Product descriptions and
      `snippets/pdp-jsonld.liquid` still say **"prepaid"**. Fix before this runs.
- [ ] **No caption names a cut, a colour or a model.** Deliberate — the jacket on screen
      is generated, so the copy stays at range level and never makes a claim about a
      specific SKU it does not show.
- [ ] **The failing jacket in shots 02 and 03 is anonymous** — no Kordovan detailing. We
      are naming a category mistake, not staging our own product failing.
- [ ] **No measurement beat in shot 04.** No tape measure, no figures, no before/after.
- [ ] **Ad set excludes** `KV — COD Refusers EXCLUDE` `120253660257910428`.
- [ ] **Northern cities only**, no `radius`: Lahore `1807162`, Islamabad `1796084`,
      Rawalpindi `1822222`. **Karachi is excluded on purpose** — style market, not a
      warmth market. See BRIEF.md. Never `countries: ["PK"]`.
- [ ] **`targeting` is a full replace via the API** — fetch the existing object and merge,
      or the audiences and exclusions are wiped.
- [ ] **Optimise on View Content**, not Purchase. Purchase optimisation cannot exit
      learning at PKR 1,000/day.
- [ ] **Judge on delivered orders in Shopify.** Jackets void at 57% — the highest refusal
      of any category — and historical jacket order counts overstate demand roughly 2x.
      Meta counts the promise; PostEx counts the parcel.
- [ ] **September is a read, not a scale.** Impressions are flat until October. Treat any
      result this month as a signal and hold budget for the ramp.
