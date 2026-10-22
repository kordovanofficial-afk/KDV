"""Transcribe a clip with word timings. Usage: transcribe.py <media> <out.json> [lang]"""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
lang = sys.argv[3] if len(sys.argv) > 3 else None
pcm = subprocess.run(["ffmpeg", "-nostdin", "-i", src, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
m = WhisperModel("large-v3", device="cpu", compute_type="int8", download_root=__import__("os").environ.get("WHISPER_MODELS", "models"))
segs, info = m.transcribe(audio, word_timestamps=True, language=lang, vad_filter=True,
    initial_prompt="Kordovan, Mocha Mate wallet, CNIC window, leather, Karachi.")
words = [[w.start, w.end, w.word.strip(), w.probability] for s in segs for w in s.words]
json.dump({"language": info.language, "words": words}, open(out, "w"), ensure_ascii=False, indent=0)
print(info.language, len(words), "words")
for w in words: print(f"{w[0]:6.2f}-{w[1]:6.2f} {w[3]:.2f} {w[2]}")
