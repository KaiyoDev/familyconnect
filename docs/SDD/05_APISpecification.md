# 05. API SPECIFICATION (SDD)

**Dự án:** FamilyConnect  
**Mã Task:** FT8-35 | **Sprint:** Sprint 3 - Thiết kế hệ thống  
**Trạng thái:** Final v1.0  
**Tệp đính kèm:** docs/SDD/openapi.yaml  

---

## 1. Overview
Tài liệu API Specification đặc tả toàn bộ các giao diện lập trình ứng dụng RESTful API dành cho hệ thống backend FamilyConnect (triển khai trên khung làm việc FastAPI). Các API này phục vụ cho cả nền tảng Web và Mobile App.

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

### 5.2 User Profile (FR-US-05, FR-US-06)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /users/me | Bearer | Lấy thông tin hồ sơ tài khoản hiện tại |
| **PUT** | /users/me | Bearer | Cập nhật thông tin cá nhân |
| **POST** | /users/me/avatar | Bearer | Tải lên/thay đổi ảnh đại diện |
| **PUT** | /users/me/password | Bearer | Đổi mật khẩu tài khoản |

### 5.3 Family & Genealogy Management (FR-FG-01 đến FR-FG-08)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **POST** | /families | Bearer | Tạo gia đình / dòng họ mới |
| **GET** | /families | Bearer | Lấy danh sách các gia đình người dùng tham gia |
| **GET** | /families/{id} | Bearer | Xem thông tin chi tiết một gia đình |
| **PUT** | /families/{id} | Bearer (Owner) | Cập nhật thông tin gia đình |
| **DELETE** | /families/{id} | Bearer (Owner) | Giải thể / xóa gia đình |
| **POST** | /families/{id}/transfer-ownership | Bearer (Owner) | Chuyển quyền quản trị dòng họ |
| **GET** | /families/{id}/branches | Bearer | Lấy danh sách chi phái / nhánh gia đình |
| **POST** | /families/{id}/branches | Bearer (Owner) | Tạo mới nhánh gia đình |
| **PUT** | /families/{id}/branches/{bid} | Bearer (Owner) | Cập nhật thông tin chi phái |
| **DELETE**| /families/{id}/branches/{bid} | Bearer (Owner) | Xóa chi phái gia đình |
| **GET** | /families/{id}/members | Bearer | Danh sách thành viên trong gia phả |
| **POST** | /families/{id}/members | Bearer (Owner) | Thêm mới thành viên vào gia phả |
| **PUT** | /families/{id}/members/{mid} | Bearer (Owner) | Cập nhật thông tin thành viên gia phả |
| **DELETE**| /families/{id}/members/{mid} | Bearer (Owner) | Xóa thành viên khỏi gia phả |
| **POST** | /families/{id}/join | Bearer | Gửi yêu cầu gia nhập gia đình bằng Mã Gia Tộc |
| **GET** | /families/{id}/join-requests | Bearer (Owner) | Lấy danh sách các yêu cầu gia nhập chờ duyệt |
| **POST** | /families/{id}/join-requests/{rid}/approve | Bearer (Owner) | Phê duyệt yêu cầu gia nhập |
| **POST** | /families/{id}/join-requests/{rid}/reject | Bearer (Owner) | Từ chối yêu cầu gia nhập |
| **GET** | /families/{id}/tree | Bearer | Lấy dữ liệu đồ thị cây gia phả tương tác |
| **POST** | /families/{id}/relationships | Bearer (Owner) | Thiết lập mối quan hệ (Cha mẹ - Con, Vợ chồng) |
| **PUT** | /families/{id}/relationships/{rel_id} | Bearer (Owner) | Thay đổi mối quan hệ gia phả |
| **DELETE**| /families/{id}/relationships/{rel_id} | Bearer (Owner) | Xóa mối quan hệ gia phả |
| **POST** | /families/{id}/relationships/lookup | Bearer | Tra cứu mối quan hệ xưng hơ giữa 2 người |
| **POST** | /families/{id}/relationships/explain | Bearer | AI phân tích và giải thích mối quan hệ gia phả |

