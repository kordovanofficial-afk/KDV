# Storyboard-generation prompt — cinematic jacket film, no narration

Paste **everything inside the box** into ChatGPT or Gemini. It is self-contained: it
carries the brand facts, the locked visual language and the output format, so the model
does not have to guess and cannot invent claims we would have to retract.

Output is a shot-by-shot board you can hand straight to a video model.

---

```
You are a director and DOP building a shot-by-shot storyboard for a 27-second vertical
film. Work only from the brief below. Do not invent facts, prices, claims or products
that are not in it.

═══════════════════════════════════════════════════════════════════════
THE BRAND
═══════════════════════════════════════════════════════════════════════
Kordovan — a full-grain leather workshop in Malir Cantt, Karachi, Pakistan, est. 2020.
Small family operation, not a factory. The house voice is "Quiet Heritage": understated,
confident, never loud, never discount-flavoured. No hype, no exclamation marks, no
urgency, no emoji.

THE PRODUCT IN THIS FILM
A men's full-grain sheepskin leather jacket, cognac brown, biker cut. From Rs 22,000.

FACTS YOU MAY USE — these are true and verified. Use nothing else.
- Made to order. Every jacket is cut for one named customer, to that person's
  measurements. There is no size run and no stock.
- 4 to 7 working days to make, then 3 to 4 days to deliver.
- One maker takes a jacket from cutting to finishing. It does not pass down a line.
- Paid online at checkout — card, debit card or JazzCash.
- Lifetime craftsmanship warranty.

FACTS YOU MUST NOT USE — these are false or forbidden:
- Do NOT mention cash on delivery. Jackets cannot be bought with COD.
- Do NOT say "delivery anywhere in the country" or "nationwide" — delivery is reliable
  in nine cities only.
- Do NOT mention any discount, sale, percentage off or promo code.
- Do NOT say "book with 50%", "deposit", or "pay the balance to the rider". That was an
  old policy and it is dead.
- Do NOT invent customer reviews, ratings, star counts or testimonials.

═══════════════════════════════════════════════════════════════════════
THE JOB THIS FILM HAS TO DO
═══════════════════════════════════════════════════════════════════════
One argument, made in pictures: THIS JACKET DOES NOT EXIST YET, AND THAT IS THE POINT.

Asking a Pakistani buyer to pay Rs 22,000+ online, in full, before anything is made, in a
market where almost everything is cash on delivery, is the hardest thing this brand asks
for. Nobody believes a claim about it. But someone who has just watched a jacket cut from
a flat hide, for one person, stops needing the claim — the payment terms become obvious
instead of suspicious.

So the film must show a TRANSFORMATION: nothing → hide → cut panels → stitched → finished
→ worn. That shape also happens to be the most watchable structure in short-form, because
people stay to see the thing completed.

The viewer should finish it thinking: "that was made for one person, not bought off a
rack." Not desire. Not urgency. Recognition of care.

═══════════════════════════════════════════════════════════════════════
HARD CONSTRAINTS — breaking any of these makes the film unusable
═══════════════════════════════════════════════════════════════════════
1. NO NARRATION AND NO SPOKEN WORDS. Not one line. Meaning is carried entirely by the
   order of the pictures, the burned-in captions and the sound design.
2. NO MUSIC OF ANY KIND. Diegetic sound only — room tone, a ceiling fan, chalk scraping
   leather, the sewing machine, a zip, leather moving under a thumb, distant street
   noise. Silence is a legitimate choice for a shot and you should use it at least twice.
3. NO FACES, EVER. Frame hands, forearms, torsos, backs, shoulders — always crop above
   the chin or shoot from behind. This is deliberate: a generated face that changes
   between cuts reads as fake instantly and destroys the documentary feel.
4. Any person in frame is PAKISTANI with warm brown skin. State this explicitly in every
   image prompt containing a person — image models default hard to European subjects.
5. Vertical 9:16. Total runtime 25–30 seconds. Six to eight shots. No shot under 2.5
   seconds or over 5 seconds.
6. ONE action per shot. These get animated by a video model that cannot handle two.
7. No text, lettering, signage, logos or watermarks inside the generated images.
   Captions are added later in the edit.

═══════════════════════════════════════════════════════════════════════
LOCKED VISUAL LANGUAGE — reuse this wording near-verbatim in every image prompt
═══════════════════════════════════════════════════════════════════════
SETTING: a small family leather workshop in Malir Cantt, Karachi — whitewashed plaster
walls with a pale sage-green painted dado along the lower half, a grey polished-concrete
floor, brown paper jacket patterns hung on nails, rolled hides stacked on open wooden
shelving, an old black cast-iron industrial sewing machine with worn gold lettering, a
grey steel almirah deep in the background, a single clear cutting-chai glass at the edge
of the bench, hard warm Karachi sunlight entering through a high iron-grilled window on
frame left and falling in one clean shaft with fine dust suspended in it, a warm brass
work lamp just out of frame right lifting the shadows, the room ordered and cared-for, a
professional craft studio and not a factory floor.

GRADE: palette built on cognac brown and saddle tan leather against warm alabaster cream,
parchment, walnut and aged antique brass with a single muted sage accent, warm
high-contrast natural light, fine 35mm film grain, soft highlight roll-off, deep espresso
shadows with absolutely no blue or teal in them, tactile close photography that makes the
grain of the leather readable, unstyled editorial documentary look, shot on a full-frame
camera.

THE CRAFTSMAN (when hands are in shot): the hands and forearms of a Pakistani craftsman
in his late thirties, warm brown skin, working hands with short clean nails and visible
callus, no watch and no rings, wearing a plain solid-colour cotton shalwar kameez with
the sleeves rolled to the elbow.

NEGATIVES to append to every image prompt: no text, no graphics, no watermark, no logo,
no lettering, no signage, no clutter, no plastic, no modern office, not a factory
production line, no faces.

═══════════════════════════════════════════════════════════════════════
WHAT TO GIVE ME
═══════════════════════════════════════════════════════════════════════
First, one short paragraph: the through-line of the film in your own words, and why your
shot order builds the argument.

Then, for EACH shot, in this exact structure:

  SHOT [n] — [three-word title] — [in]s to [out]s — [duration]s
  STARTING IMAGE PROMPT: one flowing paragraph, ready to paste into an image generator.
      Must contain: the subject and framing, then the SETTING block, then the GRADE
      block, then the NEGATIVES. Name a focal length (35mm, 50mm or 85mm macro).
  MOTION: the single action that happens, in one sentence.
  CAMERA: locked off, slow push, slow rise, or lateral slide. Say which, and how far.
      Keep it restrained — under 10% movement across the shot.
  SOUND: the exact diegetic sounds, or the word SILENCE.
  CAPTION: the on-screen text, or NONE. Maximum 6 words. Sentence case. No emoji.

Then a timing table: shot number, in, out, duration, caption — with the total.

Then a "watch for" list: the specific ways these shots usually fail in generation and
what to re-roll rather than rewrite.

CAPTION RULES
- Six words maximum. Most shots want three or four. Several shots should have none —
  let the picture breathe.
- Never state a commercial term without its reason in the same breath. "Paid online"
  alone reads as distrust in a cash-on-delivery market. "Paid online — each one is cut
  for one customer" is the same fact and reads as craft. Always pair them.
- The final caption carries the price and the payment line. Nothing before it should.
- Do not caption what the picture already says. If the shot shows chalk on a hide, the
  caption is not "drawing the pattern".
```

---

## After it gives you the board

1. **Generate the stills first**, at 832×1216. Do shot 1 and treat it as the master —
   feed it back as a reference image for the rest if your tool supports it. That locks
   the bench, wall colour and light direction harder than words ever will.
2. **Animate each still** per its MOTION line. Feed LTX or Wan at **704×1280** — both
   divisible by 32, which LTX requires.
3. **Deliver at 1080×1920.**
4. Reuse `../we-havent-made-it-yet/assemble.sh` to trim, concatenate, burn the captions
   and encode to Meta spec — it takes clips from `raw/` as `shot01.mp4` onward. Drop the
   voiceover step; there is no `audio/vo.wav` in this version.

⚠️ **If a generated clip comes back with music, throw its audio away entirely.** Do not
try to mix around it. Own the soundtrack rather than negotiating with a model.
