## 1. Giới thiệu đề tài
* **Tên đề tài:** FamilyConnect: AI-powered Digital Family Community Platform (Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo).
* **Bối cảnh dự án (Context):** Các gia đình hiện đại ngày càng phân tán về mặt địa lý do các yếu tố như giáo dục, cơ hội nghề nghiệp, di cư và toàn cầu hóa. Hệ quả là giao tiếp giữa các thành viên trở nên thưa thớt, hồ sơ gia phả khó duy trì và thế hệ trẻ có ít cơ hội hiểu về di sản gia đình cũng như xây dựng các mối quan hệ ý nghĩa.
* **Vấn đề cần giải quyết (Problem Statement):** Các mạng xã hội hiện tại hỗ trợ giao tiếp nhưng không được thiết kế để bảo tồn gia phả hoặc củng cố sự phát triển lâu dài của gia đình. Ngược lại, hệ thống gia phả truyền thống chỉ tập trung vào ghi chép thông tin dòng dõi mà thiếu tính năng cộng đồng tương tác. Do đó, cần có một nền tảng chuyên dụng vừa bảo tồn di sản, vừa tăng cường kết nối và tổ chức các hoạt động gia đình.
* **Giải pháp đề xuất (Proposed Solution):** Phát triển nền tảng FamilyConnect, kết hợp quản lý gia phả thông qua biểu đồ cấu trúc với các dịch vụ cộng đồng. Nền tảng tích hợp các dịch vụ AI để cung cấp khả năng tìm kiếm ngữ nghĩa, truy xuất kiến thức thông minh, giải thích mối quan hệ và đề xuất được cá nhân hóa.
* **Sản phẩm đầu ra (Expected Deliverables):** Cổng thông tin web (Web Portal), Ứng dụng di động (Mobile Application), các module hệ thống (Gia phả, Cộng đồng, Sự kiện, Di sản, AI Assistant, Báo cáo), dịch vụ RESTful API, Gói triển khai Docker và Tài liệu phần mềm.

## 2. Phân tích bài toán
* **Mục tiêu của hệ thống:** Xây dựng một hệ sinh thái phần mềm thống nhất tích hợp quản lý gia phả, giao tiếp gia đình, quản lý sự kiện, chia sẻ kiến thức và các dịch vụ hỗ trợ bởi AI.
* **Giá trị mang lại:** Cho phép người dùng trực quan hóa các mối quan hệ gia đình, điều hướng qua các thế hệ và duy trì hồ sơ gia đình chính xác. Hệ thống khuyến khích tương tác liên tục, chia sẻ kiến thức và hỗ trợ lẫn nhau giữa các thế hệ thông qua các tính năng cộng đồng, thay vì coi gia phả chỉ là thông tin tĩnh.
* **Đối tượng sử dụng:** 
  * Các thành viên trong gia đình (sử dụng Ứng dụng di động để tương tác, giao tiếp và xem thông tin).
  * Quản trị viên hệ thống và người quản lý gia tộc (sử dụng Web Management Portal để quản lý thành viên, cấu hình và kiểm duyệt).
* **Phạm vi của dự án:** Hệ thống áp dụng kiến trúc module bao gồm một Web Management Portal, một Mobile Application và một AI Service Layer, được kết nối với nhau thông qua các RESTful APIs.
* **Các ràng buộc ban đầu (Non-functional Requirements):** 
  * Ứng dụng Web cần tương thích với nhiều kích thước màn hình (Responsive) và ứng dụng di động đa nền tảng.
  * Yêu cầu xác thực bảo mật bằng JWT và sử dụng cơ sở dữ liệu PostgreSQL.
  * Trực quan hóa dữ liệu dạng đồ thị (Interactive Graph Visualization) và tích hợp dịch vụ AI.
  * Yêu cầu về kiến trúc bao gồm tính sẵn sàng cao (High Availability), đóng gói Docker và lưu vết hệ thống (Audit Logging).

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

## 4. Kế hoạch thực hiện Requirement Analysis
Trong Sprint 1, các tài liệu (Deliverables) cần hoàn thành cho giai đoạn Phân tích yêu cầu bao gồm:
1. **Stakeholder Analysis:** Phân tích các bên liên quan.
2. **Vision & Scope:** Tầm nhìn và phạm vi dự án.
3. **Functional Requirements:** Đặc tả các yêu cầu chức năng.
4. **Non-functional Requirements:** Đặc tả các yêu cầu phi chức năng.
5. **Use Case Diagram:** Sơ đồ Use Case tổng quan và chi tiết.
6. **Use Case Specification:** Đặc tả chi tiết kịch bản cho từng Use Case.
"""
