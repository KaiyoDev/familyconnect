# 04. THIẾT KẾ COMPONENT

## 1. Giới thiệu

### 1.1. Mục đích

Tài liệu mô tả thiết kế ở mức Component của hệ thống **FamilyConnect**, bao gồm:

* Các lớp chính và trách nhiệm.
* Các Component Frontend, Backend và AI.
* Quan hệ và phụ thuộc giữa các Component.
* Các luồng xử lý thông qua Sequence Diagram.
* Các Design Pattern được sử dụng.
* Liên kết giữa Requirement, Use Case, Class, Component và Sequence Diagram.

Thiết kế được xây dựng dựa trên System Architecture, Database Design, UI/UX Design, Functional Requirements và Use Case Specification.

### 1.2. Phạm vi

Thiết kế bao gồm:

* Backend Domain, Service và Repository.
* Frontend Page, Shared Component, Service và State Management.
* AI Service.
* Database và Storage.
* Authentication, Notification, Administration và Audit Log.

Không bao gồm chi tiết source code, database schema, API specification và cấu hình triển khai.

### 1.3. Kiến trúc tổng quan

FamilyConnect sử dụng kiến trúc phân lớp gồm:

**Frontend → Backend Services → Database/Storage**

Đối với AI:

**Backend → AI Service → RAG → Embedding → LLM**

Kiến trúc hướng đến việc tách biệt trách nhiệm, giảm phụ thuộc giữa các module, tăng khả năng tái sử dụng, bảo trì và mở rộng.

---

# 2. Class Diagram

## 2.1. Tổng quan

Các lớp chính được chia thành:

1. Backend Domain Classes
2. Backend Services
3. Backend Repositories
4. Frontend Pages
5. Frontend Shared Components
6. Frontend Services
7. Frontend State Management

## 2.2. Domain Classes

Các Domain Class chính:

* **User** – quản lý tài khoản và thông tin người dùng.
* **Family** – quản lý gia đình.
* **FamilyBranch** – quản lý các nhánh trong gia đình.
* **FamilyMember** – quản lý thành viên và thông tin gia phả.
* **Relationship** – biểu diễn quan hệ giữa các thành viên.
* **Post, Comment, Reaction** – quản lý hoạt động cộng đồng.
* **Event, EventRSVP** – quản lý sự kiện và đăng ký tham gia.
* **HeritageItem, FamilyStory** – lưu trữ di sản và câu chuyện gia đình.
* **Notification** – quản lý thông báo.
* **AuditLog** – ghi nhận các hoạt động quản trị và bảo mật.

### Quan hệ chính

* User sở hữu Family.
* Family chứa FamilyBranch và FamilyMember.
* FamilyMember liên kết với nhau thông qua Relationship.
* User tạo Post và Event.
* Post có Comment và Reaction.
* Event có EventRSVP.
* Family chứa HeritageItem và FamilyStory.
* User nhận Notification và tạo AuditLog.

## 2.3. Backend Services

Các Service chính:

| Service             | Chức năng                                  |
| ------------------- | ------------------------------------------ |
| AuthService         | Đăng ký, đăng nhập, xác thực, đổi mật khẩu |
| UserService         | Quản lý hồ sơ người dùng                   |
| FamilyService       | Tạo và quản lý gia đình                    |
| GenealogyService    | Quản lý thành viên và cây gia phả          |
| CommunityService    | Quản lý bài đăng, bình luận, tương tác     |
| EventService        | Quản lý sự kiện và RSVP                    |
| DirectoryService    | Tìm kiếm thành viên                        |
| HeritageService     | Quản lý tài liệu và câu chuyện gia đình    |
| AIService           | Tìm kiếm ngữ nghĩa, chatbot và xử lý AI    |
| NotificationService | Quản lý thông báo và email                 |
| AdminService        | Quản trị, kiểm duyệt và Audit Log          |

## 2.4. Repository

Repository chịu trách nhiệm truy cập dữ liệu và tách biệt Database khỏi Business Logic.

Các Repository chính:

* UserRepository
* FamilyRepository
* RelationshipRepository
* PostRepository
* EventRepository
* HeritageRepository
* NotificationRepository
* AuditLogRepository

## 2.5. Frontend

### Các Page chính

* LandingPage
* LoginPage
* RegisterPage
* DashboardPage
* FamilyListPage
* FamilyManagementPage
* GenealogyTreePage
* CommunityFeedPage
* EventsListPage
* EventDetailPage
* MemberDirectoryPage
* MemberProfilePage
* HeritageArchivePage
* AIAssistantPage
* AdminDashboardPage

### Shared Components

Các Component dùng chung gồm:

**Header, Sidebar, PostCard, MemberCard, EventCard, GenealogyTreeViewer, AIChatWidget, NotificationPanel, Modal, Form và DataTable.**

### State Management

Gồm:

* **AuthStore** – trạng thái đăng nhập.
* **FamilyStore** – trạng thái gia đình hiện tại.
* **UIStore** – trạng thái giao diện và dữ liệu dùng chung.

---

# 3. Component Diagram

FamilyConnect có **21 Component chính**, được chia thành 5 lớp:

### 3.1. Frontend

* Shell
* Pages
* Shared Components
* Services
* State Management

Chịu trách nhiệm giao diện, tương tác người dùng và giao tiếp với Backend.

### 3.2. Backend

* Auth
* Family Management
* Genealogy
* Community
* Event
* Directory
* Heritage
* Notification
* Admin

Mỗi Component đảm nhiệm một nhóm nghiệp vụ riêng.

### 3.3. AI Service

Gồm:

* AI Service
* RAG
* Embedding
* LLM Integration

