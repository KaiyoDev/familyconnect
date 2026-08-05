# 01. Project Analysis

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Phân tích Yêu cầu (Requirement Analysis)
> **Jira:** [FT8-2](https://familyconnect.atlassian.net/browse/FT8-2), Phân tích yêu cầu và lập kế hoạch yêu cầu
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Final v1.0

---

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
  * **Kỹ thuật:** Ứng dụng Web cần tương thích với nhiều kích thước màn hình (Responsive) và ứng dụng di động đa nền tảng. Yêu cầu xác thực bảo mật bằng JWT và sử dụng cơ sở dữ liệu PostgreSQL. Trực quan hóa dữ liệu dạng đồ thị (Interactive Graph Visualization) và tích hợp dịch vụ AI. Yêu cầu về kiến trúc bao gồm tính sẵn sàng cao (High Availability), đóng gói Docker và lưu vết hệ thống (Audit Logging).
  * **Thời gian:** Hoàn thành Sprint 1 (Phân tích yêu cầu) trong 2 tuần, Sprint 2 (Thiết kế & Development) trong 4 tuần.
  * **Ngân sách:** Giới hạn trong phạm vi dự án học tập, sử dụng các dịch vụ miễn phí (free tier) cho AI, hosting và deployment.
  * **Nhân lực:** Nhóm phát triển 2-3 thành viên, yêu cầu phân chia công việc rõ ràng và tài liệu hóa đầy đủ.

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

1. **Stakeholder Analysis:** Phân tích các bên liên quan, xác định vai trò, nhu cầu, mức độ quan tâm và ảnh hưởng của từng bên đối với dự án. Đầu ra là danh sách các stakeholder và yêu cầu chính của họ.
2. **Vision & Scope:** Tầm nhìn và phạm vi dự án, mô tả giá trị sản phẩm, đối tượng phục vụ, phạm vi (trong/ngoài) và ràng buộc, làm cơ sở thống nhất giữa các bên.
3. **Functional Requirements:** Đặc tả các yêu cầu chức năng, phân rã từng module thành các chức năng cụ thể, có mã số (FR-x.y) và tiêu chí chấp nhận.
4. **Non-functional Requirements:** Đặc tả các yêu cầu phi chức năng, hiệu năng, bảo mật, khả dụng, tương thích, khả năng mở rộng.
5. **Use Case Diagram:** Sơ đồ Use Case tổng quan và chi tiết cho từng module.
6. **Use Case Specification:** Đặc tả chi tiết kịch bản cho từng Use Case, bao gồm tác nhân, tiền điều kiện, luồng chính, luồng thay thế và hậu điều kiện.

### 4.1. Trình tự thực hiện

| Bước | Hoạt động | Kết quả đầu ra |
|------|-----------|----------------|
| 1 | Thu thập và đọc toàn bộ tài liệu đề tài, xác định bối cảnh, vấn đề, giải pháp, sản phẩm. | Tài liệu Phân tích đề tài (`01_ProjectAnalysis.md`) |
| 2 | Phân tích các bên liên quan (Stakeholder Analysis). | Ma trận stakeholder, danh sách yêu cầu của từng bên |
| 3 | Xây dựng tầm nhìn và phạm vi (Vision & Scope). | Tài liệu Vision & Scope (`03_VisionAndScope.md`) |
| 4 | Đặc tả yêu cầu chức năng và phi chức năng. | Bảng đặc tả FR/NFR có mã số |
| 5 | Thiết kế Use Case Diagram tổng quan và chi tiết. | Sơ đồ Use Case |
| 6 | Đặc tả chi tiết từng Use Case. | Bảng đặc tả Use Case (`07_UseCaseSpecification.md`) |
| 7 | Rà soát, thống nhất với các bên liên quan và chốt tài liệu SRS. | SRS hoàn chỉnh |

### 4.2. Các tài liệu sẽ tạo trong Sprint 1

| Tài liệu | Đường dẫn dự kiến | Mô tả |
|----------|-------------------|-------|
| Project Analysis | `docs/SRS/01_ProjectAnalysis.md` | Phân tích đề tài, bài toán, mục tiêu, phạm vi, danh sách module (tài liệu hiện tại) |
| Stakeholder Analysis | `docs/SRS/02_StakeholderAnalysis.md` | Phân tích các bên liên quan |
| Vision & Scope | `docs/SRS/03_VisionAndScope.md` | Tầm nhìn và phạm vi dự án |
| Functional Requirements | `docs/SRS/04_FunctionalRequirements.md` | Đặc tả yêu cầu chức năng (FR) |
| Non-functional Requirements | `docs/SRS/05_NonFunctionalRequirements.md` | Đặc tả yêu cầu phi chức năng (NFR) |
| Use Case Diagram | `docs/SRS/06_UseCaseDiagram.md` | Sơ đồ Use Case tổng quan và chi tiết |
| Use Case Specification | `docs/SRS/07_UseCaseSpecification.md` | Đặc tả chi tiết từng Use Case |
| Business Rules | `docs/SRS/08_BusinessRules.md` | Quy tắc nghiệp vụ |
| Glossary & Data Dictionary | `docs/SRS/09_GlossaryAndDataDictionary.md` | Thuật ngữ và từ điển dữ liệu |
| Business Process Model | `docs/SRS/10_BusinessProcessModel.md` | Mô hình quy trình nghiệp vụ |

### 4.3. Tiêu chí hoàn thành (Definition of Done)

**Tiêu chí chung cho toàn bộ Sprint 1:**

* Toàn bộ 9 module chính được phân tích và đặc tả yêu cầu đầy đủ.
* Mỗi yêu cầu chức năng có mã số duy nhất (FR-x.y) và tiêu chí chấp nhận đo lường được.
* Toàn bộ Use Case quan trọng (High priority) có Use Case Specification đi kèm với đầy đủ: Precondition, Main Flow, Alternative Flow, Exception Flow, Postcondition.
* Tài liệu được nhóm (giảng viên/các bên liên quan) rà soát và thống nhất.
* Các tài liệu được commit trên nhánh `feature/FT8-2-requirement-analysis` và tạo Pull Request vào `develop`.

**Tiêu chí hoàn thành cho từng module:**

| Module | Tiêu chí hoàn thành |
|--------|---------------------|
| **User & Security** | Có ít nhất 5 Use Case (Đăng ký, Đăng nhập, Quên mật khẩu, Quản lý hồ sơ, Xác thực thành viên) với đầy đủ luồng chính, luồng thay thế và ngoại lệ. Có Business Rules về mật khẩu, xác thực, phân quyền. |
| **Family & Genealogy** | Có ít nhất 4 Use Case (Quản lý gia đình, Quản lý thành viên, Xem cây gia phả, Tra cứu quan hệ). Có Business Rules về cấu trúc cây, ràng buộc tuổi, quan hệ hợp lệ. Có mô tả thuật toán truy vấn đồ thị. |
| **Community** | Có ít nhất 3 Use Case (Đăng bài, Bình luận/Tương tác, Thông báo). Có Business Rules về kiểm duyệt nội dung, quyền đăng bài, hiển thị feed. |
| **Events** | Có ít nhất 4 Use Case (Tạo sự kiện, RSVP, Quản lý người tham gia, Nhắc nhở). Có Business Rules về thời gian, trạng thái sự kiện, quyền tạo sự kiện. |
| **Family Directory** | Có ít nhất 1 Use Case (Tra cứu thành viên). Có Business Rules về tìm kiếm theo nghề nghiệp, địa điểm, thế hệ. Có mô tả thuật toán gợi ý. |
| **Family Heritage** | Có ít nhất 3 Use Case (Quản lý tư liệu, Thành viên tiêu biểu, Thư viện ảnh). Có Business Rules về quyền truy cập, định dạng file, dung lượng lưu trữ. |
| **AI-assisted Services** | Có ít nhất 2 Use Case (Tìm kiếm ngữ nghĩa, Trợ lý AI). Có mô tả kiến trúc RAG, Vector Database, LLM integration. Có Business Rules về phạm vi dữ liệu AI được truy cập. |
| **Dashboard & Reporting** | Có ít nhất 2 Use Case (Xem thống kê, Xuất báo cáo). Có mô tả các metrics cần hiển thị, quyền truy cập báo cáo. |
| **Administration** | Có ít nhất 4 Use Case (Quản lý người dùng, Kiểm duyệt, Audit Log, Backup/Restore). Có Business Rules về RBAC, nhật ký hoạt động, quy trình backup. |

## 5. Phân tích Rủi ro (Risk Analysis)

| ID | Rủi ro | Mô tả | Xác suất | Tác động | Biện pháp giảm thiểu |
|----|--------|-------|----------|----------|---------------------|
| R1 | Phạm vi dự án quá rộng | 9 modules với nhiều tính năng phức tạp, khó hoàn thành trong thời gian giới hạn | Cao | Cao | Ưu tiên MVP với 3 modules core (User & Security, Family & Genealogy, Community). Các modules khác triển khai ở Sprint 2-3. |
| R2 | Tích hợp AI phức tạp | AI Service Layer yêu cầu kiến thức về LLM, RAG, Vector Database, có thể vượt quá năng lực nhóm | Trung bình | Cao | Bắt đầu với API đơn giản (OpenAI API), scale dần. Tìm hiểu RAG framework (LangChain) trước khi implement. |
| R3 | Thiếu dữ liệu gia phả mẫu | Không có dataset thực tế để test thuật toán đồ thị và truy vấn quan hệ | Thấp | Trung bình | Tạo dataset mẫu với 50-100 nodes, import từ Excel/CSV. Sử dụng synthetic data generator nếu cần. |
| R4 | Ràng buộc thời gian | Sprint 1 chỉ có 2 tuần, Sprint 2 có 4 tuần, khó hoàn thành đầy đủ tài liệu và code | Cao | Cao | Lập kế hoạch chi tiết theo ngày, ưu tiên tài liệu trước, code MVP sau. Daily standup để track progress. |
| R5 | Thiếu kinh nghiệm với Graph Database | PostgreSQL Graph extensions (Apache AGE, pgGraph) có thể khó học và debug | Trung bình | Trung bình | Nghiên cứu tài liệu trước, tạo PoC (Proof of Concept) với 10-20 nodes trước khi scale. Consider fallback sang adjacency list nếu quá phức tạp. |
| R6 | Yêu cầu thay đổi giữa chừng | Giảng viên hoặc stakeholders có thể yêu cầu bổ sung/sửa đổi tài liệu sau khi đã hoàn thành | Trung bình | Cao | Freeze requirements sau Sprint 1. Sử dụng version control (Git) để track changes. Tạo change log cho mỗi lần sửa. |

---

## 6. Phụ lục

### 6.1. Tham khảo tài liệu

* **Đề cương dự án:** FamilyConnect - AI-powered Digital Family Community Platform
* **Công nghệ sử dụng:** Python (FastAPI), React/Next.js, PostgreSQL (Graph extensions), Docker, OpenAI API
* **Mô hình phát triển:** Agile/Scrum với 2-week sprints

### 6.2. Lịch sử thay đổi

| Phiên bản | Ngày | Tác giả | Mô tả thay đổi |
|-----------|------|---------|----------------|
| v0.1 | 2026-08-01 | Team | Khởi tạo tài liệu |
| v1.0 | 2026-08-05 | Team | Hoàn thiện Sprint 1, thêm Risk Analysis, fix file paths |
