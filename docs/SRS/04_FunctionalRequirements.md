# 4. Functional Requirements

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Đặc tả yêu cầu chức năng (Functional Requirements Specification)
> **Jira:** [FT8-6](https://familyconnect.atlassian.net/browse/FT8-6), Phân tích yêu cầu chức năng
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Final v1.0

---

## 4.1 Giới thiệu

### 4.1.1 Mục đích

Tài liệu này đặc tả toàn bộ yêu cầu chức năng (Functional Requirements, FR) của hệ thống FamilyConnect, một nền tảng cộng đồng gia đình số tích hợp trí tuệ nhân tạo. Nội dung được phân tích và mở rộng từ đề tài được giao, nhằm:

- Xác định đầy đủ, rõ ràng và có thể đo lường được các chức năng hệ thống phải cung cấp.
- Làm cơ sở để xây dựng Use Case Diagram, Use Case Specification (FT8-8, FT8-10), Business Rules (FT8-11) và thiết kế hệ thống ở các giai đoạn tiếp theo.
- Cung cấp nguồn tham chiếu duy nhất (single source of truth) cho việc lập kế hoạch, phát triển và kiểm thử.

### 4.1.2 Phạm vi

Tài liệu bao phủ 9 nhóm chức năng (modules) của hệ thống:

| STT | Module | Ký hiệu |
|-----|--------|---------|
| 1 | User & Security | `FR-US-*` |
| 2 | Family & Genealogy Management | `FR-FG-*` |
| 3 | Community | `FR-COM-*` |
| 4 | Events | `FR-EVT-*` |
| 5 | Family Directory | `FR-DIR-*` |
| 6 | Family Heritage | `FR-HER-*` |
| 7 | AI-assisted Services | `FR-AI-*` |
| 8 | Dashboard & Reporting | `FR-DASH-*` |
| 9 | Administration | `FR-ADM-*` |

Tổng cộng: **49 yêu cầu chức năng**. Không có chức năng nào ngoài phạm vi đề tài được bổ sung.

### 4.1.3 Đối tượng đọc

- BA/SA: kiểm chứng tính đầy đủ và nhất quán của yêu cầu.
- Kiến trúc sư / Developer: thiết kế và triển khai hệ thống.
- Tester: xây dựng test case dựa trên luồng chính và luồng thay thế.
- Giảng viên / Hội đồng chấm: đánh giá mức độ hoàn thiện của giai đoạn phân tích.

### 4.1.4 Thuật ngữ viết tắt

| Thuật ngữ | Ý nghĩa |
|-----------|---------|
| FR | Functional Requirement |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token |
| RSVP | Répondez S'il Vous Plaît, xác nhận tham dự |
| AI | Artificial Intelligence |
| LLM | Large Language Model |
| Owner | Trưởng gia tộc (Family Owner) |
| Member | Thành viên gia đình (Family Member) |
| Admin | Quản trị viên hệ thống (Administrator) |

### 4.1.5 Tài liệu tham chiếu

- Đề tài: *FamilyConnect: AI-powered Digital Family Community Platform* (bản đề cương được giao).
- Jira Epic: [FT8-4 Phân tích yêu cầu hệ thống](https://familyconnect.atlassian.net/browse/FT8-4) (Sprint 1).
- Jira tasks thuộc epic FT8-4 (nguồn yêu cầu và các tài liệu liên quan):

| Mã | Nội dung | Trạng thái |
|----|----------|------------|
| [FT8-2](https://familyconnect.atlassian.net/browse/FT8-2) | Phân tích yêu cầu và lập kế hoạch yêu cầu | In Progress |
| [FT8-3](https://familyconnect.atlassian.net/browse/FT8-3) | Phân tích Stakeholder | Done |
| [FT8-5](https://familyconnect.atlassian.net/browse/FT8-5) | Xây dựng Vision & Scope | In Progress |
| [FT8-6](https://familyconnect.atlassian.net/browse/FT8-6) | Phân tích yêu cầu chức năng (tài liệu này) | In Review |
| [FT8-7](https://familyconnect.atlassian.net/browse/FT8-7) | Phân tích yêu cầu phi chức năng | In Progress |
| [FT8-8](https://familyconnect.atlassian.net/browse/FT8-8) | Xây dựng Use Case Diagram (nguồn traceability) | To Do |
| [FT8-10](https://familyconnect.atlassian.net/browse/FT8-10) | Đặc tả Use Case (nguồn traceability) | To Do |
| [FT8-11](https://familyconnect.atlassian.net/browse/FT8-11) | Phân tích Business Rules | To Do |
| [FT8-12](https://familyconnect.atlassian.net/browse/FT8-12) | Xây dựng Glossary & Data Dictionary | To Do |
| [FT8-13](https://familyconnect.atlassian.net/browse/FT8-13) | Mô hình hóa quy trình nghiệp vụ (BPM) | To Do |

- Tài liệu SRS cùng thư mục (song song, sẽ bổ sung khi hoàn tất):
  - [01_GioiThieu.md](./01_GioiThieu.md) (FT8-2).
  - [02_StakeholderAnalysis.md](./02_StakeholderAnalysis.md) (FT8-3).
  - [03_VisionAndScope.md](./03_VisionAndScope.md) (FT8-5).
- IEEE 29148:2018, *Systems and software engineering, Life cycle processes, Requirements engineering*.
- Wiegers, K. & Beatty, J., *Software Requirements*, 3rd Edition.

---

## 4.2 Tổng quan yêu cầu chức năng

### 4.2.1 Actor chính của hệ thống

| Actor | Mô tả |
|-------|-------|
| **Guest** | Người chưa đăng ký/đăng nhập. Chỉ xem thông tin giới thiệu và đăng ký tài khoản. |
| **Family Member** | Thành viên đã được xác thực, thuộc ít nhất một gia đình. Người dùng chính của hệ thống. |
| **Family Owner** | Trưởng gia tộc, quản lý gia đình và các nhánh; phê duyệt thành viên; có quyền cao nhất trong phạm vi gia đình. |
| **Administrator** | Quản trị viên hệ thống, quản lý toàn bộ nền tảng (người dùng, nội dung, cấu hình, sao lưu). |
| **AI Service** | Dịch vụ trí tuệ nhân tạo nội bộ: tìm kiếm ngữ nghĩa, trợ lý tri thức, tóm tắt, gợi ý. |
| **Notification Service** | Dịch vụ gửi thông báo (in-app, email, push) hỗ trợ luồng xử lý bất đồng bộ. |

### 4.2.2 Phân bố yêu cầu theo module

| Module | Số lượng FR | Ưu tiên High | Ưu tiên Medium | Ưu tiên Low |
|--------|:-----------:|:------------:|:--------------:|:-----------:|
| 1. User & Security | 7 | 4 | 3 | 0 |
| 2. Family & Genealogy Management | 8 | 6 | 2 | 0 |
| 3. Community | 5 | 2 | 3 | 0 |
| 4. Events | 5 | 2 | 3 | 0 |
| 5. Family Directory | 4 | 1 | 2 | 1 |
| 6. Family Heritage | 5 | 1 | 3 | 1 |
| 7. AI-assisted Services | 5 | 2 | 2 | 1 |
| 8. Dashboard & Reporting | 5 | 1 | 3 | 1 |
| 9. Administration | 5 | 3 | 2 | 0 |
| **Tổng** | **49** | **22** | **23** | **4** |

### 4.2.3 Quy ước phân loại ưu tiên

| Mức ưu tiên | Ý nghĩa |
|-------------|---------|
| **High** | Chức năng lõi (core), không thể phát hành MVP nếu thiếu. |
| **Medium** | Chức năng quan trọng, triển khai sau nhóm High trong cùng giai đoạn. |
| **Low** | Chức năng tăng cường (nice-to-have), có thể trì hoãn sang phiên bản sau. |

---

## 4.3 Danh mục yêu cầu chức năng (Functional Requirement Catalog)

| ID | Tên yêu cầu | Module | Actor chính | Ưu tiên |
|----|-------------|--------|-------------|:-------:|
| FR-US-01 | Đăng ký tài khoản | User & Security | Guest | High |
| FR-US-02 | Đăng nhập | User & Security | Guest | High |
| FR-US-03 | Đăng xuất | User & Security | Family Member | Medium |
| FR-US-04 | Khôi phục mật khẩu | User & Security | Guest | Medium |
| FR-US-05 | Phân quyền truy cập theo vai trò (RBAC) | User & Security | Administrator | High |
| FR-US-06 | Quản lý hồ sơ cá nhân | User & Security | Family Member | Medium |
| FR-US-07 | Xác thực thành viên gia đình | User & Security | Family Owner | High |
| FR-FG-01 | Quản lý gia đình | Family & Genealogy | Family Owner | High |
| FR-FG-02 | Quản lý nhánh gia đình | Family & Genealogy | Family Owner | High |
| FR-FG-03 | Quản lý thành viên gia đình | Family & Genealogy | Family Owner | High |
| FR-FG-04 | Quản lý quan hệ cha mẹ – con | Family & Genealogy | Family Owner | High |
| FR-FG-05 | Quản lý hôn nhân | Family & Genealogy | Family Owner | Medium |
| FR-FG-06 | Xem cây gia phả tương tác | Family & Genealogy | Family Member | High |
| FR-FG-07 | Trực quan hóa quan hệ | Family & Genealogy | Family Member | Medium |
| FR-FG-08 | Tra cứu quan hệ | Family & Genealogy | Family Member | High |
| FR-COM-01 | Đăng và quản lý bài viết | Community | Family Member | High |
| FR-COM-02 | Bình luận và thả cảm xúc | Community | Family Member | Medium |
| FR-COM-03 | Chia sẻ tin tức gia đình | Community | Family Member | Medium |
| FR-COM-04 | Chia sẻ hình ảnh | Community | Family Member | Medium |
| FR-COM-05 | Thông báo gia đình | Community | Family Owner | High |
| FR-EVT-01 | Tạo sự kiện gia đình | Events | Family Member | High |
| FR-EVT-02 | Xác nhận tham dự (RSVP) | Events | Family Member | Medium |
| FR-EVT-03 | Quản lý người tham gia | Events | Family Owner | Medium |
| FR-EVT-04 | Thư viện ảnh sự kiện | Events | Family Member | Medium |
| FR-EVT-05 | Nhắc nhở sự kiện | Events | Family Member | High |
| FR-DIR-01 | Danh bạ thành viên | Family Directory | Family Member | Medium |
| FR-DIR-02 | Hồ sơ nghề nghiệp | Family Directory | Family Member | Low |
| FR-DIR-03 | Hồ sơ học vấn | Family Directory | Family Member | Low |
| FR-DIR-04 | Tìm kiếm theo nghề nghiệp, địa điểm, thế hệ | Family Directory | Family Member | High |
| FR-HER-01 | Quản lý tư liệu lịch sử | Family Heritage | Family Owner | Medium |
| FR-HER-02 | Quản lý câu chuyện gia đình | Family Heritage | Family Member | Medium |
| FR-HER-03 | Quản lý thành viên tiêu biểu | Family Heritage | Family Owner | Low |
| FR-HER-04 | Thư viện ảnh gia đình | Family Heritage | Family Member | Medium |
| FR-HER-05 | Kho lưu trữ số | Family Heritage | Family Owner | High |
| FR-AI-01 | Tìm kiếm ngữ nghĩa bằng AI | AI-assisted Services | Family Member | High |
| FR-AI-02 | Trợ lý tri thức gia đình (AI Assistant) | AI-assisted Services | Family Member | High |
| FR-AI-03 | Giải thích quan hệ gia đình | AI-assisted Services | Family Member | Medium |
| FR-AI-04 | Tóm tắt nội dung bằng AI | AI-assisted Services | Family Member | Medium |
| FR-AI-05 | Gợi ý thành viên và tài nguyên gia đình | AI-assisted Services | Family Member | Low |
| FR-DASH-01 | Thống kê gia đình | Dashboard & Reporting | Family Owner | Medium |
| FR-DASH-02 | Bảng điều khiển hoạt động cộng đồng | Dashboard & Reporting | Family Member | Medium |
| FR-DASH-03 | Thống kê sự kiện | Dashboard & Reporting | Family Owner | Low |
| FR-DASH-04 | Thống kê nhân khẩu | Dashboard & Reporting | Family Owner | Medium |
| FR-DASH-05 | Tạo và xuất báo cáo | Dashboard & Reporting | Family Owner | High |
| FR-ADM-01 | Quản lý người dùng | Administration | Administrator | High |
| FR-ADM-02 | Kiểm duyệt nội dung | Administration | Administrator | High |
| FR-ADM-03 | Nhật ký kiểm toán (Audit Log) | Administration | Administrator | High |
| FR-ADM-04 | Sao lưu và phục hồi | Administration | Administrator | Medium |
| FR-ADM-05 | Cấu hình hệ thống | Administration | Administrator | Medium |

---

## 4.4 Đặc tả yêu cầu chức năng

### 4.4.1 Module 1, User & Security

**Tên module:** User & Security

**Mục đích:** Quản lý vòng đời tài khoản người dùng, xác thực an toàn (JWT), phân quyền truy cập theo vai trò và đảm bảo mỗi tài khoản tham gia gia đình được xác thực bởi người có thẩm quyền. Đây là nền tảng bảo mật cho toàn bộ các module còn lại.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Đăng ký tài khoản | Guest tạo tài khoản bằng email/số điện thoại, kích hoạt qua xác nhận. |
| Đăng nhập / Đăng xuất | Xác thực danh tính, cấp JWT, quản lý phiên làm việc. |
| Khôi phục mật khẩu | Gửi mã/link đặt lại mật khẩu qua email khi người dùng quên. |
| Phân quyền RBAC | Gán vai trò (Guest, Member, Owner, Admin) và kiểm soát quyền truy cập. |
| Quản lý hồ sơ cá nhân | Cập nhật thông tin cá nhân, ảnh đại diện, cài đặt riêng tư. |
| Xác thực thành viên | Owner phê duyệt/từ chối yêu cầu tham gia gia đình. |

---

#### FR-US-01 Đăng ký tài khoản

**Description**

Hệ thống cho phép Guest tạo tài khoản FamilyConnect bằng email và mật khẩu. Tài khoản sau khi tạo ở trạng thái chưa kích hoạt; người dùng phải xác nhận địa chỉ email để kích hoạt trước khi có thể đăng nhập và sử dụng các chức năng của hệ thống. Quá trình đăng ký chỉ thu thập thông tin tối thiểu (họ tên, email, mật khẩu); các thông tin chi tiết khác được bổ sung ở bước quản lý hồ sơ cá nhân (FR-US-06).

**Primary Actor**

Guest

**Supporting Actors**

- Notification Service (gửi email xác nhận)

**Preconditions**

1. Guest chưa có tài khoản trên hệ thống.
2. Guest có địa chỉ email hợp lệ và đang hoạt động.

**Trigger**

Guest truy cập trang đăng ký và gửi biểu mẫu đăng ký tài khoản.

**Main Flow**

1. Guest mở trang đăng ký tài khoản.
2. Guest nhập họ tên, địa chỉ email và mật khẩu (tối thiểu 8 ký tự, có chữ và số).
3. Guest xác nhận mật khẩu lần hai và đồng ý với điều khoản sử dụng.
4. Hệ thống kiểm tra tính hợp lệ của biểu mẫu và tính duy nhất của email.
5. Hệ thống tạo tài khoản mới với trạng thái *Pending Activation* và vai trò mặc định *Guest*.
6. Hệ thống gửi email chứa đường dẫn kích hoạt đến địa chỉ email đã đăng ký.
7. Guest mở đường dẫn kích hoạt trong email; hệ thống chuyển trạng thái tài khoản thành *Active*.
8. Hệ thống hiển thị thông báo đăng ký thành công và chuyển hướng Guest đến trang đăng nhập.

**Alternate Flow**

- **A1, Email đã tồn tại:** Tại bước 4, nếu email đã được đăng ký, hệ thống báo lỗi "Email đã được sử dụng" và yêu cầu Guest nhập email khác hoặc chuyển đến trang đăng nhập.
- **A2, Dữ liệu không hợp lệ:** Tại bước 4, nếu mật khẩu không đủ mạnh hoặc biểu mẫu thiếu trường bắt buộc, hệ thống hiển thị thông báo lỗi tương ứng bên cạnh từng trường; Guest sửa lại và gửi lại.
- **A3, Đường dẫn kích hoạt hết hạn hoặc không hợp lệ:** Tại bước 7, nếu đường dẫn hết hạn (sau 24 giờ) hoặc sai token, hệ thống hiển thị thông báo lỗi và cho phép Guest yêu cầu gửi lại email kích hoạt.
- **A4, Email kích hoạt không đến:** Guest yêu cầu hệ thống gửi lại email kích hoạt; hệ thống tạo token mới và gửi lại.

**Postconditions**

1. Tài khoản mới tồn tại trong hệ thống với trạng thái *Active*.
2. Guest có thể đăng nhập bằng email và mật khẩu vừa tạo.

**Expected Result**

Guest tạo thành công tài khoản đã kích hoạt và đăng nhập được vào hệ thống. Không thể tạo hai tài khoản trên cùng một email.

**Priority**

High

---

#### FR-US-02 Đăng nhập

**Description**

Hệ thống xác thực danh tính người dùng bằng email và mật khẩu. Khi xác thực thành công, hệ thống cấp access token (JWT) và refresh token để duy trì phiên làm việc. Người dùng chưa kích hoạt tài khoản hoặc bị khóa sẽ không được phép đăng nhập.

**Primary Actor**

Guest (đã có tài khoản)

**Supporting Actors**

Không có.

**Preconditions**

1. Tài khoản đã được tạo và kích hoạt (FR-US-01).
2. Tài khoản không bị khóa bởi Administrator (FR-ADM-01).

**Trigger**

Guest mở trang đăng nhập và gửi thông tin đăng nhập.

**Main Flow**

1. Guest mở trang đăng nhập.
2. Guest nhập email và mật khẩu.
3. Hệ thống kiểm tra tính hợp lệ của thông tin đăng nhập.
4. Hệ thống kiểm tra trạng thái tài khoản: *Active*, chưa khóa.
5. Hệ thống xác thực mật khẩu (băm) và cấp access token (JWT) kèm thời hạn hiệu lực cùng refresh token.
6. Hệ thống ghi lại thời điểm đăng nhập và chuyển hướng người dùng đến trang chủ theo vai trò.

**Alternate Flow**

- **A1, Sai mật khẩu:** Hệ thống báo lỗi "Email hoặc mật khẩu không đúng" (không tiết lộ trường nào sai) và tăng bộ đếm thất bại; sau 5 lần thất bại liên tiếp, tài khoản tạm khóa 15 phút.
- **A2, Tài khoản chưa kích hoạt:** Hệ thống hiển thị thông báo yêu cầu kích hoạt tài khoản và cho phép gửi lại email kích hoạt.
- **A3, Tài khoản bị khóa:** Hệ thống hiển thị thông báo tài khoản bị khóa và hướng dẫn liên hệ Administrator.
- **A4, Access token hết hạn trong phiên:** Hệ thống dùng refresh token để cấp lại access token; nếu refresh token hết hạn, yêu cầu người dùng đăng nhập lại.

**Postconditions**

1. Người dùng có phiên đăng nhập hợp lệ (access token + refresh token).
2. Giao diện hiển thị theo vai trò của người dùng (RBAC, FR-US-05).

**Expected Result**

Người dùng xác thực đúng thông tin sẽ vào được hệ thống trong vòng không quá 3 giây (điều kiện mạng bình thường); thông tin sai bị từ chối với thông báo an toàn, không rò rỉ thông tin tài khoản.

**Priority**

High

---

#### FR-US-03 Đăng xuất

**Description**

Hệ thống cho phép người dùng kết thúc phiên làm việc một cách an toàn: thu hồi refresh token, vô hiệu hóa access token hiện tại và xóa trạng thái phiên trên thiết bị.

**Primary Actor**

Family Member (áp dụng cho mọi vai trò đã đăng nhập)

**Supporting Actors**

Không có.

**Preconditions**

1. Người dùng đã đăng nhập thành công (FR-US-02).

**Trigger**

Người dùng nhấn nút "Đăng xuất" trên giao diện.

**Main Flow**

1. Người dùng mở menu tài khoản và chọn "Đăng xuất".
2. Hệ thống thu hồi refresh token và vô hiệu hóa phiên hiện tại.
3. Hệ thống xóa token lưu trữ trên thiết bị.
4. Hệ thống chuyển hướng người dùng về trang đăng nhập.

**Alternate Flow**

- **A1, Token đã hết hạn:** Hệ thống vẫn xóa token cục bộ và chuyển về trang đăng nhập mà không báo lỗi.
- **A2, Phiên bị thu hồi từ xa:** Nếu Administrator đã khóa tài khoản (FR-ADM-01), yêu cầu đăng xuất được xem là thành công.

**Postconditions**

1. Không có phiên hoạt động nào còn hiệu lực trên thiết bị.
2. Người dùng phải đăng nhập lại để sử dụng hệ thống.

**Expected Result**

Người dùng đăng xuất ngay lập tức, phiên không thể tái sử dụng từ thiết bị đó.

**Priority**

Medium

---

#### FR-US-04 Khôi phục mật khẩu

**Description**

Khi người dùng quên mật khẩu, hệ thống cho phép đặt lại mật khẩu thông qua email. Hệ thống tạo mã đặt lại dùng một lần (token) với thời hạn hiệu lực ngắn, đảm bảo quy trình khôi phục an toàn.

**Primary Actor**

Guest (đã có tài khoản)

**Supporting Actors**

- Notification Service (gửi email đặt lại mật khẩu)

**Preconditions**

1. Guest có tài khoản đã kích hoạt trên hệ thống.
2. Guest quên mật khẩu hiện tại.

**Trigger**

Guest nhấn liên kết "Quên mật khẩu?" trên trang đăng nhập.

**Main Flow**

1. Guest nhấn "Quên mật khẩu?" và nhập địa chỉ email đã đăng ký.
2. Hệ thống kiểm tra sự tồn tại của email (không tiết lộ cho người dùng nếu email không tồn tại).
3. Hệ thống tạo token đặt lại mật khẩu (hiệu lực 30 phút, dùng một lần) và gửi email hướng dẫn.
4. Guest mở liên kết trong email và nhập mật khẩu mới (tuân thủ chính sách độ mạnh).
5. Hệ thống kiểm tra token còn hiệu lực, cập nhật mật khẩu mới và vô hiệu hóa token.
6. Hệ thống thông báo thành công và cho phép Guest đăng nhập với mật khẩu mới.

**Alternate Flow**

- **A1, Email không tồn tại:** Hệ thống vẫn hiển thị thông báo chung "Nếu email tồn tại, bạn sẽ nhận được hướng dẫn" để tránh lộ thông tin tài khoản.
- **A2, Token hết hạn hoặc đã sử dụng:** Hệ thống báo lỗi và cho phép Guest gửi lại yêu cầu đặt lại.
- **A3, Mật khẩu mới yếu:** Hệ thống yêu cầu nhập lại theo chính sách (≥ 8 ký tự, có chữ và số).

**Postconditions**

1. Mật khẩu mới có hiệu lực.
2. Mọi phiên đăng nhập cũ của tài khoản bị thu hồi.

**Expected Result**

Guest lấy lại được quyền truy cập tài khoản mà không làm lộ thông tin cho bên thứ ba.

**Priority**

Medium

---

#### FR-US-05 Phân quyền truy cập theo vai trò (RBAC)

**Description**

Hệ thống áp dụng mô hình kiểm soát truy cập dựa trên vai trò (RBAC). Mỗi người dùng có một hoặc nhiều vai trò; mỗi vai trò được gán tập quyền tương ứng với từng module và từng tài nguyên (family, post, event, ...). Mọi yêu cầu truy cập API đều được xác thực quyền trước khi xử lý. Thứ bậc quyền: **Guest < Family Member < Family Owner < Administrator** (quyền cao hơn bao gồm quyền thấp hơn trong phạm vi tài nguyên gia đình; Administrator có quyền toàn cục).

**Primary Actor**

Administrator (gán vai trò), mọi người dùng chịu sự ràng buộc của RBAC

**Supporting Actors**

- Family Owner (gán vai trò trong phạm vi gia đình của mình)

**Preconditions**

1. Người dùng đã đăng nhập (FR-US-02).
2. Chính sách quyền của hệ thống đã được cấu hình (mặc định theo thiết kế).

**Trigger**

Người dùng thực hiện một thao tác bất kỳ trên hệ thống; hoặc Administrator/Owner gán/điều chỉnh vai trò cho tài khoản.

**Main Flow**

1. Người dùng gửi yêu cầu truy cập một chức năng hoặc tài nguyên.
2. Hệ thống trích xuất danh tính từ access token (JWT).
3. Hệ thống tải vai trò và quyền của người dùng trong ngữ cảnh tài nguyên (ví dụ: family cụ thể).
4. Hệ thống so khớp quyền yêu cầu với quyền được gán.
5. Nếu đủ quyền, yêu cầu được chuyển tiếp cho module xử lý; nếu không đủ, trả về mã lỗi 403 với thông báo từ chối truy cập.

**Alternate Flow**

- **A1, Vai trò bị thay đổi giữa phiên:** Hệ thống đọc lại quyền từ database cho các thao tác nhạy cảm; nếu quyền đã bị thu hồi, yêu cầu bị từ chối ngay.
- **A2, Token không hợp lệ/hết hạn:** Trả về mã lỗi 401, yêu cầu đăng nhập lại.
- **A3, Người dùng không thuộc gia đình:** Các thao tác trong phạm vi gia đình bị từ chối với lỗi "Không có quyền truy cập gia đình này".

**Postconditions**

1. Mọi thao tác nhạy cảm đều được kiểm tra quyền trước khi thực thi.
2. Việc thay đổi vai trò được ghi vào nhật ký kiểm toán (FR-ADM-03).

**Expected Result**

Không có người dùng nào truy cập được chức năng ngoài quyền được gán; danh sách quyền theo vai trò được tài liệu hóa và kiểm thử đầy đủ.

**Priority**

High

---

#### FR-US-06 Quản lý hồ sơ cá nhân

**Description**

Hệ thống cho phép người dùng xem và cập nhật hồ sơ cá nhân của mình: họ tên, ảnh đại diện, số điện thoại, địa chỉ, ngày sinh, thông tin giới thiệu ngắn. Người dùng kiểm soát mức độ hiển thị thông tin cá nhân với các thành viên khác (công khai trong gia đình / chỉ riêng tư).

**Primary Actor**

Family Member

**Supporting Actors**

Không có.

**Preconditions**

1. Người dùng đã đăng nhập (FR-US-02).

**Trigger**

Người dùng mở trang hồ sơ cá nhân và chỉnh sửa thông tin.

**Main Flow**

1. Người dùng mở trang hồ sơ cá nhân.
2. Hệ thống hiển thị thông tin hiện tại của người dùng.
3. Người dùng cập nhật các trường cho phép (họ tên, ảnh đại diện, SĐT, ngày sinh, giới thiệu, cài đặt riêng tư).
4. Hệ thống kiểm tra tính hợp lệ của dữ liệu (định dạng SĐT, ngày sinh không trong tương lai, kích thước ảnh ≤ 5MB).
5. Hệ thống lưu thay đổi và hiển thị thông báo cập nhật thành công.

**Alternate Flow**

- **A1, Dữ liệu không hợp lệ:** Hệ thống báo lỗi theo từng trường, giữ nguyên các giá trị khác, người dùng sửa lại và gửi lại.
- **A2, Email không được phép sửa:** Email là định danh đăng nhập, không thay đổi được tại màn hình này (thay đổi thuộc quyền Administrator, FR-ADM-01).

**Postconditions**

1. Thông tin hồ sơ được cập nhật trong cơ sở dữ liệu.
2. Các thành viên khác thấy thông tin theo đúng cài đặt riêng tư.

**Expected Result**

Hồ sơ cá nhân luôn phản ánh thông tin mới nhất do người dùng cung cấp; dữ liệu sai định dạng bị chặn.

**Priority**

Medium

---

#### FR-US-07 Xác thực thành viên gia đình

**Description**

Để đảm bảo chỉ người thân thực sự mới được tham gia gia đình trên nền tảng, Family Owner (trưởng gia tộc) có quyền xem xét và phê duyệt/từ chối mọi yêu cầu tham gia gia đình. Thành viên chỉ nhận đầy đủ quyền truy cập dữ liệu gia đình sau khi được phê duyệt. Quy trình này cũng áp dụng khi Family Owner thêm trực tiếp một thành viên mới vào gia đình (FR-FG-03).

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (người gửi yêu cầu tham gia)
- Notification Service (thông báo kết quả xác thực)

**Preconditions**

1. Family Owner đã đăng nhập và đang quản lý gia đình (FR-FG-01).
2. Có ít nhất một yêu cầu tham gia đang chờ xử lý.

**Trigger**

Family Owner nhận thông báo về yêu cầu tham gia mới và mở trang xác thực thành viên.

**Main Flow**

1. Người dùng (chưa thuộc gia đình) gửi yêu cầu tham gia gia đình kèm lời nhắn giới thiệu.
2. Hệ thống lưu yêu cầu ở trạng thái *Pending* và thông báo cho Family Owner.
3. Family Owner mở danh sách yêu cầu chờ xử lý và xem thông tin người yêu cầu (họ tên, mối quan hệ khai báo, lời nhắn).
4. Family Owner phê duyệt hoặc từ chối yêu cầu, kèm lý do (nếu từ chối).
5. Hệ thống cập nhật trạng thái yêu cầu và gán vai trò *Family Member* cho người được phê duyệt trong gia đình đó.
6. Hệ thống thông báo kết quả cho người yêu cầu.

**Alternate Flow**

- **A1, Từ chối yêu cầu:** Hệ thống lưu lý do từ chối; người yêu cầu nhận thông báo và có thể gửi lại yêu cầu mới sau 24 giờ.
- **A2, Yêu cầu trùng:** Nếu người yêu cầu đã là thành viên của gia đình, hệ thống chặn gửi yêu cầu trùng lặp.
- **A3, Hết thời gian chờ:** Yêu cầu *Pending* quá 14 ngày được tự động đóng; người yêu cầu phải gửi lại.

**Postconditions**

1. Người được phê duyệt trở thành Family Member của gia đình với quyền tương ứng.
2. Lịch sử phê duyệt được ghi nhận cho mục đích kiểm toán (FR-ADM-03).

**Expected Result**

Chỉ những cá nhân được Family Owner phê duyệt mới truy cập được dữ liệu của gia đình.

**Priority**

High

---

### 4.4.2 Module 2, Family & Genealogy Management

**Tên module:** Family & Genealogy Management

**Mục đích:** Quản lý cấu trúc dữ liệu lõi của nền tảng, gia đình, nhánh, thành viên và các mối quan hệ huyết thống/hôn nhân. Dữ liệu được tổ chức dưới dạng đồ thị gia đình (family graph), làm nền tảng cho cây gia phả tương tác, tra cứu quan hệ và các dịch vụ AI.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Quản lý gia đình | Tạo gia đình, cập nhật thông tin, chỉ định Family Owner. |
| Quản lý nhánh | Tạo/quản lý nhánh (branch) trong gia đình. |
| Quản lý thành viên | Thêm/sửa/xóa hồ sơ thành viên trong gia đình. |
| Quan hệ cha mẹ – con | Thiết lập và quản lý quan hệ huyết thống. |
| Quản lý hôn nhân | Thiết lập và quản lý quan hệ vợ chồng. |
| Cây gia phả tương tác | Xem đồ thị gia đình trực quan, điều hướng qua các thế hệ. |
| Trực quan hóa quan hệ | Hiển thị mối quan hệ giữa các thành viên bằng sơ đồ. |
| Tra cứu quan hệ | Truy vấn quan hệ giữa hai thành viên, kèm đường đi trên đồ thị. |

---

#### FR-FG-01 Quản lý gia đình

**Description**

Hệ thống cho phép tạo mới một gia đình với thông tin cơ bản (tên gia đình/họ, mô tả, khu vực, quốc gia) và chỉ định người sáng lập làm Family Owner đầu tiên. Family Owner có thể cập nhật thông tin gia đình và chuyển quyền Owner cho thành viên khác. Mỗi người dùng có thể thuộc nhiều gia đình, nhưng chỉ là Owner của các gia đình mà họ được giao.

**Primary Actor**

Family Owner (người sáng lập gia đình)

**Supporting Actors**

- Family Member (nhận quyền Owner khi được chuyển giao)

**Preconditions**

1. Người dùng đã đăng ký và kích hoạt tài khoản (FR-US-01, FR-US-02).
2. Người dùng chưa tạo quá 5 gia đình (giới hạn chống lạm dụng).

**Trigger**

Người dùng chọn "Tạo gia đình" trên giao diện và gửi biểu mẫu khởi tạo.

**Main Flow**

1. Người dùng chọn "Tạo gia đình".
2. Hệ thống hiển thị biểu mẫu gồm: tên gia đình, mô tả, khu vực, quốc gia.
3. Người dùng nhập thông tin và gửi.
4. Hệ thống kiểm tra tính hợp lệ (tên không trống, ≤ 100 ký tự).
5. Hệ thống tạo bản ghi gia đình với trạng thái *Active*, gán người tạo làm Family Owner.
6. Hệ thống tự động tạo thành viên đầu tiên gắn với tài khoản người tạo (nút gốc của cây gia phả).
7. Hệ thống chuyển hướng đến trang quản lý gia đình vừa tạo.

**Alternate Flow**

- **A1, Cập nhật thông tin gia đình:** Family Owner mở trang thông tin, sửa mô tả/khu vực và lưu; hệ thống ghi nhận thay đổi vào audit log.
- **A2, Chuyển quyền Owner:** Family Owner chọn thành viên kế nhiệm; hệ thống yêu cầu xác nhận, đổi vai trò và thông báo cho thành viên mới.
- **A3, Tên trùng trong hệ thống:** Cho phép trùng tên (không có ràng buộc toàn cục) nhưng cảnh báo nếu tên trùng với gia đình cùng khu vực.
- **A4, Giải tán gia đình:** Family Owner gửi yêu cầu giải tán; hệ thống chuyển gia đình sang trạng thái *Inactive* (dữ liệu không xóa) và thông báo toàn bộ thành viên.

**Postconditions**

1. Gia đình mới tồn tại với Family Owner được gán.
2. Thành viên đầu tiên (Owner) xuất hiện trên cây gia phả.

**Expected Result**

Family Owner quản trị được vòng đời gia đình: tạo, cập nhật, chuyển quyền, giải tán, mọi thay đổi được ghi nhật ký.

**Priority**

High

---

#### FR-FG-02 Quản lý nhánh gia đình

**Description**

Gia đình lớn thường được phân thành nhiều nhánh (branch) theo dòng dõi. Hệ thống cho phép Family Owner tạo nhánh, gán thành viên vào nhánh và quản lý thông tin của từng nhánh (tên nhánh, mô tả, trưởng nhánh). Nhánh giúp tổ chức cây gia phả rõ ràng và phục vụ lọc theo nhánh khi xem cây.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (trưởng nhánh được chỉ định)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình đã tồn tại và có trạng thái *Active* (FR-FG-01).

**Trigger**

Family Owner mở trang quản lý nhánh của gia đình và tạo nhánh mới.

**Main Flow**

1. Family Owner mở trang "Nhánh gia đình".
2. Hệ thống hiển thị danh sách nhánh hiện có kèm số thành viên từng nhánh.
3. Family Owner chọn "Thêm nhánh" và nhập tên nhánh, mô tả, trưởng nhánh.
4. Hệ thống kiểm tra tính hợp lệ (tên nhánh duy nhất trong gia đình).
5. Hệ thống tạo nhánh và gán trưởng nhánh.
6. Family Owner chọn danh sách thành viên để gán vào nhánh (tùy chọn).
7. Hệ thống lưu và cập nhật giao diện cây gia phả theo nhánh.

**Alternate Flow**

- **A1, Sửa/xóa nhánh:** Family Owner sửa tên, mô tả hoặc trưởng nhánh; khi xóa nhánh, các thành viên trở về trạng thái không thuộc nhánh (dữ liệu thành viên không bị xóa theo).
- **A2, Tên nhánh trùng:** Hệ thống báo lỗi và yêu cầu đặt tên khác.
- **A3, Gán thành viên đã thuộc nhánh khác:** Hệ thống cảnh báo và yêu cầu xác nhận chuyển nhánh.

**Postconditions**

1. Nhánh mới tồn tại trong gia đình; thành viên được gán chính xác.
2. Cây gia phả hiển thị theo nhánh khi được lọc.

**Expected Result**

Family Owner tổ chức được cấu trúc nhánh của gia đình; mỗi thành viên thuộc tối đa một nhánh.

**Priority**

High

---

#### FR-FG-03 Quản lý thành viên gia đình

**Description**

Hệ thống cho phép Family Owner quản lý hồ sơ thành viên trong gia đình: thêm thành viên mới (đã có tài khoản hoặc chưa có), cập nhật thông tin cá nhân trong ngữ cảnh gia đình (tên, ngày sinh, giới tính, ngày mất, ảnh, ghi chú), đình chỉ hoặc xóa thành viên khỏi gia đình. Việc xóa thành viên không xóa dữ liệu tài khoản của họ trên nền tảng.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (đối tượng quản lý)
- Notification Service (thông báo thêm/loại thành viên)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình đã tồn tại (FR-FG-01).

**Trigger**

Family Owner mở trang thành viên gia đình và thực hiện thao tác thêm/sửa/xóa.

**Main Flow**

1. Family Owner mở trang "Thành viên" của gia đình.
2. Hệ thống hiển thị danh sách thành viên kèm trạng thái (Active, Suspended).
3. Family Owner chọn "Thêm thành viên" và nhập thông tin (họ tên, ngày sinh, giới tính, email/SĐT nếu có tài khoản).
4. Hệ thống tìm kiếm tài khoản theo email/SĐT; nếu tồn tại, liên kết tài khoản với hồ sơ thành viên; nếu chưa, tạo hồ sơ thành viên "chưa liên kết".
5. Hệ thống lưu hồ sơ thành viên vào gia đình.
6. Nếu thành viên có tài khoản, hệ thống gửi thông báo "Bạn đã được thêm vào gia đình".

**Alternate Flow**

- **A1, Sửa hồ sơ thành viên:** Family Owner cập nhật thông tin (đặc biệt khi có thành viên mới sinh hoặc qua đời); thay đổi được ghi audit log.
- **A2, Đình chỉ thành viên:** Family Owner chọn đình chỉ; hệ thống chuyển trạng thái *Suspended*, thu hồi quyền truy cập dữ liệu gia đình, thông báo cho thành viên.
- **A3, Xóa thành viên khỏi gia đình:** Hệ thống yêu cầu xác nhận; nếu thành viên có quan hệ được tham chiếu trong cây gia phả, hệ thống cảnh báo dữ liệu quan hệ liên quan sẽ bị xóa theo.
- **A4, Thành viên trùng:** Nếu hồ sơ đã tồn tại trong gia đình (cùng tên + ngày sinh), hệ thống cảnh báo để tránh tạo trùng lặp.

**Postconditions**

1. Danh sách thành viên gia đình phản ánh đúng thay đổi.
2. Quyền truy cập của thành viên bị đình chỉ/xóa được thu hồi kịp thời.

**Expected Result**

Family Owner kiểm soát đầy đủ hồ sơ thành viên trong gia đình, đảm bảo dữ liệu gia phả chính xác và không trùng lặp.

**Priority**

High

---

#### FR-FG-04 Quản lý quan hệ cha mẹ – con

**Description**

Hệ thống cho phép Family Owner thiết lập quan hệ huyết thống cha – con giữa hai thành viên trong gia đình. Quan hệ này là cạnh cốt lõi của đồ thị gia đình, xác định thế hệ của mỗi thành viên và được dùng cho mọi chức năng dựa trên gia phả (cây tương tác, tra cứu quan hệ, AI). Một thành viên có thể có tối đa 2 cha/mẹ trong hệ thống; một thành viên có thể là cha/mẹ của nhiều con.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (đối tượng của quan hệ)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Hai thành viên liên quan đã tồn tại trong gia đình (FR-FG-03).
3. Không tồn tại quan hệ cha–con trùng giữa cùng cặp thành viên.

**Trigger**

Family Owner mở hồ sơ thành viên và chọn "Thiết lập quan hệ cha mẹ – con".

**Main Flow**

1. Family Owner mở hồ sơ thành viên (con).
2. Family Owner chọn "Thêm cha/mẹ".
3. Hệ thống hiển thị danh sách thành viên khả dụng (cùng gia đình, khác giới tính không bắt buộc).
4. Family Owner chọn thành viên cha/mẹ và xác nhận mối quan hệ.
5. Hệ thống kiểm tra ràng buộc: không tạo vòng lặp trên đồ thị (thành viên không thể là tổ tiên của chính mình), tối đa 2 cha/mẹ.
6. Hệ thống tạo cạnh quan hệ và cập nhật thế hệ của các thành viên liên quan.
7. Hệ thống hiển thị cây gia phả cập nhật.

**Alternate Flow**

- **A1, Vi phạm ràng buộc vòng lặp:** Hệ thống từ chối và giải thích rằng quan hệ sẽ tạo mâu thuẫn thế hệ.
- **A2, Đã đủ 2 cha/mẹ:** Hệ thống báo lỗi và đề nghị sửa quan hệ hiện có.
- **A3, Gỡ quan hệ:** Family Owner gỡ cạnh cha–con; hệ thống yêu cầu xác nhận và cập nhật lại thế hệ.
- **A4, Nhầm lẫn vai trò:** Hệ thống cho phép đổi hướng quan hệ (cha/mẹ ↔ con) bằng thao tác sửa.

**Postconditions**

1. Cạnh quan hệ cha–con tồn tại trên đồ thị gia đình.
2. Thế hệ của các thành viên được tính lại chính xác.

**Expected Result**

Cây gia phả phản ánh đúng quan hệ huyết thống; hệ thống chặn mọi quan hệ tạo vòng lặp hoặc vượt giới hạn cha/mẹ.

**Priority**

High

---

#### FR-FG-05 Quản lý hôn nhân

**Description**

Hệ thống cho phép Family Owner thiết lập quan hệ hôn nhân (vợ–chồng) giữa hai thành viên trưởng thành trong gia đình. Quan hệ hôn nhân được ghi nhận kèm ngày cưới (nếu biết) và trạng thái (đang kết hôn, ly hôn, góa). Quan hệ hôn nhân kết nối hai nhánh gia đình khác nhau khi thành viên ngoại hôn được thêm vào gia đình.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (đối tượng của quan hệ)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Hai thành viên liên quan đã tồn tại trong gia đình (FR-FG-03).
3. Không tồn tại quan hệ hôn nhân đang hoạt động của mỗi người với người khác.

**Trigger**

Family Owner mở hồ sơ thành viên và chọn "Thiết lập quan hệ hôn nhân".

**Main Flow**

1. Family Owner mở hồ sơ thành viên.
2. Family Owner chọn "Thêm vợ/chồng".
3. Hệ thống hiển thị danh sách thành viên khả dụng (độ tuổi trưởng thành theo cấu hình, cùng hoặc khác gia đình).
4. Family Owner chọn đối tượng, nhập ngày cưới (tùy chọn) và xác nhận.
5. Hệ thống kiểm tra ràng buộc (mỗi người tối đa một quan hệ hôn nhân đang hoạt động).
6. Hệ thống tạo cạnh hôn nhân trên đồ thị.
7. Hệ thống hiển thị cây gia phả cập nhật với liên kết giữa hai thành viên.

**Alternate Flow**

- **A1, Đã có hôn nhân đang hoạt động:** Hệ thống chặn và yêu cầu kết thúc quan hệ hiện tại (ly hôn/góa) trước.
- **A2, Kết thúc hôn nhân:** Family Owner cập nhật trạng thái thành *Divorced* (kèm ngày) hoặc *Widowed*; cạnh quan hệ được đánh dấu lịch sử, không xóa khỏi đồ thị.
- **A3, Thành viên ngoài gia đình:** Nếu đối tượng chưa có hồ sơ, hệ thống dẫn qua luồng thêm thành viên (FR-FG-03) rồi quay lại thiết lập hôn nhân.

**Postconditions**

1. Cạnh hôn nhân tồn tại trên đồ thị với trạng thái chính xác.
2. Lịch sử hôn nhân được lưu giữ (không xóa dữ liệu).

**Expected Result**

Quan hệ hôn nhân được ghi nhận đầy đủ và chính xác; mỗi thành viên chỉ có một hôn nhân đang hoạt động tại một thời điểm.

**Priority**

Medium

---

#### FR-FG-06 Xem cây gia phả tương tác

**Description**

Hệ thống hiển thị toàn bộ gia đình dưới dạng cây gia phả trực quan (đồ thị tương tác). Family Member có thể phóng to/thu nhỏ, kéo để di chuyển, mở rộng/thu gọn nhánh, chọn thành viên để xem chi tiết và điều hướng qua các thế hệ. Cây hiển thị rõ ràng trên cả Web và Mobile, tối ưu cho cây gia đình lớn (hàng trăm thành viên).

**Primary Actor**

Family Member

**Supporting Actors**

Không có.

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình đang xem (đã được xác thực, FR-US-07).

**Trigger**

Family Member mở trang "Gia phả" của gia đình.

**Main Flow**

1. Family Member chọn gia đình từ danh sách các gia đình đang tham gia.
2. Hệ thống tải dữ liệu đồ thị gia đình (thành viên + quan hệ) từ server.
3. Hệ thống vẽ cây gia phả theo thế hệ, xếp các thành viên cùng thế hệ trên cùng một hàng.
4. Family Member tương tác: phóng to, thu nhỏ, kéo, mở rộng nhánh.
5. Family Member chọn một thành viên; hệ thống hiển thị hộp thông tin tóm tắt (tên, ngày sinh, thế hệ, nhánh) và các thao tác (xem hồ sơ, xem quan hệ).
6. Family Member chọn "Xem chi tiết" để mở hồ sơ thành viên đầy đủ.

**Alternate Flow**

- **A1, Cây quá lớn:** Hệ thống tải dữ liệu theo cụm (lazy loading), chỉ tải nhánh đang hiển thị; hiển thị trạng thái đang tải khi mở rộng nhánh mới.
- **A2, Lọc theo nhánh:** Family Member lọc cây theo nhánh gia đình (FR-FG-02) hoặc theo thế hệ; hệ thống chỉ hiển thị các thành viên khớp bộ lọc.
- **A3, Không có dữ liệu:** Gia đình mới chưa có thành viên ngoài Owner, hệ thống hiển thị cây tối thiểu và gợi ý thêm thành viên.
- **A4, Lỗi tải dữ liệu:** Hệ thống hiển thị thông báo lỗi kèm nút "Thử lại".

**Postconditions**

1. Cây gia phả hiển thị đúng cấu trúc và dữ liệu mới nhất.
2. Mọi tương tác đều mượt mà (không giật lag) trên thiết bị phổ thông.

**Expected Result**

Family Member duyệt được toàn bộ gia phả một cách trực quan, xem thông tin bất kỳ thành viên nào chỉ với vài thao tác.

**Priority**

High

---

#### FR-FG-07 Trực quan hóa quan hệ

**Description**

Ngoài cây gia phả theo thế hệ, hệ thống cung cấp chế độ xem đồ thị quan hệ (relationship graph): các nút là thành viên, các cạnh thể hiện loại quan hệ (cha–con, hôn nhân, cùng nhánh) với màu sắc/đường nét phân biệt. Chế độ này giúp người dùng nắm được mạng lưới quan hệ phức tạp của gia đình, đặc biệt với các gia đình có nhiều mối quan hệ chồng chéo.

**Primary Actor**

Family Member

**Supporting Actors**

Không có.

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Cây gia phả của gia đình có dữ liệu (FR-FG-06).

**Trigger**

Family Member chuyển chế độ xem từ "Cây thế hệ" sang "Đồ thị quan hệ".

**Main Flow**

1. Family Member mở trang gia phả và chọn chế độ "Đồ thị quan hệ".
2. Hệ thống tải dữ liệu đồ thị và vẽ các nút thành viên, cạnh quan hệ với chú giải loại cạnh.
3. Family Member chọn một thành viên; hệ thống làm nổi bật các quan hệ trực tiếp của thành viên đó.
4. Family Member chọn loại quan hệ muốn lọc (ví dụ: chỉ xem hôn nhân); hệ thống thu gọn các cạnh không thuộc loại đã chọn.
5. Family Member kéo nút để sắp xếp lại bố cục theo ý muốn; hệ thống ghi nhận bố cục tùy chỉnh cho phiên làm việc.

**Alternate Flow**

- **A1, Đồ thị quá dày:** Hệ thống tự động ẩn các cạnh gián tiếp khi số lượng cạnh vượt ngưỡng hiển thị, chỉ giữ quan hệ trực tiếp.
- **A2, Chưa có quan hệ:** Hiển thị thông báo hướng dẫn Family Owner thiết lập quan hệ (FR-FG-04, FR-FG-05).

**Postconditions**

1. Người dùng có cái nhìn trực quan về mạng lưới quan hệ gia đình.
2. Các loại quan hệ được phân biệt rõ ràng.

**Expected Result**

Family Member hiểu được mối quan hệ giữa các thành viên ở mức trực quan, hỗ trợ các tác vụ tra cứu và kể chuyện gia đình.

**Priority**

Medium

---

#### FR-FG-08 Tra cứu quan hệ

**Description**

Hệ thống cho phép Family Member tra cứu quan hệ giữa hai thành viên bất kỳ trong gia đình: hệ thống duyệt đồ thị gia đình, tìm đường đi ngắn nhất giữa hai thành viên và mô tả quan hệ bằng ngôn ngữ tự nhiên (ví dụ: "Nguyễn Văn A là chú họ của Nguyễn Thị B"). Kết quả kèm chuỗi quan hệ từng bước (path) để người dùng kiểm chứng.

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (sinh mô tả quan hệ bằng ngôn ngữ tự nhiên, hỗ trợ FR-AI-03)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Hai thành viên cần tra cứu thuộc cùng gia đình.
3. Đồ thị quan hệ có dữ liệu tối thiểu (FR-FG-04, FR-FG-05).

**Trigger**

Family Member mở trang tra cứu quan hệ, chọn hai thành viên và nhấn "Tra cứu".

**Main Flow**

1. Family Member mở trang "Tra cứu quan hệ".
2. Family Member chọn thành viên thứ nhất (A) và thành viên thứ hai (B) từ danh sách hoặc tìm kiếm.
3. Family Member nhấn "Tra cứu".
4. Hệ thống duyệt đồ thị gia đình tìm đường đi ngắn nhất giữa A và B.
5. Hệ thống xác định loại quan hệ dựa trên đường đi (cha–con, ông bà, chú bác, anh em họ, thông gia, ...).
6. Hệ thống hiển thị kết quả: tên quan hệ, mô tả ngắn, và chuỗi từng bước (A → cha → ông → B...).
7. Hệ thống cung cấp nút "Giải thích bằng AI" để sinh mô tả chi tiết (FR-AI-03).

**Alternate Flow**

- **A1, Không tìm thấy đường đi:** Hai thành viên chưa có quan hệ được thiết lập; hệ thống thông báo "Chưa xác định được quan hệ" và gợi ý kiểm tra dữ liệu gia phả.
- **A2, A trùng B:** Hệ thống báo lỗi "Vui lòng chọn hai thành viên khác nhau".
- **A3, Đường đi không duy nhất:** Hệ thống hiển thị quan hệ ngắn nhất và thông báo có các đường quan hệ khác (xem thêm nếu muốn).

**Postconditions**

1. Kết quả tra cứu hiển thị đúng quan hệ và đường đi.
2. Lịch sử tra cứu được ghi nhận phục vụ tần suất sử dụng (ẩn danh).

**Expected Result**

Family Member biết chính xác quan hệ giữa hai thành viên bất kỳ, kể cả quan hệ phức tạp, trong thời gian không quá 2 giây.

**Priority**

High

---
### 4.4.3 Module 3, Community

**Tên module:** Community

**Mục đích:** Cung cấp không gian tương tác xã hội cho các thành viên trong gia đình: chia sẻ bài viết, tin tức, hình ảnh, bình luận, thả cảm xúc và nhận thông báo. Module này biến gia phả tĩnh thành cộng đồng gia đình sống động, khuyến khích giao tiếp thường xuyên giữa các thế hệ.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Đăng và quản lý bài viết | Tạo, sửa, xóa bài viết trong phạm vi gia đình. |
| Bình luận và thả cảm xúc | Tương tác với bài viết của thành viên khác. |
| Chia sẻ tin tức gia đình | Đăng tin tức, sự kiện gia đình để mọi thành viên nắm được. |
| Chia sẻ hình ảnh | Đăng ảnh kèm mô tả vào luồng cộng đồng. |
| Thông báo gia đình | Tạo thông báo chính thức (announcement) cho toàn gia đình. |

---

#### FR-COM-01 Đăng và quản lý bài viết

**Description**

Hệ thống cho phép Family Member đăng bài viết vào luồng cộng đồng của gia đình: nội dung văn bản, kèm hình ảnh/video (tùy chọn), gắn thẻ chủ đề và mức hiển thị (toàn gia đình hoặc chỉ nhánh cụ thể). Người đăng có thể sửa nội dung, xóa bài viết của chính mình. Bài viết phải tuân thủ chính sách nội dung và có thể bị kiểm duyệt (FR-ADM-02).

**Primary Actor**

Family Member

**Supporting Actors**

- Administrator (kiểm duyệt nội dung vi phạm)
- Notification Service (thông báo bài viết mới)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình đăng bài (FR-US-07).
3. Tài khoản không bị đình chỉ.

**Trigger**

Family Member mở trang cộng đồng và gửi bài viết mới.

**Main Flow**

1. Family Member mở luồng cộng đồng của gia đình.
2. Family Member chọn "Tạo bài viết", nhập nội dung (bắt buộc, ≤ 2000 ký tự), đính kèm hình ảnh/video (tùy chọn, tối đa 10 file).
3. Family Member chọn phạm vi hiển thị (toàn gia đình / một nhánh) và nhấn "Đăng".
4. Hệ thống kiểm tra nội dung (rỗng, kích thước file, loại file cho phép).
5. Hệ thống lưu bài viết ở trạng thái *Published* và hiển thị trên luồng cộng đồng.
6. Hệ thống gửi thông báo cho các thành viên trong phạm vi hiển thị.

**Alternate Flow**

- **A1, Sửa bài viết:** Người đăng mở bài viết của mình, chỉnh sửa và lưu; hệ thống cập nhật nội dung và đánh dấu thời gian chỉnh sửa.
- **A2, Xóa bài viết:** Người đăng xóa bài viết; hệ thống xóa mềm (ẩn khỏi mọi người) và ghi audit log.
- **A3, Nội dung vi phạm:** Nếu hệ thống phát hiện (từ khóa bị chặn) hoặc Administrator gỡ bài (FR-ADM-02), bài viết chuyển trạng thái *Removed*, người đăng nhận thông báo lý do.
- **A4, File không hợp lệ:** Hệ thống báo lỗi loại/kích thước file và chặn đăng.

**Postconditions**

1. Bài viết xuất hiện trong luồng cộng đồng theo đúng phạm vi.
2. Thành viên trong phạm vi nhận được thông báo.

**Expected Result**

Family Member chia sẻ nội dung thành công với kiểm soát phạm vi hiển thị; nội dung vi phạm bị xử lý theo chính sách.

**Priority**

High

---

#### FR-COM-02 Bình luận và thả cảm xúc

**Description**

Hệ thống cho phép Family Member bình luận vào bài viết của thành viên khác và thả cảm xúc (like, yêu thích, buồn, ...). Người bình luận có thể sửa/xóa bình luận của mình; người đăng bài có thể xóa bình luận trên bài viết của mình. Số lượng cảm xúc và bình luận hiển thị công khai trong gia đình.

**Primary Actor**

Family Member

**Supporting Actors**

- Notification Service (thông báo tương tác mới)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Bài viết đang ở trạng thái *Published* và thuộc phạm vi hiển thị của người tương tác.

**Trigger**

Family Member mở một bài viết trong luồng cộng đồng và bình luận hoặc thả cảm xúc.

**Main Flow**

1. Family Member mở bài viết chi tiết.
2. Family Member nhập nội dung bình luận (≤ 500 ký tự) hoặc chọn một cảm xúc.
3. Hệ thống lưu bình luận/cảm xúc.
4. Hệ thống cập nhật số lượng tương tác trên bài viết.
5. Hệ thống gửi thông báo cho người đăng bài (và những người đã bình luận, khi có phản hồi).

**Alternate Flow**

- **A1, Sửa/xóa bình luận:** Người bình luận sửa hoặc xóa bình luận của mình; hệ thống cập nhật ngay.
- **A2, Xóa bình luận của người khác:** Người đăng bài chọn xóa bình luận vi phạm trên bài viết của mình; hệ thống xóa và ghi audit log.
- **A3, Bỏ cảm xúc:** Family Member chọn lại cùng cảm xúc để gỡ; hệ thống giảm số đếm.
- **A4, Bình luận trống:** Hệ thống chặn gửi bình luận không có nội dung.

**Postconditions**

1. Bình luận/cảm xúc được lưu và hiển thị.
2. Người liên quan nhận thông báo tương tác.

**Expected Result**

Thành viên tương tác dễ dàng với nội dung gia đình; mọi thay đổi hiển thị ngay lập tức.

**Priority**

Medium

---

#### FR-COM-03 Chia sẻ tin tức gia đình

**Description**

Hệ thống cung cấp kênh tin tức gia đình (family news feed): Family Member có thể đăng tin tức như sinh nhật, lễ cưới, thành tựu học tập, tin buồn, với định dạng có cấu trúc (loại tin, ngày diễn ra, thành viên liên quan). Tin tức được đánh dấu riêng so với bài viết thường và xuất hiện ở vị trí ưu tiên trên luồng.

**Primary Actor**

Family Member

**Supporting Actors**

- Notification Service (thông báo tin tức quan trọng)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình đăng tin (FR-US-07).

**Trigger**

Family Member chọn "Đăng tin gia đình" từ luồng cộng đồng.

**Main Flow**

1. Family Member chọn "Đăng tin gia đình".
2. Family Member chọn loại tin (sinh nhật, cưới, học tập, công việc, tin buồn, khác), nhập tiêu đề, mô tả, ngày diễn ra, thành viên liên quan.
3. Family Member đính kèm hình ảnh (tùy chọn) và nhấn "Đăng".
4. Hệ thống kiểm tra tính hợp lệ và lưu tin tức ở trạng thái *Published*.
5. Hệ thống hiển thị tin tức ở mục "Tin gia đình" và gửi thông báo cho thành viên liên quan.

**Alternate Flow**

- **A1, Sửa/xóa tin:** Người đăng sửa hoặc xóa tin tức của mình trong thời gian cho phép (7 ngày); quá hạn phải nhờ Administrator.
- **A2, Gắn tin quan trọng:** Family Owner ghim tin tức quan trọng lên đầu luồng trong tối đa 7 ngày.
- **A3, Nội dung nhạy cảm:** Tin buồn được hiển thị với giao diện trang trọng hơn; hệ thống không tự động đề xuất cảm xúc "thích" cho loại tin này.

**Postconditions**

1. Tin tức xuất hiện đúng phân loại và phạm vi.
2. Thành viên liên quan nhận được thông báo.

**Expected Result**

Thành viên gia đình nắm được các sự kiện quan trọng của người thân thông qua kênh tin tức có cấu trúc, trực quan.

**Priority**

Medium

---

#### FR-COM-04 Chia sẻ hình ảnh

**Description**

Hệ thống cho phép Family Member chia sẻ hình ảnh lên luồng cộng đồng và thư viện ảnh gia đình: tải lên nhiều ảnh cùng lúc, gắn thẻ thành viên có mặt trong ảnh, thêm mô tả, chọn album đích. Ảnh được nén tự động và lưu trữ an toàn; thành viên được gắn thẻ nhận thông báo.

**Primary Actor**

Family Member

**Supporting Actors**

- Notification Service (thông báo gắn thẻ)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình chia sẻ ảnh (FR-US-07).

**Trigger**

Family Member chọn "Chia sẻ ảnh" và gửi ảnh từ thiết bị.

**Main Flow**

1. Family Member chọn "Chia sẻ ảnh".
2. Family Member chọn một hoặc nhiều ảnh từ thiết bị (tối đa 20 ảnh/lần, mỗi ảnh ≤ 10MB).
3. Family Member nhập mô tả, gắn thẻ thành viên có mặt, chọn album đích (tùy chọn).
4. Family Member nhấn "Đăng".
5. Hệ thống kiểm tra file, xử lý nén và lưu ảnh lên bộ lưu trữ.
6. Hệ thống hiển thị ảnh trên luồng và trong album; gửi thông báo cho thành viên được gắn thẻ.

**Alternate Flow**

- **A1, Ảnh vượt giới hạn:** Hệ thống từ chối ảnh quá kích thước hoặc định dạng không hỗ trợ (JPG, PNG, WebP, HEIC), báo lỗi cụ thể từng ảnh.
- **A2, Xóa ảnh:** Người đăng hoặc Family Owner xóa ảnh; hệ thống xóa mềm khỏi luồng và album, ghi audit log.
- **A3, Gắn thẻ sai:** Người được gắn thẻ có thể gỡ thẻ chính mình khỏi ảnh.
- **A4, Tải lên thất bại:** Hệ thống giữ nguyên tiến trình, cho phép thử lại từng ảnh lỗi.

**Postconditions**

1. Ảnh được lưu trữ, nén và hiển thị đúng vị trí.
2. Thành viên được gắn thẻ nhận thông báo.

**Expected Result**

Family Member lưu giữ và chia sẻ khoảnh khắc gia đình dễ dàng; ảnh truy cập nhanh và an toàn.

**Priority**

Medium

---

#### FR-COM-05 Thông báo gia đình

**Description**

Hệ thống cho phép Family Owner tạo thông báo chính thức (announcement) gửi đến toàn bộ hoặc một nhóm thành viên: tiêu đề, nội dung, mức độ quan trọng (thường/quan trọng/khẩn cấp), thời gian hiển thị. Thông báo hiển thị ở đầu luồng cộng đồng và qua kênh thông báo của hệ thống (in-app, email, push tùy cấu hình).

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (người nhận)
- Notification Service (phân phát thông báo)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Family Owner đang quản lý gia đình (FR-FG-01).

**Trigger**

Family Owner chọn "Tạo thông báo" trên trang cộng đồng.

**Main Flow**

1. Family Owner chọn "Tạo thông báo".
2. Family Owner nhập tiêu đề (≤ 100 ký tự), nội dung (≤ 2000 ký tự), chọn mức quan trọng và phạm vi nhận.
3. Family Owner chọn thời gian đăng ngay hoặc hẹn giờ, nhấn "Gửi".
4. Hệ thống kiểm tra nội dung và lưu thông báo.
5. Hệ thống đưa thông báo lên đầu luồng theo mức quan trọng và gửi qua các kênh đã cấu hình.
6. Hệ thống ghi nhận trạng thái gửi (đã nhận/chưa nhận) ẩn danh cho Family Owner.

**Alternate Flow**

- **A1, Hẹn giờ gửi:** Hệ thống xếp hàng thông báo và tự động phát hành đúng giờ.
- **A2, Sửa/Thu hồi:** Family Owner sửa nội dung hoặc thu hồi thông báo đã gửi; thành viên nhận bản cập nhật kèm dấu hiệu đã chỉnh sửa.
- **A3, Thông báo khẩn cấp:** Thông báo loại khẩn cấp được gửi qua tất cả kênh (kể cả email/push) bất kể cấu hình cá nhân; mức thông thường chỉ gửi in-app.

**Postconditions**

1. Thông báo được phân phát đến đúng phạm vi và kênh.
2. Thông báo xuất hiện nổi bật theo mức quan trọng.

**Expected Result**

Family Owner truyền đạt thông tin chính thức đến gia đình nhanh chóng; thành viên không bỏ lỡ thông báo quan trọng.

**Priority**

High

---

### 4.4.4 Module 4, Events

**Tên module:** Events

**Mục đích:** Hỗ trợ tổ chức và tham gia các sự kiện gia đình (họp mặt, lễ cưới, giỗ, sinh nhật): tạo sự kiện, mời tham gia, xác nhận tham dự (RSVP), quản lý người tham gia, lưu giữ khoảnh khắc qua thư viện ảnh sự kiện và nhắc nhở tự động.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Tạo sự kiện | Tạo sự kiện với thông tin thời gian, địa điểm, mô tả, mời thành viên. |
| Xác nhận tham dự (RSVP) | Thành viên xác nhận tham dự/không tham dự/có thể tham dự. |
| Quản lý người tham gia | Xem danh sách, xác nhận trạng thái, hỗ trợ khách ngoài gia đình. |
| Thư viện ảnh sự kiện | Thu thập ảnh của sự kiện vào album chung. |
| Nhắc nhở sự kiện | Gửi nhắc nhở tự động trước ngày diễn ra sự kiện. |

---

#### FR-EVT-01 Tạo sự kiện gia đình

**Description**

Hệ thống cho phép Family Member tạo sự kiện gia đình: tên, loại sự kiện, thời gian bắt đầu/kết thúc, địa điểm, mô tả, ảnh bìa, danh sách khách mời (thành viên gia đình và/hoặc khách ngoài). Người tạo trở thành chủ sự kiện (Event Owner) với quyền quản lý; Family Owner cũng có quyền quản lý mọi sự kiện trong gia đình.

**Primary Actor**

Family Member

**Supporting Actors**

- Family Member (khách mời)
- Notification Service (thư mời)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình tạo sự kiện (FR-US-07).

**Trigger**

Family Member chọn "Tạo sự kiện" trên trang sự kiện của gia đình.

**Main Flow**

1. Family Member chọn "Tạo sự kiện".
2. Family Member nhập tên sự kiện, loại (họp mặt, cưới, giỗ, sinh nhật, du lịch, khác), thời gian bắt đầu/kết thúc, địa điểm, mô tả.
3. Family Member chọn khách mời từ danh sách thành viên gia đình (mặc định tất cả) và thêm email khách ngoài (tùy chọn).
4. Family Member đính kèm ảnh bìa và nhấn "Tạo".
5. Hệ thống kiểm tra tính hợp lệ (thời gian kết thúc sau thời gian bắt đầu, tên không trống).
6. Hệ thống tạo sự kiện ở trạng thái *Open*, gán người tạo làm Event Owner.
7. Hệ thống gửi thư mời cho khách mời; khách ngoài nhận email mời có đường dẫn RSVP công khai.

**Alternate Flow**

- **A1, Sửa sự kiện:** Event Owner hoặc Family Owner cập nhật thông tin; hệ thống gửi thông báo thay đổi cho người đã RSVP.
- **A2, Hủy sự kiện:** Event Owner hủy sự kiện kèm lý do; hệ thống thông báo cho toàn bộ người tham gia và khóa RSVP.
- **A3, Lịch trùng:** Hệ thống cảnh báo nếu sự kiện trùng thời gian với sự kiện khác của cùng gia đình (không chặn).
- **A4, Số lượng khách ngoài giới hạn:** Mỗi sự kiện tối đa 50 khách ngoài để tránh lạm dụng.

**Postconditions**

1. Sự kiện tồn tại với đầy đủ thông tin và khách mời.
2. Khách mời nhận được thư mời.

**Expected Result**

Thành viên tổ chức sự kiện gia đình thành công; mọi người liên quan được mời và nắm thông tin đầy đủ.

**Priority**

High

---

#### FR-EVT-02 Xác nhận tham dự (RSVP)

**Description**

Hệ thống cho phép khách mời xác nhận trạng thái tham dự sự kiện: **Tham dự (Going)**, **Không tham dự (Not Going)**, hoặc **Có thể (Maybe)**. Thành viên gia đình xác nhận trong ứng dụng; khách ngoài xác nhận qua đường dẫn công khai trong email mời. Người tham gia có thể đổi trạng thái cho đến khi sự kiện kết thúc hoặc chủ sự kiện khóa danh sách.

**Primary Actor**

Family Member (khách mời)

**Supporting Actors**

- Guest (khách ngoài gia đình, qua link RSVP)

**Preconditions**

1. Khách mời nhận được thư mời (FR-EVT-01).
2. Sự kiện đang ở trạng thái *Open* và chưa kết thúc.

**Trigger**

Khách mời mở trang chi tiết sự kiện (hoặc link RSVP) và chọn trạng thái tham dự.

**Main Flow**

1. Khách mời mở trang chi tiết sự kiện.
2. Hệ thống hiển thị thông tin sự kiện và ba lựa chọn trạng thái.
3. Khách mời chọn trạng thái (Going / Not Going / Maybe) kèm số lượng người đi cùng (tùy chọn, chỉ khi Going).
4. Hệ thống lưu trạng thái RSVP và cập nhật số liệu tham gia trên trang sự kiện.
5. Hệ thống thông báo cho Event Owner về thay đổi trạng thái.

**Alternate Flow**

- **A1, Đổi trạng thái:** Khách mời chọn trạng thái khác; hệ thống ghi đè trạng thái cũ và cập nhật số liệu.
- **A2, Khóa RSVP:** Event Owner khóa danh sách trước sự kiện 24 giờ; hệ thống chặn mọi thay đổi và hiển thị "RSVP đã đóng".
- **A3, Khách ngoài không nhận email:** Event Owner gửi lại thư mời hoặc sao chép link RSVP gửi trực tiếp.

**Postconditions**

1. Trạng thái tham dự của mỗi khách mời được lưu chính xác.
2. Số liệu tham gia trên trang sự kiện được cập nhật.

**Expected Result**

Chủ sự kiện nắm chính xác số lượng người tham dự để chủ động khâu tổ chức.

**Priority**

Medium

---

#### FR-EVT-03 Quản lý người tham gia

**Description**

Hệ thống cung cấp cho Event Owner (và Family Owner) màn hình quản lý người tham gia: danh sách theo trạng thái RSVP (Going / Maybe / Not Going / Chưa phản hồi), thêm/xóa khách mời, gửi nhắc nhở cho người chưa phản hồi, xuất danh sách tham dự. Khách ngoài được theo dõi bằng email + tên khai báo.

**Primary Actor**

Family Owner / Event Owner

**Supporting Actors**

- Family Member (khách mời)
- Notification Service (nhắc nhở phản hồi)

**Preconditions**

1. Event Owner / Family Owner đã đăng nhập (FR-US-02).
2. Sự kiện đã tồn tại (FR-EVT-01).

**Trigger**

Event Owner mở trang "Người tham gia" của sự kiện.

**Main Flow**

1. Event Owner mở trang "Người tham gia".
2. Hệ thống hiển thị thống kê tóm tắt (Going / Maybe / Not Going / Chưa phản hồi) và danh sách chi tiết.
3. Event Owner lọc theo trạng thái, tìm kiếm theo tên/email.
4. Event Owner chọn "Nhắc nhở" gửi cho nhóm chưa phản hồi; hệ thống gửi thông báo nhắc.
5. Event Owner xuất danh sách tham dự (CSV/PDF) khi cần.
6. Event Owner thêm khách mời mới hoặc xóa khách khỏi danh sách (xóa không xóa hồ sơ thành viên).

**Alternate Flow**

- **A1, Khách ngoài cần nhập danh sách:** Event Owner nhập danh sách email hàng loạt (tối đa 50/lần); hệ thống tạo thư mời cho từng email.
- **A2, Người tham gia vượt sức chứa:** Hệ thống cảnh báo khi số Going vượt sức chứa khai báo của địa điểm (nếu có).
- **A3, Xóa nhầm:** Hệ thống yêu cầu xác nhận trước khi xóa khách khỏi danh sách.

**Postconditions**

1. Danh sách người tham gia phản ánh chính xác trạng thái RSVP.
2. Nhắc nhở được gửi đúng nhóm chưa phản hồi.

**Expected Result**

Event Owner điều phối người tham gia hiệu quả từ mời đến chốt danh sách.

**Priority**

Medium

---

#### FR-EVT-04 Thư viện ảnh sự kiện

**Description**

Mỗi sự kiện có thư viện ảnh riêng (event gallery): người tham gia tải ảnh lên album chung của sự kiện, xem ảnh theo thời gian thực, gắn thẻ thành viên. Album tự động gom ảnh của sự kiện, giúp lưu giữ và chia sẻ khoảnh khắc sau khi sự kiện kết thúc.

**Primary Actor**

Family Member

**Supporting Actors**

- Guest (khách ngoài được mời tải ảnh qua link)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member là người tham gia sự kiện (RSVP Going, FR-EVT-02).

**Trigger**

Family Member mở trang thư viện ảnh của sự kiện và tải ảnh lên.

**Main Flow**

1. Family Member mở tab "Thư viện ảnh" của sự kiện.
2. Hệ thống hiển thị lưới ảnh theo thời gian tải lên.
3. Family Member chọn "Tải ảnh", chọn ảnh từ thiết bị (tối đa 20 ảnh/lần).
4. Family Member nhập mô tả, gắn thẻ thành viên (tùy chọn) và tải lên.
5. Hệ thống kiểm tra và lưu ảnh vào album sự kiện.
6. Hệ thống cập nhật thư viện và thông báo cho người được gắn thẻ.

**Alternate Flow**

- **A1, Xóa ảnh:** Người tải hoặc Event Owner xóa ảnh khỏi album; ghi audit log.
- **A2, Tải lên khi chưa kết thúc:** Cho phép tải ảnh ngay trong sự kiện (livestream-like) và sau khi kết thúc tối đa 30 ngày.
- **A3, Khách ngoài tải ảnh:** Khách ngoài truy cập qua link album với token tạm, chỉ tải lên/xem, không thấy dữ liệu khác của gia đình.

**Postconditions**

1. Ảnh được lưu trong album sự kiện với thông tin người tải.
2. Mọi người tham gia truy cập được thư viện.

**Expected Result**

Khoảnh khắc sự kiện được thu thập đầy đủ từ nhiều người, lưu giữ lâu dài cho gia đình.

**Priority**

Medium

---

#### FR-EVT-05 Nhắc nhở sự kiện

**Description**

Hệ thống tự động gửi nhắc nhở cho người đã xác nhận tham dự (Going/Maybe) theo mốc thời gian: 7 ngày, 1 ngày và 3 giờ trước sự kiện. Nhắc nhở bao gồm tóm tắt thông tin sự kiện (thời gian, địa điểm) và trạng thái RSVP hiện tại. Người dùng có thể bật/tắt nhắc nhở cho từng sự kiện.

**Primary Actor**

Family Member (người nhận)

**Supporting Actors**

- Notification Service (lập lịch và gửi nhắc nhở)
- System Scheduler (kích hoạt theo lịch)

**Preconditions**

1. Người dùng có trạng thái RSVP Going hoặc Maybe (FR-EVT-02).
2. Sự kiện chưa diễn ra.
3. Người dùng chưa tắt nhắc nhở của sự kiện.

**Trigger**

Hệ thống Scheduler kích hoạt đúng mốc thời gian nhắc nhở (tự động, không cần thao tác người dùng).

**Main Flow**

1. Scheduler phát hiện sự kiện sắp đến mốc nhắc nhở.
2. Hệ thống lọc danh sách người nhận (RSVP Going/Maybe, chưa tắt nhắc).
3. Hệ thống tạo nội dung nhắc nhở (tên sự kiện, thời gian, địa điểm, nút xem chi tiết).
4. Hệ thống gửi qua kênh ưu tiên của người dùng (in-app; email/push nếu bật).
5. Hệ thống ghi nhận nhật ký gửi (ẩn danh) phục vụ thống kê.

**Alternate Flow**

- **A1, Tắt nhắc nhở:** Người dùng tắt nhắc cho sự kiện; hệ thống loại khỏi danh sách nhận.
- **A2, Sự kiện thay đổi thời gian:** Hệ thống tính lại các mốc nhắc nhở theo thời gian mới.
- **A3, Sự kiện bị hủy:** Hệ thống gửi thông báo hủy và không còn nhắc nhở.
- **A4, Kênh gửi lỗi:** Thất bại ở một kênh không ảnh hưởng kênh khác; hệ thống thử lại tối đa 2 lần.

**Postconditions**

1. Người tham dự nhận đủ các mốc nhắc nhở trước sự kiện.
2. Không gửi nhắc nhở sau khi sự kiện kết thúc.

**Expected Result**

Giảm tỷ lệ quên sự kiện; người tham dự luôn nắm thông tin mới nhất trước giờ diễn ra.

**Priority**

High

---

### 4.4.5 Module 5, Family Directory

**Tên module:** Family Directory

**Mục đích:** Cung cấp danh bạ thành viên của gia đình với hồ sơ nghề nghiệp và học vấn, hỗ trợ tìm kiếm theo nhiều tiêu chí (nghề nghiệp, địa điểm, thế hệ). Module này giúp kết nối các thành viên cùng lĩnh vực hoặc cùng khu vực, thúc đẩy hỗ trợ lẫn nhau giữa các thế hệ.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Danh bạ thành viên | Xem danh sách thành viên với thông tin cơ bản và liên hệ. |
| Hồ sơ nghề nghiệp | Lưu thông tin nghề nghiệp, công ty, vị trí, lĩnh vực. |
| Hồ sơ học vấn | Lưu thông tin học vấn: trường, chuyên ngành, bằng cấp, năm tốt nghiệp. |
| Tìm kiếm thành viên | Tìm theo nghề nghiệp, địa điểm, thế hệ và các bộ lọc kết hợp. |

---

#### FR-DIR-01 Danh bạ thành viên

**Description**

Hệ thống hiển thị danh bạ (directory) gồm toàn bộ thành viên của gia đình: ảnh đại diện, họ tên, thế hệ, nhánh, thông tin liên hệ (theo cài đặt riêng tư của từng người). Danh bạ có thể sắp xếp theo tên, thế hệ hoặc nhánh; liên kết trực tiếp đến hồ sơ thành viên trên cây gia phả.

**Primary Actor**

Family Member

**Supporting Actors**

Không có.

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình đang xem (FR-US-07).

**Trigger**

Family Member mở trang "Danh bạ" của gia đình.

**Main Flow**

1. Family Member mở trang "Danh bạ".
2. Hệ thống tải danh sách thành viên của gia đình (đã xác thực, trạng thái Active).
3. Hệ thống hiển thị danh bạ dạng danh sách/lưới với các cột: ảnh, tên, thế hệ, nhánh, địa điểm, liên hệ.
4. Family Member sắp xếp hoặc lọc theo nhánh/thế hệ.
5. Family Member chọn một thành viên; hệ thống mở trang hồ sơ chi tiết trong danh bạ.

**Alternate Flow**

- **A1, Thông tin liên hệ ẩn:** Nếu thành viên đặt riêng tư, hệ thống chỉ hiển thị nút "Gửi tin nhắn qua hệ thống" thay vì SĐT/email trực tiếp.
- **A2, Danh bạ trống:** Gia đình mới chưa có đủ thành viên; hệ thống hiển thị gợi ý mời thêm thành viên (FR-FG-03).

**Postconditions**

1. Danh bạ hiển thị đúng thành viên hợp lệ của gia đình.
2. Thông tin hiển thị tôn trọng cài đặt riêng tư.

**Expected Result**

Family Member nhanh chóng tìm và liên hệ được với bất kỳ thành viên nào trong gia đình.

**Priority**

Medium

---

#### FR-DIR-02 Hồ sơ nghề nghiệp

**Description**

Hệ thống cho phép Family Member khai báo thông tin nghề nghiệp trong hồ sơ: nghề nghiệp/vị trí, công ty/tổ chức, lĩnh vực, địa điểm làm việc, năm bắt đầu. Thông tin được hiển thị trong danh bạ theo cài đặt riêng tư và phục vụ tìm kiếm theo nghề nghiệp (FR-DIR-04) và gợi ý kết nối (FR-AI-05).

**Primary Actor**

Family Member

**Supporting Actors**

- Family Owner (cập nhật hồ sơ nghề nghiệp của thành viên chưa có tài khoản)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member có hồ sơ thành viên trong gia đình (FR-FG-03).

**Trigger**

Family Member mở mục "Nghề nghiệp" trong hồ sơ và cập nhật thông tin.

**Main Flow**

1. Family Member mở trang hồ sơ và chọn tab "Nghề nghiệp".
2. Hệ thống hiển thị thông tin nghề nghiệp hiện tại.
3. Family Member nhập: vị trí, công ty, lĩnh vực, địa điểm, năm bắt đầu, mô tả ngắn (tùy chọn).
4. Family Member chọn mức hiển thị (công khai trong gia đình / chỉ Family Owner).
5. Hệ thống kiểm tra tính hợp lệ (lĩnh vực thuộc danh mục chuẩn hóa).
6. Hệ thống lưu và cập nhật danh bạ.

**Alternate Flow**

- **A1, Nghề nghiệp không thuộc danh mục:** Hệ thống cho phép nhập tự do và gắn nhãn "Khác".
- **A2, Cập nhật hộ thành viên chưa có tài khoản:** Family Owner cập nhật hồ sơ nghề nghiệp hộ; khi thành viên liên kết tài khoản, dữ liệu được giữ nguyên.

**Postconditions**

1. Thông tin nghề nghiệp được lưu và hiển thị đúng quyền.
2. Thành viên xuất hiện trong kết quả tìm kiếm theo nghề nghiệp.

**Expected Result**

Thông tin nghề nghiệp chính xác, cập nhật được, hỗ trợ kết nối thành viên cùng lĩnh vực.

**Priority**

Low

---

#### FR-DIR-03 Hồ sơ học vấn

**Description**

Hệ thống cho phép Family Member khai báo thông tin học vấn: trường học, chuyên ngành, bậc học/bằng cấp, năm nhập học/năm tốt nghiệp. Hồ sơ học vấn có thể có nhiều bản ghi (nhiều cấp học). Thông tin hiển thị trong danh bạ theo cài đặt riêng tư và phục vụ tìm kiếm, đồng thời hỗ trợ chia sẻ tin học tập (FR-COM-03).

**Primary Actor**

Family Member

**Supporting Actors**

- Family Owner (cập nhật hộ thành viên chưa có tài khoản)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member có hồ sơ thành viên trong gia đình (FR-FG-03).

**Trigger**

Family Member mở mục "Học vấn" trong hồ sơ và thêm bản ghi học vấn.

**Main Flow**

1. Family Member mở trang hồ sơ và chọn tab "Học vấn".
2. Family Member chọn "Thêm học vấn".
3. Family Member nhập: trường, chuyên ngành, bậc học, năm nhập học, năm tốt nghiệp.
4. Hệ thống kiểm tra tính hợp lệ (năm tốt nghiệp ≥ năm nhập học).
5. Hệ thống lưu bản ghi và hiển thị theo thứ tự thời gian.
6. Family Member có thể thêm nhiều bản ghi hoặc sửa/xóa bản ghi cũ.

**Alternate Flow**

- **A1, Đang học:** Trường "năm tốt nghiệp" được để trống; hệ thống hiển thị "Đang học".
- **A2, Dữ liệu lỗi:** Hệ thống báo lỗi năm không hợp lệ và chặn lưu.

**Postconditions**

1. Hồ sơ học vấn được lưu với các bản ghi chính xác.
2. Thông tin xuất hiện trong danh bạ và tìm kiếm.

**Expected Result**

Thông tin học vấn của thành viên đầy đủ, dễ dàng tra cứu và cập nhật.

**Priority**

Low

---

#### FR-DIR-04 Tìm kiếm thành viên theo nghề nghiệp, địa điểm, thế hệ

**Description**

Hệ thống cung cấp tìm kiếm nâng cao trong danh bạ theo các tiêu chí: nghề nghiệp/lĩnh vực, địa điểm (nơi ở/nơi làm việc), thế hệ, nhánh và tên. Người dùng có thể kết hợp nhiều bộ lọc, kết quả sắp xếp theo mức liên quan và hiển thị thông tin tóm tắt; từ kết quả có thể mở hồ sơ chi tiết hoặc nhờ AI gợi ý các thành viên tương tự (FR-AI-05).

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (xếp hạng liên quan nâng cao, tùy chọn)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Danh bạ có dữ liệu thành viên (FR-DIR-01).

**Trigger**

Family Member mở trang tìm kiếm thành viên và nhập bộ lọc.

**Main Flow**

1. Family Member mở trang "Tìm kiếm thành viên".
2. Family Member nhập từ khóa (tên) và/hoặc chọn các bộ lọc: nghề nghiệp, địa điểm, thế hệ, nhánh.
3. Family Member nhấn "Tìm kiếm".
4. Hệ thống truy vấn danh bạ với các điều kiện kết hợp.
5. Hệ thống hiển thị kết quả kèm thông tin tóm tắt (tên, thế hệ, nghề nghiệp, địa điểm) và số lượng kết quả.
6. Family Member mở hồ sơ chi tiết hoặc lưu bộ lọc tìm kiếm.

**Alternate Flow**

- **A1, Không có kết quả:** Hệ thống gợi ý giảm bớt bộ lọc hoặc tìm với từ khóa khác.
- **A2, Tìm kiếm ẩn danh tính:** Kết quả tôn trọng cài đặt riêng tư, thành viên không cho hiển thị thông tin nghề nghiệp sẽ không xuất hiện khi tìm theo nghề nghiệp.
- **A3, Lưu bộ lọc:** Family Member lưu bộ lọc tìm kiếm để dùng lại (tối đa 10 bộ lọc đã lưu).

**Postconditions**

1. Kết quả tìm kiếm chính xác theo bộ lọc và cài đặt riêng tư.
2. Thời gian phản hồi tìm kiếm không quá 3 giây.

**Expected Result**

Family Member tìm được thành viên mong muốn theo nhiều tiêu chí kết hợp, nhanh chóng và chính xác.

**Priority**

High

---

### 4.4.6 Module 6, Family Heritage

**Tên module:** Family Heritage

**Mục đích:** Bảo tồn và truyền bá di sản gia đình: tư liệu lịch sử, câu chuyện gia đình, thành viên tiêu biểu, thư viện ảnh và kho lưu trữ số. Module này giúp các thế hệ trẻ hiểu về nguồn gốc, truyền thống và những con người đã góp phần xây dựng gia đình.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Quản lý tư liệu lịch sử | Lưu trữ tài liệu lịch sử: văn bản, hình ảnh, hiện vật số hóa. |
| Quản lý câu chuyện gia đình | Đăng tải các câu chuyện, kỷ niệm của gia đình. |
| Quản lý thành viên tiêu biểu | Tôn vinh các thành viên có đóng góp nổi bật. |
| Thư viện ảnh gia đình | Album ảnh chung theo chủ đề/thời gian. |
| Kho lưu trữ số | Lưu trữ có cấu trúc, phân loại, tìm kiếm toàn bộ tư liệu. |

---

#### FR-HER-01 Quản lý tư liệu lịch sử

**Description**

Hệ thống cho phép Family Owner (và thành viên được ủy quyền) lưu trữ tư liệu lịch sử gia đình: tài liệu văn bản (sắc phong, giấy tờ cổ, thư từ), hình ảnh lịch sử, bản đồ, hiện vật số hóa. Mỗi tư liệu có thông tin mô tả: tiêu đề, loại tư liệu, niên đại, người liên quan, giai đoạn lịch sử. Tư liệu chỉ được sửa/xóa bởi người tạo hoặc Family Owner; mọi thay đổi đều được ghi nhật ký.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (người tạo tư liệu, được Owner ủy quyền)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình đã tồn tại (FR-FG-01).

**Trigger**

Family Owner mở trang "Tư liệu lịch sử" và tải lên tư liệu mới.

**Main Flow**

1. Family Owner mở trang "Tư liệu lịch sử".
2. Family Owner chọn "Thêm tư liệu".
3. Family Owner tải file lên và nhập: tiêu đề, loại tư liệu, niên đại, mô tả, giai đoạn lịch sử, thành viên liên quan.
4. Hệ thống kiểm tra định dạng và kích thước file (tối đa 25MB/tư liệu).
5. Hệ thống lưu tư liệu, tạo bản xem trước nếu là ảnh/PDF, hiển thị trong kho lưu trữ.
6. Hệ thống ghi nhật ký tạo mới tư liệu (FR-ADM-03).

**Alternate Flow**

- **A1, Sửa thông tin tư liệu:** Người tạo/Family Owner cập nhật mô tả, niên đại; hệ thống lưu lịch sử phiên bản.
- **A2, Xóa tư liệu:** Xóa mềm với xác nhận; tư liệu ẩn khỏi mọi người và ghi audit log.
- **A3, Gán nhánh cho tư liệu:** Tư liệu có thể gắn với nhánh cụ thể để lọc theo nhánh (FR-FG-02).
- **A4, Tư liệu trùng lặp:** Hệ thống cảnh báo nếu phát hiện file trùng hash với tư liệu hiện có.

**Postconditions**

1. Tư liệu được lưu trữ an toàn với đầy đủ thông tin mô tả.
2. Tư liệu truy cập được theo phân quyền gia đình.

**Expected Result**

Di sản lịch sử gia đình được số hóa và bảo tồn lâu dài, dễ dàng tra cứu.

**Priority**

Medium

---

#### FR-HER-02 Quản lý câu chuyện gia đình

**Description**

Hệ thống cho phép Family Member đăng tải câu chuyện gia đình (family stories): bài viết dài kể về kỷ niệm, truyền thống, sự kiện đáng nhớ, gắn với các thành viên liên quan. Câu chuyện hiển thị trong kho di sản với giao diện đọc đẹp, hỗ trợ ảnh minh họa; các thành viên khác có thể bày tỏ cảm xúc và bình luận (tái sử dụng tương tác từ FR-COM-02).

**Primary Actor**

Family Member

**Supporting Actors**

- Family Member (người đọc, tương tác)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình (FR-US-07).

**Trigger**

Family Member chọn "Viết câu chuyện" trong kho di sản.

**Main Flow**

1. Family Member mở mục "Câu chuyện gia đình".
2. Family Member chọn "Viết câu chuyện".
3. Family Member nhập tiêu đề (≤ 200 ký tự), nội dung (≤ 20.000 ký tự), gắn thành viên liên quan, giai đoạn, ảnh minh họa.
4. Family Member chọn lưu nháp hoặc đăng ngay.
5. Hệ thống kiểm tra nội dung và lưu câu chuyện ở trạng thái *Published*.
6. Hệ thống hiển thị câu chuyện trong kho di sản và thông báo cho thành viên được gắn.

**Alternate Flow**

- **A1, Lưu nháp:** Câu chuyện lưu ở trạng thái *Draft*, chỉ người viết thấy; có thể đăng sau.
- **A2, Sửa/xóa:** Người viết sửa hoặc xóa câu chuyện của mình; xóa phải có xác nhận.
- **A3, Nội dung vi phạm:** Câu chuyện bị gỡ nếu vi phạm chính sách nội dung (FR-ADM-02).
- **A4, Chuyển quyền sở hữu:** Nếu người viết rời gia đình, Family Owner nhận quyền quản lý câu chuyện.

**Postconditions**

1. Câu chuyện được lưu và hiển thị theo trạng thái.
2. Thành viên liên quan nhận thông báo.

**Expected Result**

Ký ức gia đình được ghi lại và truyền lại cho các thế hệ sau qua những câu chuyện có cấu trúc.

**Priority**

Medium

---

#### FR-HER-03 Quản lý thành viên tiêu biểu

**Description**

Hệ thống cho phép Family Owner tôn vinh các thành viên tiêu biểu (outstanding members) của gia đình: cá nhân có đóng góp nổi bật (học vấn, nghề nghiệp, cống hiến cộng đồng, phụng sự dòng họ). Mỗi hồ sơ tiêu biểu gồm: thành viên, danh hiệu, tiểu sử ngắn, thành tựu, giai đoạn. Hồ sơ hiển thị trang trọng trong khu vực di sản.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (đề xuất thành viên tiêu biểu)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Thành viên được đề cử tồn tại trong gia đình (FR-FG-03).

**Trigger**

Family Owner mở mục "Thành viên tiêu biểu" và tạo hồ sơ tôn vinh.

**Main Flow**

1. Family Owner mở mục "Thành viên tiêu biểu".
2. Family Owner chọn "Thêm thành viên tiêu biểu".
3. Family Owner chọn thành viên từ danh bạ, nhập danh hiệu, tiểu sử ngắn, thành tựu, giai đoạn.
4. Hệ thống kiểm tra tính hợp lệ (thành viên chưa có hồ sơ tiêu biểu).
5. Hệ thống lưu hồ sơ và hiển thị trong khu vực di sản.
6. Hệ thống ghi nhận thông tin người tạo và thời điểm (audit log).

**Alternate Flow**

- **A1, Đề xuất của thành viên:** Family Member gửi đề xuất; Family Owner duyệt hoặc từ chối kèm lý do.
- **A2, Sửa/xóa hồ sơ:** Family Owner cập nhật thành tựu hoặc gỡ hồ sơ khi cần.
- **A3, Trùng lặp:** Hệ thống chặn tạo hồ sơ tiêu biểu cho thành viên đã có.

**Postconditions**

1. Hồ sơ thành viên tiêu biểu tồn tại với đầy đủ thông tin.
2. Mọi thành viên gia đình truy cập được khu vực tôn vinh.

**Expected Result**

Tấm gương của các thành viên tiêu biểu được ghi nhận và truyền cảm hứng cho thế hệ trẻ.

**Priority**

Low

---

#### FR-HER-04 Thư viện ảnh gia đình

**Description**

Hệ thống cung cấp thư viện ảnh gia đình tập trung: ảnh được chia sẻ qua Community (FR-COM-04) và ảnh sự kiện (FR-EVT-04) được tự động gom về theo album chủ đề (năm, dịp lễ, thành viên). Family Member xem ảnh theo thời gian, lọc theo thẻ, tải xuống ảnh trong phạm vi gia đình.

**Primary Actor**

Family Member

**Supporting Actors**

Không có.

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Thư viện có dữ liệu ảnh (từ FR-COM-04 / FR-EVT-04).

**Trigger**

Family Member mở trang "Thư viện ảnh" của gia đình.

**Main Flow**

1. Family Member mở trang "Thư viện ảnh".
2. Hệ thống hiển thị các album theo chủ đề/thời gian kèm ảnh bìa và số lượng.
3. Family Member chọn album để xem lưới ảnh.
4. Family Member mở ảnh ở chế độ xem lớn (lightbox), xem thông tin (người tải, thẻ, thời gian).
5. Family Member tải xuống ảnh (bản gốc nếu có quyền, hoặc bản nén).
6. Family Member gợi ý gộp ảnh vào album phù hợp hơn (đề xuất, không tự chuyển).

**Alternate Flow**

- **A1, Tìm ảnh cũ:** Family Member tìm theo năm/thẻ/người; hệ thống lọc ảnh khớp.
- **A2, Tạo album:** Family Member tạo album riêng để tổ chức ảnh theo ý mình (album cá nhân, không ảnh hưởng album chung).
- **A3, Ảnh nhạy cảm:** Family Member đánh dấu ảnh riêng tư; chỉ người được chỉ định xem.

**Postconditions**

1. Thư viện ảnh cập nhật tự động từ các nguồn chia sẻ.
2. Quyền xem/tải tôn trọng cài đặt riêng tư.

**Expected Result**

Khoảnh khắc gia đình được lưu giữ tập trung, dễ tìm và dễ chia sẻ lại.

**Priority**

Medium

---

#### FR-HER-05 Kho lưu trữ số

**Description**

Hệ thống cung cấp kho lưu trữ số (digital archive) tập trung toàn bộ di sản: tư liệu lịch sử (FR-HER-01), câu chuyện (FR-HER-02), hồ sơ thành viên tiêu biểu (FR-HER-03), thư viện ảnh (FR-HER-04). Kho lưu trữ có phân loại theo loại nội dung, giai đoạn, nhánh; hỗ trợ tìm kiếm kết hợp và duyệt theo thời gian. Dữ liệu được sao lưu định kỳ (FR-ADM-04) và có quyền truy cập theo RBAC.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Member (đọc và tìm kiếm)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Tối thiểu một loại nội dung di sản đã tồn tại (FR-HER-01 đến FR-HER-04).

**Trigger**

Family Owner mở trang "Kho lưu trữ" của gia đình.

**Main Flow**

1. Family Owner mở trang "Kho lưu trữ".
2. Hệ thống hiển thị các danh mục: Tư liệu lịch sử, Câu chuyện, Thành viên tiêu biểu, Thư viện ảnh kèm số lượng.
3. Family Owner duyệt hoặc tìm kiếm với các bộ lọc: loại, giai đoạn, nhánh, từ khóa.
4. Family Owner mở mục để xem chi tiết từng nội dung.
5. Family Owner xem thống kê tổng quan kho lưu trữ (tổng tư liệu, tổng dung lượng).
6. Hệ thống hỗ trợ xuất báo cáo thư mục kho lưu trữ (PDF).

**Alternate Flow**

- **A1, Tìm kiếm nâng cao:** Family Member dùng tìm kiếm ngữ nghĩa AI (FR-AI-01) để tìm nội dung di sản.
- **A2, Dung lượng đầy:** Hệ thống cảnh báo khi kho đạt 90% hạn mức; Family Owner nén hoặc dọn tư liệu cũ.
- **A3, Truy cập hạn chế:** Một số tư liệu nhạy cảm chỉ Family Owner xem; RBAC kiểm soát (FR-US-05).

**Postconditions**

1. Toàn bộ di sản truy cập tập trung từ một cổng.
2. Tìm kiếm và phân loại hoạt động chính xác.

**Expected Result**

Di sản gia đình được tổ chức, bảo tồn và dễ dàng khám phá bởi mọi thế hệ.

**Priority**

High

---

### 4.4.7 Module 7, AI-assisted Services

**Tên module:** AI-assisted Services

**Mục đích:** Tích hợp trí tuệ nhân tạo như trợ lý thông minh của gia đình: tìm kiếm ngữ nghĩa, trợ lý tri thức, giải thích quan hệ, tóm tắt nội dung và gợi ý cá nhân hóa. AI giúp người dùng khám phá tri thức gia đình hiệu quả hơn, không thay thế quyết định của con người, mọi phản hồi AI đều là gợi ý, người dùng chịu trách nhiệm cuối cùng.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Tìm kiếm ngữ nghĩa | Tìm nội dung theo ý nghĩa, không chỉ từ khóa. |
| Trợ lý tri thức | Hỏi đáp về thông tin gia đình bằng ngôn ngữ tự nhiên. |
| Giải thích quan hệ | Giải thích quan hệ gia đình bằng văn bản dễ hiểu. |
| Tóm tắt nội dung | Tóm tắt bài viết, câu chuyện, sự kiện. |
| Gợi ý thông minh | Gợi ý thành viên và tài nguyên liên quan. |

---

#### FR-AI-01 Tìm kiếm ngữ nghĩa bằng AI

**Description**

Hệ thống cung cấp tìm kiếm ngữ nghĩa (semantic search) trên toàn bộ dữ liệu gia đình: gia phả, bài viết, câu chuyện, tư liệu, sự kiện. Khác với tìm kiếm từ khóa truyền thống, người dùng nhập câu hỏi hoặc mô tả theo ngôn ngữ tự nhiên và hệ thống hiểu ý nghĩa để trả về kết quả phù hợp nhất, kèm độ liên quan và giải thích ngắn.

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (embedding + xếp hạng ngữ nghĩa)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc gia đình (FR-US-07), kết quả chỉ trong phạm vi quyền của người dùng.
3. AI Service khả dụng (dịch vụ hoạt động).

**Trigger**

Family Member nhập câu hỏi vào ô tìm kiếm và nhấn tìm kiếm.

**Main Flow**

1. Family Member mở trang tìm kiếm hoặc ô tìm kiếm toàn cục.
2. Family Member nhập truy vấn ngôn ngữ tự nhiên (ví dụ: "Những ai trong gia đình làm bác sĩ?").
3. Hệ thống gửi truy vấn đến AI Service cùng phạm vi quyền truy cập.
4. AI Service chuyển truy vấn thành embedding và đối chiếu với chỉ mục ngữ nghĩa của dữ liệu gia đình.
5. Hệ thống trả về danh sách kết quả xếp theo độ liên quan, nhóm theo loại nội dung (thành viên, bài viết, tư liệu, sự kiện).
6. Family Member mở kết quả để xem chi tiết.

**Alternate Flow**

- **A1, Không có kết quả phù hợp:** Hệ thống gợi ý truy vấn khác hoặc tìm kiếm từ khóa truyền thống.
- **A2, AI Service không khả dụng:** Hệ thống tự động fallback về tìm kiếm từ khóa; hiển thị ghi chú "đang dùng chế độ tìm kiếm cơ bản".
- **A3, Truy vấn ngoài phạm vi quyền:** Kết quả tự động lọc, không trả về dữ liệu người dùng không có quyền xem.
- **A4, Truy vấn không rõ ràng:** AI hỏi lại để làm rõ ý định trước khi tìm.

**Postconditions**

1. Kết quả tìm kiếm phản ánh đúng ý định người dùng.
2. Không có dữ liệu ngoài phạm vi quyền bị lộ.

**Expected Result**

Family Member tìm được thông tin mong muốn bằng câu hỏi tự nhiên, kể cả khi không nhớ chính xác từ khóa.

**Priority**

High

---

#### FR-AI-02 Trợ lý tri thức gia đình (AI Assistant)

**Description**

Hệ thống cung cấp trợ lý ảo (AI Assistant) cho phép Family Member hỏi đáp bằng ngôn ngữ tự nhiên về mọi khía cạnh của gia đình: lịch sử, cấu trúc gia phả, thành viên, sự kiện, di sản. Trợ lý trả lời dựa trên dữ liệu gia đình đã được phép truy cập (RAG, Retrieval Augmented Generation), luôn trích dẫn nguồn. Trợ lý không trả lời các câu hỏi ngoài phạm vi dữ liệu gia đình.

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (LLM + truy xuất tri thức gia đình)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member thuộc ít nhất một gia đình (FR-US-07).
3. AI Service khả dụng.

**Trigger**

Family Member mở cửa sổ trợ lý AI và gửi câu hỏi.

**Main Flow**

1. Family Member mở cửa sổ trợ lý AI (trang hoặc widget).
2. Family Member nhập câu hỏi ngôn ngữ tự nhiên (ví dụ: "Ông nội em sinh năm nào?").
3. Hệ thống gửi câu hỏi kèm ngữ cảnh quyền truy cập của người dùng.
4. AI Service truy xuất các đoạn dữ liệu liên quan từ kho tri thức gia đình.
5. AI Service sinh câu trả lời dựa trên dữ liệu truy xuất, kèm trích dẫn nguồn.
6. Hệ thống hiển thị câu trả lời và danh sách nguồn (link đến hồ sơ/tài liệu gốc).
7. Family Member đánh giá hữu ích (👍/👎) hoặc hỏi tiếp trong cùng phiên hội thoại.

**Alternate Flow**

- **A1, Không tìm thấy dữ liệu:** Trợ lý trả lời "Chưa có thông tin trong dữ liệu gia đình" và gợi ý kiểm tra gia phả.
- **A2, Câu hỏi ngoài phạm vi:** Trợ lý từ chối nhẹ nhàng và đề nghị câu hỏi về gia đình.
- **A3, AI Service lỗi:** Hệ thống hiển thị thông báo lỗi, cho phép thử lại; hội thoại được lưu an toàn.
- **A4, Ngữ cảnh thiếu:** Trợ lý hỏi lại thông tin bổ sung (tên đầy đủ, nhánh nào...).

**Postconditions**

1. Câu trả lời hiển thị kèm nguồn trích dẫn.
2. Phiên hội thoại được lưu trong lịch sử cá nhân (tùy chọn).

**Expected Result**

Family Member tra cứu tri thức gia đình nhanh chóng bằng ngôn ngữ tự nhiên, tin cậy vì có trích dẫn nguồn.

**Priority**

High

---

#### FR-AI-03 Giải thích quan hệ gia đình

**Description**

Hệ thống cho phép Family Member yêu cầu AI giải thích quan hệ giữa hai thành viên bằng ngôn ngữ tự nhiên dễ hiểu. Dựa trên đường đi quan hệ trên đồ thị gia đình (từ FR-FG-08), AI sinh giải thích: tên quan hệ, ý nghĩa, cách tính từ góc nhìn của người hỏi, kèm lưu ý về các đường quan hệ khác (nếu có).

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (sinh văn bản giải thích)
- Family & Genealogy Module (dữ liệu đồ thị)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Hai thành viên thuộc cùng gia đình.
3. Đồ thị quan hệ có đường đi giữa hai thành viên (FR-FG-08).

**Trigger**

Family Member nhấn nút "Giải thích bằng AI" tại màn hình tra cứu quan hệ.

**Main Flow**

1. Family Member tra cứu quan hệ giữa hai thành viên (FR-FG-08).
2. Family Member nhấn "Giải thích bằng AI".
3. Hệ thống gửi đường đi quan hệ (chuỗi các mối quan hệ) cho AI Service.
4. AI Service sinh giải thích: tên quan hệ, mô tả ý nghĩa, giải thích từng bước của đường đi.
5. Hệ thống hiển thị giải thích kèm nguồn (các cạnh quan hệ trên đồ thị).
6. Family Member đánh giá độ chính xác của giải thích (đúng/sai).

**Alternate Flow**

- **A1, Đánh giá "sai":** Family Member báo cáo giải thích không chính xác; hệ thống ghi nhận phản hồi để cải thiện (không tự sửa dữ liệu gia phả).
- **A2, Không có đường đi:** Nút giải thích bị ẩn/khóa vì không có quan hệ (FR-FG-08, A1).
- **A3, AI lỗi:** Hiển thị giải thích cơ bản (tên quan hệ từ đồ thị) kèm thông báo AI tạm không khả dụng.

**Postconditions**

1. Giải thích hiển thị đúng đường đi và quan hệ.
2. Phản hồi đánh giá được ghi nhận.

**Expected Result**

Family Member hiểu rõ mối quan hệ phức tạp qua giải thích tự nhiên, dễ hiểu cho mọi lứa tuổi.

**Priority**

Medium

---

#### FR-AI-04 Tóm tắt nội dung bằng AI

**Description**

Hệ thống cho phép Family Member yêu cầu AI tóm tắt nội dung dài: bài viết, câu chuyện gia đình, thảo luận trong sự kiện. Tóm tắt được sinh tự động với độ dài tùy chọn (ngắn/vừa/đầy đủ), làm nổi bật thông tin quan trọng. Tóm tắt chỉ mang tính hỗ trợ đọc nhanh, không thay thế nội dung gốc.

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (sinh tóm tắt)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Nội dung cần tóm tắt thuộc phạm vi quyền truy cập của người dùng.
3. Nội dung có độ dài tối thiểu (≥ 500 ký tự) để tóm tắt có giá trị.

**Trigger**

Family Member nhấn nút "Tóm tắt" trên một nội dung dài.

**Main Flow**

1. Family Member mở nội dung dài (bài viết/câu chuyện).
2. Family Member nhấn "Tóm tắt bằng AI".
3. Hệ thống gửi nội dung (đã được phép truy cập) cho AI Service.
4. AI Service sinh tóm tắt theo độ dài mặc định.
5. Hệ thống hiển thị tóm tắt trong khung gọn, kèm nút "Mở rộng" xem nội dung gốc.
6. Family Member chọn độ dài khác nếu cần; hệ thống sinh lại tóm tắt.

**Alternate Flow**

- **A1, Nội dung quá ngắn:** Nút tóm tắt bị ẩn hoặc thông báo không cần tóm tắt.
- **A2, AI lỗi:** Hệ thống thông báo thử lại sau, nội dung gốc vẫn hiển thị bình thường.
- **A3, Tóm tắt nội dung nhạy cảm:** Không tóm tắt tin buồn; chỉ hiển thị nội dung gốc trang trọng.

**Postconditions**

1. Tóm tắt hiển thị chính xác nội dung chính.
2. Nội dung gốc luôn có sẵn để kiểm chứng.

**Expected Result**

Family Member nắm nhanh nội dung dài của gia đình, đặc biệt hữu ích với thành viên lớn tuổi hoặc ít thời gian.

**Priority**

Medium

---

#### FR-AI-05 Gợi ý thành viên và tài nguyên gia đình

**Description**

Hệ thống sử dụng AI để gợi ý cá nhân hóa cho Family Member: thành viên có thể kết nối (cùng nghề nghiệp, cùng địa điểm, cùng sở thích khai báo), tài nguyên di sản có thể quan tâm (câu chuyện, tư liệu liên quan đến thành viên mình quan tâm), sự kiện sắp diễn ra phù hợp. Gợi ý hiển thị ở khu vực riêng, có nút "Không quan tâm" để loại bỏ; không dùng dữ liệu nhạy cảm (sức khỏe, tôn giáo, chính trị).

**Primary Actor**

Family Member

**Supporting Actors**

- AI Service (tính toán gợi ý)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Family Member có lịch sử hoạt động tối thiểu trên hệ thống (xem hồ sơ, tương tác, khai báo nghề nghiệp).

**Trigger**

Family Member mở trang chủ hoặc khu vực "Gợi ý cho bạn".

**Main Flow**

1. Family Member mở trang chủ của gia đình.
2. Hệ thống gọi AI Service tạo gợi ý dựa trên: hồ sơ người dùng, lịch sử tương tác, cấu trúc gia đình.
3. Hệ thống hiển thị các nhóm gợi ý: thành viên có thể kết nối, tài nguyên di sản, sự kiện, mỗi nhóm tối đa 5 mục kèm lý do ngắn gọn.
4. Family Member xem hoặc bỏ qua gợi ý.
5. Family Member nhấn "Không quan tâm" để loại mục đó khỏi gợi ý tương lai.

**Alternate Flow**

- **A1, Chưa đủ dữ liệu:** Hệ thống hiển thị gợi ý cơ bản (thành viên cùng nhánh, tài liệu mới nhất) thay vì gợi ý cá nhân hóa.
- **A2, Quyền riêng tư:** Gợi ý chỉ dùng dữ liệu trong phạm vi quyền; không gợi ý thành viên đã ẩn hồ sơ.
- **A3, Tắt gợi ý:** Family Member tắt toàn bộ gợi ý trong cài đặt; hệ thống ngừng tính toán gợi ý cho tài khoản.

**Postconditions**

1. Gợi ý hiển thị đúng phạm vi quyền và sở thích.
2. Lựa chọn "Không quan tâm" được ghi nhận.

**Expected Result**

Family Member khám phá các kết nối và tài nguyên hữu ích, tăng mức độ gắn kết gia đình.

**Priority**

Low

---

### 4.4.8 Module 8, Dashboard & Reporting

**Tên module:** Dashboard & Reporting

**Mục đích:** Cung cấp cái nhìn tổng quan định lượng về gia đình: thống kê thành viên, hoạt động cộng đồng, sự kiện, nhân khẩu; hỗ trợ xuất báo cáo phục vụ quản trị và báo cáo dự án. Số liệu chỉ hiển thị trong phạm vi quyền của người xem.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Thống kê gia đình | Tổng quan số thành viên, thế hệ, nhánh, độ phủ dữ liệu. |
| Dashboard cộng đồng | Theo dõi hoạt động: bài viết, tương tác, nội dung mới. |
| Thống kê sự kiện | Số sự kiện, tỷ lệ tham dự, xu hướng theo thời gian. |
| Thống kê nhân khẩu | Phân bố độ tuổi, giới tính, địa điểm, nghề nghiệp. |
| Tạo và xuất báo cáo | Tạo báo cáo tổng hợp và xuất PDF/CSV. |

---

#### FR-DASH-01 Thống kê gia đình

**Description**

Hệ thống hiển thị trang thống kê gia đình cho Family Owner: tổng số thành viên, số nhánh, số thế hệ, tỷ lệ hồ sơ đầy đủ thông tin, số thành viên đã liên kết tài khoản. Số liệu được tính toán từ dữ liệu đồ thị gia đình và cập nhật theo thời gian thực (khi có thay đổi dữ liệu).

**Primary Actor**

Family Owner

**Supporting Actors**

- Family & Genealogy Module (nguồn dữ liệu)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình có dữ liệu thành viên (FR-FG-03).

**Trigger**

Family Owner mở trang "Thống kê gia đình".

**Main Flow**

1. Family Owner mở trang "Thống kê" của gia đình.
2. Hệ thống tính toán các chỉ số từ dữ liệu gia đình.
3. Hệ thống hiển thị thẻ chỉ số: tổng thành viên, số nhánh, số thế hệ, thành viên đã liên kết tài khoản, hồ sơ thiếu thông tin.
4. Family Owner bấm vào chỉ số để xem danh sách chi tiết (ví dụ: danh sách hồ sơ thiếu thông tin).
5. Family Owner chọn thời gian xem (tất cả / 1 năm) nếu áp dụng.

**Alternate Flow**

- **A1, Gia đình chưa có dữ liệu:** Hiển thị trạng thái trống và hướng dẫn thêm thành viên.
- **A2, Số liệu không chính xác:** Family Owner kiểm tra lại dữ liệu gốc; hệ thống chỉ hiển thị, không tự sửa.

**Postconditions**

1. Số liệu phản ánh đúng trạng thái hiện tại của gia đình.
2. Family Owner hiểu mức độ hoàn thiện dữ liệu gia phả.

**Expected Result**

Family Owner nắm bức tranh tổng thể về gia đình và phát hiện dữ liệu thiếu để cập nhật.

**Priority**

Medium

---

#### FR-DASH-02 Bảng điều khiển hoạt động cộng đồng

**Description**

Hệ thống hiển thị dashboard hoạt động cộng đồng cho Family Member (tóm tắt) và Family Owner (chi tiết): số bài viết mới, bình luận, cảm xúc, ảnh chia sẻ, thành viên hoạt động tích cực trong tuần. Mục tiêu khuyến khích tương tác và phát hiện thành viên ít tham gia.

**Primary Actor**

Family Member

**Supporting Actors**

- Community Module (nguồn dữ liệu)

**Preconditions**

1. Family Member đã đăng nhập (FR-US-02).
2. Cộng đồng gia đình có hoạt động (FR-COM-01).

**Trigger**

Family Member mở trang "Hoạt động cộng đồng" trên trang chủ.

**Main Flow**

1. Family Member mở trang "Hoạt động cộng đồng".
2. Hệ thống tính toán chỉ số hoạt động trong 7 ngày gần nhất.
3. Hệ thống hiển thị: số bài viết, bình luận, cảm xúc, ảnh mới; danh sách thành viên tích cực; nội dung nổi bật.
4. Family Member lọc theo thời gian (tuần/tháng/quý).
5. Family Member bấm vào mục để xem chi tiết hoạt động.

**Alternate Flow**

- **A1, Chưa có hoạt động:** Hiển thị trạng thái trống kèm gợi ý bắt đầu tương tác.
- **A2, Quyền hạn:** Family Member chỉ thấy số liệu tổng hợp; danh sách thành viên tích cực chi tiết chỉ Family Owner.

**Postconditions**

1. Dashboard hiển thị đúng chỉ số theo phạm vi quyền.
2. Số liệu cập nhật tối đa 5 phút một lần.

**Expected Result**

Gia đình theo dõi được sức sống cộng đồng và kịp thời thúc đẩy tương tác.

**Priority**

Medium

---

#### FR-DASH-03 Thống kê sự kiện

**Description**

Hệ thống hiển thị thống kê sự kiện cho Family Owner: số sự kiện đã tổ chức, tỷ lệ tham dự trung bình (RSVP Going / số khách mời), sự kiện sắp diễn ra, xu hướng tổ chức theo thời gian. Dữ liệu từ Events Module, giúp đánh giá hiệu quả các hoạt động gắn kết.

**Primary Actor**

Family Owner

**Supporting Actors**

- Events Module (nguồn dữ liệu)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình có lịch sử sự kiện (FR-EVT-01).

**Trigger**

Family Owner mở trang "Thống kê sự kiện".

**Main Flow**

1. Family Owner mở trang "Thống kê sự kiện".
2. Hệ thống tính toán: tổng sự kiện, tỷ lệ tham dự trung bình, sự kiện sắp tới, tỷ lệ theo loại sự kiện.
3. Hệ thống hiển thị biểu đồ theo thời gian (số sự kiện/tháng).
4. Family Owner lọc theo năm hoặc loại sự kiện.
5. Family Owner bấm vào sự kiện trong biểu đồ để xem chi tiết.

**Alternate Flow**

- **A1, Chưa có sự kiện:** Hiển thị trạng thái trống và gợi ý tạo sự kiện đầu tiên.
- **A2, Không đủ dữ liệu:** Tỷ lệ tham dự chỉ tính cho sự kiện có ≥ 3 khách mời.

**Postconditions**

1. Biểu đồ và chỉ số phản ánh đúng dữ liệu sự kiện.
2. Family Owner đánh giá được mức độ gắn kết qua sự kiện.

**Expected Result**

Family Owner nắm được hiệu quả tổ chức sự kiện và điều chỉnh kế hoạch hoạt động.

**Priority**

Low

---

#### FR-DASH-04 Thống kê nhân khẩu

**Description**

Hệ thống hiển thị thống kê nhân khẩu của gia đình cho Family Owner: phân bố theo độ tuổi (thế hệ), giới tính, địa điểm sinh sống, nghề nghiệp, tình trạng hôn nhân. Số liệu tổng hợp từ hồ sơ thành viên và danh bạ; chỉ hiển thị ở dạng thống kê tổng hợp, không lộ thông tin cá nhân chi tiết.

**Primary Actor**

Family Owner

**Supporting Actors**

- Family Directory Module (nguồn dữ liệu)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Hồ sơ thành viên có dữ liệu nhân khẩu (FR-FG-03, FR-DIR-02/03).

**Trigger**

Family Owner mở trang "Thống kê nhân khẩu".

**Main Flow**

1. Family Owner mở trang "Thống kê nhân khẩu".
2. Hệ thống tổng hợp dữ liệu nhân khẩu từ hồ sơ thành viên.
3. Hệ thống hiển thị biểu đồ: độ tuổi/thế hệ, giới tính, địa điểm, nghề nghiệp, hôn nhân.
4. Family Owner lọc theo nhánh gia đình.
5. Family Owner xem tỷ lệ thiếu dữ liệu để biết mức độ tin cậy.

**Alternate Flow**

- **A1, Thiếu dữ liệu nhân khẩu:** Biểu đồ hiển thị nhóm "Chưa khai báo"; hệ thống gợi ý cập nhật hồ sơ.
- **A2, Bảo mật:** Các nhóm có ít hơn 3 người được gộp vào nhóm "Khác" để tránh nhận diện cá nhân.

**Postconditions**

1. Biểu đồ nhân khẩu hiển thị đúng và ẩn danh.
2. Không có dữ liệu cá nhân chi tiết bị lộ qua thống kê.

**Expected Result**

Family Owner hiểu cơ cấu nhân khẩu gia đình để hoạch định hoạt động phù hợp với từng nhóm.

**Priority**

Medium

---

#### FR-DASH-05 Tạo và xuất báo cáo

**Description**

Hệ thống cho phép Family Owner tạo báo cáo tổng hợp về gia đình: thống kê thành viên, hoạt động cộng đồng, sự kiện, nhân khẩu trong một tài liệu. Báo cáo có thể xuất dạng PDF (báo cáo hoàn chỉnh có tiêu đề, biểu đồ) hoặc CSV (dữ liệu thô). Lịch sử báo cáo được lưu lại và tải lại được.

**Primary Actor**

Family Owner

**Supporting Actors**

- Dashboard Module (nguồn dữ liệu tổng hợp)

**Preconditions**

1. Family Owner đã đăng nhập (FR-US-02).
2. Gia đình có dữ liệu thống kê (FR-DASH-01 đến 04).

**Trigger**

Family Owner mở trang "Báo cáo" và chọn tạo báo cáo mới.

**Main Flow**

1. Family Owner mở trang "Báo cáo".
2. Family Owner chọn loại báo cáo (tổng hợp, cộng đồng, sự kiện, nhân khẩu) và khoảng thời gian.
3. Hệ thống tạo báo cáo từ dữ liệu hiện tại.
4. Family Owner xem trước báo cáo trên màn hình.
5. Family Owner chọn xuất PDF hoặc CSV.
6. Hệ thống sinh file và lưu vào lịch sử báo cáo.

**Alternate Flow**

- **A1, Xuất CSV:** Chỉ xuất dữ liệu thô dạng bảng theo phạm vi đã chọn.
- **A2, Báo cáo lịch sử:** Family Owner mở danh sách báo cáo đã tạo, tải lại file cũ.
- **A3, Xóa báo cáo:** Family Owner xóa báo cáo cũ; hệ thống ghi audit log.
- **A4, Xuất thất bại:** Hệ thống thông báo lỗi và cho phép thử lại.

**Postconditions**

1. File báo cáo được tạo đúng định dạng và nội dung.
2. Báo cáo lưu trong lịch sử với thời điểm tạo.

**Expected Result**

Family Owner xuất được báo cáo chuyên nghiệp phục vụ quản trị gia đình và các mục đích báo cáo khác.

**Priority**

High

---

### 4.4.9 Module 9, Administration

**Tên module:** Administration

**Mục đích:** Cung cấp công cụ quản trị nền tảng cho Administrator: quản lý người dùng toàn hệ thống, kiểm duyệt nội dung, giám sát qua nhật ký kiểm toán, sao lưu/phục hồi dữ liệu và cấu hình hệ thống. Module này đảm bảo hệ thống vận hành an toàn, tuân thủ và ổn định.

**Danh sách chức năng:**

| Chức năng | Mô tả ngắn |
|-----------|------------|
| Quản lý người dùng | Quản lý tài khoản toàn hệ thống: khóa, mở khóa, đổi vai trò. |
| Kiểm duyệt nội dung | Duyệt/gỡ nội dung vi phạm chính sách. |
| Nhật ký kiểm toán | Ghi và tra cứu toàn bộ hoạt động quan trọng. |
| Sao lưu và phục hồi | Sao lưu định kỳ, phục hồi dữ liệu khi cần. |
| Cấu hình hệ thống | Cấu hình tham số vận hành nền tảng. |

---

#### FR-ADM-01 Quản lý người dùng

**Description**

Hệ thống cung cấp cho Administrator màn hình quản lý người dùng toàn nền tảng: tìm kiếm tài khoản, xem chi tiết, khóa/mở khóa tài khoản, đổi vai trò (lên Admin, hạ quyền), ghi chú vi phạm. Administrator không tạo/xóa tài khoản thường (tài khoản tự đăng ký), nhưng có thể vô hiệu hóa tài khoản vi phạm. Mọi thao tác đều được ghi audit log.

**Primary Actor**

Administrator

**Supporting Actors**

- Family Member (đối tượng bị quản lý)

**Preconditions**

1. Administrator đã đăng nhập (FR-US-02).
2. Administrator có vai trò Admin (FR-US-05).

**Trigger**

Administrator mở trang "Quản lý người dùng" trong khu vực quản trị.

**Main Flow**

1. Administrator mở trang "Quản lý người dùng".
2. Hệ thống hiển thị danh sách tài khoản với bộ lọc: trạng thái, vai trò, thời gian tạo.
3. Administrator tìm kiếm tài khoản theo tên/email.
4. Administrator mở chi tiết tài khoản: thông tin cá nhân, vai trò, gia đình tham gia, lịch sử vi phạm.
5. Administrator thực hiện thao tác: khóa, mở khóa, đổi vai trò, thêm ghi chú.
6. Hệ thống yêu cầu xác nhận (với thao tác nhạy cảm), thực hiện và ghi audit log.

**Alternate Flow**

- **A1, Khóa tài khoản:** Tài khoản bị khóa không đăng nhập được (FR-US-02, A3); người dùng nhận email thông báo.
- **A2, Đổi vai trò:** Không thể hạ quyền Admin cuối cùng; hệ thống chặn để đảm bảo luôn có người quản trị.
- **A3, Tìm không thấy:** Hệ thống hiển thị thông báo không có kết quả.

**Postconditions**

1. Thay đổi trạng thái/vai trò có hiệu lực ngay.
2. Mọi thao tác được ghi nhật ký kiểm toán (FR-ADM-03).

**Expected Result**

Administrator kiểm soát được toàn bộ tài khoản nền tảng, xử lý nhanh vi phạm và duy trì an toàn hệ thống.

**Priority**

High

---

#### FR-ADM-02 Kiểm duyệt nội dung

**Description**

Hệ thống cung cấp cho Administrator công cụ kiểm duyệt nội dung: duyệt nội dung bị báo cáo, gỡ nội dung vi phạm chính sách (bài viết, bình luận, ảnh, câu chuyện), cảnh cáo người đăng. Nội dung vi phạm điển hình: ngôn từ thù hận, quấy rối, thông tin sai lệch, nội dung nhạy cảm. Hệ thống hỗ trợ phát hiện tự động từ khóa kết hợp duyệt thủ công.

**Primary Actor**

Administrator

**Supporting Actors**

- Family Member (người báo cáo/người đăng)

**Preconditions**

1. Administrator đã đăng nhập (FR-US-02).
2. Có nội dung bị báo cáo hoặc bị cờ tự động.

**Trigger**

Administrator nhận thông báo nội dung mới bị báo cáo, hoặc mở hàng đợi kiểm duyệt.

**Main Flow**

1. Family Member báo cáo nội dung (chọn lý do từ danh sách).
2. Hệ thống thêm nội dung vào hàng đợi kiểm duyệt kèm mức độ ưu tiên theo lý do.
3. Administrator mở hàng đợi, xem nội dung và ngữ cảnh.
4. Administrator quyết định: giữ nội dung (không vi phạm) hoặc gỡ nội dung (vi phạm).
5. Nếu gỡ, Administrator chọn mức xử lý: cảnh cáo, tạm khóa đăng bài 7 ngày, hoặc chuyển xử lý tài khoản (FR-ADM-01).
6. Hệ thống thông báo kết quả cho người đăng và người báo cáo, ghi audit log.

**Alternate Flow**

- **A1, Phát hiện tự động:** Từ khóa/pattern vi phạm được cờ tự động trước khi người dùng báo cáo.
- **A2, Không đủ thông tin:** Administrator yêu cầu thêm ngữ cảnh; hệ thống giữ nội dung ở trạng thái chờ.
- **A3, Gỡ nhầm:** Administrator khôi phục nội dung đã gỡ trong vòng 30 ngày; hệ thống ghi đầy đủ lịch sử.
- **A4, Báo cáo trùng:** Báo cáo của nhiều người về cùng nội dung được gộp thành một.

**Postconditions**

1. Nội dung vi phạm được gỡ hoặc giữ với quyết định rõ ràng.
2. Toàn bộ quyết định được ghi nhật ký kiểm toán.

**Expected Result**

Nội dung vi phạm được xử lý kịp thời, duy trì môi trường cộng đồng lành mạnh.

**Priority**

High

---

#### FR-ADM-03 Nhật ký kiểm toán (Audit Log)

**Description**

Hệ thống tự động ghi nhật ký kiểm toán (audit log) cho các hoạt động quan trọng: đăng nhập/thất bại đăng nhập, thay đổi quyền, thay đổi dữ liệu gia phả, xóa nội dung, thao tác quản trị, xuất báo cáo. Mỗi bản ghi gồm: thời gian, người thực hiện, hành động, đối tượng, chi tiết thay đổi, địa chỉ IP. Nhật ký không thể chỉnh sửa (append-only) và chỉ Administrator tra cứu.

**Primary Actor**

Administrator

**Supporting Actors**

- Toàn bộ module (nguồn phát sinh sự kiện)

**Preconditions**

1. Administrator đã đăng nhập (FR-US-02).
2. Hệ thống ghi nhận ít nhất một sự kiện quan trọng.

**Trigger**

Sự kiện quan trọng phát sinh (tự động) hoặc Administrator mở trang tra cứu nhật ký.

**Main Flow**

1. Hệ thống ghi nhận sự kiện quan trọng phát sinh từ bất kỳ module nào.
2. Hệ thống lưu bản ghi audit (append-only) với đầy đủ thông tin.
3. Administrator mở trang "Nhật ký kiểm toán".
4. Administrator lọc theo thời gian, người dùng, loại hành động, module.
5. Administrator xem chi tiết bản ghi và xuất nhật ký đã lọc (CSV).

**Alternate Flow**

- **A1, Tra cứu theo tài khoản:** Administrator xem toàn bộ lịch sử hành động của một tài khoản.
- **A2, Xuất nhật ký:** Xuất CSV tối đa 10.000 bản ghi/lần; hệ thống cảnh báo nếu vượt.
- **A3, Lưu trữ lâu dài:** Nhật ký trên 12 tháng chuyển kho lưu trữ lạnh, vẫn tra cứu được.

**Postconditions**

1. Mọi sự kiện quan trọng đều có bản ghi không thể sửa.
2. Administrator tra cứu được lịch sử đầy đủ.

**Expected Result**

Hệ thống có khả năng truy vết đầy đủ mọi hoạt động nhạy cảm, phục vụ điều tra sự cố và tuân thủ.

**Priority**

High

---

#### FR-ADM-04 Sao lưu và phục hồi

**Description**

Hệ thống tự động sao lưu dữ liệu định kỳ (hằng ngày, theo lịch cấu hình) gồm cơ sở dữ liệu và kho file. Administrator có thể xem lịch sử sao lưu, khôi phục dữ liệu từ bản sao lưu về môi trường đích, kiểm tra tính toàn vẹn. Phục hồi là thao tác nhạy cảm, yêu cầu xác nhận kép và ghi audit log.

**Primary Actor**

Administrator

**Supporting Actors**

- System Scheduler (kích hoạt sao lưu định kỳ)

**Preconditions**

1. Administrator đã đăng nhập (FR-US-02).
2. Cấu hình sao lưu đã được thiết lập (FR-ADM-05).

**Trigger**

Đến giờ sao lưu định kỳ (tự động) hoặc Administrator mở trang sao lưu để khôi phục.

**Main Flow**

1. Scheduler kích hoạt quy trình sao lưu theo lịch cấu hình.
2. Hệ thống tạo bản sao lưu database và file, nén và lưu vào kho lưu trữ an toàn.
3. Hệ thống xác minh tính toàn vẹn bản sao lưu (hash) và ghi nhận trạng thái.
4. Administrator mở trang "Sao lưu & Phục hồi" để xem danh sách bản sao lưu và trạng thái.
5. Administrator chọn bản sao lưu và nhấn "Phục hồi".
6. Hệ thống yêu cầu xác nhận kép (nhập từ khóa xác nhận), thực hiện phục hồi lên môi trường đích.
7. Hệ thống ghi audit log và thông báo kết quả.

**Alternate Flow**

- **A1, Sao lưu thất bại:** Hệ thống thử lại tối đa 3 lần, gửi cảnh báo cho Administrator và ghi nhật ký lỗi.
- **A2, Phục hồi thất bại:** Hệ thống giữ nguyên dữ liệu hiện tại, thông báo lỗi chi tiết, không tự ghi đè.
- **A3, Chính sách lưu giữ:** Bản sao lưu giữ tối đa 30 bản; bản cũ nhất tự động bị xóa.

**Postconditions**

1. Tồn tại bản sao lưu hợp lệ mới nhất theo lịch.
2. Quy trình phục hồi hoàn tất hoặc dừng an toàn khi lỗi.

**Expected Result**

Dữ liệu gia đình luôn được bảo vệ, có thể phục hồi trong trường hợp sự cố hoặc lỗi thao tác.

**Priority**

Medium

---

#### FR-ADM-05 Cấu hình hệ thống

**Description**

Hệ thống cung cấp cho Administrator trang cấu hình hệ thống: tham số vận hành (giới hạn tải file, thời gian khóa tài khoản, chính sách mật khẩu), cấu hình thông báo (kênh email/push), cấu hình AI (bật/tắt từng dịch vụ AI), lịch sao lưu. Thay đổi cấu hình có hiệu lực không cần khởi động lại và được ghi audit log.

**Primary Actor**

Administrator

**Supporting Actors**

Không có.

**Preconditions**

1. Administrator đã đăng nhập (FR-US-02).
2. Administrator có vai trò Admin (FR-US-05).

**Trigger**

Administrator mở trang "Cấu hình hệ thống" và thay đổi tham số.

**Main Flow**

1. Administrator mở trang "Cấu hình hệ thống".
2. Hệ thống hiển thị các nhóm cấu hình: chung, bảo mật, thông báo, AI, sao lưu.
3. Administrator sửa các tham số trong phạm vi cho phép.
4. Administrator nhấn "Lưu".
5. Hệ thống kiểm tra tính hợp lệ của giá trị (dải số, định dạng).
6. Hệ thống lưu cấu hình, áp dụng ngay và ghi audit log.

**Alternate Flow**

- **A1, Giá trị không hợp lệ:** Hệ thống báo lỗi theo từng trường, không lưu các giá trị sai.
- **A2, Tắt dịch vụ AI:** Khi tắt một dịch vụ AI, các chức năng tương ứng hiển thị trạng thái không khả dụng (fallback của FR-AI-01 đến FR-AI-05).
- **A3, Khôi phục mặc định:** Administrator khôi phục cấu hình mặc định nhà sản xuất cho một nhóm tham số.

**Postconditions**

1. Cấu hình mới được lưu và áp dụng ngay.
2. Mọi thay đổi được ghi nhật ký kiểm toán.

**Expected Result**

Administrator điều chỉnh hệ thống linh hoạt theo nhu cầu vận hành mà không cần can thiệp mã nguồn.

**Priority**

Medium

---

## 4.5 Ghi chú truy vết (Traceability Notes)

### 4.5.1 Nguyên tắc truy vết

- Mỗi FR có ID duy nhất theo cấu trúc `FR-<MODULE>-<STT>`.
- Mỗi FR ánh xạ tối thiểu **một** Use Case trong Use Case Diagram (FT8-8) và Use Case Specification (FT8-10). Quy ước: FR-xx-yy ↔ UC-xx-yy cùng số thứ tự, giữ nguyên ký hiệu module.
- Mỗi FR có thể liên quan **nhiều** Business Rules (FT8-11); danh sách cụ thể được hoàn thiện trong tài liệu BR.
- Mỗi FR cung cấp tiêu chí cơ sở cho Test Case: luồng chính (main flow) và luồng thay thế (alternate flow) là nguồn trực tiếp cho kịch bản kiểm thử.

### 4.5.2 Ma trận ánh xạ FR ↔ Use Case (gợi ý cho FT8-8)

| Module | FR | Use Case gợi ý |
|--------|-----|----------------|
| User & Security | FR-US-01 | UC-01 Đăng ký tài khoản |
| User & Security | FR-US-02 | UC-02 Đăng nhập |
| User & Security | FR-US-03 | UC-03 Đăng xuất |
| User & Security | FR-US-04 | UC-04 Khôi phục mật khẩu |
| User & Security | FR-US-05 | UC-05 Phân quyền truy cập |
| User & Security | FR-US-06 | UC-06 Quản lý hồ sơ cá nhân |
| User & Security | FR-US-07 | UC-07 Xác thực thành viên |
| Family & Genealogy | FR-FG-01 | UC-08 Quản lý gia đình |
| Family & Genealogy | FR-FG-02 | UC-09 Quản lý nhánh gia đình |
| Family & Genealogy | FR-FG-03 | UC-10 Quản lý thành viên gia đình |
| Family & Genealogy | FR-FG-04 | UC-11 Quản lý quan hệ cha mẹ – con |
| Family & Genealogy | FR-FG-05 | UC-12 Quản lý hôn nhân |
| Family & Genealogy | FR-FG-06 | UC-13 Xem cây gia phả tương tác |
| Family & Genealogy | FR-FG-07 | UC-14 Trực quan hóa quan hệ |
| Family & Genealogy | FR-FG-08 | UC-15 Tra cứu quan hệ |
| Community | FR-COM-01 | UC-16 Đăng và quản lý bài viết |
| Community | FR-COM-02 | UC-17 Bình luận và thả cảm xúc |
| Community | FR-COM-03 | UC-18 Chia sẻ tin tức gia đình |
| Community | FR-COM-04 | UC-19 Chia sẻ hình ảnh |
| Community | FR-COM-05 | UC-20 Thông báo gia đình |
| Events | FR-EVT-01 | UC-21 Tạo sự kiện gia đình |
| Events | FR-EVT-02 | UC-22 Xác nhận tham dự (RSVP) |
| Events | FR-EVT-03 | UC-23 Quản lý người tham gia |
| Events | FR-EVT-04 | UC-24 Thư viện ảnh sự kiện |
| Events | FR-EVT-05 | UC-25 Nhắc nhở sự kiện |
| Family Directory | FR-DIR-01 | UC-26 Xem danh bạ thành viên |
| Family Directory | FR-DIR-02 | UC-27 Quản lý hồ sơ nghề nghiệp |
| Family Directory | FR-DIR-03 | UC-28 Quản lý hồ sơ học vấn |
| Family Directory | FR-DIR-04 | UC-29 Tìm kiếm thành viên |
| Family Heritage | FR-HER-01 | UC-30 Quản lý tư liệu lịch sử |
| Family Heritage | FR-HER-02 | UC-31 Quản lý câu chuyện gia đình |
| Family Heritage | FR-HER-03 | UC-32 Quản lý thành viên tiêu biểu |
| Family Heritage | FR-HER-04 | UC-33 Quản lý thư viện ảnh gia đình |
| Family Heritage | FR-HER-05 | UC-34 Quản lý kho lưu trữ số |
| AI-assisted Services | FR-AI-01 | UC-35 Tìm kiếm ngữ nghĩa bằng AI |
| AI-assisted Services | FR-AI-02 | UC-36 Trợ lý tri thức gia đình |
| AI-assisted Services | FR-AI-03 | UC-37 Giải thích quan hệ gia đình |
| AI-assisted Services | FR-AI-04 | UC-38 Tóm tắt nội dung bằng AI |
| AI-assisted Services | FR-AI-05 | UC-39 Gợi ý thành viên và tài nguyên |
| Dashboard & Reporting | FR-DASH-01 | UC-40 Xem thống kê gia đình |
| Dashboard & Reporting | FR-DASH-02 | UC-41 Xem dashboard cộng đồng |
| Dashboard & Reporting | FR-DASH-03 | UC-42 Xem thống kê sự kiện |
| Dashboard & Reporting | FR-DASH-04 | UC-43 Xem thống kê nhân khẩu |
| Dashboard & Reporting | FR-DASH-05 | UC-44 Tạo và xuất báo cáo |
| Administration | FR-ADM-01 | UC-45 Quản lý người dùng |
| Administration | FR-ADM-02 | UC-46 Kiểm duyệt nội dung |
| Administration | FR-ADM-03 | UC-47 Tra cứu nhật ký kiểm toán |
| Administration | FR-ADM-04 | UC-48 Sao lưu và phục hồi |
| Administration | FR-ADM-05 | UC-49 Cấu hình hệ thống |

> **Lưu ý:** Bảng trên là ánh xạ đề xuất (1 FR ↔ 1 UC) làm định hướng cho FT8-8. Khi dựng Use Case Diagram, một số FR có thể gộp/chẻ thành nhiều Use Case (ví dụ: <<include>> Đăng nhập); ma trận chính thức được hoàn thiện trong FT8-8 và FT8-10.

### 4.5.3 Phụ thuộc giữa các FR

| FR phụ thuộc | Phụ thuộc vào | Lý do |
|--------------|---------------|-------|
| FR-US-02, FR-US-06, ... (mọi FR có Precondition đăng nhập) | FR-US-01, FR-US-02 | Cần tài khoản và xác thực trước. |
| FR-US-07 | FR-FG-01 | Cần gia đình tồn tại để xác thực thành viên. |
| FR-FG-02…FR-FG-08 | FR-FG-01, FR-FG-03 | Cần gia đình và thành viên trước khi quản lý cấu trúc. |
| FR-FG-04, FR-FG-05 | FR-FG-03 | Cần hồ sơ thành viên để thiết lập quan hệ. |
| FR-FG-08 | FR-FG-04, FR-FG-05 | Tra cứu quan hệ dựa trên đồ thị quan hệ. |
| FR-AI-03 | FR-FG-08 | Giải thích AI dựa trên đường đi quan hệ. |
| FR-AI-01, FR-AI-02, FR-AI-04, FR-AI-05 | Dữ liệu từ Module 2, 3, 4, 6 | AI trả lời/gợi ý dựa trên dữ liệu hệ thống. |
| FR-COM-02 | FR-COM-01 | Tương tác cần bài viết tồn tại. |
| FR-EVT-02, FR-EVT-03 | FR-EVT-01 | RSVP và quản lý cần sự kiện tồn tại. |
| FR-EVT-04 | FR-EVT-02 | Tải ảnh cần người dùng tham gia sự kiện. |
| FR-DASH-01…FR-DASH-05 | Dữ liệu Module 2, 3, 4, 5 | Báo cáo tổng hợp từ dữ liệu nghiệp vụ. |
| FR-ADM-04 | FR-ADM-05 | Sao lưu dùng lịch từ cấu hình hệ thống. |

---

## 4.6 Kiểm tra tính đầy đủ (Completeness Check)

### 4.6.1 Đối chiếu với đề tài

| Nhóm chức năng trong đề tài | FR tương ứng | Đầy đủ? |
|------------------------------|--------------|:-------:|
| User registration and authentication | FR-US-01, FR-US-02, FR-US-03, FR-US-04 | ✅ |
| Role-Based Access Control (RBAC) | FR-US-05 | ✅ |
| User profile management | FR-US-06 | ✅ |
| Family member verification | FR-US-07 | ✅ |
| Family management | FR-FG-01 | ✅ |
| Branch management | FR-FG-02 | ✅ |
| Member management | FR-FG-03 | ✅ |
| Parent-child relationship management | FR-FG-04 | ✅ |
| Marriage management | FR-FG-05 | ✅ |
| Interactive genealogy tree | FR-FG-06 | ✅ |
| Relationship visualization | FR-FG-07 | ✅ |
| Relationship query | FR-FG-08 | ✅ |
| Create and manage posts | FR-COM-01 | ✅ |
| Comment and react to posts | FR-COM-02 | ✅ |
| Share family news | FR-COM-03 | ✅ |
| Photo sharing | FR-COM-04 | ✅ |
| Family announcements | FR-COM-05 | ✅ |
| Create family events | FR-EVT-01 | ✅ |
| RSVP management | FR-EVT-02 | ✅ |
| Participant management | FR-EVT-03 | ✅ |
| Event gallery | FR-EVT-04 | ✅ |
| Event reminders | FR-EVT-05 | ✅ |
| Family directory | FR-DIR-01 | ✅ |
| Professional profiles | FR-DIR-02 | ✅ |
| Education profiles | FR-DIR-03 | ✅ |
| Search by profession, location, generation | FR-DIR-04 | ✅ |
| Historical documents | FR-HER-01 | ✅ |
| Family stories | FR-HER-02 | ✅ |
| Outstanding family members | FR-HER-03 | ✅ |
| Photo gallery | FR-HER-04 | ✅ |
| Digital archives | FR-HER-05 | ✅ |
| AI-powered semantic search | FR-AI-01 | ✅ |
| AI family knowledge assistant | FR-AI-02 | ✅ |
| AI relationship explanation | FR-AI-03 | ✅ |
| AI content summarization | FR-AI-04 | ✅ |
| AI recommendation of members and resources | FR-AI-05 | ✅ |
| Family statistics | FR-DASH-01 | ✅ |
| Community activity dashboard | FR-DASH-02 | ✅ |
| Event statistics | FR-DASH-03 | ✅ |
| Family demographics | FR-DASH-04 | ✅ |
| Report generation | FR-DASH-05 | ✅ |
| User management | FR-ADM-01 | ✅ |
| Content moderation | FR-ADM-02 | ✅ |
| Audit logging | FR-ADM-03 | ✅ |
| Backup & Restore | FR-ADM-04 | ✅ |
| System configuration | FR-ADM-05 | ✅ |

**Kết luận:** 100% nhóm chức năng trong đề tài được bao phủ (46/46 mục chức năng). Không có FR nào ngoài phạm vi đề tài.

### 4.6.2 Tiêu chí chất lượng yêu cầu (kiểm chứng theo IEEE 29148)

| Tiêu chí | Đạt? | Ghi chú |
|----------|:----:|---------|
| Không mơ hồ (Unambiguous) | ✅ | Mỗi FR dùng thuật ngữ nhất quán, có giới hạn định lượng (số lượng, ký tự, thời gian) |
| Kiểm chứng được (Verifiable) | ✅ | Main Flow / Expected Result có tiêu chí đo lường |
| Nhất quán (Consistent) | ✅ | Thuật ngữ dùng chung; không FR nào mâu thuẫn |
| Đầy đủ (Complete) | ✅ | Bao phủ 46/46 mục đề tài |
| Truy vết được (Traceable) | ✅ | ID duy nhất, ma trận ánh xạ Use Case (4.5.2) |
| Không trùng lặp | ✅ | Mỗi chức năng xuất hiện đúng một FR; ranh giới module rõ ràng |

### 4.6.3 Giả định khi phân tích

1. **Actor** dựa trên Stakeholder Analysis (FT8-3): Guest, Family Member, Family Owner, Administrator, AI Service, Notification Service. Nếu FT8-3 thay đổi danh sách actor, cập nhật lại Mục 4.2.1.
2. **Một người dùng thuộc nhiều gia đình**, mỗi quan hệ thành viên có vai trò riêng theo gia đình (Owner của gia đình A, Member của gia đình B).
3. **Thành viên "chưa liên kết tài khoản"** tồn tại hợp lệ trong gia phả (do Owner tạo hộ), có thể liên kết tài khoản sau.
4. **Giới hạn định lượng** (kích thước file, số ký tự, thời gian hiệu lực token, số lần thử) là đề xuất hợp lý của BA, được chốt chính thức khi thiết kế chi tiết.
5. **Các số liệu thống kê** hiển thị ẩn danh (anonymized) cho nhóm nhỏ hơn 3 người để tránh nhận diện cá nhân.
6. **AI Service** là dịch vụ nội bộ (self-hosted hoặc API LLM), ranh giới tích hợp cụ thể thuộc NFR (FT8-7) và thiết kế hệ thống.

---

## 4.7 Lịch sử tài liệu

| Phiên bản | Ngày | Người cập nhật | Mô tả |
|-----------|------|----------------|--------|
| 1.0 | 2026-08-03 | Đặng Hoàng Ân | Tạo tài liệu lần đầu: 9 modules, 49 FR, catalog, đặc tả chi tiết, traceability |
