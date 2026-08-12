# 05. RESTful API Specification - FamilyConnect Backend

## 1. Overview
Tài liệu này định nghĩa chi tiết toàn bộ hệ thống RESTful API cho Backend ứng dụng FamilyConnect. API được thiết kế tuân thủ mô hình kiến trúc, các quy tắc nghiệp vụ (Business Rules) và đáp ứng các Functional Requirements (FRs) cùng Use Cases (UCs).

* Base URL (Dev): http://localhost:8000/api/v1
* Base URL (Prod): https://api.familyconnect.vn/api/v1
* API Versioning Strategy: URI Versioning (/api/v1/).
* Format: JSON (UTF-8).

---

## 2. Authentication & Authorization
Hệ thống sử dụng cơ chế JWT (JSON Web Token) Bearer Token kết hợp với RBAC (Role-Based Access Control).

### Header Requirement:
Authorization: Bearer <access_token>

### Roles (RBAC Hierarchy):
* System Admin
* Family Owner / Admin
* Member
* Guest / Public

---

## 3. Standard Request/Response Format

### 3.1. Success Response Schema
{
  "success": true,
  "data": {},
  "message": "Operation completed successfully",
  "timestamp": "2026-08-12T16:30:00Z"
}

### 3.2. Paginated Response Schema
{
  "success": true,
  "data": [],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 100,
    "total_pages": 5
  },
  "timestamp": "2026-08-12T16:30:00Z"
}

### 3.3. Standard Error Response Schema
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email address format"
      }
    ]
  },
  "timestamp": "2026-08-12T16:30:00Z"
}

---

## 4. Error Handling & Standard Codes

| Status Code | Error Code | Description |
| :--- | :--- | :--- |
| 400 Bad Request | VALIDATION_ERROR | Dữ liệu đầu vào không đúng định dạng. |
| 401 Unauthorized | AUTHENTICATION_FAILED | Tên đăng nhập hoặc mật khẩu không chính xác. |
| 401 Unauthorized | TOKEN_EXPIRED | JWT Token đã hết hạn. |
| 401 Unauthorized | TOKEN_INVALID | JWT Token không hợp lệ. |
| 403 Forbidden | PERMISSION_DENIED | Người dùng không có quyền truy cập tài nguyên. |
| 404 Not Found | RESOURCE_NOT_FOUND | Không tìm thấy tài nguyên yêu cầu. |
| 409 Conflict | DUPLICATE_RESOURCE | Tài nguyên đã tồn tại. |
| 422 Unprocessable | BUSINESS_RULE_VIOLATION | Vi phạm quy tắc nghiệp vụ hệ thống. |
| 422 Unprocessable | CYCLE_DETECTED | Phát hiện vòng lặp vô lý trong cây gia phả. |
| 422 Unprocessable | MAX_PARENTS_EXCEEDED | Một người có nhiều hơn 2 cha/mẹ ruột. |
| 429 Too Many Req | RATE_LIMIT_EXCEEDED | Tần suất gửi yêu cầu vượt quá giới hạn. |
| 500 Internal Error | INTERNAL_ERROR | Lỗi nội bộ máy chủ. |
| 503 Unavailable | SERVICE_UNAVAILABLE | Dịch vụ đang tạm dừng. |

---

## 5. Rate Limiting Policy

