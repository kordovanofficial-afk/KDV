# KORDOVAN Meta ads study, Nov 1-27 2026, and the plan from Dec 1
**Status:** L0 analysis + L3 proposals for the Founder. **Nothing was changed live** (no Meta, Shopify, theme, git push or WhatsApp action).
**Written:** 27 Nov 2026, Claude through the Alex lens (`.claude/agents/alex.md`). **Extends** `ops/marketing/ads/DEC_2026_STRUCTURE_ALEX.md` (5,000/day): same ad sets and budgets, and it adds a placement rule, a video rule and a production plan.
**Founder's question (Nov 27):** which ads and creatives performed this month and why; should we push only image ads or video too, and WHY; where do sales come from by placement, so that from Dec 1 we spend only there.

**Sources:** Meta account `995683712074843`. Ad level, placement (publisher_platform × platform_position) and device for Nov 1-27, plus a second placement cut for Nov 14-27. Shopify: all 238 orders created Nov 1-27, joined to ads by last-visit `utm_content`. H1 and H3 also carry `utm_term={{placement}}`, so their orders can be matched to placements in Shopify.
**How to read the numbers:** "Meta" = Meta-reported, which over-reports by about 2.05x. "Placed" = Shopify orders, cancelled ones included. "Live" = orders that are not cancelled. Many orders from Nov 20 on are still PENDING, so final COD refusal is not known yet. Ceilings are Shopify placed CPA per product: Mocha ~1,460 · gloves 1,000 · catalogue mix ~1,500 · hats ~1,800 (provisional).

---

## 1. Executive verdict [Alex lens]
1. **The real problem is not image vs video. It's that we have only ~3 ads that sell, and the best one is getting tired.** H1 Mocha "Comparison" is 26% of November spend and 32% of Meta-tagged Shopify orders. Its 7-day Meta CPA went 926 → 874 → 1,168 → 1,324 over four weeks, CTR fell from 2.29% to 1.96% and CPM rose. Mocha Mate also has about 11 units left.
2. **Our #1 ad is already a VIDEO, but it sells like a picture.** The H1 video is 64 seconds long, people watch it for 4 seconds on average, and only 0.5% reach 95%. The sale happens in the first frames: two wallets side by side, "one is new, one is six months old". **Format is not the lever. The hook (a visible comparison or proof) and the product/price are.**
3. **Shopify-confirmed cost per placed order by format:** video 1,245 · carousel 1,138 · catalogue 1,385 · single image 1,597 (1,920 without the Clifford hat). No format wins on its own. What wins is the **comparison hook on cold traffic** (H1 1,173, W01 gloves 1,157) and a **warm, high-ticket, single-product static** (Clifford hat 744 per placed order, Rs 84.6k live revenue on Rs 8.2k spend).
4. **Sales come from four placements:** FB Feed, FB Reels, IG Feed and IG Reels take **89.8% of spend and 95.1% of Meta purchases**. FB Reels is the cheapest (Meta CPA 800; H1 by Shopify utm_term: 865 per placed order). The tail (Stories with 4:5 creatives, In-stream, WhatsApp Status, Audience Network, Search, Threads) took ~10% of spend for ~4% of purchases, and **0 purchases in the last 14 days** (Rs 5.3k outside the four core placements and marketplace/explore).
5. **From Dec 1:** make **3 new creatives a week** (12 in December), about 2 statics to 1 short video (8-15 s, hook in the first second, 4:5). Build the H1 successor now. Use the 4 core placements on new or changed ad sets only. **Leave the proven ad sets alone** (H1, Retarget v2, RT-W).

**One thing this week:** the Founder sends the original H1 video file and films three 15-second desk clips by Dec 6 (section 5).

---

