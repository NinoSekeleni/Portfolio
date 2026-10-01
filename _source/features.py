import json
P='/home/claude/site/index.html'
h=open(P).read()
assert 'class="who"' not in h

CV='nino-sekeleni-cv.pdf?v=2026-10-01'
def L(id,t): return f'<a href="#{id}" data-j="{id}">{t}</a>'

# ---------- WORLDS ----------
W={
 'fintech':{'chip':'Fintech','short':'fintech and payments','top':3,
   'order':['visa','fnb','deloitte','icc','lions','woza','ikigai','jifa','airfrance','hillcountry','harmony','petra','migration'],
   'intro':"I lead creative for payments and financial-services brands, from Visa's partner-bank campaigns across Africa, which brought Visa $2.4M in revenue in a single quarter, to FNB's FIFA World Cup platform, and I bring AI into every stage of that work."},
 'sport':{'chip':'Sport','short':'sport','top':5,
   'order':['lions','woza','icc','visa','fnb','ikigai','deloitte','airfrance','jifa','hillcountry','harmony','petra','migration'],
   'intro':"I lead creative for sport properties and the sponsors around them, from four seasons building The Pride of Jozi for the DP World Lions to the Proteas' T20 World Cup campaign and Visa's Paris 2024 platform, and I bring AI into every stage of that work."},
 'fmcg':{'chip':'FMCG and retail','short':'FMCG and retail','top':4,
   'order':['ikigai','visa','woza','fnb','lions','airfrance','hillcountry','deloitte','icc','jifa','harmony','petra','migration'],
   'intro':"I build consumer brands and the campaigns that move them, from a coffee house identity carried into packaging, menus, signage and the website to mass-market platforms for Visa and Cricket South Africa that got people spending, buying tickets and showing up."},
 'agency':{'chip':'Agency','short':'agencies and studios','top':5,
   'order':['visa','lions','woza','deloitte','hillcountry','fnb','ikigai','icc','airfrance','harmony','petra','jifa','migration'],
   'intro':"I lead creative teams across a full client roster, from Visa and Cricket South Africa to Deloitte Digital and the DP World Lions, taking work from the pitch and the idea through to production, and I build AI workflows that help a studio move faster while keeping the craft high."},
}

