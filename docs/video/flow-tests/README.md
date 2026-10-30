# Flow (Veo) test clips

- `mocha-mate-lightsweep-v2-PASS.mp4`: raw 720p Veo clip from Google Flow, real product photo as start frame.
- `Kordovan_MochaMate_IG_LightSweep_11s_9x16.mp4`: Instagram post. Clip upscaled to 1080x1920, headline
  "Asli leather." (Fraunces, one italic accent), espresso end card with the horse mark, Rs 3,200, COD + lifetime
  warranty, "Link bio mein".
- Audio: "Night Driving" by HoliznaCC0 (CC0, Hugging Face `SoundSafari/Public-Domain-Music`) from 7.37 s, plus
  whoosh-short + click-soft (Pixabay Content License) on the end card. -14 LUFS target.
- ⚠️ libass ignores `fontsdir` for Fraunces here. Copy the fonts to `~/.fonts` and run `fc-cache -f` first, or the
  headline silently falls back to a sans.
- AI-generated footage: switch on Instagram's "AI label" when posting.

## v2 (Oct 30 2026): `Kordovan_MochaMate_IG_LightSweep_v2_11s_9x16.mp4`
- Camera move added in the edit: slow push-in 106% → 118% plus a gentle tilt −1.2° → +1.2°, eased, rendered from a
  2160×3840 upscale to avoid zoompan jitter (frame-diff max 1.49 vs mean 0.69, no spikes).
- Music: Beethoven, Sonata No. 8 "Pathétique", II. Adagio cantabile, played by Daniel Veesey (CC0, Hugging Face
  `SoundSafari/Public-Domain-Music`). Starts at 1.2 s so the first note lands on frame 5. −16 LUFS.
- The tilt is a 2D roll, not a real change of camera angle. A true orbit needs a new Flow generation.