| Endpoint Group | Rate Limit Window | Max Requests |
| :--- | :--- | :--- |
| /auth/* | 15 minutes | 10 requests |
| /ai/* | 1 minute | 30 requests |
| Tất cả Endpoints khác | 1 minute | 100 requests |

---

## 6. Endpoints Summary

### 6.1. Authentication Module
* POST /auth/register - Đăng ký tài khoản (Public)
* POST /auth/login - Đăng nhập nhận JWT (Public)
* POST /auth/logout - Đăng xuất / Revoke Token (Bearer)
* POST /auth/refresh - Cấp lại Token từ Refresh Token (Bearer)
* POST /auth/verify-email - Xác minh Email (Public)
* POST /auth/forgot-password - Yêu cầu khôi phục mật khẩu (Public)
* POST /auth/reset-password - Đặt lại mật khẩu mới (Public)
* POST /auth/oauth/google - Đăng nhập OAuth Google (Public)
* POST /auth/oauth/apple - Đăng nhập OAuth Apple (Public)

### 6.2. User Profile Module
* GET /users/me - Lấy thông tin tài khoản hiện tại (Bearer)
* PUT /users/me - Cập nhật thông tin cá nhân (Bearer)
* POST /users/me/avatar - Tải lên ảnh đại diện (Bearer)
* PUT /users/me/password - Đổi mật khẩu (Bearer)
* PUT /users/me/profession - Cập nhật nghề nghiệp (Bearer)
* GET/POST/PUT /users/me/education - Quản lý trình độ học vấn (Bearer)

### 6.3. Family Management Module
* POST /families - Tạo gia tộc mới (Bearer)
* GET /families - Danh sách các gia tộc người dùng tham gia (Bearer)
* GET /families/{id} - Chi tiết gia tộc (Bearer)
* PUT /families/{id} - Cập nhật thông tin gia tộc (Family Owner)
* DELETE /families/{id} - Giải thể gia tộc (Family Owner)
* POST /families/{id}/transfer-ownership - Chuyển quyền Trưởng họ (Family Owner)
* GET/POST/PUT/DELETE /families/{id}/branches - CRUD Chi/Nhánh gia đình (Family Owner)
* GET/POST/PUT/DELETE /families/{id}/members - CRUD Thành viên gia tộc (Family Owner)
* POST /families/{id}/join - Gửi yêu cầu gia nhập gia tộc (Bearer)
* GET /families/{id}/join-requests - Danh sách yêu cầu gia nhập (Family Owner)
* POST /families/{id}/join-requests/{rid}/approve - Duyệt yêu cầu gia nhập (Family Owner)
* POST /families/{id}/join-requests/{rid}/reject - Từ chối yêu cầu gia nhập (Family Owner)

### 6.4. Genealogy Module
* GET /families/{id}/tree - Truy vấn Đồ thị Cây gia phả (Bearer)
* POST/PUT/DELETE /families/{id}/relationships - CRUD Quan hệ gia phả (Family Owner)
* POST /families/{id}/relationships/lookup - Tra cứu quan hệ giữa 2 thành viên (Bearer)
* POST /families/{id}/relationships/explain - Gọi AI giải thích cách xưng hô (Bearer)

### 6.5. Community Module
* GET /families/{id}/posts - Lấy danh sách bài viết / Bảng tin (Bearer)
* POST /families/{id}/posts - Đăng bài viết mới (Bearer)
* GET /posts/{id} - Chi tiết bài viết (Bearer)
* PUT /posts/{id} - Chỉnh sửa bài viết (Author)
* DELETE /posts/{id} - Xóa bài viết (Author/Family Owner)
* POST/PUT/DELETE /posts/{id}/comments - CRUD Bình luận (Bearer)
* POST/DELETE /posts/{id}/reactions - Thả/Bỏ thả cảm xúc (Bearer)
* POST /families/{id}/news - Đăng tin tức gia đình (Bearer)
* POST /families/{id}/announcements - Tạo thông báo quan trọng (Family Owner)

### 6.6. Events Module
* GET /families/{id}/events - Danh sách sự kiện gia đình (Bearer)
* POST /families/{id}/events - Tạo sự kiện mới (Bearer)
* GET /events/{id} - Chi tiết sự kiện (Bearer)
* PUT /events/{id} - Cập nhật sự kiện (Event Owner/Family Owner)
* DELETE /events/{id} - Hủy sự kiện (Event Owner/Family Owner)
* POST /events/{id}/rsvp - Xác nhận tham gia RSVP (Bearer)
* GET /events/{id}/participants - Danh sách tham gia (Family Owner)
* POST /events/{id}/remind - Gửi nhắc nhở sự kiện (Family Owner)
* POST/GET /events/{id}/gallery - Quản lý thư viện ảnh sự kiện (Bearer)
* GET /events/{id}/export - Xuất danh sách điểm danh (Family Owner)

### 6.7. Directory & Heritage Module
* GET /families/{id}/directory - Tìm kiếm danh bạ thành viên (Bearer)
* GET /members/{id}/profile - Xem hồ sơ chi tiết thành viên (Bearer)
* GET /families/{id}/heritage - Tổng quan di sản gia tộc (Bearer)
* POST/GET/PUT/DELETE /heritage/documents - CRUD Tài liệu lịch sử (Family Owner)
* POST/GET/PUT/DELETE /heritage/stories - CRUD Câu chuyện gia đình (Bearer)
* POST/GET /families/{id}/heritage/outstanding - Vinh danh thành viên ưu tú (Bearer)
* GET /families/{id}/photos - Thư viện ảnh di sản gia tộc (Bearer)

### 6.8. AI Service Module
* POST /ai/search - Tìm kiếm ngữ nghĩa AI Semantic Search (Bearer)
* POST /ai/chat - Hỏi đáp tri thức gia đình với Chatbot RAG (Bearer)
* GET /ai/chat/{id}/history - Lịch sử hội thoại AI (Bearer)
* POST /ai/summarize - Tóm tắt văn bản di sản / gia sử (Bearer)
* POST /ai/suggest - AI gợi ý kết nối thành viên / sự kiện (Bearer)

### 6.9. Admin & System Module
* GET/PUT /admin/users - Quản lý danh sách người dùng (System Admin)
* POST /admin/users/{id}/suspend - Tạm khóa tài khoản (System Admin)
* POST /admin/users/{id}/activate - Kích hoạt tài khoản (System Admin)
* GET /admin/moderation - Danh sách nội dung bị báo cáo (System Admin)
* POST /admin/moderation/{id}/approve - Duyệt nội dung (System Admin)
* POST /admin/moderation/{id}/remove - Gỡ bỏ nội dung vi phạm (System Admin)
* GET /admin/audit-log - Truy vấn nhật ký hệ thống (System Admin)
* POST /admin/backup & POST /admin/restore - Sao lưu / Phục hồi dữ liệu (System Admin)
* GET /admin/backups - Danh sách bản sao lưu (System Admin)
* GET/PUT /admin/config - Cấu hình tham số hệ thống (System Admin)

### 6.10. Notifications Module
* GET /notifications - Danh sách thông báo (Bearer)
* PUT /notifications/{id}/read - Đánh dấu đã đọc 1 thông báo (Bearer)
* PUT /notifications/read-all - Đánh dấu đã đọc tất cả (Bearer)
* GET/PUT /notifications/settings - Cấu hình nhận thông báo (Bearer)

---

## 7. Traceability Matrix

| Functional Requirement (FR) | Use Case (UC) | Screen ID | RESTful API Endpoint | HTTP Method |
| :--- | :--- | :--- | :--- | :--- |
| FR-US-01 | UC-01 | S-PUB-01 | /auth/login | POST |
| FR-US-02 | UC-02 | S-PUB-02 | /auth/register | POST |
| FR-US-05 | UC-01 | S-USR-01 | /users/me | GET / PUT |
| FR-FG-01 | UC-03 | S-FAM-01 | /families | POST |
| FR-FG-04 | UC-04 | S-GEN-01 | /families/{id}/relationships | POST |
| FR-FG-05 | UC-05 | S-GEN-02 | /families/{id}/tree | GET |
| FR-COM-01 | UC-06 | S-COM-01 | /families/{id}/posts | GET / POST |
| FR-EVT-01 | UC-07 | S-EVT-01 | /families/{id}/events | GET / POST |
| FR-AI-01 | UC-10 | S-AI-01 | /ai/chat | POST |
| FR-ADM-01 | UC-12 | S-ADM-01 | /admin/users | GET |