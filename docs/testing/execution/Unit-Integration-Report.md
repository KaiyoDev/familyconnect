# Unit & Integration Test Report — FamilyConnect

> **Project:** FamilyConnect — Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo  
> **Version:** v1.0  
> **Date:** 2025-09-15  
> **Tester:** Automated Test Suite  

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases** | 213 |
| **Passed** | **206 (96.7%)** |
| **Failed** | **7 (3.3%)** |
| **Blocked** | 0 |
| **Not Run** | 0 |
| **Overall Coverage** | **82%** (backend source) |
| **Defects Found** | **2** |

> ⚠️ **Note:** 7 failures are all in `backend/tests/test_auth.py` — integration tests testing endpoints `/api/auth/register`, `/api/auth/login`, `/api/auth/profile` that **do not exist** in the current backend implementation. The `auth_controller.py` only exposes `/auth/forgot-password`, `/auth/reset-password`, `/auth/refresh`.

---

## 2. Test Scope

### 2.1 Unit Tests (160 tests — ALL PASSED)

| Module | Test File | Tests | Coverage (module) |
|--------|-----------|-------|-------------------|
| **Domain Utils** (password, JWT) | `tests/unit/domain/test_domain_utils.py` | 8 | 100% |
| **Repositories — User/Admin/Family** | `tests/unit/repositories/test_repositories.py` | 25 | 69–97% |
| **Repositories — AI** | `tests/unit/repositories/test_ai_repository.py` | 7 | 100% |
| **Repositories — Post/Comment/Reaction/Event/Branch/Member/Relationship** | `tests/unit/repositories/test_community_event_repos.py` | 25 | 78–100% |
| **Repositories — RSVP** | `tests/unit/repositories/test_rsvp_repository.py` | 4 | 100% |
| **Service — Auth & Admin** | `tests/unit/services/test_auth_admin_service.py` | 26 | 91–98% |
| **Service — Community** | `tests/unit/services/test_community_service.py` | 21 | 99% |
| **Service — Event** | `tests/unit/services/test_event_service.py` | 17 | 100% |
| **Service — Family** | `tests/unit/services/test_family_service.py` | 12 | 84% |
| **Service — AI** | `tests/unit/services/test_ai_service.py` | 15 | 61% |

### 2.2 Integration Tests (18 tests — 11 PASSED, 7 FAILED)

> **Classification note:** `test_community.py` and `test_event.py` are written as service-layer tests with mocked repositories. They are correctly counted as additional **unit/service tests** (35 tests), not HTTP integration tests. Only 18 tests below are true API-contract integration tests using a live `TestClient` against the FastAPI app.

| Module | Test File | Type | Tests | Passed | Failed |
|--------|-----------|------|-------|--------|--------|
| **Auth (API contract)** | `tests/test_auth.py` | TestClient | 9 | 2 | 7 |
| **Family (API contract)** | `tests/test_family.py` | TestClient | 9 | 9 | 0 |
| **Community (service)** | `tests/test_community.py` | Service+mock | 19 | 19 | 0 |
| **Event (service)** | `tests/test_event.py` | Service+mock | 16 | 16 | 0 |

**Unit tests:** 160 ✅
**Service-layer tests (new):** 35 (19 + 16) ✅
**API-contract integration tests:** 18 (2 + 16 → 9 + 9 = 18)
**Total executed:** 160 + 35 + 18 = **213** (206 PASS, 7 FAIL)

---

## 3. Test Results by Module

### Module US — User & Security

