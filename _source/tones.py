import re
# id: (bg, fg, accent)  -- mute/text2/line/bg2 derived
T = {
 'visa':        ('#1a1f71','#f5f5fb','#f7b600'),
 'fnb':         ('#16b3b0','#04201f','#00363a'),
 'lions':       ('#f9ba34','#141a45','#8a2a12'),
 'woza':        ('#006140','#f3fbf6','#ffd23f'),
 'icc':         ('#2a1a96','#f4f2ff','#63e3b4'),
 'ikigai':      ('#1b3a2d','#f3eee2','#d8c79f'),
 'deloitte':    ('#86bc25','#0a1200','#123f14'),
 'jifa':        ('#e6e2d1','#1a140c','#7a5631'),
 'airfrance':   ('#0b1d4c','#f2f4fa','#ff5a64'),
 'hillcountry': ('#efe4cf','#2a1d10','#8a5426'),
 'harmony':     ('#7e3520','#fbf1e9','#f2c76b'),
 'petra':       ('#2e241b','#f3ebe2','#f0a43a'),
 'migration':   ('#ebe7e0','#161613','#161613'),
}
def rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def lum(c):
    def f(v):
        v/=255; return v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4
    r,g,b=map(f,c); return .2126*r+.7152*g+.0722*b
def cr(a,b):
    la,lb=lum(a),lum(b); return (max(la,lb)+.05)/(min(la,lb)+.05)
def mix(a,b,t): return tuple(round(a[i]*(1-t)+b[i]*t) for i in range(3))
def hx(c): return '#%02x%02x%02x'%c
out=[];rows=[]
for k,(bg,fg,ac) in T.items():
    B,F,A=rgb(bg),rgb(fg),rgb(ac)
    dark=lum(B)<.18
    t=.34
    while cr(mix(F,B,t),B)<4.7: t-=.02
    mute=mix(F,B,t); t2=mix(F,B,.16)
    bg2=mix(B,F,.07)
    line='rgba(%d,%d,%d,.2)'%F
    bar='rgba(%d,%d,%d,.86)'%B
    rows.append((k,round(cr(F,B),1),round(cr(mute,B),1),round(cr(A,B),1)))
    out.append(f'--case-bg:{bg};--case-bg2:{hx(bg2)};--case-fg:{fg};--case-mute:{hx(mute)};--case-t2:{hx(t2)};--case-acc:{ac};--case-line:{line};--case-bar:{bar};--case-scheme:{"dark" if dark else "light"}')
for r in rows: print(r)
import json; json.dump(dict(zip(T,out)),open('/home/claude/tools/tones.json','w'))
