const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file:///home/claude/prog/programme.html');await p.waitForTimeout(1200);
await p.evaluate(()=>document.fonts.ready);
const ff=await p.evaluate(()=>[...document.fonts].map(f=>f.family+':'+f.status));console.log(ff);
await p.pdf({path:'/home/claude/prog/nino-sekeleni-programme.pdf',preferCSSPageSize:true,printBackground:true});
await b.close()})();