Reference: `FR-US-01` through `FR-US-07`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-US-001P | FR-US-01 | Register success (API) | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-001N | FR-US-01 | Register duplicate email (API) | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-001N2 | FR-US-01 | Register weak password (validation) | **PASS** | unit (service) | — |
| TC-US-001V | FR-US-01 | Email uniqueness via API | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-002P | FR-US-02 | Login success (API) | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-002N | FR-US-02 | Login wrong password (API) | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-002N4 | FR-US-02 | Login non-existent email -> 401 no leak | **PASS** | unit test | — |
| TC-US-003P | FR-US-03 | Logout | **PASS** | unit test | — |
| TC-US-004P | FR-US-04 | Refresh token | **PASS** | unit test | — |
| TC-US-004N | FR-US-04 | Invalid refresh token -> 401 | **PASS** | unit test | — |
| TC-US-006P | FR-US-06 | Get profile (with token, API) | **FAIL** | [log](evidence/unit-integration/all-tests-full.log) | BUG-002 |
| TC-US-006N | FR-US-06 | Profile not found (service) | **PASS** | unit test | — |
| TC-US-007P | FR-US-07 | Forgot password | **PASS** | unit test | — |
| TC-US-007N | FR-US-07 | Forgot password (non-existent, no leak) | **PASS** | unit test | — |

### Module FG — Family & Genealogy Management

Reference: `FR-FG-01` through `FR-FG-04`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-FG-001P | FR-FG-01 | Create family (service) | **PASS** | unit test | — |
| TC-FG-001P | FR-FG-01 | Create family (repository) | **PASS** | unit test | — |
| TC-FG-001N | FR-FG-01 | Get non-existent family | **PASS** | unit test | — |
| TC-FG-001P2 | FR-FG-01 | Update family | **PASS** | unit test | — |
| TC-FG-001P3 | FR-FG-01 | Delete family | **PASS** | unit test | — |
| TC-FG-001V | FR-FG-01 | Reject branch from another family | **PASS** | unit test | — |
| TC-FG-002P | FR-FG-02 | Add member to valid branch | **PASS** | unit test | — |
| TC-FG-003P | FR-FG-03 | Add parent-child relationship | **PASS** | unit test | — |
| TC-FG-003P2 | FR-FG-03 | Add marriage relationship | **PASS** | unit test | — |
| TC-FG-003V | FR-FG-03 | Self-relationship rejected | **PASS** | unit test | — |
| TC-FG-003V2 | FR-FG-03 | Invalid relationship type | **PASS** | unit test | — |
| TC-FG-004P | FR-FG-04 | Genealogy tree | **PASS** | unit test | — |
| TC-FG-004P2 | FR-FG-04 | Relationship lookup | **PASS** | unit test | — |

### Module COM — Community

Reference: `FR-COM-01` through `FR-COM-05`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-COM-001P | FR-COM-01 | Create post (normal) | **PASS** | unit test | — |
| TC-COM-001N | FR-COM-01 | Create post empty content | **PASS** | unit test | — |
| TC-COM-001N2 | FR-COM-01 | Non-author update → Forbidden | **PASS** | unit test | — |
| TC-COM-001P2 | FR-COM-01 | Author updates own post | **PASS** | unit test | — |
| TC-COM-001P3 | FR-COM-01 | Author deletes own post | **PASS** | unit test | — |
| TC-COM-001N2 | FR-COM-01 | Non-author delete → Forbidden | **PASS** | unit test | — |
| TC-COM-003P | FR-COM-03 | Get feed | **PASS** | unit test | — |
| TC-COM-001N | FR-COM-03 | Invalid page → ValidationError | **PASS** | unit test | — |
| TC-COM-002P | FR-COM-02 | Add comment | **PASS** | unit test | — |
| TC-COM-002N | FR-COM-02 | Empty comment → ValidationError | **PASS** | unit test | — |
| TC-COM-002N2 | FR-COM-02 | Comment >1000 chars | **PASS** | unit test | — |
| TC-COM-002P2 | FR-COM-02 | Add reaction LIKE | **PASS** | unit test | — |
| TC-COM-002N | FR-COM-02 | Invalid reaction type | **PASS** | unit test | — |
| TC-COM-002V | FR-COM-02 | Duplicate reaction → ConflictError | **PASS** | unit test | — |
| TC-COM-002E | FR-COM-02 | IntegrityError → ConflictError | **PASS** | unit test | — |
| TC-COM-002N | FR-COM-02 | Remove non-existent reaction | **PASS** | unit test | — |
| TC-COM-005P | FR-COM-05 | Create announcement | **PASS** | unit test | — |
| TC-COM-005N | FR-COM-05 | Announcement empty content | **PASS** | unit test | — |

