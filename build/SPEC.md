# SafeVision AI — AUTHORITATIVE SPECIFICATION (single source of truth)

Every chapter MUST use exactly these names, fields, routes and types. Never invent
conflicting variants. If a value is unknown, use the placeholder form described here.

## 0. Document language rules
- Prose: Arabic (Modern Standard, simple, Egyptian-university friendly).
- Technical terms, identifiers, file names, commands, code, JSON keys: English, wrapped in
  `<span class="en">...</span>` (or `<code>...</code>` inside tables/code).
- At the FIRST mention of an important term, give a short Arabic definition, e.g.
  `**Backend:** الجزء المسؤول عن استقبال الطلبات ...`
- Code comments: English only. Never Arabic inside `<pre>`.

## 1. Repository layout (canonical)
```text
safevision-ai/
  backend/    (FastAPI application, package name: app)
  frontend/   (React + TypeScript + Vite)
  models/     (model checkpoints, NOT in git)
  data/       raw | processed | sample
  storage/    uploads | evidence | reports   (NOT in git)
  docs/  scripts/  docker-compose.yml  .env.example  .gitignore  README.md
```
Backend package layout: `app/main.py`, `app/api/v1/`, `app/core/`, `app/db/`, `app/models/`,
`app/schemas/`, `app/repositories/`, `app/services/`, `app/ai/`, `app/workers/`,
`app/storage/`, `app/reports/`, `app/utils/`, plus `backend/migrations/` (Alembic), `backend/tests/`.

## 2. Technology stack (canonical, with MVP status)
| Area | Choice | MVP |
|---|---|---|
| Language (backend/AI) | Python 3.11 | required |
| Web framework | FastAPI + Uvicorn | required |
| Validation | Pydantic v2 + pydantic-settings | required |
| ORM | SQLAlchemy 2.0 (declarative, typed) | required |
| Migrations | Alembic | required |
| Database | PostgreSQL 16 | required |
| DB driver | psycopg (v3) | required |
| Auth | JWT (PyJWT) + bcrypt password hashing | MVP-optional (behind a flag) |
| CV | OpenCV (opencv-python) | required |
| DL | PyTorch + Ultralytics YOLO (where compatible with agreed checkpoints) | required |
| Tracking | ByteTrack (via Ultralytics `model.track`) | required for person tracking |
| Numerics | NumPy; Pandas for analytics/reports | required |
| Job runner | DB-backed job queue + standalone worker process | required (MVP) |
| Status updates | Frontend polling | required |
| Frontend | React 18 + TypeScript 5 + Vite 5 | required |
| Styling | Tailwind CSS 3 | required |
| Charts | Recharts | required |
| HTTP client | Axios | required |
| Routing | react-router-dom v6 | required |
| Containers | Docker + Docker Compose | required for delivery |
| CI | GitHub Actions | optional (post-MVP) |
Explicitly NOT in the MVP: Kubernetes, Kafka, Redis, Celery, microservices, live RTSP streaming.

Version note: the pins above are a starting point. Always confirm the exact current versions on
PyPI/npm before pinning, because versions change.

## 3. Database schema (canonical)

Enums (stored as PostgreSQL native enum or VARCHAR + CHECK):
- `video_status`: uploaded | processing | processed | failed
- `job_status`: queued | running | completed | failed | cancelled
- `incident_type`: ppe_violation | fire_smoke | machine_proximity
- `incident_severity`: low | medium | high | critical
- `incident_status`: detected | pending_review | confirmed | rejected | closed
- `evidence_kind`: image | clip | metadata
- `review_action`: confirm | reject | close | comment
- `user_role`: admin | safety_officer | viewer

### users  (MVP-optional, only if auth is enabled)
| column | type | key | null | purpose |
|---|---|---|---|---|
| id | UUID | PK | no | primary key |
| email | VARCHAR(255) | unique | no | login identifier |
| full_name | VARCHAR(150) |  | no | display name |
| hashed_password | VARCHAR(255) |  | no | bcrypt hash (never plaintext) |
| role | user_role |  | no | default 'safety_officer' |
| is_active | BOOLEAN |  | no | default true |
| created_at / updated_at | TIMESTAMPTZ |  | no | audit timestamps |

