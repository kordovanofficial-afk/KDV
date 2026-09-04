# SHOTS — "We haven't made it yet"

**27.0 seconds · 7 scenes · 9:16 · 0 FILM / 7 GENERATE**

Stills at **832×1216**. Deliver at **1080×1920**. Feed LTX/Wan at **704×1280** — both
divisible by 32, which LTX requires. Clips land in `raw/` as `shot01.mp4` … `shot07.mp4`.

Durations must match `captions.srt` and the `DURS` array in `assemble.sh`. Change one,
change all three or the captions drift off their pictures.

Starting-image prompts are in `prompts/` — regenerate them with `./build-prompts.sh`
after editing any locked block.

---

## Scene 01 — the empty bench · `00.0 → 04.0` · 4.0s

- **Starts.** Locked on the empty bench. Rolled hide, folded pattern, chalk, shears. A shaft of hard sun crosses frame with dust suspended in it. Nothing is being touched.
- **Happens.** Almost nothing, and that is the point. Dust drifts slowly through the light. No hands enter; nothing on the bench moves.
- **Camera.** Extremely slow push in — no more than 5% over four seconds. The frame should feel like it is breathing, not moving.
- **Ends.** Same composition, fractionally closer. The bench is still empty.
- **Voiceover.** "This? This is your jacket." *(one full beat)* "No, no. We have not made it yet." Under it: faint room tone, distant ceiling fan.
- **Caption.** "This is your jacket." → "We haven't made it yet."

> **NO MUSIC OF ANY KIND. Voiceover and natural room sound only.**

---

## Scene 02 — the chalk line · `04.0 → 08.0` · 4.0s

- **Starts.** Overhead on the hide with the paper pattern laid across it. The craftsman's hand enters from the right holding white chalk.
- **Happens.** One long, continuous, confident chalk line along the pattern edge, right to left. Unbroken — no hesitation, no correction. The hand withdraws.
- **Camera.** Completely locked off. The only motion in frame is the hand.
- **Ends.** Hand out of frame. The white line sits clean against the brown hide.
- **Voiceover.** "One hide. Cut to your measurement — not small, medium, large." Under it: the dry scrape of chalk on leather.
- **Caption.** "Cut to your measurements."

> **NO MUSIC OF ANY KIND. Voiceover and natural sound only.**

---

## Scene 03 — panels laid out · `08.0 → 12.0` · 4.0s

- **Starts.** Directly overhead. Cut panels arranged flat in the shape of a jacket — two fronts, a back, two sleeves.
- **Happens.** A hand enters, straightens one sleeve panel by a couple of centimetres, withdraws. That adjustment is the entire action.
- **Camera.** Very slow rise straight up, as if the ceiling is receding, revealing how clearly the layout reads as a jacket.
- **Ends.** Wider overhead frame, the full jacket shape unmistakable, hands out.
- **Voiceover.** **None.** Room tone only — ceiling fan, faint street noise.
- **Caption.** "Not a size run."

> **NO MUSIC OF ANY KIND. Natural room sound only.**

---

## Scene 04 — the machine · `12.0 → 17.0` · 5.0s

- **Starts.** Low and close beside the machine bed at needle height. Two panels under the presser foot. Needle up and still.
- **Happens.** The machine starts. The needle punches rhythmically, leather feeds steadily through, a line of even stitching grows and runs back toward camera. His hands guide; they do not push.
- **Camera.** Locked off, shallow focus on the needle. Let the leather move through frame rather than moving the camera.
- **Ends.** Machine slows and stops. Needle at rest. A finished seam runs the length of frame.
- **Voiceover.** "Seven days. One man — start to finish. Haath ka kaam." Under it: the real machine.
- **Caption.** "Seven days. One maker."

> **NO MUSIC OF ANY KIND. Voiceover and natural machine sound only.**

---

## Scene 05 — the zip · `17.0 → 20.0` · 3.0s

- **Starts.** Macro on an antique-brass zip half-set into the jacket's front edge, cream quilted lining turned back beneath.
- **Happens.** A thumb presses the zip tape flat and runs slowly down the edge, seating it against the leather.
- **Camera.** Slow lateral slide following the thumb, holding the same distance. Shallow focus.
- **Ends.** Thumb reaches the bottom and lifts away. Zip fully seated.
- **Voiceover.** **None.** Leather under a thumb and the faint metallic tick of the zip.
- **Caption.** None — let the shot breathe.

> **NO MUSIC OF ANY KIND. Natural sound only.**

---

## Scene 06 — finished, on the hanger · `20.0 → 23.0` · 3.0s

- **Starts.** The finished jacket on a broad wooden hanger, still, sun shaft catching one shoulder.
- **Happens.** It settles — one sleeve swings once, very slightly, as though just hung. Dust drifts across the chest.
- **Camera.** Slow push in toward the shoulder seam, ending close enough that the grain is clearly readable.
- **Ends.** Tight on shoulder and collar, grain and stitching sharp, jacket motionless.
- **Voiceover.** "Bas. Now it is yours." Then silence for the rest of the shot.
- **Caption.** "Genuine full-grain sheepskin."

> **NO MUSIC OF ANY KIND. Voiceover and natural room sound only.**

---

## Scene 07 — worn, leaving · `23.0 → 27.0` · 4.0s

- **Starts.** Behind the man, framed from the collarbone down, wearing the finished jacket. A bright open doorway ahead.
- **Happens.** Two unhurried steps toward the doorway. The daylight grows and begins to blow out, rim-lighting his shoulders through the dust.
- **Camera.** Locked off. He walks away from the frame rather than the camera following — the workshop stays, he leaves.
- **Ends.** Smaller in frame, edge-lit against the doorway, light almost white. Hold one beat on the workshop as he clears frame.
- **Voiceover.** "Made in Karachi. Half to begin, half at your door."
- **Caption.** "Made to order in Karachi" → "From Rs 22,000 · Book with 50%, balance to the rider"

> **NO MUSIC OF ANY KIND. Voiceover and natural room sound only.**
>
> ⚠️ **This scene deliberately drops the environment block.** The doorway flare replaces
> the window as the light source, because this shot is the exit. Palette and grade stay
> identical so it still cuts against the other six.

---

## Timing table

| # | In | Out | Dur | VO | Caption |
|---|---|---|---|---|---|
| 01 | 00.0 | 04.0 | 4.0 | yes | yes |
| 02 | 04.0 | 08.0 | 4.0 | yes | yes |
| 03 | 08.0 | 12.0 | 4.0 | — | yes |
| 04 | 12.0 | 17.0 | 5.0 | yes | yes |
| 05 | 17.0 | 20.0 | 3.0 | — | — |
| 06 | 20.0 | 23.0 | 3.0 | yes | yes |
| 07 | 23.0 | 27.0 | 4.0 | yes | yes |
| | | **Total** | **27.0s** | 4 lines | 8 cues |

## Re-roll guidance

Re-roll the seed rather than rewriting the prompt when you see:

- **A face creeping in** at the top edge of scenes 2, 4, 5 or 7. The crop is the whole
  identity strategy — a face that changes between cuts reads as fake instantly.
- **Skin drifting pale.** Models default hard to European subjects. Re-roll; do not
  stack more adjectives.
- **The cognac shifting** darker or redder between scenes. Do not fix with colour
  words — that moves the whole grade. Scene 2 is the reference.
- **Wrong finger counts** in 2, 4 and 5 — the three shots with hands. If two re-rolls
  do not fix it, tighten framing until only the cuff and the working edge are in shot.