### Module EVT — Events

Reference: `FR-EVT-01` through `FR-EVT-05`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-EVT-001P | FR-EVT-01 | Create event | **PASS** | unit test | — |
| TC-EVT-001P2 | FR-EVT-01 | List events | **PASS** | unit test | — |
| TC-EVT-001E | FR-EVT-01 | List events (empty) | **PASS** | unit test | — |
| TC-EVT-001P3 | FR-EVT-01 | Get event by ID | **PASS** | unit test | — |
| TC-EVT-001N | FR-EVT-01 | Event not found → 404 | **PASS** | unit test | — |
| TC-EVT-001V | FR-EVT-01 | Update event | **PASS** | unit test | — |
| TC-EVT-001N2 | FR-EVT-01 | Update non-existent → 404 | **PASS** | unit test | — |
| TC-EVT-001N3 | FR-EVT-01 | Cancel non-existent → 404 | **PASS** | unit test | — |
| TC-EVT-002P | FR-EVT-02 | RSVP "going" | **PASS** | unit test | — |
| TC-EVT-002P2 | FR-EVT-02 | RSVP "maybe" | **PASS** | unit test | — |
| TC-EVT-002N | FR-EVT-02 | RSVP "not_going" | **PASS** | unit test | — |
| TC-EVT-002N2 | FR-EVT-02 | Invalid RSVP status → 400 | **PASS** | unit test | — |
| TC-EVT-002V | FR-EVT-02 | Update existing RSVP | **PASS** | unit test | — |
| TC-EVT-003P | FR-EVT-03 | Get all attendees | **PASS** | unit test | — |
| TC-EVT-003P2 | FR-EVT-03 | Filter attendees by status | **PASS** | unit test | — |
| TC-EVT-003E | FR-EVT-03 | No attendees (empty) | **PASS** | unit test | — |
| TC-EVT-005P | FR-EVT-05 | Send reminder | **PASS** | unit test | — |

### Module AI — AI-assisted Services

Reference: `FR-AI-01` through `FR-AI-04`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-AI-001P | FR-AI-01 | Semantic search returns results | **PASS** | unit test | — |
| TC-AI-001N | FR-AI-01 | Semantic search no results | **PASS** | unit test | — |
| TC-AI-002P | FR-AI-02 | Create conversation | **PASS** | unit test | — |
| TC-AI-002P2 | FR-AI-02 | Get conversation with messages | **PASS** | unit test | — |
| TC-AI-002N | FR-AI-02 | Conversation not found | **PASS** | unit test | — |
| TC-AI-002P3 | FR-AI-02 | List conversations | **PASS** | unit test | — |
| TC-AI-002P4 | FR-AI-02 | Delete conversation | **PASS** | unit test | — |
| TC-AI-002N2 | FR-AI-02 | Delete non-existent | **PASS** | unit test | — |
| TC-AI-002P5 | FR-AI-02 | Chat (mock provider) | **PASS** | unit test | — |
| TC-AI-003P | FR-AI-03 | Explain parent-child | **PASS** | unit test | — |
| TC-AI-003P2 | FR-AI-03 | Explain marriage | **PASS** | unit test | — |
| TC-AI-004P | FR-AI-04 | Summarize (short/medium/full) | **PASS** | unit test | — |
| TC-AI-004N | FR-AI-04 | Invalid length mode | **PASS** | unit test | — |

### Module ADM — Administration

Reference: `FR-ADM-01` through `FR-ADM-05`