Luồng xử lý:

**Backend → AI Service → RAG → Embedding → LLM**

RAG lấy dữ liệu liên quan từ Database để cung cấp Context cho mô hình AI.

### 3.4. Data & Storage

* **Database:** lưu dữ liệu có cấu trúc như User, Family, Genealogy, Event, Community và AI/RAG.
* **Storage:** lưu hình ảnh, tài liệu, media và file di sản.

### 3.5. Nguyên tắc thiết kế

* Mỗi Component có trách nhiệm rõ ràng.
* Giao tiếp thông qua các ranh giới được xác định.
* Tách Database khỏi Frontend.
* Backend API sử dụng FastAPI.
* AI được tách thành một Layer riêng.
* Database và File Storage được phân tách.
* Hạn chế Circular Dependency.

---

# 4. Sequence Diagrams

Hệ thống có các luồng xử lý chính:

### SD-01 – Login

**User → LoginPage → AuthService → Auth Component → UserRepository → Database**

Xử lý đăng nhập, kiểm tra tài khoản, xác thực mật khẩu và trả kết quả.

### SD-02 – Register

**User → RegisterPage → AuthService → Auth Component → UserRepository → Database**

Xử lý đăng ký, kiểm tra dữ liệu, kiểm tra email, mã hóa mật khẩu và tạo tài khoản.

### SD-03 – Create Family

**Owner → FamilyListPage → FamilyService → Family Management → FamilyRepository → Database**

Tạo gia đình, kiểm tra dữ liệu và ghi Audit Log.

### SD-04 – Add Member & Relationship

**Owner → GenealogyTreePage → GenealogyService → Genealogy Component → Database**

Thêm thành viên và tạo quan hệ trong cây gia phả.

### SD-05 – View Genealogy Tree

**Member → GenealogyTreePage → GenealogyService → Genealogy Component → Database**

Lấy thông tin thành viên và quan hệ để xây dựng cây gia phả.

### SD-06 – Create Post & Interact

**Member → CommunityFeedPage → CommunityService → Community Component → Database**

Hỗ trợ tạo bài đăng, bình luận, reaction và thông báo.

### SD-07 – Create Event & RSVP

**Member → EventDetailPage → EventService → Event Component → Database**

Tạo sự kiện, đăng ký tham gia và gửi thông báo.

### SD-08 – Search Directory

**Member → MemberDirectoryPage → DirectoryService → Directory Component → Database**

Tìm kiếm thành viên và hiển thị kết quả.

### SD-09 – AI Assistant

**Member → AIAssistantPage → AIService → RAG → Embedding → Database → LLM**

Hệ thống tìm kiếm Context phù hợp trước khi gửi dữ liệu cho LLM để tạo câu trả lời.

### SD-10 – Admin Moderation

**Admin → AdminDashboardPage → AdminService → Admin Component**

Xử lý xác thực quyền, kiểm duyệt nội dung, cập nhật trạng thái, ghi Audit Log và gửi thông báo.

---

# 5. Design Patterns

### 5.1. Repository Pattern

Tách logic truy cập Database khỏi Business Logic.

**Lợi ích:** dễ kiểm thử, giảm phụ thuộc Database và dễ bảo trì.

### 5.2. Service Layer Pattern

Mỗi nhóm nghiệp vụ được quản lý bởi một Service riêng.

**Lợi ích:** logic tập trung, trách nhiệm rõ ràng và dễ mở rộng.

### 5.3. Layered Architecture

Hệ thống được chia thành:

**Presentation → API → Business → AI → Persistence**

Giúp hệ thống dễ bảo trì, kiểm thử và mở rộng.

### 5.4. Dependency Injection

Cho phép truyền Repository và Dependency vào Service.

**Lợi ích:** giảm coupling và hỗ trợ Unit Test.

### 5.5. RAG Pattern

AI sử dụng RAG để lấy thông tin liên quan trước khi tạo câu trả lời:

**AI → RAG → Embedding → Database → Context → LLM → Response**

Giúp câu trả lời phù hợp với dữ liệu gia đình và giảm nguy cơ hallucination.

### 5.6. State Management

Frontend sử dụng AuthStore, FamilyStore và UIStore để quản lý trạng thái tập trung.

---

# 6. Traceability

Traceability đảm bảo Requirement được liên kết xuyên suốt hệ thống:

**Requirement → Architecture → Database → UI/UX → Class → Component → Sequence Diagram**

Các Functional Requirement được ánh xạ tới Class và Service tương ứng.

Use Case được liên kết với Sequence Diagram, ví dụ:

| Use Case                  | Sequence |
| ------------------------- | -------- |
| Login                     | SD-01    |
| Register                  | SD-02    |
| Create Family             | SD-03    |
| Add Member & Relationship | SD-04    |
| View Genealogy Tree       | SD-05    |
| Create Post & Interact    | SD-06    |
| Create Event & RSVP       | SD-07    |
| Search Directory          | SD-08    |
| AI Assistant              | SD-09    |
| Admin Moderation          | SD-10    |

Frontend Page cũng được liên kết với Backend Component tương ứng.

---

# 7. Kết luận

Component Design của **FamilyConnect** cung cấp cái nhìn tổng thể về cấu trúc và hoạt động của hệ thống.

Thiết kế kết nối:

**Requirements → Classes → Components → Services → Database → UI → Runtime Interactions**

Việc sử dụng Class Diagram, Component Diagram, Sequence Diagram, Design Patterns và Traceability giúp hệ thống có cấu trúc rõ ràng, dễ bảo trì, kiểm thử, mở rộng và phát triển các tính năng trong tương lai.
