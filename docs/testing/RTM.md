# Requirements Traceability Matrix (RTM) - FamilyConnect

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Ma trận truy xuất nguồn gốc yêu cầu (Requirements Traceability Matrix)
> **Phiên bản:** v1.0
> **Ngày tạo:** 2026-08-20

---

## Quy ước

- **Mức bao phủ:** ✅ = Đầy đủ, ⚠️ = Một phần, ❌ = Chưa có
- **Tổng số Test Case**: ~200 TC
- **Tổng số FR**: 49
- **Tổng số BR**: 34
- **Tổng số NFR**: 13
- **Tổng số UC**: 12

---

## 1. FR ↔ Test Case

### Module 1: User & Security (US)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-US-01 | Đăng ký tài khoản | TC-US-001P, TC-US-001N, TC-US-001N2, TC-US-001N3, TC-US-001N4, TC-US-001N5, TC-US-001V, TC-US-001B, TC-US-001E | 9 | ✅ |
| FR-US-02 | Đăng nhập | TC-US-002P, TC-US-002N, TC-US-002N2, TC-US-002N3, TC-US-002N4, TC-US-002V, TC-US-002A, TC-US-002B | 8 | ✅ |
| FR-US-03 | Đăng xuất | TC-US-003P, TC-US-003N, TC-US-003A | 3 | ✅ |
| FR-US-04 | Khôi phục mật khẩu | TC-US-004P, TC-US-004N, TC-US-004N2, TC-US-004V | 4 | ✅ |
| FR-US-05 | Phân quyền truy cập theo vai trò (RBAC) | TC-US-005P, TC-US-005P2, TC-US-005A, TC-US-005A2, TC-US-005A3, TC-US-005A4, TC-US-005E | 7 | ✅ |
| FR-US-06 | Quản lý hồ sơ cá nhân | TC-US-006P, TC-US-006N, TC-US-006N2, TC-US-006N3, TC-US-006B, TC-US-006V | 6 | ✅ |
| FR-US-07 | Xác thực thành viên gia đình | TC-US-007P, TC-US-007N, TC-US-007A, TC-US-007N2, TC-US-007E, TC-US-007V | 6 | ✅ |

### Module 2: Family & Genealogy Management (FG)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-FG-01 | Quản lý gia đình | TC-FG-001P, TC-FG-001N, TC-FG-001N2, TC-FG-001P2, TC-FG-001P3, TC-FG-001N3, TC-FG-001N4, TC-FG-001A, TC-FG-001B | 9 | ✅ |
| FR-FG-02 | Quản lý nhánh gia đình | TC-FG-002P, TC-FG-002N, TC-FG-002N2, TC-FG-002A, TC-FG-002V | 5 | ✅ |
| FR-FG-03 | Quản lý thành viên gia đình | TC-FG-003P, TC-FG-003P2, TC-FG-003N, TC-FG-003N2, TC-FG-003A, TC-FG-003V, TC-FG-003A2 | 7 | ✅ |
| FR-FG-04 | Quản lý quan hệ cha mẹ - con | TC-FG-004P, TC-FG-004N, TC-FG-004N2, TC-FG-004V, TC-FG-004P2 | 5 | ✅ |
| FR-FG-05 | Quản lý hôn nhân | TC-FG-005P, TC-FG-005N, TC-FG-005P2, TC-FG-005A | 4 | ✅ |
| FR-FG-06 | Xem cây gia phả tương tác | TC-FG-006P, TC-FG-006P2, TC-FG-006N, TC-FG-006A, TC-FG-006V | 5 | ✅ |
| FR-FG-07 | Trực quan hóa quan hệ | TC-FG-007P, TC-FG-007P2, TC-FG-007E | 3 | ✅ |
| FR-FG-08 | Tra cứu quan hệ | TC-FG-008P, TC-FG-008N, TC-FG-008N2, TC-FG-008V, TC-FG-008A | 5 | ✅ |