| TC ID | Requirement | Feature | Status | Evidence | Defect |
|:-----:|:-----------:|---------|:------:|:--------:|:------:|
| TC-ADM-001P | FR-ADM-01 | List users (pagination) | **PASS** | unit test | — |
| TC-ADM-005N | FR-ADM-05 | Invalid page_size → ValidationError | **PASS** | unit test | — |
| TC-ADM-001P2 | FR-ADM-01 | Activate/block user | **PASS** | unit test | — |
| TC-ADM-001N | FR-ADM-01 | Invalid status → ValidationError | **PASS** | unit test | — |
| TC-ADM-001N2 | FR-ADM-01 | User not found | **PASS** | unit test | — |
| TC-ADM-001P3 | FR-ADM-01 | Suspend user | **PASS** | unit test | — |
| TC-ADM-003P | FR-ADM-03 | Get audit log | **PASS** | unit test | — |
| TC-ADM-002P | FR-ADM-02 | Moderate post → REMOVED | **PASS** | unit test | — |
| TC-ADM-002N | FR-ADM-02 | Invalid content type | **PASS** | unit test | — |
| TC-ADM-005P | FR-ADM-05 | Update system config | **PASS** | unit test | — |

---

## 4. Defect Report

### Defect BUG-001: Missing Route Registration in `register_routes()`

| Field | Value |
|-------|-------|
| **ID** | **BUG-001** |
| **Severity** | 🔴 **Critical** |
| **Status** | **Fixed** |
| **Location** | `backend/app/api/routes.py` — `register_routes()` |
| **Description** | The `register_routes()` function imports 9 routers (`health`, `auth`, `event`, `community`, `ai`, `admin`, `heritage`, `directory`, `family`) but only registers `heritage` and `directory` via `app.include_router()`. The other 7 routers are imported but never attached to the application, making all their endpoints return 404. |
| **Impact** | All auth, event, community, AI, admin, health, and family endpoints are inaccessible. Frontend calls to these APIs fail with 404. |
| **Fix** | Added missing `app.include_router()` calls for all 7 routers. Committed in `routes.py`. |
| **Evidence** | All integration tests except `test_auth.py` now pass. Previously all 7 missing routers returned 404; after fix, only the auth-specific tests fail due to BUG-002. |

### Defect BUG-002: Missing Auth Endpoints (Register/Login/Profile)

| Field | Value |
|-------|-------|
| **ID** | **BUG-002** |
| **Severity** | 🔴 **Critical** |
| **Status** | **Unresolved** |
| **Location** | `backend/app/api/controllers/auth_controller.py` |
| **Description** | The auth controller only implements 3 endpoints (`/auth/forgot-password`, `/auth/reset-password`, `/auth/refresh`). Frontend (`frontend/src/services/api.ts`) calls the following missing endpoints: `POST /auth/register`, `POST /auth/login`, `POST /auth/logout`, `POST /auth/verify-email`, `GET /users/me`. The corresponding service layer (`AuthService` in `app/services/auth_service.py`) has full implementations for register, login, logout, get_profile, update_profile, refresh_token, forgot_password, reset_password — but the controller doesn't expose them. |
| **Impact** | Users cannot register, login, or view their profile via the API. The application is unusable for end users. |
| **Affected Tests** | 7 integration tests in `test_auth.py` fail with 404 |
| **Evidence** | [all-tests-full.log](evidence/unit-integration/all-tests-full.log) |

---

## 5. Coverage Report

### 5.1 Overall Coverage

| Metric | Value |
|--------|-------|
| **Lines Covered** | 3,629 / 4,446 |
| **Coverage %** | **82%** |
| **Missing Lines** | 817 |

### 5.2 Coverage by Service Module

| Service | Coverage | Missed Lines |
|---------|:--------:|:------------:|
| `auth_service.py` | **98%** | 43 |
| `community_service.py` | **99%** | 170 |
| `event_service.py` | **100%** | — |
| `family_service.py` | **84%** | 23, 34, 37-43, 52, 64, 96, 107, 118, 126-130 |
| `admin_service.py` | **91%** | 47, 57, 61, 63, 67 |
| `ai_service.py` | **61%** | 35-46, 54-63, 120-153, 210-211 |