# ---------- ASK NINO ----------
QA=[
 {'q':'Have you led teams?','k':['team','teams','lead','led','leader','leadership','manage','managed','manager','management','direct','directed','people','mentor','coach','coaching','staff','report','reports'],
  'a':f"Yes. At Migration I direct designers and content creators across the full project lifecycle, from brief to delivery, and I work alongside the strategy and account teams on every account. On {L('woza','Woza Nawe')} I directed the design and animation team across in-stadium, outdoor, ticketing and social, and I lead the creative for Visa's marketing services team on its {L('visa','partner-bank campaigns')}. I'm at my best when a whole team is pulling towards one clear idea."},
 {'q':'Have you worked in FMCG or retail?','k':['fmcg','retail','consumer','packaging','cpg','shopper','store','stores','product','products','food','drink','drinks','beverage','beverages','beer','coffee','grocery','supermarket','brewery'],
  'a':f"My closest FMCG and retail work is {L('ikigai','Ikigai Kofi Hys')}, a coffee house in Alexandra, where I built the identity and carried it into packaging, signage, uniforms, the menu and the website, which I designed and built myself. Much of my campaign work speaks to consumers too, from {L('visa','A Moment for More')}, which drove Visa card spend in store and online, to {L('woza','Woza Nawe')}, whose ticket promotions helped bring fans back to domestic cricket. I'm open to roles in any industry."},
 {'q':'What results can you show?','k':['result','results','roi','impact','numbers','number','revenue','metrics','metric','kpi','kpis','proof','prove','effective','effectiveness','performance','data','growth','measured','sales'],
  'a':f"The clearest numbers come from Visa's own report for the first quarter of its 2026 financial year, where four partner-bank campaigns I led, for FNB, Investec, CBZ and Chipper Cash, brought Visa $2.4M in revenue, with FNB's new-card spend up 32%. For the DP World Lions, Nielsen Sports valued the sponsor media on the club's channels at R3.5M, and the club was named Sport Organisation of the Year in 2023 and 2024. Earlier, at Soccer Laduma and KickOff, I grew the social audience from about 500K to 4M. {L('proof','See all the proof')}."},
 {'q':'How do you use AI?','k':['ai','a.i','artificial','intelligence','generative','genai','midjourney','chatgpt','claude','runway','sora','kling','firefly','automation','automate','prompt','prompting','llm'],
  'a':f"AI is part of how I work every day. I use it to research, concept, write, generate and art-direct imagery, and to build working products, such as the three client review sites for the {L('hillcountry','Hill Country book cover')}. I led the proposal to bring Claude into Migration's toolkit, and my talk Beyond the Prompt argues that when everyone has the same tools, judgement and taste are what set the work apart. The tools I use most are Claude, ChatGPT, Midjourney, Adobe Firefly, Runway, Kling and Sora."},
 {'q':'Which tools do you use?','k':['tool','tools','software','adobe','figma','photoshop','illustrator','indesign','premiere','canva','stack','programs','apps','asana','monday','hootsuite','analytics'],
  'a':"For design I use Photoshop, Illustrator, InDesign, Premiere Pro, Figma, Canva and Frame.io, and for generative work Claude, ChatGPT, Adobe Firefly, Midjourney, Google AI Studio, Runway, Kling and Sora. On the media side I work in Google Ads, Meta Ads Manager, TikTok Ads Manager, LinkedIn Campaign Manager and Google Analytics 4, and I run projects in Asana, Monday.com and Slack."},
 {'q':'How much experience do you have?','k':['experience','experienced','years','year','background','career','history','cv','resume','résumé','previous','before','senior','seniority','roles','jobs'],
  'a':f"I have about ten years of experience across creative strategy, art direction and design. I've been Creative Lead at Migration since May 2022, and before that I was Senior and Lead Multimedia Designer at BET.co.za, Creative and Social Media Lead at Soccer Laduma and KickOff, and a storyboard artist on Supa Strikas for Disney XD. <a href=\"{CV}\" target=\"_blank\" rel=\"noopener\">Download my full CV</a>."},
 {'q':'What did you study?','k':['study','studied','degree','education','qualification','qualifications','university','college','school','afda','honours','honors','trained','training','film school'],
  'a':"I trained in film at AFDA, the South African School of Motion Picture and Live Performance, where I earned a BA in Motion Picture Medium and then a BA Honours specialising in media production and technology. That grounding in storytelling and production still shapes how I run a project from strategy through to the finished work."},
 {'q':'What sport work have you done?','k':['sport','sports','sporting','cricket','football','soccer','olympics','olympic','sponsorship','sponsor','sponsors','rugby','athlete','athletes','club','stadium','proteas','lions','fifa','afcon','icc'],
  'a':f"Sport is where much of my work sits. I've led brand and campaign creative for the {L('lions','DP World Lions')} for four seasons, created {L('woza','Woza Nawe')} for Cricket South Africa, ran the Proteas' {L('icc','T20 World Cup 2024')} campaign, and led Visa's Paris 2024 platform with {L('visa','Akani Simbine')} and FNB's {L('fnb','FIFA World Cup')} campaign. Before that I grew Soccer Laduma and KickOff's social audience eightfold."},
 {'q':'Have you worked in financial services?','k':['fintech','bank','banks','banking','payment','payments','financial','finance','visa','card','cards','insurance','investec','fnb','absa','money'],
  'a':f"Yes, payments is one of my strongest areas. I've led Visa's {L('visa','A Moment for More')} for Paris 2024, FNB's {L('fnb','It Starts Here')} for the FIFA World Cup 2026, and creative for Visa's marketing services team on campaigns with partner banks including Investec, CBZ and Chipper Cash. Visa's own report credits four of those campaigns with $2.4M in revenue in one quarter."},
 {'q':'Do you do brand identity?','k':['identity','identities','logo','logos','branding','brand','guidelines','rebrand','rebranding','brandbook','book','typography','design system','visual identity'],
  'a':f"Yes. I've built identities from the ground up for {L('ikigai','Ikigai Kofi Hys')} and the {L('jifa','Judicial Institute for Africa')}, art-directed {L('lions','The Pride of Jozi')} into a full brand book for the DP World Lions, created the colour-burst identity for {L('woza','Woza Nawe')}, and designed the event identity for {L('airfrance','Air France')}'s 70 years of flights to Johannesburg."},
 {'q':'Have you worked on film and animation?','k':['film','films','video','videos','animation','animated','tvc','motion','shoot','shoots','director','directing','storyboard','storyboards','commercial','commercials','production'],
  'a':f"Film is where I started. I trained at AFDA and storyboarded Supa Strikas for Disney XD, and since then I've set the creative direction for FNB's 60-second {L('fnb','manifesto film')}, the {L('lions','DP World Lions manifesto films')}, the SuperSport TVC for {L('woza','Woza Nawe')}, and a four-film animated series for {L('petra','Petra Diamonds')}, adapted into Swahili for Tanzania."},
 {'q':'How do you approach strategy?','k':['strategy','strategic','strategist','insight','insights','positioning','research','planning','plan','thinking','idea','ideas','concept','concepts'],
  'a':f"I start from what the audience actually believes. For Visa's Paris 2024 work we turned three truths about Millennials and Gen Z into one flexible platform, {L('visa','A Moment for More')}, and for Deloitte Digital, {L('deloitte','Time for What Matters')} started from an insight about an audience that was tired of campaigns. On {L('woza','Woza Nawe')} I originated both the platform and the name."},
 {'q':'Have you pitched for new business?','k':['pitch','pitches','pitching','new business','proposal','proposals','tender','tenders','win','won','winning','credentials'],
  'a':f"Yes. I led the creative for Migration's 2025 proposal to {L('lions','Lions Cricket')}, which kept the partnership going into a fifth season, and I've developed pitch and partnership decks for leading financial institutions across Southern Africa and EMEA as part of my Visa work."},
 {'q':'Where are you based?','k':['relocate','relocation','remote','location','located','based','where','move','moving','hybrid','office','abroad','overseas','international','country','city','johannesburg','travel'],
  'a':"I'm based in Johannesburg, South Africa, and I work with brands across Africa, EMEA and beyond. For questions about relocation, remote or hybrid set-ups, send me a note about the role and I'll answer for that specific opportunity."},
 {'q':'Are you available?','k':['available','availability','notice','start','salary','rate','rates','cost','fee','fees','compensation','package','freelance','contract','hire','hiring','open','job','role','position','vacancy'],
  'a':"I'm available for creative director and creative lead roles in any industry. Notice period, salary and start dates depend on the role, so the best next step is a short email with the details, and I'll come back to you."},
 {'q':'How can I contact you?','k':['contact','email','mail','phone','call','reach','talk','meet','meeting','interview','linkedin','number','chat'],
  'a':f"The quickest way is email, at <a href=\"mailto:sekelenin@gmail.com\">sekelenin@gmail.com</a>. You can also find me on <a href=\"https://www.linkedin.com/in/nino-sekeleni-a16b88121/\" target=\"_blank\" rel=\"noopener\">LinkedIn</a>, and my phone number is on my <a href=\"{CV}\" target=\"_blank\" rel=\"noopener\">CV</a>."},
 {'q':'Have you won awards?','k':['award','awards','awarded','recognition','recognised','recognized','winner','prize','accolade','accolades'],
  'a':f"The DP World Lions were named Sport Organisation of the Year at the Hollard Sport Industry Awards in 2023 and 2024, during the seasons I led their brand and campaign creative. I co-led the award submission strategy and coordinated the evidence packs and creative assets. {L('lions','See the Lions work')}."},
 {'q':'How do you work?','k':['process','approach','work style','working style','philosophy','style','craft','collaborate','collaboration','culture','values','how do you work','way you work'],
  'a':"I lead from the work, I care about the craft, and I push for creative that is sharp enough to stand out and grounded enough to deliver. Collaboration sits at the heart of it: I've spent years coordinating designers, content creators, strategists and account teams, and I run a project from strategy and concept through to production, performance tracking and stakeholder reporting."},
 {'q':'What social media work have you done?','k':['social','instagram','tiktok','facebook','twitter','community','followers','following','audience','audiences','digital','content','posts','channels'],
  'a':f"A lot. At Soccer Laduma and KickOff I grew the combined social following from about 500K to 4M and co-created the Soccer Laduma Podcast. At Migration I've run the Proteas' social end-to-end across international tours and two ICC 50-over World Cups, and I designed the {L('lions','match-day content system')} that helped grow the Lions' Instagram following by 124%."},
 {'q':'Which markets have you worked in?','k':['africa','african','markets','market','countries','emea','global','nigeria','zimbabwe','kenya','tanzania','swahili','pan-african','regional','multi-market'],
  'a':f"Most of my work runs across Africa. For Visa I've led partner-bank campaigns in South Africa, Zimbabwe and Nigeria and worked on pitch decks across Southern Africa and EMEA, I adapted the {L('petra','Petra Diamonds')} films into Swahili for Tanzania, and I've designed for {L('jifa','pan-African')} institutions and for {L('airfrance','Air France')}'s Paris to Johannesburg route."},
 {'q':'Who is Nino?','k':['who','yourself','summary','introduce','introduction','about','overview','tell me about','bio'],
  'a':"I'm a creative director, art director and creative strategist based in Johannesburg, currently Creative Lead at Migration. I lead creative for sport, culture and financial-services brands such as Visa, Cricket South Africa and the DP World Lions, and I bring AI into every stage of the work, from the first idea to the finished campaign."},
]

