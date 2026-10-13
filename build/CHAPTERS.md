# CHAPTER PLAN — exact titles, kicker tokens and mandatory content
Each chapter file must use EXACTLY the kicker token and title below, and must cover every listed
topic. Organise the listed topics into numbered `h3` sections (`N.1`, `N.2`, ...).
Target length is given in printed pages (A4, ~500 Arabic words per full page of body text plus tables/code).

---
## CH02 — `CH02 &middot; SYSTEM ARCHITECTURE` — البنية الكاملة للنظام  (~4 pages)
Sub: من رفع الفيديو حتى التقرير: المكوّنات ومسؤولياتها واتجاه التواصل
Topics: المكوّنات العشرة (Video Upload Interface, Frontend, FastAPI Backend, Video Processing Service,
AI Inference Components, Safety Rules Engine, Background Job Processing, PostgreSQL, Evidence/Video
Storage, Reporting Module, Optional Notifications)؛ مسؤولية كل مكوّن؛ اتجاه التواصل؛
الفرق بين الطلب المتزامن (Synchronous) والوظيفة غير المتزامنة (Asynchronous job)؛
لماذا Modular Monolith أفضل من Microservices لفريق طلابي؛ جدول المكوّنات.
DIAGRAMS REQUIRED: (1) High-Level System Architecture; (2) Backend Component Architecture;
(3) AI Processing Pipeline; (4) Frontend↔Backend Communication; (5) Incident & Evidence Data Flow.
Use `.fig` + `.dg` primitives. Make sure the diagrams are readable and consistently coloured.

## CH03 — `CH03 &middot; TECHNOLOGY STACK` — حزمة التقنيات واختيار الأدوات  (~3 pages)
Sub: لماذا اخترنا كل أداة، وما البدائل، وما هو مطلوب في الـ MVP
Topics: لكل تقنية (ما تفعله، لماذا نحتاجها، من يستخدمها، MVP أم اختياري، البديل) — Python, PyTorch,
Ultralytics YOLO, OpenCV, ByteTrack, NumPy, Pandas, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL,
JWT, background jobs, polling/WebSocket, React, TypeScript, Vite, Tailwind CSS, Recharts, Axios,
Git/GitHub, VS Code, venv, Node/npm, Docker, Docker Compose, GitHub Actions.
جدول مقارنة التقنيات. قسم صريح: ما لا نستخدمه في الـ MVP ولماذا (Kubernetes, Kafka, Redis, Celery،
Microservices، البث المباشر) وتكلفة كل منها. ملاحظة أن أرقام الإصدارات يجب التحقق منها من المصادر الرسمية.

## CH04 — `CH04 &middot; REPOSITORY LAYOUT` — هيكل المستودع وتنظيم المجلدات  (~3 pages)
Sub: أين يوضع كل ملف، وما لا يجب أن يدخل Git أبداً
Topics: شجرة المجلدات الكاملة (استخدم شجرة backend/frontend/models/data/storage/docs/scripts كما في SPEC)؛
وظيفة كل مجلد مهم؛ ما يحتوي بيانات كبيرة محلية وما يُستثنى من Git؛ لماذا لا نرفع الفيديوهات والدليل إلى GitHub؛
ملف `.gitignore` كامل؛ ملف `.env.example` بقيم Placeholder فقط؛ اتفاقيات تسمية الملفات والفروع.
CODE: `.gitignore` و `.env.example` (كاملان).

## CH05 — `CH05 &middot; ENVIRONMENT SETUP` — تجهيز بيئة التطوير  (~3 pages)
Sub: من جهاز فارغ إلى Backend و Frontend يعملان ويتحدثان معاً
Topics: تثبيت/التحقق من Python و Git و Node.js/npm و PostgreSQL و Docker Desktop و VS Code؛
شرح مبسّط للـ Terminal ومفهوم مجلد العمل والـ Ports و Environment Variables؛
12 خطوة عملية (إنشاء المستودع، venv، التنشيط في PowerShell، تثبيت متطلبات الـ Backend،
إنشاء تطبيق React بـ Vite و TypeScript، تثبيت متطلبات الـ Frontend، إعداد .env، تشغيل PostgreSQL،
تشغيل الـ Backend، تشغيل الـ Frontend، فتح Swagger، التأكد من التواصل)؛ أوامر كاملة قابلة للنسخ
(Windows PowerShell أساساً + بدائل Linux/macOS)؛ جدول أخطاء الإعداد الشائعة وحلولها.
CODE: أوامر طرفية فقط داخل `.code-wrap` + `pre.term`.

