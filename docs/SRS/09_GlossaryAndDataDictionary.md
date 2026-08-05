# 09. Glossary and Data Dictionary

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Glossary & Data Dictionary
> **Jira:** [FT8-12](https://familyconnect.atlassian.net/browse/FT8-12), Xây dựng Glossary & Data Dictionary
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Final v1.0

---

## 1. Glossary (Thuật ngữ hệ thống)

Tài liệu này định nghĩa các thuật ngữ, khái niệm cốt lõi được sử dụng xuyên suốt trong hệ thống FamilyConnect nhằm đảm bảo sự thống nhất về mặt ý nghĩa giữa các bên liên quan (Developers, Stakeholders, Users).

| Term | Definition | Related Modules | Notes |
| :--- | :--- | :--- | :--- |
| **Family** | Đơn vị gia đình/dòng họ lớn nhất trên hệ thống, bao gồm tập hợp các thành viên có liên quan về huyết thống hoặc hôn nhân. | Family & Genealogy Management | Mỗi Family có thể chứa nhiều Family Branch. |
| **Family Branch** | Chi/nhánh trong dòng họ (ví dụ: Chi trưởng, Chi thứ), giúp phân loại và quản lý các nhánh con của gia đình lớn. | Family & Genealogy Management | Phân nhánh theo phả hệ. |
| **Family Owner** | Người khởi tạo hoặc giữ quyền quản trị cao nhất của một gia đình/dòng họ trên hệ thống, có quyền duyệt thành viên và phân quyền. | User & Security, Administration | Có toàn quyền quản lý dữ liệu phả hệ của Family. |
| **Family Member** | Một cá nhân (còn sống hoặc đã mất) nằm trong cây gia phả. Có thể liên kết với một tài khoản người dùng (`User`) hoặc chỉ tồn tại dưới dạng hồ sơ dữ liệu. | Family & Genealogy Management, Family Directory | Không bắt buộc mọi Family Member phải có tài khoản đăng nhập (`User`). |
| **Generation** | Thế hệ/đời trong dòng họ (ví dụ: Đời thứ 1, Đời thứ 2). Được tính toán dựa trên mối quan hệ cha/mẹ - con trên cây phả hệ. | Family & Genealogy Management, Dashboard | Dùng để truy vấn và phân loại thành viên. |
| **Relationship** | Mối quan hệ giữa hai thành viên trong gia đình, bao gồm quan hệ huyết thống (Cha-Con, Mẹ-Con) và quan hệ hôn nhân (Vợ-Chồng). | Family & Genealogy Management | Được mô hình hóa dưới dạng đồ thị (Graph Data). |
| **Heritage** | Di sản gia đình, bao gồm tài liệu lịch sử, câu chuyện dòng họ, hình ảnh tư liệu và thông tin các thành viên danh nhân/tiêu biểu. | Family Heritage | Dùng để lưu trữ và bảo tồn truyền thống gia đình. |
| **Event** | Sự kiện của gia đình (ví dụ: Lễ giỗ tổ, Mừng thọ, Họp mặt dòng họ, Sinh nhật). | Events | Hỗ trợ điểm danh (RSVP), nhắc lịch và đính kèm bộ sưu tập ảnh. |
| **Community** | Không gian tương tác cộng đồng nội bộ gia đình, nơi các thành viên chia sẻ bài viết, hình ảnh, thông báo và thảo luận. | Community | Giúp tăng cường kết nối giữa các thế hệ. |
| **Announcement** | Thông báo chính thức từ Ban liên lạc/Family Owner đến toàn thể thành viên trong gia đình (ví dụ: Thông báo quỹ, việc hỷ/hiếu). | Community | Thường được ghim hoặc gửi thông báo đẩy. |
| **Administrator** | Quản trị viên hệ thống (System Admin), có quyền quản lý toàn bộ tài khoản, kiểm duyệt nội dung, xem nhật ký hệ thống và cấu hình server. | Administration | Phân biệt với Family Owner (chỉ quản lý trong phạm vi 1 Family). |
| **AI Assistant** | Trợ lý trí tuệ nhân tạo tích hợp trong hệ thống, hỗ trợ tìm kiếm ngữ nghĩa, giải thích mối quan hệ gia phả, tóm tắt nội dung và đưa ra gợi ý. | AI-assisted Services | Sử dụng công nghệ LLM và Semantic Search. |
| **LLM** | (Large Language Model) Mô hình ngôn ngữ lớn làm nền tảng cho AI Assistant: hiểu câu hỏi, sinh câu trả lời, tóm tắt và giải thích quan hệ. | AI-assisted Services | Chi phí gọi API LLM cần được tối ưu hóa theo ràng buộc nguồn lực. |
| **Guest** | Người chưa đăng ký/đăng nhập. Chỉ xem thông tin giới thiệu và đăng ký tài khoản. | User & Security | Actor đầu tiên trong vòng đời người dùng; sau khi đăng ký trở thành Family Member. |
| **Event Owner** | Người tạo ra sự kiện, giữ quyền quản lý sự kiện đó (sửa, hủy, quản lý người tham gia). Family Owner có quyền quản lý mọi sự kiện trong gia đình. | Events | Khác với Family Owner, phạm vi chỉ trong một sự kiện. |
| **RSVP** | Trạng thái xác nhận tham gia sự kiện của thành viên (Tham gia / Không tham gia / Có thể). | Events | Viết tắt từ tiếng Pháp "RÉpondez S'il Vous Plaît". |
| **RBAC** | (Role-Based Access Control) Cơ chế kiểm soát truy cập dựa trên vai trò của người dùng trong hệ thống (Admin, Family Owner, Member, Guest). | User & Security | Đảm bảo tính bảo mật và riêng tư dữ liệu gia đình. |
| **JWT** | (JSON Web Token) Cơ chế xác thực: hệ thống cấp access token + refresh token khi đăng nhập thành công để duy trì phiên làm việc an toàn. | User & Security | Bắt buộc theo ràng buộc công nghệ (Technology Constraints). |
| **AI Service** | Dịch vụ trí tuệ nhân tạo nội bộ thực hiện embedding, xếp hạng ngữ nghĩa, trả lời truy vấn và gợi ý. | AI-assisted Services | Được gọi qua RESTful API; có cơ chế fallback về tìm kiếm từ khóa khi không khả dụng. |
| **Semantic Search** | Tìm kiếm ngữ nghĩa: hiểu ý nghĩa của truy vấn ngôn ngữ tự nhiên thay vì chỉ khớp từ khóa. | AI-assisted Services | Sử dụng embedding + chỉ mục ngữ nghĩa của dữ liệu gia đình. |
| **Notification Service** | Dịch vụ gửi thông báo (in-app, email, push) hỗ trợ các luồng xử lý bất đồng bộ (thư mời, nhắc sự kiện, xác nhận tài khoản). | User & Security, Community, Events | Actor hỗ trợ (Supporting Actor) trong nhiều use case. |
| **Audit Log** | Nhật ký kiểm toán ghi lại toàn bộ thao tác quan trọng (đăng nhập, tạo/sửa/xóa dữ liệu nhạy cảm, thay đổi vai trò) phục vụ truy vết và tuân thủ. | Administration | Chỉ Administrator được tra cứu. |
| **Digital Archive** | Kho lưu trữ số: lưu trữ có cấu trúc, phân loại và tìm kiếm toàn bộ tư liệu di sản gia đình. | Family Heritage | Thuộc khái niệm Heritage; hỗ trợ xem trước ảnh/PDF. |

---

## 2. Data Dictionary (Từ điển dữ liệu)

Dưới đây là chi tiết các Thực thể dữ liệu (Entities) chính và danh sách thuộc tính (Attributes) trong hệ thống FamilyConnect.

### Danh sách các Entity chính:
1. **User**: Lưu trữ thông tin tài khoản đăng nhập và xác thực.
2. **Family**: Thông tin dòng họ/gia đình.
3. **FamilyBranch**: Thông tin các chi/nhánh trong gia đình.
4. **FamilyMember**: Hồ sơ chi tiết của thành viên trong cây phả hệ.
5. **Relationship**: Mối quan hệ giữa các thành viên (Parent-Child, Marriage).
6. **Post**: Bài viết tương tác cộng đồng.
7. **Comment**: Bình luận trong bài viết.
8. **Event**: Sự kiện gia đình.
9. **EventRSVP**: Xác nhận tham dự sự kiện.
10. **HeritageItem**: Tài liệu, câu chuyện, tư liệu di sản gia đình.
11. **AuditLog**: Nhật ký thao tác hệ thống dành cho Admin.
12. **Notification**: Thông báo đến người dùng (in-app/email/push).

> **Ghi chú thiết kế:** Danh sách trên là các thực thể cốt lõi (core entities) ở mức khái niệm. Khi triển khai chi tiết (Database Design, Work Package 1), mỗi Entity có thể được chuẩn hóa thành nhiều bảng vật lý; ví dụ hồ sơ nghề nghiệp/học vấn của Family Directory (`Profession`, `Education`) có thể tách thành các bảng riêng (EmploymentProfile, EducationProfile) để hỗ trợ nhiều vị trí/công ty và nhiều bằng cấp, thay vì lưu cố định một giá trị trên FamilyMember.

---

### Chi tiết các Entity và thuộc tính (Attribute Details)

#### 2.1. Entity: `User`
Lưu trữ thông tin tài khoản người dùng đăng nhập hệ thống.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `UserID` | UUID / INT | Mã định danh duy nhất của người dùng | Yes | Primary Key | `usr_98b12f4a` |
| `FullName` | VARCHAR(100) | Họ và tên đầy đủ | Yes | Non-empty | `"Nguyễn Văn An"` |
| `Email` | VARCHAR(150) | Địa chỉ Email đăng nhập | Yes | Unique, Email format | `"an.nguyen@gmail.com"` |
| `Password` | VARCHAR(255) | Mật khẩu đã được mã hóa | Yes | Hashed (BCrypt/Argon2) | `"$2a$12$eImi..."` |
| `Phone` | VARCHAR(20) | Số điện thoại liên lạc | No | Phone number format | `"0912345678"` |
| `Role` | VARCHAR(30) | Vai trò hệ thống (`ADMIN`, `USER`) | Yes | Enum: `ADMIN`, `USER` | `"USER"` |
| `Status` | VARCHAR(20) | Trạng thái tài khoản | Yes | Enum: `PENDING`, `ACTIVE`, `INACTIVE`, `BLOCKED`, `SUSPENDED` | `"ACTIVE"` |
| `CreatedAt` | TIMESTAMP | Thời gian tạo tài khoản | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 10:00:00` |

---

#### 2.2. Entity: `Family`
Lưu trữ thông tin tổng quan của một gia đình/dòng họ.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `FamilyID` | UUID / INT | Mã định danh duy nhất của Family | Yes | Primary Key | `fam_10293847` |
| `FamilyName` | VARCHAR(150) | Tên dòng họ / gia đình | Yes | Non-empty | `"Dòng Họ Nguyễn Văn (Đồng Nai)"` |
| `Description` | TEXT | Mô tả ngắn về lịch sử/truyền thống | No | Max 2000 chars | `"Dòng họ gốc tại..."` |
| `CreatedBy` | UUID / INT | ID của người khởi tạo (Family Owner) | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Status` | VARCHAR(20) | Trạng thái gia đình | Yes | Enum: `ACTIVE`, `INACTIVE` | `"ACTIVE"` |
| `CreatedAt` | TIMESTAMP | Ngày khởi tạo Family trên hệ thống | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 10:30:00` |

---

#### 2.3. Entity: `FamilyBranch`
Lưu trữ thông tin các chi/nhánh trong một gia đình (ví dụ: Chi trưởng, Chi thứ).

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `BranchID` | UUID / INT | Mã định danh duy nhất của nhánh | Yes | Primary Key | `brn_0012` |
| `FamilyID` | UUID / INT | Thuộc dòng họ nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `BranchName` | VARCHAR(150) | Tên chi/nhánh | Yes | Non-empty | `"Chi trưởng"` |
| `FounderID` | UUID / INT | Thành viên khai sáng nhánh (nếu có) | No | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8400` |
| `Description` | TEXT | Mô tả lịch sử của nhánh | No | Max 2000 chars | `"Nhánh con trưởng, định cư tại..."` |
| `CreatedAt` | TIMESTAMP | Ngày khởi tạo nhánh trên hệ thống | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 10:40:00` |

---

#### 2.4. Entity: `FamilyMember`
Lưu trữ thông tin hồ sơ của cá nhân trong phả hệ.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `MemberID` | UUID / INT | Mã định danh thành viên phả hệ | Yes | Primary Key | `mem_550e8400` |
| `FamilyID` | UUID / INT | Thuộc dòng họ nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `BranchID` | UUID / INT | Thuộc chi/nhánh nào | No | Foreign Key -> `FamilyBranch.BranchID` | `brn_0012` |
| `UserID` | UUID / INT | Liên kết tài khoản đăng nhập (nếu có) | No | Foreign Key -> `User.UserID`, Unique | `usr_98b12f4a` |
| `FullName` | VARCHAR(100) | Họ tên đầy đủ trong phả hệ | Yes | Non-empty | `"Nguyễn Văn Đức"` |
| `Gender` | VARCHAR(10) | Giới tính | Yes | Enum: `MALE`, `FEMALE`, `OTHER` | `"MALE"` |
| `DateOfBirth` | DATE | Ngày tháng năm sinh | No | Valid Date | `1985-05-20` |
| `IsAlive` | BOOLEAN | Còn sống hay đã mất | Yes | Default: `TRUE` | `TRUE` |
| `DateOfDeath` | DATE | Ngày mất (nếu IsAlive = FALSE) | No | Date >= DateOfBirth | `2020-01-15` |
| `Generation` | INT | Đời thứ mấy trong gia đình | Yes | Positive Integer (>= 1) | `3` |
| `Status` | VARCHAR(20) | Trạng thái thành viên trong gia đình | Yes | Enum: `PENDING`, `ACTIVE`, `SUSPENDED` | `"ACTIVE"` |
| `Profession` | VARCHAR(100) | Nghề nghiệp hiện tại/trước đây | No | Max 100 chars | `"Kỹ sư Phần mềm"` |
| `Education` | VARCHAR(100) | Trình độ học vấn | No | Max 100 chars | `"Đại học"` |

---

#### 2.5. Entity: `Relationship`
Mô tả mối quan hệ giữa hai thành viên trong cây phả hệ (Graph Node Connection).

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `RelationshipID`| UUID / INT | Mã định danh mối quan hệ | Yes | Primary Key | `rel_99887766` |
| `FromMemberID` | UUID / INT | ID thành viên nguồn (ví dụ: Cha/Mẹ/Chồng) | Yes | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8400` |
| `ToMemberID` | UUID / INT | ID thành viên đích (ví dụ: Con/Vợ) | Yes | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8401` |
| `Type` | VARCHAR(30) | Loại quan hệ | Yes | Enum: `PARENT_CHILD`, `MARRIAGE` | `"PARENT_CHILD"` |
| `Notes` | VARCHAR(255) | Ghi chú thêm (vd: Con nuôi, Đã ly hôn) | No | Max 255 chars | `"Con ruột"` |

---

#### 2.6. Entity: `Event`
Lưu trữ thông tin sự kiện gia đình.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `EventID` | UUID / INT | Mã định danh sự kiện | Yes | Primary Key | `evt_11223344` |
| `FamilyID` | UUID / INT | Sự kiện thuộc gia đình nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `Title` | VARCHAR(200) | Tên sự kiện | Yes | Non-empty | `"Lễ Giỗ Tổ Dòng Họ 2026"` |
| `Description` | TEXT | Nội dung chi tiết sự kiện | No | Max 5000 chars | `"Kính mời toàn thể..."` |
| `Location` | VARCHAR(255) | Địa điểm tổ chức | No | Max 255 chars | `"Nhà thờ tổ, Từ Liêm, Hà Nội"` |
| `StartTime` | TIMESTAMP | Thời gian bắt đầu | Yes | Valid Timestamp | `2026-09-10 08:00:00` |
| `EndTime` | TIMESTAMP | Thời gian kết thúc | No | Timestamp > StartTime | `2026-09-10 12:00:00` |
| `Type` | VARCHAR(30) | Loại sự kiện | Yes | Enum: `MEETING`, `WEDDING`, `MEMORIAL`, `BIRTHDAY`, `TRIP`, `OTHER` | `"MEMORIAL"` |
| `Status` | VARCHAR(20) | Trạng thái sự kiện | Yes | Enum: `OPEN`, `CANCELLED`, `COMPLETED` | `"OPEN"` |
| `CreatedBy` | UUID / INT | Người tạo sự kiện (Event Owner) | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |

---

#### 2.7. Entity: `HeritageItem`
Lưu trữ tài liệu lịch sử, câu chuyện, tư liệu di sản.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `HeritageID` | UUID / INT | Mã định danh di sản/tư liệu | Yes | Primary Key | `her_77665544` |
| `FamilyID` | UUID / INT | Thuộc gia đình nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `BranchID` | UUID / INT | Nhánh liên quan (để lọc theo nhánh) | No | Foreign Key -> `FamilyBranch.BranchID` | `brn_0012` |
| `Title` | VARCHAR(200) | Tiêu đề di sản/câu chuyện | Yes | Non-empty | `"Sắc phong vua ban năm 1890"` |
| `Type` | VARCHAR(30) | Loại tư liệu | Yes | Enum: `DOCUMENT`, `IMAGE`, `MAP`, `ARTIFACT`, `STORY` | `"DOCUMENT"` |
| `Category` | VARCHAR(50) | Phân loại nội dung | Yes | Enum: `STORY`, `DOCUMENT`, `OUTSTANDING_MEMBER` | `"DOCUMENT"` |
| `Period` | VARCHAR(100) | Niên đại / giai đoạn lịch sử | No | Max 100 chars | `"Thời Nguyễn (1802–1945)"` |
| `Content` | TEXT | Nội dung chi tiết văn bản/câu chuyện | No | Long text | `"Năm Kỷ Hợi, gia tộc..."` |
| `Status` | VARCHAR(20) | Trạng thái xuất bản | Yes | Enum: `DRAFT`, `PUBLISHED`, `REMOVED` | `"PUBLISHED"` |
| `MediaURL` | VARCHAR(500) | Đường dẫn ảnh/file tư liệu lưu trên Cloud | No | Valid URL | `"https://s3.amazonaws.com/..."` |
| `CreatedAt` | TIMESTAMP | Ngày đăng tài liệu | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 11:00:00` |

---

#### 2.8. Entity: `Post`
Bài viết trong luồng cộng đồng của gia đình.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `PostID` | UUID / INT | Mã định danh bài viết | Yes | Primary Key | `pst_55667788` |
| `FamilyID` | UUID / INT | Bài viết thuộc gia đình nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `AuthorID` | UUID / INT | Người đăng bài (Family Member) | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Content` | TEXT | Nội dung văn bản của bài viết | Yes | ≤ 2000 ký tự, Non-empty | `"Họp mặt đầu năm..."` |
| `VisibilityScope` | VARCHAR(20) | Phạm vi hiển thị | Yes | Enum: `FAMILY`, `BRANCH` | `"FAMILY"` |
| `BranchID` | UUID / INT | Nhánh được hiển thị (nếu VisibilityScope = BRANCH) | No | Foreign Key -> `FamilyBranch.BranchID` | `brn_0012` |
| `Status` | VARCHAR(20) | Trạng thái bài viết | Yes | Enum: `PUBLISHED`, `DRAFT`, `REMOVED` | `"PUBLISHED"` |
| `MediaURLs` | JSON / ARRAY | Danh sách ảnh/video đính kèm (tối đa 10 file) | No | Max 10 items | `["url1","url2"]` |
| `CreatedAt` | TIMESTAMP | Thời điểm đăng bài | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-05 09:15:00` |
| `UpdatedAt` | TIMESTAMP | Thời điểm sửa gần nhất | No | >= CreatedAt | `2026-08-05 09:30:00` |

---

#### 2.9. Entity: `Comment`
Bình luận trên một bài viết.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `CommentID` | UUID / INT | Mã định danh bình luận | Yes | Primary Key | `cmt_12345678` |
| `PostID` | UUID / INT | Bài viết chứa bình luận | Yes | Foreign Key -> `Post.PostID` | `pst_55667788` |
| `AuthorID` | UUID / INT | Người bình luận | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Content` | VARCHAR(1000) | Nội dung bình luận | Yes | Non-empty, ≤ 1000 ký tự | `"Chúc mừng năm mới!"` |
| `CreatedAt` | TIMESTAMP | Thời điểm bình luận | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-05 09:20:00` |

> **Ghi chú:** Cảm xúc (React: like, yêu thích, buồn...) và chia sẻ tin tức có thể được mô hình hóa dưới dạng các bảng riêng (`PostReaction`, `Share`) hoặc trường đếm trên `Post`, quyết định chi tiết thuộc Database Design.

---

#### 2.10. Entity: `EventRSVP`
Xác nhận tham dự sự kiện của từng thành viên/khách mời.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `RSVPID` | UUID / INT | Mã định danh xác nhận tham dự | Yes | Primary Key | `rsv_44332211` |
| `EventID` | UUID / INT | Sự kiện liên quan | Yes | Foreign Key -> `Event.EventID` | `evt_11223344` |
| `MemberID` | UUID / INT | Thành viên gia đình xác nhận (NULL nếu là khách ngoài) | No | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8400` |
| `GuestEmail` | VARCHAR(150) | Email khách ngoài gia đình | No | Email format, tối đa 50 khách/sự kiện | `"friend@example.com"` |
| `Response` | VARCHAR(20) | Trạng thái xác nhận | Yes | Enum: `GOING`, `NOT_GOING`, `MAYBE`, `NO_RESPONSE` | `"GOING"` |
| `RespondedAt` | TIMESTAMP | Thời điểm xác nhận | No | Valid Timestamp | `2026-09-01 10:00:00` |

---

#### 2.11. Entity: `Image`
Ảnh trong thư viện ảnh sự kiện (Event Gallery) và thư viện ảnh gia đình (Photo Gallery).

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `ImageID` | UUID / INT | Mã định danh ảnh | Yes | Primary Key | `img_00998877` |
| `EventID` | UUID / INT | Sự kiện chứa ảnh (nếu thuộc Event Gallery) | No | Foreign Key -> `Event.EventID` | `evt_11223344` |
| `FamilyID` | UUID / INT | Gia đình sở hữu ảnh (nếu thuộc Photo Gallery) | No | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `UploadedBy` | UUID / INT | Người tải lên | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Caption` | VARCHAR(255) | Mô tả/chú thích ảnh | No | Max 255 chars | `"Gia đình tại lễ giỗ 2026"` |
| `URL` | VARCHAR(500) | Đường dẫn ảnh trên Cloud | Yes | Valid URL | `"https://s3.amazonaws.com/..."` |
| `UploadedAt` | TIMESTAMP | Thời điểm tải lên | Yes | Default: `CURRENT_TIMESTAMP` | `2026-09-10 09:00:00` |

---

#### 2.12. Entity: `AuditLog`
Nhật ký kiểm toán ghi lại các thao tác quan trọng.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `LogID` | UUID / INT | Mã định danh nhật ký | Yes | Primary Key | `log_11221122` |
| `ActorID` | UUID / INT | Người thực hiện thao tác | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Action` | VARCHAR(50) | Hành động (CREATE, UPDATE, DELETE, LOGIN, ROLE_CHANGE...) | Yes | Enum: `CREATE`, `UPDATE`, `DELETE`, `LOGIN`, `ROLE_CHANGE`, `MODERATE`, `BACKUP`, `RESTORE` | `"ROLE_CHANGE"` |
| `EntityType` | VARCHAR(50) | Loại thực thể bị tác động | Yes | VD: `User`, `Post`, `FamilyMember` | `"User"` |
| `EntityID` | UUID / INT | ID của thực thể bị tác động | No | Valid ID | `usr_98b12f4a` |
| `Detail` | TEXT | Mô tả chi tiết thay đổi | No | Long text | `"Đổi vai trò USER -> ADMIN"` |
| `IPAddress` | VARCHAR(45) | Địa chỉ IP nguồn | No | IPv4/IPv6 | `"103.21.58.61"` |
| `CreatedAt` | TIMESTAMP | Thời điểm ghi nhật ký | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 14:00:00` |

---

#### 2.13. Entity: `Notification`
Thông báo gửi đến người dùng (in-app, email, push).

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `NotificationID` | UUID / INT | Mã định danh thông báo | Yes | Primary Key | `ntf_88776655` |
| `UserID` | UUID / INT | Người nhận thông báo | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |
| `Type` | VARCHAR(30) | Loại thông báo | Yes | Enum: `EVENT_REMINDER`, `INVITATION`, `NEW_POST`, `COMMENT`, `ANNOUNCEMENT`, `ACCOUNT` | `"EVENT_REMINDER"` |
| `Title` | VARCHAR(200) | Tiêu đề thông báo | Yes | Non-empty | `"Nhắc lịch: Lễ Giỗ Tổ"` |
| `Content` | TEXT | Nội dung chi tiết | No | Long text | `"Sự kiện diễn ra vào 08:00..."` |
| `IsRead` | BOOLEAN | Đã đọc hay chưa | Yes | Default: `FALSE` | `FALSE` |
| `CreatedAt` | TIMESTAMP | Thời điểm tạo thông báo | Yes | Default: `CURRENT_TIMESTAMP` | `2026-09-08 08:00:00` |

---

## 3. Đối chiếu với Functional Requirements (Validation matrix)

Bảng đối chiếu đảm bảo mọi yêu cầu chức năng (Functional Requirements) đều có đầy đủ thuật ngữ định nghĩa và thực thể dữ liệu tương ứng:

| Module / Requirement | Thuật ngữ liên quan (Glossary) | Thực thể dữ liệu tương ứng (Data Dictionary) | Trạng thái đối chiếu |
| :--- | :--- | :--- | :---: |
| **1. User & Security** | `Guest`, `Family Member`, `Family Owner`, `Administrator`, `RBAC`, `JWT` | `User` | ✅ Đã khớp |
| **2. Family & Genealogy Management** | `Family`, `Family Branch`, `Family Member`, `Generation`, `Relationship` | `Family`, `FamilyBranch`, `FamilyMember`, `Relationship` | ✅ Đã khớp |
| **3. Community** | `Community`, `Announcement`, `Family Member` | `Post`, `Comment`, `Notification` | ✅ Đã khớp |
| **4. Events** | `Event`, `Event Owner`, `RSVP`, `Family Member` | `Event`, `EventRSVP`, `Image`, `Notification` | ✅ Đã khớp |
| **5. Family Directory** | `Family Member`, `Generation`, `Family Branch` | `FamilyMember` (`Profession`, `Education`, `Generation`, `BranchID`) | ✅ Đã khớp |
| **6. Family Heritage** | `Heritage`, `Digital Archive`, `Family Member` | `HeritageItem`, `Image` | ✅ Đã khớp |
| **7. AI-assisted Services** | `AI Assistant`, `AI Service`, `Semantic Search`, `LLM` | *(Truy vấn tổng hợp từ `FamilyMember`, `HeritageItem`, `Relationship`, `Post`, `Event`)* | ✅ Đã khớp |
| **8. Dashboard & Reporting** | `Generation`, `Family Branch`, `Family Member` | *(Tính toán tổng hợp từ `Family`, `FamilyMember`, `Post`, `Event`)* | ✅ Đã khớp |
| **9. Administration** | `Administrator`, `RBAC`, `Audit Log`, `Family Owner` | `User`, `AuditLog` | ✅ Đã khớp |

---

## 4. Deliverables (Sản phẩm bàn giao)

Tài liệu này cung cấp các sản phẩm sau:

1. **Glossary**, Danh sách đầy đủ các thuật ngữ hệ thống với định nghĩa, module liên quan và ghi chú, dùng chung cho toàn bộ nhóm phát triển (Developers, Stakeholders, Users).
2. **Data Dictionary**, Từ điển dữ liệu mô tả chi tiết từng thực thể dữ liệu chính (Entity) và danh sách thuộc tính (Attribute) kèm kiểu dữ liệu, mô tả, tính bắt buộc, ràng buộc và ví dụ minh họa.
3. **Danh sách Entity**, 13 thực thể cốt lõi: `User`, `Family`, `FamilyBranch`, `FamilyMember`, `Relationship`, `Post`, `Comment`, `Event`, `EventRSVP`, `HeritageItem`, `Image`, `AuditLog`, `Notification`.
4. **Danh sách thuộc tính dữ liệu**, Bảng chi tiết thuộc tính của từng thực thể (Field Name, Data Type, Description, Required, Constraints, Example).
5. **Ma trận đối chiếu**, Bảng ánh xạ giữa Functional Requirements (9 module) ↔ Glossary ↔ Data Dictionary nhằm đảm bảo tính thống nhất và không có thuật ngữ trùng/mâu thuẫn.

---

## 5. Definition of Done (Tiêu chí hoàn thành)

- [x] Hoàn thành Glossary (đầy đủ thuật ngữ từ 9 module Functional Requirements).
- [x] Hoàn thành Data Dictionary (đủ 13 Entity và thuộc tính chi tiết).
- [x] Các thuật ngữ thống nhất với Functional Requirements (không trùng, không mâu thuẫn, xem mục 3).
- [x] Cập nhật tài liệu `docs/SRS/09_GlossaryAndDataDictionary.md`.
- [ ] Commit và Push lên GitHub.
- [ ] Tạo Pull Request (`feature/FT8-12-glossary-data-dictionary` → `develop`).
- [ ] Pull Request được Review và Merge.

---