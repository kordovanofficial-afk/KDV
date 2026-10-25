# Original upbeat 15s track + SFX for the Mocha Mate stop-motion ad. Synthesised from scratch (no samples, no licence).
# 120 BPM, F major (F - Dm - Bb - C), bouncy house groove. Every SFX sits on a cut or a text pop.
import numpy as np, sys, wave
SR=48000; DUR=15.0; N=int(SR*DUR); rng=np.random.default_rng(3)
L=np.zeros(N); R=np.zeros(N)
def hz(m): return 440*2**((m-69)/12)
def put(s,at,g=1.0,pan=0.0):
    i=int(at*SR); j=min(N,i+len(s)); s=s[:j-i]*g
    L[i:j]+=s*np.sqrt((1-pan)/2)*1.414; R[i:j]+=s*np.sqrt((1+pan)/2)*1.414
def t_(d): return np.arange(int(d*SR))/SR
def lp(x,fc):
    fc=np.broadcast_to(np.asarray(fc,float),x.shape); a=np.exp(-2*np.pi*fc/SR); y=np.empty_like(x); s=0.0
    for k in range(len(x)): s=(1-a[k])*x[k]+a[k]*s; y[k]=s
    return y
def hp(x,fc): return x-lp(x,fc)
# --- drums
def kick():
    x=t_(0.35); return np.sin(2*np.pi*np.cumsum(50+110*np.exp(-x/0.03))/SR)*np.exp(-x/0.16)+rng.normal(0,1,len(x))*np.exp(-x/0.003)*0.2
def clap():
    x=t_(0.25); n=hp(rng.normal(0,1,len(x)),900); e=sum(np.exp(-np.maximum(0,x-o)/0.01)*(x>=o) for o in (0,0.011,0.022))+np.exp(-x/0.09)*0.6
    return n*e*0.5
def hat(open_=False):
    x=t_(0.18 if open_ else 0.05); return hp(rng.normal(0,1,len(x)),7000)*np.exp(-x/(0.06 if open_ else 0.012))
# --- tonal
def pluck(m,d=0.22,b=7):
    x=t_(d); return sum(np.sin(2*np.pi*hz(m)*k*x)/k**1.5*np.exp(-x*k*b) for k in range(1,6))*np.minimum(1,x/0.003)
def marimba(m,d=0.35):
    x=t_(d); return (np.sin(2*np.pi*hz(m)*x)+0.35*np.sin(2*np.pi*hz(m)*4*x)*np.exp(-x/0.03))*np.exp(-x/0.12)*np.minimum(1,x/0.002)
def bass(m,d=0.22):
    x=t_(d); s=np.sign(np.sin(2*np.pi*hz(m)*x))*0.5+np.sin(2*np.pi*hz(m)*x); return lp(s*np.exp(-x/0.12)*np.minimum(1,x/0.004),900)
def stab(ms,d=0.18):
    x=t_(d); s=sum(np.sin(2*np.pi*hz(m+dt)*k*x+rng.uniform(0,6))/k**1.3 for m in ms for dt in (-0.06,0.06) for k in range(1,6))
    return lp(s*np.exp(-x/0.07)*np.minimum(1,x/0.003),3500)/len(ms)