## CH06 — `CH06 &middot; FASTAPI BACKEND` — معمارية الـ Backend بـ FastAPI  (~4 pages)
Sub: طبقات واضحة: Route ثم Schema ثم Model ثم Repository ثم Service
Topics: نقطة الدخول، الـ Routers، Pydantic schemas، SQLAlchemy models، إدارة الـ session،
طبقة Repository، طبقة Service، Dependency Injection، معالجة الأخطاء، Logging، إدارة الإعدادات،
CORS، التحقق من الملفات المرفوعة، Authentication/Authorization، API versioning؛
الفرق بين Route/Schema/Model/Repository/Service/Worker؛ ترتيب التنفيذ خطوة بخطوة.
DIAGRAM REQUIRED: Backend Layered Architecture.
CODE REQUIRED (ملفات مترابطة قابلة للتشغيل فعلاً، بنفس الأسماء في كل مكان):
`backend/app/main.py`, `backend/app/core/config.py`, `backend/app/db/session.py`,
`backend/app/models/video.py`, `backend/app/schemas/video.py`,
`backend/app/repositories/video_repository.py`, `backend/app/services/video_service.py`,
`backend/app/api/v1/router.py`, `backend/app/api/v1/endpoints/health.py` و `videos.py`,
`backend/requirements.txt`. تأكد من توافق الاستيرادات بين الملفات حرفياً.

## CH07 — `CH07 &middot; API CONTRACT` — تصميم الـ API وتوثيق الـ Endpoints  (~4 pages)
Sub: عقد واحد يتفق عليه الـ Backend والـ Frontend قبل كتابة الكود
Topics: جدول الـ Endpoints الكامل (Method, Endpoint, Purpose, Request, Response, Auth, Errors) لجميع
المسارات في SPEC.md؛ شرح رموز الحالة 200/201/202/204/400/401/403/404/409/413/422/500؛
أمثلة JSON حقيقية للطلب والرد (VideoOut, JobOut, IncidentOut, AnalyticsOverview, pagination envelope)؛
Pagination و Filtering و Sorting و Date-range؛
كيف نحافظ على استقرار العقد أثناء العمل المتوازي (ملف OpenAPI، versioning، mock server،
types مشتركة)؛ أخطاء الـ API الموحّدة.
CODE: أمثلة curl/HTTP + JSON، ومقتطف Pydantic للـ pagination.

## CH08 — `CH08 &middot; DATABASE DESIGN` — تصميم قاعدة البيانات مع PostgreSQL  (~4 pages)
Sub: الجداول والعلاقات والـ migrations
Topics: Primary/Foreign keys، Indexes، العلاقات، Timestamps، Constraints، Migrations؛
شرح كل جدول في SPEC مع جدول أعمدة (اسم، نوع، مفتاح، Nullable، الغرض)؛ الجداول الأساسية للـ MVP
والجداول المؤجَّلة؛ العلاقات (1..N) كما في SPEC؛ دعم الفلترة بالتاريخ والنوع والخطورة والفيديو والحالة؛
لماذا لا نخزّن الفيديو داخل PostgreSQL؛ إعداد Alembic وأول migration (أوامر كاملة)؛
ملاحظة أن `detections` ينمو بسرعة وخيار PERSIST_ALL_DETECTIONS؛
عدم تخزين هويات حقيقية للعاملين.
DIAGRAM REQUIRED: ER Diagram باستخدام `.er` و `.er-table`.
CODE: `backend/app/models/*.py` مختصرة، `backend/alembic.ini` مقتطف، أوامر Alembic.

