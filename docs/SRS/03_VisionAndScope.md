# Vision and Scope Document - FamilyConnect

## Document Control
* **Project Name:** FamilyConnect - Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo (AI-powered Digital Family Community Platform)
* **File Path:** `docs/SRS/03_VisionAndScope.md`
* **Status:** Draft / Approved

---

## 1. Product Vision (Tầm nhìn sản phẩm)

### 1.1. Tầm nhìn của hệ thống (System Vision)
Trong bối cảnh toàn cầu hóa, gia đình hiện đại ngày càng bị phân tán về mặt địa lý do học tập, công tác và định cư. **FamilyConnect** được định hướng trở thành **Nền tảng Cộng đồng Gia đình số hàng đầu**, không chỉ đơn thuần là công cụ lưu trữ gia phả tĩnh mà còn là môi trường kết nối trực tuyến toàn diện. Hệ thống kết hợp giữa quản lý gia phả dạng đồ thị (Family Graph), mạng xã hội nội bộ gia đình và Trí tuệ nhân tạo (AI) nhằm gìn giữ truyền thống, thắt chặt mối quan hệ giữa các thế hệ và hỗ trợ lẫn nhau trong cuộc sống.

### 1.2. Giá trị cốt lõi mang lại (Core Values)
* **Gìn giữ & Kết nối (Preserve & Connect):** Số hóa và bảo tồn lịch sử, truyền thống gia đình; duy trì sợi dây liên lạc khăng khít giữa các thành viên dù ở bất kỳ đâu.
* **Bảo mật & Riêng tư (Privacy & Security):** Đảm bảo thông tin gia đình, hình ảnh, tài liệu lịch sử được bảo vệ tối đa, chỉ chia sẻ nội bộ trong gia tộc theo phân quyền (RBAC).
* **Thông minh & Tiện lợi (AI-driven & Convenience):** Ứng dụng AI giúp tra cứu mối quan hệ, truy vấn thông tin gia tộc bằng ngôn ngữ tự nhiên và gợi ý kết nối tri thức một cách thông minh.
* **Tương tác đa thế hệ (Multi-generational Engagement):** Giao diện thân thiện, đa nền tảng (Web & Mobile) giúp cả người lớn tuổi lẫn thế hệ trẻ đều dễ dàng truy cập và sử dụng.

### 1.3. Định hướng phát triển (Development Roadmap)
* **Giai đoạn 1 (MVP - Hiện tại):** Hoàn thiện các chức năng lõi gồm Quản lý tài khoản, Cây gia phả tương tác, Mạng xã hội gia đình (bài đăng, sự kiện), Trợ lý AI cơ bản và Dashboard thống kê.
* **Giai đoạn 2 (Growth):** Nâng cao năng lực AI (phân tích ngữ nghĩa chuyên sâu, tóm tắt gia sử), phát triển danh mục lưu trữ số di sản gia đình (Family Heritage Archive), mở rộng kết nối Mobile App mượt mà.
* **Giai đoạn 3 (Scale):** Tích hợp các dịch vụ gia tăng (hỗ trợ lập quỹ gia đình, số hóa tư liệu cổ bằng OCR, hỗ trợ cây gia phả quy mô cực lớn hàng ngàn thành viên).

### 1.4. Mục tiêu dài hạn (Long-term Goals)
* Trở thành nền tảng quản lý gia phả và cộng đồng gia đình phổ biến nhất cho các họ tộc tại Việt Nam và cộng đồng người Việt toàn cầu.
* Số hóa thành công hơn $10.000+$ cây gia phả và kết nối hàng triệu thành viên gia đình.
* Giúp thế hệ trẻ duy trì sự hiểu biết về nguồn cội với tỷ lệ tương tác hàng tháng (MAU) đạt trên $70\%$ người dùng đăng ký.

---

## 2. Business Goals (Mục tiêu kinh doanh & Dự án)

### 2.1. Mục tiêu tổng quát
Phát triển hệ thống FamilyConnect hoàn chỉnh theo mô hình kiến trúc hiện đại (Web Management Portal, Cross-platform Mobile App, AI Service Layer kết nối qua RESTful API), giải quyết triệt để bài toán đứt gãy kết nối gia đình và thất lạc thông tin gia phả truyền thống.

