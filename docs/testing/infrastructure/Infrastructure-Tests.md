# Infrastructure & Non-Functional Testing - FamilyConnect

> **Tài liệu:** Kiểm thử cơ sở hạ tầng và yêu cầu phi chức năng
> **Phiên bản:** v1.0

---

## 1. Tổng quan

Tài liệu này bổ sung các test case cho **6 NFR** chưa được bao phủ trong functional test:

| NFR ID | NFR Name | Loại test | Công cụ đề xuất |
|--------|----------|-----------|-----------------|
| NFR-01 | Responsive Web Application | UI/Responsive | Playwright / Cypress |
| NFR-04 | RESTful API Architecture | API Contract | Postman/Newman + OpenAPI |
| NFR-05 | Modular Software Architecture | Code Structure | SonarQube / manual review |
| NFR-07 | PostgreSQL Database | Data Integrity | pytest + SQL tests |
| NFR-09 | Docker Deployment | Container | Docker Compose + health checks |
| NFR-10 | High Availability | Resilience | k6 / Locust + uptime monitoring |

---

## 2. Test Case bổ sung cho NFR

### 2.1. NFR-01: Responsive Web Application

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-NFR-001P | NFR-01 | Responsive - Desktop 1440px | 1. Mở trình duyệt Chrome/Firefox/Edge.<br>2. Thiết lập viewport 1440x900. | URL: FamilyConnect Web Portal<br>Viewport: 1440x900 | 1. Mở trang đăng nhập.<br>2. Mở trang cây gia phả.<br>3. Mở trang dashboard.<br>4. Kiểm tra bố cục. | 1. Bố cục hiển thị đầy đủ.<br>2. Không có thanh cuộn ngang.<br>3. Các thành phần không bị chồng/che.<br>4. Font chữ đọc được. | NOT RUN | | |
| TC-NFR-001P2 | NFR-01 | Responsive - Tablet 768px | 1. Mở trình duyệt.<br>2. Thiết lập viewport 768x1024. | URL: FamilyConnect Web Portal<br>Viewport: 768x1024 | 1. Mở trang đăng nhập.<br>2. Mở trang cây gia phả.<br>3. Mở trang danh bạ.<br>4. Kiểm tra bố cục. | 1. Bố cục tự động chuyển sang dạng tablet.<br>2. Menu thu gọn (hamburger).<br>3. Cây gia phả vẫn thao tác được (zoom/pan).<br>4. Không có thanh cuộn ngang. | NOT RUN | | |
| TC-NFR-001P3 | NFR-01 | Responsive - Mobile 375px | 1. Mở trình duyệt.<br>2. Thiết lập viewport 375x667. | URL: FamilyConnect Web Portal<br>Viewport: 375x667 | 1. Mở trang đăng nhập.<br>2. Mở trang cộng đồng.<br>3. Mở trang sự kiện.<br>4. Kiểm tra bố cục. | 1. Bố cục dạng một cột (single column).<br>2. Form đăng nhập vừa màn hình.<br>3. Các nút bấm đủ lớn để chạm (≥ 44px).<br>4. Cuộn dọc mượt mà. | NOT RUN | | |
| TC-NFR-001N | NFR-01 | Responsive - Trình duyệt không hỗ trợ | 1. Mở IE11 hoặc trình duyệt cũ. | URL: FamilyConnect Web Portal | 1. Mở portal trên IE11. | 1. Hiển thị thông báo "Trình duyệt không được hỗ trợ. Vui lòng sử dụng Chrome/Firefox/Edge mới nhất."<br>2. Hoặc layout vẫn hoạt động ở mức cơ bản (graceful degradation). | NOT RUN | | |

---

