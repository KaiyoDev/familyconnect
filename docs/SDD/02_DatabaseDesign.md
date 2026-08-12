# 02. DATABASE DESIGN DOCUMENT (DDD)
**Dự án:** FamilyConnect  
**Mã Task:** FT8-32 | **Sprint:** Sprint 3 - Thiết kế hệ thống  
**Hệ quản trị CSDL Target:** PostgreSQL 16+  
**Trạng thái:** Final v1.0  

---

## 1. Giới thiệu

### 1.1 Mục đích
Tài liệu **Database Design Document (DDD)** này được xây dựng nhằm mô tả chi tiết thiết kế cơ sở dữ liệu vật lý cho hệ thống **FamilyConnect**. Tài liệu thực hiện chuyển đổi 13 Entities khái niệm từ **SRS 09 (Glossary & Data Dictionary)** thành mô hình dữ liệu vật lý hoàn chỉnh trên hệ quản trị CSDL PostgreSQL, làm căn cứ kỹ thuật cho việc lập trình Backend, viết các bản Migration Script và triển khai ORM Mapping.

### 1.2 Phạm vi
Tài liệu bao gồm toàn bộ các khía cạnh thiết kế CSDL của hệ thống:
* **Mô hình Dữ liệu (Data Models):** Bao gồm sơ đồ CDM (Khái niệm), LDM (Logic - chuẩn hóa 3NF) và PDM (Vật lý - PostgreSQL).
* **Cấu trúc Đồ thị Gia phả (Genealogy Graph):** Chiến lược lưu trữ cạnh (edges), chỉ mục (indexes) và các truy vấn đệ quy (Recursive CTE) hỗ trợ hiển thị cây gia phả.
* **Bảo mật & Phân quyền:** Cơ chế lưu trữ tài khoản, băm mật khẩu, lưu vết Refresh Token và mô hình RBAC.
* **Tối ưu Hiệu năng & Lưu trữ:** Chiến lược đánh chỉ mục (Index strategy), phân vùng dữ liệu (Monthly Range Partitioning cho `audit_logs` và `notifications`) và quy hoạch lưu trữ Media.
* **Danh mục Dữ liệu Mở rộng (Extended Data Dictionary):** Chi tiết cấu trúc các bảng vật lý bao gồm kiểu dữ liệu, ràng buộc (Constraints) và chỉ mục.
* **Ma trận Truy xuất Nguồn gốc (Traceability Matrix):** Ánh xạ từ các FR, BR, NFR, UC trong SRS sang các yếu tố thiết kế trong CSDL.

### 1.3 Đối tượng sử dụng
* **Database Administrator (DBA) / Data Engineer:** Dùng để triển khai DDL Scripts, tối ưu truy vấn, tạo Partitions và cấu hình chỉ mục.
* **Backend Developers:** Dùng làm tài liệu tham chiếu xây dựng Entity Models (ORM/SQL queries), viết API và triển khai truy vấn đồ thị gia tộc.
* **Software Architects / Tech Lead:** Dùng để đánh giá tính toàn vẹn hệ thống, tuân thủ kiến trúc tổng thể (SAD) và duyệt Pull Request (PR).
* **QA / QC Team:** Dùng để xây dựng các kịch bản kiểm thử tích hợp (Integration Test) và kiểm tra ràng buộc dữ liệu.
## 2. Data Requirements

Bảng tổng hợp yêu cầu ảnh hưởng đến thiết kế cơ sở dữ liệu:

| Requirement Type | Source | Nội dung | Ảnh hưởng Database |
| :--- | :--- | :--- | :--- |
| **FR** | FR-FG-01 | Create/manage family tree | Relationship table, recursive queries |
| **FR** | FR-US-01 | User authentication | User table, password hashing |
| **BR** | BR-FG-01 | Tree integrity: no circular | CHECK constraint hoặc trigger |
| **BR** | BR-US-01 | Unique email per user | UNIQUE constraint on User.Email |
| **NFR** | NFR-06 | Graph visualization < 2s | Indexes on Relationship, CTE optimization |
| **NFR** | NFR-07 | PostgreSQL | Physical data model specifics |
| **NFR** | NFR-11 | Audit logging | AuditLog partitioning strategy |
| **UC** | UC-05 | Query ancestor/descendant | Recursive CTE design |
| **SRS09 Note** | Mục 2.4 | Profession/Education separation | EmploymentProfile, EducationProfile tables |

---
## 3. Conceptual ERD (CDM)

Vẽ ERD ở mức khái niệm từ 13 Entities SRS 09. Xác định:

- 13 Entities
- Relationships: 1:N, N:N, 1:1 với cardinality
- Foreign key placement

**Relationships chính:**