## CH09 — `CH09 &middot; UPLOAD &amp; STORAGE` — رفع الفيديو وتخزين الملفات  (~3 pages)
Sub: كيف يستقبل النظام الفيديو ويحفظه بأمان
Topics: الصيغ المدعومة وحدود الحجم؛ التحقق من الامتداد والمحتوى (magic bytes / OpenCV probe)؛
أسماء ملفات فريدة وآمنة؛ مسارات التخزين؛ Metadata؛ منع التكرار بـ checksum؛ الفيديو التالف؛
الوصول الآمن للملفات (streaming endpoint)؛ تنظيف الرفع المتروك؛ سياسات الاحتفاظ؛
توليد صور الدليل والمقاطع القصيرة؛ Local storage للتطوير و Object storage للإنتاج؛
مقارنة (مجلد محلي / S3-compatible / تخزين سحابي)؛ طبقة Storage abstraction؛
الفرق بين سجل قاعدة البيانات والملف نفسه.
CODE: `backend/app/storage/base.py` + `local.py`، ومقتطف endpoint الرفع مع التحقق.

## CH10 — `CH10 &middot; AI MODEL INTEGRATION` — دمج الـ AI Models المتفق عليها  (~4 pages)
Sub: تحميل الـ checkpoints وتحويل مخرجاتها إلى صيغة داخلية موحّدة
Topics: لا نعيد تصميم الـ Models؛ إعداد الـ Models ومساراتها؛ تحميل الـ checkpoint؛ CPU مقابل GPU
واختيار الجهاز؛ إعدادات الـ Inference؛ تغيير الحجم؛ خريطة أسماء الأصناف؛ عتبات الثقة؛ NMS؛
المعالجة بالإطار مقابل الدفعات؛ Model warm-up؛ إدارة الموارد؛ معالجة الأخطاء؛ تسجيل إصدار الـ Model؛
قابلية إعادة الإنتاج؛ الواجهات البرمجية PPEDetectionService / FireSmokeDetectionService /
PersonTrackingService / SafetyRuleEngine؛ صيغة الكشف الموحّدة (class_name, confidence, bbox,
frame_number, timestamp_seconds, model_name, model_version, track_id)؛
لماذا لا ندمج بيانات تدريب مختلفة دون التحقق من خريطة الأصناف وتنسيق الـ annotation والـ splits؛
حالات: أوزان مفقودة، صيغة checkpoint غير متوافقة، لا يوجد GPU، نفاد الذاكرة؛
الـ accuracy تُقاس على مجموعة الاختبار ولا تُفترض.
CODE: `backend/app/ai/base.py` (Protocol/dataclass للكشف), `backend/app/ai/model_registry.py`,
`backend/app/ai/ppe_detector.py`, `backend/app/ai/demo_adapter.py` (محوّل تجريبي واضح أنه وهمي
ولا يمثّل مخرجات Model حقيقي)، وإعدادات الـ models في `core/config.py`.

## CH11 — `CH11 &middot; VIDEO PIPELINE` — خط معالجة الفيديو والـ Background Jobs  (~4 pages)
Sub: لماذا لا نعالج فيديو طويلاً داخل طلب HTTP واحد
Topics: لماذا الطلب المتزامن خطأ؛ تصميم Job-based workflow بالخطوات الست عشرة؛
حالات الـ Job (queued/running/completed/failed/cancelled)؛ نسبة التقدّم ورسائل الخطأ؛
تنفيذ worker بسيط يعمل محلياً وقابل للاختبار؛ متى نحتاج Task Queue فعلاً؛
لماذا لا نستخدم FastAPI BackgroundTasks كنظام jobs موثوق؛
منع المعالجة المزدوجة والوصول المتزامن لنفس الـ Model ونفاد الموارد؛
Frame sampling كمعامل قابل للضبط وكيف نتحقق من معدله (event recall / مدة الفيديو / سرعة المعالجة / العتاد)؛
Pseudocode + تنفيذ عملي.
DIAGRAM REQUIRED: Video Processing Sequence Diagram (استخدم `.seq`).
CODE: `backend/app/workers/processor.py`, `backend/app/workers/run_worker.py`,
`backend/app/services/job_service.py`, `backend/app/core/config.py` (متغيرات الـ pipeline).