FALLBACK="I haven't written an answer to that one yet, but I'd like to hear it. Send me the question and I'll reply myself."

who_html='''<div class="who" role="group" aria-label="Who's looking? Choose your industry to see the most relevant work first">
          <span class="who-k">Who's looking?</span>
          <button type="button" data-w="fintech" aria-pressed="false">Fintech</button><button type="button" data-w="sport" aria-pressed="false">Sport</button><button type="button" data-w="fmcg" aria-pressed="false">FMCG and retail</button><button type="button" data-w="agency" aria-pressed="false">Agency</button><button type="button" class="who-x" data-w="" hidden>Show everything</button>
        </div>
        '''
a='<h1 class="hero-h">'; assert a in h; h=h.replace(a,who_html+a,1)
a='<p class="thesis fade-up d1">'; assert a in h; h=h.replace(a,'<p class="thesis fade-up d1" id="thesis" aria-live="polite">',1)
# work intro id
a='<p>Thirteen projects in four chapters'; assert a in h; h=h.replace(a,'<p id="work-intro">Thirteen projects in four chapters',1)
# world groups at top of index
a='<ul class="index" id="index">\n'; assert a in h
h=h.replace(a,a+'      <li class="grp wgrp" data-cat="world" data-w="top" hidden><span>Most relevant</span></li>\n      <li class="grp wgrp" data-cat="world" data-w="rest" hidden><span>More work</span></li>\n',1)

