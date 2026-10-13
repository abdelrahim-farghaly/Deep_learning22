const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
  const p = await b.newPage();
  await p.goto('http://127.0.0.1:8899/dbg.html', {waitUntil:'networkidle0'});
  const out = await p.evaluate(async () => {
    const res = {};
    for (const [name, url] of [['TAJ','/fonts/Tajawal-Regular.ttf'],['CAI','/fonts/Cairo.ttf'],['NK','/fonts/NotoNaskhArabic.ttf']]) {
      try {
        const ff = new FontFace('T_'+name, `url(${url})`);
        await ff.load();
        res[name] = 'ok';
      } catch (e) { res[name] = 'ERR ' + (e && e.message) + ' / ' + (e && e.name); }
    }
    return res;
  });
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