- User → Family (1:N) - creates
- Family → FamilyBranch (1:N) - has
- Family → FamilyMember (1:N) - has
- FamilyBranch → FamilyMember (1:N) - contains
- User ↔ FamilyMember (1:1) - linked
- FamilyMember → Relationship (1:N) - has
- Post → Comment (1:N) - has
- Family → Event (1:N) - has
- Event → EventRSVP (1:N) - has
- Event → Image (1:N) - has
- Family → HeritageItem (1:N) - has
- User → Notification (1:N) - receives
- User → AuditLog (1:N) - creates

**Công cụ:** Power Designer / Rational Rose / Draw.io

**Output:** docs/SDD/diagrams/erd-conceptual.png

---
## 4. Logical ERD (LDM) – Normalization

### 4.1. Normalization Decisions

Các quyết định chuẩn hóa dữ liệu được thực hiện nhằm giảm dư thừa dữ liệu, đảm bảo tính toàn vẹn và hỗ trợ mở rộng hệ thống:

| Nội dung | Quyết định thiết kế | Lý do |
| :--- | :--- | :--- |
| `FamilyMember.Profession` | Tách thành `EmploymentProfile` | Một thành viên có thể có nhiều nghề nghiệp |
| `FamilyMember.Education` | Tách thành `EducationProfile` | Một thành viên có thể có nhiều cấp/bậc học vấn |
| `Post.MediaURLs` | Giữ dạng JSON hoặc tách thành `PostMedia` | Phụ thuộc vào nhu cầu truy vấn và quản lý media |
| Comment reactions | Tách thành bảng `PostReaction` | Chuẩn hóa dữ liệu reaction và hỗ trợ quan hệ nhiều-nhiều |
| Post shares | Tách thành bảng `Share` nếu cần | Lưu thông tin chia sẻ bài viết độc lập |

### 4.2. Junction Tables cho quan hệ N-N

Các quan hệ nhiều-nhiều được triển khai thông qua các bảng trung gian (junction tables):

- `PostReaction`
- `EventParticipant`

Các bảng này chứa các Foreign Key tham chiếu đến các Entity liên quan và cho phép biểu diễn quan hệ N-N trong Logical Data Model.

### 4.3. Primary Keys

- Sử dụng **UUID** làm Primary Key cho tất cả các bảng.
- Mỗi bảng phải có một Primary Key duy nhất.
- UUID giúp định danh bản ghi ổn định và phù hợp với hệ thống phân tán.

### 4.4. Foreign Keys và Referential Actions

Các Foreign Key được xác định giữa các bảng dựa trên relationships trong Conceptual ERD.

Các hành động `ON DELETE` được lựa chọn tùy theo mức độ phụ thuộc của dữ liệu:

- `CASCADE`: sử dụng khi bản ghi con không có ý nghĩa nếu bản ghi cha bị xóa.
- `RESTRICT`: sử dụng để ngăn xóa bản ghi cha khi vẫn còn dữ liệu liên quan.
- `SET NULL`: sử dụng khi dữ liệu con vẫn có thể tồn tại mà không cần bản ghi cha.

### 4.5. Logical ERD

Logical ERD mô tả các Entity sau khi chuẩn hóa, bao gồm Primary Key, Foreign Key và các bảng trung gian cần thiết.

**Output**: docs/SDD/diagrams/erd-logical.png

---
## 5. Physical data model ERD (PDM) cho PostgreSQL

### 5.1 PostgreSQL-specific Data Types

- `UUID` cho Primary Keys (PKs)
- `VARCHAR(n)` cho các trường chuỗi có độ dài giới hạn
- `TEXT` cho nội dung văn bản dài
- `TIMESTAMPTZ` cho các trường timestamp
- `JSONB` cho dữ liệu linh hoạt
- `SMALLINT` cho các giá trị có phạm vi nhỏ

### 5.2 Index Strategy

- Tất cả Foreign Keys (FKs) đều có index
- Index cho các trường thường xuyên được tìm kiếm/truy vấn:
  - `User.Email` (`UNIQUE`)
  - `Post.FamilyID + CreatedAt`
  - Các trường tìm kiếm phổ biến khác
- Sử dụng **Partial Index** cho các cột có thể nhận giá trị `NULL`

### 5.3 Constraints

- Sử dụng `CHECK` constraints cho các trường dạng enum
- Sử dụng `UNIQUE` constraint cho các trường yêu cầu không trùng lặp:
  - Email
  - Phone
- Sử dụng `NOT NULL` cho các trường bắt buộc

### 5.4 Partitioning

- `AuditLog`: Partition theo `CreatedAt` với phương pháp **Monthly RANGE Partitioning**
- `Notification`: Partition theo `CreatedAt` với phương pháp **Monthly RANGE Partitioning**

### 5.5 Storage Strategy

- Media files được lưu trữ trên **Cloud Storage (S3)**
- Database chỉ lưu **URL/reference** đến file
- Không lưu trực tiếp file dạng `BLOB` trong PostgreSQL

### Output:`docs/SDD/diagrams/erd-physical.png`