ask_html='''
<button class="ask-btn" id="ask-btn" type="button" aria-haspopup="dialog" aria-controls="ask" aria-expanded="false"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 4.5h12a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5H9l-4 3v-3H4A1.5 1.5 0 0 1 2.5 13V6A1.5 1.5 0 0 1 4 4.5z"/></svg><span>Ask Nino</span></button>
<section class="ask" id="ask" role="dialog" aria-modal="false" aria-labelledby="ask-h" hidden>
  <header class="ask-head">
    <div><h2 id="ask-h">Ask Nino</h2><p>Answers I've written from my CV and case studies. Anything I haven't covered comes straight to my inbox.</p></div>
    <button type="button" class="ask-x" id="ask-x" aria-label="Close Ask Nino">&#215;</button>
  </header>
  <div class="ask-log" id="ask-log" aria-live="polite"></div>
  <div class="ask-sugg" id="ask-sugg"></div>
  <form class="ask-form" id="ask-form" autocomplete="off">
    <label for="ask-in" class="sr-only">Your question</label>
    <input id="ask-in" type="text" maxlength="240" placeholder="Ask about experience, sectors, results…" enterkeyhint="send">
    <button type="submit" aria-label="Send question"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg></button>
  </form>
</section>
'''
a='<script>\n(function(){'; assert a in h; h=h.replace(a,ask_html+a,1)

