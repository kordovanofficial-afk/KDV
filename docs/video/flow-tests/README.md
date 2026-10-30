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
