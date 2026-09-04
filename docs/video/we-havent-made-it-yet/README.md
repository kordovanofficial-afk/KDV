# "We haven't made it yet" — jacket film

27 seconds · 9:16 · seven scenes · September 2026 cold campaign.

## Why this film

The leather-test angle is a *category* argument — any of the ten brands in our
comparison article could run it. **Made-to-order is the one thing only we do**, and
it answers all three of the measured problems in a single idea:

- **Why Rs 22,000** — you watch where the money goes; no claim needed.
- **Why 4–7 days** — you watch why, so the wait stops being an annoyance.
- **Why 50% up front** — the important one. 58% of jacket orders die at the deposit.
  After watching a jacket cut from nothing, "half to start" reads as reasonable
  rather than suspicious.

Transformation is also the most reliably watchable shape in short-form: people stay
to see the thing finished. It works muted, needs no actor and no lighting kit, and
the footage is evergreen — the same clips feed Reels, the PDP and the Our Craft page.

## Files

| | |
|---|---|
| `build-prompts.sh` | assembles the seven image prompts from the locked blocks → `prompts/` |
| `prompts/scene1–7.txt` | paste-ready starting-image prompts, 832×1216 |
| `SHOTS.md` | motion direction, camera, voiceover and caption per scene |
| `VOICEOVER.md` | voice brief and full script |
| `captions.srt` | burned-in captions, timed to the shot durations |
| `assemble.sh` | trims, concatenates, burns captions, lays the voiceover, encodes to Meta spec |
| `COPY.md` | ad copy for the Meta placement |

## Running it

1. Generate the seven stills at **832×1216** from `prompts/`. Do Scene 1 first and
   treat it as the master — feed it back as a reference image for 2–6 if your tool
   supports it. That locks bench, wall colour and light direction harder than words can.
2. Animate each still per `SHOTS.md`. One action per clip. Feed LTX/Wan at **704×1280**
   (both divisible by 32, which LTX requires).
3. Drop the clips in `raw/` as `shot01.mp4` … `shot07.mp4`.
4. Record the voiceover (see `VOICEOVER.md`) and save it as `audio/vo.wav`.
5. `./assemble.sh` → `jacket_film_v1.mp4` at 1080×1920.

## Two rules that matter more than they look

- **Skin tone drifts white unless held.** Image models default hard to European
  subjects, which is why "Pakistani… warm brown skin" is in every prompt with a
  person. Re-roll rather than piling on adjectives.
- **Generated audio is disposable.** If a clip returns with music, `assemble.sh`
  discards its audio entirely. Own the soundtrack rather than negotiating with a model.
