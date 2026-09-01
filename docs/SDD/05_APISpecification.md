# 05. API SPECIFICATION (SDD)

**Dự án:** FamilyConnect  
**Mã Task:** FT8-35 | **Sprint:** Sprint 3 - Thiết kế hệ thống  
**Trạng thái:** Final v1.0  
**Tệp đính kèm:** docs/SDD/openapi.yaml  

---

## 1. Overview
Tài liệu API Specification đặc tả toàn bộ các giao diện lập trình ứng dụng RESTful API dành cho hệ thống backend FamilyConnect (triển khai trên khung làm việc FastAPI). Các API này phục vụ **Web Portal** (phạm vi hiện tại). Mobile App (React Native) là hướng phát triển tương lai (future/optional) và sẽ tái sử dụng cùng tập API này.

* **Base URLs:**
  * **Development:** http://localhost:8000/api/v1
  * **Production:** [https://api.familyconnect.vn/api/v1](https://api.familyconnect.vn/api/v1)
* **Protocol:** HTTPS
* **Format:** JSON (application/json)
* **Versioning:** URL Path /api/v1/

---

## 2. Authentication & Authorization

### 2.1 JSON Web Token (JWT) Strategy
Hệ thống sử dụng cơ chế xác thực vô trạng thái (Stateless) dựa trên chuẩn JWT:
* **Header:** Authorization: Bearer <access_token>
* **Access Token Life:** 30 phút (chứa user_id, email, system_role).
* **Refresh Token Life:** 14 ngày (được lưu vết trong CSDL để xử lý thu hồi/logout).

### 2.2 Role-Based Access Control (RBAC) & Contextual Authorization
* **System Roles:** ADMIN, USER, GUEST
* **Family Context Roles:** FAMILY_OWNER, BRANCH_ADMIN, FAMILY_MEMBER
* **Quyền truy cập:** Kiểm tra đồng thời System Role và vai trò của người dùng trong gia đình (family_id).

---

## 3. Request/Response Format

### 3.1 Standard Response Format
{
  "success": true,
  "data": { ... },
  "message": "Operation successful",
  "timestamp": "2026-08-13T08:45:00Z"
}

### 3.2 Standard Paginated Response Format
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 100,
    "total_pages": 5
  },
  "message": "Operation successful",
  "timestamp": "2026-08-13T08:45:00Z"
}

### 3.3 Standard Error Response Format
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input validation failed",
    "details": [
      {
        "field": "email",
        "message": "Email cannot be empty"
      }
    ]
  },
  "timestamp": "2026-08-13T08:45:00Z"
}

---

## 4. Error Handling & Error Codes Reference

### 4.1 HTTP Status Codes Map
* **200 OK:** Truy vấn hoặc cập nhật thành công.
* **201 Created:** Tạo mới tài nguyên thành công.
* **204 No Content:** Xóa/thực thi thành công, không trả về body.
* **400 Bad Request:** Lỗi cú pháp hoặc validation.
* **401 Unauthorized:** Chưa xác thực hoặc Token hết hạn/không hợp lệ.
* **403 Forbidden:** Không đủ quyền truy cập (RBAC).
* **404 Not Found:** Không tìm thấy tài nguyên.
* **409 Conflict:** Trùng lặp dữ liệu độc bản.
* **422 Unprocessable Entity:** Vi phạm quy tắc nghiệp vụ (Business Rules).
* **429 Too Many Requests:** Vượt quá hạn mức truy cập (Rate Limit).
* **500 Internal Server Error:** Lỗi hệ thống.
* **503 Service Unavailable:** Dịch vụ tạm thời gián đoạn.

### 4.2 System Error Codes Table

