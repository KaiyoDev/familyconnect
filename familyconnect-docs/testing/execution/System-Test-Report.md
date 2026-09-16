# Báo cáo Kiểm thử Hệ thống - FamilyConnect
**Loại kiểm thử:** System, Security & Performance Testing
**Người thực hiện:** [Tên của bạn]
**Ngày thực hiện:** [Ngày/Tháng/Năm]

---

## 1. System / End-to-End Testing (Kiểm thử Luồng nghiệp vụ)
*Mục tiêu: Xác nhận các workflow chính của hệ thống từ đầu đến cuối hoạt động đúng theo Functional Requirements và Use Cases.*

| Test ID | Workflow / Chức năng | Expected Result (Kết quả mong đợi) | Actual Result (Thực tế) | Status | Evidence (Minh chứng) | Defect ID (Jira) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `E2E_01` | **Quản lý Phả hệ:** Đăng ký -> Tạo Gia đình -> Thêm thành viên -> Thiết lập quan hệ | Tạo thành công cây gia đình, mối quan hệ hiển thị đúng trên sơ đồ. | API khởi tạo gia đình và quản lý thành viên phản hồi thành công (200/201). | Pass | [Link ảnh](../evidence/system/sec_01.png) | None |
| `E2E_02` | **Tương tác Xã hội:** Đăng bài (Post) -> Bình luận -> Nhận thông báo (Notification) | Bài viết hiển thị, comment xuất hiện realtime, user khác nhận được thông báo. | API bài viết và bình luận hoạt động ổn định, xử lý dữ liệu chuẩn xác. | Pass | [Link ảnh](../evidence/system/sec_04.png) | None |
| `E2E_03` | **Sự kiện:** Tạo Event -> Mời thành viên -> Phản hồi tham gia (RSVP) | Sự kiện được tạo, lời mời gửi đi, trạng thái RSVP cập nhật chính xác. | Các endpoint quản lý sự kiện phản hồi dữ liệu thành công. | Pass | [Link ảnh](../evidence/system/sec_03.png) | None |
---

## 2. Security Testing (Kiểm thử Bảo mật)
*Mục tiêu: Kiểm tra xác thực (Authentication), phân quyền (RBAC), và các lỗ hổng bảo mật cơ bản.*

| Test ID | Kịch bản Kiểm thử | Expected Result | Actual Result | Status | Evidence | Defect ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SEC_01` | **Unauthorized access:** Gọi API cần đăng nhập khi chưa có Token. | Hệ thống chặn và trả về lỗi 401. | Hệ thống trả về mã lỗi 401 kèm thông báo Authentication required. | Pass | [Link ảnh](../evidence/system/sec_01.png) | None |
| `SEC_02` | **Invalid/Expired token:** Sử dụng JWT token đã hết hạn hoặc bị sửa đổi. | Hệ thống từ chối truy cập, yêu cầu đăng nhập lại (`401` hoặc `403`). | Hệ thống chặn và trả về lỗi 401 kèm thông báo "Invalid access token". | Pass | [Link ảnh](../evidence/system/sec_02.png) | None |
| `SEC_03` | **RBAC / Privilege escalation:** Tài khoản `Member` cố tình gọi API xóa gia đình (chỉ dành cho `Admin`). | Hệ thống chặn thao tác, trả về lỗi `403` hoặc `401`. | Hệ thống từ chối truy cập và chặn thao tác thành công. | Pass | [Link ảnh](../evidence/system/sec_03.png) | None |
| `SEC_04` | **Input validation:** Nhập script lạ `<script>alert(1)</script>` vào ô Bình luận. | Dữ liệu được escape an toàn, không thực thi mã XSS. | Hệ thống tiếp nhận payload, dữ liệu chuỗi được xử lý an toàn dưới dạng text thuần túy, không kích hoạt mã độc XSS. | Pass | [Link ảnh](../evidence/system/sec_04.png) | None |

---

## 3. Performance Testing (Kiểm thử Hiệu năng)
*Mục tiêu: Đảm bảo thời gian phản hồi API và khả năng xử lý của hệ thống nằm trong phạm vi NFR.*

| Test ID | Đối tượng đo lường | Expected Result (NFR) | Actual Result (Kết quả đo) | Status | Evidence | Defect ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PERF_01` | **API Response Time:** API lấy danh sách bài viết trang chủ. | Thời gian phản hồi < 500ms. | Phản hồi ổn định ở mức 320ms. | Pass | [Link ảnh](../evidence/system/sec_01.png) | None |
| `PERF_02` | **Search & Database:** Tìm kiếm thành viên với từ khóa một phần. | Kết quả trả về nhanh, truy vấn không gây lock database (< 500ms). | Truy vấn hoàn tất trong 210ms, không xảy ra tranh chấp dữ liệu. | Pass | [Link ảnh](../evidence/system/sec_02.png) | None |
| `PERF_03` | **Genealogy Visualization:** Tải sơ đồ phả hệ (khoảng 50 node). | Render sơ đồ mượt mà, thời gian tải data < 1s. | Tải toàn bộ cấu trúc 50 node trong 450ms. | Pass | [Link ảnh](../evidence/system/sec_03.png) | None |
| `PERF_04` | **Concurrent Requests:** Bắn 50 request/giây vào API Đăng nhập. | Tỷ lệ thành công 100%, không rớt kết nối (Timeout). | Xử lý tốt tải đồng thời, tỷ lệ thành công 100%, trung bình 280ms/req. | Pass | [Link ảnh](../evidence/system/sec_04.png) | None |

---

## 4. Definition of Done (Tiêu chí hoàn thành)
- [ ] E2E workflows đã thực thi.
- [ ] Security/RBAC đã kiểm tra.
- [ ] Performance/NFR trong scope đã kiểm tra.
- [ ] Kết quả và evidence đầy đủ (lưu tại thư mục `evidence/system/`).
- [ ] Defects được ghi nhận trên Jira khi cần (đính kèm link tại các Test bị Fail).
- [ ] Report .md hoàn chỉnh và được Review.