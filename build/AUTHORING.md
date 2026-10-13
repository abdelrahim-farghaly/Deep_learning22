# AUTHORING GUIDE — how to write a chapter fragment

You write ONE file per chapter: `/workspace/build/content/chNN.html` (NN = 01..30).
The file contains ONLY the inner HTML of the chapter (no <html>, <head>, <body>, no <style>).
A build script wraps it. Start the file with the `.chapter` wrapper and the opener.

## Exact chapter skeleton
```html
<section class="chapter" id="ch07">
  <div class="opener">
    <div class="op-num">07</div>
    <div class="op-txt">
      <p class="op-kicker">CH07 &middot; API CONTRACT</p>
      <h2>تصميم الـ API وتوثيق الـ Endpoints</h2>
      <p class="op-sub">سطر واحد يلخّص الفصل</p>
    </div>
  </div>

  <div class="lead"><p>فقرة تمهيدية قصيرة: ماذا سيتعلم الفريق في هذا الفصل ولماذا يهم.</p></div>

  <h3>7.1 عنوان القسم</h3>
  <p>...</p>
  ...

  <div class="eoc">
    <div class="eoc-head">خلاصة الفصل 7</div>
    <div class="eoc-body">
      <div class="eoc-row"><h4>ما تعلّمناه</h4><p>...</p></div>
      <div class="eoc-row"><h4>ما يجب تنفيذه</h4><ul class="checklist"><li>...</li></ul></div>
      <div class="eoc-row"><h4>المخرجات المتوقعة</h4><ul><li>...</li></ul></div>
      <div class="eoc-row"><h4>كيف نتحقق من الإنجاز</h4><ul><li>...</li></ul></div>
      <div class="eoc-row"><h4>أخطاء شائعة</h4><ul><li>...</li></ul></div>
    </div>
  </div>
</section>
```
The `CH07` token inside `.op-kicker` is REQUIRED and unique per chapter (used to build the TOC).
Section numbers MUST match the chapter number (7.1, 7.2, ...).

## Available CSS classes (use only these)
- Text: `p`, `ul`, `ol`, `li`, `strong`, `em`, `span.en` (English term), `code`, `.small`, `.center`
- Headings: `h3` (main section), `h4`, `h5`
- `div.lead` — intro box
- Tables: `<table class="tbl"><caption>..</caption><thead><tr><th>..</th></tr></thead><tbody>...`
  Use `<td class="c">` for centered cells, `<td class="mono">` for identifiers, `.mono` spans.
- Code: 
```html
<div class="code-wrap"><div class="code-head"><span class="fname">backend/app/main.py</span><span class="ftag">python</span></div>
<pre>code here, English comments only</pre></div>
```
  Add class `long` (`code-wrap long`) for blocks taller than ~half a page so they can split.
  Terminal blocks: `<pre class="term">$ command</pre>` (still inside `.code-wrap`).
  Optional syntax spans inside `<pre>`: `<span class="kw">`, `.str`, `.num`, `.fn`, `.cmt`.
  IMPORTANT: inside `<pre>` escape `<` as `&lt;` and `>` as `&gt;` and `&` as `&amp;`.
- Callouts: `<div class="callout warn"><span class="co-title">تحذير</span><p>...</p></div>`
  variants: `info` (teal, معلومات), `warn` (orange, تحذير), `danger` (red, خطر), `tip` (green, نصيحة),
  `example` (violet, مثال عملي), `note` (رمادي).
- Checklists: `<ul class="checklist">`
- Badges: `<span class="badge mvp">MVP</span>`, `.future` (مستقبلي), `.opt` (اختياري), `.req` (مطلوب)
- Cards: `<div class="grid2">` / `.grid3` containing `<div class="card">` (variants `.navy .orange .red .green`)
- Figures: `<div class="fig"><div class="dg">...</div><div class="fig-cap"><b>شكل 2-1:</b> وصف</div></div>`
- Diagram primitives inside `.dg`:
  - `<div class="drow">` row of boxes, `<div class="dcol">` column
  - `<div class="dbox navy">نص<span class="dsub">تفصيل</span><span class="dtag">API</span></div>`
    variants: `navy teal orange red green violet gray dash`
  - `<div class="darrow"></div>` vertical arrow down; `.darrow.teal` / `.darrow.orange`
  - `<div class="darrow-h"></div>` horizontal arrow (points left in RTL)
  - `<div class="dline"></div>` plain connector line; `<div class="dlabel">text</div>`
  - `<div class="dgroup"><div class="dg-title">عنوان المجموعة</div> ... </div>`
- Sequence diagram: `<table class="seq">` with `<th>` actor columns, rows `<td class="actor">..</td><td class="msg">..</td>`
  and `<span class="mt">GET /api/v1/videos</span>` inside a `.msg` cell. `.sync` / `.async` row tint.
- ER diagram: `<div class="er">` containing `<div class="er-table"><div class="er-name">videos</div><ul><li class="pk">id</li>...</ul></div>`
  classes on li: `pk`, `fk`, `mut`. Variants on the table: `alt` (teal header), `late` (grey header).
- Wireframes: `<div class="wf"><div class="wf-top">..</div><div class="wf-body"><div class="wf-side">..</div><div class="wf-main"><div class="wf-row solid">..</div></div></div></div>`
- Utilities: `.pb` (page break before), `.nobreak`, `.sep` (hr)

## Hard rules
1. Only the classes listed above. No inline `style=` attributes. No external images.
2. Do NOT write `<html>`, `<body>`, `<h1>`, `<h2>` (except inside `.opener`).
3. Every code block must state its filename in `.code-head` and the text must explain where the file lives.
4. Prose in Arabic; identifiers/code/commands in English. Never Arabic inside `<pre>`.
5. Do not invent results: no accuracy/mAP/FPS numbers. Use blank result tables with a `(يُملأ بعد التجربة)` note.
6. Keep the SPEC.md names EXACTLY (routes, fields, env vars, enums).
7. Escape `&`, `<`, `>` correctly. Use `&middot;`, `&rarr;` (avoid), `&larr;` where useful.
8. Aim for the requested page budget: roughly 450-650 Arabic words per printed page; a chapter of
   3 pages is ~1400-1900 words plus tables/code.
9. No fabricated links. Link only to official documentation roots you are confident about
   (docs.python.org, fastapi.tiangolo.com, react.dev, vitejs.dev, postgresql.org/docs,
   docs.sqlalchemy.org, alembic.sqlalchemy.org, docs.docker.com, docs.opencv.org, pytorch.org/docs,
   docs.ultralytics.com, nodejs.org/docs, tailwindcss.com/docs, recharts.org, www.typescriptlang.org/docs).
10. Write the file with a single `cat > /workspace/build/content/chNN.html <<'HTMLEOF' ... HTMLEOF` shell
    command (or several appends). Do not use the editor tool for very large payloads.