### 5.3 Coverage by Repository Module

| Repository | Coverage | Missed Lines |
|------------|:--------:|:------------:|
| `user_repository.py` | **95%** | 35-36 |
| `admin_repository.py` | **97%** | 68, 82 |
| `family_repository.py` | **69%** | 28-29, 32-33, 36-39, 42-45, 48-51 |
| `post_repository.py` | **91%** | 79, 82, 85 |
| `comment_repository.py` | **89%** | 37-41 |
| `reaction_repository.py` | **100%** | — |
| `event_repository.py` | **97%** | 30 |
| `rsvp_repository.py` | **100%** | — |
| `ai_repository.py` | **100%** | — |
| `branch_repository.py` | **83%** | 28-29, 32-33 |
| `member_repository.py` | **78%** | 14, 28-29, 32-33 |
| `relationship_repository.py` | **78%** | 14, 31-32, 35-36 |

---

## 6. Key Observations

### 6.1 Strengths
- ✅ **High coverage** on core business logic: Event (100%), Community (99%), Auth (98%), Admin (91%)
- ✅ **Comprehensive validation** on test cases: normal, boundary, edge case, and error handling covered
- ✅ **Fake/in-memory repositories** used for FamilyService tests — clean separation of concerns
- ✅ **Async mocking** correctly used for all async repository/service interactions
- ✅ **Integration test framework** (FastAPI TestClient + SQLite) works for endpoint contract testing

### 6.2 Issues Found
- ⚠️ **7 tests fail** due to missing auth endpoints (BUG-002)
- ⚠️ **Deprecation warnings** for `datetime.utcnow()` in 3 repository files (ai, rsvp)
- ⚠️ **Pydantic V2 deprecation** for class-based `Config` in `app/schemas/auth.py`
- ⚠️ **Low coverage areas**: `directory_service.py` (20%), `heritage_service.py` (40%), `directory_repository.py` (39%), `heritage_repository.py` (25%)
- ⚠️ **No frontend tests** exist (React components have no `.test.tsx` files)

### 6.3 Missing Test Areas
- **Directory module** — no unit or integration tests
- **Heritage module** — no unit or integration tests
- **Frontend** — no component/unit tests
- **Dashboard** — no tests
- **API contract tests** for Family, Event, Community controllers
- **Load/performance tests** (P95 < 3s for login)

---

## 7. Environment

| Component | Version |
|-----------|---------|
| Python | 3.14.5 |
| pytest | 9.1.1 |
| pytest-cov | 7.1.0 |
| pytest-asyncio | 1.4.0 |
| FastAPI | 0.139.2 |
| SQLAlchemy | 2.0.51 |
| Coverage.py | 7.16.1 |
| OS | macOS (Darwin) |

---

## 8. Appendix

### 8.1 File Structure

```
docs/testing/
├── Test-Cases.md
├── execution/
│   └── Unit-Integration-Report.md          ← this file
└── evidence/
    └── unit-integration/
        ├── unit-tests-full.log             ← full pytest output (unit only)
        ├── all-tests-full.log              ← full pytest output (all tests)
        └── all-tests-summary.log           ← PASS/FAIL summary per test
```

### 8.2 Run Commands

```bash
# Run unit tests only
DATABASE_URL="sqlite+aiosqlite:///./test.db" python3 -m pytest backend/tests/unit/ --cov=backend --cov-report=term-missing

# Run all tests (unit + integration)
DATABASE_URL="sqlite+aiosqlite:///./test.db" python3 -m pytest backend/tests/ --cov=backend --cov-report=term-missing
```

### 8.3 Author

- **Role:** Automated Test Suite (pi coding agent)
- **Reviewed by:** (pending)