const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
  const p = await b.newPage();
  p.on('console', m => console.log('PAGE:', m.text()));
  p.on('requestfailed', r => console.log('REQFAIL:', r.url(), r.failure()&&r.failure().errorText));
  p.on('response', r => { if(r.url().includes('.ttf')) console.log('RESP', r.status(), r.url(), r.headers()['content-type']); });
  await p.goto('http://127.0.0.1:8899/dbg.html', {waitUntil:'networkidle0'});
  await p.evaluate(()=>document.fonts.ready);
  console.log(JSON.stringify(await p.evaluate(()=>({fonts:[...document.fonts].map(f=>f.family+':'+f.status), taj:document.fonts.check('24px TAJ'), cai:document.fonts.check('24px CAI'), nk:document.fonts.check('24px NK')})),null,1));
  await b.close();
})();