### Module 3: Community (COM)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-COM-01 | Đăng và quản lý bài viết | TC-COM-001P, TC-COM-001P2, TC-COM-001N, TC-COM-001A, TC-COM-001A2, TC-COM-001P3, TC-COM-001N2, TC-COM-001B, TC-COM-001B2 | 9 | ✅ |
| FR-COM-02 | Bình luận và thả cảm xúc | TC-COM-002P, TC-COM-002P2, TC-COM-002N, TC-COM-002A, TC-COM-002V, TC-COM-002V2 | 6 | ✅ |
| FR-COM-03 | Chia sẻ tin tức gia đình | TC-COM-003P, TC-COM-003N, TC-COM-003P2 | 3 | ✅ |
| FR-COM-04 | Chia sẻ hình ảnh | TC-COM-004P, TC-COM-004N, TC-COM-004B, TC-COM-004V | 4 | ✅ |
| FR-COM-05 | Thông báo gia đình | TC-COM-005P, TC-COM-005A, TC-COM-005P2, TC-COM-005P3, TC-COM-005A2 | 5 | ✅ |

### Module 4: Events (EVT)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-EVT-01 | Tạo sự kiện gia đình | TC-EVT-001P, TC-EVT-001N, TC-EVT-001A, TC-EVT-001P2, TC-EVT-001V, TC-EVT-001N2 | 6 | ✅ |
| FR-EVT-02 | Xác nhận tham dự (RSVP) | TC-EVT-002P, TC-EVT-002N, TC-EVT-002V, TC-EVT-002P2 | 4 | ✅ |
| FR-EVT-03 | Quản lý người tham gia | TC-EVT-003P, TC-EVT-003P2, TC-EVT-003P3, TC-EVT-003A | 4 | ✅ |
| FR-EVT-04 | Thư viện ảnh sự kiện | TC-EVT-004P, TC-EVT-004A | 2 | ✅ |
| FR-EVT-05 | Nhắc nhở sự kiện | TC-EVT-005P, TC-EVT-005P2, TC-EVT-005N, TC-EVT-005V | 4 | ✅ |

### Module 5: Family Directory (DIR)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-DIR-01 | Danh bạ thành viên | TC-DIR-001P, TC-DIR-001A, TC-DIR-001V | 3 | ✅ |
| FR-DIR-02 | Hồ sơ nghề nghiệp | TC-DIR-002P | 1 | ✅ |
| FR-DIR-03 | Hồ sơ học vấn | TC-DIR-003P, TC-DIR-003N, TC-DIR-003V | 3 | ✅ |
| FR-DIR-04 | Tìm kiếm theo nghề nghiệp, địa điểm, thế hệ | TC-DIR-004P, TC-DIR-004P2, TC-DIR-004N, TC-DIR-004V | 4 | ✅ |

### Module 6: Family Heritage (HER)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-HER-01 | Quản lý tư liệu lịch sử | TC-HER-001P, TC-HER-001N, TC-HER-001V, TC-HER-001A | 4 | ✅ |
| FR-HER-02 | Quản lý câu chuyện gia đình | TC-HER-002P, TC-HER-002P2 | 2 | ✅ |
| FR-HER-03 | Quản lý thành viên tiêu biểu | TC-HER-003P, TC-HER-003N, TC-HER-003A | 3 | ✅ |
| FR-HER-04 | Thư viện ảnh gia đình | TC-HER-004P, TC-HER-004P2, TC-HER-004V | 3 | ✅ |
| FR-HER-05 | Kho lưu trữ số | TC-HER-005P, TC-HER-005P2, TC-HER-005A | 3 | ✅ |

### Module 7: AI-assisted Services (AI)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-AI-01 | Tìm kiếm ngữ nghĩa bằng AI | TC-AI-001P, TC-AI-001N, TC-AI-001N2, TC-AI-001A | 4 | ✅ |
| FR-AI-02 | Trợ lý tri thức gia đình (AI Assistant) | TC-AI-002P, TC-AI-002N, TC-AI-002N2, TC-AI-002V | 4 | ✅ |
| FR-AI-03 | Giải thích quan hệ gia đình | TC-AI-003P, TC-AI-003N | 2 | ✅ |
| FR-AI-04 | Tóm tắt nội dung bằng AI | TC-AI-004P, TC-AI-004N | 2 | ✅ |
| FR-AI-05 | Gợi ý thành viên và tài nguyên gia đình | TC-AI-005P, TC-AI-005N, TC-AI-005V | 3 | ✅ |

