Test Strategy - FamilyConnect
Dự án: FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
Tài liệu: Chiến lược kiểm thử (Test Strategy)
Phiên bản: v1.0
Ngày cập nhật: 2026-08-20

1. Mục tiêu kiểm thử (Testing Objectives)
Đảm bảo toàn bộ các Yêu cầu chức năng (FR), Yêu cầu phi chức năng (NFR), Quy tắc nghiệp vụ (BR) và Ca sử dụng (UC) hoạt động chính xác theo đúng tài liệu đặc tả.

Xác thực độ ổn định, tính bảo mật phân quyền (RBAC), hiệu năng API và khả năng tích hợp của hệ thống AI-assisted Services.

Đạt tỷ lệ bao phủ mã nguồn và test case theo đúng chuẩn chất lượng dự án đề ra.

2. Các cấp độ kiểm thử (Levels of Testing)
Unit Testing: Kiểm thử từng hàm, module độc lập (app/services, app/domain) bằng pytest.

Integration Testing: Kiểm thử sự kết hợp giữa các module (Controller -> Service -> Repository -> PostgreSQL Database).

System Testing: Kiểm thử toàn bộ hệ thống từ đầu đến cuối trên môi trường tích hợp.

User Acceptance Testing (UAT): Kiểm thử nghiệm thu người dùng dựa trên các kịch bản thực tế (xác nhận tài liệu, hiển thị đồ thị gia phả).

3. Các loại kiểm thử chuyên sâu (Types of Testing)
Functional Testing: Kiểm tra các tính năng chính (Đăng ký, Quản lý phả hệ, Sự kiện, Di sản, Thảo luận cộng đồng).

Security & Authorization Testing: Kiểm tra cơ chế xác thực JWT và phân quyền theo vai trò (Family Owner, Family Member, Admin, Guest).

Performance & Load Testing: Kiểm thử tải API (P95 < 2s) bằng công cụ k6.

Compatibility Testing: Kiểm tra tính tương thích giao diện trên các kích thước màn hình (Responsive Web Application).

4. Tiêu chí Nhận và Dừng kiểm thử (Entry & Exit Criteria)
Entry Criteria (Điều kiện bắt đầu):

Mã nguồn backend/frontend đã được build thành công không lỗi cú pháp.

Môi trường cơ sở dữ liệu PostgreSQL đã được khởi tạo dữ liệu mẫu (Test Data).

Các kịch bản test case và ma trận RTM đã được thông qua.

Exit Criteria (Điều kiện kết thúc):

100% các Test Case Critical và High được thực thi và đạt trạng thái PASS.

Không còn lỗi nghiêm trọng (Critical/High Defect) nào chưa được khắc phục.

Đạt tỷ lệ line coverage mục tiêu trên các module trọng yếu (Service layer đạt ~86%).

5. Tiêu chí Pass / Fail & Mức độ lỗi (Pass/Fail & Defect Severity)
Pass: Kết quả thực tế khớp hoàn toàn với mong đợi của Test Case.

Fail: Kết quả trả về sai lệch, phát sinh exception không xử lý hoặc vi phạm quy tắc nghiệp vụ.

Mức độ lỗi (Severity):

Critical: Sập hệ thống, mất dữ liệu, lỗi bảo mật nghiêm trọng.

High: Tính năng chính không hoạt động, sai lệch kết quả phân quyền.

Medium: Lỗi giao diện nhỏ, thông báo lỗi chưa trực quan.

Low: Lỗi chính tả, căn chỉnh bố cục giao diện không ảnh hưởng nghiệp vụ.