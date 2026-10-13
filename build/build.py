#!/usr/bin/env python3
"""Assemble the SafeVision AI Arabic handbook, render it and post-process the PDF."""
import json, os, re, subprocess, sys

BUILD = '/workspace/build'
CONTENT = os.path.join(BUILD, 'content')
TOTAL_CH = 30


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def write(p, t):
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(t)


def collect():
    frags, metas = [], []
    for n in range(0, TOTAL_CH + 1):
        p = os.path.join(CONTENT, 'ch%02d.html' % n)
        if not os.path.exists(p):
            print('  [missing] ch%02d.html' % n)
            continue
        html = read(p)
        frags.append(html)
        m = {'num': n}
        g = lambda pat: (re.search(pat, html, re.S).group(1) if re.search(pat, html, re.S) else '')
        m['opnum'] = re.sub(r'<[^>]+>', '', g(r'<div class="op-num">(.*?)</div>')).strip() or '%02d' % n
        m['kicker'] = re.sub(r'<[^>]+>', '', g(r'<p class="op-kicker">(.*?)</p>')).strip()
        m['title'] = re.sub(r'<[^>]+>', '', g(r'<div class="op-txt">.*?<h2>(.*?)</h2>')).strip()
        m['sub'] = re.sub(r'<[^>]+>', '', g(r'<p class="op-sub">(.*?)</p>')).strip()
        m['sections'] = [re.sub(r'<[^>]+>', '', s).strip() for s in re.findall(r'<h3>(.*?)</h3>', html, re.S)]
        metas.append(m)
    return frags, metas


def build_toc(metas, pages=None):
    rows = ['<div class="toc-sec"><div class="toc-title">فهرس المحتويات</div>',
            '<p class="small">أرقام الصفحات تشير إلى ترقيم صفحات المحتوى. يمكنك أيضاً استخدام لوحة الـ '
            'Bookmarks في قارئ الـ PDF للانتقال السريع بين الفصول.</p>', '<ul class="toc">']
    for m in metas:
        pg = str(pages.get(m['num'], '')) if pages else '&nbsp;'
        rows.append('<li><span class="t-num">%s</span><span class="t-txt">%s'
                    '<span class="xmk">TOC%02d</span></span><span class="t-pg">%s</span></li>'
                    % (m['opnum'], m['title'] or m['kicker'], m['num'], pg))
        # Section-level entries are intentionally omitted from the printed TOC to keep it
        # compact; navigation to sections is available through the PDF outline/bookmarks.
    rows.append('</ul></div>')
    return '\n'.join(rows)


def build_content(toc, frags):
    head = ('<!doctype html><html dir="rtl" lang="ar"><head><meta charset="utf-8">'
            '<title>SafeVision AI - Implementation Handbook</title>'
            '<link rel="stylesheet" href="/css/handbook.css"></head><body>')
    return head + toc + '\n'.join(frags) + '</body></html>'


def render(rel, out):
    r = subprocess.run([os.path.join(BUILD, 'runrender.sh'), rel, out], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2500:]); print(r.stderr[-2500:]); raise SystemExit('render failed: ' + rel)
    for line in r.stderr.splitlines():
        if line.startswith('INFO') or line.startswith('PAGEERROR') or line.startswith('REQFAIL'):
            print('  ' + line[:300])
    return r


def chapter_pages(pdf_path):
    """Return {chapter_number: printed_page_number} using the CHxx kicker tokens."""
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    out = {}
    for i, page in enumerate(reader.pages):
        try:
            txt = page.extract_text() or ''
        except Exception:
            txt = ''
        for n in range(0, TOTAL_CH + 1):
            if n in out:
                continue
            if 'CH%02d' % n in txt.replace(' ', ''):
                out[n] = i + 1
    return out