## CH12 — `CH12 &middot; SAFETY RULES` — قواعد السلامة وتوليد الوقائع  (~3.5 pages)
Sub: كيف يتحول الكشف الخام إلى واقعة لها معنى
Topics: الفرق بين Detection / Track / Rule violation / Incident / Evidence / Review / Notification؛
عتبات الثقة؛ التأكيد الزمني؛ منع التكرار؛ فترات التهدئة (cooldown)؛ الربط بالـ tracking؛
وقت البداية والنهاية؛ تصنيف الخطورة؛ اختيار الدليل؛ المراجعة البشرية؛
قواعد الاقتراب من المعدات (صناديق، مسارات، مناطق خطر مُعرَّفة) وحدود الهندسة بالبكسل والمنظور؛
مثال واقعة مُولَّدة من عدة إطارات؛ لماذا لا يتحول إطار واحد غير مؤكد إلى مخالفة خطيرة مؤكَّدة.
CODE: `backend/app/ai/rules.py` (SafetyRuleEngine) + `backend/app/services/incident_service.py` (مقتطف).

## CH13 — `CH13 &middot; INCIDENT LIFECYCLE` — دورة حياة الواقعة والمراجعة البشرية  (~2.5 pages)
Sub: detected ثم pending_review ثم confirmed/rejected ثم closed
Topics: دورة الحياة؛ ما يفعله مسؤول السلامة (فتح الواقعة، عرض الدليل، الوقت والفيديو المصدر،
تأكيد/رفض، ملاحظة، تغيير الحالة، البحث التاريخي)؛ Auditability ولماذا نسجّل كل إجراء؛
مثال كامل: طلب API + تحديث قاعدة البيانات + سلوك الـ Frontend؛
تنبيه أن الكشف الآلي يساعد المراجعة ولا يحل محل الحكم المهني.
DIAGRAM REQUIRED: Incident Lifecycle Diagram.
CODE: `backend/app/api/v1/endpoints/incidents.py` (PATCH) + JSON مثال + `backend/app/models/incident_review.py`.

## CH14 — `CH14 &middot; FRONTEND ARCHITECTURE` — معمارية الـ Frontend بـ React و TypeScript  (~3.5 pages)
Sub: بنية قابلة للصيانة، هوية بصرية صناعية، وتجربة استخدام واضحة
Topics: بنية تطبيق React؛ أنواع TypeScript؛ الصفحات والمكوّنات القابلة لإعادة الاستخدام؛ Routing؛
طبقة API service؛ حالات Loading/Error/Empty؛ التحقق من النماذج؛ الإشعارات Toast؛ حالة المصادقة؛
التصميم المتجاوب؛ إمكانية الوصول؛ Environment Variables؛
الهوية البصرية (Dark Navy للبنية، Teal للمعلومة، Orange للتحذير، Red للخطر، خلفيات محايدة)
وتجنّب التدرجات الزائدة والحركات غير الضرورية؛
وصف كل صفحة من الصفحات العشر: الغرض، التخطيط، المكوّنات، نداءات الـ API، إجراءات المستخدم،
سلوك التحميل والخطأ. استخدم `.wf` لرسم Wireframes مصغّرة للصفحات الرئيسية (على الأقل 4 صفحات).
DIAGRAM REQUIRED: Frontend Page Structure (خريطة الصفحات والمسارات).
CODE: شجرة `frontend/src` الكاملة + `frontend/src/types/api.ts` (واجهات TypeScript مطابقة حرفياً
لـ VideoOut/JobOut/IncidentOut/EvidenceOut/AnalyticsOverview/Paginated).