### 2.2. Mục tiêu cụ thể (SMART Goals)
* **Thời gian:** Hoàn thành phát triển, kiểm thử và đóng gói Docker deployment cho phiên bản 1.0 đúng tiến độ cam kết.
* **Chất lượng:** Đảm bảo đáp ứng $100\%$ các Functional Requirements cấp thiết (Authentication, Genealogy Tree, Community, Events, AI Assistant, Dashboard).
* **Hiệu năng & Khả dụng:** Hệ thống phản hồi API dưới $2$ giây với các truy vấn thông thường, cây gia phả tương tác mượt mà, thời gian hoạt động (Uptime) đạt $99.5\%$.
* **Kiến trúc:** Đạt chuẩn thiết kế phần mềm với cơ sở dữ liệu PostgreSQL, bảo mật JWT, RESTful API và tài liệu SRS đầy đủ.

### 2.3. Lợi ích mang lại cho người dùng
* **Thành viên gia đình:** Dễ dàng tra cứu xem "mình gọi người này là gì" thông qua tính năng giải thích quan hệ của AI; không bỏ lỡ các sự kiện, ngày giỗ, sinh nhật trong họ.
* **Trưởng họ / Ban quản trị gia phả:** Tiết kiệm thời gian cập nhật, chỉnh sửa gia phả; dễ dàng lưu trữ hình ảnh, tư liệu truyền thống mà không lo hư hỏng theo thời gian.
* **Thế hệ trẻ:** Có không gian riêng tư, an toàn để chia sẻ thành tích, kết nối công việc/học tập với các thành viên khác trong dòng họ dựa trên danh mục nghề nghiệp (Family Directory).

### 2.4. Giá trị đối với cộng đồng
* Bối tồn các giá trị văn hóa, lịch sử và truyền thống gia đình Việt Nam trong thời đại số.
* Thúc đẩy sự gắn kết cộng đồng, tương trợ lẫn nhau giữa các thế hệ trong cùng dòng tộc.

---

## 3. Project Scope (Phạm vi dự án)

### 3.1. Trong phạm vi triển khai (In Scope)

| Phân hệ / Module | Các chức năng chính triển khai trong phiên bản này |
| :--- | :--- |
| **Quản lý tài khoản & Bảo mật (User & Security)** | - Đăng ký, đăng nhập, xác thực bằng JWT.<br>- Phân quyền người dùng dựa trên vai trò (RBAC: Admin, Family Leader, Member).<br>- Quản lý thông tin cá nhân và xác minh thành viên gia đình. |
| **Quản lý Gia phả (Family & Genealogy)** | - Tạo và quản lý gia tộc, chi/nhánh gia đình.<br>- Quản lý quan hệ Cha-Con, Vợ-Chồng.<br>- Hiển thị Cây gia phả tương tác (Interactive Genealogy Tree).<br>- Trực quan hóa và truy vấn mối quan hệ giữa 2 thành viên bất kỳ. |
| **Cộng đồng Gia đình (Community)** | - Tạo bài đăng, chia sẻ tin tức gia đình, hình ảnh, thông báo.<br>- Tương tác: Bình luận, thả cảm xúc (React). |
| **Quản lý Sự kiện (Events)** | - Tạo sự kiện gia đình (ngày giỗ, họp họ, mừng thọ...).<br>- Quản lý điểm danh / xác nhận tham gia (RSVP).<br>- Nhắc lịch sự kiện và thư viện ảnh sự kiện. |
| **Trợ lý Trí tuệ nhân tạo (AI Assistant)** | - Tìm kiếm ngữ nghĩa thông minh (AI Semantic Search).<br>- Trợ lý tri thức gia đình (hỏi đáp thông tin gia tộc).<br>- Giải thích mối quan hệ họ hàng tự động.<br>- Tóm tắt nội dung và gợi ý thành viên/nguồn lực liên quan. |
| **Danh mục & Di sản (Directory & Heritage)** | - Danh bạ gia đình: Tra cứu theo nghề nghiệp, vị trí, thế hệ.<br>- Lưu trữ tài liệu lịch sử, câu chuyện gia đình, vinh danh thành viên ưu tú. |
| **Báo cáo & Quản trị (Dashboard & Admin)** | - Dashboard thống kê dân số gia đình, hoạt động cộng đồng, sự kiện.<br>- Quản lý người dùng, duyệt nội dung (Moderation), Audit Log, Backup/Restore. |