### Module 8: Dashboard & Reporting (DASH)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-DASH-01 | Thống kê gia đình | TC-DASH-001P, TC-DASH-001A, TC-DASH-001E | 3 | ✅ |
| FR-DASH-02 | Bảng điều khiển hoạt động cộng đồng | TC-DASH-002P, TC-DASH-002E | 2 | ✅ |
| FR-DASH-03 | Thống kê sự kiện | TC-DASH-003P | 1 | ✅ |
| FR-DASH-04 | Thống kê nhân khẩu | TC-DASH-004P | 1 | ✅ |
| FR-DASH-05 | Tạo và xuất báo cáo | TC-DASH-005P, TC-DASH-005P2, TC-DASH-005P3, TC-DASH-005A | 4 | ✅ |

### Module 9: Administration (ADM)

| FR ID | FR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| FR-ADM-01 | Quản lý người dùng | TC-ADM-001P, TC-ADM-001P2, TC-ADM-001P3, TC-ADM-001P4, TC-ADM-001N, TC-ADM-001A | 6 | ✅ |
| FR-ADM-02 | Kiểm duyệt nội dung | TC-ADM-002P, TC-ADM-002P2, TC-ADM-002P3 | 3 | ✅ |
| FR-ADM-03 | Nhật ký kiểm toán (Audit Log) | TC-ADM-003P, TC-ADM-003P2, TC-ADM-003V, TC-ADM-003A | 4 | ✅ |
| FR-ADM-04 | Sao lưu và phục hồi | TC-ADM-004P, TC-ADM-004P2, TC-ADM-004N | 3 | ✅ |
| FR-ADM-05 | Cấu hình hệ thống | TC-ADM-005P, TC-ADM-005N, TC-ADM-005A, TC-ADM-005P2, TC-ADM-005P3 | 5 | ✅ |

---

## 2. BR ↔ Test Case

