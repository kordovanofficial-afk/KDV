"""Transcribe a Founder voice note (free, local). Usage: python3 tools/voice/transcribe.py <audio file> [en|ur]
Needs: pip install faster-whisper (once per session) + ffmpeg. Decodes with ffmpeg because the bundled PyAV breaks."""
import subprocess, sys, numpy as np
from faster_whisper import WhisperModel
path = sys.argv[1]; lang = sys.argv[2] if len(sys.argv) > 2 else None
raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(raw, np.float32)
model = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = model.transcribe(audio, language=lang)
print(f"[language {info.language}, {info.duration:.0f}s]")
print(" ".join(s.text.strip() for s in segs))
