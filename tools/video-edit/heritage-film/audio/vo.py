import sys, soundfile as sf
from kokoro_onnx import Kokoro
k=Kokoro("kokoro-v1.0.onnx","voices-v1.0.bin")
lines=["Leather remembers.","Every road. Every year.","Cut by hand. Made to be kept.","Kordovan."]
for v in sys.argv[1:]:
    for i,t in enumerate(lines):
        a,sr=k.create(t,voice=v,speed=0.82,lang="en-gb" if v.startswith("b") else "en-us")
        sf.write(f"{v}_{i}.wav",a,sr)
    print(v,sr)