| BR ID | BR Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| BR-US-001 | Email phải là duy nhất | TC-US-001P, TC-US-001N, TC-US-001V | 3 | ✅ |
| BR-US-002 | Mật khẩu phải đạt độ mạnh tối thiểu | TC-US-001P, TC-US-001N2, TC-US-004P, TC-US-004V | 4 | ✅ |
| BR-US-003 | Tài khoản phải kích hoạt trước khi đăng nhập | TC-US-001P, TC-US-001N5, TC-US-002P, TC-US-002N2, TC-US-002V | 5 | ✅ |
| BR-US-004 | Quyền truy cập theo vai trò (RBAC) | TC-US-005P, TC-US-005P2, TC-US-005A, TC-US-005A2, TC-US-005A3, TC-US-005A4, TC-US-005E | 7 | ✅ |
| BR-US-005 | Một người dùng chỉ có một hồ sơ cá nhân | TC-US-006P, TC-US-006V | 2 | ✅ |
| BR-US-006 | Phiên làm việc phải kết thúc khi đăng xuất | TC-US-003P, TC-US-003N | 2 | ✅ |
| BR-FG-001 | Chỉ Family Owner mới được duyệt thành viên | TC-US-007P, TC-US-007N, TC-US-007A, TC-US-007V, TC-FG-003P, TC-FG-003A, TC-FG-003A2 | 7 | ✅ |
| BR-FG-002 | Mỗi Family chỉ có một Family Owner | TC-FG-001P, TC-FG-001P3, TC-FG-001N3 | 3 | ✅ |
| BR-FG-003 | Mỗi FamilyMember chỉ thuộc một nhánh | TC-FG-002P, TC-FG-002V | 2 | ✅ |
| BR-FG-004 | Quan hệ cha mẹ - con phải hợp lệ về thế hệ | TC-FG-004P, TC-FG-004N, TC-FG-004N2, TC-FG-004V | 4 | ✅ |
| BR-FG-005 | Mỗi người chỉ có tối đa một cặp hôn nhân đồng thời | TC-FG-005P, TC-FG-005N | 2 | ✅ |
| BR-FG-006 | Dữ liệu phả hệ không thể xóa vĩnh viễn | TC-FG-001N4 | 1 | ✅ |
| BR-FG-007 | Thông tin cây gia phả phải chính xác | TC-FG-006P, TC-FG-007P, TC-FG-008P | 3 | ✅ |
| BR-COM-001 | Chỉ thành viên đã xác thực mới được đăng nội dung | TC-COM-001P, TC-COM-001A, TC-COM-001A2, TC-COM-002P, TC-COM-002A, TC-COM-003P, TC-COM-004P | 7 | ✅ |
| BR-COM-002 | Người tạo bài viết được xóa bài viết của mình | TC-COM-001N2 | 1 | ✅ |
| BR-COM-003 | Thông báo chỉ được tạo bởi Family Owner | TC-COM-005P, TC-COM-005A, TC-COM-005A2 | 3 | ✅ |
| BR-COM-004 | Nội dung vi phạm bị kiểm duyệt | TC-ADM-002P | 1 | ✅ |
| BR-EVT-001 | Chỉ Family Member mới được tạo sự kiện | TC-EVT-001P, TC-EVT-001A | 2 | ✅ |
| BR-EVT-002 | Mỗi thành viên chỉ xác nhận RSVP một lần | TC-EVT-002P, TC-EVT-002N, TC-EVT-002V | 3 | ✅ |
| BR-EVT-003 | Chỉ Event Owner hoặc Family Owner được hủy sự kiện | TC-EVT-003P, TC-EVT-003A | 2 | ✅ |
| BR-EVT-004 | Thời điểm bắt đầu phải trước thời điểm kết thúc | TC-EVT-001N | 1 | ✅ |
| BR-EVT-005 | Hình ảnh sự kiện chỉ được thêm bởi người tham gia | TC-EVT-004P, TC-EVT-004A | 2 | ✅ |
| BR-DIR-001 | Chỉ Family Member được xem danh bạ | TC-DIR-001P, TC-DIR-001A, TC-DIR-004P | 3 | ✅ |
| BR-HER-001 | Chỉ Family Member mới được đóng góp tư liệu di sản | TC-HER-001P, TC-HER-001A, TC-HER-002P | 3 | ✅ |
| BR-HER-002 | Tư liệu di sản phải được duyệt trước khi công khai | TC-HER-005P, TC-HER-005A | 2 | ✅ |
| BR-HER-003 | Tư liệu được phân loại và gắn thẻ ngữ cảnh | TC-HER-001P | 1 | ✅ |
| BR-AI-001 | AI chỉ truy cập dữ liệu trong phạm vi quyền của người dùng | TC-AI-001P, TC-AI-001A, TC-AI-002P, TC-AI-005P | 4 | ✅ |
| BR-AI-002 | Kết quả AI phải được gán nhãn và không thay thế quyết định con người | TC-AI-002P, TC-AI-002V, TC-AI-004P | 3 | ✅ |
| BR-AI-003 | AI Service phải có cơ chế fallback khi không khả dụng | TC-AI-001N2 | 1 | ✅ |
| BR-DASH-001 | Dữ liệu báo cáo phải từ dữ liệu đã xác thực | TC-DASH-001P, TC-DASH-002P, TC-DASH-003P, TC-DASH-004P, TC-DASH-005P | 5 | ✅ |
| BR-ADM-001 | Chỉ Administrator mới được quản lý tài khoản người dùng | TC-ADM-001P, TC-ADM-001P2, TC-ADM-001A | 3 | ✅ |
| BR-ADM-002 | Mọi thao tác nhạy cảm phải được ghi vào Audit Log | TC-ADM-001P2, TC-ADM-003P, TC-ADM-003V | 3 | ✅ |
| BR-ADM-003 | Chỉ Administrator mới được cấu hình hệ thống | TC-ADM-005P, TC-ADM-005A | 2 | ✅ |
| BR-ADM-004 | Sao lưu và phục hồi chỉ được thực hiện bởi Administrator | TC-ADM-004P, TC-ADM-004P2 | 2 | ✅ |

---

## 3. NFR ↔ Test Case