B=0.5
prog=[(65,[65,69,72]),(62,[62,65,69]),(58,[58,62,65]),(60,[60,64,67])]   # F Dm Bb C
mel=[77,81,79,77, 74,77,76,72, 74,77,79,82, 81,79,77,76]                  # bouncy hook, 8ths
# intro 0-2s: thin (hook + rewind) so the SFX read; groove from 2.0s; break 8.5-10.5 drums only stutter; outro 10.5-15
for b in range(30):
    at=b*B
    if 2.0<=at<10.5 or 10.5<=at<14.0:
        put(kick(),at,0.9)
        if b%2==1: put(clap(),at,0.45)
        put(hat(True),at+0.25,0.13,0.3)
        if at<8.5 or at>=10.5:
            for q in (0.0,0.125,0.375): put(hat(),at+q,0.07,-0.3)
    root,ch=prog[(b//4)%4]
    if at>=2.0 and not (8.5<=at<10.5) and at<14.0:
        put(bass(root-24),at,0.5); put(bass(root-12),at+0.25,0.35)
        if b%2==0: put(stab([m+12 for m in ch]),at+0.25,0.28,0.2)
    if (2.0<=at<8.5) or (10.5<=at<14.0):
        for h in (0,1):
            put(marimba(mel[(2*b+h)%16]),at+h*0.25,0.22,-0.2 if h else 0.2)
# hook bar 0-1.5: tick-tock plucks (stop-motion feel)
for i,m in enumerate([77,77,84,77,77,84]): put(pluck(m,0.12,14),i*0.25,0.25,(-1)**i*0.3)
# break 8.5-10.5: 16th stutter claps rising
for i in range(16): put(clap(),8.5+i*0.125,0.12+0.02*i); put(pluck(60+i,0.1,20),8.5+i*0.125,0.12)
put(kick(),10.5,1.0); put(stab([65,69,72,77]),10.5,0.4)
# final chord 14.0
x=t_(1.0); put(stab([65,69,72,77],1.0)*1.5,14.0,0.5); put(marimba(89,0.8),14.0,0.25)
# --- SFX
def pop():  x=t_(0.09); return np.sin(2*np.pi*np.cumsum(1400*np.exp(-x/0.015)+300)/SR)*np.exp(-x/0.025)
def boing(): x=t_(0.45); f=180+120*np.sin(2*np.pi*14*x)*np.exp(-x/0.2)+x*200; return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-x/0.18)
def scratch():
    x=t_(0.5); f=600+500*np.sin(2*np.pi*6*x); n=rng.normal(0,1,len(x)); return (lp(n,f)-lp(lp(n,f*0.3),f*0.3))*np.sin(np.pi*x/0.5)*3
def thud(): x=t_(0.3); return np.sin(2*np.pi*np.cumsum(60+90*np.exp(-x/0.02))/SR)*np.exp(-x/0.08)+lp(rng.normal(0,1,len(x)),1500)*np.exp(-x/0.02)*0.6
def jingle():
    out=np.zeros(int(0.6*SR))
    for k in range(9):
        o=int(rng.uniform(0,0.35)*SR); x=t_(0.25); f=rng.uniform(3000,6500)
        s=(np.sin(2*np.pi*f*x)+0.5*np.sin(2*np.pi*f*2.7*x))*np.exp(-x/0.05); out[o:o+len(s)]+=s[:len(out)-o]*0.3
    return out
def click(): x=t_(0.06); return hp(rng.normal(0,1,len(x)),2500)*np.exp(-x/0.006)+np.sin(2*np.pi*1800*x)*np.exp(-x/0.01)*0.5
def ding(): x=t_(0.9); return sum(a*np.sin(2*np.pi*1567*r*x)*np.exp(-x/(0.5*d)) for r,a,d in ((1,1,1),(2.0,0.3,0.5),(3.0,0.15,0.3)))
def whoosh(d=0.3):
    x=t_(d); n=rng.normal(0,1,len(x)); fc=400*(12)**(x/d); return (lp(n,fc)-lp(n,fc*0.3))*np.sin(np.pi*x/d)**2*1.5
def chaching():
    return np.concatenate([click()*0.8, np.zeros(int(0.06*SR))]), ding()
for at,s,g in [(0.05,pop(),0.5),(0.5,boing(),0.45),(1.5,scratch(),0.35),(2.0,thud(),0.6),(3.25,pop(),0.55),
               (4.0,whoosh(),0.3),(4.35,jingle(),0.5),(5.8,click(),0.6),(6.5,whoosh(),0.3),(6.55,pop(),0.4),
               (7.5,ding(),0.25),(8.5,thud(),0.4),(9.0,thud(),0.4),(9.5,thud(),0.4),(10.5,whoosh(0.4),0.35)]:
    put(s,at,g)
c,d=chaching(); put(c,11.6,0.5); put(d,11.66,0.3)        # price stamp
put(pop(),12.3,0.4); put(pop(),12.6,0.4)
# master
def verb(x,seed):
    r=np.random.default_rng(seed); n=int(0.9*SR); ir=r.normal(0,1,n)*np.exp(-np.arange(n)/SR/0.2); ir=lp(ir,6000); ir/=np.sqrt((ir**2).sum())
    m=1<<int(np.ceil(np.log2(len(x)+n))); return np.fft.irfft(np.fft.rfft(x,m)*np.fft.rfft(ir,m),m)[:len(x)]
L=L+0.15*verb(L,1); R=R+0.15*verb(R,2)
t=np.arange(N)/SR; f=np.clip((DUR-t)/0.6,0,1); L*=f; R*=f
mx=np.stack([L,R],1); mx=np.tanh(mx/np.abs(mx).max()*1.6)
w=wave.open(sys.argv[1],"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mx/np.abs(mx).max()*0.89*32767).astype(np.int16).tobytes()); w.close(); print("ok")