## CH15 — `CH15 &middot; DASHBOARD &amp; API WIRING` — بناء لوحة التحكم وربطها بالـ API  (~4 pages)
Sub: من أول نداء Axios إلى رسم بياني يعتمد على بيانات حقيقية
Topics: Dashboard Overview (عدد الفيديوهات المعالجة، عدد الوقائع، حسب النوع، حسب الخطورة، أحدث الوقائع،
حالة الـ Jobs)؛ Video Library (الرفع، التاريخ، الحالة، البحث والفلترة، إعادة المعالجة)؛
Incident Management (جدول، نطاق تاريخ، فلترة النوع/الخطورة/الحالة، Pagination، معاينة الدليل، إجراءات المراجعة)؛
Analytics (الاتجاهات الزمنية، المخالفات حسب النوع، توزيع الخطورة، المخالفات المتكررة، مقارنة الفيديوهات)؛
Reports (ملخص يومي/أسبوعي، فلترة، تصدير CSV).
CODE REQUIRED (مترابط): `frontend/src/api/client.ts`, `frontend/src/api/videos.ts`,
`frontend/src/api/incidents.ts`, `frontend/src/hooks/usePolling.ts`,
`frontend/src/features/videos/UploadVideoForm.tsx` (FormData + progress),
`frontend/src/features/incidents/IncidentTable.tsx`, `frontend/src/features/analytics/OverviewCards.tsx`,
مثال Recharts، ومثال تنزيل CSV. اشرح CORS وكيف يُضبط Base URL من Environment Variables
ولا تُكتب روابط الإنتاج داخل المكوّنات.

## CH16 — `CH16 &middot; REAL-TIME STATUS` — التحديثات الفورية وحالة المعالجة  (~2 pages)
Sub: Polling الآن، WebSocket لاحقاً
Topics: الفرق بين Polling و Server-Sent Events و WebSocket؛ اختيار Polling للـ MVP؛
كود Polling يتوقف عند الحالة النهائية؛ تجنّب تسريب المؤقتات؛ Backoff بسيط؛
WebSocket كتحسين مستقبلي؛ التنبيه أن معالجة فيديو مسجَّل ليست "نظاماً لحظياً".
CODE: `frontend/src/hooks/useJobStatus.ts` + `backend/app/api/v1/endpoints/ws.py` (مستقبلي، موضّح أنه غير منفَّذ).

## CH17 — `CH17 &middot; ANALYTICS &amp; REPORTS` — التحليلات وتقارير الالتزام والتصدير  (~3 pages)
Sub: كل رقم في اللوحة يجب أن يأتي من صف مخزَّن في قاعدة البيانات
Topics: حساب المؤشرات من السجلات الفعلية؛ العدّ حسب التاريخ والنوع والخطورة وحالة المراجعة؛
المخالفات المتكررة؛ الملخصات اليومية؛ تصدير CSV؛ PDF كخيار مستقبلي؛
الفلترة بالتاريخ والفيديو والكاميرا والنوع؛
لماذا لا يجوز استخدام أرقام ثابتة في الكود؛ ووسم البيانات الاصطناعية بوضوح عند عدم توفر بيانات حقيقية.
CODE: `backend/app/services/analytics_service.py` (استعلامات SQLAlchemy)،
`backend/app/api/v1/endpoints/reports.py` (CSV Response)، وكود React لتنزيل الملف.

## CH18 — `CH18 &middot; SECURITY &amp; PRIVACY` — الأمان والخصوصية والمصادقة  (~3 pages)
Sub: أمان عملي لمشروع طلابي صناعي، بدون مبالغة وبدون ثغرات واضحة
Topics: تشفير كلمات المرور (bcrypt)؛ JWT أو بديل مناسب؛ Authentication مقابل Authorization؛
RBAC إذا لزم؛ أمان رفع الملفات وحدود الحجم وأسماء الملفات؛ منع SQL Injection؛
إدارة الأسرار؛ تقييد CORS؛ التحقق من المدخلات؛ Rate limiting عند الحاجة؛ النسخ الاحتياطي؛
Logs بدون بيانات حساسة؛ ضبط الوصول للفيديو والدليل؛ سياسات الاحتفاظ؛
تتبّع مجهول الهوية وعدم استخدام التعرف على الوجوه؛ توضيح أن track_id مؤقت داخل الفيديو وليس هوية حقيقية.
CODE: `backend/app/core/security.py`، `backend/app/api/deps.py` (get_current_user)، `.env.example` بقيم Placeholder.

