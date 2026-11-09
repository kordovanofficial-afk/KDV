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
- **Meta description (151):** `Original men's leather jacket prices in Pakistan: Rs 22,000 to 35,000. Top-grain sheepskin, each cut in your size, so allow about 3 weeks to your door.`
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
<li><strong>Rs 30,000 to 35,000.</strong> The patterns that use the most hide: <a href="/products/desert-voyager-mens-brown-sheepskin-leather-bomber-jacket">Desert Voyager</a>, the double-breasted <a href="/products/hawkeye-mens-brown-double-breasted-vintage-coat-s012">Hawkeye</a>, <a href="/products/mens-urban-rider-brown-leather-biker-jacket">Urban Rider</a>.</li>
</ul>

<h3>What drives the price</h3>
<ul>
<li><strong>The grade of hide.</strong> Full-grain keeps the whole outer surface; top-grain is lightly corrected for an even finish. "Genuine leather" on a label is a grade name, often split hide, the weaker under-layer. Every jacket here is top-grain sheepskin, lighter and softer than cowhide.</li>
<li><strong>How much hide.</strong> A jacket takes roughly 25 to 35 square feet. Longer cuts, quilting and double-breasted fronts use more.</li>
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
<p>Not by rule. Price follows the grade and the amount of hide more than the animal. Sheepskin is lighter and softer; cowhide is heavier and tougher. Every jacket we make is sheepskin.</p>
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
    {"@type": "Question", "name": "Is a sheep leather jacket cheaper than cow leather?", "acceptedAnswer": {"@type": "Answer", "text": "Not by rule. Price follows the grade and the amount of hide more than the animal. Sheepskin is lighter and softer; cowhide is heavier and tougher. Every jacket we make is sheepskin."}},
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
- **Meta description (153):** `Oxford shoes price in Pakistan: Rs 21,000. Black cow leather, leather sole, made in your size in our own workshop, so allow about 3 weeks. Free delivery.`
  - "Made in your size … so allow about 3 weeks" pairs the term with its reason.
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
- **Meta description (154):** `Genuine leather wallet prices in Pakistan: Rs 1,499 to 6,500. Full-grain, crazy horse and nappa, stitched in our own workshop. Cash on delivery available.`
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
<p>A wallet is the one piece of leather you reach for every single day, so it is the one that shows whether you bought well. Ours are cut and hand-stitched in Pakistan from full-grain, nappa and crazy horse hide — leathers that do not merely survive daily carry but improve with it, darkening at the fold and along the edge into a patina that is yours alone.</p>

<h2>Leather wallet price in Pakistan</h2>
<p>Our men's wallets cost <strong>Rs 1,499 to Rs 6,500</strong> at regular price, inside the honest band for a genuine leather wallet made in Pakistan.</p>
<ul>
<li><strong>Rs 1,499 to 2,499.</strong> Slim sheep leather and minimal card carry: <a href="/products/rigor-wallet-lite">Rigor Lite</a>, the full-grain <a href="/products/the-luke-minimalist-wallet">Luke</a>, the nappa <a href="/products/nappa-leather-bifold-wallet-for-men-dark-brown">Plain Bifold</a>.</li>
<li><strong>Rs 2,500 to 3,999.</strong> Everyday cow-leather bifolds: <a href="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet">The Bastion</a>, <a href="/products/mocha-mate">Mocha Mate</a>, the crazy horse <a href="/products/the-truckkr-bi-fold">Truckkr</a>.</li>
<li><strong>Rs 4,000 to 6,500.</strong> More leather, more hand work: <a href="/products/the-armour-dual-mobile-wallet-with-notepad">The Armour</a>, <a href="/products/bronco-handcrafted-wallet">Bronco</a>, the handwoven full-grain <a href="/products/stallion-handcrafted-wallet">Stallion</a>.</li>
</ul>
<p>Our <a href="/collections/smart-wallets">RFID smart wallets</a> sit at Rs 2,300 to Rs 2,450.</p>

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
<p>Wallets are ready-made and dispatched from stock, so <strong>cash on delivery is available</strong>, along with card and JazzCash. Delivery is free on orders over Rs 5,500 paid online.</p>
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
<p>Cow leather is tougher and darkens well with use, so it suits a bifold you carry daily. Sheep leather is thinner and lighter, which is why slim front-pocket wallets use it.</p>
<h3>How much does an RFID wallet cost, and do I need one?</h3>
<p>Our RFID smart wallets are Rs 2,300 to Rs 2,450. RFID shielding only matters if you carry contactless cards; with chip-and-PIN cards alone, it does nothing for you.</p>
<h3>Can I pay cash on delivery for a wallet?</h3>
<p>Yes. Wallets are ready-made and dispatched from stock, so cash on delivery is available, as well as card and JazzCash. Delivery is free on orders over Rs 5,500 paid online.</p>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is the price of a genuine leather wallet in Pakistan?", "acceptedAnswer": {"@type": "Answer", "text": "A genuine leather wallet made in Pakistan costs roughly Rs 1,500 to Rs 7,000. Ours run from Rs 1,499 to Rs 6,500 at regular price, depending on the leather and how much hand work goes into it."}},
    {"@type": "Question", "name": "Why are some leather wallets under Rs 1,000?", "acceptedAnswer": {"@type": "Answer", "text": "Below about Rs 800 a wallet is almost always PU, rexine or bonded leather. It looks right for a season, then cracks along the fold, because that is where a coating fails first."}},
    {"@type": "Question", "name": "Is a cow leather wallet better than sheep leather?", "acceptedAnswer": {"@type": "Answer", "text": "Cow leather is tougher and darkens well with use, so it suits a bifold you carry daily. Sheep leather is thinner and lighter, which is why slim front-pocket wallets use it."}},
    {"@type": "Question", "name": "How much does an RFID wallet cost, and do I need one?", "acceptedAnswer": {"@type": "Answer", "text": "Our RFID smart wallets are Rs 2,300 to Rs 2,450. RFID shielding only matters if you carry contactless cards; with chip-and-PIN cards alone, it does nothing for you."}},
    {"@type": "Question", "name": "Can I pay cash on delivery for a wallet?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Wallets are ready-made and dispatched from stock, so cash on delivery is available, as well as card and JazzCash. Delivery is free on orders over Rs 5,500 paid online."}}
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
