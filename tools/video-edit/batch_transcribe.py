"""Load Whisper once; for each clip: English slate pass (first 4s) + full pass (auto language)."""
import sys, json, subprocess, numpy as np, glob, os
from faster_whisper import WhisperModel
src_dir, out_dir, models = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out_dir, exist_ok=True)
m = WhisperModel("large-v3", device="cpu", compute_type="int8", download_root=models)
def pcm(f):
    b = subprocess.run(["ffmpeg", "-nostdin", "-i", f, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                       capture_output=True, check=True).stdout
    return np.frombuffer(b, np.int16).astype(np.float32) / 32768.0
P = "Kordovan, Mocha Mate, CNIC, scene, take, B-roll."
for f in sorted(glob.glob(os.path.join(src_dir, "*.mp4"))):
    a = pcm(f)
    slate = " ".join(s.text.strip() for s in m.transcribe(a[:16000 * 4], language="en", initial_prompt="Scene H1, take 1. Scene S3, take 2. B-roll B4.")[0])
    segs, info = m.transcribe(a, word_timestamps=True, vad_filter=True, initial_prompt=P)
    words = [[w.start, w.end, w.word.strip(), w.probability] for s in segs for w in s.words]
    rec = {"file": os.path.basename(f), "dur": len(a) / 16000, "slate": slate, "lang": info.language, "words": words}
    json.dump(rec, open(os.path.join(out_dir, os.path.basename(f) + ".json"), "w"), ensure_ascii=False)
    print(rec["file"], "|", slate, "|", info.language, "|", " ".join(w[2] for w in words)[:160], flush=True)