### 5.4 Community (FR-COM-01 đến FR-COM-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{id}/posts | Bearer | Bảng tin cộng đồng của gia đình |
| **POST** | /families/{id}/posts | Bearer | Đăng bài viết mới lên dòng thời gian |
| **GET** | /posts/{id} | Bearer | Xem chi tiết bài viết |
| **PUT** | /posts/{id} | Bearer (Author) | Chỉnh sửa bài viết |
| **DELETE**| /posts/{id} | Bearer (Author/Owner) | Xóa bài viết |
| **GET** | /posts/{id}/comments | Bearer | Danh sách bình luận bài viết |
| **POST** | /posts/{id}/comments | Bearer | Thêm bình luận |
| **PUT** | /comments/{cid} | Bearer (Author) | Sửa bình luận |
| **DELETE**| /comments/{cid} | Bearer (Author/Owner) | Xóa bình luận |
| **POST** | /posts/{id}/reactions | Bearer | Thả cảm xúc (Like, Heart,...) |
| **DELETE**| /posts/{id}/reactions | Bearer | Bỏ cảm xúc |
| **POST** | /families/{id}/news | Bearer | Đăng tin tức gia đình |
| **POST** | /families/{id}/announcements | Bearer (Owner) | Tạo thông báo chính thức từ Trưởng họ |

### 5.5 Events (FR-EVT-01 đến FR-EVT-04)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{id}/events | Bearer | Lịch sự kiện/giỗ chạp gia đình |
| **POST** | /families/{id}/events | Bearer | Tạo sự kiện mới |
| **GET** | /events/{id} | Bearer | Xem chi tiết sự kiện |
| **PUT** | /events/{id} | Bearer (Owner/Creator) | Cập nhật thông tin sự kiện |
| **DELETE**| /events/{id} | Bearer (Owner/Creator) | Hủy bỏ sự kiện |
| **POST** | /events/{id}/rsvp | Bearer | Gửi phản hồi xác nhận tham dự (RSVP) |
| **GET** | /events/{id}/participants | Bearer (Owner) | Danh sách người tham gia sự kiện |
| **POST** | /events/{id}/remind | Bearer (Owner) | Gửi thông báo nhắc nhở sự kiện |
| **POST** | /events/{id}/gallery | Bearer | Tải hình ảnh vào album sự kiện |
| **GET** | /events/{id}/gallery | Bearer | Tải danh sách ảnh kỷ niệm của sự kiện |
| **GET** | /events/{id}/export | Bearer (Owner) | Xuất danh sách tham dự ra file Excel/PDF |

### 5.6 Family Directory (FR-DIR-01 đến FR-DIR-04)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{id}/directory | Bearer | Tra cứu danh bạ gia đình |
| **GET** | /members/{id}/profile | Bearer | Xem hồ sơ liên hệ chi tiết của thành viên |
| **PUT** | /users/me/profession | Bearer | Cập nhật thông tin nghề nghiệp cá nhân |
| **GET** | /users/me/education | Bearer | Lấy thông tin học vấn cá nhân |
| **POST** | /users/me/education | Bearer | Thêm quá trình học vấn |
| **PUT** | /users/me/education/{eid}| Bearer | Cập nhật thông tin học vấn |

### 5.7 Family Heritage (FR-HER-01 đến FR-HER-05)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /families/{id}/heritage | Bearer | Tổng quan kho lưu trữ tư liệu gia tộc |
| **GET** | /heritage/documents | Bearer | Danh sách tài liệu/sắc phong/văn bản |
| **POST** | /heritage/documents | Bearer (Owner) | Tải lên tư liệu lịch sử mới |
| **PUT** | /heritage/documents/{doc_id} | Bearer (Owner) | Cập nhật thông tin tư liệu |
| **DELETE**| /heritage/documents/{doc_id} | Bearer (Owner) | Xóa tư liệu lịch sử |
| **GET** | /heritage/stories | Bearer | Danh sách các câu chuyện/giai thoại gia tộc |
| **POST** | /heritage/stories | Bearer | Đăng câu chuyện gia đình |
| **PUT** | /heritage/stories/{sid} | Bearer (Author) | Sửa câu chuyện gia đình |
| **DELETE**| /heritage/stories/{sid} | Bearer (Author/Owner) | Xóa câu chuyện |
| **POST** | /families/{id}/heritage/outstanding | Bearer (Owner) | Bổ sung danh hiệu tôn vinh thành viên |
| **GET** | /families/{id}/heritage/outstanding | Bearer | Danh sách các thành viên tiêu biểu |
| **GET** | /families/{id}/photos | Bearer | Thư viện ảnh/kho phương tiện gia tộc |