| Code | Description | HTTP Status |
| :--- | :--- | :--- |
| **VALIDATION_ERROR** | Dữ liệu đầu vào không đúng định dạng/thiếu trường bắt buộc | 400 |
| **AUTHENTICATION_FAILED** | Thông tin đăng nhập không chính xác | 401 |
| **TOKEN_EXPIRED** | JWT Access Token đã hết hạn | 401 |
| **TOKEN_INVALID** | JWT Token không đúng cấu trúc hoặc sai chữ ký | 401 |
| **PERMISSION_DENIED** | Không đủ quyền thực thi hành động này | 403 |
| **RESOURCE_NOT_FOUND** | Tài nguyên yêu cầu không tồn tại | 404 |
| **DUPLICATE_RESOURCE** | Email hoặc dữ liệu đã tồn tại trên hệ thống | 409 |
| **BUSINESS_RULE_VIOLATION** | Vi phạm quy tắc nghiệp vụ hệ thống | 422 |
| **CYCLE_DETECTED** | Phát hiện vòng lặp quan hệ trong cây gia phả | 422 |
| **MAX_PARENTS_EXCEEDED** | Một thành viên không thể có quá 2 cha/mẹ ruột | 422 |
| **RATE_LIMIT_EXCEEDED** | Tần suất gửi request vượt quá giới hạn cho phép | 429 |
| **INTERNAL_ERROR** | Lỗi máy chủ nội bộ | 500 |
| **SERVICE_UNAVAILABLE** | Dịch vụ AI hoặc Storage tạm thời ngừng hoạt động | 503 |

---

## 5. API Endpoints Catalog

### 5.1 Authentication & Security (FR-US-01 đến FR-US-04)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **POST** | /auth/register | Public | Đăng ký tài khoản người dùng mới |
| **POST** | /auth/login | Public | Đăng nhập bằng Email & Mật khẩu |
| **POST** | /auth/logout | Bearer | Đăng xuất và vô hiệu hóa Refresh Token |
| **POST** | /auth/refresh | Bearer | Cấp mới Access Token từ Refresh Token |
| **POST** | /auth/verify-email | Public | Xác thực email đăng ký qua mã OTP/Token |
| **POST** | /auth/forgot-password | Public | Yêu cầu gửi email khôi phục mật khẩu |
| **POST** | /auth/reset-password | Public | Đặt lại mật khẩu mới với reset token |
| **POST** | /auth/oauth/google | Public | Đăng nhập/Đăng ký qua Google OAuth2 |
| **POST** | /auth/oauth/apple | Public | Đăng nhập/Đăng ký qua Apple ID |

> **Ghi chú phạm vi (OPTIONAL):** Đăng nhập qua Google/Apple (OAuth2) **không nằm trong FR/BR hiện tại**. Tính năng này được đánh dấu **OPTIONAL / OUT OF SCOPE**, chỉ triển khai khi requirement được bổ sung. Các endpoint OAuth giữ ở đây làm định hướng tích hợp tương lai, không được tính vào mức độ phủ của thiết kế hiện tại.

### 5.2 User Profile (FR-US-05, FR-US-06)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /users/me | Bearer | Lấy thông tin hồ sơ tài khoản hiện tại |
| **PUT** | /users/me | Bearer | Cập nhật thông tin cá nhân |
| **POST** | /users/me/avatar | Bearer | Tải lên/thay đổi ảnh đại diện |
| **PUT** | /users/me/password | Bearer | Đổi mật khẩu tài khoản |

### 5.3 Family & Genealogy Management (FR-FG-01 đến FR-FG-08)

> **Quy ước đường dẫn:** Tài nguyên thuộc phạm vi gia đình dùng `/families/{family_id}/...`. Tham số định danh dùng tên mô tả đầy đủ (`{family_id}`, `{member_id}`, `{branch_id}`, `{request_id}`, `{relationship_id}`).

| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **POST** | /families | Bearer | Tạo gia đình / dòng họ mới |
| **GET** | /families | Bearer | Lấy danh sách các gia đình người dùng tham gia |
| **GET** | /families/{family_id} | Bearer | Xem thông tin chi tiết một gia đình |
| **PUT** | /families/{family_id} | Bearer (Owner) | Cập nhật thông tin gia đình |
| **DELETE** | /families/{family_id} | Bearer (Owner) | Giải thể / xóa gia đình |
| **POST** | /families/{family_id}/transfer-ownership | Bearer (Owner) | Chuyển quyền quản trị dòng họ |
| **GET** | /families/{family_id}/branches | Bearer | Lấy danh sách chi phái / nhánh gia đình |
| **POST** | /families/{family_id}/branches | Bearer (Owner) | Tạo mới nhánh gia đình |
| **PUT** | /families/{family_id}/branches/{branch_id} | Bearer (Owner) | Cập nhật thông tin chi phái |
| **DELETE**| /families/{family_id}/branches/{branch_id} | Bearer (Owner) | Xóa chi phái gia đình |
| **GET** | /families/{family_id}/members | Bearer | Danh sách thành viên trong gia phả |
| **POST** | /families/{family_id}/members | Bearer (Owner) | Thêm mới thành viên vào gia phả |
| **PUT** | /families/{family_id}/members/{member_id} | Bearer (Owner) | Cập nhật thông tin thành viên gia phả |
| **DELETE**| /families/{family_id}/members/{member_id} | Bearer (Owner) | Xóa thành viên khỏi gia phả |
| **POST** | /families/{family_id}/join | Bearer | Gửi yêu cầu gia nhập gia đình bằng Mã Gia Tộc |
| **GET** | /families/{family_id}/join-requests | Bearer (Owner) | Lấy danh sách các yêu cầu gia nhập chờ duyệt |
| **POST** | /families/{family_id}/join-requests/{request_id}/approve | Bearer (Owner) | Phê duyệt yêu cầu gia nhập |
| **POST** | /families/{family_id}/join-requests/{request_id}/reject | Bearer (Owner) | Từ chối yêu cầu gia nhập |
| **GET** | /families/{family_id}/tree | Bearer | Lấy dữ liệu đồ thị cây gia phả tương tác |
| **POST** | /families/{family_id}/relationships | Bearer (Owner) | Thiết lập mối quan hệ (Parent-Child, Marriage) |
| **PUT** | /families/{family_id}/relationships/{relationship_id} | Bearer (Owner) | Thay đổi mối quan hệ gia phả |
| **DELETE**| /families/{family_id}/relationships/{relationship_id} | Bearer (Owner) | Xóa mối quan hệ gia phả |
| **POST** | /families/{family_id}/relationships/lookup | Bearer | Tra cứu mối quan hệ xưng hô giữa 2 người |
| **POST** | /families/{family_id}/relationships/explain | Bearer | AI phân tích và giải thích mối quan hệ gia phả |

### 5.4 Community (FR-COM-01 đến FR-COM-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{family_id}/posts | Bearer | Bảng tin cộng đồng của gia đình |
| **POST** | /families/{family_id}/posts | Bearer | Đăng bài viết mới lên dòng thời gian |
| **GET** | /posts/{post_id} | Bearer | Xem chi tiết bài viết |
| **PUT** | /posts/{post_id} | Bearer (Author) | Chỉnh sửa bài viết |
| **DELETE**| /posts/{post_id} | Bearer (Author/Owner) | Xóa bài viết |
| **GET** | /posts/{post_id}/comments | Bearer | Danh sách bình luận bài viết |
| **POST** | /posts/{post_id}/comments | Bearer | Thêm bình luận |
| **PUT** | /comments/{comment_id} | Bearer (Author) | Sửa bình luận |
| **DELETE**| /comments/{comment_id} | Bearer (Author/Owner) | Xóa bình luận |
| **POST** | /posts/{post_id}/reactions | Bearer | Thả cảm xúc (Like, Heart,...) |
| **DELETE**| /posts/{post_id}/reactions | Bearer | Bỏ cảm xúc |
| **POST** | /families/{family_id}/news | Bearer | Đăng tin tức gia đình |
| **POST** | /families/{family_id}/announcements | Bearer (Owner) | Tạo thông báo chính thức từ Trưởng họ |

