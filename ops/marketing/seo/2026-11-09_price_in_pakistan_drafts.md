# "Price in Pakistan" drafts: 3 ranking pages (L1 DRAFT)

**HQ assignment:** `founder-price-in-pakistan-pages` (Founder priority)
**Maker:** CMO (Omar) · **Date:** 2026-11-09 · **Level:** L1 internal draft → CQRO → CEO → Founder (L2, because it is customer-facing)
**Status:** READY FOR CQRO
**Nothing has been changed in Shopify.** Every live value below was read with read-only GraphQL on 2026-11-09. GSC baselines come from `gsc_query` (`siteUrl https://kordovanleather.com/`, 2026-08-10 → 2026-11-07, queries containing "price", page+query, filtered locally).

---

## 0. Read this first: four findings that change the brief

1. **On collection pages, `descriptionHtml` is NOT the content surface.** `sections/main-collection.liquid:34-35` prints only `collection.description | strip_html | truncatewords: 40`, as plain text in the hero. Anything after word 40 never renders and is not in the HTML. The only full-HTML surface is **`custom.editorial`** (`main-collection.liquid:144-145`, below the grid, output raw).
   - Result: the long wallet buying guide, FAQ and `<details>` block in the wallet `descriptionHtml` are **invisible to shoppers and to Google**.
   - So every content block and FAQ below goes in **`custom.editorial`**. The JSON-LD goes there too, as a `<script>` tag, because the field is output raw. No theme push is needed.