## CH19 — `CH19 &middot; DOCKER` — Docker والنشر المحلي  (~3.5 pages)
Sub: تشغيل الـ Backend و الـ Frontend و PostgreSQL بأمر واحد
Topics: شرح Docker و Docker Compose من البداية؛ حاويات الـ Backend والـ Frontend و PostgreSQL؛
كيف تُوفَّر ملفات الـ Models والفيديوهات للحاويات (volumes)؛
الـ Container networking وأسماء الخدمات بدلاً من localhost؛
الخطوات السبع (build, up, logs, migrate, health, restart, data persistence)؛
حدود دعم GPU في Docker خصوصاً على Windows، وبديل CPU للعرض التوضيحي؛
جدول أوامر Docker Compose.
DIAGRAM REQUIRED: Docker Deployment Diagram.
CODE: `backend/Dockerfile`, `frontend/Dockerfile`, `.dockerignore`, `docker-compose.yml`,
`.env.example`, وأوامر التشغيل — كلها متوافقة مع SPEC (أسماء الخدمات، DATABASE_URL، المنافذ).

## CH20 — `CH20 &middot; PRODUCTION DEPLOYMENT` — النشر في بيئة الإنتاج  (~3 pages)
Sub: خياران واقعيان لمشروع تخرّج، وما يجب الحذر منه
Topics: الخيار A: نشر بسيط للعرض (Frontend على استضافة ثابتة، Backend على App server،
PostgreSQL مُدار، Object storage)؛ الخيار B: استضافة ذاتية أو قادرة على GPU مع Reverse proxy و HTTPS؛
لكل خيار: التكلفة، توفر GPU، حدود رفع الفيديو، التخزين الدائم، سرعة الشبكة، زمن المعالجة،
النوم/البدء البارد، الأسرار، HTTPS، الـ migrations، النسخ الاحتياطي، الـ Logs، Health checks؛
لماذا لا تصلح الاستضافة الثابتة المجانية للـ inference الطويل؛
تحذير صريح: القدرات والأسعار والـ free tiers وتوفّر الـ GPU تتغيّر ويجب التحقق من التوثيق الرسمي
وقت النشر — ولا نكتب أسعاراً أو وعود GPU مجاني؛ قائمة تحقق النشر والترتيب الآمن؛
فصل بيئة التطوير عن الإنتاج.

## CH21 — `CH21 &middot; CI/CD` — الـ CI/CD وسير عمل GitHub  (~2.5 pages)
Sub: كيف يعمل خمسة طلاب على مستودع واحد دون فوضى
Topics: إنشاء المستودع؛ الفروع؛ Feature branches؛ Pull requests؛ مراجعة الكود؛ حل تعارضات الدمج؛
رسائل الـ commit؛ `.gitignore`؛ GitHub Issues؛ Milestones؛ Release tags؛
GitHub Actions اختياري: فحص Python والاختبارات، بناء الـ Backend، بناء الـ Frontend، Lint،
Type checking، بناء صورة Docker؛ متى يصبح الـ CI/CD مفيداً فعلاً؛
تحذير من رفع الفيديوهات الخاصة وكلمات المرور وملفات الـ Models.
CODE: `.github/workflows/ci.yml` كامل + أوامر Git اليومية.

## CH22 — `CH22 &middot; TESTING` — الاختبارات وضمان الجودة  (~3.5 pages)
Sub: كيف نتأكد أن النظام يعمل فعلاً قبل المناقشة
Topics: Unit Testing (التحقق من الفيديو، خريطة الأصناف، فلترة الثقة، تقييم القواعد، منع تكرار الوقائع،
حسابات التقارير)؛ Integration Testing (API↔DB، الرفع↔التخزين، Job↔AI، مخرجات الـ AI↔سجلات الوقائع،
الوقائع↔التقارير، Frontend↔Backend)؛ End-to-End Testing بخطوات الرحلة الكاملة العشر؛
جدول حالات اختبار (Test ID, Scenario, Preconditions, Steps, Expected, Actual, Pass/Fail)
مع ترك خانتي Actual/Pass-Fail فارغتين (يُملأ بعد التنفيذ)؛ الاختبار بدون GPU؛
فيديو صناعي صغير جداً كـ fixture؛ أدوات pytest و httpx/TestClient و Vitest.
CODE: `backend/tests/conftest.py`, `backend/tests/test_rules.py`, `backend/tests/test_api_incidents.py`.