css='''
/* ---------- v17: who's looking, ask nino ---------- */
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.who{display:flex;flex-wrap:wrap;align-items:center;gap:.45rem;margin:0 0 clamp(1.4rem,2.6vw,2.2rem)}
.who-k{font-size:var(--step--1);font-weight:600;color:var(--gold);margin-right:.35rem}
.who button{font:inherit;font-size:.82rem;color:var(--on-ink-mute);background:transparent;border:1px solid var(--line-ink);border-radius:999px;padding:.38rem .8rem;cursor:pointer;transition:color .2s,background .2s,border-color .2s}
.who button:hover{color:var(--on-ink);border-color:var(--on-ink-mute)}
.who button[aria-pressed="true"]{background:var(--on-ink);color:var(--ink);border-color:var(--on-ink)}
.who .who-x{border-style:dashed}
.who .who-x[hidden]{display:none}
#thesis,#work-intro{transition:opacity .35s ease}
#thesis.swap,#work-intro.swap{opacity:0}
.ask-btn{position:fixed;left:clamp(12px,2vw,24px);bottom:calc(clamp(12px,2vw,24px) + env(safe-area-inset-bottom,0px));z-index:56;display:inline-flex;align-items:center;gap:.5rem;font:inherit;font-weight:600;font-size:var(--step--1);color:var(--on-ink);background:var(--bar);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border:1px solid var(--line-ink);border-radius:999px;padding:.7rem 1.05rem;cursor:pointer;box-shadow:0 10px 30px rgba(0,0,0,.25);transition:background .2s,color .2s,border-color .2s}
.ask-btn svg{width:18px;height:18px}
.ask-btn:hover{border-color:var(--on-ink-mute)}
.ask-btn[aria-expanded="true"]{opacity:0;pointer-events:none}
.ask{position:fixed;left:clamp(12px,2vw,24px);bottom:calc(clamp(12px,2vw,24px) + env(safe-area-inset-bottom,0px));z-index:70;width:min(400px,calc(100vw - 24px));height:min(600px,calc(100vh - 110px));display:flex;flex-direction:column;background:var(--ink-2);color:var(--on-ink);border:1px solid var(--line-ink);border-radius:20px;box-shadow:0 30px 80px rgba(0,0,0,.45);overflow:hidden}
.ask[hidden]{display:none}
.ask-head{display:flex;gap:1rem;justify-content:space-between;align-items:flex-start;padding:1.1rem 1.1rem .9rem 1.2rem;border-bottom:1px solid var(--line-ink)}
.ask-head h2{font-size:var(--step-1);letter-spacing:-.01em}
.ask-head p{margin:.3rem 0 0;font-size:.78rem;line-height:1.45;color:var(--on-ink-mute);max-width:32ch}
.ask-x{flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--line-ink);background:transparent;color:var(--on-ink);font-size:1.2rem;line-height:1;cursor:pointer}
.ask-log{flex:1;overflow-y:auto;padding:1rem 1.1rem;display:flex;flex-direction:column;gap:.7rem;overscroll-behavior:contain}
.ask-msg{max-width:88%;font-size:.9rem;line-height:1.55;padding:.7rem .9rem;border-radius:14px}
.ask-msg.me{align-self:flex-end;background:var(--on-ink);color:var(--ink);border-bottom-right-radius:4px}
.ask-msg.nino{align-self:flex-start;background:var(--ink);border:1px solid var(--line-ink);border-bottom-left-radius:4px}
.ask-msg.nino a{color:var(--gold);text-underline-offset:2px}
.ask-msg .ask-mail{display:inline-flex;margin-top:.6rem;font-weight:600;font-size:.82rem;color:var(--ink);background:var(--gold);padding:.45rem .8rem;border-radius:999px;text-decoration:none}
.ask-sugg{display:flex;gap:.4rem;overflow-x:auto;padding:0 1.1rem .7rem;scrollbar-width:none}
.ask-sugg::-webkit-scrollbar{display:none}
.ask-sugg button{flex:none;font:inherit;font-size:.78rem;color:var(--on-ink);background:transparent;border:1px solid var(--line-ink);border-radius:999px;padding:.4rem .75rem;cursor:pointer;white-space:nowrap}
.ask-sugg button:hover{border-color:var(--on-ink-mute)}
.ask-form{display:flex;gap:.5rem;padding:.8rem 1rem 1rem;border-top:1px solid var(--line-ink)}
.ask-form input{flex:1;min-width:0;font:inherit;font-size:16px;color:var(--on-ink);background:var(--ink);border:1px solid var(--line-ink);border-radius:999px;padding:.65rem 1rem}
.ask-form input:focus{outline:2px solid var(--gold);outline-offset:1px}
.ask-form button{flex:none;width:44px;height:44px;border-radius:50%;border:0;background:var(--on-ink);color:var(--ink);display:grid;place-items:center;cursor:pointer}
.ask-form button svg{width:16px;height:16px}
@media (max-width:620px){.ask{left:8px;right:8px;width:auto;bottom:8px;height:min(78vh,620px)}}
@media print{.ask,.ask-btn,.who{display:none!important}}
'''
i=h.find('</style>'); h=h[:i]+css+h[i:]

