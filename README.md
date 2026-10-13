# SafeVision AI — Complete Arabic Implementation Handbook

**SafeVision AI — AI-Powered Industrial Safety Management System**
الدليل العربي الشامل للتنفيذ: المعمارية، الـ Backend، الـ Frontend، قاعدة البيانات، دمج الـ AI، الاختبارات، والنشر.

Academic Year 2026–2027 · Graduation Project Documentation

## 📄 The deliverable

The finished handbook is a single PDF at the repository root:

```
SafeVision-AI-Implementation-Handbook-AR.pdf
```

It is written in Arabic (RTL) with English technical terminology preserved, contains 31 numbered
chapters (an introduction plus the 30 chapters of the specification), architecture diagrams,
database diagrams, wireframes, sequence diagrams, complete code examples, tables, checklists and
a clickable table of contents plus PDF bookmarks.

## 📁 Handbook sources

| Path | Purpose |
|---|---|
| `build/SPEC.md` | Authoritative specification: stack, database schema, API contract, enums, env vars. Every chapter follows it. |
| `build/CHAPTERS.md` | Per-chapter plan: title, kicker token, mandatory topics, page budget, required diagrams/code. |
| `build/AUTHORING.md` | HTML authoring rules and the allowed CSS class vocabulary. |
| `build/css/handbook.css` | The print design system (palette, typography, tables, code blocks, callouts, diagram primitives). |
| `build/content/ch00.html` … `ch30.html` | One HTML fragment per chapter. |
| `build/build.py` | Assembler + renderer + PDF post-processing (TOC page numbers, footers, bookmarks, TOC links). |
| `build/render.js` | Headless-Chromium renderer (injects the Arabic fonts, prints A4). |
| `build/check_chapter.py` | Validator for a chapter fragment (structure, tag balance, forbidden constructs, fabricated-metric guard). |
| `build/fonts/` | Cairo, Tajawal and JetBrains Mono (SIL Open Font License). |

## 🔧 Rebuilding the PDF

Requirements: Python 3.11, Node.js 20+, Chromium via Puppeteer, and an Arabic-capable font stack.

```bash
cd build
python3 -m http.server 8899 --bind 127.0.0.1 --directory . &   # serve the sources for the renderer
python3 build.py                                              # assemble -> render -> merge -> post-process
```

The build performs two render passes: the first discovers the printed page number of every chapter
so the table of contents can be filled in, the second renders the final document. Afterwards the
script merges the full-bleed cover, draws the footers (page number + Arabic chapter label), adds the
PDF outline/bookmarks and turns every table-of-contents row into an internal link.

Validate a single chapter before rebuilding:

```bash
python3 build/check_chapter.py 11
```

## ✅ Honesty rules used throughout the document

- No accuracy, mAP, FPS, latency or benchmark figure appears anywhere unless it was measured. Result
tables are shipped blank and marked _(يُملأ بعد التجربة)_.
- `MVP` and `Future` scope are separated explicitly in every scope table.
- Unknown values use visible placeholders such as `<PPE_MODEL_CHECKPOINT_PATH>`,
  `<UNIVERSITY_NAME>`, `<SUPERVISOR_NAME>` — never invented names or numbers.
- No credentials, no real worker identities, no dataset licences are claimed.
- Docker/hosting guidance tells the reader to verify current capabilities, pricing and free tiers
  against official documentation at deployment time.
