Test Data - FamilyConnect
Dự án: FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
Tài liệu: Dữ liệu kiểm thử (Test Data)
Phiên bản: v1.0
Ngày cập nhật: 2026-08-20

1. Tổng quan dữ liệu kiểm thử (Test Data Overview)
Tài liệu này định nghĩa tập dữ liệu mẫu (Test Data Set) cần thiết để khởi tạo, chạy thử nghiệm và nghiệm thu hệ thống FamilyConnect trên môi trường staging/local.

Đảm bảo tính bảo mật, không sử dụng dữ liệu định danh cá nhân (PII) thật, mọi dữ liệu đều là dữ liệu giả lập (mock data) phục vụ kiểm thử.

2. Dữ liệu Tài khoản Người dùng & Phân quyền (User Accounts & RBAC)
Administrator (ADM-01):

Username: admin_root

Email: admin@familyconnect.test

Role: Administrator (Toàn quyền kiểm duyệt, quản trị hệ thống)

Family Owner (OWN-01):

Username: nguyen_van_a

Email: owner.a@familyconnect.test

Role: Family Owner (Quản lý nhánh dòng họ, duyệt thành viên)

Family Member (MEM-01):

Username: tran_thi_b

Email: member.b@familyconnect.test

Role: Family Member (Thành viên phả hệ, xem danh bạ, tham gia sự kiện)

Guest / Unverified (GST-01):

Username: le_van_c

Email: guest.c@familyconnect.test

Role: Guest (Quyền hạn hạn chế, chưa xác thực nhánh)

3. Dữ liệu Cấu trúc Cây Phả hệ (Genealogy Test Data)
Nhánh dòng họ mẫu: "Dòng họ Nguyễn Văn tại Thừa Thiên Huế"

Các nút quan hệ (Nodes & Edges):

Thế hệ 1: Cụ tổ (Nguyễn Văn Tòng) & Vợ (Lê Thị Hoa)

Thế hệ 2: Trưởng nam (Nguyễn Văn Hùng) & Con thứ (Nguyễn Thị Mai)

Thế hệ 3: Cháu nội (Nguyễn Văn An, Nguyễn Văn Bình)

Kiểm thử quan hệ huyết thống, cha mẹ - con cái và hôn nhân hợp lệ cho module đồ thị phả hệ.

4. Dữ liệu Sự kiện & Di sản (Events & Heritage Test Data)
Sự kiện dòng họ (Events):

Lễ giỗ tổ dòng họ (Sự kiện có thông báo nhắc nhở).

Họp mặt gia đình định kỳ.

Tư liệu di sản (Family Heritage):

Hình ảnh tư liệu lịch sử gia phả (Định dạng .jpg, dung lượng tối ưu < 5MB).

Văn bản mô tả di tích, gia phả dòng họ.

5. Dữ liệu Tương tác Cộng đồng & AI (Community & AI Services Test Data)
Bài viết thảo luận mẫu trên bảng tin cộng đồng (Community Feed).

Câu lệnh mẫu kiểm thử trợ lý ảo AI (AI-assisted Services):

"Hãy tóm tắt lịch sử phát triển của dòng họ Nguyễn Văn."

"Tìm mối quan hệ giữa nút thành viên A và nút thành viên B trong phả hệ."