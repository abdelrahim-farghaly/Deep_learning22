// Renders an HTML document served over http://127.0.0.1:8899 to a PDF.
// Fonts are injected through the CSS Font Loading API because this sandbox has no
// system fonts and file:// font loading is blocked by CORS in headless Chromium.
const puppeteer = require('puppeteer');

const FONTS = [
  { family: 'Cairo',         file: '/fonts/Cairo.ttf',            weight: '200 1000' },
  { family: 'Tajawal',       file: '/fonts/Tajawal-Regular.ttf',  weight: '400' },
  { family: 'Tajawal',       file: '/fonts/Tajawal-Bold.ttf',     weight: '700' },
  { family: 'JetBrainsMono', file: '/fonts/JetBrainsMono.ttf',    weight: '100 800' },
];

async function attempt(rel, out) {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none',
           '--disable-crash-reporter', '--no-first-run', '--disable-extensions'],
  });
  try {
    const page = await browser.newPage();
    page.on('pageerror', e => console.error('PAGEERROR: ' + e.message));
    page.on('requestfailed', r => console.error('REQFAIL: ' + r.url()));
    await page.goto('http://127.0.0.1:8899/' + rel, { waitUntil: 'load', timeout: 600000 });
    await page.evaluate(async (fonts) => {
      for (const f of fonts) {
        const face = new FontFace(f.family, `url(${f.file})`, { weight: f.weight });
        await face.load();
        document.fonts.add(face);
      }
      await document.fonts.ready;
    }, FONTS);
    await new Promise(r => setTimeout(r, 800));
    const info = await page.evaluate(() => ({
      h: document.body.scrollHeight,
      fonts: [...document.fonts].map(f => `${f.family}:${f.status}`).join(','),
    }));
    console.error('INFO ' + JSON.stringify(info));
    await page.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  } finally {
    await browser.close().catch(() => {});
  }
}

(async () => {
  const rel = process.argv[2];
  const out = process.argv[3];
  for (let i = 1; i <= 3; i++) {
    try {
      await attempt(rel, out);
      console.log('OK ' + out);
      process.exit(0);
    } catch (e) {
      console.error('attempt ' + i + ' failed: ' + (e && e.message));
      await new Promise(r => setTimeout(r, 3000));
    }
  }
  console.error('render failed after 3 attempts: ' + rel);
  process.exit(1);
})();