## CH23 — `CH23 &middot; EVALUATION` — تقييم الـ AI وأداء النظام  (~3 pages)
Sub: تقييم الـ Models منفصلة عن تقييم التطبيق، وبأرقام حقيقية فقط
Topics: Precision, Recall, F1, Confusion Matrix, mAP، مقاييس التتبع؛ False Positives/Negatives؛
تقييم على مستوى الواقعة؛ زمن المعالجة، FPS، زمن معالجة الفيديو، زمن استجابة الـ API،
نسبة فشل الـ Jobs، نسبة نجاح توليد الدليل؛
لماذا لا تضمن mAP العالية نظام إدارة وقائع مفيداً؛
خطة تقييم خط الأنابيب كاملاً في ظروف إضاءة مختلفة، حجب (occlusion)، زوايا كاميرا، مشاهد مزدحمة،
وحالات صعبة؛ جداول نتائج فارغة (يُملأ بعد التجربة) — لا أرقام مُختلقة إطلاقاً.
CODE: `scripts/evaluate_model.py` (سكربت تقييم) ووصف مخرجاته المتوقعة شكلاً لا رقماً.

## CH24 — `CH24 &middot; ERRORS &amp; LOGGING` — معالجة الأخطاء والـ Logging والمراقبة  (~2.5 pages)
Sub: كيف يتصرف النظام عندما تسوء الأمور
Topics: فيديو تالف، رفع كبير جداً، checkpoint مفقود، ذاكرة GPU غير كافية، قاعدة البيانات غير متاحة،
فشل Job، انقطاع اتصال الـ Frontend، فشل تخزين الدليل، مخرجات Model غير صالحة؛
Logging مفيد مع سياق، ربط الأخطاء بـ job_id، عدم كشف الأسرار، التمييز بين الأخطاء القابلة للاسترجاع
وغير القابلة، إعادة المحاولة الآمنة، منع تكرار الوقائع بعد إعادة المحاولة، مراقبة صحة الخدمة؛
جدول استكشاف أخطاء (الأعراض، الأسباب المحتملة، الحل).
CODE: `backend/app/core/logging.py`, `backend/app/core/errors.py`.

## CH25 — `CH25 &middot; TEAM DIVISION` — توزيع العمل على خمسة أعضاء  (~3 pages)
Sub: من يفعل ماذا، وما يعتمد على من، وكيف نمنع أن يصبح عضو واحد عنق الزجاجة
Topics: الأدوار الخمسة كما في SPEC (M1..M5) وتفصيل مسؤوليات كل دور؛ الاعتماديات بين الأدوار؛
التأكيد أن M5 ليس مسؤولاً وحده عن إصلاح مشاكل الدمج في النهاية وأن التكامل يبدأ مبكراً؛
جدول (المسؤولية، المخرجات، الاعتماديات، معايير القبول) لكل عضو؛
كيف يعمل الجميع على نفس الـ API contract ونفس هياكل البيانات؛
اقتراح اجتماع أسبوعي قصير وقواعد للتواصل؛ استخدام Placeholder لأسماء الأعضاء
`<TEAM_MEMBER_1_NAME>` .. `<TEAM_MEMBER_5_NAME>`.
DIAGRAM REQUIRED: Five-Person Team Dependency Diagram.

## CH26 — `CH26 &middot; TIMELINE` — الجدول الزمني والمراحل  (~3 pages)
Sub: خطة 8–10 أسابيع قابلة للتعديل
Topics: المراحل العشر (تثبيت المتطلبات وإعداد المستودع، بيئة التطوير وعقد الـ API، قاعدة البيانات
وأساس الـ Backend، دمج الـ inference، معالجة الفيديو والـ jobs، خط الوقائع والدليل، لوحة التحكم،
التقارير والمراجعة، التكامل والاختبارات، Docker والعرض التوضيحي)؛
لكل مرحلة: المدة، المهام، الاعتماديات، المخرجات، معايير القبول، المخاطر؛
ما يمكن تنفيذه بالتوازي؛ قائمة تحقق للمراحل (Milestone checklist) قابلة للقياس؛
جدول زمني مرئي (استخدم `.dg` كـ Gantt مبسّط).