### 5.5 Events (FR-EVT-01 đến FR-EVT-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{family_id}/events | Bearer | Lịch sự kiện/giỗ chạp gia đình |
| **POST** | /families/{family_id}/events | Bearer | Tạo sự kiện mới |
| **GET** | /events/{event_id} | Bearer | Xem chi tiết sự kiện |
| **PUT** | /events/{event_id} | Bearer (Owner/Creator) | Cập nhật thông tin sự kiện |
| **DELETE**| /events/{event_id} | Bearer (Owner/Creator) | Hủy bỏ sự kiện |
| **POST** | /events/{event_id}/rsvp | Bearer | Gửi phản hồi xác nhận tham dự (RSVP) |
| **GET** | /events/{event_id}/participants | Bearer (Owner) | Danh sách người tham gia sự kiện |
| **POST** | /events/{event_id}/remind | Bearer (Owner) | Gửi thông báo nhắc nhở sự kiện |
| **POST** | /events/{event_id}/gallery | Bearer (RSVP = Tham gia) | Tải hình ảnh vào album sự kiện (BR-EVT-005) |
| **GET** | /events/{event_id}/gallery | Bearer | Tải danh sách ảnh kỷ niệm của sự kiện |
| **GET** | /events/{event_id}/export | Bearer (Owner) | Xuất danh sách tham dự ra file Excel/PDF |

### 5.6 Family Directory (FR-DIR-01 đến FR-DIR-04)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{family_id}/directory | Bearer | Tra cứu danh bạ gia đình |
| **GET** | /families/{family_id}/directory/{member_id}/profile | Bearer | Xem hồ sơ liên hệ chi tiết của thành viên |
| **PUT** | /users/me/profession | Bearer | Cập nhật thông tin nghề nghiệp cá nhân |
| **GET** | /users/me/education | Bearer | Lấy thông tin học vấn cá nhân |
| **POST** | /users/me/education | Bearer | Thêm quá trình học vấn |
| **PUT** | /users/me/education/{education_id} | Bearer | Cập nhật thông tin học vấn |

### 5.7 Family Heritage (FR-HER-01 đến FR-HER-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{family_id}/heritage | Bearer | Tổng quan kho lưu trữ tư liệu gia tộc |
| **GET** | /families/{family_id}/heritage/documents | Bearer | Danh sách tài liệu/sắc phong/văn bản |
| **POST** | /families/{family_id}/heritage/documents | Bearer (Member) | Tải lên tư liệu lịch sử mới (trạng thái Pending Review, BR-HER-001) |
| **PUT** | /families/{family_id}/heritage/documents/{document_id} | Bearer (Author/Owner) | Cập nhật thông tin tư liệu |
| **DELETE**| /families/{family_id}/heritage/documents/{document_id} | Bearer (Author/Owner) | Xóa tư liệu lịch sử |
| **POST** | /families/{family_id}/heritage/documents/{document_id}/approve | Bearer (Owner/Admin) | Duyệt công khai tư liệu di sản (BR-HER-002) |
| **POST** | /families/{family_id}/heritage/documents/{document_id}/reject | Bearer (Owner/Admin) | Từ chối tư liệu di sản (BR-HER-002) |
| **GET** | /families/{family_id}/heritage/stories | Bearer | Danh sách các câu chuyện/giai thoại gia tộc |
| **POST** | /families/{family_id}/heritage/stories | Bearer (Member) | Đăng câu chuyện gia đình (Pending Review) |
| **PUT** | /families/{family_id}/heritage/stories/{story_id} | Bearer (Author) | Sửa câu chuyện gia đình |
| **DELETE**| /families/{family_id}/heritage/stories/{story_id} | Bearer (Author/Owner) | Xóa câu chuyện |
| **POST** | /families/{family_id}/heritage/outstanding | Bearer (Owner) | Bổ sung danh hiệu tôn vinh thành viên |
| **GET** | /families/{family_id}/heritage/outstanding | Bearer | Danh sách các thành viên tiêu biểu |
| **GET** | /families/{family_id}/photos | Bearer | Thư viện ảnh/kho phương tiện gia tộc |