## 2. Creative leaderboard, Nov 1-27 (ad level)
Sorted by spend. Shopify = last-visit utm_content. Cancel % = cancelled ÷ placed so far. CTR = link CTR (Meta's "CTR (all)" is in brackets for the larger ads).

| # | Ad (utm_content) | Format | Angle | Product | Audience | Spend | Meta purch / value | Shopify placed / live / live rev | Cost per placed | Cancel % | CTR | CPM | Freq | Verdict + WHY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 "Comparison" (`h1_comparison`) | **Video 64 s** | comparison: new vs 6-month-old (proof + value) | Mocha Mate 3,200 | cold LLA 1-3% | 41,064 | 39 / 132,030 | **35 / 25 / 83,780** | **1,173** (0.80x ceiling) | 29% | 1.6% (2.1%) | 416 | 1.81 | **WINNER, tiring.** Why it sells: frame 1 is the whole argument (two wallets, "can you tell which?"), the copy kills the fake-leather fear, and it names Pakistani details (CNIC window, checkpost, COD). Hook rate 17.8%, average watch 4 s. Fatigue: weekly CPA +43% from week 1 to week 4, CTR −14%. Not at the refresh trigger yet (CTR −30%), but close. |
| 2 | Retarget catalogue (old, `Facebook_UA`) | Catalogue (DPA) | reminder "you were almost there" | mix | warm + buyers | 24,468 | 38 / 183,299 | 19 / 14 / 55,750 | 1,288 (0.86x) | 26% | 5.1% | 347 | 4.58 | **Worked, now DISAPPROVED** (tobacco cases in the set). Its replacement, v2, is live. Its copy promised "7-Day No-Questions Return" and showed jackets, which is wrong for MTO. Never reuse. |
| 3 | W01 Gloves comparison (`w01_comparison`) | Single image | comparison: synthetic vs sheep leather | Gloves 1,950 | cold | 12,730 (two ad sets) | 12 / 66,250 | 11 / 9 / 25,750 | 1,157 (1.16x) | 18% | 1.2% | 200 | 1.57 | Good early in the month, then burned out (Monday read: 1,959 per order Nov 9-22). Comparison works for gloves too, but the gloves audience is small and gets saturated fast. |
| 4 | BF Clifford hat (`bf_clifford`) | Single image 4:5 | price + status ("was 10,500"), real end date | Clifford hat 6,820 | warm (bag/hat viewers + visitors + buyers) | 8,182 | 11 / 77,770 | **11 / 10 / 84,590** (+1-2 untagged hat orders) | **744** (0.41x) | 9% | 2.2% (3.1%) | 272 | 1.73 | **BEST ROI of the month.** High ticket, few look-alikes in Pakistan, warm audience, honest sale price. Several orders were 2 hats. Low cancel rate (higher price = more considered order, as in ADS_PLAYBOOK §6). It must re-prove itself at full price. |
| 5 | S4 11.11 carousel 6 wallets | Carousel | sale % off | 6 wallets | warm 180D | 6,143 | 7 / 17,123 | 5 / 4 / 9,120 | 1,229 | 20% | 2.1% | 411 | 2.00 | OK in the sale. **This corrects the Nov 23 read** ("1 placed / 0 live"): that read used a Nov 9-22 window and missed the Nov 8 orders. Low order value (avg ~2,280). |
| 6 | MOF Ordered vs Arrived (`mof_mocha_orderedvsarrived_trust_real_v1`) | Single image (real photo) | trust | Mocha | warm, no ATC | 5,296 | 2 / 6,900 | 1 / 1 / 2,650 | 5,296 | 0% | 1.8% | 292 | 1.61 | **LOST.** It answers a fear but gives no reason to buy now. A trust image without the product's value argument doesn't close. Keep the idea as a supporting card, not a standalone ad. |
| 7 | Shopify Autopilot (catalogue) | Catalogue | none ("Shop our collection") | mix | all Pakistan, no refuser exclusion | 5,160 | 2 / 4,650 | 2 / 1 / 2,450 | 2,580 | 50% | 5.0% | 425 | 1.76 | **LOST**, correctly paused. Generic copy, no targeting discipline. |
| 8 | TEASER T1+T2 (ThruPlay) | Video 14 s, 9:16 | "something is being made" | none | cold | 5,236 | 0 | 0 | — | — | 1.2-1.5% | 177-200 | 1.3 | **LOST for sales.** It bought cheap views (75% hook, 65% ThruPlay), which is not purchases. Its copy also said "our own workshop" (banned now). Never run awareness objectives on this budget. |
| 9 | S1 11.11 Bastion static 4:5 | Single image | sale % off | Bastion (wallets) | warm 180D | 4,974 | 3 / 16,250 | 4 / 4 / 18,370 | 1,244 | 0% | 2.6% | 429 | 1.91 | OK. One 11,710 order made it look like the winner. Copy said "full-grain, made in our own workshop" (banned). |
| 10 | S2 11.11 five-wallet video 15 s 9:16 | Video 15 s | sale % off, 5 products | 5 wallets | warm 180D | 4,949 | 5 / 19,490 | 3 / 3 / 13,090 | 1,650 | 0% | 2.4% | 528 | **2.88** | Weakest of the three sale formats. **Hook rate only 11.5%** (vs H1 17.8%): it opens on a sale graphic, not on a product reason. Highest CPM and frequency. |
| 11 | W-RT2 gloves leather close-up | Single image | proof (texture) | Gloves | warm 180D | 4,588 | 3 / 7,150 | 2 / **0** / 0 | — | **100%** | 1.5% | 204 | 1.40 | **LOST.** Both orders cancelled. Close-ups alone don't sell. |
| 12 | Truckkr comparison Rs 900 vs 3,800 | Single image | comparison (value) | Truckkr 3,800 | cold test | 4,270 | 1 / 4,200 | 1 / 0 | — | 100% | 1.2% | 614 | 1.35 | **LOST.** An unknown Rs 3,800 wallet cold, very high CPM (614), and the copy said "zip coin pocket" (coins rule broken; it is paused). Comparison alone can't carry a product nobody is searching for. |
| 13 | H3 Founder voice | Video 69 s | founder story, 6 months of use | Mocha | cold | 3,772 | 3 / 14,500 | 2 / 2 / 7,850 | 1,886 (1.29x) | 0% | 2.2% | 502 | 1.48 | **LOST** (paused Nov 8). Same product and hook rate (17.7%) as H1, but it opens on a person talking, so the PROOF comes late. Copy said "Karachi workshop" (banned). |
| 14 | RT comparison gloves v2 | Single image | comparison | Gloves | gloves viewers 30D | 3,281 | 1 / 2,450 | 2 / 2 / 4,900 | 1,640 (1.64x) | 0% | 1.2% | 246 | 1.43 | Right to pause. The warm audience had already seen the cold comparison. |
| 15 | W-RT1 Winter Kit cap + gloves | Single image | bundle | Cap + gloves | warm 180D | 3,092 | 3 / 13,850 | 2 / 2 / 6,900 | 1,546 | 0% | 1.8% | 427 | 1.41 | Middling. A bundle without a bundle price is just two products. |
| 16 | RT-W chai dhaba (`rtw_gloves_chaidhaba_warm_lifestyle_v2`) | Single image, lifestyle | lifestyle/emotion ("doodh patti, warm hands") + "you had a look" | Gloves | gloves viewers 30D | 3,007 | 5 / 16,430 | 3 / 3 / 6,850 | 1,002 (1.00x) | 0% | 1.3% | 386 | 1.61 | **KEEP.** The only gloves ad still at its ceiling. Warm audience + a local, emotional scene + price + COD. 80% of its Meta purchases came from FB Feed. |
| 17 | BF bag statics (Gridle, Venture, Executive, DBLP, Corporate, Diva) + carousel | Image / carousel | sale price + patina | Bags 4,290-21,400 | warm | 10,422 total | 5 / 50,520 | 5 / 4 / 32,080 tagged | ~2,084 | 20% | ~2.0% | 410-777 | 1.4 | **Weak per Rs spent**, but there were two big untagged bag orders (40,220 and 39,840) that we can't attribute. Bags = long consideration. Per Dec plan, no bag ad set in December. |
| 18 | Retarget v2 clean catalogue (`bof_clean_v2`) | Catalogue | reminder, COD, 7-day returns | in-stock mix | warm | 2,231 (since Nov 26) | 2 / 6,350 | 2 / 2 / 6,350 | 1,116 | 0% | 2.3% | 338 | 1.70 | Early, on track. Judge at ≥3,000 spend (Dec 4). |
| — | Truckkr patina, zip; W02-W05; S3 story 9:16; BF Diva/Corporate | various | — | — | — | each < 1,800 | 0-1 | 0 | — | — | — | — | — | Too little spend to judge (W02-W05) or failed (S3: 973 spent, 0 orders, a 9:16 static). |

**Totals Nov 1-27:** Meta spend **157,578**; Meta purchases 143 / Rs 642,932 (4.08x Meta ROAS). Shopify Meta-tagged orders: **109 placed / 85 live / Rs 353,940 live**. That is Meta ÷ Shopify-live = **1.82x** (consistent with the ~2x rule), real ROAS on tagged live revenue **2.25x**, right at break-even (2.22x). Another 122 orders had no utm (Rs 750k live, including the big bag/jacket orders, IG link-in-bio, organic and direct); some of them are Meta-influenced, but we can't prove it.

### Patterns, each seen in ≥2 ads (this is what "winning" means in the Ads OS)
- **Comparison beats every other cold hook:** H1 (1,173) and W01 (1,157) won; Truckkr comparison lost because of the product, not the hook. **Founder-led storytelling, teasers and close-ups lose** (H3, T1/T2, W-RT2).
- **Warm + single product + real price beats warm + many products:** Clifford 744 and chai dhaba 1,002, vs bags carousel/statics ~2,084, Winter Kit 1,546 and S4 1,229 (sale-only).
- **Higher price = lower cancel:** Clifford 9%, bags 20%, vs Mocha 29% and Autopilot 50%. The **H1 orders from FB Reels cancel at 33% (7 of 21)** against 1 of 14 from other placements. That is an early warning on cheap-reach placements (small sample).
- **Trust-only creatives don't close on their own** (MOF Ordered vs Arrived, W-RT2 close-up).
- **Rule check on old copy:** S1, S2, T1 ("our own workshop", "full-grain"), H3 ("Karachi workshop"), Truckkr ("zip coin pocket") and the old Retarget (jackets with 7-day returns) all break current rules. They are paused or ended. **Never relaunch any of them as-is.** H1's copy is clean, but "Over 4,000 wallets sold since 2021" needs a source (see section 8).

---

## 3. Image vs video: the answer and the WHY
### What our own data says
| Format (Nov 1-27) | Spend | Shopify placed / live | Live revenue | Cost per placed | Cost per live | Live rev ÷ spend |
|---|---|---|---|---|---|---|
| Video (H1, S2, H3) | 49,785 | 40 / 30 | 104,720 | **1,245** | 1,660 | 2.10 |
| Single image (all statics) | 63,868 | 40 / 33 | 171,010 | 1,597 | 1,935 | **2.68** |
| … of which Clifford hat | 8,182 | 11 / 10 | 84,590 | 744 | 818 | 10.34 |
| … images without Clifford | 55,686 | 29 / 23 | 86,420 | 1,920 | 2,421 | 1.55 |
| Carousel (S4, BF bags) | 6,831 | 6 / 5 | 13,660 | 1,138 | 1,366 | 2.00 |
| Catalogue (Retarget old/v2, Autopilot) | 31,859 | 23 / 17 | 64,550 | 1,385 | 1,874 | 2.03 |
| Teaser video (ThruPlay objective) | 5,236 | 0 | 0 | — | — | 0 |

**Video hook metrics** (3-sec plays ÷ impressions = hook rate; ThruPlay ÷ 3-sec plays = hold):
| Ad | Length | Hook rate | Hold | Avg watch | p25 / p50 / p95 of impressions | Result |
|---|---|---|---|---|---|---|
| H1 Comparison | 64 s | **17.8%** | 30% | 4 s | 5.1% / 2.8% / 0.5% | WINNER |
| H3 Founder | 69 s | 17.7% | 25% | 5 s | 4.2% / 2.7% / 0.3% | lost |
| S2 five wallets | 15 s | 11.5% | 21% | 2 s | 9.4% / 4.7% / 2.5% | weak |
| T1/T2 teaser | 14 s | 75% (ThruPlay-optimised, bought viewers) | 87% | 10 s | — | 0 sales |

### WHY, in our context
1. **The winning video is a moving picture.** 99.5% of people never see the end of H1, and the average viewer watches 4 seconds. The sale is made by what is on screen in seconds 0-3 (two wallets, the question) and by the copy. So "video" earns its place only when the **first frame is the argument**. A 64-second video costs as much to make as a 12-second one and the extra 60 seconds sell nothing.
2. **Same product, same hook rate, different first second:** H1 and H3 are both Mocha, both 6-month proof, both a ~17.7% hook rate. H1 opens on the comparison and won; H3 opens on a person talking and lost (1,886 vs 1,173). **Proof first, person later.**
3. **Video has one structural advantage in OUR account: the Reels inventory.** Reels (FB + IG) take 40% of spend at the cheapest CPMs (302-345) and gave 43% of Meta purchases. But the **Clifford 4:5 STATIC sold best in IG Reels** (5 of 11 Meta purchases, CPA 437). So Meta already puts statics into Reels. Video is **not required** to reach Reels; it is a way to show **motion proof** (flex, fit, what fits inside, patina) that a still can't.
4. **Pakistan mobile + COD:** 98% of spend is on phones (Android 55% of spend at CPA 1,061; iPhone 44% at CPA 1,175, with higher order value: 4,550 vs 3,870 per Meta purchase). Mobile data and sound-off viewing favour **short, silent-readable** video (on-screen text in English with an optional Roman-Urdu line), not talk.
5. **Production reality:** no workshop footage exists or can be shot. The only real video source is the Founder's desk (hands + product). AI motion from stills is free if Claude makes it (parallax, push-in, light sweep, text animation; no paid generators, per the HARD RULE). A Founder phone clip takes about 10 minutes plus about 30 minutes of Claude editing. A GPT static takes about 10 minutes. **Cost per test is similar, so the choice should follow what the hook needs.**

### Recommendation
- **Not image-only, and not video-first. Hook-first:** ~2 statics : 1 short video per week. Statics stay the backbone (cheap, fast, proven on warm and high-ticket). Videos are reserved for hooks that need motion.
- **Videos to make:** (a) **8-15 s edited desk clips** from the Founder's office, opening with the result in frame 1 (pocket test, glove fit/flex, new-vs-used wallet side by side). (b) **A 15 s re-cut of H1** (first 3 s unchanged, cut to the proof plus 3 benefit cards plus price/COD end card) as its successor. (c) **6-8 s AI-motion versions of a winning static** (subtle push-in + text animation), tested against the same static.
- **Video spec:** 1080×1350 (4:5) master, 8-15 s. Hook visible at 0.0 s, price on screen by 5 s, end card with price + "Cash on delivery all over Pakistan" + logo for the last 2 s. Captions/text burned in, readable with sound off, no music the account doesn't own a licence for. File < 4 GB, H.264, 30 fps.
- **Don't make:** talking-head founder intros · 30-70 s stories · teasers or ThruPlay-objective videos · multi-product sale-graphic videos (S2) · 9:16-only statics (S3) · anything implying "our workshop" footage · UGC actors or fake customers (reviews provenance rule).

---

## 4. Placement analysis
### 4a. Account, Nov 1-27 (Meta-reported)
| Placement | Spend | Spend share | Meta purch | Purch share | Meta CPA | ≈ real CPA (×2.05) | Link CTR | CPM | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| FB Feed | 53,411 | 33.9% | 50 | 35.0% | 1,068 | ~2,190 | 2.52% | 334 | High (keep) |
| **FB Reels** | 32,799 | 20.8% | 41 | **28.7%** | **800** | ~1,640 | 2.14% | 345 | High (keep, best) |
| IG Reels | 30,183 | 19.2% | 21 | 14.7% | 1,437 | ~2,950 | 2.12% | 302 | Medium (keep, watch) |
| IG Feed | 24,989 | 15.9% | 24 | 16.8% | 1,041 | ~2,130 | 2.33% | 430 | High (keep) |
| FB In-stream video | 6,217 | 3.9% | 2 | 1.4% | 3,108 | ~6,370 | 1.46% | 249 | Medium (mostly the teaser; cut) |
| IG Stories | 5,947 | 3.8% | 2 | 1.4% | 2,974 | ~6,100 | 3.24% | 544 | Medium-high (cut for 4:5) |
| FB Stories | 1,059 | 0.7% | 1 | 0.7% | 1,059 | — | 4.47% | 667 | Low (cut with IG Stories) |
| WhatsApp Status | 842 | 0.5% | 0 | 0 | — | — | 1.60% | 562 | Medium (all in the last 14 d; cut) |
| FB Search | 713 | 0.5% | 0 | 0 | — | — | 6.33% | 981 | Low (cut, CPM 981) |
| FB Reels overlay | 408 | 0.3% | 0 | 0 | — | — | 1.95% | 169 | Low (cut) |
| Audience Network | 368 | 0.2% | 0 | 0 | — | — | 8.56% (accidental clicks) | 768 | Medium (cut, known click fraud risk) |
| Threads | 199 | 0.1% | 0 | 0 | — | — | 4.00% | 234 | Low (cut) |
| FB Marketplace, IG Explore, others | 443 | 0.3% | 2 | 1.4% | ~220 | — | — | 63-103 | Low (harmless; keep) |
| **Total** | **157,578** | | **143** | | **1,102** | | | | |

**The four core placements = 89.8% of spend, 95.1% of Meta purchases.** Everything else = 10.2% of spend, 4.9% of purchases.

### 4b. Last 14 days, Nov 14-27 (second cut)
| Placement | Spend | Share | Meta purch | Share | Meta CPA |
|---|---|---|---|---|---|
| FB Feed | 25,767 | 34.5% | 22 | 34.4% | 1,171 |
| FB Reels | 16,933 | 22.7% | 19 | 29.7% | **891** |
| IG Reels | 14,530 | 19.5% | 12 | 18.8% | 1,211 |
| IG Feed | 11,402 | 15.3% | 9 | 14.1% | 1,267 |
| IG + FB Stories | 3,444 | 4.6% | 0 | 0 | — |
| WhatsApp Status | 841 | 1.1% | 0 | 0 | — |
| In-stream, Search, AN, Threads, overlay, other | 1,774 | 2.4% | 2 (marketplace/explore) | 3.1% | — |
| **Total** | **74,691** | | **64** | | **1,167** |
The tail outside core + marketplace/explore: **Rs 6.1k (8%) for 0 purchases**. Stories: 0 purchases on Rs 3.4k (in Nov 1-27 overall, 3 purchases on Rs 7.0k).

### 4c. Per ad, where each winner sells (Meta-reported, Nov 1-27)
| Ad | FB Feed | FB Reels | IG Feed | IG Reels | Stories |
|---|---|---|---|---|---|
| H1 Mocha (video) | 14% spend / 15% purch, CPA 1,001 | **44% / 63%, CPA 757** | 7% / 10%, CPA 784 | 27% / **10%, CPA 2,786** | 4% / 0 |
| Retarget old (catalogue) | 46% / 48%, CPA 611 | 16% / 24%, CPA 449 | 18% / 10%, CPA 1,114 | 13% / 10%, CPA 789 | 4% / 5%, CPA 504 |
| Clifford hat (static 4:5) | 34% / 18%, CPA 1,376 | 14% / 18%, CPA 571 | 19% / 18%, CPA 760 | 27% / **45%, CPA 437** | 4% / 0 |
| W01 gloves (static) | 52% / 66%, CPA 741 | 6% / 0 | 20% / 8%, CPA 2,317 | 17% / 25%, CPA 668 | 3% / 0 |
| RT-W chai dhaba (static) | 57% / **80%, CPA 420** | 6% / 20% | 18% / 0 | 17% / 0 | — |
| S4 carousel | 17% / 0 | 6% / 16% | **48% / 66%, CPA 724** | 19% / 16% | 7% / 0 |
**Lesson:** the best placement differs by ad (H1 → FB Reels; Clifford → IG Reels; chai dhaba → FB Feed; carousel → IG Feed). **That is why we keep all four core placements and do not pick one platform.** Cutting to "only FB Reels" would have killed the Clifford hat's best placement.

### 4d. Shopify check (H1 only; it carries `utm_term={{placement}}`)
| H1 placement | Spend | Meta purch | Shopify placed / live | Cost per placed | Cost per live | Cancel |
|---|---|---|---|---|---|---|
| FB Reels | 18,173 | 24 | **21 / 14** | **865** | 1,298 | **33%** |
| FB Feed | 6,007 | 6 | 6 / 3 | 1,001 | 2,002 | 50% |
| IG Reels | 11,145 | 4 | 4 / 4 | **2,786** (1.9x ceiling) | 2,786 | 0% |
| IG Feed + Explore | ~3,150 | 4 | 3 / 3 | ~1,050 | ~1,050 | 0% |
| Stories + In-stream | 2,512 | 0 | 1 ("Others") / 1 | ~2,500 | — | — |
**Meta and Shopify agree closely on H1** (FB Reels 63% of Meta purchases vs 60% of Shopify orders). That gives us more confidence in the account-level Meta placement split. It also shows two risks: **IG Reels is weak for H1** and **FB Reels orders cancel more**. Only H1/H3/the teaser carry `{{placement}}`. **Every other placement number in this file is Meta-reported only (×~2 discount).**

### 4e. Device (Nov 1-27, Meta)
Android 85,937 (55%) → 81 purchases (57%), CPA 1,061, avg value 3,870 · iPhone 69,316 (44%) → 59 (41%), CPA 1,175, avg value 4,550 · desktop/iPad 2,114 → 3 (two big orders, 25k and 36k). **No device cut.** Both phone platforms are profitable at about the same rate, and iPhone buys bigger baskets.

### 4f. THE PLACEMENT RULE from Dec 1 (L3: needs the Founder's yes)
**Keep:** FB Feed, FB Reels, IG Feed, IG Reels (+ FB Marketplace and IG Explore, which come free in those groups and are harmless).
**Cut:** Audience Network, WhatsApp Status, Threads, FB Search, FB In-stream video, FB Reels overlay, right column, notifications/profile feed, and **IG + FB Stories while our creatives are 4:5** (Founder rule: no 9:16). A 4:5 image in Stories shows letter-boxed, which explains the 0 purchases in 14 days.
**Where (ad-set level; Meta has no account-wide placement switch):**
| Ad set | Placement change | When | Why |
|---|---|---|---|
| TOF Prospecting `120256055941820428` (no live ad today) | manual: 4 core | Dec 1, with the 2 new ads | no learning to lose |
| New TEST ad set | manual: 4 core | at creation | clean test |
| Winter Hats (ex BF HATS) `120256204345990428` | manual: 4 core | **in the same Dec 1 edit** as budget/end date/ad swap (one change in 72 h) | it gets a learning reset that day anyway; Stories gave it 0 of 11 |
| **H1 Mocha, Retarget v2, RT-W** | **NO CHANGE** | — | proven; Founder rule "leave good campaigns"; a placement edit resets learning; breakdown effect |
**Minimum evidence before any further cut (e.g. IG Reels on H1):** the placement has spent **≥2x the product's ceiling inside that ad set**, its Meta CPA is **≥2x the ad set's average** in **two consecutive 14-day windows**, and **Shopify** (utm_term) confirms it where available. IG Reels on H1 meets this in window 1 only (11.1k spend, Shopify 2,786 per placed). Re-check at the **Dec 14** read. Even then, prefer leaving H1 alone and putting the next Mocha creative in a 4-core ad set without IG Reels as a test, over editing the winner.
**Risks:** (1) **Breakdown effect.** Meta optimises marginal cost, so cheap Stories/AN impressions may assist sales credited elsewhere. The amount at stake is small (~8-10% of spend), which caps the downside. (2) **Narrower inventory can raise CPM.** The kept placements average CPM ~349 vs ~362 for the account, so the expected effect is neutral or slightly better. (3) **Learning reset** on the hats set, accepted because it is reset anyway on Dec 1. (4) We would lose the chance to find a Stories winner. If we ever make true 9:16 creatives, test Stories again in the TEST slot.
**Expected effect:** about Rs 400-500/day moves from ~0-purchase inventory to placements converting at ~1,100 Meta CPA. That is ≈ +0.4 Meta purchases/day, ≈ +0.2 real orders/day, about 6 orders in December. Small but free.

**Tracking fix (L1, no spend):** every NEW ad from Dec 1 carries `utm_source=facebook&utm_medium=paid&utm_campaign={tier}_202612&utm_content={ad name}&utm_term={{placement}}`. Don't re-tag the proven ads (their history depends on the current tags). From the first Monday read onward, placement claims can then be Shopify-confirmed for every new ad.

---

## 5. December creative production plan
**Why 3 a week:** cold spend is 3,000/day (≈21k/week). H1 shows fatigue after ~5 weeks, and the hats/gloves audiences are small (fatigue in 2-3 weeks). Each week needs **1 TEST challenger + 1 refresh/backup for a live winner + 1 next-week asset**. Total **12 new creatives in December** (5 already in the Dec plan + 7 new here).

### Priority list (higher probability first)
| # | utm_content | Format | Angle | Product | Replaces / role | Maker | Spec | P(winner)* | Due |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `warm_clifford_static_status_studio_v2` | static | status + real full price, no sale words | Clifford hat | **replaces bf_clifford** (sale copy) | Founder GPT image (from the real product photo) + Claude copy | 1080×1350 4:5 | 45% | Nov 30 (in Dec plan) |
| 2 | `tof_mocha_video_comparison_studio_v2` | **video 15 s re-cut of H1** | same comparison, faster | Mocha | **H1 successor, held** until H1 7-d Shopify CPA > 1.3x ceiling (1,900) or CTR −30%, AND Mocha restocked | Claude edits the original H1 file (Founder sends it) | 4:5, 15 s, hook 0-3 s unchanged | 45% | build Dec 3, hold |
| 3 | `tof_executive_static_value_studio_v1` | static | value (price per year of use, honest numbers) | Executive belt | TOF Prospecting ad 2 (Dec plan) | Founder GPT | 4:5 | 30% | Nov 30 |
| 4 | `tof_gloves_lifestyle_problem_lifestyle_v1` | static | chai dhaba scene, cold version | Gloves | TOF Prospecting ad 1 (Dec plan) | reuse the existing chai dhaba image, new cold copy | 4:5 | 30% | Nov 30 |
| 5 | `test_gloves_video_proof_real_v1` | **video 10-12 s** | desk demo: hand slides in, flex, wrist strap closes, "Rs 1,950 · COD" | Gloves | TEST week 2 | Founder phone clip → Claude edit | 4:5, 12 s | 30% | clip by Dec 6 |
| 6 | `test_gloves_faq_trust_textled_v1` | static | FAQ: real leather? COD? sizes? returns? | Gloves | TEST week 1 | Founder GPT + Claude text | 4:5 | 20% | Nov 30 |
| 7 | `test_gift_static_gift_studio_v1` | static | gift under Rs 5,500, real full prices | gloves + cap / belt + wallet | TEST week 4 | Founder GPT | 4:5 | 30% | Dec 18 |
| 8 | `test_wallet_patina_proof_real_v1` | **video 10 s** (or static) | the Founder's own used wallet beside a new one, on the desk (H1's hook, filmed for real) | Mocha / Bastion | TEST week 3 fallback (if jackets not ready) | Founder clip → Claude edit | 4:5, 10 s | 35% | clip by Dec 6 |
| 9 | `warm_clifford_motion_status_studio_v3` | **AI motion 6-8 s** from the v2 static | same as #1, slow push-in + light sweep | Clifford hat | **hat refresh** when v2 freq > 6 or CTR −30% | Claude (free, from the static) | 4:5, 8 s | 30% | Dec 10, hold |
| 10 | `rtw_gloves_chaidhaba_warm_lifestyle_v3` | static | same scene, new frame (evening, two cups) | Gloves | **RT-W refresh** when freq > 6 / CTR −30% | Founder GPT | 4:5 | 30% | Dec 10, hold |
| 11 | `tof_mocha_static_comparison_studio_v1` | static | H1's first frame as a still (new vs 6-month) + 3 bullets | Mocha | H1 backup / test vs video | Founder GPT, or a still from the H1 file | 4:5 | 35% | Dec 3, hold |
| 12 | `bof_jacket_static_trust_studio_v1` | static | made to order, about 3 weeks, paid online because each is cut for one customer; top-grain sheepskin | Jacket | TEST week 3 **only if** checkout ≥25% for 7 d | Founder GPT | 4:5 | 20% | Dec 14 |
*P(winner) = Alex's estimate that the ad reaches ≥2 Shopify orders at ≤ ceiling. Based on our hit rate: ~4 winners out of ~25 November ads (≈16%). Proven hooks on proven products score higher.