COVER = '''<!doctype html><html dir="rtl" lang="ar"><head><meta charset="utf-8">
<style>
@page{size:A4;margin:0;}
*{box-sizing:border-box;}
body{margin:0;padding:0;font-family:"Cairo",sans-serif;direction:rtl;}
.cv{width:210mm;height:297mm;position:relative;overflow:hidden;
    background:linear-gradient(160deg,#071a33 0%,#0b2545 45%,#123a63 100%);color:#fff;}
.cv .grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);
  background-size:26px 26px;}
.cv .glow{position:absolute;width:420px;height:420px;border-radius:50%;
  background:radial-gradient(circle,rgba(15,139,158,.55) 0%,rgba(15,139,158,0) 70%);
  top:-140px;left:-120px;}
.cv .glow2{position:absolute;width:520px;height:520px;border-radius:50%;
  background:radial-gradient(circle,rgba(23,162,184,.28) 0%,rgba(23,162,184,0) 70%);
  bottom:-220px;right:-160px;}
.cv .bar{position:absolute;top:0;right:0;left:0;height:9px;
  background:linear-gradient(90deg,#0f8b9e 0%,#17a2b8 45%,#d97706 100%);}
.cv .inner{position:absolute;inset:0;padding:26mm 20mm 20mm 20mm;display:flex;flex-direction:column;}
.cv .kicker{font-family:"JetBrainsMono",monospace;direction:ltr;text-align:left;font-size:8.5pt;
  letter-spacing:3px;color:#7fd8e6;text-transform:uppercase;}
.cv h1{font-family:"Tajawal",sans-serif;font-size:47pt;line-height:1.06;margin:7mm 0 0 0;color:#fff;font-weight:700;}
.cv h1 .ai{color:#2fd0e8;}
.cv .ar-title{font-family:"Tajawal",sans-serif;font-size:16.5pt;color:#e8f4fb;margin:4mm 0 0 0;font-weight:400;}
.cv .rule{width:64mm;height:4px;background:#0f8b9e;border-radius:3px;margin:7mm 0 6mm 0;}
.cv .doc{font-size:20pt;font-family:"Tajawal",sans-serif;color:#fff;font-weight:700;}
.cv .pipe{margin-top:4mm;font-size:10.5pt;color:#bfe3ee;line-height:2;}
.cv .pipe b{color:#2fd0e8;font-weight:700;}
.cv .chips{margin-top:8mm;display:flex;flex-wrap:wrap;gap:6px;}
.cv .chip{border:1px solid rgba(127,216,230,.55);border-radius:20px;padding:2px 11px;font-size:9pt;
  color:#d9f2f8;font-family:"JetBrainsMono",monospace;direction:ltr;}
.cv .spacer{flex:1 1 auto;}
.cv .inside{background:rgba(255,255,255,.055);border:1px solid rgba(127,216,230,.3);border-radius:10px;padding:6mm 7mm;}
.cv .inside-title{font-family:"Tajawal",sans-serif;font-weight:700;font-size:12pt;color:#2fd0e8;margin-bottom:3mm;}
.cv .inside-grid{display:grid;grid-template-columns:1fr 1fr;gap:2mm 8mm;font-size:10pt;color:#dceaf5;}
.cv .inside-grid div::before{content:"\25AA";color:#0f8b9e;margin-inline-end:6px;}
.cv .meta{border-top:1px solid rgba(255,255,255,.22);padding-top:5mm;font-size:10.5pt;color:#dbe9f4;line-height:1.95;}
.cv .meta .row{display:flex;gap:8px;}
.cv .meta .k{color:#7fd8e6;min-width:44mm;font-family:"Tajawal",sans-serif;font-weight:700;}
.cv .ph{color:#f0b46b;font-family:"JetBrainsMono",monospace;font-size:9.5pt;direction:ltr;}
.cv .foot{position:absolute;bottom:8mm;left:20mm;right:20mm;font-size:8.5pt;color:#8fb4cc;
  display:flex;justify-content:space-between;font-family:"JetBrainsMono",monospace;direction:ltr;}
</style></head><body>
<div class="cv"><div class="grid"></div><div class="glow"></div><div class="glow2"></div><div class="bar"></div>
 <div class="inner">
  <div class="kicker">Graduation Project &middot; Software Implementation Handbook</div>
  <h1>SafeVision <span class="ai">AI</span></h1>
  <div class="ar-title">نظام ذكي لإدارة السلامة الصناعية بالاعتماد على الرؤية الحاسوبية</div>
  <div class="rule"></div>
  <div class="doc">الدليل العربي الشامل للتنفيذ</div>
  <div class="pipe"><b>Backend</b> &middot; <b>Frontend</b> &middot; <b>Database</b> &middot; <b>AI Integration</b> &middot; <b>Testing</b> &middot; <b>Deployment</b><br>
    المعمارية الكاملة &middot; الـ API &middot; قاعدة البيانات &middot; خط معالجة الفيديو &middot; الواجهة &middot; النشر &middot; خطة الفريق</div>
  <div class="chips"><span class="chip">Python</span><span class="chip">FastAPI</span><span class="chip">PostgreSQL</span>
   <span class="chip">SQLAlchemy</span><span class="chip">React</span><span class="chip">TypeScript</span>
   <span class="chip">OpenCV</span><span class="chip">PyTorch</span><span class="chip">Docker</span><span class="chip">Alembic</span></div>
  <div class="spacer"></div>
  <div class="inside">
    <div class="inside-title">ما يغطّيه هذا الدليل</div>
    <div class="inside-grid">
      <div>المعمارية الكاملة للنظام والـ AI Pipeline</div>
      <div>الـ Backend بـ FastAPI والـ API Contract</div>
      <div>قاعدة البيانات و PostgreSQL و Alembic</div>
      <div>دمج الـ Models وخط معالجة الفيديو</div>
      <div>واجهة React وربطها بالـ API</div>
      <div>الاختبارات و Docker والنشر وخطة الفريق</div>
    </div>
  </div>
  <div class="spacer"></div>
  <div class="meta">
   <div class="row"><span class="k">التوثيق</span><span>وثائق مشروع التخرّج</span></div>
   <div class="row"><span class="k">إعداد</span><span>فريق مشروع التخرّج &mdash; Graduation Project Team</span></div>
   <div class="row"><span class="k">القسم</span><span>قسم علوم الحاسب / الذكاء الاصطناعي</span></div>
   <div class="row"><span class="k">الجامعة</span><span class="ph">&lt;UNIVERSITY_NAME&gt;</span></div>
   <div class="row"><span class="k">إشراف</span><span class="ph">&lt;SUPERVISOR_NAME&gt;</span></div>
   <div class="row"><span class="k">العام الدراسي</span><span>2026 &ndash; 2027</span></div>
  </div>
 </div>
 <div class="foot"><span>SafeVision AI</span><span>v1.0 &middot; Implementation Handbook</span></div>
</div></body></html>'''