### cameras (planned)
id UUID PK, name VARCHAR(120) NOT NULL, location_label VARCHAR(180), description TEXT,
created_at TIMESTAMPTZ NOT NULL.

### videos (MVP)
| column | type | key | null | purpose |
|---|---|---|---|---|
| id | UUID | PK | no | |
| camera_id | UUID | FK -> cameras.id | yes | nullable in MVP |
| original_filename | VARCHAR(255) |  | no | as uploaded by the user |
| stored_filename | VARCHAR(255) |  | no | sanitized unique name on disk |
| storage_key | VARCHAR(512) | unique | no | relative path / object key |
| content_type | VARCHAR(100) |  | no | e.g. video/mp4 |
| size_bytes | BIGINT |  | no | file size |
| duration_seconds | NUMERIC(10,3) |  | yes | filled after validation |
| fps | NUMERIC(8,3) |  | yes | |
| width / height | INTEGER |  | yes | frame size |
| frame_count | INTEGER |  | yes | |
| checksum_sha256 | CHAR(64) | index | yes | duplicate detection |
| status | video_status |  | no | default 'uploaded' |
| uploaded_by | UUID | FK -> users.id | yes | |
| created_at / updated_at | TIMESTAMPTZ |  | no | |

### processing_jobs (MVP)
id UUID PK; video_id UUID FK->videos.id (NOT NULL, ON DELETE CASCADE); status job_status NOT NULL
default 'queued'; progress NUMERIC(5,2) NOT NULL default 0; frames_total INTEGER;
frames_processed INTEGER NOT NULL default 0; sample_every_n_frames INTEGER NOT NULL default 5;
model_bundle_version VARCHAR(80); error_message TEXT; worker_id VARCHAR(80);
started_at TIMESTAMPTZ; finished_at TIMESTAMPTZ; created_at TIMESTAMPTZ NOT NULL.
Unique partial index to prevent two active jobs for the same video:
`UNIQUE (video_id) WHERE status IN ('queued','running')` (implemented as a partial unique index).

### detections (MVP)
id BIGSERIAL PK; job_id UUID FK->processing_jobs.id ON DELETE CASCADE; video_id UUID FK->videos.id;
frame_number INTEGER NOT NULL; timestamp_seconds NUMERIC(10,3) NOT NULL; class_name VARCHAR(80) NOT NULL;
confidence NUMERIC(5,4) NOT NULL; bbox_x1/bbox_y1/bbox_x2/bbox_y2 INTEGER NOT NULL; track_id INTEGER;
model_name VARCHAR(80) NOT NULL; model_version VARCHAR(40) NOT NULL; created_at TIMESTAMPTZ NOT NULL.
Indexes: (job_id, frame_number), (class_name), (video_id).
Note: `detections` grows fast. MVP writes only detections that matter (see ch.11/12) or samples them;
full per-frame storage is a configurable flag `PERSIST_ALL_DETECTIONS=false`.

### tracks (MVP, optional but recommended)
id BIGSERIAL PK; job_id UUID FK; video_id UUID FK; track_id INTEGER NOT NULL; class_name VARCHAR(80);
first_frame INTEGER; last_frame INTEGER; first_ts NUMERIC(10,3); last_ts NUMERIC(10,3); hits INTEGER;
UNIQUE (job_id, track_id).

### incidents (MVP)
id UUID PK; video_id UUID FK->videos.id NOT NULL; job_id UUID FK->processing_jobs.id;
incident_type incident_type NOT NULL; severity incident_severity NOT NULL default 'medium';
status incident_status NOT NULL default 'detected'; started_at_seconds NUMERIC(10,3) NOT NULL;
ended_at_seconds NUMERIC(10,3); frame_number INTEGER; track_id INTEGER; confidence NUMERIC(5,4);
class_name VARCHAR(80); zone_name VARCHAR(120); summary TEXT; detection_count INTEGER default 1;
created_at / updated_at TIMESTAMPTZ NOT NULL.
Indexes: (video_id), (incident_type), (severity), (status), (created_at).

