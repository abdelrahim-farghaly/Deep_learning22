#!/usr/bin/env python3
"""Validate a chapter HTML fragment against the handbook authoring rules."""
import re, sys, os

VOID = {'br', 'hr', 'img', 'input', 'meta', 'link'}
TAGS = ['div', 'section', 'table', 'caption', 'thead', 'tbody', 'tr', 'th', 'td', 'ul', 'ol', 'li',
        'pre', 'span', 'p', 'strong', 'em', 'h3', 'h4', 'h5', 'code']
ARABIC = re.compile(r'[\u0600-\u06ff]')


def main(n):
    path = '/workspace/build/content/ch%02d.html' % n
    if not os.path.exists(path):
        print('MISSING', path); return 1
    s = open(path, encoding='utf-8').read()
    errs, warns = [], []

    if not re.search(r'<div class="op-num">\s*%02d\s*</div>' % n, s):
        errs.append('opener op-num must be %02d' % n)
    if ('CH%02d' % n) not in s:
        errs.append('missing kicker token CH%02d' % n)
    if s.count('<section') != 1 or s.count('</section>') != 1:
        errs.append('must contain exactly one <section>...</section>')
    if 'id="ch%02d"' % n not in s:
        errs.append('section must have id="ch%02d"' % n)
    if 'class="eoc"' not in s:
        errs.append('missing .eoc end-of-chapter block')
    for label in ['ما تعلّمناه', 'ما يجب تنفيذه', 'المخرجات المتوقعة', 'كيف نتحقق من الإنجاز', 'أخطاء شائعة']:
        if label not in s:
            warns.append('eoc row missing: ' + label)
    if 'style=' in s:
        errs.append('inline style= attribute found (not allowed)')

    for t in TAGS:
        o = len(re.findall(r'<%s(?=[\s>])' % t, s))
        c = len(re.findall(r'</%s>' % t, s))
        if o != c:
            errs.append('tag imbalance <%s>: %d open / %d close' % (t, o, c))

    for i, m in enumerate(re.finditer(r'<pre[^>]*>(.*?)</pre>', s, re.S)):
        if ARABIC.search(m.group(1)):
            errs.append('Arabic text inside <pre> block #%d (must be English only)' % (i + 1))

    for m in re.finditer(r'<h3>(.*?)</h3>', s, re.S):
        txt = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if not re.match(r'^%d\.[0-9]+' % n, txt):
            errs.append('h3 does not start with %d.x : %s' % (n, txt[:40]))

    body = re.sub(r'<pre.*?</pre>', ' ', s, flags=re.S)
    words = len(re.findall(r'[\u0600-\u06ff]+', body))
    if words < 700:
        warns.append('only ~%d Arabic words - check the page budget' % words)
    sus = re.findall(r'(?:accuracy|mAP|FPS|دقة|سرعة المعالجة)[^.<>]{0,30}?\b\d+(?:\.\d+)?\s*%', s)
    if sus:
        warns.append('possible fabricated metric: ' + ' | '.join(sus[:3]))

    print('== ch%02d.html ==  arabic words ~%d  figures=%d  tables=%d  code blocks=%d'
          % (n, words, s.count('class="fig"'), s.count('class="tbl"'), s.count('class="code-wrap')))
    for e in errs:
        print('  ERROR:', e)
    for w in warns:
        print('  warn :', w)
    print('  RESULT:', 'FAIL' if errs else 'OK')
    return 1 if errs else 0


if __name__ == '__main__':
    ns = [int(a) for a in sys.argv[1:]] or list(range(1, 31))
    bad = 0
    for n in ns:
        bad += main(n)
    sys.exit(1 if bad else 0)
