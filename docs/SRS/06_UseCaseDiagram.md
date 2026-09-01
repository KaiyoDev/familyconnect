# 06. Use Case Diagram

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Sơ đồ Use Case (Use Case Diagram)
> **Jira:** [FT8-8](https://familyconnect.atlassian.net/browse/FT8-8), Xây dựng Use Case Diagram
> **Thuộc Epic:** FT8-4, Phân tích yêu cầu hệ thống (Sprint 1)
> **Trạng thái:** Final v1.0

---

## 1. Mục tiêu
Xây dựng Use Case Diagram cho hệ thống FamilyConnect nhằm mô hình hóa các chức năng chính và mối quan hệ giữa các Actor với hệ thống. Sơ đồ Use Case là cơ sở để đặc tả Use Case chi tiết và thiết kế hệ thống trong các Sprint tiếp theo.

---

## 2. Xác định Actor (Tác nhân)

| STT | Tên Actor | Loại Actor | Mô tả vai trò & Phạm vi tương tác |
| :---: | :--- | :--- | :--- |
| 1 | **Guest** | Human | Người dùng chưa đăng nhập hoặc truy cập qua liên kết mời (Invite Link). |
| 2 | **Family Member** | Human | Thành viên chính thức trong gia đình, có quyền sử dụng các tính năng tương tác, đăng bài, xem gia phả, sự kiện, danh bạ. |
| 3 | **Family Owner** | Human | Trưởng nhóm / Chủ không gian gia đình, quản lý cây gia phả, nhánh gia đình và duyệt thành viên (Kế thừa toàn bộ quyền từ Family Member). |
| 4 | **Administrator** | Human | Quản trị viên hệ thống toàn cục, quản lý người dùng, kiểm duyệt nội dung, nhật ký và cấu hình hệ thống. |
| 5 | **AI Service** | External System | Tác nhân AI bên ngoài hỗ trợ tìm kiếm ngữ nghĩa, trợ lý AI, tóm tắt và giải thích quan hệ gia đình. |

---

## 3. Danh sách Use Case chuẩn (12 Use Cases)

> FamilyConnect chốt **12 Use Case chuẩn** (`UC-01`..`UC-12`). Đây là hệ mã Use Case duy nhất dùng chung toàn dự án: Use Case Specification (FT8-10), ma trận FR↔UC (04_FunctionalRequirements.md, mục 4.5.2), Business Rules (FT8-11), UI/UX (FT8-33) và tài liệu thiết kế. Các Use Case theo module trước đây (UC1.1..UC9.4) được gộp về 12 Use Case chuẩn, mỗi Use Case liệt kê các chức năng con tương ứng.

### 3.1. UC-01: Đăng nhập & Xác thực (Authentication)
- Đăng nhập
- Đăng xuất
- Khôi phục mật khẩu (quên mật khẩu)
- Phân quyền truy cập theo vai trò (RBAC)
- Kiểm soát phiên làm việc (JWT)

### 3.2. UC-02: Đăng ký & Xác minh Thành viên (Registration & Member Verification)
- Đăng ký tài khoản
- Kích hoạt tài khoản
- Xác thực / phê duyệt thành viên tham gia gia đình

### 3.3. UC-03: Quản lý Gia đình & Chi nhánh (Family & Branch Management)
- Tạo & quản lý gia đình (Family)
- Quản lý chi nhánh (FamilyBranch)
- Quản lý thành viên gia đình (FamilyMember)

### 3.4. UC-04: Quản lý Quan hệ Cây gia phả (Genealogy Relationship Management)
- Quản lý quan hệ cha mẹ – con (Parent-Child)
- Quản lý quan hệ hôn nhân (Marriage)
- Kiểm soát chu trình (loop) và tính hợp lệ thế hệ

### 3.5. UC-05: Truy vấn & Trực quan hóa Cây gia phả (Genealogy Tree Query & Visualization)
- Xem cây gia phả tương tác (Interactive Tree)
- Trực quan hóa đồ thị quan hệ (Relationship Graph)
- Tra cứu quan hệ (đường đi, mức thân tộc)

### 3.6. UC-06: Quản lý Bài viết & Tương tác (Posts & Interactions)
- Đăng & quản lý bài viết
- Bình luận & thả cảm xúc
- Chia sẻ tin tức gia đình và hình ảnh
- Thông báo gia đình (Announcement)

### 3.7. UC-07: Quản lý Sự kiện & RSVP (Events & RSVP)
- Tạo & quản lý sự kiện
- Xác nhận tham dự (RSVP) & quản lý người tham gia
- Thư viện ảnh sự kiện (Event Gallery)
- Nhắc nhở sự kiện

### 3.8. UC-08: Tra cứu Danh bạ & Hồ sơ (Directory & Profiles)
- Xem danh bạ thành viên
- Hồ sơ nghề nghiệp (Professional) & hồ sơ học vấn (Education)
- Tìm kiếm thành viên (theo nghề nghiệp, địa điểm, thế hệ)

### 3.9. UC-09: Quản lý Lưu trữ & Di sản (Heritage & Digital Archive)
- Quản lý tư liệu lịch sử & câu chuyện gia đình
- Quản lý thành viên tiêu biểu
- Quản lý thư viện ảnh & kho lưu trữ số
- Duyệt tư liệu di sản (moderation, BR-HER-002)

### 3.10. UC-10: Trợ lý AI & Truy vấn Tri thức (AI Assistant & Knowledge Query)
- Tìm kiếm ngữ nghĩa bằng AI
- Trợ lý tri thức gia đình (chat + RAG)
- Giải thích quan hệ gia đình
- Tóm tắt nội dung & gợi ý thành viên/tài nguyên

### 3.11. UC-11: Xem Báo cáo & Thống kê (Dashboard & Reports)
- Thống kê gia đình, cộng đồng, sự kiện, nhân khẩu
- Xem dashboard
- Tạo & xuất báo cáo

### 3.12. UC-12: Quản trị Hệ thống & Kiểm duyệt (Administration & Moderation)
- Quản lý người dùng
- Kiểm duyệt nội dung
- Nhật ký kiểm toán (Audit Log)
- Sao lưu & phục hồi (Backup & Restore)
- Cấu hình hệ thống

---

## 4. Sơ đồ Use Case Diagram (PlantUML Source)

> **Tệp tin đính kèm:**
> - **File thiết kế:** `docs/SRS/diagrams/UseCase.drawio`
> - **Ảnh PNG xem trực tiếp:** `docs/SRS/diagrams/UseCase.png`
> - **File xuất PDF:** `docs/SRS/diagrams/UseCase.pdf`

![FamilyConnect Use Case Diagram](diagrams/UseCase.png)

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam actorStyle stickman

' --- ACTORS ---
actor "Guest" as guest
actor "Family Member" as member
actor "Family Owner" as owner
actor "Administrator" as admin
actor "AI Service" as ai << System >>

' Kế thừa Actor
owner --|> member

' --- SYSTEM BOUNDARY ---
rectangle "Hệ thống FamilyConnect" {

    ' Package 1: User & Security
    package "User & Security" {
        usecase "Đăng ký tài khoản" as UC_Register
        usecase "Đăng nhập" as UC_Login
        usecase "Quên mật khẩu" as UC_ForgotPass
        usecase "Quản lý hồ sơ cá nhân" as UC_Profile
        usecase "Xác thực thành viên" as UC_Auth
    }

    ' Package 2: Family & Genealogy
    package "Family & Genealogy" {
        usecase "Quản lý gia đình & nhánh" as UC_Family
        usecase "Quản lý thành viên & quan hệ" as UC_Genealogy
        usecase "Xem cây gia phả & Tra cứu" as UC_Tree
    }

    ' Package 3: Community & Events
    package "Community & Events" {
        usecase "Đăng bài & Chia sẻ media" as UC_Post
        usecase "Bình luận & Thả cảm xúc" as UC_Interact
        usecase "Quản lý sự kiện & RSVP" as UC_Event
        usecase "Quản lý thư viện ảnh sự kiện" as UC_EventMedia
        usecase "Gửi nhắc nhở sự kiện" as UC_Remind
    }

    ' Package 4: Directory & Heritage
    package "Directory & Heritage" {
        usecase "Tra cứu danh bạ gia đình" as UC_Directory
        usecase "Quản lý tư liệu & kho lưu trữ số" as UC_Heritage
    }

    ' Package 5: AI Services
    package "AI-assisted Services" {
        usecase "Tìm kiếm ngữ nghĩa & Gợi ý" as UC_AISearch
        usecase "Trợ lý AI & Giải thích quan hệ" as UC_AIAssistant
    }

    ' Package 6: Admin & Reporting
    package "Dashboard & Administration" {
        usecase "Xem thống kê & Xuất báo cáo" as UC_Report
        usecase "Quản lý người dùng & Kiểm duyệt" as UC_AdminUser
        usecase "Nhật ký, Cấu hình & Sao lưu" as UC_AdminSystem
    }

    ' --- RELATIONSHIPS (Include / Extend) ---
    UC_Post ..> UC_Auth : <<include>>
    UC_Event ..> UC_Auth : <<include>>
    UC_Genealogy ..> UC_Auth : <<include>>

    UC_Event <.. UC_EventMedia : <<extend>>
    UC_Event <.. UC_Remind : <<extend>>
    UC_Tree <.. UC_AIAssistant : <<extend>>
}

' --- ASSOCIATIONS ---
guest --> UC_Register
guest --> UC_Login
guest --> UC_ForgotPass

member --> UC_Profile
member --> UC_Tree
member --> UC_Post
member --> UC_Interact
member --> UC_Event
member --> UC_Directory
member --> UC_Heritage

owner --> UC_Family
owner --> UC_Genealogy

admin --> UC_Report
admin --> UC_AdminUser
admin --> UC_AdminSystem

ai --> UC_AISearch
ai --> UC_AIAssistant
@enduml
> **Ghi chú:** Bản ảnh PNG hiện tại là bản vẽ theo module. Khi tái xuất sơ đồ, dùng **12 Use Case chuẩn** (`UC-01`..`UC-12`) theo danh sách ở Mục 3, với các Actor: Guest, Family Member, Family Owner, Administrator, AI Service. Mục 3 là nguồn chính thức cho mã UC; ảnh PNG là minh họa và phải được cập nhật để khớp.