### evidence (MVP)
id UUID PK; incident_id UUID FK->incidents.id ON DELETE CASCADE; kind evidence_kind NOT NULL;
storage_key VARCHAR(512) NOT NULL; content_type VARCHAR(100); size_bytes BIGINT;
frame_number INTEGER; timestamp_seconds NUMERIC(10,3); created_at TIMESTAMPTZ NOT NULL.

### incident_reviews (MVP)
id UUID PK; incident_id UUID FK->incidents.id ON DELETE CASCADE; reviewer_id UUID FK->users.id (nullable);
action review_action NOT NULL; previous_status incident_status; new_status incident_status;
note TEXT; created_at TIMESTAMPTZ NOT NULL.

### model_runs (planned)
id UUID PK; job_id UUID FK; model_name VARCHAR(80); model_version VARCHAR(40); device VARCHAR(20);
weights_path VARCHAR(512); classes_json JSONB; duration_ms INTEGER; error TEXT; created_at TIMESTAMPTZ NOT NULL.

### notifications (future)
id UUID PK; user_id UUID FK; incident_id UUID FK; channel VARCHAR(40); status VARCHAR(30); created_at TIMESTAMPTZ NOT NULL.

Relationship summary (must be stated consistently):
- videos 1..N processing_jobs
- processing_jobs 1..N detections ; processing_jobs 1..N tracks
- videos 1..N incidents ; processing_jobs 1..N incidents
- incidents 1..N evidence ; incidents 1..N incident_reviews
- model_runs N..1 processing_jobs
Video binaries are NEVER stored in PostgreSQL: only metadata + `storage_key`.

## 4. REST API contract (canonical)
Base URL: `http://localhost:8000`, prefix `/api/v1`. All bodies JSON unless noted.

| Method | Endpoint | Purpose | Auth | Success |
|---|---|---|---|---|
| GET | /api/v1/health | liveness + component status | no | 200 |
| POST | /api/v1/videos | upload a video (multipart/form-data) | yes* | 201 |
| GET | /api/v1/videos | paginated video list | yes* | 200 |
| GET | /api/v1/videos/{video_id} | one video + latest job | yes* | 200 |
| DELETE | /api/v1/videos/{video_id} | delete video + files (safe delete) | yes* | 204 |
| POST | /api/v1/videos/{video_id}/process | create a processing job | yes* | 202 |
| GET | /api/v1/jobs/{job_id} | job status + progress | yes* | 200 |
| GET | /api/v1/jobs | list jobs (filter by status/video) | yes* | 200 |
| GET | /api/v1/incidents | paginated + filtered incident list | yes* | 200 |
| GET | /api/v1/incidents/{incident_id} | incident detail | yes* | 200 |
| PATCH | /api/v1/incidents/{incident_id} | review/status change | yes* | 200 |
| GET | /api/v1/incidents/{incident_id}/evidence | evidence list | yes* | 200 |
| GET | /api/v1/evidence/{evidence_id}/file | stream evidence image/clip | yes* | 200 |
| GET | /api/v1/analytics/overview | dashboard KPIs | yes* | 200 |
| GET | /api/v1/analytics/timeseries | incidents per day | yes* | 200 |
| GET | /api/v1/reports/daily | daily summary rows | yes* | 200 |
| GET | /api/v1/reports/export | CSV export (text/csv) | yes* | 200 |
| POST | /api/v1/auth/login | obtain JWT | no | 200 |
| GET | /api/v1/auth/me | current user | yes | 200 |
`*` Auth is enforced only when `AUTH_ENABLED=true`. In MVP demo mode `AUTH_ENABLED=false` and the
endpoints behave as if a default `safety_officer` user were logged in. Document this clearly.