### 5.8 AI Service Services (FR-AI-01 đến FR-AI-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **POST** | /ai/search | Bearer | Tìm kiếm ngữ nghĩa (Semantic Vector Search) |
| **POST** | /ai/chat | Bearer | Trò chuyện với Trợ lý AI Gia tộc; lưu hội thoại vào `AIConversation`/`AIMessage` |
| **GET** | /ai/conversations | Bearer | Danh sách các hội thoại AI của người dùng |
| **GET** | /ai/conversations/{conversation_id}/messages | Bearer | Lấy lịch sử đoạn hội thoại với AI (bản ghi `AIMessage`) |
| **DELETE**| /ai/conversations/{conversation_id} | Bearer | Xóa hội thoại AI |
| **POST** | /ai/summarize | Bearer | Tóm tắt nội dung tài liệu gia tộc dài |
| **POST** | /ai/suggest | Bearer | Gợi ý mối quan hệ hoặc sự kiện kết nối |

> **Ghi chú:** API lịch sử hội thoại khớp với thực thể `AIConversation`/`AIMessage` trong Domain Model và Database Design. Không dùng endpoint `/ai/chat/{id}/history` cũ.

### 5.9 System Administration (FR-ADM-01 đến FR-ADM-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /admin/users | Bearer (Admin) | Quản lý danh sách toàn bộ người dùng hệ thống |
| **GET** | /admin/users/{user_id} | Bearer (Admin) | Chi tiết thông tin người dùng |
| **PUT** | /admin/users/{user_id} | Bearer (Admin) | Cập nhật trạng thái/quyền hạn người dùng |
| **POST** | /admin/users/{user_id}/suspend | Bearer (Admin) | Tạm khóa tài khoản người dùng |
| **POST** | /admin/users/{user_id}/activate | Bearer (Admin) | Mở khóa tài khoản |
| **GET** | /admin/moderation | Bearer (Admin) | Danh sách nội dung bị báo cáo vi phạm |
| **POST** | /admin/moderation/{item_id}/approve | Bearer (Admin) | Phê duyệt nội dung (Giữ lại) |
| **POST** | /admin/moderation/{item_id}/remove | Bearer (Admin) | Gỡ bỏ nội dung vi phạm |
| **GET** | /admin/audit-log | Bearer (Admin) | Truy vấn nhật ký hệ thống (Audit Logs) |
| **POST** | /admin/backup | Bearer (Admin) | Khởi chạy sao lưu CSDL hệ thống |
| **POST** | /admin/restore | Bearer (Admin) | Khôi phục CSDL từ bản sao lưu |
| **GET** | /admin/backups | Bearer (Admin) | Danh sách các bản sao lưu |
| **GET** | /admin/config | Bearer (Admin) | Lấy thông số cấu hình hệ thống |
| **PUT** | /admin/config | Bearer (Admin) | Thay đổi tham số cấu hình hệ thống |

### 5.10 Dashboard & Reporting (FR-DASH-01 đến FR-DASH-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{family_id}/analytics | Bearer | Thống kê tổng hợp gia đình (FR-DASH-01, FR-DASH-02) |
| **GET** | /families/{family_id}/analytics/demographics | Bearer | Thống kê nhân khẩu (FR-DASH-04) |
| **GET** | /families/{family_id}/analytics/events | Bearer | Thống kê sự kiện (FR-DASH-03) |
| **POST** | /families/{family_id}/reports | Bearer (Owner) | Tạo báo cáo theo mẫu (FR-DASH-05) |
| **GET** | /families/{family_id}/reports/{report_id} | Bearer | Xem báo cáo đã tạo |
| **GET** | /families/{family_id}/reports/{report_id}/export | Bearer (Owner) | Xuất báo cáo PDF/Excel |

### 5.11 Notifications
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /notifications | Bearer | Danh sách thông báo cá nhân |
| **PUT** | /notifications/{notification_id}/read | Bearer | Đánh dấu đã đọc 1 thông báo |
| **PUT** | /notifications/read-all | Bearer | Đánh dấu đã đọc tất cả thông báo |
| **GET** | /notifications/settings | Bearer | Xem cấu hình nhận thông báo |
| **PUT** | /notifications/settings | Bearer | Thay đổi cấu hình cài đặt thông báo |