### 2.2. NFR-04: RESTful API Architecture

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-NFR-004P | NFR-04 | API tuân thủ RESTful conventions | 1. Backend đang chạy.<br>2. Có OpenAPI spec. | OpenAPI spec file | 1. Dùng OpenAPI validator kiểm tra spec.<br>2. Gọi từng endpoint và kiểm tra HTTP methods. | 1. OpenAPI spec hợp lệ (không lỗi schema).<br>2. GET chỉ dùng để đọc, POST để tạo, PUT/PATCH để cập nhật, DELETE để xóa.<br>3. Response dùng đúng HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 500). | NOT RUN | | |
| TC-NFR-004P2 | NFR-04 | API trả về định dạng JSON | 1. Backend đang chạy. | Token: valid_jwt | 1. Gọi API GET /api/v1/families.<br>2. Kiểm tra Content-Type header. | Content-Type: application/json. Response body là JSON hợp lệ. | NOT RUN | | |
| TC-NFR-004N | NFR-04 | API không hỗ trợ định dạng khác | 1. Backend đang chạy. | Accept: application/xml | 1. Gọi API với Accept header không phải JSON. | API trả về 406 Not Acceptable hoặc ignore Accept header và vẫn trả JSON. | NOT RUN | | |

---

### 2.3. NFR-07: PostgreSQL Database

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-NFR-007P | NFR-07 | Kết nối database thành công | 1. PostgreSQL container đang chạy.<br>2. Connection string đúng. | DB: familyconnect<br>User: fc_user | 1. Kết nối đến PostgreSQL.<br>2. Chạy SELECT 1. | Kết nối thành công. Query trả về 1. | NOT RUN | | |
| TC-NFR-007P2 | NFR-07 | Kiểm tra các bảng và ràng buộc | 1. Database đã migrate. | — | 1. Liệt kê tất cả bảng.<br>2. Kiểm tra primary keys, foreign keys, unique constraints, not null constraints. | 1. Tất cả bảng theo Data Dictionary tồn tại.<br>2. Các ràng buộc được tạo đúng.<br>3. Unique constraint trên User.email.<br>4. Foreign key từ FamilyMember.user_id → User.id. | NOT RUN | | |
| TC-NFR-007N | NFR-07 | Kiểm tra truy vấn đồ thị (recursive CTE) | 1. Database có dữ liệu gia phả mẫu (≥ 5 thế hệ). | Family ID: family-A | 1. Chạy recursive CTE truy vấn tất cả hậu duệ của member-root.<br>2. Đo thời gian. | 1. Truy vấn trả về đúng danh sách hậu duệ.<br>2. Thời gian < 500ms cho 1000 node. | NOT RUN | | |

---

### 2.4. NFR-09: Docker Deployment

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-NFR-009P | NFR-09 | Docker build thành công | 1. Docker installed.<br>2. Dockerfile tồn tại. | docker-compose.yml | 1. Chạy `docker compose build`.<br>2. Kiểm tra exit code. | Build thành công (exit code 0). Các image được tạo. | NOT RUN | | |
| TC-NFR-009P2 | NFR-09 | Docker compose up thành công | 1. Docker images đã build.<br>2. Ports không bị conflict. | docker-compose.yml | 1. Chạy `docker compose up -d`.<br>2. Kiểm tra container status. | 1. Tất cả container ở trạng thái Up (healthy).<br>2. Health check endpoint trả về 200.<br>3. Log không có lỗi critical. | NOT RUN | | |
| TC-NFR-009N | NFR-09 | Restart container giữ dữ liệu | 1. Container đang chạy.<br>2. Đã insert dữ liệu test vào DB. | Sample data | 1. Chạy `docker compose restart`.<br>2. Kiểm tra dữ liệu vẫn còn. | 1. Dữ liệu không bị mất (volume persistent).<br>2. App hoạt động bình thường sau restart. | NOT RUN | | |
| TC-NFR-009V | NFR-09 | Kiểm tra docker-compose.yml cấu hình đúng | 1. Docker installed. | docker-compose.yml | 1. Chạy `docker compose config`.<br>2. Kiểm tra output. | 1. File cấu hình hợp lệ (không lỗi YAML).<br>2. Các service: backend, frontend, database, ai-service được định nghĩa.<br>3. Volume cho database được mount.<br>4. Network cho phép các service giao tiếp. | NOT RUN | | |