### Response shapes (exact field names — reuse everywhere)
`VideoOut`: id, original_filename, stored_filename, content_type, size_bytes, duration_seconds, fps,
width, height, frame_count, status, created_at, updated_at, latest_job (JobOut | null)
`JobOut`: id, video_id, status, progress, frames_total, frames_processed, sample_every_n_frames,
started_at, finished_at, error_message, created_at
`IncidentOut`: id, video_id, job_id, incident_type, severity, status, started_at_seconds,
ended_at_seconds, frame_number, track_id, confidence, class_name, zone_name, summary,
detection_count, created_at, updated_at, evidence (EvidenceOut[])
`EvidenceOut`: id, incident_id, kind, storage_key, content_type, size_bytes, frame_number,
timestamp_seconds, file_url
`IncidentPatch`: status?, note?, reviewer_id?
`AnalyticsOverview`: total_videos, processed_videos, total_incidents, incidents_by_type (object),
incidents_by_severity (object), incidents_by_status (object), pending_review, jobs_running, jobs_failed,
last_incident_at
`TimeseriesPoint`: date (YYYY-MM-DD), ppe_violation, fire_smoke, machine_proximity, total
Pagination envelope for list endpoints: `{ "items": [...], "total": 0, "page": 1, "page_size": 20,
"pages": 0 }` with query params `page`, `page_size` (max 100), plus filters and `sort` (e.g. `-created_at`).

### Detection normalization contract (internal, used by ch.10-12)
```json
{
  "class_name": "person",
  "confidence": 0.87,
  "bbox": [x1, y1, x2, y2],
  "frame_number": 120,
  "timestamp_seconds": 4.0,
  "model_name": "ppe_detector",
  "model_version": "v1.0.0",
  "track_id": 7
}
```

## 5. Placeholders (mandatory format)
When a real value is unknown use exactly: `<PPE_MODEL_CHECKPOINT_PATH>`, `<FIRE_SMOKE_MODEL_CHECKPOINT_PATH>`,
`<PERSON_TRACKER_CHECKPOINT_PATH>`, `<MODEL_VERSION>`, `<DATASET_NAME>`, `<TEAM_MEMBER_1_NAME>`, `<SUPERVISOR_NAME>`,
`<UNIVERSITY_NAME>`. Every placeholder must be explained where it is introduced and listed in ch.30.
NEVER invent accuracy, mAP, FPS, latency, test results, or claim a module is finished.

## 6. Environment variables (canonical names)
APP_NAME, APP_ENV, APP_DEBUG, API_V1_PREFIX, AUTH_ENABLED, SECRET_KEY, JWT_ALGORITHM,
ACCESS_TOKEN_EXPIRE_MINUTES, CORS_ORIGINS,
POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, DATABASE_URL,
STORAGE_BACKEND, LOCAL_STORAGE_ROOT, UPLOAD_DIR, EVIDENCE_DIR, REPORT_DIR,
S3_ENDPOINT_URL, S3_BUCKET, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, S3_REGION,
MAX_UPLOAD_MB, ALLOWED_VIDEO_EXTENSIONS, UPLOAD_CHUNK_MB,
MODEL_DIR, PPE_MODEL_PATH, FIRE_SMOKE_MODEL_PATH, PERSON_TRACKER_PATH, MODEL_DEVICE,
DETECTION_CONF_THRESHOLD, NMS_IOU_THRESHOLD, INFERENCE_IMG_SIZE, PERSIST_ALL_DETECTIONS,
FRAME_SAMPLE_EVERY_N, MAX_FRAMES_PER_JOB,
INCIDENT_CONFIRM_FRAMES, INCIDENT_COOLDOWN_SECONDS, PPE_CONF_THRESHOLD, FIRE_CONF_THRESHOLD,
SMOKE_CONF_THRESHOLD, PROXIMITY_MIN_OVERLAP, DANGER_ZONE_CONFIG,
WORKER_POLL_INTERVAL_SECONDS, WORKER_ID, WORKER_CONCURRENCY, JOB_MAX_RETRIES,
VITE_API_BASE_URL, VITE_ENABLE_AUTH

## 7. Incident lifecycle (canonical)
detected -> pending_review -> confirmed | rejected -> closed
- `detected`: created automatically by the pipeline.
- `pending_review`: queued for a human safety officer.
- `confirmed` / `rejected`: after human review (a row is appended to incident_reviews).
- `closed`: no further action. `closed` may follow confirmed or rejected.

## 8. Team roles (canonical)
M1 AI Models & Inference; M2 Video Processing & Safety Logic; M3 Backend & Database;
M4 Frontend; M5 Integration, QA & Deployment.
