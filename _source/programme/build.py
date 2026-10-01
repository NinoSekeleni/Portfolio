import json,html
T=json.load(open('/home/claude/tools/tones.json'))
def tone(k):
    d={}
    for part in T[k].split(';'):
        a,b=part.split(':',1); d[a.strip()]=b.strip()
    return d
F='/tmp/claude-0/pf/fonts/node_modules/@fontsource-variable'
E=html.escape
FEAT=[
 ('visa','Visa · Paris 2024 Olympic Games','A Moment for More','Creative Lead, campaign and digital · 2024','mfm-akani.jpg','band','70% 32%',
  "Visa's Paris 2024 brief was to get Millennials and Gen Z using their cards, so we turned three audience truths into one flexible platform led by sprinter Akani Simbine across TikTok, Meta, in-game media and live activations.",
  [('$2.4M','Visa revenue from four partner-bank campaigns I led in one quarter'),('9','influencers across three tiers, led by Akani Simbine'),('2','global Visa properties led in one year')]),
 ('fnb','Visa × FNB · FIFA World Cup 2026','It Starts Here','Creative Lead, campaign and art direction · 2025','fnb-kv.jpg','band','30% 40%',
  "FNB became the first South African bank to bring the FIFA World Cup 2026 to its customers, launched a year early with a 60-second manifesto film and carried across radio, digital out-of-home, social, direct mail and a Mall of Africa activation.",
  [('+32%','growth in new-card spend, Visa Q1 FY26 report'),('1st','South African bank to bring the World Cup to its customers'),('3','customers flown to the World Cup through Tap & Win')]),
 ('lions','DP World Lions Cricket','The Pride of Jozi','Creative Lead, brand and campaigns · 2022/23 to today','lions-matchday-titans.jpg','side','50% 20%',
  "Over four seasons I built The Pride of Jozi into a full brand for the DP World Lions, from the brand book and kit to a match-day content engine whose sponsor placements Nielsen Sports valued at R3.5M.",
  [('R3.5M','sponsor media value on Lions social, Nielsen Sports'),('+124%','Instagram followers, May 2021 to May 2024'),('2×','Sport Organisation of the Year, 2023 and 2024')]),
 ('woza','Cricket South Africa','Woza Nawe','Creative Lead, concept and identity · 2023/24 and 2024/25','woza-kv.jpg','band','50% 50%',
  "To bring South Africans back to domestic cricket I created Woza Nawe, an isiZulu invitation to be part of it, which ran as CSA's domestic theme for two seasons with a SuperSport TVC, an original song and dance challenge, and ticket promotions.",
  [('2','seasons as the domestic theme'),('16','domestic teams under one banner'),('2,000','fans a stadium given free entry')]),
 ('icc','ICC Men\'s T20 World Cup 2024 · Proteas','Road to the final','Creative Lead, tournament campaign and match-day content · 2024','t20-semi.jpg','side','50% 22%',
  "For the Proteas' T20 World Cup 2024 we ran the tournament campaign and a live match-day content system that covered every toss, milestone and result through eight straight wins to the country's first men's World Cup final.",
  [('20M+','people reached, paid and organic (Migration estimate)'),('9','matches covered live'),('1st','men\'s World Cup final for the Proteas')]),
 ('ikigai','Ikigai Kofi Hys','Where hustle meets harmony','Brand identity, art direction and web design · 2026','ik-cups.jpg','band','50% 55%',
  "For a new coffee house in Alexandra I created a brand that feels tranquil and vibrant at once, and carried it from the guidelines into packaging, signage, uniforms, the menu and a website I designed and built.",
  [('14','touchpoints designed, from the cup to the website'),('6','chapters in the brand guidelines'),('3','enquiry types handled through one website')]),
 ('deloitte','Deloitte Digital','Time for What Matters','Creative Lead, concept and visual identity · 2021 to 2025','tfwm.jpg','band','50% 50%',
  "Time for What Matters gave Deloitte Digital a platform built on an insight about an audience tired of campaigns, and it ran for more than three years across LinkedIn, Instagram, a podcast and two Mining Indaba editions.",
  [('3+','years as the team\'s platform'),('19','illustrated characters of the team'),('2','Mining Indaba editions, 2024 and 2025')]),
 ('hillcountry','Lwazi Loyiso Qhama Dekeda · AI-led book cover','Formed to Take the Hill Country','Cover design and art direction · 2026','hc-final-front.jpg','side','50% 30%',
  "For an author who wanted to be surprised by something true, I used AI to build four creative worlds and three full cover directions, reviewed through client sites I built, before preparing the print-ready cover.",
  [('4','creative worlds in the first mood board'),('3','complete cover directions'),('3','interactive client sites, built with AI')]),
]
SQUAD=[
 ('jifa','Judicial Institute for Africa','A brand for African justice','jifa-1.jpg',"A professional, authoritative identity for the institute that leads judicial training across Africa, with guidelines and templates its own team can use."),
 ('airfrance','Air France','Decades of Connection','af-poster-1.jpg',"The event identity for a one-night theatrical performance marking 70 years of Air France flights between Paris and Johannesburg, down to a boarding-pass invitation."),
 ('harmony','Harmony Gold','Mining with Purpose','harmony-hero.jpg',"Communication for Harmony Gold's Mining with Purpose message, from the results campaign and Mining Indaba speakers to a stark 16 Days of Activism poster series."),
 ('petra','Petra Diamonds','Purpose Statement','petra-9.jpg',"A four-film illustrated animation series explaining Petra Diamonds' purpose and culture code, adapted into Swahili for its operations in Tanzania."),
 ('migration','Migration','Studio website','ux-hero.jpg',"UX and UI for Migration's studio website, from wireframes to a black full-screen menu built around the studio's M."),
]
PAGES={'visa':3,'fnb':3,'lions':4,'woza':4,'icc':5,'ikigai':5,'deloitte':6,'hillcountry':6}
def foot(n,dark=False):
    return f'<footer class="pf{" dk" if dark else ""}"><span>Nino Sekeleni · Match-day programme 2026</span><span>{n:02d}</span></footer>'