| NFR ID | NFR Name | Test Case IDs | Số TC | Mức bao phủ | Ghi chú |
|--------|----------|:------------:|:-----:|:-----------:|---------|
| NFR-01 | Responsive Web Application | TC-NFR-001P, TC-NFR-001P2, TC-NFR-001P3, TC-NFR-001N | 4 | ✅ | `infrastructure/Infrastructure-Tests.md` |
| NFR-02 | Cross-platform Mobile Application | — | 0 | ⚠️ | Ngoài phạm vi MVP, cần test riêng khi có mobile app |
| NFR-03 | Secure Authentication (JWT) | TC-US-002P, TC-US-002V, TC-US-002A | 3 | ✅ | |
| NFR-04 | RESTful API Architecture | TC-NFR-004P, TC-NFR-004P2, TC-NFR-004N | 3 | ✅ | `infrastructure/Infrastructure-Tests.md` + Postman collection |
| NFR-05 | Modular Software Architecture | — | 0 | ✅ | Đã phân tích cấu trúc module (`app/domain`, `app/services`, `app/infrastructure`) bằng dependency analysis; không phát hiện circular import. Chi tiết xem `Module-Architecture.md` |
| NFR-06 | Interactive Graph Visualization | TC-FG-006P, TC-FG-006V | 2 | ✅ | |
| NFR-07 | PostgreSQL Database | TC-NFR-007P, TC-NFR-007P2, TC-NFR-007N | 3 | ✅ | `infrastructure/Infrastructure-Tests.md` + SQL script |
| NFR-08 | AI Service Integration | TC-AI-001P, TC-AI-001N2 | 2 | ✅ | |
| NFR-09 | Docker Deployment | TC-NFR-009P, TC-NFR-009P2, TC-NFR-009N, TC-NFR-009V | 4 | ✅ | `infrastructure/Infrastructure-Tests.md` |
| NFR-10 | High Availability | TC-NFR-010P, TC-NFR-010P2, TC-NFR-010N, TC-NFR-010V | 4 | ✅ | `infrastructure/Infrastructure-Tests.md` + k6 load test |
| NFR-11 | Audit Logging | TC-ADM-003P, TC-ADM-003V, TC-ADM-003P2 | 3 | ✅ | |
| NFR-12 | API Latency (P95 < 2s) | TC-FG-008V, TC-US-002B, TC-FG-006V, TC-NFR-010V | 4 | ✅ | Load test (k6) trong infrastructure tests |
| NFR-13 | Test Coverage (≥ 70%) | — | 0 | ⚠️ | Đã chạy `pytest --cov` trên `backend/app`: **160 test case, 160/160 PASS (~62% line coverage)** trên toàn `app/`; riêng `app/services` đạt **~86%**. Chi tiết xem `reports/coverage/` |

---

## 4. UC ↔ Test Case

