# Mocha Mate — Founder Video Script v2 (shoot Oct 22 2026)

v1 (the coin angle) is DEAD. User: coins are barely used in Pakistan any more. The founder has
carried a Mocha Mate daily for ~6 months and uses the back button pocket for keys and the
small things worth keeping safe. v2 is built on that real use.

Verified live Oct 21 2026: Rs 3,200 · 44 in stock · genuine cow leather · outer button pocket ·
ID window (a CNIC is standard card size) · 5–6 card slots + cash pocket · lifetime craftsmanship
warranty · 153 sold (net) in 12 months · COD available (not made to order). Delivery is not free
at this price (the threshold is Rs 5,500), so nothing promises it.

**Concept: "6 months in my pocket."** An honest founder review of their own wallet. Three ideas
carry it: the hidden pocket, the CNIC window, and the 6-month patina next to a new wallet.
Lines avoid gendered Urdu verbs so they work for any speaker.

## 3 hooks (film all three; the body is the same; Meta tests which one holds attention)
- **A · Patina:** worn wallet in hand → "Chhe mahine se yeh wallet roz meri jeb mein hai. Dekhiye ab kya haal hai." | Caption: 6 months. Every single day.
- **B · Hidden pocket:** open the back button → "Har wallet mein ek chupi jeb honi chahiye. Meri wali mein yeh rehta hai." (pull out the spare key) | Caption: Every wallet needs a secret pocket.
- **C · Founder honesty:** to camera → "Apne hi brand ka wallet chhe mahine istemal kiya. Ab imaandari se batata/batati hoon kaisa nikla." | Caption: I tested my own wallet for 6 months.
  (C is the one line that can't avoid a gendered verb. Pick the form that fits you.)

## Body (~45s, after any hook)
| # | Shot | Say | Caption |
|---|---|---|---|
| 1 | Founder to camera | "Main [naam], Kordovan ka founder. Yeh hai Mocha Mate — aur yeh meri apni hai, display wali nahi." | [Name] · Founder, Kordovan |
| 2 | Flip it; snap the button close to the mic; take out what's REALLY in there | "Peeche button wali jeb. Meri mein ghar ki spare chaabi rehti hai, aur ek emergency note — jo tab yaad aata hai jab sach mein zaroorat ho." | The pocket for things you can't lose |
| 3 | Slide the CNIC out of the window, then back | "CNIC is window mein. Naaka ho, bank ho — bas dikhao, nikalne ki zaroorat nahi." | CNIC window — show, don't dig |
| 4 | Cards in, notes in, close it, into a back pocket | "Andar chhe cards tak, notes ki poori jagah — aur phir bhi jeb mein bhaari nahi lagta." | Up to 6 cards · cash pocket |
| 5 | **The money shot:** new wallet beside the 6-month one, then a slow tilt of the worn one in window light | "Yeh naya hai. Yeh chhe mahine purana. Asli leather ghis-ta nahi — rang pakadta hai." | New vs 6 months. Real leather ages. |
| 6 | Thumb along the stitching | "Silai abhi tak waisi hai. Aur waise bhi — har silai par lifetime warranty hai." | Lifetime craftsmanship warranty |
| 7 | To camera | "Pichle saal ek sau pachaas se zyada logon ne yeh wallet liya." | 150+ sold this year |
| 8 | To camera, holding it | "Teen hazaar do sau. Online pay karein ya cash on delivery — link neeche." | Rs 3,200 · kordovanleather.com |
| 9 | (organic version only) | "Aur batayein — aap ke wallet ki chupi jeb mein kya hai? Comment mein likhein." | What's in YOUR secret pocket? 👇 |

Cuts from the same footage: **master ~50s** (hook + 1–8) · **30s** (hook + 2, 3, 5, 8) ·
**15s** (hook + 5 + 8) · **organic Reel** = master + line 9 (the comment question drives reach).
Each length gets all 3 hooks → 9 ad variants from one shoot.

## B-roll (no talking, 5–10s each)
1. Button pocket snapping open and shut, macro — the signature shot
2. Spare key / note coming out of the back pocket
3. CNIC sliding out of the window and back
4. **New and 6-month wallets side by side**, top-down, then a slow push-in
5. The worn wallet tilted in window light (the patina catching the light)
6. Into and out of a back jeans pocket
7. Everyday moments: on the car dashboard, on a café table next to chai, into a pocket at the door
8. Optional: workshop / hands stitching

## Honesty rules for the shoot
- Only pull out what you **actually** keep in there. Real items read as real; staged ones don't.
- The worn wallet must be **your real 6-month wallet**. Don't age a new one to fake it.
- Don't say "best-seller" or quote numbers beyond the 150+ above.

## Filming
- Vertical, 30fps; tap and hold to lock focus and exposure. Window light from the side, never behind you.
- Plain wall or wooden desk, plain dark shirt. Look into the lens. Phone at eye level.
- Quiet room, fan off, phone close or a wired-earphone mic. Record 10s of silence at the end.
- Read a line, look up, say it. 2–3 takes per line with a 2s pause before and after. Send raw files.

## When it runs as an ad
New ad set (TOF-A retest, 9 cities, refusers excluded), 3 hooks as separate ads. Write the kill
threshold in rupees BEFORE launch. Read on day 3 and day 5; scale the winning hook, drop the others.

## Edit pipeline: what this environment can and can't do (checked Oct 21 2026)
- ✅ ffmpeg 6.1 installed (cuts, `loudnorm`, `afftdn`/`arnndn` denoise, `ass` animated captions,
  `lut3d` grading, `zoompan` punch-ins). npm and PyPI are reachable (Remotion for motion graphics,
  `faster-whisper` installable). Google Fonts reachable (Fraunces + Inter for captions).
- 🔴 **huggingface.co is BLOCKED**, so Whisper models can't download and there's no automatic transcription.
  Fix: add `huggingface.co` to the environment's allowed domains. Fallback: align the script
  text to the speech gaps (works when the founder sticks to the scripted lines).
- 🔴 Claude can't HEAR audio. It works from waveforms, silence detection and sampled frames,
  so the founder should review the draft and correct any take choice.
- 🔴 Google Drive (the MCP auth fails; the hosts get a 403), Dropbox and WeTransfer are all blocked.
  Transfer route = attach the files in the Claude chat; fallback = GitHub web upload (25MB per
  file) to the session branch, NEVER to `kordovan`.
- Film **1080p 30fps, one clip per line** → ~10–20MB per clip, small enough for either route.

## Raw clip retention rule (user, Oct 23 2026)
Raw clips live in `mocha-mate/` on the session branch. **Do NOT delete any raw clip until the user
has signed off on the FINAL versions of every cut** (all edits, enhancements and re-cuts done).
Deletion happens only on their explicit go-ahead. Until then, never merge this branch into `kordovan`
with the clips in it.

## Scene map (built Oct 24 2026 from Whisper transcripts of the 34 clips in `mocha-mate/`)
⚠️ The clips in `mocha-mate/` are HandBrake copies (encoder tag `HandBrake 1.11.2`, 1080×1080 with SAR 9:16 =
vertical, but only ~608px of real width, ~0.75 Mbps). The user's true iPhone originals are being pushed in
batches to `mocha-mate/originals/`. **Sort on the copies, render from the originals.**
⚠️ ffprobe reports these as 1080×1080. ALWAYS read `sample_aspect_ratio` before calling a clip square
(that mistake was made once). Strip metadata on export (`-map_metadata -1`): the clips carry the GPS location.

| Scene | Clips (take) | Pick | Why |
|---|---|---|---|
| H1 New vs 6 months | 1479 (false start) · 1480 (cut short) · 1481 t1 · 1482 t2 · 1483 t3 | **1483** (alt 1481) | complete line; t2 has a slip ("meri jebna") |
| H2 Secret pocket | 1484 t1 · 1485 t2 · 1486 t3 · 1487 t4 · 1488 t5 | **1485** (alt 1487) | cleanest complete line, keys named |
| H3 Honest review | 1489 t1 (slate misheard as S3) · 1490 t2 | **1490** (alt 1489) | complete honest-review line |
| S1 Who I am | 1491 t1 · 1492 t2 | **1492** | name + "co-founder of Kordovan Leather" clearly said |
| S2 Pocket demo | 1493 t1 · 1494 t2 | **1494** | tighter: "spare keys aur change" |
| S3 CNIC | 1495 t1 · 1496 t2 · 1497 t3 · 1500 t4 | **1497** (alt 1495) | short; 1495 is longer, names checkposts + banks |
| S4 Inside | 1501 t1 · 1502 t2 (cut) · 1503 t3 | **1503** | cards + cash + "never feels bulky" |
| S5 Patina | 1504 only | **1504** | |
| S6 Stitching | 1505 only | **1505** | |
| S7 Proof | 1506 (false start) · 1507 t2 · 1508 t3 · 1509 (slate only) · 1510 t4 | **1508** + caption "4,000+ wallets sold since 2021" | see claim check |
| S8 Offer | 1511 t1 · 1512 t2/3 | **1512** | complete, ends on "link neeche" |
| S9 Comment ask | not shot | on-screen text instead | organic version only |
| B-roll | 1498, 1499 (short, near-silent) + macro shots inside H2/S2 takes | cutaways | dedicated B-roll mostly not shot |

**Claim checks (Shopify, Oct 24 2026):** wallets sold online since 2021 = **4,134** (150 · 271 · 608 · 785 ·
1,421 · 899) → "thousands of wallets in 5 years" is TRUE. Mocha Mate alone = **523** since launch in 2023
→ "thousands of THESE wallets" (take 1510) is FALSE. Do not use 1510.
S4 says "6 to 12 cards"; the PDP says 5–6 card slots → user to confirm before captioning a number.