**Who makes what:**
- Founder: 7 GPT statics, made from **one self-contained prompt per image** (full spec inside each prompt, per CLAUDE.md). Claude delivers the prompt pack as a PDF, one prompt per page, by **Nov 29**. Plus 3 desk clips by **Dec 6**: gloves fit/flex, own-wallet patina, Mocha "what fits + button pocket". Each is 20-30 s raw, phone vertical or 4:5, daylight from a window, plain desk, no faces needed.
- Claude: 3 video edits (H1 15 s re-cut, gloves demo, patina), 1 AI-motion cut, all on-screen text/end cards, copy for every ad, and a CQRO rule check before anything goes live (coins, Karachi, workshop, full-grain on jackets, fake urgency, unprovable claims).

**Copy rules for all 12:** honest full prices after Dec 1 (no "sale continues"). "Handcrafted in Pakistan". COD line on in-stock items only. No coins, no croc/exotic words, no "only X left". No free-delivery badge on items under 5,500.

---

## 6. Dated action list (Dec 1-31)
| Date | Action | Owner | Level | Metric / rule |
|---|---|---|---|---|
| Nov 28-29 | Prompt pack PDF (7 statics) + video shot list for the Founder; verify `bf_clifford` wording | Claude | L1 | — |
| Nov 30 | Founder makes #1, #3, #4, #6. Claude builds them as PAUSED drafts with the 4-core placements + `{{placement}}` tags; CQRO check | Founder + Claude | L2 | creatives clean |
| **Dec 1 ~00:10 PKT** | Dec plan go-live (hats 700 with v2 ad + 4-core placements; Prospecting 640 with #3 + #4 on 4-core; TEST 500 with #6 on 4-core). Read back budgets (= 5,000) | Claude after the Founder's yes | **L3** | totals = 5,000 |
| Dec 1-3 | BF read into the playbook (per-ad Shopify, placement split, the S4 correction above) | Claude | L0 | — |
| Dec 3 | Build #2 (H1 15 s re-cut) and #11 (H1 still), **held** | Claude (needs the H1 file) | L1 | — |
| Dec 4 | 72 h check, report only. Retarget v2 judged at ≥3,000 spend | Claude | L0 | v2 ≤ 1,500 per placed |
| Dec 6 | Founder's 3 desk clips in → Claude edits #5 + #8 | Founder → Claude | L1 | — |
| **Dec 7 (Mon)** | Weekly read: per-ad table, placement (now Shopify-confirmed on new ads), H1 fatigue check, Mocha stock. Week-2 test #5 goes live (L3) | Claude → Founder | L3 | kill: cold CTR < 0.6% after 3,000 impr; ≥1.5x ceiling with 0 orders; scale +20% at ≤0.7x ceiling with ≥3 orders |
| Dec 10 | Build refreshes #9 + #10, held. Jacket checkout condition starts | Claude | L1 | — |
| **Dec 14 (Mon)** | Weekly read + **second 14-day placement window**: decide on IG Reels for Mocha (rule 4f) and on Stories, only if the evidence repeats. Week-3 test (#12 or #8) | Claude → Founder | L3 | the 4f evidence threshold |
| Dec 18 | #7 gift static made | Founder | L2 | — |
| **Dec 21 (Mon)** | Weekly read. Week-4 test #7. Swap in the hat/gloves refresh if their trigger is hit (freq > 6 warm AND CTR −30% vs week 1) | Claude → Founder | L3 | refresh rule |
| Any day | H1 successor #2 goes live **only if** H1 7-d Shopify CPA > 1,900 (1.3x) or CTR −30%, AND Mocha is in stock. Same ad set? No: TOF Prospecting, so H1 keeps its learning | Founder yes | L3 | — |
| Any day | Pause an ad at the stock guard (Mocha ≤3 sellable without a dated restock; hats ≤3 per best size) | Founder yes | L3 | stock |
| **Dec 28 (Mon)** | Weekly read + December scorecard → CREATIVE_PLAYBOOK (proven/lost) + January tests | Claude | L0 → L3 | — |
| Dec 31 | Hats season end check; move its 700 to Prospecting only if a Prospecting ad has ≥2 Shopify orders under its ceiling | Founder yes | L3 | — |

---

## 7. What we are NOT doing (and why)
- **Not going video-only or image-only.** Neither format wins on our numbers; the hook and the product do.
- **Not making long videos** (30-70 s), founder talking heads (H3 lost) or awareness/ThruPlay teasers (Rs 5.2k, 0 sales).
- **Not editing H1, Retarget v2 or RT-W** (placements, copy, budget). Proven, Founder rule, learning reset.
- **Not cutting a platform** (FB vs IG): each winner has a different best placement (4c).
- **Not cutting IG Reels yet** for H1: one window only; it is Clifford's best placement.
- **Not making 9:16 creatives** (Founder rule Nov 10; S3 9:16 lost). This is the reason we drop Stories for now.
- **Not using Advantage+ Shopping/Autopilot** (no refuser exclusion, all Pakistan; 2,580 per placed, 50% cancel).
- **Not running bag ads at full price, or jackets before the checkout fix** (Dec plan, decisions 3 and 5).
- **Not using paid AI video tools** (HARD RULE: free only); AI motion is made by Claude from stills.
- **Not relaunching any old creative with banned wording** (workshop, Karachi, full-grain, coins, cigarette/tobacco).
- **Not judging any placement or ad on Meta's count alone.**

## 8. Not verified
- Placement results for every ad except H1/H3/teaser are **Meta-reported only** (url_tags lack `{{placement}}`). Apply the ~2x discount.
- Final COD refusal per ad: orders from ~Nov 20 are still PENDING. The cancel % above is "so far".
- 122 orders (Rs 750k live) had no utm; some are Meta-influenced (view-through, IG link-in-bio). Shopify attribution here is last-visit only.
- Untagged hat orders (e.g. #23182, #23146) are probably from `bf_clifford` but are not counted.
- H1 video aspect ratio and the availability of the original source file for a re-cut.
- "Over 4,000 wallets sold since 2021" (H1 copy): needs a Shopify count before it is reused in any new creative.
- Mocha restock date; hat/glove stock per size on Dec 1; the full-price hat ceiling (CFO, by Dec 2).
- P(winner) numbers are judgement, not statistics. Most per-placement purchase counts are small (< 25), so treat CPA differences under ~30% as noise.
