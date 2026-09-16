# FamilyConnect Backend — Chuẩn bị kết nối Frontend (backend-only, P0+P1)

## Context

Frontend (develop) gọi API qua `frontend/src/services/api.ts`, base URL = `http://localhost:8000` (`.env.local`, không có prefix `/api/v1`). Hiện frontend chạy `VITE_MOCK=true` nên chưa lộ lỗi; bật real mode thì nhiều endpoint backend **thiếu, sai path, hoặc trả payload thiếu trường**.

Ràng buộc: **không sửa frontend** — mọi fix nằm phía backend. Scope chốt: **P0 + P1** (endpoint frontend thật sự gọi + sửa prefix/naming). Join-request xử lý dạng nhẹ (chỉ loại 422, không thêm model/migration). Branch hiện tại: `fix/backend-routes-only`.

## Audit — gap cần fix (P0 + P1)

### P0 (screens thật sự gọi API)
| # | Frontend call | Vấn đề backend | Fix |
|---|---|---|---|
| 1 | `POST /auth/login` cần `{access_token, refresh_token, user}` | trả thiếu `user` → auth store user undefined | thêm `user` vào `TokenResponse` + `login()` trả user |
| 2 | `POST /auth/verify-email` (PUB-05) | 404 | thêm endpoint + `AuthService.verify_email(token)` |
| 3 | `PUT /users/me` (PRF-01) | backend chỉ có `PUT /auth/me` + `PUT /auth/users/me` | thêm router root `/users` (GET+PUT `/users/me`) |
| 4 | `POST /families/{id}/branches` (FAM-03) | không có route | thêm route + `FamilyService.create_branch` (dùng `BranchRepository`) |
| 5 | `POST /families/{id}/events` (EVT-03) | controller stub, không nối service | wire `EventService` (đã sẵn 8 methods), bỏ stub |
| 6 | `familyApi.update` approve/reject join (FAM-05) | `FamilyUpdate` thiếu `action`/`request_id` → 422 | thêm 2 field optional; `update_family` tolerate → 200 (mock, không thêm model) |
| 7 | events naming `GET /events/{id}/participants` | backend có `/events/{id}/attendees` | thêm alias `participants` → cùng logic |

OK rồi (giữ): `register`, `forgot-password`, `POST /families`, `POST /families/{id}/members`, `POST /families/{id}/relationships`, `POST /families/{id}/posts`, `POST /ai/search`.

### P1 (sai prefix/path — đang mock, bật real là 404)
| # | Frontend call | Backend hiện tại | Fix |
|---|---|---|---|
| 8 | `/admin/users`... | `prefix="/api/admin"` | đổi prefix → `"/admin"` (giữ routes con `users`, `moderation`, `audit-log`, `backup(s)`, `config`) |
| 9 | `/families/{id}/heritage/documents\|stories\|outstanding` + `/families/{id}/photos` | `prefix="/api"` + flat routes | bỏ `/api` prefix; thêm `documents` (lọc type DOCUMENT), `stories` (type STORY), `photos` (→ media) song song, giữ routes flat cũ |
| 10 | `/families/{id}/directory*` (chưa gọi) | `prefix="/api"` | bỏ `/api` prefix cho khớp về sau |

Lưu ý: đổi prefix admin/heritage/directory là **rename path** (không phá frontend vì frontend đang mock, gọi theo path không-prefix). Không đụng routes mà frontend P0 đã dùng.

## Files cần sửa
- `app/api/controllers/auth_controller.py` — verify-email, `/users` alias nếu tách, login payload
- `app/api/controllers/event_controller.py` — wire service (bỏ stub), participants alias
- `app/api/controllers/family_controller.py` — branches route, FamilyUpdate +action/request_id, join tolerate
- `app/api/controllers/admin_controller.py` — prefix `/api/admin` → `/admin`
- `app/api/controllers/heritage_controller.py` — bỏ `/api`, thêm documents/stories/photos
- `app/api/controllers/directory_controller.py` — bỏ `/api`
- `app/api/controllers/user_controller.py` (mới) — GET/PUT `/users/me`
- `app/api/routes.py` — đăng ký user_controller
- `app/services/auth_service.py` — `verify_email`, login trả user
- `app/services/family_service.py` — `create_branch`, `update_family` tolerate join action
- `app/schemas/auth.py` — `TokenResponse.user`
- `app/schemas/family.py` (nếu FamilyUpdate nằm ở đây — hiện nằm trong family_controller.py, sửa tại đó)

## Reuse hiện có
- `BranchRepository.create/update/delete` — `app/infrastructure/repositories/branch_repository.py`
- `EventService` (create/get_events/get_event/update/cancel/rsvp/get_attendees/send_reminder) — `app/services/event_service.py`
- `AuthService.get_profile/update_profile` — `app/services/auth_service.py`
- DI pattern `get_family_service` — `app/api/dependencies.py` (mẫu để thêm `get_event_service`)
- Heritage service + `HERITAGE_TYPES` — lọc documents/stories theo type

## Steps
- [x] P0-1: `TokenResponse.user` + `login()` trả user
- [x] P0-2: `POST /auth/verify-email` + `AuthService.verify_email`
- [x] P0-3: router `/users` (GET+PUT `/users/me`) + đăng ký routes.py
- [x] P0-4: `POST /families/{id}/branches` + `FamilyService.create_branch`
- [x] P0-5: wire event_controller với EventService (bỏ stub), alias `participants`
- [x] P0-6: `FamilyUpdate` +action/request_id optional; `update_family` tolerate join → 200
- [x] P1-8: admin prefix `/api/admin` → `/admin`
- [x] P1-9: heritage bỏ `/api` + routes documents/stories/photos
- [x] P1-10: directory bỏ `/api`
- [x] Chạy lại test (test_auth, test_family) — đảm bảo không regression (đặc biệt các test đang assert login không có user → cập nhật assertion nếu cần)

## Verification
- `python -c "from create_app import create_app; create_app()"` OK
- Smoke sequence (TestClient/curl):
  - `POST /auth/register` → `POST /auth/login` trả JSON có `user` object
  - `POST /auth/verify-email` không 404
  - `PUT /users/me` cập nhật được profile
  - `POST /families/{id}/branches` tạo branch (BranchRepository)
  - `POST /families/{id}/events` trả event thật từ DB (không stub)
  - `GET /events/{id}/participants` 200
  - `PUT /families/{id}` payload `{action:'approve_join_request'}` không 422
  - `GET /admin/users`, `GET /families/{id}/heritage/documents` không 404 (đổi prefix)
- Frontend (user tự test, không commit): set `VITE_MOCK=false` trong `.env.local` → các screen gọi API thật hoạt động