# ---------- JS: filters + nav hooks ----------
old="""    rows.concat(cases).forEach(function(el){el.hidden=!(f==='all'||el.getAttribute('data-cat')===f)});
  })});"""
new="""    rows.concat(cases).forEach(function(el){el.hidden=!(f==='all'||el.getAttribute('data-cat')===f)});
    refreshGroups();
  })});
  // group headers depend on the filter and on the chosen world
  var world=null;
  function curFilter(){var pb=document.querySelector('.filters button[aria-pressed="true"]');return pb?pb.getAttribute('data-f'):'all'}
  function grpHidden(cat,f){if(cat==='world')return !(world&&f==='all');if(world)return f==='all'?true:cat!==f;return !(f==='all'||cat===f)}
  function refreshGroups(){var f=curFilter();[].forEach.call(document.querySelectorAll('#index li.grp, .rail-grp, #worknav-grid li.wn-grp'),function(g){g.hidden=grpHidden(g.getAttribute('data-cat'),f)})}"""
assert old in h; h=h.replace(old,new,1)
old="    function visible(){return arts.filter(function(a){return !a.hidden})}"
assert old in h; h=h.replace(old,"    function visible(){return [].slice.call(document.querySelectorAll('article.case')).filter(function(a){return !a.hidden})}",1)
old="""    var k=0;
    [].forEach.call(document.querySelectorAll('#index li'),function(li){
      if(li.classList.contains('grp')){var g=document.createElement('li');g.className='wn-grp';g.setAttribute('data-cat',li.getAttribute('data-cat'));g.textContent=li.textContent;grid.appendChild(g);return}"""
new="""    function buildGrid(){
    grid.innerHTML='';var k=0;
    [].forEach.call(document.querySelectorAll('#index li'),function(li){
      if(li.classList.contains('grp')){var g=document.createElement('li');g.className='wn-grp';g.setAttribute('data-cat',li.getAttribute('data-cat'));g.textContent=li.textContent;g.hidden=li.hidden;grid.appendChild(g);return}"""
assert old in h; h=h.replace(old,new,1)
old="""      grid.appendChild(item);
    });
    function openNav(){"""
new="""      grid.appendChild(item);
    });
    }
    buildGrid();
    function openNav(){"""
assert old in h; h=h.replace(old,new,1)
old="""        if(li.classList.contains('wn-grp')){li.hidden=!(on==='all'||li.getAttribute('data-cat')===on);return}"""
new="""        if(li.classList.contains('wn-grp')){li.hidden=grpHidden(li.getAttribute('data-cat'),on);return}"""
assert old in h; h=h.replace(old,new,1)
old="""        var f=b.getAttribute('data-f');[].forEach.call(document.querySelectorAll('.rail-grp'),function(g){g.hidden=!(f==='all'||g.getAttribute('data-cat')===f)});"""
new="""        refreshGroups();"""
assert old in h; h=h.replace(old,new,1)
old="""    buildSteps();
    if(location.hash"""
new="""    buildSteps();
    window.__nsRebuild=function(){
      tabs.forEach(function(t){var a=document.getElementById(t.getAttribute('data-case'));t.hidden=!!(a&&a.hidden)});
      buildGrid();buildSteps();current=null;onScroll();
    };
    if(location.hash"""
