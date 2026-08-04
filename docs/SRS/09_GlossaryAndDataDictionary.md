# 09. Glossary and Data Dictionary

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
| **RSVP** | Trạng thái xác nhận tham gia sự kiện của thành viên (Tham gia / Không tham gia / Có thể). | Events | Viết tắt từ tiếng Pháp "RÉpondez S'il Vous Plaît". |
| **RBAC** | (Role-Based Access Control) Cơ chế kiểm soát truy cập dựa trên vai trò của người dùng trong hệ thống (Admin, Family Owner, Member, Guest). | User & Security | Đảm bảo tính bảo mật và riêng tư dữ liệu gia đình. |

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
| `Status` | VARCHAR(20) | Trạng thái tài khoản | Yes | Enum: `ACTIVE`, `INACTIVE`, `BLOCKED` | `"ACTIVE"` |
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
| `CreatedAt` | TIMESTAMP | Ngày khởi tạo Family trên hệ thống | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 10:30:00` |

---

#### 2.3. Entity: `FamilyMember`
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
| `Profession` | VARCHAR(100) | Nghề nghiệp hiện tại/trước đây | No | Max 100 chars | `"Kỹ sư Phần mềm"` |
| `Education` | VARCHAR(100) | Trình độ học vấn | No | Max 100 chars | `"Đại học"` |

---

#### 2.4. Entity: `Relationship`
Mô tả mối quan hệ giữa hai thành viên trong cây phả hệ (Graph Node Connection).

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `RelationshipID`| UUID / INT | Mã định danh mối quan hệ | Yes | Primary Key | `rel_99887766` |
| `FromMemberID` | UUID / INT | ID thành viên nguồn (ví dụ: Cha/Mẹ/Chồng) | Yes | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8400` |
| `ToMemberID` | UUID / INT | ID thành viên đích (ví dụ: Con/Vợ) | Yes | Foreign Key -> `FamilyMember.MemberID` | `mem_550e8401` |
| `Type` | VARCHAR(30) | Loại quan hệ | Yes | Enum: `PARENT_CHILD`, `MARRIAGE` | `"PARENT_CHILD"` |
| `Notes` | VARCHAR(255) | Ghi chú thêm (vd: Con nuôi, Đã ly hôn) | No | Max 255 chars | `"Con ruột"` |

---

#### 2.5. Entity: `Event`
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
| `CreatedBy` | UUID / INT | Người tạo sự kiện | Yes | Foreign Key -> `User.UserID` | `usr_98b12f4a` |

---

#### 2.6. Entity: `HeritageItem`
Lưu trữ tài liệu lịch sử, câu chuyện, tư liệu di sản.

| Field Name | Data Type | Description | Required | Constraints | Example |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `HeritageID` | UUID / INT | Mã định danh di sản/tư liệu | Yes | Primary Key | `her_77665544` |
| `FamilyID` | UUID / INT | Thuộc gia đình nào | Yes | Foreign Key -> `Family.FamilyID` | `fam_10293847` |
| `Title` | VARCHAR(200) | Tiêu đề di sản/câu chuyện | Yes | Non-empty | `"Sắc phong vua ban năm 1890"` |
| `Category` | VARCHAR(50) | Phân loại | Yes | Enum: `STORY`, `DOCUMENT`, `OUTSTANDING_MEMBER` | `"DOCUMENT"` |
| `Content` | TEXT | Nội dung chi tiết văn bản/câu chuyện | No | Long text | `"Năm Kỷ Hợi, gia tộc..."` |
| `MediaURL` | VARCHAR(500) | Đường dẫn ảnh/file tư liệu lưu trên Cloud | No | Valid URL | `"https://s3.amazonaws.com/..."` |
| `CreatedAt` | TIMESTAMP | Ngày đăng tài liệu | Yes | Default: `CURRENT_TIMESTAMP` | `2026-08-04 11:00:00` |

---

## 3. Đối chiếu với Functional Requirements (Validation matrix)

Bảng đối chiếu đảm bảo mọi yêu cầu chức năng (Functional Requirements) đều có đầy đủ thuật ngữ định nghĩa và thực thể dữ liệu tương ứng:

| Module / Requirement | Thuật ngữ liên quan (Glossary) | Thực thể dữ liệu tương ứng (Data Dictionary) | Trạng thái đối chiếu |
| :--- | :--- | :--- | :---: |
| **User & Security** | `Family Owner`, `Administrator`, `RBAC` | `User` | ✅ Đã khớp |
| **Family & Genealogy Management** | `Family`, `Family Branch`, `Family Member`, `Generation`, `Relationship` | `Family`, `FamilyBranch`, `FamilyMember`, `Relationship` | ✅ Đã khớp |
| **Community** | `Community`, `Announcement` | `Post`, `Comment` | ✅ Đã khớp |
| **Events** | `Event`, `RSVP` | `Event`, `EventRSVP` | ✅ Đã khớp |
| **Family Directory** | `Family Member`, `Generation` | `FamilyMember` (`Profession`, `Education`) | ✅ Đã khớp |
| **Family Heritage** | `Heritage` | `HeritageItem` | ✅ Đã khớp |
| **AI-assisted Services** | `AI Assistant` | *(Truy vấn dữ liệu tổng hợp từ FamilyMember, HeritageItem, Relationship)* | ✅ Đã khớp |
| **Administration** | `Administrator`, `RBAC` | `User`, `AuditLog` | ✅ Đã khớp |

---