### 5.8 AI Service Services (FR-AI-01 đến FR-AI-03)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **POST** | /ai/search | Bearer | Tìm kiếm ngữ nghĩa (Semantic Vector Search) |
| **POST** | /ai/chat | Bearer | Trò chuyện với Trợ lý AI Gia tộc |
| **GET** | /ai/chat/{id}/history | Bearer | Lấy lịch sử đoạn hội thoại với AI |
| **POST** | /ai/summarize | Bearer | Tóm tắt nội dung tài liệu gia tộc dài |
| **POST** | /ai/suggest | Bearer | Gợi ý mối quan hệ hoặc sự kiện kết nối |

### 5.9 System Administration (FR-ADM-*)
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /admin/users | Bearer (Admin) | Quản lý danh sách toàn bộ người dùng hệ thống |
| **GET** | /admin/users/{id} | Bearer (Admin) | Chi tiết thông tin người dùng |
| **PUT** | /admin/users/{id} | Bearer (Admin) | Cập nhật trạng thái/quyền hạn người dùng |
| **POST** | /admin/users/{id}/suspend | Bearer (Admin) | Tạm khóa tài khoản người dùng |
| **POST** | /admin/users/{id}/activate | Bearer (Admin) | Mở khóa tài khoản |
| **GET** | /admin/moderation | Bearer (Admin) | Danh sách nội dung bị báo cáo vi phạm |
| **POST** | /admin/moderation/{id}/approve | Bearer (Admin) | Phê duyệt nội dung (Giữ lại) |
| **POST** | /admin/moderation/{id}/remove | Bearer (Admin) | Gỡ bỏ nội dung vi phạm |
| **GET** | /admin/audit-log | Bearer (Admin) | Truy vấn nhật ký hệ thống (Audit Logs) |
| **POST** | /admin/backup | Bearer (Admin) | Khởi chạy sao lưu CSDL hệ thống |
| **POST** | /admin/restore | Bearer (Admin) | Khôi phục CSDL từ bản sao lưu |
| **GET** | /admin/backups | Bearer (Admin) | Danh sách các bản sao lưu |
| **GET** | /admin/config | Bearer (Admin) | Lấy thông số cấu hình hệ thống |
| **PUT** | /admin/config | Bearer (Admin) | Thay đổi tham số cấu hình hệ thống |

### 5.10 Notifications
| Verb | Endpoint | Auth | Description |
| :--- | :--- | :--- | :--- |
| **GET** | /notifications | Bearer | Danh sách thông báo cá nhân |
| **PUT** | /notifications/{id}/read | Bearer | Đánh dấu đã đọc 1 thông báo |
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
Toàn bộ định dạng chuẩn OpenAPI 3.0.3 chi tiết của các API trên đã được đóng gói và kiểm tra tính hợp lệ (validated) tại đường dẫn: docs/SDD/openapi.yaml.

---

## 9. Traceability Matrix

### Mapping: Functional Requirements (SRS) -> Screen Code -> API Endpoint

| SRS Requirement ID | Screen Code (UI/UX) | API Endpoint Path | Verb |
| :--- | :--- | :--- | :--- |
| **FR-US-01** (Đăng ký) | S-PUB-02 | /auth/register | POST |
| **FR-US-02** (Đăng nhập) | S-PUB-01 | /auth/login | POST |
| **FR-US-06** (Hồ sơ cá nhân) | S-USR-01 | /users/me | GET, PUT |
| **FR-FG-01** (Tạo gia đình) | S-FAM-01 | /families | POST |
| **FR-FG-03** (Thêm thành viên) | S-GEN-02 | /families/{id}/members | POST |
| **FR-FG-06** (Xem cây gia phả) | S-GEN-01 | /families/{id}/tree | GET |
| **FR-FG-08** (Tra cứu quan hệ) | S-GEN-03 | /families/{id}/relationships/lookup | POST |
| **FR-COM-01** (Bảng tin gia đình) | S-COM-01 | /families/{id}/posts | GET, POST |
| **FR-EVT-01** (Sự kiện/Giỗ chạp) | S-EVT-01 | /families/{id}/events | GET, POST |
| **FR-DIR-01** (Danh bạ gia đình) | S-DIR-01 | /families/{id}/directory | GET |
| **FR-HER-01** (Lưu trữ tư liệu) | S-HER-01 | /heritage/documents | GET, POST |
| **FR-AI-01** (Tìm kiếm ngữ nghĩa) | S-AI-01 | /ai/search | POST |
| **FR-AI-02** (Trợ lý AI Chat) | S-AI-02 | /ai/chat | POST |

---

## 10. Appendix
- File đính kèm mẫu Request/Response JSON: docs/SDD/api-examples/
- Swagger UI khả dụng tại: [https://api.familyconnect.vn/docs](https://api.familyconnect.vn/docs)
<!-- updated for PR review -->