2. **Jacket material contradiction (live).** All 28 jackets have `custom.material` = *top-grain* sheep leather (one is "Top-grain sheep suede"). But the live collection `descriptionHtml` ("from full-grain sheepskin") and `custom.editorial` ("Full-grain sheepskin throughout") say *full-grain*. My drafts follow the product metafields (top-grain). **The Founder must confirm which is true.** Under the sweep rule, either answer means fixing every surface: collection hero, editorial, the jacket blog and the product metafields.
3. **Jackets come in standard sizes, not to measure.** Options are S to XXXL with chest ranges (checked on The Iconic). The live hero ("built to your measurements"), the editorial ("cut to your measurements rather than pulled from a size run") and the jacket blog all overstate this. My drafts say **"cut in your size, for one customer, after you order"**. That is true, and it keeps the made-to-order reason intact.
4. **Errors in the live wallet copy:**
   - The editorial links `/products/the-bastion-bifold-wallet`. That handle does not exist and has no redirect, so the link is broken. The real handle is `the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet`.
   - The editorial names "the Gator", which is DRAFT.
   - The hidden `descriptionHtml` links `/collections/kv2-gifting` (gift sets were discontinued Nov 8).
   - The SEO description says "22 wallets", but 21 are ACTIVE (Gator and HM The Lord's are DRAFT).
   - "Delivery is free on orders over Rs 5,500" sits next to COD. Free delivery over 5,500 applies to **paid-online** orders only (COD over 5,500 pays 250).
   - All of these are fixed in the drafts below.

**Prices used.** The 11.11 sale runs to Nov 12, so every band uses the **regular price**: compare-at where a compare-at is set, otherwise the price. Where the wording calls for it, the copy says "regular price".

**Publish date recommendation:** **Nov 13**, after the Nov 12 19:00Z price revert (`trig_01WyrESV1ANvpmToo8kkweVq`). Until then the pages show sale prices: the Oxford is Rs 17,850 against Rs 21,000 in the new meta, and the jacket floor is Rs 18,700 against Rs 22,000. Publishing early would break "match the post to the click".

---

## 1. Men's leather jackets: `/collections/mens-leather-jackets`

Collection `gid://shopify/Collection/438804021488` · 28 products, all ACTIVE, all `made_to_order = true`.

### Live now (quoted)
- **SEO title (57):** "Men's Leather Jackets Pakistan — From Rs 22,000 | Kordovan"
- **SEO description:** "Genuine sheepskin leather jackets for men in Pakistan. Biker, bomber and cafe racer cuts from Rs 22,000, handcrafted to order. Free delivery nationwide."
- **GSC baseline (price queries → this page, 90d):** 106 queries · 4,606 impr · 128 clicks · **CTR 2.78%** · weighted pos 6.0. The top query, "leather jacket price in pakistan", has 1,045 impr at pos 6.7 with 19 clicks. "Original leather jacket price in pakistan": 602 impr at pos 5.1 with 27 clicks. "Leather jacket price": 225 impr at pos 4.9 with **0 clicks**.

### Regular-price bands from the live catalogue (28 jackets)
| Band | Count | Examples (regular price) |
|---|---|---|
| Rs 22,000 – 25,999 | 8 | The Iconic 22,000 · Alveraz 23,000 · Sheppard 24,300 · Vanguard 25,350 |
| Rs 26,000 – 29,999 | 13 | Alonzo 26,100 · Rodriguez (quilted) 26,400 · The Ace 27,500 · The Spy 28,500 · Marc Ed 29,400 |
| Rs 30,000 – 35,000 | 7 | Desert Voyager 32,000 · Hawkeye (double-breasted) 32,000 · Reacher 33,600 · Urban Rider (fur collar) 35,000 |

### a) Proposed SEO (send BOTH, because `seo` is a full replace)
- **Title (53):** `Leather Jacket Price in Pakistan: Rs 22,000 to 35,000`
  - There is no room for "| Kordovan" inside 60 characters. Google already shows the site name above the title, and the theme appends nothing (`layout/theme.liquid:96` prints `page_title` only).
- **Meta description (151):** `Original men's leather jacket prices in Pakistan: Rs 22,000–35,000. Each cut in your size for one customer, so paid online; about 3 weeks to your door.` *(CQRO fix F1, Nov 9: added "paid online" with its reason; removed "Top-grain sheepskin" until the Founder settles the grade. Omar may restore the material word once Q1 is answered, if it still fits in 155.)*
  - The terms come with their reason: "each cut in your size, so allow about 3 weeks".
  - The meta leads with the highest-volume variants: "original", "men's", "leather jacket price in pakistan".

### b) Field: `custom.editorial` (full replacement value below)
This keeps the live "Choosing your cut" and "Getting the size right" sections word for word. It makes these changes:
- The intro sentence is corrected (sizes, not measurements).
- The old "What a leather jacket costs" section is replaced. Its bands (8k / 8–18k / 22–35k / 60k+) contradicted our own blog (8k / 8–15k / 20–40k / 45k+); the new section uses the blog's bands.
- The "What the leather is" section is removed: it carried the "full-grain" claim, and the price block now covers the hide.
- The "payment and delivery" section is merged into the price block.

New price block: about 475 words including headings and link text (prose alone is about 440), from `<h2>Leather jacket price in Pakistan</h2>` to the blog link.

```html
<h2>Buying men's leather jackets in Pakistan</h2>
<p>Every jacket on this page is made to order in our own workshop. We hold no finished stock, so yours is cut in your size, for you, after you check out. Production takes time, and that is the trade we have chosen: fit is the one thing a leather jacket cannot fake.</p>

<h2>Leather jacket price in Pakistan</h2>
<p>Our men's leather jackets cost <strong>Rs 22,000 to Rs 35,000</strong> at regular price, the honest range for a genuine sheepskin jacket made in Pakistan. Here is how they divide.</p>
<ul>
<li><strong>Rs 22,000 to 25,999.</strong> Our simplest patterns: <a href="/products/iconic-mens-black-sheepskin-leather-jacket">The Iconic</a> and the <a href="/products/sheppard-mens-cafe-racer-black-leather-jacket">Sheppard</a> cafe racer.</li>
<li><strong>Rs 26,000 to 29,999.</strong> More panels, quilting, bomber trims and waxed or vintage finishes: <a href="/products/alonzo-mens-brown-sheepskin-leather-jacket">Alonzo</a>, <a href="/products/mens-ace-black-leather-bomber-jacket">The Ace</a>, <a href="/products/rodriguez-mens-quilted-leather-biker-jacket">Rodriguez</a>.</li>
<li><strong>Rs 30,000 to 35,000.</strong> The top of the range: <a href="/products/desert-voyager-mens-brown-sheepskin-leather-bomber-jacket">Desert Voyager</a>, the double-breasted <a href="/products/hawkeye-mens-brown-double-breasted-vintage-coat-s012">Hawkeye</a>, <a href="/products/mens-urban-rider-brown-leather-biker-jacket">Urban Rider</a>.</li>
</ul>

<h3>What drives the price</h3>
<ul>
<li><strong>The grade of hide.</strong> Full-grain keeps the whole outer surface; top-grain is lightly corrected for an even finish. "Genuine leather" on a label is a grade name, often split hide, the weaker under-layer. Every jacket here is top-grain sheepskin, lighter and softer than cowhide.</li>
<li><strong>How much hide.</strong> Longer cuts, quilting and double-breasted fronts use more of it.</li>
<li><strong>Lining, stitching and zips.</strong> The parts you notice in the second winter.</li>
</ul>

<h3>What leather jackets cost across Pakistan</h3>
<ul>
<li><strong>Under Rs 8,000:</strong> almost always PU, rexine or bonded leather. The hide alone costs more than that.</li>
<li><strong>Rs 8,000 to 15,000:</strong> a blend, a thin hide, or a genuine jacket on heavy discount. Ask what the shell is.</li>
<li><strong>Rs 20,000 to 40,000:</strong> the honest band for a full genuine leather jacket made locally.</li>
<li><strong>Above Rs 45,000:</strong> usually imported or a designer margin, not necessarily better leather.</li>
</ul>
<p>Bands are indicative; other brands' prices change weekly, so we do not quote them.</p>

<h3>Real leather or rexine: three checks</h3>
<ul>
<li><strong>Pores.</strong> Irregular on real hide; repeating on rexine, which is printed from a roll.</li>
<li><strong>Press it.</strong> Leather creases and springs back. Rexine stays flat and uniform.</li>
<li><strong>The cut edge.</strong> Inside a pocket or under the hem, leather shows a fibrous underside. Rexine shows a fabric backing.</li>
</ul>

<h3>Why jackets are paid online, and how long they take</h3>
<p>Each jacket is cut for one customer, in your size, and cannot be resold if refused at the door. That is why it is <strong>paid in full online</strong> (card or JazzCash) and cash on delivery is not offered. Allow <strong>about 3 weeks to your door</strong>; winter is our busiest season, and we would rather quote honestly than promise a date we cannot hold. Delivery is free.</p>
<p>Still comparing brands? Our <a href="/blogs/jackets/top-10-leather-jacket-brands-in-pakistan">guide to the top 10 leather jacket brands in Pakistan</a> sets these bands against ten labels, ours included.</p>

<h3>Choosing your cut</h3>
<p><strong><a href="/collections/mens-biker-leather-jackets">Biker jackets</a></strong> have the asymmetric zip and belted waist — the most structured shape here, and the most casual. <strong><a href="/collections/mens-bomber-leather-jackets">Bombers</a></strong> use a ribbed collar, cuff and hem, which makes them the most forgiving to wear and the easiest to size. <strong>Cafe racers</strong> are minimal, with a band collar and a straight centre zip; they are the only cut in the range that sits comfortably over a shirt. <strong>Vintage and distressed</strong> finishes arrive already broken in, and hide everyday scuffing better than a clean finish does.</p>
<p>Looking for one colour in particular? See every <a href="/collections/mens-black-leather-jackets">black leather jacket</a> across all three cuts.</p>

<h3>Getting the size right</h3>
<p>The most common mistake is buying for September and wearing in January. Order to the measurement chart rather than your usual shirt size, and if you are in Lahore, Islamabad, Rawalpindi or anywhere further north, allow room across the chest for a sweater underneath. In the south, around Hyderabad and the coast, a lined jacket on its own carries most of the season, so a closer fit works.</p>

<!-- FAQ block (c) follows here: visible HTML + JSON-LD -->
```

### c) FAQ (append to the same `custom.editorial` value, after the sizing section)
The questions follow price intent and are worded differently from the blog's FAQ, so the two pages do not compete for the same question.

```html
<h2>Leather jacket prices: common questions</h2>
<h3>What is the price of an original leather jacket in Pakistan?</h3>
<p>A genuine leather jacket made in Pakistan costs roughly Rs 20,000 to Rs 40,000. Ours run from Rs 22,000 to Rs 35,000 at regular price, all in top-grain sheepskin.</p>
<h3>Why are some leather jackets so cheap?</h3>
<p>Below about Rs 8,000 a jacket is almost always PU, rexine or bonded leather, because the hide for a full jacket costs more than that before any cutting or stitching.</p>
<h3>How can I tell a real leather jacket from rexine?</h3>
<p>Check three things: irregular pores (rexine repeats), a surface that creases and springs back when pressed, and a fibrous, suede-like underside at a cut edge instead of a fabric backing.</p>
<h3>Is a sheep leather jacket cheaper than cow leather?</h3>
<p>Not by rule. Price follows the grade and the amount of hide more than the animal. Sheepskin is lighter and softer; cowhide is heavier and tougher. Every jacket on this page is sheepskin; any style can also be made in cowhide, priced separately, if you ask us on WhatsApp.</p>
<h3>Why are your jackets paid online, and how long is delivery?</h3>
<p>Each jacket is cut for one customer in your size and cannot be resold, so it is paid in full online and cash on delivery is not offered. Allow about 3 weeks to your door; winter is our busiest season. Delivery is free.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is the price of an original leather jacket in Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "A genuine leather jacket made in Pakistan costs roughly Rs 20,000 to Rs 40,000. Ours run from Rs 22,000 to Rs 35,000 at regular price, all in top-grain sheepskin."}},
    {"@type": "Question", "name": "Why are some leather jackets so cheap?", "acceptedAnswer": {"@type": "Answer", "text": "Below about Rs 8,000 a jacket is almost always PU, rexine or bonded leather, because the hide for a full jacket costs more than that before any cutting or stitching."}},
    {"@type": "Question", "name": "How can I tell a real leather jacket from rexine?", "acceptedAnswer": {"@type": "Answer", "text": "Check three things: irregular pores (rexine repeats), a surface that creases and springs back when pressed, and a fibrous, suede-like underside at a cut edge instead of a fabric backing."}},
    {"@type": "Question", "name": "Is a sheep leather jacket cheaper than cow leather?", "acceptedAnswer": {"@type": "Answer", "text": "Not by rule. Price follows the grade and the amount of hide more than the animal. Sheepskin is lighter and softer; cowhide is heavier and tougher. Every jacket on this page is sheepskin; any style can also be made in cowhide, priced separately, if you ask us on WhatsApp."}},
    {"@type": "Question", "name": "Why are your jackets paid online, and how long is delivery?", "acceptedAnswer": {"@type": "Answer", "text": "Each jacket is cut for one customer in your size and cannot be resold, so it is paid in full online and cash on delivery is not offered. Allow about 3 weeks to your door; winter is our busiest season. Delivery is free."}}
  ]
}
</script>
```

### Optional companion fix: hero lead (`descriptionHtml`, first paragraph only)
Only the first 40 words render, and they currently say "full-grain". Proposed first `<p>` (39 words). The second paragraph's "built to your measurements" should also become "cut in your size for one customer".
> Genuine leather jackets for men, made in Pakistan: cut and stitched in our own workshop from top-grain sheepskin. Biker, bomber, cafe racer and vintage cuts in black, brown, claret and blue, at Rs 22,000 to Rs 35,000.

### Expected traffic (ESTIMATE)
- **Baseline:** 4,606 impr / 90d, 128 clicks, CTR 2.78%, pos 6.0.
- **Target:** pos about 4.5 on the price cluster (the content now answers the query directly), with a CTR of **5.0%**.
- **Estimate:** 4,606 × 5.0% = **about 230 clicks / 90d, +100** over baseline (about +35/month).
- Winter peak impressions would push this higher. I am not counting that.

---

## 2. Oxford shoe: `/products/kordovans-premium-oxford-leather-shoes-black`

Product `gid://shopify/Product/8220921266416` · ACTIVE · `custom.made_to_order = true`, tag `made-to-order` · `custom.subtitle` "Made to order in your size — about 3 weeks to your door" · regular price **Rs 21,000** on all 6 sizes (sale price 17,850 until Nov 12) · `custom.material` "Genuine leather"; the description says "Soft cow leather" and "leather sole".

### Live now (quoted)
- **SEO title (54):** "Premium Oxford Leather Shoes Black | Kordovan Pakistan"
- **SEO description:** "Premium Oxford leather shoes for men in black, Rs 21,000. Made to order in our own workshop — about 3 weeks to your door. Free delivery."
- **GSC baseline (90d):** 13 price queries · 1,671 impr · **16 clicks · CTR 0.96%** · weighted pos 4.5.
  - "oxford shoes price in pakistan": 1,047 impr, pos 3.9, 10 clicks.
  - **"black shoes price in pakistan": 109 impr at pos 1.8, 0 clicks.**
  - "oxford black shoes price in pakistan": 123 impr, pos 2.4, 3 clicks.
  - The page ranks. The snippet never says "price in Pakistan", so it does not answer the searcher.

### d) Proposed SEO (send BOTH; the product body stays as it is)
- **Title (52):** `Oxford Shoes Price in Pakistan: Rs 21,000 | Kordovan`
- **Meta description (153):** `Oxford shoes price in Pakistan: Rs 21,000. Black cow leather, made in your size for one customer, paid online, about 3 weeks to your door. Free delivery.` *(CQRO fix F5, Nov 9: the draft omitted "paid online"; added it next to its reason and restored the standard "about 3 weeks to your door". "Leather sole" and "our own workshop" dropped for length; both stay true on the product page.)*
  - "Made in your size for one customer" is the reason for both terms (paid online, about 3 weeks).
  - "Free delivery" is true: footwear is paid online, and Rs 21,000 is above 5,500.
  - Nothing promises COD.
- **Field:** product `seo { title description }` only.

### Expected traffic (ESTIMATE)
- **Baseline:** 1,671 impr, 16 clicks, 0.96%.
- **Target:** CTR **4.0%** at the current pos of about 4.5. This is a snippet fix, so no position change is assumed.
- **Estimate:** 1,671 × 4.0% = **about 67 clicks / 90d, +51**.

---

## 3. Men's leather wallets: `/collections/mens-leather-wallets`

Collection `gid://shopify/Collection/438804578544` · 23 products, **21 ACTIVE** (The Gator and HM The Lord's are DRAFT). Wallets are ready-made, so COD is available.

### Live now (quoted)
- **SEO title (69, already over 60):** "Wallets for Men in Pakistan: Genuine Leather from Rs 1,499 | Kordovan"
- **SEO description:** "22 genuine leather wallets for men, Rs 1,499 to Rs 6,500. Bifold, slim, card holder and RFID styles, made in our own workshop. Cash on delivery available."
- **GSC baseline (price queries → this page, 90d):** 34 queries · 1,101 impr · 58 clicks · **CTR 5.27%** · weighted pos 7.9.
  - "leather wallet price in pakistan": 384 impr, pos 7.1, 26 clicks.
  - "genuine leather wallet price in pakistan": 333 impr, pos 6.9, 13 clicks.
- **Caution:** this page also ranks for "wallets for men" and "leather wallet for men" (the 15k-impression non-brand cluster in the archive). The current title targets that cluster. See the trade-off note under (a).

### Regular-price bands from the live catalogue (21 active wallets)
| Band | Count | Examples (regular price, in stock) |
|---|---|---|
| Rs 1,499 – 2,499 | 8 | Rigor Lite 1,499 · The Seamless 2,000 · The Luke 2,400 · Plain Bifold (nappa) 2,400 |
| Rs 2,500 – 3,999 | 7 | The Bastion 2,500 · Mocha Mate 3,200 · The Hunter HM 3,200 · The Truckkr 3,800 · The Elite mobile 3,900 |
| Rs 4,000 – 6,500 | 6 | The Aristocrat 4,200 · The Armour 5,850 · Bronco 6,200 · The Stallion 6,500 |
| RFID (in `smart-wallets`) | 3 | KODO 2,300 · The Razor 2,450 · Kodo Vertical 2.0 2,450 (out of stock per the Oct 31 data pack, so not named in the copy) |

Out-of-stock wallets are deliberately not named: Crazy Horse Long, Elite Card Holder, Midtown Lite and The Kingsman, plus Sheppard and Saffiano with 1 unit each.

### a) Proposed SEO (send BOTH)
- **Title (59):** `Leather Wallet Price in Pakistan: Rs 1,499–6,500 | Kordovan`
- **Meta description (150):** `Genuine leather wallet prices in Pakistan: Rs 1,499 to 6,500. Full-grain, crazy horse and nappa, made in our own workshop. COD available, Rs 250 more.` *(CQRO fix F6, Nov 9: COD stated with its fee, as in CB-4 and LIVE-d; "stitched" → "made" because The Seamless is stitch-less.)*
  - No free-delivery claim in the meta, because COD orders over 5,500 still pay 250.
- **Trade-off (CEO decision):**
  - The price cluster is about 1,100 impr. The "wallets for men" cluster on the same page is much larger, and the current title serves it.
  - A safer alternative keeps both: `Leather Wallets for Men: Price in Pakistan Rs 1,499–6,500` (57 characters, no brand).
  - **My recommendation is the alternative**, because it protects the larger cluster. If the CEO prefers the pure price title, measure "leather wallet for men" position at 28 days and revert if it drops by more than 1 place.

### b) Field: `custom.editorial` (full replacement value below)
This keeps the live intro, the "Which wallet suits how you carry" section and the "Care" section, with these fixes:
- The Bastion link is repaired.
- The DRAFT Gator is removed.
- The delivery line is corrected.
- The old cost section and the "How to tell" section are replaced by the new block.

New price block: about 440 words including headings, from `<h2>Leather wallet price in Pakistan</h2>` to the blog link.

```html
<h2>Leather Wallets for Men in Pakistan</h2>
<p>A wallet is the one piece of leather you reach for every single day, so it is the one that shows whether you bought well. Ours are made in Pakistan from full-grain, nappa and crazy horse hide — leathers that do not merely survive daily carry but improve with it, darkening at the fold and along the edge into a patina that is yours alone.</p>

<h2>Leather wallet price in Pakistan</h2>
<p>Our men's wallets cost <strong>Rs 1,499 to Rs 6,500</strong> at regular price, inside the honest band for a genuine leather wallet made in Pakistan.</p>
<ul>
<li><strong>Rs 1,499 to 2,499.</strong> Slim sheep leather and minimal card carry: <a href="/products/rigor-wallet-lite">Rigor Lite</a>, the full-grain <a href="/products/the-luke-minimalist-wallet">Luke</a>, the nappa <a href="/products/nappa-leather-bifold-wallet-for-men-dark-brown">Plain Bifold</a>.</li>
<li><strong>Rs 2,500 to 3,999.</strong> Everyday bifolds in cow and crazy horse leather: <a href="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet">The Bastion</a>, <a href="/products/mocha-mate">Mocha Mate</a>, the crazy horse <a href="/products/the-truckkr-bi-fold">Truckkr</a>.</li>
<li><strong>Rs 4,000 to 6,500.</strong> More leather, more hand work: <a href="/products/the-armour-dual-mobile-wallet-with-notepad">The Armour</a>, <a href="/products/bronco-handcrafted-wallet">Bronco</a>, the handwoven full-grain <a href="/products/stallion-handcrafted-wallet">Stallion</a>.</li>
</ul>
<p>Our RFID wallets, the KODO and The Razor, sit at Rs 2,300 to Rs 2,450; see the <a href="/collections/smart-wallets">smart wallet range</a>.</p>

<h3>What drives the price</h3>
<ul>
<li><strong>Which layer of the hide.</strong> Full-grain keeps the outer surface and develops a patina; top-grain is sanded even. "Genuine leather" is a grade name, often split hide.</li>
<li><strong>Which leather.</strong> Cow is toughest, crazy horse is waxed so scratches burnish back, nappa is soft from day one, sheep is thinnest.</li>
<li><strong>Stitching and slots.</strong> The fold and card slots fail first on a cheap wallet. Tight, even stitching is where the money goes.</li>
<li><strong>RFID and hardware.</strong> A shielded lining, zip or clip adds cost.</li>
</ul>

<h3>What leather wallets cost across Pakistan</h3>
<ul>
<li><strong>Under Rs 800:</strong> almost certainly PU, rexine or bonded leather. It cracks along the fold, usually within a year.</li>
<li><strong>Rs 800 to 1,500:</strong> a blend, a thin split hide, or genuine leather on heavy discount. Ask what the outer material is.</li>
<li><strong>Rs 1,500 to 7,000:</strong> the honest band for a genuine leather wallet made locally.</li>
<li><strong>Above Rs 12,000:</strong> usually an imported label, not better hide.</li>
</ul>
<p>Bands are indicative; other brands' prices change weekly, so we do not quote them.</p>

<h3>Real leather or PU: three checks</h3>
<ul>
<li><strong>Press it.</strong> Leather creases and springs back; PU stays flat.</li>
<li><strong>Look at the pores.</strong> Irregular on hide, repeating on printed PU.</li>
<li><strong>Look inside a card slot.</strong> A fibrous, suede-like cut edge, not a fabric mesh.</li>
</ul>
<p>Wallets are ready-made and dispatched from stock, so <strong>cash on delivery is available</strong> (Rs 250 more), along with card and JazzCash. Delivery is free on orders over Rs 5,500 paid online.</p>
<p>Comparing brands? Read our <a href="/blogs/wallets/top-10-leather-wallet-brands-in-pakistan">guide to the top 10 leather wallet brands in Pakistan</a>.</p>

<h3>Which wallet suits how you carry</h3>
<ul><li><strong>Bifold</strong> — the default, and still the best for cash plus six to eight cards. Try <a href="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet">the Bastion</a> or the <a href="/products/mocha-mate">Mocha Mate</a>.</li><li><strong>Slim and minimalist</strong> — front-pocket carry, three to five cards, no bulk against the hip. See <a href="/collections/smart-wallets">the smart wallet range</a>, including RFID-protected options.</li><li><strong>Long wallet</strong> — notes flat and unfolded, which is how currency lasts. The right choice if you carry cash daily.</li><li><strong>Card holder and money clip</strong> — cards and a folded note, nothing else. The smallest thing that still does the job.</li></ul>

<h3>Care, and how long it should last</h3>
<p>A full-grain wallet should outlast a decade of daily use. Keep it out of a back pocket you sit on — the constant flex, not age, is what kills stitching — and condition it lightly once or twice a year. It will get darker and softer, and that is the leather working correctly, not wearing out.</p>
<p>Every Kordovan wallet carries a <strong>lifetime craftsmanship warranty</strong>: if stitching or hardware fails in normal use, we repair or replace it.</p>

<!-- FAQ block (c) follows here -->
```

### c) FAQ (append to the same `custom.editorial` value)
```html
<h2>Leather wallet prices: common questions</h2>
<h3>What is the price of a genuine leather wallet in Pakistan?</h3>
<p>A genuine leather wallet made in Pakistan costs roughly Rs 1,500 to Rs 7,000. Ours run from Rs 1,499 to Rs 6,500 at regular price, depending on the leather and how much hand work goes into it.</p>
<h3>Why are some leather wallets under Rs 1,000?</h3>
<p>Below about Rs 800 a wallet is almost always PU, rexine or bonded leather. It looks right for a season, then cracks along the fold, because that is where a coating fails first.</p>
<h3>Is a cow leather wallet better than sheep leather?</h3>
<p>Cow leather is tougher and darkens well with use, so it suits a bifold you carry daily. Sheep leather is thinner and lighter, which is why our slimmest wallets, such as the Rigor Lite, use it.</p>
<h3>How much does an RFID wallet cost, and do I need one?</h3>
<p>Our RFID wallets, the KODO and The Razor, are Rs 2,300 to Rs 2,450. RFID shielding only matters if you carry contactless cards; with chip-and-PIN cards alone, it does nothing for you.</p>
<h3>Can I pay cash on delivery for a wallet?</h3>
<p>Yes. Wallets are ready-made and dispatched from stock, so cash on delivery is available (Rs 250 more), as well as card and JazzCash. Delivery is free on orders over Rs 5,500 paid online.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is the price of a genuine leather wallet in Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "A genuine leather wallet made in Pakistan costs roughly Rs 1,500 to Rs 7,000. Ours run from Rs 1,499 to Rs 6,500 at regular price, depending on the leather and how much hand work goes into it."}},
    {"@type": "Question", "name": "Why are some leather wallets under Rs 1,000?", "acceptedAnswer": {"@type": "Answer", "text": "Below about Rs 800 a wallet is almost always PU, rexine or bonded leather. It looks right for a season, then cracks along the fold, because that is where a coating fails first."}},
    {"@type": "Question", "name": "Is a cow leather wallet better than sheep leather?", "acceptedAnswer": {"@type": "Answer", "text": "Cow leather is tougher and darkens well with use, so it suits a bifold you carry daily. Sheep leather is thinner and lighter, which is why our slimmest wallets, such as the Rigor Lite, use it."}},
    {"@type": "Question", "name": "How much does an RFID wallet cost, and do I need one?", "acceptedAnswer": {"@type": "Answer", "text": "Our RFID wallets, the KODO and The Razor, are Rs 2,300 to Rs 2,450. RFID shielding only matters if you carry contactless cards; with chip-and-PIN cards alone, it does nothing for you."}},
    {"@type": "Question", "name": "Can I pay cash on delivery for a wallet?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Wallets are ready-made and dispatched from stock, so cash on delivery is available (Rs 250 more), as well as card and JazzCash. Delivery is free on orders over Rs 5,500 paid online."}}
  ]
}
</script>
```

### Optional companion fix: `descriptionHtml`
The first paragraph (the 40 words that render) is accurate; keep it. Everything after it never renders and still carries the discontinued `kv2-gifting` link. Recommendation: trim `descriptionHtml` to the first `<p>` only.

### Expected traffic (ESTIMATE)
- **Baseline:** 1,101 impr / 90d, 58 clicks, CTR 5.27%, pos 7.9.
- **Target:** pos about 5.5 with a CTR of **7.0%**.
- **Estimate:** 1,101 × 7.0% = **about 77 clicks / 90d, +19**.

---

## 4. What this is worth in rupees (commercial line)

**Forecast = extra clicks × checkout rate × order value × survival.** All three pages are ESTIMATES.

| Page | +clicks / 90d | Checkout rate | Order value (regular) | Survival | Surviving revenue / 90d |
|---|---|---|---|---|---|
| Jackets | +100 | 0.58% | 28,066 (avg jacket price, CLAUDE.md) | 0.75 | **≈ Rs 12,200** |
| Oxford | +51 | 0.58% | 21,000 | 0.75 | **≈ Rs 4,700** |
| Wallets | +19 | 0.58% | 3,000 | 0.75 | **≈ Rs 250** |
| **Total** | +170 | | | | **≈ Rs 17,000 / 90d** |

**Assumptions** (each with the test that replaces it):
- **Clicks ≈ sessions.** Test: Shopify sessions by landing page for these 3 URLs, 28 days after publishing.
- **Checkout rate = 0.58%**, the site-wide Google-search rate (data pack, 90d to Oct 31). Price-intent searchers probably convert better, but that is unmeasured. Test: Shopify conversion by landing page.
- **Survival = 0.75**, from October's 25.3% real lost-order rate. Prepaid made-to-order pieces may survive better, but October jacket checkouts died at payment. Test: day-14 survival of orders that landed on these pages.
- **Target CTRs** are judgement against the measured site curve: the blog earns 14.8% at pos 2.2, and the jacket collection earns 4.5% at pos 5.1 on "original…".

**Not counted:**
- winter-peak impression growth;
- clicks on non-price queries for the same pages;
- AI-answer citations from the FAQ blocks;
- the blog's 1,514 impressions on "leather jacket price in pakistan".

**Honest read:**
- The direct rupee value is small: about Rs 17k per quarter at site-average conversion.
- The jacket page carries 70% of it. Jackets are the highest-value item and it is peak season, so **jackets first**, then the Oxford (a cheap snippet fix), then wallets.
- Do the work because it costs nothing and compounds. Do not expect it to fix November.

**Measure and STOP:**
- Re-pull `gsc_query ["query","page"]` 28 days after publishing (about Dec 11), for the same queries and pages.
- **Stop or revert rule:** if a page's price-query CTR has not risen at least **+1.0 point** at a similar position (±1), restore the previous title and meta. The old values are quoted above.
- If "leather wallet for men" loses more than 1 position, revert the wallet title at once.

---

## 5. Notes for whoever applies this (after Founder approval)
- `seo:` is a full replace: send the title AND the description each time.
- Write `custom.editorial` (`multi_line_text_field`) through GraphQL **variables**, not a `"""` block string. The JSON-LD contains quotes, and block strings keep backslashes literally. Re-query and read the value back afterwards.
- Editorial and the hero are separate surfaces. If the Founder settles full-grain versus top-grain, sweep:
  - the collection `descriptionHtml` and `custom.editorial`;
  - the jacket blog;
  - the product `custom.material`;
  - the `seo.description` on every jacket.
- **FAQ rich results:** since 2023, Google shows FAQ rich results only for authoritative government and health sites. So the FAQPage JSON-LD will **not** add SERP space or CTR. Its value is the visible on-page answers and machine-readable Q&A for AI answers (ChatGPT already sends orders: 2 orders, Rs 5,800 in 90d). My CTR estimates do not depend on it.
- Out of scope, flagged only: both Top-10 blogs name the shop's neighbourhood in the "Kordovan" entry. That is legacy content and not covered by the new-content rule, but it sits close to it. CEO's call.

---

## 6. Self-check against the hard rules
| Rule | Check |
|---|---|
| Never mention Karachi | None in any customer-facing draft (grep run on this file). The city list in the kept sizing section names Lahore, Islamabad, Rawalpindi and Hyderabad only. |
| No invented reviews, ratings, "X sold", stock counts | None. No ratings, quotes or sales counts. The product counts in the band tables are internal and not in the copy. |
| Competitor prices only as bands | Market bands only. No competitor is named anywhere in the drafts. |
| MTO = jackets + footwear, paid 100% online, "about 3 weeks to your door", terms paired with reason | Jacket block, jacket FAQ and both metas pair the terms with "cut for one customer in your size, cannot be resold" and "winter is our busiest season". The Oxford meta pairs "about 3 weeks" with "made in your size". No 4–7 days, no 50% deposit. |
| No COD promised on MTO | Jackets: "cash on delivery is not offered". Oxford: no COD mention. COD appears only on wallets (ready-made). |
| Free delivery over PKR 5,500 | Wallets: "over Rs 5,500 paid online". Jackets and Oxford say "free delivery", which is true because they are prepaid and above 5,500. |
| Prices true after Nov 12 | Every figure is a regular (compare-at) price. Publish Nov 13. |
| Claims match live product data | Materials follow `custom.material`. Top-grain versus full-grain is flagged for the Founder. "Fur collar" comes from the Urban Rider title. "Leather sole" and "cow leather" come from the Oxford description. |
| Free tools only, no Shopify writes | Read-only GraphQL and GSC only. Nothing changed. |
| Voice | No emoji, no exclamation marks, no urgency, no discount voice. |

**Unverified, needs a human:**
1. Full-grain or top-grain on the jackets (live copy and metafields disagree).
2. "Lifetime craftsmanship warranty": `custom.warranty` is empty on every product read. The claim exists only in the theme fallback, the blogs and the live editorial. I kept it on the wallet page, where it is already live, and added it nowhere new.
3. The "fur collar" material on Urban Rider (real or faux). The copy says only "fur collar", as the product title does.
4. Whether jacket linings are a full lining on every style ("properly lined" is carried over from the blog).

**READY FOR CQRO**

---

## 7. CQRO review (Hamna Qureshi, 2026-11-09)

**Level:** L2 (customer-facing, Founder approves). The maker's classification is correct. Register rows PP-1 to PP-14.
**Sources (all read-only, 2026-11-09):** Shopify GraphQL: both collections with every product, variant price/compareAt/stock, `custom.material`, `custom.made_to_order`, `custom.editorial`, SEO; Oxford product; Iconic + Hawkeye size options; Nightfall, Waxed Rider and Urban Rider descriptions; `smart-wallets` collection; the 3 linked jacket collections; all blogs/articles; delivery profile `48076685501`. GSC `["page"]`, queries containing "price", 2026-08-10 → 11-07. `sections/main-collection.liquid:34-35, 144-145`.

### Verdict per page
| Page | Verdict | Gate before publish |
|---|---|---|
| `/collections/mens-leather-jackets` | **APPROVED WITH FIXES** | (1) Founder answers Q1 (grade). (2) The hero `descriptionHtml` fix is **mandatory, not optional**, and ships in the same change, or the page says full-grain above the grid and top-grain below it. |
| `/products/kordovans-premium-oxford-leather-shoes-black` | **APPROVED WITH FIXES** | Publish on/after Nov 13 (price revert). |
| `/collections/mens-leather-wallets` | **APPROVED WITH FIXES** | Title choice (Q2). Publish on/after Nov 13. |

### What checked out (live, Nov 9)
- **Jacket bands:** 28 products, all ACTIVE, all `made_to_order = true`, regular (compare-at) min 22,000 (Iconic), max 35,000 (Urban Rider). Bands 8 / 13 / 7 reproduce exactly. Average compare-at = 785,850 ÷ 28 = **28,066.07**, which matches the CLAUDE.md figure used in §4. Sizes S to XXXL with chest ranges (Iconic, Hawkeye).
- **Oxford:** ACTIVE, MTO true + tag, 6 sizes at 17,850 / compare-at **21,000**. "Cow leather" is sourced (description "Soft cow leather", tags `cow`, `cowleather`).
- **Wallets:** 23 in collection, 21 ACTIVE (Gator, HM The Lord's DRAFT). In-stock regular min 1,499 (Rigor Lite, also Sheppard 1 unit), max 6,500 (Stallion, 8 units). Every named wallet is ACTIVE and in stock. Materials match `custom.material` (Rigor Lite sheep, Luke full-grain cow, Plain Bifold nappa, Bastion distressed cow, Mocha Mate cow, Truckkr crazy horse, Stallion full-grain cow). RFID: KODO 2,300 (16) and Razor 2,450 (65); Kodo Vertical 2.0 out of stock, correctly not named.
- **Delivery terms:** live profile: Pay Online 250 (≤5,499) / 0 (≥5,500); COD 500 / 250. So "free over 5,500 paid online" and "COD Rs 250 more" are exact; jackets and the Oxford are always prepaid and over 5,500, so "Delivery is free" is true for them.
- **Links:** every product/collection/blog link in the blocks (8 jacket products, 9 wallet products, 4 collections, 2 articles) resolves to ACTIVE products, published collections (biker 17, bomber 6, black 15, smart-wallets 6 products) or published articles (`jackets/top-10-leather-jacket-brands-in-pakistan`, `wallets/top-10-leather-wallet-brands-in-pakistan`). The repaired Bastion handle is correct.
- **Hard rules:** no Karachi, no competitor named, no review, rating, count or "sold" figure, no 4–7 days, no 50% deposit, no COD on any MTO line, no "!".
- **JSON-LD:** both blocks are well-formed JSON (straight quotes, no inner double quotes, no trailing commas) and each Answer text is identical to its visible `<p>` (re-checked after my edits). Rendered raw by `main-collection.liquid:145`, so it will reach the HTML. Agree with §5: no FAQ rich result is expected; CTR estimates do not rely on it.
- **Character counts** (recounted): jacket title 53, Oxford title 52, wallet title 59 (alternative 57). Metas after fixes: 151 / 153 / 150. Both SEO fields are given for all three pages.
- **Arithmetic:** 4,606 × 5.0% = 230 (+102); 1,671 × 4.0% = 67 (+51); 1,101 × 7.0% = 77 (+19). Rupee lines 12,209 / 4,659 / 248 = 17,116; jackets 71%. All labelled ESTIMATE. GSC clicks reproduce exactly (128 / 16 / 58). Note: page-level impressions are higher (4,740 / 1,815 / 1,261) because the page view includes anonymised queries; **the Dec 11 re-measure must use the same query+page method**, or the before/after will not compare.

### Fixes made by CQRO (mechanical, sourced; meaning, offer and price unchanged)
| # | Where | Was | Now | Source / rule |
|---|---|---|---|---|
| F1 | Jacket meta | No payment term; "Top-grain sheepskin" | "Each cut in your size for one customer, so paid online; about 3 weeks to your door." Material word removed pending Q1 | MTO terms always with reason (CLAUDE.md); grade unresolved |
| F2 | Jacket block, top band | "The patterns that use the most hide" | "The top of the range" | Unsourced product fact |
| F3 | Jacket "What drives the price" | "A jacket takes roughly 25 to 35 square feet" | Number removed | Only source is our own unpublished blog draft `docs/blog/leather-jacket-price-in-pakistan.html:71`; no workshop figure |
| F4 | Jacket FAQ Q4 (visible + JSON-LD) | "Every jacket we make is sheepskin." | "Every jacket on this page is sheepskin; any style can also be made in cowhide, priced separately, if you ask us on WhatsApp." | Every jacket description (live): "We can also make any of them in cow hide… priced separately" |
| F5 | Oxford meta | No "paid online" | "made in your size for one customer, paid online, about 3 weeks to your door. Free delivery." | MTO rule |
| F6 | Wallet meta | "stitched…", "Cash on delivery available." | "made in our own workshop. COD available, Rs 250 more." | Delivery profile; precedent CB-4, LIVE-d; The Seamless is stitch-less |
| F7 | Wallet intro | "cut and hand-stitched" (universal) | "made in Pakistan" | The Seamless "Stitch-less" (live title) |
| F8 | Wallet band 2 | "Everyday cow-leather bifolds" | "Everyday bifolds in cow and crazy horse leather" | Truckkr `custom.material` "Crazy Horse Leather" (no animal stated) |
| F9 | Wallet RFID line + FAQ Q4 (visible + JSON-LD) | "RFID smart wallets" linked to `smart-wallets` | "RFID wallets, the KODO and The Razor…; see the smart wallet range" | `smart-wallets` also holds non-RFID Mocha Mate, Illusion, Elite Card Holder |
| F10 | Wallet payment line + FAQ Q5 (visible + JSON-LD) | "cash on delivery is available" | "…available (Rs 250 more)" | Delivery profile |
| F11 | Wallet FAQ Q3 (visible + JSON-LD) | "which is why slim front-pocket wallets use it" | "which is why our slimmest wallets, such as the Rigor Lite, use it" | Luke and Stallion are slim but cow leather |

### Corrections to the maker's findings (§0)
- **Finding 3 is half right.** Standard sizes S to XXXL are the default, but every jacket description offers "built to your own measurements" on WhatsApp. So the live "built to your measurements" is over-broad, not false. The draft wording "cut in your size" is true and stays.
- **Finding 2:** 26 of 28 `custom.material` values say top-grain; Nightfall ("Diamond-quilted sheep leather") and Waxed Rider ("Waxed pull-up sheep leather") state no grade. Both *descriptions* say "Premium top-grain sheep leather", as do all the others, so the top-grain claim is sourced across all 28. The full-grain claim lives only on the collection hero, the collection editorial and the blog, and in my own Oct 31 AD-1 fix to `ad-director.md` (which used "full-grain"; that must be swept too).

### Returned / open (needs the Founder or Omar)
- **R1 (Founder, Q1):** jacket grade. Product data says top-grain on all 28. If confirmed, sweep: collection hero + editorial (this draft), `seo.description` of every jacket, the jacket blog(s), `ad-director.md` (AD-1 text), any live jacket ad creative. If full-grain is true instead, all 28 product descriptions and 26 metafields are wrong and the drafts must change.
- **R2 (CEO/Founder, Q2):** wallet title. CQRO has no compliance preference; both are true and within 60. Omar recommends the alternative to protect the "wallets for men" cluster.
- **R3 (Omar, low):** the market list jumps from "8,000 to 15,000" to "20,000 to 40,000" and from 40,000 to "above 45,000" (wallets: 7,000 to 12,000). A reader will ask about the gap. Close it or say "bands are indicative" earlier. Not a blocker.
- **R4 (Omar, low):** §4 uses wallet order value 3,000 with no source (CLAUDE.md: the 8 sale orders before Nov 8 averaged ~2,300; regular in-stock wallet midpoint ~2,800). Label it an assumption. Survival 0.75 uses CLAUDE.md's 25.3%; register CR-5 restated October at 22.3%. Either way the total moves by under Rs 1,000.
- Warranty line on wallets: sourced to the theme's PDP fallback (`snippets/pdp-main.liquid`, CB-2) and already live; no wallet has a narrower warranty (the 1-year exception is the Stallion **boot**, not the Stallion wallet). Approved.

**Riskiest item:** publishing the jacket editorial without the hero fix (or without Q1), which would put "full-grain" and "top-grain" on one page. **Next check:** on Nov 13, before apply, re-read compare-at = price on all three pages (revert done) and read back the written `custom.editorial` values.

---
## 8. PUBLISHED 2026-11-13 ~09:47 PKT (Founder "go ahead", Nov 13)
- Jackets: seo title+description (F1), hero `descriptionHtml` (top-grain, "cut in your size for one customer", no workshop), `custom.editorial` (price block + FAQ + JSON-LD; intro "made to order in Pakistan").
- Wallets: alternative title "Leather Wallets for Men: Price in Pakistan Rs 1,499–6,500" (Q2), meta with "handcrafted in Pakistan" (supplier rule, Nov 12), `custom.editorial` (price block + FAQ + JSON-LD).
- Oxford: seo title + description (F5).
- All read back live; all named products ACTIVE, wallets in stock, prices = regular. GSC re-measure ~Dec 11 with the SAME query+page method; revert any page whose price-query CTR is not up ~1 pt.
- Not done (optional): trimming the hidden wallet `descriptionHtml` (still holds a `kv2-gifting` link that never renders).