def merge_pdfs(paths, out):
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    for p in paths:
        for pg in PdfReader(p).pages:
            w.add_page(pg)
    with open(out, 'wb') as fh:
        w.write(fh)


def add_footers(pdf_in, pdf_out, metas, page_map):
    """Draw a footer rule + Latin page number + Arabic chapter label on every page except the cover."""
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import io
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        pdfmetrics.registerFont(TTFont('ArFooter', os.path.join(BUILD, 'fonts', 'Tajawal-Regular.ttf')))
        have_ar = True
    except Exception as exc:  # pragma: no cover
        print('  [footer] arabic font unavailable:', exc)
        have_ar = False

    starts = sorted(page_map.items(), key=lambda kv: kv[1])
    reader = PdfReader(pdf_in)
    n = len(reader.pages)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    W, H = A4
    for i in range(n):
        printed = i  # cover is merged page 0 (unprinted); content pages start at 1
        if i == 0:
            c.showPage()
            continue
        c.setStrokeColorRGB(0.78, 0.82, 0.87)
        c.setLineWidth(0.6)
        c.line(45, 40, W - 45, 40)
        c.setFont('Helvetica', 7)
        c.setFillColorRGB(0.35, 0.40, 0.46)
        c.drawString(45, 30, 'SafeVision AI  |  Complete Arabic Implementation Handbook')
        c.drawRightString(W - 45, 30, 'Page %d' % printed)
        label = ''
        cur = None
        for num, pg in starts:
            if pg <= printed:
                cur = num
        if cur is not None:
            meta = next((m for m in metas if m['num'] == cur), None)
            if meta:
                label = (meta['title'] if meta['num'] == 0 else 'الفصل %s \u2014 %s' % (meta['opnum'], meta['title']))
        elif printed >= 1:
            label = 'فهرس المحتويات'
        if label and have_ar:
            try:
                shaped = get_display(arabic_reshaper.reshape(label))
                c.setFont('ArFooter', 7.2)
                c.setFillColorRGB(0.07, 0.15, 0.27)
                c.drawCentredString(W / 2.0, 30, shaped)
            except Exception as exc:
                print('  [footer] shape failed:', exc)
        c.showPage()
    c.save()
    buf.seek(0)
    overlay = PdfReader(buf)
    w = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i < len(overlay.pages):
            page.merge_page(overlay.pages[i])
        w.add_page(page)
    with open(pdf_out, 'wb') as fh:
        w.write(fh)