---

### 2.5. NFR-10: High Availability

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-NFR-010P | NFR-10 | Health check endpoint hoạt động | 1. App đang chạy. | URL: /api/v1/health | 1. Gọi GET /api/v1/health. | 1. Response 200 OK.<br>2. Body JSON: `{ "status": "healthy", "uptime": 12345, "db": "connected", "ai_service": "available" }`.<br>3. Thời gian phản hồi < 500ms. | NOT RUN | | |
| TC-NFR-010P2 | NFR-10 | Uptime monitoring - 7 ngày | 1. App triển khai trên môi trường test ổn định.<br>2. Monitoring tool (Prometheus/UptimeRobot) cấu hình. | URL: /api/v1/health | 1. Monitor health check mỗi 5 phút trong 7 ngày.<br>2. Tính uptime. | Uptime ≥ 99% (tương đương < 1.68 giờ downtime trong 7 ngày). | NOT RUN | | |
| TC-NFR-010N | NFR-10 | Recovery sau khi crash | 1. App đang chạy.<br>2. Giả lập crash (kill process). | — | 1. Kill backend process.<br>2. Đo thời gian recovery.<br>3. Kiểm tra dữ liệu. | 1. Docker tự động restart container (restart policy).<br>2. RTO < 4 giờ (trên môi trường production).<br>3. Dữ liệu không mất (RPO < 1 giờ). | NOT RUN | | |
| TC-NFR-010V | NFR-10 | Load test cơ bản | 1. App đang chạy.<br>2. Có k6/Locust installed. | Script: load_test.js | 1. Chạy load test với 50 virtual users trong 5 phút.<br>2. Đo response time, error rate. | 1. P95 response time < 2s (NFR-12).<br>2. Error rate < 1%.<br>3. Không có timeout. | NOT RUN | | |

---

## 3. Script kiểm thử tự động

### 3.1. Docker health check script

```bash
#!/bin/bash
# docker-healthcheck.sh
# Kiểm tra tất cả container đều running

echo "=== FamilyConnect Docker Health Check ==="

# Kiểm tra docker compose
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"

# Kiểm tra từng service
SERVICES=("backend" "frontend" "database" "ai-service")
for svc in "${SERVICES[@]}"; do
    STATUS=$(docker compose ps --format "{{.Status}}" "$svc" 2>/dev/null)
    if echo "$STATUS" | grep -q "Up"; then
        echo "✅ $svc: $STATUS"
    else
        echo "❌ $svc: DOWN"
    fi
done

# Kiểm tra health endpoint
echo ""
echo "=== Health Endpoint ==="
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:8000/api/v1/health
```

### 3.2. Database integrity check script

```sql
-- db-integrity-check.sql
-- Kiểm tra ràng buộc database FamilyConnect

-- 1. Kiểm tra các bảng tồn tại
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public' 
  AND table_type = 'BASE TABLE'
ORDER BY table_name;

-- 2. Kiểm tra unique constraint trên User.email
SELECT 
    tc.constraint_name, tc.table_name, tc.constraint_type
FROM information_schema.table_constraints tc
WHERE tc.table_name = 'user' AND tc.constraint_type = 'UNIQUE';

-- 3. Kiểm tra foreign keys
SELECT
    tc.table_schema, 
    tc.table_name, 
    kc.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kc
      ON tc.constraint_name = kc.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY';

-- 4. Kiểm tra không có orphan records
SELECT 'Kiểm tra FamilyMember không có Family tương ứng:' AS check_name;
SELECT COUNT(*) FROM family_member fm
LEFT JOIN family f ON fm.family_id = f.id
WHERE f.id IS NULL;

-- 5. Kiểm tra recursive CTE cho cây gia phả
WITH RECURSIVE descendants AS (
    SELECT id, full_name, 0 AS depth
    FROM family_member
    WHERE id = 'member-grandfather'
    UNION ALL
    SELECT fm.id, fm.full_name, d.depth + 1
    FROM family_member fm
    JOIN relationship r ON r.from_member_id = d.id
    JOIN descendants d ON r.to_member_id = fm.id
    WHERE r.type = 'PARENT_CHILD'
)
SELECT * FROM descendants ORDER BY depth;
```

