# 05. Non-Functional Requirements

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Yêu cầu Phi chức năng (Non-Functional Requirements Specification)
> **Jira:** [FT8-7](https://familyconnect.atlassian.net/browse/FT8-7), Phân tích yêu cầu phi chức năng
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Draft v1.0

---

Tài liệu này xác định các tiêu chí về chất lượng, hiệu năng, bảo mật, khả năng mở rộng và các ràng buộc kỹ thuật của nền tảng **FamilyConnect**, làm cơ sở để thiết kế kiến trúc hệ thống và đánh giá chất lượng phần mềm trong các giai đoạn tiếp theo.

---

## 1. Phân loại và Danh sách Non-Functional Requirements

Hệ thống FamilyConnect phân loại các yêu cầu phi chức năng thành các nhóm chính dựa trên định hướng của đề tài:

| Mã ID | Tên yêu cầu | Nhóm phân loại | Mô tả tóm tắt | Mức độ ưu tiên |
| :--- | :--- | :--- | :--- | :--- |
| **NFR-01** | Responsive Web Application | Usability / Compatibility | Giao diện web tự động thích ứng với nhiều kích thước màn hình thiết bị. | High |
| **NFR-02** | Cross-platform Mobile Application | Compatibility / Portability | Ứng dụng di động hoạt động đa nền tảng (iOS/Android). | High |
| **NFR-03** | Secure Authentication (JWT) | Security | Xác thực người dùng an toàn bằng JSON Web Token. | High |
| **NFR-04** | RESTful API Architecture | Maintainability / Compatibility | Kiến trúc giao tiếp chuẩn RESTful giữa các tầng hệ thống. | High |
| **NFR-05** | Modular Software Architecture | Maintainability / Scalability | Kiến trúc phần mềm phân chia thành các mô-đun độc lập. | High |
| **NFR-06** | Interactive Graph Visualization | Performance / Usability | Biểu diễn và tương tác đồ thị gia phả trực quan. | Medium |
| **NFR-07** | PostgreSQL Database | Reliability / Performance | Lưu trữ dữ liệu quan hệ và cấu trúc đồ thị bằng PostgreSQL. | High |
| **NFR-08** | AI Service Integration | Performance / Functionality | Tích hợp dịch vụ AI hỗ trợ tìm kiếm ngữ nghĩa và trợ lý tri thức. | High |
| **NFR-09** | Docker Deployment | Portability / Maintainability | Đóng gói và triển khai ứng dụng bằng Docker container. | High |
| **NFR-10** | High Availability | Availability | Đảm bảo hệ thống vận hành liên tục, giảm thiểu thời gian chết. | Medium |
| **NFR-11** | Audit Logging | Security / Reliability | Ghi nhận toàn bộ nhật ký hoạt động hệ thống và bảo mật. | High |

---

## 2. Đặc tả chi tiết từng yêu cầu phi chức năng

### 1. Responsive Web Application
* **Requirement ID:** NFR-01
* **Requirement Name:** Responsive Web Application
* **Description:** Web Management Portal phải tự động điều chỉnh bố cục, hình ảnh và thành phần giao diện sao cho phù hợp với mọi kích thước màn hình.
* **Rationale:** Giúp người dùng dễ dàng quản lý gia phả và tương tác với cộng đồng mọi lúc, mọi nơi trên trình duyệt web mà không gặp lỗi hiển thị.
* **Acceptance Criteria:** Giao diện hiển thị tốt trên các trình duyệt phổ biến và vượt qua các bài kiểm tra giao diện tương thích.
* **Priority:** High

### 2. Cross-platform Mobile Application
* **Requirement ID:** NFR-02
* **Requirement Name:** Cross-platform Mobile Application
* **Description:** Ứng dụng di động dành cho thành viên gia đình phải được phát triển dưới dạng đa nền tảng.
* **Rationale:** Đảm bảo khả năng tiếp cận rộng rãi cho mọi thế hệ thành viên trong gia đình sử dụng các dòng điện thoại thông minh khác nhau.
* **Acceptance Criteria:** Ứng dụng được biên dịch và chạy ổn định trên các hệ điều hành di động chính.
* **Priority:** High

### 3. Secure Authentication (JWT)
* **Requirement ID:** NFR-03
* **Requirement Name:** Secure Authentication (JWT)
* **Description:** Hệ thống sử dụng JSON Web Token (JWT) để quản lý phiên đăng nhập và xác thực.
* **Rationale:** Cung cấp cơ chế xác thực stateless bảo mật cao, tối ưu hóa hiệu năng cho các ứng dụng phân tán.
* **Acceptance Criteria:** Quản lý phiên đăng nhập hợp lệ thông qua token bảo mật và mã hóa thông tin người dùng an toàn.
* **Priority:** High

### 4. RESTful API Architecture
* **Requirement ID:** NFR-04
* **Requirement Name:** RESTful API Architecture
* **Description:** Giao tiếp giữa các thành phần hệ thống phải tuân thủ chuẩn kiến trúc RESTful API.
* **Rationale:** Đảm bảo tính tách biệt giữa Frontend và Backend, giúp dễ dàng mở rộng và bảo trì.
* **Acceptance Criteria:** Các điểm cuối (endpoints) tuân thủ tiêu chuẩn REST và định dạng JSON.
* **Priority:** High

### 5. Modular Software Architecture
* **Requirement ID:** NFR-05
* **Requirement Name:** Modular Software Architecture
* **Description:** Phần mềm được thiết kế theo kiến trúc mô-đun.
* **Rationale:** Giảm độ phức tạp khi phát triển, cho phép làm việc song song và dễ dàng mở rộng tính năng mới.
* **Acceptance Criteria:** Các mô-đun được tách biệt độc lập theo chức năng.
* **Priority:** High

### 6. Interactive Graph Visualization
* **Requirement ID:** NFR-06
* **Requirement Name:** Interactive Graph Visualization
* **Description:** Mô-đun quản lý gia phả cung cấp giao diện trực quan hóa đồ thị gia đình tương tác.
* **Rationale:** Giúp người dùng dễ dàng nắm bắt mối quan hệ họ hàng qua nhiều thế hệ.
* **Acceptance Criteria:** Biểu diễn sơ đồ cây gia phả rõ ràng, hỗ trợ tương tác mượt mà.
* **Priority:** Medium

### 7. PostgreSQL Database
* **Requirement ID:** NFR-07
* **Requirement Name:** PostgreSQL Database
* **Description:** Hệ thống sử dụng cơ sở dữ liệu quan hệ PostgreSQL.
* **Rationale:** Cung cấp tính toàn vẹn dữ liệu cao và hỗ trợ các truy vấn cấu trúc hiệu quả.
* **Acceptance Criteria:** Kết nối và vận hành ổn định với cơ sở dữ liệu PostgreSQL.
* **Priority:** High

### 8. AI Service Integration
* **Requirement ID:** NFR-08
* **Requirement Name:** AI Service Integration
* **Description:** Tích hợp tầng dịch vụ AI để hỗ trợ tìm kiếm ngữ nghĩa, trợ lý tri thức và gợi ý.
* **Rationale:** Mang lại trải nghiệm thông minh, giúp người dùng khai thác sâu hơn kho tàng tri thức dòng họ.
* **Acceptance Criteria:** Phản hồi chính xác các tác vụ trợ lý AI theo yêu cầu hệ thống.
* **Priority:** High

### 9. Docker Deployment
* **Requirement ID:** NFR-09
* **Requirement Name:** Docker Deployment
* **Description:** Toàn bộ hệ thống phải được đóng gói bằng Docker container.
* **Rationale:** Đảm bảo tính đồng nhất giữa môi trường phát triển và vận hành.
* **Acceptance Criteria:** Hệ thống có khả năng khởi chạy thành công thông qua cấu hình Docker.
* **Priority:** High

### 10. High Availability
* **Requirement ID:** NFR-10
* **Requirement Name:** High Availability
* **Description:** Hệ thống được thiết kế hướng tới tính sẵn sàng cao.
* **Rationale:** Đảm bảo người dùng có thể truy cập thông tin gia đình bất cứ lúc nào.
* **Acceptance Criteria:** Hệ thống duy trì hoạt động ổn định và có khả năng tự phục hồi lỗi.
* **Priority:** Medium

### 11. Audit Logging
* **Requirement ID:** NFR-11
* **Requirement Name:** Audit Logging
* **Description:** Hệ thống phải ghi nhận toàn bộ nhật ký hoạt động quan trọng.
* **Rationale:** Phục vụ cho công tác kiểm tra bảo mật và theo dõi lịch sử thao tác dữ liệu.
* **Acceptance Criteria:** Lưu trữ đầy đủ các bản ghi nhật ký (audit logs) cho các sự kiện quan trọng.
* **Priority:** High