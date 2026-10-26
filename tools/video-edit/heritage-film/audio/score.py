# Original 15s luxury score: low cello drone (D minor), sparse felt piano, sub swell into a low hit at the logo.
# VO is mixed on top with ducking. Synthesised from scratch, no samples, no licence.
import numpy as np, sys, wave, soundfile as sf
SR=48000; DUR=15.0; N=int(SR*DUR); rng=np.random.default_rng(11)
L=np.zeros(N); R=np.zeros(N); t=np.arange(N)/SR
def hz(m): return 440*2**((m-69)/12)
def put(s,at,g=1.0,pan=0.0,buf=None):
    i=int(at*SR); j=min(N,i+len(s)); s=s[:j-i]*g
    L[i:j]+=s*np.sqrt((1-pan)/2)*1.414; R[i:j]+=s*np.sqrt((1+pan)/2)*1.414
def lp(x,fc):
    a=np.exp(-2*np.pi*fc/SR); y=np.empty_like(x); s=0.0
    for k in range(len(x)): s=(1-a)*x[k]+a*s; y[k]=s
    return y
# drone: D2 + A2 bowed (saw harmonics, slow vibrato, slow swell)
def bow(m,d,att=2.0):
    x=np.arange(int(d*SR))/SR; vib=1+0.004*np.sin(2*np.pi*5*x)
    ph=2*np.pi*np.cumsum(hz(m)*vib)/SR; s=sum(np.sin(k*ph)/k for k in range(1,12))
    e=np.minimum(1,x/att)*np.minimum(1,(d-x)/1.0); return lp(s*e,1400)*0.25
put(bow(38,12.0),0.0,0.55,-0.2); put(bow(45,11.5,3.0),0.5,0.35,0.2); put(bow(50,6,2.5),6.0,0.2)
def piano(m,d=3.0):
    x=np.arange(int(d*SR))/SR
    s=sum(a*np.sin(2*np.pi*hz(m)*k*x)*np.exp(-x*(0.9+k*0.6)) for k,a in ((1,1),(2,0.35),(3,0.15),(4,0.06)))
    return s*np.minimum(1,x/0.006)
for at,m in [(0.4,74),(3.0,69),(3.6,77),(5.6,76),(7.6,74),(8.4,81),(10.2,72)]: put(piano(m),at,0.18,rng.uniform(-.4,.4))
# sub swell 10.8 -> 12.0 then low hit at 12.0 (logo)
x=np.arange(int(1.2*SR))/SR; put(np.sin(2*np.pi*np.cumsum(30+25*x)/SR)*(x/1.2)**2,10.8,0.6)
x=np.arange(int(3*SR))/SR; hit=np.sin(2*np.pi*np.cumsum(40+50*np.exp(-x/0.06))/SR)*np.exp(-x/1.0)+lp(rng.normal(0,1,len(x)),600)*np.exp(-x/0.3)*0.3
put(hit,12.0,0.8)
for m in (62,69,74,77): put(piano(m,3.0),12.05,0.12)
# reverb
def verb(x,seed):
    r=np.random.default_rng(seed); n=int(2.8*SR); ir=r.normal(0,1,n)*np.exp(-np.arange(n)/SR/0.8); ir=lp(ir,4000); ir/=np.sqrt((ir**2).sum())
    m=1<<int(np.ceil(np.log2(len(x)+n))); return np.fft.irfft(np.fft.rfft(x,m)*np.fft.rfft(ir,m),m)[:len(x)]
L=L+0.45*verb(L,1); R=R+0.45*verb(R,2)
mus=np.stack([L,R],1); mus/=np.abs(mus).max()
# voiceover placements + ducking
vo=np.zeros((N,2))
for i,at in enumerate((0.7,3.3,7.7,12.5)):
    a,sr=sf.read(f"vo{i}.wav"); assert sr==48000; s=int(at*SR); e=min(N,s+len(a)); vo[s:e]+=a[:e-s]
vo/=np.abs(vo).max()
env=np.convolve((np.abs(vo).max(1)>0.02).astype(float),np.ones(int(0.25*SR))/int(0.25*SR),'same')
duck=1-0.45*np.clip(env*3,0,1)
mix=mus*0.42*duck[:,None]+vo*0.9
fade=np.clip((DUR-t)/1.2,0,1)[:,None]; mix*=fade
mix=np.tanh(mix*1.1); mix/=np.abs(mix).max(); mix*=0.89
w=wave.open(sys.argv[1],"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close(); print("ok")