---

## 6. Rate Limiting Policy

| Endpoint Group | Limit | Window | Error Handling |
| :--- | :--- | :--- | :--- |
| **Authentication (/auth/*)** | 10 requests | 15 minutes | HTTP 429 (RATE_LIMIT_EXCEEDED) |
| **AI Services (/ai/*)** | 30 requests | 1 minute | HTTP 429 (RATE_LIMIT_EXCEEDED) |
| **General APIs (Các API khác)** | 100 requests | 1 minute | HTTP 429 (RATE_LIMIT_EXCEEDED) |

---

## 7. Versioning Strategy
- Tất cả API Endpoints bắt buộc đính kèm chuỗi định danh phiên bản trực tiếp trên đường dẫn URI /api/v1/.
- Khi nâng cấp có breaking changes: Tạo mới nhánh /api/v2/. Các client cũ vẫn được hỗ trợ song song trên /api/v1/ trong thời gian Deprecation Notice (tối thiểu 6 tháng).

---

## 8. OpenAPI Specification Overview
API catalog trong **Mục 5** là nguồn chính thức của thiết kế API. Bản mô tả chuẩn **OpenAPI 3.0.3** của toàn bộ catalog được lưu tại `docs/SDD/openapi.yaml` và được đồng bộ với Mục 5. `openapi.yaml` phải được chạy kiểm tra hợp lệ (validate) bằng tool OpenAPI (ví dụ `npx @redocly/cli lint`) trước mỗi lần triển khai.

---

## 9. Traceability Matrix

### Mapping: Functional Requirements (SRS) -> Screen Code -> API Endpoint

> Screen Code dùng ID màn hình thực tế trong 03_UIUXDesign.md (PUB-*, SHL-*, FAM-*, GEN-*, COM-*, EVT-*, DIR-*, HER-*, AI-*, DSH-*, ADM-*, PRF-*).

| SRS Requirement ID | Screen Code (UI/UX) | API Endpoint Path | Verb |
| :--- | :--- | :--- | :--- |
| **FR-US-01** (Đăng ký) | PUB-03, PUB-05 | /auth/register | POST |
| **FR-US-02** (Đăng nhập) | PUB-02 | /auth/login | POST |
| **FR-US-06** (Hồ sơ cá nhân) | PRF-01 | /users/me | GET, PUT |
| **FR-FG-01** (Tạo gia đình) | FAM-01 | /families | POST |
| **FR-FG-03** (Thêm thành viên) | GEN-05 | /families/{family_id}/members | POST |
| **FR-FG-06** (Xem cây gia phả) | GEN-01 | /families/{family_id}/tree | GET |
| **FR-FG-08** (Tra cứu quan hệ) | GEN-03 | /families/{family_id}/relationships/lookup | POST |
| **FR-COM-01** (Bảng tin gia đình) | COM-01, COM-03 | /families/{family_id}/posts | GET, POST |
| **FR-EVT-01** (Sự kiện/Giỗ chạp) | EVT-01, EVT-03 | /families/{family_id}/events | GET, POST |
| **FR-DIR-01** (Danh bạ gia đình) | DIR-01 | /families/{family_id}/directory | GET |
| **FR-HER-01** (Lưu trữ tư liệu) | HER-02 | /families/{family_id}/heritage/documents | GET, POST |
| **FR-AI-01** (Tìm kiếm ngữ nghĩa) | SHL-03, AI-02 | /ai/search | POST |
| **FR-AI-02** (Trợ lý AI Chat) | AI-01 | /ai/chat | POST |
| **FR-DASH-05** (Xuất báo cáo) | DSH-03 | /families/{family_id}/reports | POST |

---

## 10. Appendix
- File đính kèm mẫu Request/Response JSON: docs/SDD/api-examples/
- Swagger UI khả dụng tại: [https://api.familyconnect.vn/docs](https://api.familyconnect.vn/docs)
<!-- updated for PR review -->