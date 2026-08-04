# FamilyConnect – Phân tích Yêu cầu (Requirement Analysis)

## 1. Giới thiệu đề tài

* **Tên đề tài:** FamilyConnect: AI-powered Digital Family Community Platform.
* **Tên tiếng Việt:** FamilyConnect: Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo.
* **Bối cảnh dự án (Context):** Các gia đình hiện đại ngày càng phân tán về mặt địa lý do các yếu tố như giáo dục, cơ hội nghề nghiệp, di cư và toàn cầu hóa. Hệ quả là giao tiếp giữa các thành viên trở nên thưa thớt, hồ sơ gia phả khó duy trì và thế hệ trẻ có ít cơ hội hiểu về di sản gia đình cũng như xây dựng các mối quan hệ ý nghĩa.
* **Vấn đề cần giải quyết (Problem Statement):** Các mạng xã hội hiện tại hỗ trợ giao tiếp nhưng không được thiết kế để bảo tồn gia phả hoặc củng cố sự phát triển lâu dài của gia đình. Ngược lại, hệ thống gia phả truyền thống chỉ tập trung vào ghi chép thông tin dòng dõi mà thiếu tính năng cộng đồng tương tác. Do đó, cần có một nền tảng chuyên dụng vừa bảo tồn di sản, vừa tăng cường kết nối và tổ chức các hoạt động gia đình.
* **Giải pháp đề xuất (Proposed Solution):** Phát triển nền tảng FamilyConnect, kết hợp quản lý gia phả thông qua biểu đồ cấu trúc với các dịch vụ cộng đồng. Nền tảng tích hợp các dịch vụ AI để cung cấp khả năng tìm kiếm ngữ nghĩa, truy xuất kiến thức thông minh, giải thích mối quan hệ và đề xuất được cá nhân hóa. Hệ thống áp dụng kiến trúc module: Web Management Portal, Mobile Application và AI Service Layer kết nối qua RESTful APIs.
* **Sản phẩm đầu ra (Expected Deliverables):** Cổng thông tin web (Web Portal), Ứng dụng di động (Mobile Application), các module hệ thống (Gia phả, Cộng đồng, Sự kiện, Di sản, AI Assistant, Báo cáo), dịch vụ RESTful API, Gói triển khai Docker và Tài liệu phần mềm.

## 2. Phân tích bài toán

* **Mục tiêu của hệ thống:** Xây dựng một hệ sinh thái phần mềm thống nhất tích hợp quản lý gia phả, giao tiếp gia đình, quản lý sự kiện, chia sẻ kiến thức và các dịch vụ hỗ trợ bởi AI.
* **Giá trị mang lại:** Cho phép người dùng trực quan hóa các mối quan hệ gia đình, điều hướng qua các thế hệ và duy trì hồ sơ gia đình chính xác. Hệ thống khuyến khích tương tác liên tục, chia sẻ kiến thức và hỗ trợ lẫn nhau giữa các thế hệ thông qua các tính năng cộng đồng, thay vì coi gia phả chỉ là thông tin tĩnh.
* **Đối tượng sử dụng (User Groups):**
  * **Thành viên gia đình (End Users):** sử dụng Ứng dụng di động để tương tác, giao tiếp, xem gia phả và tham gia các hoạt động gia đình.
  * **Người quản lý gia tộc / Quản trị viên (Family Admin / System Admin):** sử dụng Web Management Portal để quản lý thành viên, kiểm duyệt nội dung, cấu hình hệ thống và xem báo cáo.
  * **Khách (Guests):** xem các thông tin công khai được gia đình cho phép (dự kiến ở các giai đoạn sau).
* **Phạm vi của dự án (Project Scope):**
  * *Trong phạm vi (In-scope):* Web Management Portal, Mobile Application, AI Service Layer, RESTful API, Docker Deployment và tài liệu phần mềm.
  * *Ngoài phạm vi (Out-of-scope):* Tích hợp thanh toán, đa ngôn ngữ đầy đủ (chỉ hỗ trợ tiếng Việt/tiếng Anh ở mức cơ bản), ứng dụng gốc (native) chuyên biệt cho từng nền tảng (chỉ triển khai đa nền tảng), tính năng gia phả DNA/ADN.
* **Các ràng buộc ban đầu (Initial Constraints):**
  * Ứng dụng Web cần tương thích với nhiều kích thước màn hình (Responsive) và ứng dụng di động đa nền tảng.
  * Yêu cầu xác thực bảo mật bằng JWT và sử dụng cơ sở dữ liệu PostgreSQL.
  * Trực quan hóa dữ liệu dạng đồ thị (Interactive Graph Visualization) và tích hợp dịch vụ AI.
  * Yêu cầu về kiến trúc bao gồm tính sẵn sàng cao (High Availability), đóng gói Docker và lưu vết hệ thống (Audit Logging).

## 3. Danh sách module chính

Hệ thống được chia thành các module cốt lõi sau:

* **User & Security:** Đăng ký, xác thực, quản lý phân quyền (RBAC), quản lý hồ sơ và xác minh thành viên.
* **Family & Genealogy Management:** Quản lý dòng họ, nhánh, thành viên, quan hệ cha con/hôn nhân, cây gia phả tương tác và truy vấn trực quan hóa mối quan hệ.
* **Community:** Tạo/quản lý bài viết, bình luận, tương tác, chia sẻ tin tức/hình ảnh và thông báo.
* **Events:** Tạo sự kiện, quản lý đăng ký (RSVP), quản lý người tham gia, thư viện ảnh sự kiện và nhắc nhở.
* **Family Directory:** Danh bạ thành viên, hồ sơ chuyên môn/học vấn, tìm kiếm thành viên theo nghề nghiệp, vị trí hoặc thế hệ.
* **Family Heritage:** Lưu trữ tài liệu lịch sử, câu chuyện gia đình, vinh danh thành viên tiêu biểu, thư viện ảnh và kho lưu trữ số.
* **AI-assisted Services:** Tìm kiếm ngữ nghĩa bằng AI, trợ lý kiến thức gia đình, giải thích mối quan hệ, tóm tắt nội dung và đề xuất thành viên/tài nguyên.
* **Dashboard & Reporting:** Thống kê gia đình, bảng điều khiển hoạt động cộng đồng, thống kê sự kiện, nhân khẩu học và trích xuất báo cáo.
* **Administration:** Quản lý người dùng, kiểm duyệt nội dung, nhật ký hoạt động (Audit logging), sao lưu & phục hồi và cấu hình hệ thống.

## 4. Kế hoạch thực hiện Requirement Analysis (Sprint 1)

Trong Sprint 1, các tài liệu (Deliverables) cần hoàn thành cho giai đoạn Phân tích yêu cầu bao gồm:

1. **Stakeholder Analysis:** Phân tích các bên liên quan — xác định vai trò, nhu cầu, mức độ quan tâm và ảnh hưởng của từng bên đối với dự án. Đầu ra là danh sách các stakeholder và yêu cầu chính của họ.
2. **Vision & Scope:** Tầm nhìn và phạm vi dự án — mô tả giá trị sản phẩm, đối tượng phục vụ, phạm vi (trong/ngoài) và ràng buộc, làm cơ sở thống nhất giữa các bên.
3. **Functional Requirements:** Đặc tả các yêu cầu chức năng — phân rã từng module thành các chức năng cụ thể, có mã số (FR-x.y) và tiêu chí chấp nhận.
4. **Non-functional Requirements:** Đặc tả các yêu cầu phi chức năng — hiệu năng, bảo mật, khả dụng, tương thích, khả năng mở rộng.
5. **Use Case Diagram:** Sơ đồ Use Case tổng quan và chi tiết cho từng module.
6. **Use Case Specification:** Đặc tả chi tiết kịch bản cho từng Use Case — bao gồm tác nhân, tiền điều kiện, luồng chính, luồng thay thế và hậu điều kiện.

### 4.1. Trình tự thực hiện

| Bước | Hoạt động | Kết quả đầu ra |
|------|-----------|----------------|
| 1 | Thu thập và đọc toàn bộ tài liệu đề tài, xác định bối cảnh, vấn đề, giải pháp, sản phẩm. | Tài liệu Phân tích đề tài (`01_ProjectAnalysis.md`) |
| 2 | Phân tích các bên liên quan (Stakeholder Analysis). | Ma trận stakeholder, danh sách yêu cầu của từng bên |
| 3 | Xây dựng tầm nhìn và phạm vi (Vision & Scope). | Tài liệu Vision & Scope (`02_VisionScope.md`) |
| 4 | Đặc tả yêu cầu chức năng và phi chức năng. | Bảng đặc tả FR/NFR có mã số |
| 5 | Thiết kế Use Case Diagram tổng quan và chi tiết. | Sơ đồ Use Case |
| 6 | Đặc tả chi tiết từng Use Case. | Bảng đặc tả Use Case (`04_UseCaseSpecification.md`) |
| 7 | Rà soát, thống nhất với các bên liên quan và chốt tài liệu SRS. | SRS hoàn chỉnh |

### 4.2. Các tài liệu sẽ tạo trong Sprint 1

| Tài liệu | Đường dẫn dự kiến | Mô tả |
|----------|-------------------|-------|
| Project Analysis | `docs/SRS/01_ProjectAnalysis.md` | Phân tích đề tài, bài toán, mục tiêu, phạm vi, danh sách module (tài liệu hiện tại) |
| Stakeholder Analysis | `docs/SRS/02_StakeholderAnalysis.md` | Phân tích các bên liên quan |
| Vision & Scope | `docs/SRS/03_VisionScope.md` | Tầm nhìn và phạm vi dự án |
| Software Requirements Specification | `docs/SRS/04_SRS.md` | Đặc tả yêu cầu chức năng (FR) và phi chức năng (NFR) |
| Use Case Diagram | `docs/SRS/05_UseCaseDiagram.md` | Sơ đồ Use Case tổng quan và chi tiết |
| Use Case Specification | `docs/SRS/06_UseCaseSpecification.md` | Đặc tả chi tiết từng Use Case |

### 4.3. Tiêu chí hoàn thành (Definition of Done)

* Toàn bộ 9 module chính được phân tích và đặc tả yêu cầu đầy đủ.
* Mỗi yêu cầu chức năng có mã số duy nhất và tiêu chí chấp nhận đo lường được.
* Toàn bộ Use Case quan trọng có Use Case Specification đi kèm.
* Tài liệu được nhóm (giảng viên/các bên liên quan) rà soát và thống nhất.
* Các tài liệu được commit trên nhánh `feature/FT8-2-requirement-analysis` và tạo Pull Request vào `develop`.
