# Testing - FamilyConnect

> **Thư mục:** `docs/testing/`
> **Phiên bản:** v1.0
> **Cập nhật lần cuối:** 2026-08-20

---

## Tổng quan

Thư mục này chứa toàn bộ tài liệu kiểm thử cho dự án FamilyConnect. Đây là nguồn tham chiếu duy nhất (single source of truth) cho hoạt động kiểm thử, bao gồm test case, ma trận truy xuất, test data, automation scripts và infrastructure tests.

---

## Cấu trúc thư mục

```
docs/testing/
├── README.md                                              # Tài liệu này
├── Test-Cases.md                                          # 206 test cases chi tiết (9 modules)
├── RTM.md                                                 # Ma trận truy xuất nguồn gốc
│
├── test-data/                                             # Dữ liệu test mẫu
│   ├── sample-family.json                                 # Gia đình mẫu: 8 thành viên, 4 thế hệ, 2 nhánh
│   └── sample-users.json                                  # Người dùng mẫu: 7 users với các vai trò
│
├── infrastructure/                                        # Kiểm thử hạ tầng & NFR
│   └── Infrastructure-Tests.md                            # Test NFR-01, 04, 07, 09, 10
│
└── automation/                                            # Script tự động hóa
    ├── test_familyconnect.py                              # Pytest suite (API tests)
    ├── familyconnect-postman-collection.json               # Postman collection (API tests)
    ├── run-all-tests.sh                                   # Test runner tổng hợp
    └── responsive.spec.js                                 # Playwright responsive tests (NFR-01)
```

---

## Thống kê

| Hạng mục | Số lượng | Ghi chú |
|----------|:--------:|---------|
| **Total Test Cases** | 206 | 9 modules |
| Positive (P) | 84 | 41% |
| Negative (N) | 54 | 26% |
| Authorization (A) | 31 | 15% |
| Validation (V) | 24 | 12% |
| Boundary (B) | 7 | 3% |
| Edge Case (E) | 6 | 3% |
| **FR Coverage** | 49/49 (100%) | ✅ |
| **BR Coverage** | 34/34 (100%) | ✅ |
| **UC Coverage** | 12/12 (100%) | ✅ |
| **NFR Coverage** | 11/13 (85%) | ⚠️ |

---

## Cách sử dụng

### 1. Chạy API tests (pytest)

```bash
# Yêu cầu: Backend đang chạy, Python with pytest + httpx
pip install pytest httpx pytest-cov pytest-html

# Chạy toàn bộ test suite
cd docs/testing/automation
pytest test_familyconnect.py -v --cov=backend --cov-report=html --html=report.html

# Chạy theo module
pytest test_familyconnect.py -v -k "TestUserSecurity"
pytest test_familyconnect.py -v -k "TestFamilyGenealogy"
pytest test_familyconnect.py -v -k "TestCommunity or TestAIServices"

# Chạy một test cụ thể
pytest test_familyconnect.py::TestUserSecurity::test_us_001_register_success -v
```

### 2. Chạy Postman collection

```bash
# Yêu cầu: Newman installed (npm install -g newman)
newman run docs/testing/automation/familyconnect-postman-collection.json \
  --env-var "base_url=http://localhost:8000/api/v1" \
  --reporters cli,json \
  --reporter-json-export postman-report.json \
  --delay-request 100
```

### 3. Chạy Responsive tests (Playwright)

```bash
# Yêu cầu: Node.js, Playwright
npm install -D @playwright/test
npx playwright install

# Chạy responsive tests
npx playwright test --config=playwright.config.js docs/testing/automation/responsive.spec.js

# Xem báo cáo
npx playwright show-report
```

### 4. Chạy Infrastructure tests

```bash
# Docker health check
./docs/testing/automation/run-all-tests.sh --docker

# Database integrity
psql -U fc_user -d familyconnect -f docs/testing/infrastructure/db-integrity-check.sql

# Load test (k6)
k6 run docs/testing/infrastructure/load-test.js
```

### 5. Chạy tất cả

```bash
./docs/testing/automation/run-all-tests.sh
```

---

## Quy ước

### Test Case ID

```
TC-<MODULE>-<STT><LOẠI>
```

| Module code | Module |
|:-----------:|--------|
| US | User & Security |
| FG | Family & Genealogy |
| COM | Community |
| EVT | Events |
| DIR | Family Directory |
| HER | Family Heritage |
| AI | AI-assisted Services |
| DASH | Dashboard & Reporting |
| ADM | Administration |
| NFR | Non-Functional Requirements |

| Loại | Ý nghĩa |
|:----:|---------|
| P | Positive |
| N | Negative |
| A | Authorization / RBAC |
| V | Validation / Business Rule |
| B | Boundary |
| E | Edge Case |

### Trạng thái

| Status | Ý nghĩa |
|--------|---------|
| `PASS` | Test passed |
| `FAIL` | Test failed |
| `BLOCKED` | Bị chặn (phụ thuộc khác chưa xong) |
| `NOT RUN` | Chưa thực thi |

### Bug ID & Evidence

```
Bug:     BUG-<MODULE>-<STT>          (ví dụ: BUG-US-001)
Evidence: evidence/<MODULE>/<TC-ID>.<ext>   (ví dụ: evidence/US/TC-US-001P.png)
```

---

## Test Data

### sample-family.json

Gia đình mẫu với 4 thế hệ, 8 thành viên, 2 nhánh, 9 quan hệ:

```
Thế hệ 1: Ông Tổ (1940) + Bà Cố (1945)      ← Nhánh Chi trưởng
Thế hệ 2: Cha (1965) + Mẹ (1968)            ← Nhánh Chi trưởng
          Chú (1970) + Thím (1972)           ← Nhánh Chi thứ
Thế hệ 3: Con (1995)                         ← Nhánh Chi trưởng
Thế hệ 4: Cháu (2020)                        ← Nhánh Chi trưởng
```

### sample-users.json

| User | Vai trò | Trạng thái |
|------|---------|:----------:|
| admin@familyconnect.com | ADMIN | ACTIVE |
| owner@example.com | FAMILY_OWNER | ACTIVE |
| memberB@example.com | FAMILY_MEMBER | ACTIVE |
| memberC@example.com | FAMILY_MEMBER | ACTIVE |
| guestD@example.com | USER | PENDING |
| blockedE@example.com | USER | BLOCKED |
| inactiveF@example.com | USER | INACTIVE |

---

## Các NFR còn thiếu

| NFR | Lý do chưa test | Hướng dẫn |
|-----|----------------|------------|
| **NFR-02** Cross-platform Mobile | Ngoài phạm vi MVP | Khi có mobile app, cần test trên iOS Simulator + Android Emulator |
| **NFR-05** Modular Architecture | Cần static analysis | Chạy `dependency-cruiser` cho frontend, `pylint` với plugin cho backend |
| **NFR-13** Test Coverage | Cần chạy code | Chạy `pytest --cov=backend --cov-report=term` và đảm bảo ≥ 70% |

---

## Các file liên quan

| File | Mô tả |
|------|-------|
| `../SRS/04_FunctionalRequirements.md` | 49 Functional Requirements |
| `../SRS/05_NonFunctionalRequirements.md` | 13 Non-Functional Requirements |
| `../SRS/08_BusinessRules.md` | 34 Business Rules |
| `../SRS/07_UseCaseSpecification.md` | 12 Use Cases |