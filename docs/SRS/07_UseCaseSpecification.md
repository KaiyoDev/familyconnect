# 07. Use Case Specification

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Đặc tả Use Case (Use Case Specification)
> **Jira:** [FT8-10](https://familyconnect.atlassian.net/browse/FT8-10), Đặc tả Use Case
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Final v1.0

---

## 1. Danh sách Use Case & Bảng ánh xạ Yêu cầu (Traceability Matrix)

| ID | Tên Use Case | Primary Actor | Yêu cầu chức năng tương ứng (FR) | Độ ưu tiên | Tần suất |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UC-01** | Đăng nhập & Xác thực | All Users | User & Security (Registration, Auth, Security) | High | Daily |
| **UC-02** | Đăng ký & Xác minh Thành viên | Guest / Member | User & Security (Registration, Verification) | High | Low |
| **UC-03** | Quản lý Gia đình & Chi nhánh | Family Admin | Family & Genealogy (Family/Branch Mgt) | High | Low |
| **UC-04** | Quản lý Quan hệ Cây gia phả | Member / Admin | Family & Genealogy (Parent-Child, Marriage) | High | Medium |
| **UC-05** | Truy vấn & Trực quan hóa Cây gia phả | All Users | Family & Genealogy (Tree, Relationship Query) | High | High |
| **UC-06** | Quản lý Bài viết & Tương tác | Member | Community (Posts, Comments, Reactions, Media) | Medium | Daily |
| **UC-07** | Quản lý Sự kiện & Điểm danh (RSVP) | Member | Events (Create, RSVP, Reminders, Gallery) | Medium | Medium |
| **UC-08** | Tra cứu Danh bạ & Hồ sơ Thành viên | Member | Family Directory (Search by profession/location) | Medium | Medium |
| **UC-09** | Quản lý Lưu trữ & Di sản Gia đình | Member | Family Heritage (Stories, Historical Docs, Archives) | Low | Medium |
| **UC-10** | Trợ lý AI & Truy vấn Tri thức Gia đình | Member | AI-assisted Services (Semantic Search, Assistant) | High | Daily |
| **UC-11** | Xem Báo cáo & Thống kê | Admin / Member | Dashboard & Reporting (Demographics, Activity) | Low | Low |
| **UC-12** | Quản trị Hệ thống & Kiểm duyệt | System Admin | Administration (User Mgt, Moderation, Audit Log) | High | Low |

---

## 2. Đặc tả Chi tiết các Use Case Chính (Template Standard)

### UC-01: Đăng nhập & Xác thực (Login & Authentication)
* **Use Case ID:** UC-01
* **Use Case Name:** Đăng nhập & Xác thực người dùng
* **Brief Description:** Cho phép người dùng xác thực vào hệ thống qua tài khoản cá nhân để nhận quyền truy cập tương ứng với vai trò.
* **Primary Actor:** Người dùng (Member, Family Admin, System Admin)
* **Secondary Actor:** AI Service (Gợi ý xác thực/Phát hiện bất thường)
* **Trigger:** Người dùng mở ứng dụng Mobile/Web Portal và chọn Đăng nhập.
* **Preconditions:** Người dùng đã có tài khoản trên hệ thống.
* **Postconditions:** Người dùng được cấp Token JWT và truy cập đúng giao diện theo quyền (RBAC).
* **Main Flow:**
  1. Người dùng nhập Email/Số điện thoại và Mật khẩu.
  2. Hệ thống kiểm tra thông tin đăng nhập trong Cơ sở dữ liệu.
  3. Hệ thống tạo chuỗi JWT Access Token và Refresh Token.
  4. Hệ thống điều hướng người dùng đến Trang chủ/Dashboard.
* **Alternative Flow:**
  * **2a. Đăng nhập qua OAuth (Google/Apple):** Người dùng chọn đăng nhập qua bên thứ ba -> Hệ thống xác thực qua SDK -> Tạo phiên làm việc.
* **Exception Flow:**
  * **2b. Sai thông tin:** Hệ thống báo lỗi "Tài khoản hoặc mật khẩu không chính xác" và yêu cầu nhập lại.
  * **2c. Tài khoản bị khóa:** Hệ thống thông báo lý do bị khóa bởi Kiểm duyệt viên.
* **Business Rules:** Mật khẩu nhập sai quá 5 lần sẽ khóa tạm thời 15 phút.
* **Priority:** High | **Frequency of Use:** Daily

---

### UC-04: Quản lý Quan hệ Cây gia phả (Genealogy Relationship Management)
* **Use Case ID:** UC-04
* **Use Case Name:** Cập nhật thông tin và Quan hệ Cây gia phả
* **Brief Description:** Thêm, chỉnh sửa thông tin thành viên, thiết lập quan hệ cha-con, vợ-chồng để cập nhật dữ liệu dòng họ.
* **Primary Actor:** Member (được cấp quyền), Family Admin
* **Secondary Actor:** PostgreSQL (Graph Data Store)
* **Trigger:** Người dùng muốn thêm thành viên mới hoặc nối quan hệ trong cây gia phả.
* **Preconditions:** Đã tạo Gia đình (UC-03) và có quyền quản lý thông tin gia phả.
* **Postconditions:** Đồ thị gia phả được cập nhật thành công, phát sự kiện đồng bộ dữ liệu tới AI Layer.
* **Main Flow:**
  1. Người dùng chọn nút "Thêm thành viên" hoặc "Nối quan hệ" trên giao diện Cây gia phả.
  2. Hệ thống hiển thị Form điền thông tin (Họ tên, Ngày sinh, Thế hệ, Loại quan hệ: Vợ/Chồng, Cha/Mẹ - Con).
  3. Người dùng nhập thông tin và lưu.
  4. Hệ thống kiểm tra logic quan hệ (Business Rules).
  5. Hệ thống lưu nút (Node) và cạnh (Edge) mới vào cơ sở dữ liệu đồ thị.
  6. Hệ thống làm mới (render lại) cây gia phả.
* **Alternative Flow:**
  * **3a. Thêm thành viên từ Danh bạ có sẵn:** Người dùng gán một tài khoản Member đã có vào làm con/vợ/chồng của một nút trên cây.
* **Exception Flow:**
  * **4a. Mâu thuẫn logic:** Nhập tuổi con lớn hơn tuổi cha/mẹ -> Hệ thống chặn và hiển thị thông báo lỗi logic.
* **Business Rules:** Khoảng cách tuổi giữa cha/mẹ và con tối thiểu là 12 năm. Một người không thể có nhiều hơn 2 cha/mẹ ruột.
* **Priority:** High | **Frequency of Use:** Medium

---

### UC-05: Truy vấn & Trực quan hóa Cây gia phả (Interactive Genealogy Tree)
* **Use Case ID:** UC-05
* **Use Case Name:** Xem và Tương tác Cây gia phả
* **Brief Description:** Hiển thị trực quan cây gia phả dạng sơ đồ đồ thị tương tác, hỗ trợ phóng to/thu nhỏ, tìm kiếm và giải thích quan hệ.
* **Primary Actor:** All Users (Thành viên trong dòng họ)
* **Secondary Actor:** AI Service (Phân tích và giải thích xưng hô)
* **Trigger:** Người dùng truy cập vào mục "Cây gia phả".
* **Preconditions:** Người dùng thuộc về ít nhất một Gia đình trên hệ thống.
* **Postconditions:** Sơ đồ cây được tải thành công.
* **Main Flow:**
  1. Người dùng chọn gia đình/chi nhánh cần xem.
  2. Hệ thống truy vấn dữ liệu đồ thị và hiển thị sơ đồ Cây gia phả (Interactive Graph).
  3. Người dùng thao tác: Zoom, Pan, hoặc click vào một nút thành viên để xem Tóm tắt hồ sơ.
  4. Người dùng chọn 2 nút bất kỳ và ấn "Giải thích quan hệ".
  5. Hệ thống gọi AI Service để xuất ra cách xưng hô chuẩn (ví dụ: "Ông Cố Họ", "Cháu Họ").
* **Alternative Flow:**
  * **2a. Chế độ Xem danh sách (List View):** Người dùng chuyển từ dạng Graph sang dạng Danh sách phân cấp (Tree View).
* **Exception Flow:**
  * **2b. Dữ liệu quá lớn:** Cây có hơn 1000 nút -> Hệ thống tự động phân trang/thu gọn các nhánh xa và chỉ hiển thị 3 thế hệ gần nhất.
* **Business Rules:** Người dùng ngoài dòng họ không thể truy cập sơ đồ gia phả (nếu cài đặt chế độ Riêng tư).
* **Priority:** High | **Frequency of Use:** High

---

### UC-10: Trợ lý AI & Truy vấn Tri thức Gia đình (AI Family Knowledge Assistant)
* **Use Case ID:** UC-10
* **Use Case Name:** Hỏi đáp và Tìm kiếm Ngữ nghĩa với Trợ lý AI
* **Brief Description:** Tích hợp mô hình ngôn ngữ lớn (LLM) cho phép tìm kiếm ngữ nghĩa, tóm tắt di sản và trả lời các câu hỏi liên quan đến lịch sử, quan hệ gia đình.
* **Primary Actor:** Member
* **Secondary Actor:** AI Service (LLM & Vector Database / RAG)
* **Trigger:** Người dùng nhập câu hỏi vào ô tìm kiếm AI hoặc giao diện Chatbot.
* **Preconditions:** Dữ liệu di sản, bài viết và gia phả đã được trích xuất vector hóa (Indexing).
* **Postconditions:** AI đưa ra câu trả lời chính xác dựa trên tri thức gia đình.
* **Main Flow:**
  1. Người dùng gửi câu hỏi (Ví dụ: *"Cho tôi biết thông tin về những người trong họ làm ngành Y?"* hoặc *"Tóm tắt tiểu sử của Cụ Tôn"*).
  2. Hệ thống gửi câu hỏi đến AI Service Layer.
  3. AI Service thực hiện Tìm kiếm Ngữ nghĩa (Semantic Search) trong cơ sở dữ liệu Vector (RAG).
  4. Hệ thống tổng hợp dữ liệu, tạo câu trả lời và trích dẫn nguồn (bài viết, hồ sơ gia phả).
  5. Hiển thị kết quả cho người dùng.
* **Alternative Flow:**
  * **1a. Gợi ý thông minh:** AI tự động hiển thị danh sách các thành viên có liên quan hoặc sự kiện sắp tới dựa trên hành vi của người dùng.
* **Exception Flow:**
  * **3a. Không tìm thấy thông tin:** AI phản hồi lịch sự: *"Hệ thống chưa có dữ liệu về thông tin này trong di sản gia đình."*
* **Business Rules:** AI chỉ được truy vấn dữ liệu trong phạm vi Gia đình mà người dùng đó là thành viên (đảm bảo tính bảo mật).
* **Priority:** High | **Frequency of Use:** Daily

---

## 3. Kiểm tra tính đầy đủ & Nhất quán (Verification Check)

- **Độ bao phủ Requirement (100% Coverage):** Tất cả các nhóm chức năng (User Security, Genealogy, Community, Events, Directory, Heritage, AI, Dashboard, Admin) đã được ánh xạ thành 12 Use Case bao quát.
- **Tính nhất quán Actor:** Các Actor (`Member`, `Family Admin`, `System Admin`, `AI Service`) được định nghĩa rõ ràng về vai trò và phạm vi truy cập (RBAC).
- **Tính thực thi:** Kiến trúc tuân thủ mô hình 3 lớp (Mobile/Web Portal -> RESTful API -> AI Service Layer & PostgreSQL Graph).