def feature(i,c):
    k,client,title,role,img,lay,pos,summary,res=c; t=tone(k)
    st=f"--bg:{t['--case-bg']};--fg:{t['--case-fg']};--mu:{t['--case-mute']};--ac:{t['--case-acc']};--ln:{t['--case-line']}"
    rs=''.join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a,b in res)
    txt=f'''<div class="ft"><p class="eb"><span class="no">{i:02d}</span>{E(client)}</p><h3>{E(title)}</h3><p class="sum">{E(summary)}</p><p class="role">{E(role)}</p><div class="rs">{rs}</div></div>'''
    im=f'<div class="fi"><img src="a/{img}" style="object-position:{pos}" alt=""></div>'
    if lay=='side':
        from PIL import Image as _I
        w,h=_I.open('/home/claude/prog/a/'+img).size
        st+=f';grid-template-columns:{min(104,round(130*w/h,1))}mm 1fr'
    return f'<section class="feat {lay}" style="{st}">{im}{txt}</section>'
order=[f[0] for f in FEAT]+[s[0] for s in SQUAD]
names={f[0]:(f[2],f[1]) for f in FEAT}; names.update({s[0]:(s[2],s[1]) for s in SQUAD})
fix=''.join(f'<li><span class="n">{i+1:02d}</span><span class="dot" style="background:{tone(k)["--case-bg"]}"></span><b>{E(names[k][0])}</b><span class="cl">{E(names[k][1].split(" · ")[0])}</span><span class="pg">{PAGES.get(k,7)}</span></li>' for i,k in enumerate(order))
squad=''.join(f'''<li><img src="a/{img}" alt=""><div><p class="eb"><span class="dot" style="background:{tone(k)["--case-bg"]}"></span>{E(cl)}</p><h4>{E(ti)}</h4><p>{E(tx)}</p></div></li>''' for k,cl,ti,img,tx in SQUAD)
pages=[]
pages.append(f'''<div class="page cover"><div class="glow"></div>
<div class="ctop"><span>Match-day programme</span><span>Season 2026</span></div>
<div class="cname"><h1>Nino<br>Sekeleni</h1><p>Creative Director</p></div>
<img class="cport" src="a/nino.png" alt="">
<div class="cbot"><p class="k">Selected work, 2022 to 2026</p><p class="cl">Visa · FNB · DP World Lions · Cricket South Africa · Proteas · Ikigai Kofi Hys · Deloitte Digital · Air France · Harmony Gold · Petra Diamonds</p><p class="url">ninosekeleni.github.io/Portfolio</p></div>
</div>''')
pages.append(f'''<div class="page paper"><p class="kick">Team news</p>
<h2 class="big">Creative director, art director and creative strategist, based in Johannesburg.</h2>
<div class="intro"><p>I'm Creative Lead at Migration, where over the last four years I've led creative for sport, culture and financial-services brands such as Visa, Cricket South Africa and the DP World Lions. I build campaign platforms that run for whole seasons, and today I bring AI into every stage of that work, from the first idea to the finished campaign.</p><p>This programme is the short version of my portfolio. The full stories, films and credits are online at ninosekeleni.github.io/Portfolio, and I'm open to creative director and creative lead roles in any industry.</p></div>
<div class="stats"><div><b>10yr</b><span>across creative strategy, art direction and design</span></div><div><b>$2.4M</b><span>Visa revenue from my partner-bank campaigns in one quarter</span></div><div><b>R3.5M</b><span>sponsor media value for the DP World Lions</span></div><div><b>+32%</b><span>new-card spend on FNB × Visa</span></div><div><b>20M+</b><span>people reached by the Proteas' T20 World Cup campaign</span></div><div><b>2×</b><span>Sport Organisation of the Year with Lions Cricket</span></div></div>
<p class="src">Sources: Visa Q1 FY26 marketing report, Nielsen Sports, Hollard Sport Industry Awards and Migration estimates.</p>
<p class="kick k2">The fixture list</p><ol class="fix">{fix}</ol>
{foot(2)}</div>''')
for p in range(4):
    a,b=FEAT[2*p],FEAT[2*p+1]
    pages.append(f'<div class="page feats">{feature(2*p+1,a)}{feature(2*p+2,b)}{foot(3+p)}</div>')
