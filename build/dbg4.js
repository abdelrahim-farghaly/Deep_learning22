const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
  const p = await b.newPage();
  await p.setViewport({width:900,height:400});
  await p.goto('http://127.0.0.1:8899/blank.html', {waitUntil:'networkidle0'});
  await p.evaluate(async () => {
    const defs = [['TAJ','/fonts/Tajawal-Regular.ttf'],['CAI','/fonts/Cairo.ttf'],['NK','/fonts/NotoNaskhArabic.ttf']];
    for (const [name,url] of defs) {
      const ff = new FontFace(name, `url(${url})`);
      await ff.load();
      document.fonts.add(ff);
    }
    document.body.innerHTML = '<div style="font-family:TAJ;font-size:26px" dir=rtl>مرحبا Tajawal 123 — Test</div>'
      + '<div style="font-family:CAI;font-size:26px" dir=rtl>مرحبا Cairo — اختبار 456</div>'
      + '<div style="font-family:NK;font-size:26px" dir=rtl>مرحبا Naskh — اختبار 789</div>';
  });
  await new Promise(r=>setTimeout(r,300));
  await p.screenshot({path:'/workspace/build/dbg4.png'});
  await b.close();
})();
