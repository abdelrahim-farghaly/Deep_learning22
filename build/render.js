// Renders an HTML document served over http://127.0.0.1:8899 to a PDF.
// Fonts are injected through the CSS Font Loading API because this sandbox has no
// system fonts and file:// font loading is blocked by CORS in headless Chromium.
const puppeteer = require('puppeteer');
const path = require('path');

const FONTS = [
  { family: 'Cairo',         file: '/fonts/Cairo.ttf',            weight: '200 1000' },
  { family: 'Tajawal',       file: '/fonts/Tajawal-Regular.ttf',  weight: '400' },
  { family: 'Tajawal',       file: '/fonts/Tajawal-Bold.ttf',     weight: '700' },
  { family: 'JetBrainsMono', file: '/fonts/JetBrainsMono.ttf',    weight: '100 800' },
];

(async () => {
  const rel = process.argv[2];
  const out = process.argv[3];
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  page.on('pageerror', e => console.error('PAGEERROR:', e.message));
  await page.goto('http://127.0.0.1:8899/' + rel, { waitUntil: 'networkidle0', timeout: 300000 });
  await page.evaluate(async (fonts) => {
    for (const f of fonts) {
      const face = new FontFace(f.family, `url(${f.file})`, { weight: f.weight });
      await face.load();
      document.fonts.add(face);
    }
    await document.fonts.ready;
  }, FONTS);
  await new Promise(r => setTimeout(r, 600));
  const info = await page.evaluate(() => ({
    h: document.body.scrollHeight,
    w: document.body.scrollWidth,
    fonts: [...document.fonts].map(f => `${f.family}:${f.weight}:${f.status}`),
  }));
  console.error('INFO ' + JSON.stringify(info));
  await page.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('OK ' + out);
})();