pages.append(f'''<div class="page paper"><p class="kick">The rest of the squad</p><h2 class="big sm">Identity, events, design and animation for brands across Africa.</h2><ul class="squad">{squad}</ul>{foot(7)}</div>''')
pages.append(f'''<div class="page back"><div class="glow"></div><p class="kick">Post-match</p><h2>Let's make<br>something together.</h2>
<p class="lead">I'm open to creative director and creative lead roles in any industry. Send me a note about the role and I'll come back to you.</p>
<dl class="ct"><dt>Email</dt><dd>sekelenin@gmail.com</dd><dt>LinkedIn</dt><dd>linkedin.com/in/nino-sekeleni-a16b88121</dd><dt>Portfolio</dt><dd>ninosekeleni.github.io/Portfolio</dd><dt>Based</dt><dd>Johannesburg, South Africa</dd></dl>
<div class="qr"><img src="a/qr.svg" alt=""><p>Scan for the full portfolio, with every film, case study and credit.</p></div>
{foot(8,True)}</div>''')
css=f'''
@font-face{{font-family:"Bricolage";src:url("{F}/bricolage-grotesque/files/bricolage-grotesque-latin-standard-normal.woff2") format("woff2");font-weight:200 800;font-stretch:75% 100%}}
@font-face{{font-family:"Hanken";src:url("{F}/hanken-grotesk/files/hanken-grotesk-latin-wght-normal.woff2") format("woff2");font-weight:100 900}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:"Hanken",Helvetica,Arial,sans-serif;color:#161613;font-size:9.5pt;line-height:1.5}}
h1,h2,h3,h4{{font-family:"Bricolage",Helvetica,Arial,sans-serif;font-weight:700;letter-spacing:-.025em;line-height:1}}
.page{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;break-after:page;padding:14mm 14mm 0}}
.page:last-child{{page-break-after:auto;break-after:auto}}
.pf{{position:absolute;left:14mm;right:14mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7pt;letter-spacing:.04em;color:#77736b;border-top:.3mm solid rgba(22,22,19,.15);padding-top:2.2mm}}
.pf.dk{{color:#9a968d;border-color:rgba(239,236,230,.18)}}
.cover,.back{{background:#0e0e0c;color:#efece6}}
.glow{{position:absolute;inset:0;background:radial-gradient(120mm 120mm at 78% 72%,rgba(239,236,230,.13),transparent 70%),radial-gradient(110mm 90mm at 0% 0%,rgba(230,178,109,.16),transparent 70%)}}
.ctop{{position:relative;display:flex;justify-content:space-between;font-size:8pt;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#e6b26d;padding-bottom:3mm;border-bottom:.3mm solid rgba(239,236,230,.2)}}
.cname{{position:relative;margin-top:16mm}}
.cname h1{{font-size:66pt;line-height:.9;letter-spacing:-.04em}}
.cname p{{font-family:"Bricolage";font-weight:700;font-size:30pt;letter-spacing:-.03em;color:#9a968d;margin-top:3mm}}
.cport{{position:absolute;right:6mm;bottom:0;height:196mm;width:auto}}
.cbot{{position:absolute;left:14mm;bottom:14mm;width:92mm}}
.cbot .k{{font-size:8pt;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#e6b26d;margin-bottom:2.5mm}}
.cbot .cl{{font-size:9pt;line-height:1.55;color:#cfcbc3}}
.cbot .url{{margin-top:5mm;font-weight:600;font-size:10pt}}
.paper{{background:#ebe7e0}}
.kick{{font-size:8pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#a8691e;margin-bottom:4mm}}
.k2{{margin-top:8mm}}
.big{{font-size:26pt;line-height:1.05;max-width:165mm}}
.big.sm{{font-size:22pt;max-width:150mm;margin-bottom:8mm}}
.intro{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:6mm;font-size:10pt;line-height:1.55;color:#3b3832}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);margin-top:8mm;border-top:.3mm solid rgba(22,22,19,.18)}}
.stats div{{padding:4mm 4mm 4mm 0;border-bottom:.3mm solid rgba(22,22,19,.18);display:flex;flex-direction:column;gap:1mm}}
.stats div:not(:nth-child(3n+1)){{padding-left:4mm;border-left:.3mm solid rgba(22,22,19,.18)}}
.stats b{{font-family:"Bricolage";font-size:22pt;letter-spacing:-.03em;line-height:1}}
.stats span{{font-size:8pt;color:#5f5b53;line-height:1.35}}
.src{{font-size:6.8pt;color:#77736b;margin-top:2.5mm}}
.fix{{list-style:none;columns:2;column-gap:10mm}}
.fix li{{display:grid;grid-template-columns:7mm 3.4mm 1fr auto;align-items:baseline;gap:0 2mm;padding:2mm 0;border-bottom:.3mm solid rgba(22,22,19,.14);break-inside:avoid;font-size:8.8pt}}
.fix .n{{font-size:7.5pt;color:#77736b;font-variant-numeric:tabular-nums}}
.fix .dot{{width:2.6mm;height:2.6mm;border-radius:50%;align-self:center;box-shadow:0 0 0 .2mm rgba(22,22,19,.25)}}
.fix b{{font-weight:650}}
.fix .cl{{grid-column:3;font-size:7.5pt;color:#5f5b53}}
.fix .pg{{grid-column:4;grid-row:1;font-size:7.5pt;color:#77736b}}
.feats{{background:#0e0e0c;padding-top:10mm;display:flex;flex-direction:column;gap:5mm}}
.feat{{background:var(--bg);color:var(--fg);border-radius:5mm;overflow:hidden;height:130mm;display:grid}}
.feat.band{{grid-template-rows:62mm 1fr}}
.feat.side{{grid-template-columns:72mm 1fr}}
.fi{{overflow:hidden}}
.fi img{{width:100%;height:100%;object-fit:cover;display:block}}
.ft{{padding:6mm 7mm 6mm;display:flex;flex-direction:column}}
.feat.side .ft{{padding:7mm 7mm 6mm}}
.eb{{font-size:7.6pt;font-weight:600;letter-spacing:.04em;color:var(--ac);display:flex;align-items:center;gap:2.5mm}}
.eb .no{{font-variant-numeric:tabular-nums;border:.3mm solid var(--ln);border-radius:99px;padding:.3mm 2mm;color:var(--fg)}}
.feat h3{{font-size:21pt;margin:2.5mm 0 2.5mm}}
.feat.side h3{{font-size:19pt;margin:2.5mm 0 3mm}}
.feat.side .sum{{font-size:8.8pt}}
.sum{{font-size:9.2pt;line-height:1.5}}
.role{{font-size:7.5pt;color:var(--mu);margin-top:2mm}}
.rs{{margin-top:auto;display:grid;grid-template-columns:repeat(3,1fr);border-top:.3mm solid var(--ln);padding-top:3mm;gap:3mm}}
.feat.side .rs{{grid-template-columns:1fr;gap:2.5mm}}
.rs div{{display:flex;flex-direction:column;gap:.6mm}}
.feat.side .rs div{{flex-direction:row;align-items:baseline;gap:3mm}}
.rs b{{font-family:"Bricolage";font-size:17pt;letter-spacing:-.03em;line-height:1;white-space:nowrap}}
.feat.side .rs b{{min-width:19mm;font-size:15pt}}
.rs span{{font-size:7.4pt;line-height:1.35;color:var(--mu)}}
.feats .pf{{color:#9a968d;border-color:rgba(239,236,230,.18)}}
.squad{{list-style:none;display:flex;flex-direction:column;gap:5mm}}
.squad li{{display:grid;grid-template-columns:56mm 1fr;gap:7mm;align-items:center;padding-bottom:5mm;border-bottom:.3mm solid rgba(22,22,19,.15)}}
.squad img{{width:56mm;height:34mm;object-fit:cover;border-radius:2.5mm;display:block}}
.squad .eb{{color:#5f5b53}}
.squad .dot{{width:2.6mm;height:2.6mm;border-radius:50%;box-shadow:0 0 0 .2mm rgba(22,22,19,.25)}}
.squad h4{{font-size:15pt;margin:1.5mm 0 2mm}}
.squad p:not(.eb){{font-size:9pt;color:#3b3832;line-height:1.5}}
.back .kick{{position:relative;color:#e6b26d;margin-top:30mm}}
.back h2{{position:relative;font-size:48pt;line-height:.95;letter-spacing:-.04em}}
.back .lead{{position:relative;font-size:12pt;line-height:1.5;color:#cfcbc3;max-width:120mm;margin-top:8mm}}
.ct{{position:relative;display:grid;grid-template-columns:28mm 1fr;gap:3mm 4mm;margin-top:14mm;font-size:11pt;border-top:.3mm solid rgba(239,236,230,.18);padding-top:6mm;max-width:150mm}}
.ct dt{{color:#9a968d;font-size:9pt;padding-top:.6mm}}
.ct dd{{font-weight:600}}
.qr{{position:absolute;left:14mm;bottom:24mm;display:flex;align-items:center;gap:7mm}}
.qr img{{width:34mm;height:34mm;background:#efece6;padding:3mm;border-radius:3mm}}
.qr p{{font-size:9pt;color:#cfcbc3;max-width:60mm}}
'''
doc=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Nino Sekeleni, Match-day programme 2026</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open('/home/claude/prog/programme.html','w').write(doc); print('ok')
