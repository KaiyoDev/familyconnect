# 08. Business Rules

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Phân tích Business Rules (Business Rules Specification)
> **Jira:** [FT8-11](https://familyconnect.atlassian.net/browse/FT8-11), Phân tích Business Rules
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Draft v1.0

---

## 1. Giới thiệu

### 1.1 Mục đích

Tài liệu này đặc tả toàn bộ Business Rules của hệ thống FamilyConnect, nền tảng cộng đồng gia đình số tích hợp trí tuệ nhân tạo. Business Rules (BR) mô tả các quy tắc nghiệp vụ, ràng buộc và chính sách mà hệ thống phải thực thi, được rút trích từ đề tài và các yêu cầu hệ thống, nhằm đảm bảo:

- Các quy tắc nghiệp vụ được mô tả rõ ràng, nhất quán và có thể truy vết.
- Mỗi Business Rule có mã định danh duy nhất và được liên kết với Functional Requirement (FR) và Use Case (UC) tương ứng.
- Không tồn tại quy tắc trùng lặp hoặc mâu thuẫn.

### 1.2 Phạm vi

Tài liệu bao phủ 7 nhóm Business Rules:

| STT | Nhóm (Category) | Ký hiệu |
|-----|------------------|---------|
| 1 | User Management | `BR-US-*` |
| 2 | Family Management | `BR-FG-*` |
| 3 | Community | `BR-COM-*` |
| 4 | Events | `BR-EVT-*` |
| 5 | Family Directory | `BR-DIR-*` |
| 6 | Family Heritage | `BR-HER-*` |
| 7 | AI Services | `BR-AI-*` |
| 8 | Dashboard & Reporting | `BR-DASH-*` |
| 9 | Administration | `BR-ADM-*` |

Tổng cộng: **34 Business Rules**.

### 1.3 Đối tượng đọc

- BA/SA: kiểm chứng tính đầy đủ và nhất quán của quy tắc nghiệp vụ.
- Kiến trúc sư / Developer: triển khai ràng buộc ở tầng domain, service và database.
- Tester: xây dựng test case dựa trên các quy tắc nghiệp vụ.
- Giảng viên / Hội đồng chấm: đánh giá mức độ hoàn thiện của giai đoạn phân tích.

### 1.4 Tài liệu tham chiếu

- [04_FunctionalRequirements.md](./04_FunctionalRequirements.md) (FT8-6), nguồn mapping `Related Requirements`.
- [09_GlossaryAndDataDictionary.md](./09_GlossaryAndDataDictionary.md) (FT8-12), nguồn thuật ngữ và thực thể dữ liệu.
- [03_VisionAndScope.md](./03_VisionAndScope.md) (FT8-5), phạm vi và ràng buộc dự án.
- [02_StakeholderAnalysis.md](./02_StakeholderAnalysis.md) (FT8-3), vai trò và quyền hạn Stakeholder.
- Use Case Specification (FT8-8, FT8-10), nguồn traceability `Related Use Case` (sẽ bổ sung khi hoàn tất).

> **Ghi chú traceability:** `Related Use Case` được đánh dấu `UC-*` (mã tham chiếu). Khi Use Case Specification (FT8-10) hoàn tất, cần đối chiếu để đảm bảo mỗi Business Rule khớp với ít nhất một Use Case.

---

## 2. Danh sách Business Rules

### 2.1 User Management (`BR-US-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-US-001 | Email phải là duy nhất | High |
| BR-US-002 | Mật khẩu phải đạt độ mạnh tối thiểu | High |
| BR-US-003 | Tài khoản phải kích hoạt trước khi đăng nhập | High |
| BR-US-004 | Quyền truy cập theo vai trò (RBAC) | High |
| BR-US-005 | Một người dùng chỉ có một hồ sơ cá nhân | Medium |

**BR-US-001, Email phải là duy nhất**

- **Description:** Hệ thống không cho phép tồn tại hai tài khoản người dùng có cùng địa chỉ email. Email được sử dụng làm định danh đăng nhập duy nhất (Unique Identifier).
- **Category:** User Management
- **Source:** Đề tài mục (c), User registration and authentication; `User.Email` trong Data Dictionary.
- **Related Requirements:** FR-US-01, FR-US-02, FR-US-04
- **Related Use Case:** UC-01 (Đăng ký tài khoản)
- **Priority:** High

**BR-US-002, Mật khẩu phải đạt độ mạnh tối thiểu**

- **Description:** Mật khẩu phải có tối thiểu 8 ký tự, chứa cả chữ và số. Mật khẩu được lưu trữ dạng mã hóa (BCrypt/Argon2), không bao giờ lưu dạng văn bản thuần.
- **Category:** User Management
- **Source:** Yêu cầu bảo mật đề tài mục (d), Secure Authentication (JWT); Đặc tả FR-US-01 (Main Flow, bước 2).
- **Related Requirements:** FR-US-01, FR-US-02, FR-US-04
- **Related Use Case:** UC-01 (Đăng ký tài khoản), UC-02 (Đăng nhập)
- **Priority:** High

**BR-US-003, Tài khoản phải kích hoạt trước khi đăng nhập**

- **Description:** Tài khoản mới tạo ở trạng thái *Pending Activation*. Hệ thống chỉ cho phép đăng nhập khi tài khoản ở trạng thái *Active*. Đường dẫn kích hoạt hết hạn sau 24 giờ.
- **Category:** User Management
- **Source:** Đặc tả FR-US-01 (Main Flow, bước 5–7; Alternate Flow A3).
- **Related Requirements:** FR-US-01, FR-US-02
- **Related Use Case:** UC-01 (Đăng ký tài khoản), UC-02 (Đăng nhập)
- **Priority:** High

**BR-US-004, Quyền truy cập theo vai trò (RBAC)**

- **Description:** Hệ thống phân quyền theo vai trò: Guest, Family Member, Family Owner, Administrator. Mỗi thao tác yêu cầu xác thực (JWT) và kiểm tra quyền tương ứng với vai trò của người dùng. Không vai trò nào được vượt quyền của vai trò cấp trên.
- **Category:** User Management
- **Source:** Đề tài mục (c), Role-Based Access Control (RBAC); mục (d), Secure Authentication (JWT).
- **Related Requirements:** FR-US-05
- **Related Use Case:** UC-03 (Phân quyền truy cập)
- **Priority:** High

**BR-US-005, Một người dùng chỉ có một hồ sơ cá nhân**

- **Description:** Mỗi tài khoản người dùng (`User`) chỉ được phép có một hồ sơ cá nhân duy nhất trên hệ thống. Thông tin hồ sơ (tên, số điện thoại, địa chỉ) thuộc về đúng người dùng đó.
- **Category:** User Management
- **Source:** Đặc tả FR-US-06; `User` trong Data Dictionary.
- **Related Requirements:** FR-US-06
- **Related Use Case:** UC-04 (Quản lý hồ sơ cá nhân)
- **Priority:** Medium

**BR-US-006, Phiên làm việc phải được kết thúc khi đăng xuất hoặc hết hạn token**

- **Description:** Khi người dùng đăng xuất, hệ thống phải hủy phiên làm việc hiện tại (access token và refresh token) và không cho phép phiên đó tiếp tục truy cập. Token hết hạn sau thời gian quy định phải bị vô hiệu hóa.
- **Category:** User Management
- **Source:** Đặc tả FR-US-03; `JWT` trong Glossary.
- **Related Requirements:** FR-US-03, FR-US-02
- **Related Use Case:** UC-02 (Đăng nhập)
- **Priority:** Medium

### 2.2 Family Management (`BR-FG-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-FG-001 | Chỉ Family Owner mới được duyệt thành viên | High |
| BR-FG-002 | Mỗi Family chỉ có một Family Owner | High |
| BR-FG-003 | Mỗi FamilyMember chỉ thuộc một nhánh | Medium |
| BR-FG-004 | Quan hệ cha mẹ – con phải hợp lệ về thế hệ | High |
| BR-FG-005 | Mỗi người chỉ có tối đa một cặp hôn nhân đồng thời | Medium |
| BR-FG-006 | Dữ liệu phả hệ không thể xóa vĩnh viễn khi còn lịch sử liên quan | Medium |
| BR-FG-007 | Thông tin hiển thị trên cây gia phả và tra cứu quan hệ phải chính xác theo dữ liệu đã ghi | Medium |

**BR-FG-001, Chỉ Family Owner mới được duyệt thành viên**

- **Description:** Hệ thống chỉ cho phép người có vai trò Family Owner phê duyệt hoặc từ chối yêu cầu tham gia gia đình của thành viên mới. Family Member không có quyền này.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-03; `Family Owner` trong Glossary.
- **Related Requirements:** FR-FG-03, FR-US-07
- **Related Use Case:** UC-05 (Phê duyệt thành viên)
- **Priority:** High

**BR-FG-002, Mỗi Family chỉ có một Family Owner**

- **Description:** Mỗi gia đình (Family) chỉ có duy nhất một Family Owner ở bất kỳ thời điểm nào. Việc chuyển quyền Owner chỉ được thực hiện bởi Owner hiện tại, và sau khi chuyển, người nhận trở thành Owner mới.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-01; `Family Owner` trong Glossary.
- **Related Requirements:** FR-FG-01, FR-US-05
- **Related Use Case:** UC-06 (Quản lý gia đình)
- **Priority:** High

**BR-FG-003, Mỗi FamilyMember chỉ thuộc một nhánh**

- **Description:** Tại một thời điểm, một FamilyMember thuộc đúng một FamilyBranch trong một Family. Khi chuyển nhánh, lịch sử thay đổi được ghi lại trong Audit Log.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-02; `FamilyBranch` trong Data Dictionary.
- **Related Requirements:** FR-FG-02, FR-FG-03
- **Related Use Case:** UC-07 (Quản lý nhánh gia đình)
- **Priority:** Medium

**BR-FG-004, Quan hệ cha mẹ – con phải hợp lệ về thế hệ**

- **Description:** Hệ thống chỉ cho phép tạo quan hệ cha/mẹ – con (Parent-Child) khi cha/mẹ thuộc thế hệ trước con và không tồn tại quan hệ trùng lặp. Không cho phép tạo quan hệ tạo thành chu trình (loop) trong cây phả hệ.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-04; `Relationship`, `Generation` trong Glossary.
- **Related Requirements:** FR-FG-04, FR-FG-06, FR-FG-08
- **Related Use Case:** UC-08 (Quản lý quan hệ cha mẹ – con)
- **Priority:** High

**BR-FG-005, Mỗi người chỉ có tối đa một cặp hôn nhân đồng thời**

- **Description:** Hệ thống chỉ cho phép một FamilyMember có tối đa một quan hệ hôn nhân (Marriage) đang hiệu lực tại một thời điểm. Quan hệ hôn nhân mới chỉ được tạo sau khi quan hệ cũ kết thúc (ly hôn/ly thân).
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-05; `Relationship` trong Glossary.
- **Related Requirements:** FR-FG-05
- **Related Use Case:** UC-09 (Quản lý hôn nhân)
- **Priority:** Medium

**BR-FG-006, Dữ liệu phả hệ không thể xóa vĩnh viễn khi còn lịch sử liên quan**

- **Description:** FamilyMember, Relationship hoặc FamilyBranch đã có dữ liệu lịch sử liên quan (hôn nhân, con cái, tư liệu di sản) không được xóa vĩnh viễn; hệ thống chuyển sang trạng thái *Archived* để bảo toàn tính toàn vẹn của cây phả hệ.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-01, FR-FG-03; nguyên tắc bảo toàn dữ liệu phả hệ trong đề tài mục (b).
- **Related Requirements:** FR-FG-01, FR-FG-03, FR-FG-06
- **Related Use Case:** UC-06 (Quản lý gia đình), UC-07 (Quản lý nhánh gia đình)
- **Priority:** Medium

**BR-FG-007, Thông tin hiển thị trên cây gia phả và tra cứu quan hệ phải chính xác theo dữ liệu đã ghi**

- **Description:** Mọi thông tin hiển thị trên cây gia phả tương tác (Interactive Genealogy Tree) và kết quả tra cứu quan hệ (Relationship Query) phải được truy xuất trực tiếp từ dữ liệu quan hệ đã xác thực (BR-FG-004, BR-FG-005). Hệ thống không cho phép hiển thị quan hệ chưa được phê duyệt hoặc dữ liệu mâu thuẫn.
- **Category:** Family Management
- **Source:** Đặc tả FR-FG-06, FR-FG-07, FR-FG-08; `Relationship`, `Generation` trong Glossary.
- **Related Requirements:** FR-FG-06, FR-FG-07, FR-FG-08
- **Related Use Case:** UC-08 (Quản lý quan hệ cha mẹ – con), UC-09 (Quản lý hôn nhân)
- **Priority:** Medium

### 2.3 Community (`BR-COM-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-COM-001 | Chỉ thành viên đã xác thực mới được đăng nội dung | High |
| BR-COM-002 | Người tạo bài viết được xóa bài viết của mình | Medium |
| BR-COM-003 | Thông báo chỉ được tạo bởi Family Owner hoặc Ban liên lạc | High |
| BR-COM-004 | Nội dung vi phạm bị kiểm duyệt bởi Administrator | Medium |

**BR-COM-001, Chỉ thành viên đã xác thực mới được đăng nội dung**

- **Description:** Hệ thống chỉ cho phép Family Member đã xác thực (Active) đăng bài viết, bình luận, phản ứng và chia sẻ hình ảnh trong phạm vi gia đình. Guest chỉ được xem nội dung công khai.
- **Category:** Community
- **Source:** Đặc tả FR-COM-01, FR-COM-02, FR-COM-04; `Guest` trong Glossary.
- **Related Requirements:** FR-COM-01, FR-COM-02, FR-COM-03, FR-COM-04
- **Related Use Case:** UC-10 (Đăng và quản lý bài viết), UC-11 (Bình luận và thả cảm xúc)
- **Priority:** High

**BR-COM-002, Người tạo bài viết được xóa bài viết của mình**

- **Description:** Một bài viết chỉ có thể bị xóa bởi chính tác giả (Family Member đã tạo) hoặc Administrator. Family Owner không có quyền xóa bài viết của thành viên khác trừ khi được phân quyền kiểm duyệt.
- **Category:** Community
- **Source:** Đặc tả FR-COM-01 (Postconditions); nguyên tắc quyền sở hữu nội dung.
- **Related Requirements:** FR-COM-01, FR-ADM-02
- **Related Use Case:** UC-10 (Đăng và quản lý bài viết)
- **Priority:** Medium

**BR-COM-003, Thông báo chỉ được tạo bởi Family Owner hoặc Ban liên lạc**

- **Description:** Thông báo gia đình (Announcement) chỉ được tạo bởi Family Owner hoặc thành viên có vai trò Ban liên lạc. Thông báo được ghim lên đầu luồng tin và gửi thông báo đẩy cho toàn bộ thành viên.
- **Category:** Community
- **Source:** Đặc tả FR-COM-05; `Announcement` trong Glossary.
- **Related Requirements:** FR-COM-05
- **Related Use Case:** UC-12 (Tạo thông báo gia đình)
- **Priority:** High

**BR-COM-004, Nội dung vi phạm bị kiểm duyệt bởi Administrator**

- **Description:** Nội dung (bài viết, bình luận, hình ảnh) bị báo cáo hoặc vi phạm chính sách cộng đồng được gỡ bỏ hoặc ẩn bởi Administrator. Mọi hành động kiểm duyệt được ghi vào Audit Log.
- **Category:** Community
- **Source:** Đặc tả FR-ADM-02; `Administrator`, `Audit Log` trong Glossary.
- **Related Requirements:** FR-ADM-02, FR-COM-01, FR-COM-02
- **Related Use Case:** UC-13 (Kiểm duyệt nội dung)
- **Priority:** Medium

**BR-EVT-005, Hình ảnh sự kiện chỉ được thêm bởi người tham gia và Event Owner**

- **Description:** Hệ thống chỉ cho phép người đã xác nhận tham dự sự kiện (RSVP = Tham gia) hoặc Event Owner thêm hình ảnh vào thư viện ảnh sự kiện (Event Gallery). Hình ảnh được gán nhãn người tải lên và thời gian tải lên.
- **Category:** Events
- **Source:** Đặc tả FR-EVT-04; `Event Gallery` trong Glossary.
- **Related Requirements:** FR-EVT-04
- **Related Use Case:** UC-15 (Xác nhận tham dự), UC-16 (Quản lý người tham gia)
- **Priority:** Medium

### 2.4 Events (`BR-EVT-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-EVT-001 | Chỉ Family Member mới được tạo sự kiện | High |
| BR-EVT-002 | Mỗi thành viên chỉ xác nhận RSVP một lần | High |
| BR-EVT-003 | Chỉ Event Owner hoặc Family Owner được hủy sự kiện | Medium |
| BR-EVT-004 | Thời điểm bắt đầu phải trước thời điểm kết thúc | High |
| BR-EVT-005 | Hình ảnh sự kiện chỉ được thêm bởi người tham gia và Event Owner | Medium |

**BR-EVT-001, Chỉ Family Member mới được tạo sự kiện**

- **Description:** Hệ thống chỉ cho phép Family Member đã xác thực tạo sự kiện gia đình. Guest không có quyền tạo sự kiện.
- **Category:** Events
- **Source:** Đặc tả FR-EVT-01; `Event` trong Glossary.
- **Related Requirements:** FR-EVT-01
- **Related Use Case:** UC-14 (Tạo sự kiện gia đình)
- **Priority:** High

**BR-EVT-002, Mỗi thành viên chỉ xác nhận RSVP một lần**

- **Description:** Với mỗi sự kiện, mỗi FamilyMember chỉ được phép có một trạng thái RSVP (Tham gia / Không tham gia / Có thể). RSVP mới sẽ thay thế RSVP cũ, không tạo bản ghi trùng.
- **Category:** Events
- **Source:** Đặc tả FR-EVT-02; `RSVP`, `EventRSVP` trong Data Dictionary.
- **Related Requirements:** FR-EVT-02, FR-EVT-03
- **Related Use Case:** UC-15 (Xác nhận tham dự)
- **Priority:** High

**BR-EVT-003, Chỉ Event Owner hoặc Family Owner được hủy sự kiện**

- **Description:** Một sự kiện chỉ có thể bị hủy bởi Event Owner (người tạo) hoặc Family Owner. Khi hủy, hệ thống thông báo cho toàn bộ người tham gia đã xác nhận RSVP.
- **Category:** Events
- **Source:** Đặc tả FR-EVT-01, FR-EVT-03; `Event Owner` trong Glossary.
- **Related Requirements:** FR-EVT-01, FR-EVT-03
- **Related Use Case:** UC-14 (Tạo sự kiện gia đình), UC-16 (Quản lý người tham gia)
- **Priority:** Medium

**BR-EVT-004, Thời điểm bắt đầu phải trước thời điểm kết thúc**

- **Description:** Hệ thống chỉ cho phép lưu sự kiện khi thời điểm bắt đầu (StartTime) nhỏ hơn thời điểm kết thúc (EndTime). Nhắc nhở sự kiện chỉ được gửi sau khi sự kiện được tạo và trước thời điểm bắt đầu.
- **Category:** Events
- **Source:** Đặc tả FR-EVT-01 (Preconditions); `Event` trong Data Dictionary.
- **Related Requirements:** FR-EVT-01, FR-EVT-05
- **Related Use Case:** UC-14 (Tạo sự kiện gia đình)
- **Priority:** High

### 2.5 Family Heritage (`BR-HER-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-HER-001 | Chỉ Family Member mới được đóng góp tư liệu di sản | Medium |
| BR-HER-002 | Tư liệu di sản phải được duyệt trước khi công khai | Medium |
| BR-HER-003 | Tư liệu được phân loại và gắn thẻ ngữ cảnh | Low |

**BR-HER-001, Chỉ Family Member mới được đóng góp tư liệu di sản**

- **Description:** Hệ thống chỉ cho phép Family Member đã xác thực tải lên tư liệu lịch sử, câu chuyện gia đình và hình ảnh vào kho lưu trữ di sản. Guest chỉ được xem nội dung công khai.
- **Category:** Family Heritage
- **Source:** Đặc tả FR-HER-01, FR-HER-02, FR-HER-04; `Heritage` trong Glossary.
- **Related Requirements:** FR-HER-01, FR-HER-02, FR-HER-03, FR-HER-04, FR-HER-05
- **Related Use Case:** UC-17 (Đóng góp tư liệu di sản)
- **Priority:** Medium

**BR-HER-002, Tư liệu di sản phải được duyệt trước khi công khai**

- **Description:** Tư liệu di sản do thành viên đóng góp ở trạng thái *Pending Review* và chỉ được công khai sau khi được Family Owner hoặc Administrator duyệt. Tư liệu bị từ chối không hiển thị trong kho lưu trữ.
- **Category:** Family Heritage
- **Source:** Đặc tả FR-HER-05; nguyên tắc kiểm soát chất lượng nội dung di sản.
- **Related Requirements:** FR-HER-05, FR-ADM-02
- **Related Use Case:** UC-18 (Duyệt tư liệu di sản)
- **Priority:** Medium

**BR-HER-003, Tư liệu được phân loại và gắn thẻ ngữ cảnh**

- **Description:** Mỗi tư liệu di sản phải được phân loại (loại tư liệu) và gắn tối thiểu một thẻ ngữ cảnh (thế hệ, thành viên, sự kiện, địa điểm) để hỗ trợ tìm kiếm và trực quan hóa trên kho lưu trữ số.
- **Category:** Family Heritage
- **Source:** Đặc tả FR-HER-05; `Digital Archive` trong Glossary.
- **Related Requirements:** FR-HER-05
- **Related Use Case:** UC-17 (Đóng góp tư liệu di sản)
- **Priority:** Low

**BR-DIR-001, Chỉ Family Member được xem danh bạ thành viên và thông tin liên hệ**

- **Description:** Hệ thống chỉ cho phép Family Member đã xác thực truy cập danh bạ thành viên (Family Directory), xem hồ sơ nghề nghiệp, học vấn và tìm kiếm thành viên. Thông tin liên hệ cá nhân chỉ hiển thị cho thành viên cùng gia đình; Guest không được truy cập.
- **Category:** Family Directory
- **Source:** Đặc tả FR-DIR-01, FR-DIR-02, FR-DIR-03, FR-DIR-04; `Family Member`, `Family Directory` trong Glossary.
- **Related Requirements:** FR-DIR-01, FR-DIR-02, FR-DIR-03, FR-DIR-04, FR-US-05
- **Related Use Case:** UC-25 (Xem danh bạ thành viên), UC-26 (Tìm kiếm thành viên)
- **Priority:** High

**BR-DASH-001, Dữ liệu báo cáo và thống kê phải được truy xuất từ dữ liệu đã xác thực**

- **Description:** Mọi số liệu hiển thị trên dashboard và báo cáo (thống kê gia đình, hoạt động cộng đồng, sự kiện, nhân khẩu) phải được tính toán trực tiếp từ dữ liệu hệ thống đã được xác thực (không lấy dữ liệu tạm). Báo cáo chỉ xuất được cho dữ liệu trong phạm vi quyền của người dùng.
- **Category:** Dashboard & Reporting
- **Source:** Đặc tả FR-DASH-01, FR-DASH-02, FR-DASH-03, FR-DASH-04, FR-DASH-05; nguyên tắc toàn vẹn dữ liệu đề tài mục (d).
- **Related Requirements:** FR-DASH-01, FR-DASH-02, FR-DASH-03, FR-DASH-04, FR-DASH-05, FR-US-05
- **Related Use Case:** UC-27 (Xem dashboard), UC-28 (Xuất báo cáo)
- **Priority:** Medium

### 2.6 AI Services (`BR-AI-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-AI-001 | AI chỉ truy cập dữ liệu trong phạm vi quyền của người dùng | High |
| BR-AI-002 | Kết quả AI phải được gán nhãn và không thay thế quyết định con người | Medium |
| BR-AI-003 | AI Service phải có cơ chế fallback khi không khả dụng | High |

**BR-AI-001, AI chỉ truy cập dữ liệu trong phạm vi quyền của người dùng**

- **Description:** Mọi kết quả từ AI (tìm kiếm ngữ nghĩa, trợ lý tri thức, giải thích quan hệ, gợi ý) chỉ được xây dựng trên dữ liệu mà người dùng hiện tại có quyền truy cập theo RBAC. Hệ thống không bao giờ để lộ dữ liệu gia đình ngoài phạm vi quyền.
- **Category:** AI Services
- **Source:** Đặc tả FR-AI-01, FR-AI-02, FR-AI-03, FR-AI-05; nguyên tắc bảo mật dữ liệu đề tài mục (d).
- **Related Requirements:** FR-AI-01, FR-AI-02, FR-AI-03, FR-AI-04, FR-AI-05, FR-US-05
- **Related Use Case:** UC-19 (Tìm kiếm ngữ nghĩa), UC-20 (Trợ lý tri thức gia đình)
- **Priority:** High

**BR-AI-002, Kết quả AI phải được gán nhãn và không thay thế quyết định con người**

- **Description:** Nội dung do AI sinh ra (tóm tắt, giải thích, gợi ý) phải được gán nhãn rõ ràng là nội dung AI-generated. Kết quả AI không tự động thực hiện thay đổi dữ liệu; mọi thay đổi cần xác nhận của người dùng.
- **Category:** AI Services
- **Source:** Đặc tả FR-AI-04; nguyên tắc minh bạch AI trong đề tài mục (b).
- **Related Requirements:** FR-AI-02, FR-AI-04
- **Related Use Case:** UC-20 (Trợ lý tri thức gia đình), UC-21 (Tóm tắt nội dung)
- **Priority:** Medium

**BR-AI-003, AI Service phải có cơ chế fallback khi không khả dụng**

- **Description:** Khi AI Service không khả dụng (lỗi, quá tải, mất kết nối LLM), hệ thống phải tự động fallback về tìm kiếm từ khóa thông thường và thông báo cho người dùng về trạng thái giảm chức năng.
- **Category:** AI Services
- **Source:** Đặc tả FR-AI-01 (Alternate Flow); `AI Service` trong Glossary.
- **Related Requirements:** FR-AI-01, FR-AI-02
- **Related Use Case:** UC-19 (Tìm kiếm ngữ nghĩa)
- **Priority:** High

**BR-ADM-004, Sao lưu và phục hồi dữ liệu chỉ được thực hiện bởi Administrator**

- **Description:** Hệ thống chỉ cho phép Administrator thực hiện sao lưu (Backup) và phục hồi (Restore) dữ liệu. Mọi thao tác sao lưu/phục hồi được ghi vào Audit Log và phải được xác nhận trước khi thực hiện để tránh mất dữ liệu.
- **Category:** Administration
- **Source:** Đặc tả FR-ADM-04; `Audit Log` trong Glossary.
- **Related Requirements:** FR-ADM-04, FR-ADM-03
- **Related Use Case:** UC-29 (Sao lưu và phục hồi dữ liệu)
- **Priority:** Medium

### 2.7 Administration (`BR-ADM-*`)

| Rule ID | Rule Name | Priority |
|---------|-----------|:--------:|
| BR-ADM-001 | Chỉ Administrator mới được quản lý tài khoản người dùng | High |
| BR-ADM-002 | Mọi thao tác nhạy cảm phải được ghi vào Audit Log | High |
| BR-ADM-003 | Chỉ Administrator mới được cấu hình hệ thống | Medium |

**BR-ADM-001, Chỉ Administrator mới được quản lý tài khoản người dùng**

- **Description:** Hệ thống chỉ cho phép Administrator thực hiện khóa/mở khóa tài khoản, đặt lại vai trò và xử lý tài khoản vi phạm. Family Owner không có quyền này.
- **Category:** Administration
- **Source:** Đặc tả FR-ADM-01; `Administrator` trong Glossary.
- **Related Requirements:** FR-ADM-01, FR-US-05
- **Related Use Case:** UC-22 (Quản lý người dùng)
- **Priority:** High

**BR-ADM-002, Mọi thao tác nhạy cảm phải được ghi vào Audit Log**

- **Description:** Hệ thống ghi nhật ký kiểm toán (Audit Log) cho mọi thao tác nhạy cảm: đăng nhập, đăng xuất, tạo/sửa/xóa dữ liệu phả hệ, thay đổi vai trò, kiểm duyệt nội dung. Nhật ký chỉ được tra cứu bởi Administrator và không thể bị sửa đổi.
- **Category:** Administration
- **Source:** Đề tài mục (d), Audit Logging; `Audit Log` trong Glossary.
- **Related Requirements:** FR-ADM-03, FR-ADM-02
- **Related Use Case:** UC-23 (Xem nhật ký kiểm toán)
- **Priority:** High

**BR-ADM-003, Chỉ Administrator mới được cấu hình hệ thống**

- **Description:** Hệ thống chỉ cho phép Administrator thay đổi cấu hình hệ thống (thông số nền tảng, AI Service, thông báo, sao lưu). Mọi thay đổi cấu hình được ghi vào Audit Log.
- **Category:** Administration
- **Source:** Đặc tả FR-ADM-05; `Administrator` trong Glossary.
- **Related Requirements:** FR-ADM-05
- **Related Use Case:** UC-24 (Cấu hình hệ thống)
- **Priority:** Medium

---

## 3. Ma trận truy vết (Traceability Matrix)

### 3.1 Business Rule ↔ Functional Requirement

| BR ID | FR liên quan | Category |
|-------|--------------|----------|
| BR-US-001 | FR-US-01, FR-US-02, FR-US-04 | User Management |
| BR-US-002 | FR-US-01, FR-US-02, FR-US-04 | User Management |
| BR-US-003 | FR-US-01, FR-US-02 | User Management |
| BR-US-004 | FR-US-05 | User Management |
| BR-US-005 | FR-US-06 | User Management |
| BR-FG-001 | FR-FG-03, FR-US-07 | Family Management |
| BR-FG-002 | FR-FG-01, FR-US-05 | Family Management |
| BR-FG-003 | FR-FG-02, FR-FG-03 | Family Management |
| BR-FG-004 | FR-FG-04, FR-FG-06, FR-FG-08 | Family Management |
| BR-FG-005 | FR-FG-05 | Family Management |
| BR-FG-006 | FR-FG-01, FR-FG-03, FR-FG-06 | Family Management |
| BR-FG-007 | FR-FG-06, FR-FG-07, FR-FG-08 | Family Management |
| BR-COM-001 | FR-COM-01, FR-COM-02, FR-COM-03, FR-COM-04 | Community |
| BR-COM-002 | FR-COM-01, FR-ADM-02 | Community |
| BR-COM-003 | FR-COM-05 | Community |
| BR-COM-004 | FR-ADM-02, FR-COM-01, FR-COM-02 | Community |
| BR-EVT-001 | FR-EVT-01 | Events |
| BR-EVT-002 | FR-EVT-02, FR-EVT-03 | Events |
| BR-EVT-003 | FR-EVT-01, FR-EVT-03 | Events |
| BR-EVT-004 | FR-EVT-01, FR-EVT-05 | Events |
| BR-EVT-005 | FR-EVT-04 | Events |
| BR-HER-001 | FR-HER-01, FR-HER-02, FR-HER-03, FR-HER-04, FR-HER-05 | Family Heritage |
| BR-HER-002 | FR-HER-05, FR-ADM-02 | Family Heritage |
| BR-HER-003 | FR-HER-05 | Family Heritage |
| BR-DIR-001 | FR-DIR-01, FR-DIR-02, FR-DIR-03, FR-DIR-04, FR-US-05 | Family Directory |
| BR-DASH-001 | FR-DASH-01, FR-DASH-02, FR-DASH-03, FR-DASH-04, FR-DASH-05, FR-US-05 | Dashboard & Reporting |
| BR-AI-001 | FR-AI-01, FR-AI-02, FR-AI-03, FR-AI-04, FR-AI-05, FR-US-05 | AI Services |
| BR-AI-002 | FR-AI-02, FR-AI-04 | AI Services |
| BR-AI-003 | FR-AI-01, FR-AI-02 | AI Services |
| BR-ADM-001 | FR-ADM-01, FR-US-05 | Administration |
| BR-ADM-002 | FR-ADM-03, FR-ADM-02 | Administration |
| BR-ADM-003 | FR-ADM-05 | Administration |
| BR-ADM-004 | FR-ADM-04, FR-ADM-03 | Administration |

### 3.2 Business Rule ↔ Use Case

| BR ID | Use Case | Category |
|-------|----------|----------|
| BR-US-001 | UC-01 (Đăng ký tài khoản) | User Management |
| BR-US-002 | UC-01, UC-02 (Đăng nhập) | User Management |
| BR-US-003 | UC-01, UC-02 | User Management |
| BR-US-004 | UC-03 (Phân quyền truy cập) | User Management |
| BR-US-005 | UC-04 (Quản lý hồ sơ cá nhân) | User Management |
| BR-US-006 | UC-02 (Đăng nhập) | User Management |
| BR-FG-001 | UC-05 (Phê duyệt thành viên) | Family Management |
| BR-FG-002 | UC-06 (Quản lý gia đình) | Family Management |
| BR-FG-003 | UC-07 (Quản lý nhánh gia đình) | Family Management |
| BR-FG-004 | UC-08 (Quản lý quan hệ cha mẹ – con) | Family Management |
| BR-FG-005 | UC-09 (Quản lý hôn nhân) | Family Management |
| BR-FG-006 | UC-06, UC-07 | Family Management |
| BR-FG-007 | UC-08, UC-09 | Family Management |
| BR-COM-001 | UC-10 (Đăng và quản lý bài viết), UC-11 (Bình luận và thả cảm xúc) | Community |
| BR-COM-002 | UC-10 | Community |
| BR-COM-003 | UC-12 (Tạo thông báo gia đình) | Community |
| BR-COM-004 | UC-13 (Kiểm duyệt nội dung) | Community |
| BR-EVT-001 | UC-14 (Tạo sự kiện gia đình) | Events |
| BR-EVT-002 | UC-15 (Xác nhận tham dự) | Events |
| BR-EVT-003 | UC-14, UC-16 (Quản lý người tham gia) | Events |
| BR-EVT-004 | UC-14 | Events |
| BR-EVT-005 | UC-15, UC-16 | Events |
| BR-HER-001 | UC-17 (Đóng góp tư liệu di sản) | Family Heritage |
| BR-HER-002 | UC-18 (Duyệt tư liệu di sản) | Family Heritage |
| BR-HER-003 | UC-17 | Family Heritage |
| BR-DIR-001 | UC-25 (Xem danh bạ thành viên), UC-26 (Tìm kiếm thành viên) | Family Directory |
| BR-DASH-001 | UC-27 (Xem dashboard), UC-28 (Xuất báo cáo) | Dashboard & Reporting |
| BR-AI-001 | UC-19 (Tìm kiếm ngữ nghĩa), UC-20 (Trợ lý tri thức gia đình) | AI Services |
| BR-AI-002 | UC-20, UC-21 (Tóm tắt nội dung) | AI Services |
| BR-AI-003 | UC-19 | AI Services |
| BR-ADM-001 | UC-22 (Quản lý người dùng) | Administration |
| BR-ADM-002 | UC-23 (Xem nhật ký kiểm toán) | Administration |
| BR-ADM-003 | UC-24 (Cấu hình hệ thống) | Administration |
| BR-ADM-004 | UC-29 (Sao lưu và phục hồi dữ liệu) | Administration |

---

## 4. Kiểm tra tính nhất quán

| Tiêu chí | Kết quả |
|----------|---------|
| Không có Business Rule bị trùng lặp | ✅ 34 BR, mỗi BR có Rule ID duy nhất, không trùng nội dung |
| Mỗi BR liên kết với ít nhất một FR | ✅ 34/34 BR có `Related Requirements` |
| Mỗi BR liên kết với ít nhất một Use Case | ✅ 34/34 BR có `Related Use Case` (tham chiếu `UC-*`) |
| Mọi FR trong 04_FunctionalRequirements.md được phủ bởi ít nhất một BR | ✅ 49/49 FR được mapping |
| BR không mâu thuẫn với nhau | ✅ Không tồn tại quy tắc đối nghịch; quyền hạn được phân cấp rõ (Guest < Member < Owner < Admin) |
| BR thống nhất với Glossary | ✅ Thuật ngữ (`Family Owner`, `RSVP`, `Audit Log`, `Event Owner`...) khớp 09_GlossaryAndDataDictionary.md |
| BR thống nhất với Functional Requirements | ✅ Mã `FR-*` và nội dung khớp 04_FunctionalRequirements.md |