## CH27 — `CH27 &middot; MVP DEFINITION` — تعريف الـ MVP ومعايير القبول  (~3 pages)
Sub: أصغر نظام مكتمل يمكن عرضه بنجاح
Topics: قائمة الـ MVP (واجهة تعمل، Backend يعمل، PostgreSQL، رفع وتحقق، خط jobs،
دمج checkpoints، كشف وقواعد، توليد وقائع، تخزين دليل، سجل وفلترة، إجراءات مراجعة،
تحليلات من سجلات حقيقية، تصدير CSV، أمان وتحقق أساسي، تعليمات تشغيل محلي، فيديو عرض مُختبر)؛
ما لا يدخل الـ MVP ويُذكر صراحة كـ Pending؛
Definition of Done لكل وحدة رئيسية (Backend, Database, AI, Pipeline, Frontend, Reports, Deployment)؛
مصفوفة (الميزة، معيار القبول، كيف نقيسه، الحالة) مع ترك الحالة للتعبئة.

## CH28 — `CH28 &middot; FINAL DEMO` — العرض النهائي لمشروع التخرّج  (~2.5 pages)
Sub: خطة عرض من 8 إلى 12 دقيقة بالترتيب
Topics: الخطوات الثلاث عشرة بالترتيب (المشكلة، المعمارية، فتح التطبيق، رفع فيديو، بدء المعالجة،
التقدّم، الوقائع، تفاصيل واقعة ودليلها، المراجعة، التحليلات، تصدير تقرير، نتائج تقييم الـ AI،
الحدود والتحسينات المستقبلية)؛ جدول توزيع الوقت؛
خطة بديلة عند فشل GPU أو الإنترنت أو النشر (فيديو مسجَّل، نتائج محفوظة، Docker محلي)؛
التمييز الصريح بين العرض الحي والمواد المسجَّلة مسبقاً؛
تدريب على الأسئلة المتوقعة من اللجنة (مع إجابات مقترحة قصيرة).

## CH29 — `CH29 &middot; FINAL CHECKLIST` — قائمة التحقق النهائية واستكشاف الأخطاء  (~3 pages)
Sub: قبل المناقشة، تحقّق من كل شيء
Topics: قائمة تحقق شاملة (تنظيم الكود، الـ Backend، الـ Frontend، قاعدة البيانات، دمج الـ Models،
خط الفيديو، تخزين الملفات، الأمان، الاختبارات، النشر، التقارير، التوثيق، جاهزية الفريق)؛
مرجع استكشاف أخطاء يغطي: بيئات Python، تعارض الإصدارات، FastAPI، اتصال PostgreSQL، SQLAlchemy،
Alembic، CORS، طلبات React، رفع الملفات، OpenCV، الـ checkpoints، ذاكرة GPU، شبكة Docker،
الـ volumes، متغيرات بيئة الإنتاج — ولكل خطأ تسلسل تشخيص (خطوات مرتّبة) لا تخميناً لسبب واحد.

## CH30 — `CH30 &middot; REFERENCES` — المراجع والمواد المرجعية  (~3 pages)
Sub: كل ما يحتاجه الفريق في مكان واحد
Topics: روابط التوثيق الرسمي (FastAPI, React, Vite, TypeScript, Tailwind, Recharts, PostgreSQL,
SQLAlchemy, Alembic, Docker, OpenCV, PyTorch, Ultralytics, Node.js, Python, GitHub Actions, pydantic)
— استخدم جذور الروابط الرسمية فقط، وأضف عمود "يحتاج تحققاً يدوياً" إن لم تتحقق؛
قاموس مصطلحات (إنجليزي + شرح عربي) لعشرات المصطلحات المهمة في جدول من ثلاث أعمدة
(المصطلح، النطق/الاختصار إن وُجد، الشرح بالعربية)؛
قائمة كاملة بمتغيرات البيئة من SPEC.md (الاسم، الوصف، قيمة Placeholder، إلزامي/اختياري)؛
ملخص هيكل المستودع؛ ملخص عقد الـ API؛ خريطة الاعتماديات النهائية بين المكوّنات (استخدم `.dg`).

---
## Final page budget check
The handbook should land between roughly 75 and 95 printed pages of content. If a chapter comes out
much shorter than its budget, add a practical example, a troubleshooting table or an extra figure —
never filler text.