assert old in h; h=h.replace(old,new,1)

# ---------- JS: world, ask, chrome ----------
js='''
  // Who's looking? Reorders the work and rewrites the intro for the visitor's world
  (function(){
    var W=__WORLDS__;
    var idx=document.getElementById('index'),cw=document.getElementById('cases'),tb=document.getElementById('rail-tabs');
    var thesis=document.getElementById('thesis'),wi=document.getElementById('work-intro');
    var chips=[].slice.call(document.querySelectorAll('.who button'));
    var clear=document.querySelector('.who .who-x');
    var orig={idx:[].slice.call(idx.children),arts:[].slice.call(cw.querySelectorAll(':scope>article.case')),tabs:[].slice.call(tb.children),thesis:thesis.textContent,wi:wi.textContent};
    function pad(n){return (n<10?'0':'')+n}
    function swapText(el,txt){if(el.textContent===txt)return;el.classList.add('swap');setTimeout(function(){el.textContent=txt;el.classList.remove('swap')},reduce?0:220)}
    function apply(w,save){
      var cfg=W[w]||null;world=cfg?w:null;
      if(cfg){
        var top=idx.querySelector('[data-w="top"]'),rest=idx.querySelector('[data-w="rest"]');
        top.querySelector('span').textContent='Most relevant to '+cfg.short;
        var items=cfg.order.map(function(id){return idx.querySelector('a[href="#'+id+'"]').parentNode});
        idx.appendChild(top);items.slice(0,cfg.top).forEach(function(li){idx.appendChild(li)});
        idx.appendChild(rest);items.slice(cfg.top).forEach(function(li){idx.appendChild(li)});
        [].forEach.call(idx.querySelectorAll('li.grp:not(.wgrp)'),function(g){idx.appendChild(g)});
        cfg.order.forEach(function(id){cw.appendChild(document.getElementById(id))});
        [].forEach.call(tb.querySelectorAll('.rail-grp'),function(g){tb.appendChild(g)});
        cfg.order.forEach(function(id,i){var t=tb.querySelector('a[data-case="'+id+'"]');t.querySelector('span').textContent=pad(i+1);tb.appendChild(t)});
        swapText(thesis,cfg.intro);
        swapText(wi,'Showing the work most relevant to '+cfg.short+' first, followed by the rest of my thirteen projects. Choose a project to jump to its story, or use the tabs that follow you down the page.');
      }else{
        orig.idx.forEach(function(li){idx.appendChild(li)});
        orig.arts.forEach(function(a){cw.appendChild(a)});
        var n=0;orig.tabs.forEach(function(t){if(t.tagName==='A'){n++;t.querySelector('span').textContent=pad(n)}tb.appendChild(t)});
        swapText(thesis,orig.thesis);swapText(wi,orig.wi);
      }
      chips.forEach(function(c){var d=c.getAttribute('data-w');if(d)c.setAttribute('aria-pressed',d===world?'true':'false')});
      clear.hidden=!world;
      refreshGroups();
      if(window.__nsRebuild)window.__nsRebuild();
      if(save){
        try{if(world)localStorage.setItem('ns-world',world);else localStorage.removeItem('ns-world')}catch(e){}
        try{var u=new URL(location.href);if(world)u.searchParams.set('for',world);else u.searchParams.delete('for');history.replaceState(null,'',u.pathname+u.search+u.hash)}catch(e){}
      }
    }
    chips.forEach(function(c){c.addEventListener('click',function(){var d=c.getAttribute('data-w');apply(d&&d!==world?d:null,true)})});
    var start=null;
    try{start=new URL(location.href).searchParams.get('for')}catch(e){}
    if(!W[start]){try{start=localStorage.getItem('ns-world')}catch(e){start=null}}
    if(W[start])apply(start,false);
  })();

  // Ask Nino: answers written from the CV and case studies, matched by keywords
  (function(){
    var QA=__QA__,FALL=__FALL__;
    var btn=document.getElementById('ask-btn'),panel=document.getElementById('ask'),x=document.getElementById('ask-x');
    var log=document.getElementById('ask-log'),sugg=document.getElementById('ask-sugg'),form=document.getElementById('ask-form'),input=document.getElementById('ask-in');
    var asked={},started=false;
    function norm(s){return ' '+s.toLowerCase().replace(/[’']/g,'').replace(/[^a-z0-9\\u00e0-\\u00ff.+ -]/g,' ').replace(/\\s+/g,' ').trim()+' '}
    function match(q){
      var t=norm(q),words={};t.trim().split(' ').forEach(function(w){words[w.replace(/[.?!,]+$/,'')]=1});
      var best=-1,score=0;
      QA.forEach(function(e,i){var s=0;e.k.forEach(function(k){if(k.indexOf(' ')>-1){if(t.indexOf(' '+k+' ')>-1||t.indexOf(k)>-1)s+=2}else if(words[k])s+=1});
        if(s>score){score=s;best=i}});
      return score>0?best:-1;
    }
    function add(cls,html){var d=document.createElement('div');d.className='ask-msg '+cls;d.innerHTML=html;log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
    function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
    function suggestions(){
      sugg.innerHTML='';var n=0;
      QA.forEach(function(e,i){if(asked[i]||n>=4)return;n++;var b=document.createElement('button');b.type='button';b.textContent=e.q;b.addEventListener('click',function(){ask(e.q,i)});sugg.appendChild(b)});
    }
    function ask(q,i){
      q=q.trim();if(!q)return;
      add('me',esc(q));
      if(i==null)i=match(q);
      setTimeout(function(){
        if(i>-1){asked[i]=1;add('nino',QA[i].a)}
        else add('nino',FALL+'<br><a class="ask-mail" href="mailto:sekelenin@gmail.com?subject='+encodeURIComponent('A question from your portfolio')+'&body='+encodeURIComponent(q+'\\n\\n')+'">Email this question</a>');
        suggestions();
      },reduce?0:280);
    }
    function open(){
      panel.hidden=false;btn.setAttribute('aria-expanded','true');
      if(!started){started=true;add('nino',"Hi, I'm Nino. Ask me anything a hiring manager might want to know, or tap one of the questions below.");suggestions()}
      setTimeout(function(){input.focus({preventScroll:true})},30);
    }
    function close(){panel.hidden=true;btn.setAttribute('aria-expanded','false');btn.focus({preventScroll:true})}
    btn.addEventListener('click',open);x.addEventListener('click',close);
    panel.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
    form.addEventListener('submit',function(e){e.preventDefault();var q=input.value;input.value='';ask(q)});
    log.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-j]');if(a&&window.innerWidth<=620)close()});
  })();

  // Brand colour beyond the page: browser bar and tab icon follow the current case
  (function(){
    var head=document.head||document.getElementsByTagName('head')[0];
    var meta=document.querySelector('meta[name="theme-color"]');
    if(!meta){meta=document.createElement('meta');meta.name='theme-color';head.appendChild(meta)}
    var icon=document.querySelector('link[rel="icon"]');
    if(!icon){icon=document.createElement('link');icon.rel='icon';icon.type='image/svg+xml';head.appendChild(icon)}
    var last='';
    function paint(){
      var cs=getComputedStyle(root),bg=cs.getPropertyValue('--ink').trim(),fg=cs.getPropertyValue('--gold').trim();
      var key=bg+'|'+fg;if(key===last)return;last=key;
      meta.setAttribute('content',bg);
      var svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="15" fill="'+bg+'"/><text x="32" y="45" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-weight="700" font-size="38" fill="'+fg+'">N</text></svg>';
      icon.href='data:image/svg+xml,'+encodeURIComponent(svg);
    }
    paint();
    if('MutationObserver' in window)new MutationObserver(function(){paint()}).observe(root,{attributes:true,attributeFilter:['data-case','data-mode']});
  })();
'''
js=js.replace('__WORLDS__',json.dumps({k:{kk:v[kk] for kk in ('short','top','order','intro')} for k,v in W.items()},ensure_ascii=False))
js=js.replace('__QA__',json.dumps(QA,ensure_ascii=False)).replace('__FALL__',json.dumps(FALLBACK))
anchor="\n  // Copy buttons"
assert anchor in h; h=h.replace(anchor,js+anchor,1)
open(P,'w').write(h); print('ok',len(h))