### 3.2. Ngoài phạm vi triển khai (Out of Scope - Phiên bản hiện tại)
* Tính năng thanh toán trực tuyến hoặc quyên góp Quỹ dòng họ trực tiếp qua cổng thanh toán (Payment Gateway integration).
* Tính năng nhận diện khuôn mặt tự động trong ảnh gia đình (Facial Recognition tagging).
* Số hóa tự động gia phả bằng hình ảnh/chữ viết tay cổ (OCR chữ Hán Nôm) — sẽ xem xét ở giai đoạn sau.
* Cuộc gọi video/thoại riêng tư tích hợp (Tạm thời sử dụng liên kết ứng dụng bên thứ 3).

---

## 4. Assumptions and Constraints (Giả định và Ràng buộc)

### 4.1. Các giả định (Assumptions)
* Người dùng có thiết bị kết nối Internet (Smartphone hoặc Máy tính) để truy cập hệ thống.
* Trưởng họ hoặc người đại diện gia đình có sẵn thông tin cơ bản về gia phả để nhập liệu ban đầu.
* Các dịch vụ hạ tầng đám mây và LLM API (phục vụ AI Assistant) duy trì hoạt động ổn định trong quá trình phát triển và vận hành.

### 4.2. Ràng buộc về thời gian (Time Constraints)
* Dự án phải tuân thủ nghiêm ngặt tiến độ theo từng Work Package đã đề xuất.
* Tài liệu Vision & Scope và SRS phải được hoàn thiện trước khi tiến hành viết code cho các module nâng cao.

### 4.3. Ràng buộc về công nghệ (Technology Constraints)
* **Cơ sở dữ liệu:** Bắt buộc sử dụng PostgreSQL (kết hợp các mô hình dữ liệu dạng đồ thị / quan hệ).
* **Kiến trúc:** RESTful API Architecture, hệ thống phân tách giữa Backend, Frontend Web Portal, Mobile App và AI Service Layer.
* **Bảo mật:** Sử dụng cơ chế JWT cho authentication và RBAC cho authorization.
* **Triển khai:** Đóng gói toàn bộ ứng dụng bằng **Docker** để đảm bảo khả năng đóng gói và đóng chạy nhất quán trên các môi trường.

### 4.4. Ràng buộc về nguồn lực (Resource Constraints)
* Hệ thống được phát triển bởi nhóm dự án theo các phân công công việc định sẵn.
* Chi phí gọi API AI (LLM) cần được tối ưu hóa để tránh vượt ngân sách thử nghiệm của dự án.

---

## 5. Success Criteria (Tiêu chí đánh giá thành công)

1. **Tiến độ & Sản phẩm bàn giao (Deliverables):** Hoàn thành đầy đủ các sản phẩm cam kết (Web Portal, Mobile App, AI Services, Docker Package, SRS Documentation) đúng hạn.
2. **Độ phủ yêu cầu (Functional Completeness):** Đáp ứng trọn vẹn tất cả các yêu cầu chức năng thuộc phạm vi **In Scope**.
3. **Độ ổn định hệ thống (System Stability):** Hệ thống vận hành ổn định, không có lỗi nghiêm trọng (Critical Bug) trên môi trường kiểm thử.
4. **Trải nghiệm người dùng (UX/UI):** Cây gia phả hiển thị trực quan, mượt mà; Trợ lý AI trả lời chính xác quan hệ dòng họ và thông tin gia tộc.
5. **Chất lượng tài liệu:** Tài liệu SRS và tài liệu kỹ thuật được cập nhật đầy đủ, rõ ràng trên GitHub Repository.

eview và Merge.