def finish(pdf_in, pdf_out, metas, page_map):
    """Add PDF bookmarks and in-page links from the TOC rows to the chapter start pages."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    reader = PdfReader(pdf_in)
    writer = PdfWriter(clone_from=pdf_in)
    try:
        writer.add_outline_item('الغلاف', 0)
        writer.add_outline_item('فهرس المحتويات', 1)
        for m in metas:
            pg = page_map.get(m['num'])
            if pg is not None and pg < len(reader.pages):
                lbl = (m['title']) if m['num'] == 0 else ('الفصل %s - %s' % (m['opnum'], m['title']))
                writer.add_outline_item(lbl, pg)
    except Exception as exc:
        print('  [outline] failed:', exc)

    # locate the invisible TOCxx markers inside the TOC pages and link each row
    try:
        import pymupdf
        from pypdf.annotations import Link
        doc = pymupdf.open(pdf_in)
        hits = {}
        for i in range(min(10, len(doc))):
            for blk in doc[i].get_text('dict').get('blocks', []):
                for line in blk.get('lines', []):
                    flat = ''.join(sp.get('text', '') for sp in line.get('spans', [])).replace(' ', '')
                    mt = re.search(r'TOC(\d{2})', flat)
                    if mt:
                        num = int(mt.group(1))
                        hits.setdefault(num, (i, line['bbox']))
        added = 0
        for num, (pi, bbox) in hits.items():
            target = page_map.get(num)
            if target is None or target >= len(reader.pages):
                continue
            rect = RectangleObject((45, bbox[1] - 3, 550, bbox[3] + 5))
            writer.add_annotation(page_number=pi, annotation=Link(rect=rect, target_page_index=target))
            added += 1
        print('  [links] %d TOC links added' % added)
    except Exception as exc:
        print('  [links] skipped:', exc)

    with open(pdf_out, 'wb') as fh:
        writer.write(fh)


def main():
    out_final = '/workspace/SafeVision-AI-Implementation-Handbook-AR.pdf'
    write(os.path.join(BUILD, 'cover.html'), COVER)
    render('cover.html', os.path.join(BUILD, 'cover.pdf'))
    frags, metas = collect()
    print('chapters found: %d' % len(metas))

    write(os.path.join(BUILD, 'content.html'), build_content(build_toc(metas, None), frags))
    render('content.html', os.path.join(BUILD, 'content_pass1.pdf'))
    pm = chapter_pages(os.path.join(BUILD, 'content_pass1.pdf'))
    print('page map pass1:', pm)

    write(os.path.join(BUILD, 'content.html'), build_content(build_toc(metas, pm), frags))
    render('content.html', os.path.join(BUILD, 'content.pdf'))
    pm2 = chapter_pages(os.path.join(BUILD, 'content.pdf'))
    if pm2 != pm:
        print('page map shifted, re-rendering once more')
        pm = pm2
        write(os.path.join(BUILD, 'content.html'), build_content(build_toc(metas, pm), frags))
        render('content.html', os.path.join(BUILD, 'content.pdf'))
        pm2 = chapter_pages(os.path.join(BUILD, 'content.pdf'))
    print('page map final:', pm2)

    merge_pdfs([os.path.join(BUILD, 'cover.pdf'), os.path.join(BUILD, 'content.pdf')],
               os.path.join(BUILD, 'merged.pdf'))
    add_footers(os.path.join(BUILD, 'merged.pdf'), os.path.join(BUILD, 'footed.pdf'), metas, pm2)
    finish(os.path.join(BUILD, 'footed.pdf'), out_final, metas, pm2)
    from pypdf import PdfReader
    r = PdfReader(out_final)
    print('FINAL: %s  pages=%d  size=%.2f MB' % (out_final, len(r.pages),
          os.path.getsize(out_final) / 1048576.0))
    json.dump(pm2, open(os.path.join(BUILD, 'pagemap.json'), 'w'), ensure_ascii=False)


if __name__ == '__main__':
    main()