| UC ID | UC Name | Test Case IDs | Số TC | Mức bao phủ |
|-------|---------|:------------:|:-----:|:-----------:|
| UC-01 | Đăng nhập & Xác thực | TC-US-002P → TC-US-002B, TC-US-003P → TC-US-003A, TC-US-004P → TC-US-004V, TC-US-005P → TC-US-005E | ~22 | ✅ |
| UC-02 | Đăng ký & Xác minh Thành viên | TC-US-001P → TC-US-001E, TC-US-007P → TC-US-007V | ~15 | ✅ |
| UC-03 | Quản lý Gia đình & Chi nhánh | TC-FG-001P → TC-FG-001B, TC-FG-002P → TC-FG-002V, TC-FG-003P → TC-FG-003V | ~21 | ✅ |
| UC-04 | Quản lý Quan hệ Cây gia phả | TC-FG-004P → TC-FG-004P2, TC-FG-005P → TC-FG-005A | ~9 | ✅ |
| UC-05 | Truy vấn & Trực quan hóa Cây gia phả | TC-FG-006P → TC-FG-006V, TC-FG-007P → TC-FG-007E, TC-FG-008P → TC-FG-008A | ~13 | ✅ |
| UC-06 | Quản lý Bài viết & Tương tác | TC-COM-001P → TC-COM-001B2, TC-COM-002P → TC-COM-002V2, TC-COM-003P → TC-COM-003P2, TC-COM-004P → TC-COM-004V, TC-COM-005P → TC-COM-005A2 | ~27 | ✅ |
| UC-07 | Quản lý Sự kiện & RSVP | TC-EVT-001P → TC-EVT-001N2, TC-EVT-002P → TC-EVT-002P2, TC-EVT-003P → TC-EVT-003A, TC-EVT-004P → TC-EVT-004A, TC-EVT-005P → TC-EVT-005V | ~20 | ✅ |
| UC-08 | Tra cứu Danh bạ & Hồ sơ | TC-DIR-001P → TC-DIR-001V, TC-DIR-002P, TC-DIR-003P → TC-DIR-003V, TC-DIR-004P → TC-DIR-004V, TC-US-006P → TC-US-006V | ~14 | ✅ |
| UC-09 | Quản lý Lưu trữ & Di sản | TC-HER-001P → TC-HER-001A, TC-HER-002P → TC-HER-002P2, TC-HER-003P → TC-HER-003A, TC-HER-004P → TC-HER-004V, TC-HER-005P → TC-HER-005A | ~15 | ✅ |
| UC-10 | Trợ lý AI & Truy vấn Tri thức | TC-AI-001P → TC-AI-001A, TC-AI-002P → TC-AI-002V, TC-AI-003P → TC-AI-003N, TC-AI-004P → TC-AI-004N, TC-AI-005P → TC-AI-005V | ~15 | ✅ |
| UC-11 | Xem Báo cáo & Thống kê | TC-DASH-001P → TC-DASH-001E, TC-DASH-002P → TC-DASH-002E, TC-DASH-003P, TC-DASH-004P, TC-DASH-005P → TC-DASH-005A | ~11 | ✅ |
| UC-12 | Quản trị Hệ thống & Kiểm duyệt | TC-ADM-001P → TC-ADM-001A, TC-ADM-002P → TC-ADM-002P3, TC-ADM-003P → TC-ADM-003A, TC-ADM-004P → TC-ADM-004N, TC-ADM-005P → TC-ADM-005P3, TC-US-005P, TC-US-005A | ~21 | ✅ |

---

## 5. Loại Test Case thống kê

| Loại test | Số lượng | Tỷ lệ |
|:---------:|:--------:|:-----:|
| Positive (P) | ~75 | ~38% |
| Negative (N) | ~50 | ~25% |
| Authorization (A) | ~30 | ~15% |
| Validation (V) | ~20 | ~10% |
| Boundary (B) | ~10 | ~5% |
| Edge Case (E) | ~10 | ~5% |
| **Tổng** | **~195** | **100%** |

---

## 6. Thống kê bao phủ tổng thể

| Hạng mục | Số lượng | Đã bao phủ | Tỷ lệ |
|----------|:--------:|:----------:|:-----:|
| FR | 49 | 49 | **100%** |
| BR | 34 | 34 | **100%** |
| NFR | 13 | 9 | **69%** ⚠️ |
| UC | 12 | 12 | **100%** |
| Test Case | ~206 | 206 | **100%** |

> **Cập nhật v1.1 (2026-08-20):**
> - ✅ Đã chạy `pytest --cov` trên code backend thật<br>
> - ✅ 160 test case unit test, **160/160 PASS** (0 failed)<br>
> - ✅ **62% line coverage** trên toàn bộ `app/` package<br>
> - ✅ **~86% line coverage** trên `app/services` (business logic chính)<br>
> - ✅ NFR-05 (Modular Architecture): không phát hiện circular import, phân tách rõ Domain ↔ Service ↔ Infrastructure<br>
> - ❌ NFR-13 (≥70% overall line coverage): đạt **62%** do chưa cover hết repositories, models, và mappers code.<br>
> - ❌ NFR-02 (Mobile): ngoài phạm vi<br>
> - ⚠️ Các NFR chưa cover (NFR-02) cần triển khai riêng trong roadmap sau.<br>
> - Báo cáo coverage HTML: `docs/testing/reports/coverage/index.html`<br>
> - **Bug đã sửa trong quá trình test**:
>   - `genealogy.py`: AmbiguousForeignKeysError (ADDED `foreign_keys`)
>   - `rsvp_repository.py`: column sai (`user_id`→`member_id`, `status`→`response`)
>   - `admin_repository.py`: moderate_post/get_user dùng `db.get()` thay vì `db.execute()`
>   - `event_service.py`: dùng `member_id`/`response` thay `user_id`/`status`