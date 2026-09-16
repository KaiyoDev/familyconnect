Test Plan - FamilyConnect
Dự án: FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
Tài liệu: Kế hoạch kiểm thử (Test Plan)
Phiên bản: v1.0
Ngày cập nhật: 2026-08-20

1. Phạm vi kiểm thử (Test Scope)
In-Scope (Trong phạm vi):

9 Module chính: User & Security (US), Family & Genealogy (FG), Community (COM), Events (EVT), Directory (DIR), Heritage (HER), AI Services (AI), Dashboard (DASH), Administration (ADM).

Out-of-Scope (Ngoài phạm vi):

Ứng dụng di động độc lập (Mobile App - NFR-02) dành cho giai đoạn sau.

2. Môi trường kiểm thử (Test Environment)
Backend & DB: Python/Flask Clean Architecture, PostgreSQL.

Tools: Postman, Pytest (pytest --cov), k6 (Load testing).

Test Accounts: Administrator, Family Owner, Family Member, Guest.

3. Dữ liệu kiểm thử (Test Data)
Tập dữ liệu giả lập (Mock data) không chứa thông tin thật (PII).

Gồm tài khoản phân quyền, cây gia phả mẫu, sự kiện và tư liệu di sản.

4. Lịch trình & Phân công (Schedule & Resources)
Chuẩn bị: Xây dựng Test Strategy, Test Plan, RTM.

Thực thi: Chạy tự động qua Pytest trên CI/CD và môi trường local.

Nghiệm thu: Kiểm tra giao diện, file bằng chứng (docs/testing/evidence/uat/).

5. Sản phẩm bàn giao (Deliverables)
docs/testing/Test-Strategy.md

docs/testing/Test-Plan.md

docs/testing/Test-Data.md

docs/testing/RTM.md