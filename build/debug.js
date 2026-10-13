const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--allow-file-access-from-files']});
  const p = await b.newPage();
  p.on('console', m => console.log('PAGE:', m.text()));
  p.on('requestfailed', r => console.log('REQFAIL:', r.url(), r.failure() && r.failure().errorText));
  await p.setContent(`<html dir=rtl><head><meta charset=utf-8><style>
  @font-face{font-family:TAJ;src:url('file:///workspace/build/fonts/Tajawal-Regular.ttf') format('truetype')}
  @font-face{font-family:CAI;src:url('file:///workspace/build/fonts/Cairo.ttf') format('truetype')}
  #a{font-family:TAJ;font-size:24px}#b{font-family:CAI;font-size:24px}
  </style></head><body><div id=a>مرحبا Tajawal</div><div id=b>مرحبا Cairo</div></body></html>`);
  await p.evaluate(()=>document.fonts.ready);
  const r = await p.evaluate(()=>({
    taj: document.fonts.check('24px TAJ'),
    cai: document.fonts.check('24px CAI'),
    loaded: [...document.fonts].map(f=>f.family+':'+f.status),
    wa: document.getElementById('a').getBoundingClientRect().width,
    wb: document.getElementById('b').getBoundingClientRect().width
  }));
  console.log(JSON.stringify(r,null,1));
  await b.close();
})();
