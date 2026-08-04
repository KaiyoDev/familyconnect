# Stakeholder Analysis

## 1. Stakeholder List (Danh sách Stakeholder)
Dựa trên kiến trúc và yêu cầu của hệ thống FamilyConnect[cite: 1], dưới đây là danh sách các bên liên quan:
*   **Guest (Khách)**: Người dùng chưa đăng nhập hoặc đang chờ xác thực.
*   **Family Member (Thành viên gia đình)**: Người dùng cuối, thành viên thuộc một gia tộc đã được xác thực trên hệ thống.
*   **Family Owner (Trưởng gia tộc / Quản trị viên gia đình)**: Người chịu trách nhiệm quản lý thông tin gia phả và các hoạt động của một gia đình/dòng họ cụ thể.
*   **System Administrator (Quản trị viên hệ thống)**: Nhân sự kỹ thuật vận hành, bảo trì và quản lý toàn bộ nền tảng FamilyConnect.
*   **AI Service (Dịch vụ Trí tuệ nhân tạo)**: Hệ thống đóng vai trò như một trợ lý thông minh cung cấp các dịch vụ xử lý ngôn ngữ và gợi ý[cite: 1].
*   **Notification/Email Service (Dịch vụ Thông báo)**: Hệ thống bên thứ ba hỗ trợ gửi email, mã xác thực và nhắc nhở sự kiện.

## 2. Stakeholder Description (Phân tích Stakeholder)

### Guest (Khách)
*   **Vai trò:** Người dùng truy cập hệ thống nhưng chưa có tài khoản hoặc chưa được xác thực vào một gia đình cụ thể.
*   **Mục tiêu:** Tìm hiểu nền tảng, thực hiện đăng ký tài khoản và chờ được phê duyệt để gia nhập không gian số của gia đình[cite: 1].
*   **Quyền hạn:** Xem trang chủ giới thiệu, đăng ký tài khoản, đăng nhập.
*   **Trách nhiệm:** Cung cấp thông tin cá nhân chính xác để quá trình xác minh diễn ra thuận lợi.
*   **Mức độ ảnh hưởng:** Thấp (Low).
*   **Mức độ quan tâm:** Trung bình (Medium).

### Family Member (Thành viên gia đình)
*   **Vai trò:** Người dùng chính của hệ thống, tương tác trực tiếp qua Web Portal hoặc Mobile Application[cite: 1].
*   **Mục tiêu:** Kết nối với người thân, cập nhật tin tức, xem cây gia phả, tìm kiếm thông tin và tham gia các sự kiện gia đình[cite: 1].
*   **Quyền hạn:** Đăng bài, bình luận, chia sẻ ảnh, xác nhận tham gia sự kiện (RSVP), truy vấn trợ lý AI, xem danh bạ gia đình[cite: 1].
*   **Trách nhiệm:** Tuân thủ quy định của cộng đồng gia đình, bảo mật thông tin nội bộ.
*   **Mức độ ảnh hưởng:** Trung bình (Medium).
*   **Mức độ quan tâm:** Cao (High).

### Family Owner (Trưởng gia tộc / Quản trị viên gia đình)
*   **Vai trò:** Người có thẩm quyền cao nhất trong một không gian gia đình (Family workspace).
*   **Mục tiêu:** Số hóa và bảo tồn di sản gia đình, tổ chức sự kiện, gắn kết các thế hệ và quản lý thông tin gia phả chính xác[cite: 1].
*   **Quyền hạn:** Quản lý thành viên (phê duyệt/xóa), quản lý cấu trúc gia phả (thêm nhánh, nút), tạo sự kiện, quản lý kho lưu trữ số (di sản gia đình)[cite: 1].
*   **Trách nhiệm:** Duy trì tính chính xác của cây gia phả, điều phối các hoạt động chung của dòng họ.
*   **Mức độ ảnh hưởng:** Cao (High).
*   **Mức độ quan tâm:** Cao (High).

### System Administrator (Quản trị viên hệ thống)
*   **Vai trò:** Nhân viên kỹ thuật quản lý hệ thống FamilyConnect thông qua Dashboard.
*   **Mục tiêu:** Đảm bảo hệ thống hoạt động ổn định, bảo mật cao và sẵn sàng mở rộng[cite: 1].
*   **Quyền hạn:** Quản lý toàn bộ người dùng (Role-Based Access Control), kiểm duyệt nội dung, cấu hình hệ thống, thực hiện Backup & Restore[cite: 1].
*   **Trách nhiệm:** Giám sát nhật ký hoạt động (Audit logging), đảm bảo tính sẵn sàng cao (High Availability), hỗ trợ kỹ thuật[cite: 1].
*   **Mức độ ảnh hưởng:** Cao (High).
*   **Mức độ quan tâm:** Cao (High).

### AI Service (Dịch vụ Trí tuệ nhân tạo)
*   **Vai trò:** Hệ thống backend cung cấp các tính năng thông minh qua RESTful APIs[cite: 1].
*   **Mục tiêu:** Cung cấp trải nghiệm tìm kiếm ngữ nghĩa, giải thích mối quan hệ và gợi ý nội dung cá nhân hóa[cite: 1].
*   **Quyền hạn:** Truy cập (chỉ đọc) vào đồ thị gia phả và dữ liệu người dùng để huấn luyện hoặc trích xuất ngữ cảnh.
*   **Trách nhiệm:** Phản hồi chính xác các truy vấn của người dùng, hoạt động ổn định và bảo mật dữ liệu.
*   **Mức độ ảnh hưởng:** Cao (High) - Do là tính năng cốt lõi của dự án[cite: 1].
*   **Mức độ quan tâm:** Thấp (Low) - Do là hệ thống máy móc.

## 3. Stakeholder Matrix (Ma trận Stakeholder)

| Stakeholder | Vai trò (Role) | Quyền hạn (Permissions) | Mức độ ảnh hưởng (Power/Influence) | Mức độ quan tâm (Interest) | Chiến lược quản lý |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Family Owner** | Quản lý gia đình | Full quyền trong phạm vi gia đình | Cao | Cao | Quản lý chặt chẽ (Manage Closely) |
| **System Admin** | Vận hành hệ thống | Full quyền toàn hệ thống | Cao | Cao | Quản lý chặt chẽ (Manage Closely) |
| **AI Service** | Trợ lý thông minh | Đọc/Xử lý dữ liệu | Cao | Thấp | Giữ hài lòng (Keep Satisfied) |
| **Family Member** | Người dùng cuối | Tương tác, xem gia phả | Trung bình | Cao | Luôn thông tin (Keep Informed) |
| **Guest** | Khách truy cập | Đăng ký, xem giới thiệu | Thấp | Trung bình | Giám sát (Monitor) |

## 4. Stakeholder Map (Sơ đồ Stakeholder)

```mermaid
mindmap
  root((FamilyConnect
  System))
    Internal Users
      System Administrator
        ::icon(fas fa-user-shield)
    Core Users
      Family Owner
        ::icon(fas fa-user-tie)
      Family Member
        ::icon(fas fa-users)
    External Users
      Guest
        ::icon(fas fa-user)
    External/System Services
      AI Service Layer
        ::icon(fas fa-robot)
      Notification Service
        ::icon(fas fa-envelope)