### 3.3. Load test script (k6)

```javascript
// load-test.js
// k6 run load-test.js
import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 10 },  // ramp up
    { duration: '3m', target: 50 },  // stress
    { duration: '1m', target: 0 },   // ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<2000'], // NFR-12: P95 < 2s
    http_req_failed: ['rate<0.01'],     // < 1% errors
  },
};

const BASE_URL = 'http://localhost:8000/api/v1';
const TOKEN = 'test-jwt-token';

export default function () {
  const headers = {
    'Authorization': `Bearer ${TOKEN}`,
    'Content-Type': 'application/json',
  };

  // Test các endpoint chính
  const endpoints = [
    { name: 'health', url: `${BASE_URL}/health`, method: 'GET' },
    { name: 'family_tree', url: `${BASE_URL}/families/family-A/tree`, method: 'GET' },
    { name: 'directory', url: `${BASE_URL}/families/family-A/members`, method: 'GET' },
    { name: 'posts', url: `${BASE_URL}/families/family-A/posts`, method: 'GET' },
    { name: 'events', url: `${BASE_URL}/families/family-A/events`, method: 'GET' },
  ];

  for (const ep of endpoints) {
    const res = http.get(ep.url, { headers });
    check(res, {
      [`${ep.name} status 200`]: (r) => r.status === 200,
      [`${ep.name} response < 2s`]: (r) => r.timings.duration < 2000,
    });
  }

  sleep(1);
}
```

---

## 4. Checklist kiểm thử NFR

| NFR | Test | Công cụ | Hoàn thành |
|-----|------|---------|:----------:|
| NFR-01 | Desktop 1440px | Playwright | ⬜ |
| NFR-01 | Tablet 768px | Playwright | ⬜ |
| NFR-01 | Mobile 375px | Playwright | ⬜ |
| NFR-01 | Cross-browser (Chrome, Firefox, Edge, Safari) | Playwright | ⬜ |
| NFR-04 | OpenAPI spec validation | OpenAPI CLI | ⬜ |
| NFR-04 | HTTP methods đúng conventions | Postman/Newman | ⬜ |
| NFR-04 | Response format JSON | Postman/Newman | ⬜ |
| NFR-04 | HTTP status codes đúng | Postman/Newman | ⬜ |
| NFR-05 | Module tách biệt (imports) | ESLint/PyLint | ⬜ |
| NFR-05 | Không có circular dependencies | madge / dependency-cruiser | ⬜ |
| NFR-07 | Database connection | pg_isready | ⬜ |
| NFR-07 | Constraints (PK, FK, Unique) | SQL script | ⬜ |
| NFR-07 | Recursive CTE performance | EXPLAIN ANALYZE | ⬜ |
| NFR-07 | Không có orphan records | SQL script | ⬜ |
| NFR-09 | Docker build | docker compose build | ⬜ |
| NFR-09 | Docker compose up | docker compose up -d | ⬜ |
| NFR-09 | Volume persistence | docker compose restart | ⬜ |
| NFR-09 | Container health check | docker compose ps | ⬜ |
| NFR-10 | Health endpoint | curl /api/v1/health | ⬜ |
| NFR-10 | Uptime monitoring (7 ngày) | Prometheus/UptimeRobot | ⬜ |
| NFR-10 | Restart after crash | docker compose restart | ⬜ |
| NFR-10 | Load test (50 VUs) | k6 | ⬜ |
| NFR-10 | RTO < 4h, RPO < 1h | Measure | ⬜ |