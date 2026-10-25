# Original 16 s score for the Kordovan teaser. Synthesised from scratch: no samples, no licence.
# 120 BPM (beat 0.5 s). Cuts at 1.5 3 4 5.5 7.5(keys punch) 8 (drop) 11 (logo).
import numpy as np, sys
SR=48000; DUR=16.0; N=int(SR*DUR); t=np.arange(N)/SR
rng=np.random.default_rng(7)
L=np.zeros(N); R=np.zeros(N)
def hz(m): return 440*2**((m-69)/12)
def put(sig, at, gain=1.0, pan=0.0):
    i=int(at*SR); j=min(N,i+len(sig)); s=sig[:j-i]*gain
    L[i:j]+=s*np.sqrt((1-pan)/2)*1.414; R[i:j]+=s*np.sqrt((1+pan)/2)*1.414
def env(n, a, d):  # attack / exp decay (seconds)
    x=np.arange(n)/SR; e=np.minimum(1, x/max(a,1e-4))*np.exp(-np.maximum(0,x-a)/d); return e
def lp(x, fc):  # one-pole lowpass, fc may be array
    fc=np.broadcast_to(np.asarray(fc,float),x.shape); a=np.exp(-2*np.pi*fc/SR); y=np.empty_like(x); s=0.0
    for k in range(len(x)): s=(1-a[k])*x[k]+a[k]*s; y[k]=s
    return y
def kick(g=1.0):
    n=int(0.6*SR); x=np.arange(n)/SR; f=45+80*np.exp(-x/0.04); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-x/0.28)*g + rng.normal(0,1,n)*np.exp(-x/0.004)*0.15
def pluck(m, dur=0.45, bright=4):
    n=int(dur*SR); x=np.arange(n)/SR; s=sum(np.sin(2*np.pi*hz(m)*k*x)/k**1.6 * np.exp(-x*k*bright) for k in range(1,7))
    return s*env(n,0.004,dur/3)
def pad(ms, dur, att=0.6):
    n=int(dur*SR); x=np.arange(n)/SR; s=np.zeros(n)
    for m in ms:
        for det in (-0.08,0,0.08):
            for k in range(1,9): s+=np.sin(2*np.pi*hz(m+det)*k*x+rng.uniform(0,6.28))/k**1.4
    e=np.minimum(1,x/att)*np.minimum(1,(dur-x)/0.5); return s*e/ (len(ms)*6)
def noise_sweep(dur, f0, f1, shape="whoosh"):
    n=int(dur*SR); x=np.arange(n)/SR; fc=f0*(f1/f0)**(x/dur); nz=rng.normal(0,1,n)
    y=lp(nz,fc)-lp(lp(nz,fc*0.25),fc*0.25)
    e=np.sin(np.pi*x/dur)**2 if shape=="whoosh" else (x/dur)**2.5
    return y*e
def bell(m, dur=2.5):
    n=int(dur*SR); x=np.arange(n)/SR
    return sum(a*np.sin(2*np.pi*hz(m)*r*x)*np.exp(-x/(dur*d)) for r,a,d in ((1,1,.5),(2.76,.4,.25),(5.4,.2,.12),(8.9,.08,.06)))

# chords (D minor): Dm  Bb  F  C  | drop Dm | logo Bbmaj7 -> Dm(add9)
prog=[(0,[50,53,57]),(2,[46,50,53]),(4,[41,45,48,53]),(6,[48,52,55])]
for at,ch in prog:
    put(pad([m+12 for m in ch],2.05,0.25),at,0.22)
    root=ch[0]-12 if ch[0]>45 else ch[0]
    for b in range(8):  # 8th-note bass ostinato
        put(pluck(root if b%2==0 else root+12,0.24,5),at+b*0.25,0.55)
    arp=[ch[0]+24,ch[1]+24,ch[2]+24,ch[1]+36]
    for b in range(8): put(pluck(arp[b%4],0.5,3),at+b*0.25,0.16,pan=(-0.4 if b%2 else 0.4))
# kicks: soft four-on-the-floor 0-7.5, half-time after the drop
for b in range(15): put(kick(0.9 if b%2==0 else 0.6),b*0.5,0.7)
for b in range(0,15): put(rng.normal(0,1,int(0.03*SR))*env(int(0.03*SR),0.001,0.01), b*0.5+0.25,0.05,pan=0.3)
# whooshes on the cuts
for c in (1.5,3.0,4.0,5.5,11.0): put(noise_sweep(0.5,300,6000),c-0.32,0.5,pan=rng.uniform(-.3,.3))
put(noise_sweep(0.35,600,8000),6.95,0.35)                     # keys punch-in
# riser into the drop at 8.0
put(noise_sweep(1.0,200,9000,"rise"),7.0,0.55)
x=np.arange(int(1.0*SR))/SR; put(np.sin(2*np.pi*np.cumsum(220*2**(x*1.5))/SR)*(x**2)*0.5,7.0,0.25)
# DROP 8.0: impact + big Dm
def impact(g):
    n=int(2.5*SR); x=np.arange(n)/SR
    return (np.sin(2*np.pi*np.cumsum(38+60*np.exp(-x/0.08))/SR)*np.exp(-x/0.9) + lp(rng.normal(0,1,n),1200)*np.exp(-x/0.25)*0.8)*g
put(impact(1.0),8.0,0.9)
put(pad([38,50,53,57,62,64],3.1,0.05),8.0,0.38)
for b in range(6): put(kick(0.8),8.0+b*0.5 if b%2==0 else 8.0+b*0.5,0.0 if b%2 else 0.55)
for b in range(12): put(pluck([62,65,69,72][b%4]+12,0.6,2.5),8.0+b*0.25,0.11,pan=(-.5 if b%2 else .5))
# LOGO 11.0: boom, low drone, bell shimmer as the horse draws, resolve
put(impact(0.9),11.0,0.85)
put(pad([34,46,50,53,57],2.2,0.3),11.0,0.32)
put(pad([38,50,53,57,64],3.0,0.4),13.0,0.32)
for i,m in enumerate([74,81,77,86]): put(bell(m,2.6),11.25+i*0.45,0.12,pan=(-.4,.4,-.2,.2)[i])
put(bell(62,3.0),13.0,0.18)

# reverb: convolve with decaying stereo noise
def verb(x, seed):
    r=np.random.default_rng(seed); n=int(1.9*SR); ir=r.normal(0,1,n)*np.exp(-np.arange(n)/SR/0.45); ir=lp(ir,5000); ir/=np.sqrt((ir**2).sum())
    m=1<<int(np.ceil(np.log2(len(x)+n))); return np.fft.irfft(np.fft.rfft(x,m)*np.fft.rfft(ir,m),m)[:len(x)]
L=L+0.35*verb(L,1); R=R+0.35*verb(R,2)
fade=np.clip((DUR-t)/1.2,0,1); L*=fade; R*=fade
mx=np.tanh(np.stack([L,R],1)*1.2/np.abs(np.stack([L,R])).max()*1.3)
import wave; w=wave.open(sys.argv[1],"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mx/np.abs(mx).max()*0.89*32767).astype(np.int16).tobytes()); w.close(); print("ok")
