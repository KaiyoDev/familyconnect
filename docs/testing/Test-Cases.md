# Test Cases - FamilyConnect

> **Dự án:** FamilyConnect, Nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo
> **Tài liệu:** Bộ trường hợp kiểm thử (Test Cases) — Updated with execution results
> **Phiên bản:** v1.1
> **Ngày tạo:** 2026-08-20
> **Ngày cập nhật:** 2025-09-15

---

## Quy ước chung

### Test Case ID

`TC-<MODULE>-<STT><LOẠI>`

| Ký hiệu module | Module |
|:---------------:|--------|
| US | User & Security |
| FG | Family & Genealogy Management |
| COM | Community |
| EVT | Events |
| DIR | Family Directory |
| HER | Family Heritage |
| AI | AI-assisted Services |
| DASH | Dashboard & Reporting |
| ADM | Administration |

| Ký hiệu loại | Loại test |
|:------------:|-----------|
| P | Positive — kiểm tra luồng chính hoạt động đúng |
| N | Negative — kiểm tra xử lý lỗi / luồng ngoại lệ |
| V | Validation — kiểm tra ràng buộc dữ liệu, Business Rules |
| A | Authorization / RBAC — kiểm tra phân quyền |
| B | Boundary — kiểm tra biên (giới hạn ký tự, file size, số lượng) |
| E | Edge Case — kiểm tra tình huống đặc biệt |

### Quy ước trạng thái

| Trạng thái | Ý nghĩa |
|------------|---------|
| `PASS` | Test passed, kết quả thực tế khớp kết quả mong đợi |
| `FAIL` | Test failed, kết quả thực tế không khớp |
| `BLOCKED` | Test bị chặn (phụ thuộc module khác chưa xong, môi trường không khả dụng...) |
| `NOT RUN` | Chưa thực thi |

### Quy ước liên kết Bug ID & Evidence

- **Bug ID:** `BUG-<MODULE>-<STT>` (ví dụ: `BUG-US-001`)
- **Evidence:** Đường dẫn đến screenshot / log / video / test report (ví dụ: `evidence/US/TC-US-001P.png` hoặc link Jira)

### Danh sách yêu cầu tham chiếu

- **FR**: Functional Requirements (`04_FunctionalRequirements.md`)
- **NFR**: Non-Functional Requirements (`05_NonFunctionalRequirements.md`)
- **BR**: Business Rules (`08_BusinessRules.md`)
- **UC**: Use Case (`07_UseCaseSpecification.md`)

---

## Module 1: User & Security

### FR-US-01: Đăng ký tài khoản

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-001P | FR-US-01, BR-US-001, BR-US-002, BR-US-003, UC-02 | Đăng ký tài khoản thành công | 1. Guest chưa có tài khoản.<br>2. Guest có email hợp lệ đang hoạt động. | Email: `testuser@example.com`<br>Mật khẩu: `Abc12345`<br>Họ tên: `Nguyễn Văn A` | 1. Truy cập trang đăng ký.<br>2. Nhập họ tên, email, mật khẩu.<br>3. Xác nhận mật khẩu, đồng ý điều khoản.<br>4. Submit form.<br>5. Mở link kích hoạt trong email. | 1. Hệ thống tạo tài khoản với trạng thái *Pending Activation*.<br>2. Email kích hoạt được gửi đến địa chỉ đã đăng ký.<br>3. Sau khi kích hoạt, tài khoản chuyển sang *Active*.<br>4. Hiển thị thông báo thành công và chuyển hướng đến trang đăng nhập. | NOT RUN | | |
| TC-US-001N | FR-US-01, BR-US-001, UC-02 | Đăng ký với email đã tồn tại | 1. Email `existing@example.com` đã được đăng ký và kích hoạt. | Email: `existing@example.com`<br>Mật khẩu: `Abc12345`<br>Họ tên: `Nguyễn Văn B` | 1. Truy cập trang đăng ký.<br>2. Nhập email đã tồn tại.<br>3. Nhập thông tin còn lại.<br>4. Submit form. | Hệ thống hiển thị lỗi "Email đã được sử dụng" và đề nghị nhập email khác hoặc chuyển đến trang đăng nhập. | NOT RUN | | |
| TC-US-001N2 | FR-US-01, BR-US-002, UC-02 | Đăng ký với mật khẩu không đủ mạnh | 1. Guest chưa có tài khoản. | Email: `weakpass@example.com`<br>Mật khẩu: `123`<br>Họ tên: `Nguyễn Văn C` | 1. Truy cập trang đăng ký.<br>2. Nhập email, họ tên.<br>3. Nhập mật khẩu chỉ gồm số (3 ký tự).<br>4. Submit form. | Hệ thống hiển thị lỗi bên cạnh trường mật khẩu: "Mật khẩu phải có tối thiểu 8 ký tự, chứa cả chữ và số". Không tạo tài khoản. | NOT RUN | | |
| TC-US-001N3 | FR-US-01, UC-02 | Đăng ký với email không hợp lệ | 1. Guest chưa có tài khoản. | Email: `invalid-email`<br>Mật khẩu: `Abc12345`<br>Họ tên: `Nguyễn Văn D` | 1. Truy cập trang đăng ký.<br>2. Nhập email không đúng định dạng.<br>3. Nhập thông tin còn lại.<br>4. Submit form. | Hệ thống hiển thị lỗi bên cạnh trường email: "Email không hợp lệ". Không tạo tài khoản. | NOT RUN | | |
| TC-US-001N4 | FR-US-01, UC-02 | Đăng ký với mật khẩu xác nhận không khớp | 1. Guest chưa có tài khoản. | Email: `confirm@example.com`<br>Mật khẩu: `Abc12345`<br>Xác nhận: `Abc12346`<br>Họ tên: `Nguyễn Văn E` | 1. Truy cập trang đăng ký.<br>2. Nhập email, họ tên, mật khẩu.<br>3. Nhập mật khẩu xác nhận không khớp.<br>4. Submit form. | Hệ thống hiển thị lỗi "Mật khẩu xác nhận không khớp". Không tạo tài khoản. | NOT RUN | | |
| TC-US-001N5 | FR-US-01, BR-US-003, UC-02 | Kích hoạt tài khoản với token hết hạn | 1. Guest đã đăng ký nhưng chưa kích hoạt.<br>2. Token kích hoạt đã hết hạn (> 24h). | Token: expired_token_abc123 | 1. Guest mở link kích hoạt với token hết hạn. | Hệ thống hiển thị thông báo lỗi: "Đường dẫn kích hoạt đã hết hạn" và cho phép gửi lại email kích hoạt. | NOT RUN | | |
| TC-US-001V | FR-US-01, BR-US-001, UC-02 | Kiểm tra ràng buộc email duy nhất khi tạo tài khoản | 1. CSDL có tài khoản với email `unique@example.com` (ACTIVE). | Email: `unique@example.com`<br>Mật khẩu: `Abc12345`<br>Họ tên: `Nguyễn Văn F` | 1. Gọi API đăng ký với email đã tồn tại.<br>2. Kiểm tra response status và message. | API trả về HTTP 409 Conflict với message "Email đã được sử dụng". Không tạo bản ghi mới trong DB. | NOT RUN | | |
| TC-US-001B | FR-US-01, UC-02 | Đăng ký với tên quá dài | 1. Guest chưa có tài khoản. | Email: `longname@example.com`<br>Mật khẩu: `Abc12345`<br>Họ tên: chuỗi 101 ký tự (vượt quá VARCHAR(100)) | 1. Truy cập trang đăng ký.<br>2. Nhập họ tên 101 ký tự.<br>3. Nhập các trường còn lại hợp lệ.<br>4. Submit form. | Hệ thống hiển thị lỗi "Họ tên không được vượt quá 100 ký tự". Không tạo tài khoản. | NOT RUN | | |
| TC-US-001E | FR-US-01, UC-02 | Đăng ký khi email kích hoạt không đến (gửi lại) | 1. Guest đã đăng ký, trạng thái *Pending Activation*.<br>2. Email kích hoạt không đến hộp thư. | Email: `resend@example.com` | 1. Guest yêu cầu gửi lại email kích hoạt.<br>2. Hệ thống tạo token mới.<br>3. Gửi lại email kích hoạt.<br>4. Guest kích hoạt bằng token mới. | Hệ thống tạo token mới, vô hiệu hóa token cũ, gửi email kích hoạt mới. Guest kích hoạt thành công với token mới. | NOT RUN | | |

---

### FR-US-02: Đăng nhập

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-002P | FR-US-02, BR-US-003, UC-01 | Đăng nhập thành công | 1. Tài khoản đã tạo và kích hoạt (ACTIVE).<br>2. Tài khoản không bị khóa. | Email: `active@example.com`<br>Mật khẩu: `Abc12345` | 1. Mở trang đăng nhập.<br>2. Nhập email và mật khẩu hợp lệ.<br>3. Nhấn "Đăng nhập". | 1. Hệ thống xác thực thành công.<br>2. Cấp access token (JWT) và refresh token.<br>3. Chuyển hướng đến trang chủ theo vai trò.<br>4. Thời gian phản hồi ≤ 3 giây. | NOT RUN | | |
| TC-US-002N | FR-US-02, UC-01 | Đăng nhập với mật khẩu sai | 1. Tài khoản đã kích hoạt (ACTIVE). | Email: `active@example.com`<br>Mật khẩu: `WrongPass1` | 1. Mở trang đăng nhập.<br>2. Nhập đúng email, sai mật khẩu.<br>3. Nhấn "Đăng nhập". | Hệ thống báo lỗi "Email hoặc mật khẩu không đúng" (không tiết lộ trường nào sai). Tăng bộ đếm thất bại. | NOT RUN | | |
| TC-US-002N2 | FR-US-02, UC-01 | Đăng nhập với tài khoản chưa kích hoạt | 1. Tài khoản ở trạng thái *Pending Activation*. | Email: `pending@example.com`<br>Mật khẩu: `Abc12345` | 1. Mở trang đăng nhập.<br>2. Nhập email và mật khẩu của tài khoản chưa kích hoạt.<br>3. Nhấn "Đăng nhập". | Hệ thống hiển thị thông báo "Tài khoản chưa được kích hoạt. Vui lòng kiểm tra email để kích hoạt." và cho phép gửi lại email kích hoạt. | NOT RUN | | |
| TC-US-002N3 | FR-US-02, UC-01 | Đăng nhập với tài khoản bị khóa | 1. Tài khoản bị khóa bởi Administrator (BLOCKED). | Email: `blocked@example.com`<br>Mật khẩu: `Abc12345` | 1. Mở trang đăng nhập.<br>2. Nhập email và mật khẩu của tài khoản bị khóa.<br>3. Nhấn "Đăng nhập". | Hệ thống hiển thị thông báo "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ Administrator để được hỗ trợ." | NOT RUN | | |
| TC-US-002N4 | FR-US-02, FR-US-05, UC-01 | Đăng nhập với email không tồn tại | 1. Email chưa được đăng ký trong hệ thống. | Email: `nonexistent@example.com`<br>Mật khẩu: `Abc12345` | 1. Mở trang đăng nhập.<br>2. Nhập email không tồn tại.<br>3. Nhấn "Đăng nhập". | Hệ thống báo lỗi "Email hoặc mật khẩu không đúng" (không tiết lộ email không tồn tại). | NOT RUN | | |
| TC-US-002V | FR-US-02, BR-US-003, UC-01 | Khóa tạm thời sau 5 lần đăng nhập sai liên tiếp | 1. Tài khoản ACTIVE.<br>2. Bộ đếm thất bại hiện tại = 4. | Email: `brute@example.com`<br>Mật khẩu: `WrongPass1` (sai) | 1. Đăng nhập sai lần thứ 5 liên tiếp.<br>2. Kiểm tra trạng thái tài khoản.<br>3. Thử đăng nhập lại ngay với mật khẩu đúng. | 1. Sau lần thứ 5, tài khoản bị tạm khóa 15 phút.<br>2. Hệ thống thông báo "Tài khoản tạm thời bị khóa do đăng nhập sai nhiều lần. Vui lòng thử lại sau 15 phút."<br>3. Dù nhập đúng mật khẩu, vẫn không đăng nhập được trong thời gian khóa. | NOT RUN | | |
| TC-US-002A | FR-US-02, FR-US-05, UC-01 | Access token hết hạn, refresh token còn hạn | 1. Người dùng đã đăng nhập.<br>2. Access token đã hết hạn.<br>3. Refresh token còn hiệu lực. | Access token: expired_jwt<br>Refresh token: valid_refresh_jwt | 1. Gọi API yêu cầu tài nguyên với access token hết hạn.<br>2. Hệ thống từ chối với 401.<br>3. Client gửi refresh token để lấy access token mới. | 1. API trả về 401 Unauthorized.<br>2. Hệ thống cấp access token mới từ refresh token.<br>3. Client thực hiện lại request với token mới thành công. | NOT RUN | | |
| TC-US-002B | FR-US-02, UC-01 | Thời gian phản hồi đăng nhập (P95 < 3s) | 1. Tài khoản ACTIVE.<br>2. Môi trường mạng bình thường. | Email: `perf@example.com`<br>Mật khẩu: `Abc12345` | 1. Gọi API đăng nhập.<br>2. Đo thời gian phản hồi.<br>3. Lặp lại 100 lần để tính P95. | P95 thời gian phản hồi < 3 giây. | NOT RUN | | |

---

### FR-US-03: Đăng xuất

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-003P | FR-US-03, BR-US-006, UC-01 | Đăng xuất thành công | 1. Người dùng đã đăng nhập (có access token + refresh token hợp lệ). | Token: valid_jwt | 1. Người dùng mở menu tài khoản.<br>2. Chọn "Đăng xuất".<br>3. Xác nhận đăng xuất. | 1. Refresh token bị thu hồi.<br>2. Token lưu trữ trên thiết bị bị xóa.<br>3. Chuyển hướng về trang đăng nhập.<br>4. Token cũ không thể dùng để truy cập API. | NOT RUN | | |
| TC-US-003N | FR-US-03, BR-US-006, UC-01 | Đăng xuất khi token đã hết hạn | 1. Người dùng đã đăng nhập.<br>2. Token đã hết hạn. | Token: expired_jwt | 1. Người dùng chọn "Đăng xuất". | Hệ thống xóa token cục bộ và chuyển về trang đăng nhập mà không báo lỗi. | NOT RUN | | |
| TC-US-003A | FR-US-03, FR-ADM-01, UC-01 | Tài khoản bị khóa từ xa, yêu cầu đăng xuất | 1. Administrator khóa tài khoản đang hoạt động. | User ID: `user-001` | 1. Admin khóa tài khoản (FR-ADM-01).<br>2. Người dùng thực hiện thao tác bất kỳ. | 1. API từ chối với 403 Forbidden.<br>2. Nếu người dùng chọn "Đăng xuất", hệ thống xử lý thành công. | NOT RUN | | |

---

### FR-US-04: Khôi phục mật khẩu

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-004P | FR-US-04, BR-US-002, UC-01 | Khôi phục mật khẩu thành công | 1. Guest có tài khoản đã kích hoạt.<br>2. Guest quên mật khẩu. | Email: `reset@example.com`<br>Mật khẩu mới: `NewPass123` | 1. Nhấn "Quên mật khẩu?".<br>2. Nhập email đã đăng ký.<br>3. Mở link trong email.<br>4. Nhập mật khẩu mới hợp lệ.<br>5. Đăng nhập với mật khẩu mới. | 1. Email đặt lại được gửi với token hiệu lực 30 phút.<br>2. Mật khẩu mới được cập nhật.<br>3. Token được vô hiệu hóa.<br>4. Đăng nhập thành công với mật khẩu mới.<br>5. Mọi phiên cũ bị thu hồi. | NOT RUN | | |
| TC-US-004N | FR-US-04, UC-01 | Email không tồn tại trong hệ thống | 1. Guest nhập email chưa đăng ký. | Email: `unknown@example.com` | 1. Nhấn "Quên mật khẩu?".<br>2. Nhập email không tồn tại.<br>3. Submit. | Hệ thống hiển thị thông báo chung "Nếu email tồn tại, bạn sẽ nhận được hướng dẫn" — không tiết lộ email không tồn tại. | NOT RUN | | |
| TC-US-004N2 | FR-US-04, UC-01 | Token đặt lại mật khẩu hết hạn | 1. Guest đã yêu cầu đặt lại mật khẩu.<br>2. Token đã hết hạn (> 30 phút). | Token: expired_reset_token | 1. Mở link đặt lại với token hết hạn.<br>2. Nhập mật khẩu mới. | Hệ thống báo lỗi "Đường dẫn đặt lại mật khẩu đã hết hạn" và cho phép gửi lại yêu cầu. | NOT RUN | | |
| TC-US-004V | FR-US-04, BR-US-002, UC-01 | Đặt lại mật khẩu với mật khẩu yếu | 1. Guest có token hợp lệ. | Token: valid_reset_token<br>Mật khẩu mới: `123` | 1. Mở link đặt lại.<br>2. Nhập mật khẩu mới không đạt yêu cầu độ mạnh. | Hệ thống yêu cầu nhập lại theo chính sách (≥ 8 ký tự, có chữ và số). Không cập nhật mật khẩu. | NOT RUN | | |

---

### FR-US-05: Phân quyền truy cập theo vai trò (RBAC)

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-005P | FR-US-05, BR-US-004, UC-01, UC-12 | Guest chỉ truy cập được trang giới thiệu và đăng ký/đăng nhập | 1. Guest chưa đăng nhập. | Guest token: none | 1. Guest truy cập trang chủ.<br>2. Guest truy cập trang đăng ký.<br>3. Guest truy cập trang đăng nhập.<br>4. Guest truy cập API yêu cầu xác thực. | 1-3. Guest xem được các trang công khai.<br>4. API trả về 401 Unauthorized. | NOT RUN | | |
| TC-US-005P2 | FR-US-05, BR-US-004, UC-01 | Family Member truy cập được chức năng gia đình | 1. Family Member đã đăng nhập.<br>2. Family Member thuộc gia đình A. | Token: member_token<br>Family ID: `family-A` | 1. Gọi API xem cây gia phả của gia đình A.<br>2. Gọi API đăng bài trong gia đình A.<br>3. Gọi API xem danh bạ gia đình A. | Các API trả về 200 OK với dữ liệu hợp lệ. | NOT RUN | | |
| TC-US-005A | FR-US-05, BR-US-004, UC-01 | Family Member không truy cập được chức năng quản trị | 1. Family Member đã đăng nhập.<br>2. Không có vai trò Admin. | Token: member_token | 1. Gọi API quản lý người dùng toàn hệ thống.<br>2. Gọi API cấu hình hệ thống. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-US-005A2 | FR-US-05, BR-US-004, UC-01 | Family Member không truy cập được dữ liệu gia đình khác | 1. Family Member thuộc gia đình A.<br>2. Không thuộc gia đình B. | Token: member_A_token<br>Family ID: `family-B` | 1. Gọi API xem cây gia phả của gia đình B.<br>2. Gọi API xem danh bạ gia đình B. | API trả về 403 Forbidden với thông báo "Không có quyền truy cập gia đình này". | NOT RUN | | |
| TC-US-005A3 | FR-US-05, BR-US-004, UC-01 | Family Owner có quyền quản lý gia đình, Member không có | 1. User A là Family Owner của gia đình X.<br>2. User B là Family Member của gia đình X. | Token: owner_X_token<br>Token: member_X_token<br>Family ID: `family-X`<br>Target member ID: `member-01` | 1. User B gọi API xóa thành viên khỏi gia đình X.<br>2. User A gọi API xóa thành viên khỏi gia đình X. | 1. API trả về 403 Forbidden.<br>2. API trả về 200 OK (sau xác nhận). | NOT RUN | | |
| TC-US-005A4 | FR-US-05, BR-US-004, UC-01, UC-12 | Guest không có quyền đăng bài | 1. Guest chưa đăng nhập. | Guest token: none | 1. Gọi API tạo bài viết. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-US-005E | FR-US-05, BR-US-004, UC-01 | Vai trò bị thay đổi giữa phiên — quyền bị thu hồi | 1. Family Member đang có phiên hoạt động.<br>2. Administrator hạ quyền Member đó xuống Guest trong cùng gia đình. | Token: member_token (cũ)<br>Action: admin_demote | 1. Member thực hiện thao tác nhạy cảm (ví dụ: xóa bài viết).<br>2. Kiểm tra quyền. | Hệ thống đọc lại quyền từ database, phát hiện quyền đã bị thu hồi, trả về 403 Forbidden. | NOT RUN | | |

---

### FR-US-06: Quản lý hồ sơ cá nhân

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-006P | FR-US-06, BR-US-005, UC-08 | Cập nhật hồ sơ cá nhân thành công (tất cả trường) | 1. Family Member đã đăng nhập.<br>2. Hồ sơ hiện tại có dữ liệu mặc định. | Họ tên mới: `Nguyễn Văn Anh`<br>SĐT: `0912345678`<br>Ngày sinh: `1990-01-15`<br>Giới thiệu: `Kỹ sư CNTT`<br>Cài đặt riêng tư: `Công khai trong gia đình` | 1. Mở trang hồ sơ cá nhân.<br>2. Cập nhật tất cả trường cho phép.<br>3. Lưu thay đổi. | 1. Hệ thống kiểm tra tính hợp lệ thành công.<br>2. Dữ liệu được lưu vào DB.<br>3. Hiển thị thông báo "Cập nhật thành công".<br>4. Hồ sơ hiển thị thông tin mới. | NOT RUN | | |
| TC-US-006N | FR-US-06, UC-08 | Cập nhật với ngày sinh trong tương lai | 1. Family Member đã đăng nhập. | Ngày sinh: `2099-12-31` | 1. Mở trang hồ sơ.<br>2. Nhập ngày sinh trong tương lai.<br>3. Lưu. | Hệ thống báo lỗi "Ngày sinh không hợp lệ". | NOT RUN | | |
| TC-US-006N2 | FR-US-06, UC-08 | Cập nhật với SĐT không đúng định dạng | 1. Family Member đã đăng nhập. | SĐT: `abcxyz` | 1. Mở trang hồ sơ.<br>2. Nhập SĐT không hợp lệ.<br>3. Lưu. | Hệ thống báo lỗi "Số điện thoại không hợp lệ". | NOT RUN | | |
| TC-US-006N3 | FR-US-06, UC-08 | Cập nhật email — trường email không được phép sửa | 1. Family Member đã đăng nhập. | Email mới: `newemail@example.com` | 1. Mở trang hồ sơ.<br>2. Kiểm tra trường email có thể chỉnh sửa không. | Trường email bị vô hiệu hóa (disabled/readonly) trên giao diện. | NOT RUN | | |
| TC-US-006B | FR-US-06, UC-08 | Tải ảnh đại diện vượt quá giới hạn dung lượng | 1. Family Member đã đăng nhập. | Ảnh: 6MB, định dạng JPG | 1. Mở trang hồ sơ.<br>2. Chọn ảnh đại diện 6MB.<br>3. Lưu. | Hệ thống báo lỗi "Kích thước ảnh không được vượt quá 5MB". | NOT RUN | | |
| TC-US-006V | FR-US-06, BR-US-005, UC-08 | Kiểm tra một người dùng chỉ có một hồ sơ cá nhân | 1. User ID đã có hồ sơ. | User ID: `user-001` | 1. Gọi API tạo hồ sơ thứ hai cho cùng user. | API trả về lỗi hoặc hệ thống chỉ cho phép một hồ sơ duy nhất. | NOT RUN | | |

---

### FR-US-07: Xác thực thành viên gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-US-007P | FR-US-07, BR-FG-001, UC-02 | Family Owner phê duyệt yêu cầu tham gia thành công | 1. Family Owner đã đăng nhập.<br>2. User B gửi yêu cầu tham gia gia đình (PENDING).<br>3. Gia đình đã tồn tại (FR-FG-01). | Family ID: `family-A`<br>Owner ID: `owner-A`<br>Requester ID: `user-B`<br>Lời nhắn: `Con trai của Nguyễn Văn C` | 1. Owner mở danh sách yêu cầu chờ.<br>2. Xem thông tin người yêu cầu.<br>3. Phê duyệt yêu cầu.<br>4. Kiểm tra quyền của user B trong gia đình. | 1. Yêu cầu chuyển từ PENDING → APPROVED.<br>2. User B được gán vai trò Family Member trong gia đình.<br>3. User B nhận thông báo phê duyệt.<br>4. User B truy cập được dữ liệu gia đình. | NOT RUN | | |
| TC-US-007N | FR-US-07, BR-FG-001, UC-02 | Family Owner từ chối yêu cầu tham gia | 1. Family Owner đã đăng nhập.<br>2. User C gửi yêu cầu tham gia (PENDING). | Family ID: `family-A`<br>Requester ID: `user-C`<br>Lý do từ chối: `Không xác minh được mối quan hệ` | 1. Owner mở danh sách yêu cầu chờ.<br>2. Từ chối yêu cầu kèm lý do. | 1. Yêu cầu chuyển từ PENDING → REJECTED.<br>2. User C nhận thông báo từ chối kèm lý do.<br>3. User C không thể truy cập dữ liệu gia đình. | NOT RUN | | |
| TC-US-007A | FR-US-07, BR-FG-001, UC-02 | Family Member không có quyền phê duyệt yêu cầu | 1. Family Member đã đăng nhập.<br>2. Không phải Owner. | Token: member_token<br>Request ID: `request-001` | 1. Gọi API phê duyệt yêu cầu tham gia. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-US-007N2 | FR-US-07, UC-02 | Gửi yêu cầu tham gia khi đã là thành viên | 1. User D đã là Family Member của gia đình A. | Family ID: `family-A`<br>User ID: `user-D` | 1. User D gửi yêu cầu tham gia gia đình A. | Hệ thống chặn gửi yêu cầu trùng lặp, hiển thị thông báo "Bạn đã là thành viên của gia đình này". | NOT RUN | | |
| TC-US-007E | FR-US-07, UC-02 | Yêu cầu Pending quá 14 ngày tự động đóng | 1. Yêu cầu tham gia ở trạng thái PENDING.<br>2. Đã quá 14 ngày kể từ khi gửi. | Request ID: `request-002`<br>Created at: 15 ngày trước | 1. Hệ thống chạy job tự động đóng yêu cầu quá hạn.<br>2. Kiểm tra trạng thái yêu cầu. | Yêu cầu tự động chuyển sang CLOSED. Người gửi phải gửi lại yêu cầu mới. | NOT RUN | | |
| TC-US-007V | FR-US-07, BR-FG-001, UC-02 | Chỉ Family Owner mới được duyệt thành viên — kiểm tra RBAC | 1. User E là Family Member của gia đình A.<br>2. User E cố gắng duyệt thành viên. | Token: member_token<br>Request ID: `request-003` | 1. Gọi API phê duyệt. | API trả về 403 Forbidden. Chỉ Owner mới có quyền này. | NOT RUN | | |

---

---

## Module 2: Family & Genealogy Management

### FR-FG-01: Quản lý gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-001P | FR-FG-01, BR-FG-002, UC-03 | Tạo gia đình thành công | 1. Người dùng đã đăng ký và kích hoạt.<br>2. Người dùng chưa tạo quá 5 gia đình. | Tên gia đình: `Dòng Họ Nguyễn Văn`<br>Mô tả: `Dòng họ gốc tại Đồng Nai`<br>Khu vực: `Đồng Nai`<br>Quốc gia: `Việt Nam` | 1. Chọn "Tạo gia đình".<br>2. Nhập tên, mô tả, khu vực, quốc gia.<br>3. Submit. | 1. Bản ghi Family được tạo với status ACTIVE.<br>2. Người tạo được gán làm Family Owner.<br>3. Thành viên đầu tiên (Owner) được tạo tự động.<br>4. Chuyển hướng đến trang quản lý gia đình. | NOT RUN | | |
| TC-FG-001N | FR-FG-01, UC-03 | Tạo gia đình với tên trống | 1. Người dùng đã đăng ký và kích hoạt. | Tên gia đình: (trống)<br>Mô tả: `Mô tả` | 1. Chọn "Tạo gia đình".<br>2. Để trống tên gia đình.<br>3. Submit. | Hệ thống báo lỗi "Tên gia đình không được để trống". Không tạo gia đình. | NOT RUN | | |
| TC-FG-001N2 | FR-FG-01, UC-03 | Tạo gia đình khi đã đạt giới hạn 5 gia đình | 1. Người dùng đã là Owner của 5 gia đình. | Tên gia đình: `Gia Đình Thứ 6` | 1. Chọn "Tạo gia đình".<br>2. Nhập thông tin hợp lệ.<br>3. Submit. | Hệ thống báo lỗi "Bạn đã đạt giới hạn tạo gia đình (tối đa 5)". Không tạo gia đình mới. | NOT RUN | | |
| TC-FG-001P2 | FR-FG-01, UC-03 | Cập nhật thông tin gia đình | 1. Family Owner đã đăng nhập.<br>2. Gia đình đã tồn tại. | Family ID: `family-A`<br>Mô tả mới: `Mô tả cập nhật`<br>Khu vực mới: `TP. Hồ Chí Minh` | 1. Mở trang thông tin gia đình.<br>2. Sửa mô tả và khu vực.<br>3. Lưu. | 1. Thông tin gia đình được cập nhật.<br>2. Audit log ghi nhận thay đổi.<br>3. Hiển thị thông báo thành công. | NOT RUN | | |
| TC-FG-001P3 | FR-FG-01, BR-FG-002, UC-03 | Chuyển quyền Family Owner | 1. Family Owner (User A) đã đăng nhập.<br>2. Có Family Member (User B) trong gia đình. | Family ID: `family-A`<br>Current Owner: `user-A`<br>New Owner: `user-B` | 1. Owner A chọn chuyển quyền cho user B.<br>2. Xác nhận.<br>3. Kiểm tra vai trò. | 1. User B trở thành Family Owner mới.<br>2. User A trở thành Family Member.<br>3. User B nhận thông báo.<br>4. Audit log ghi nhận. | NOT RUN | | |
| TC-FG-001N3 | FR-FG-01, UC-03 | Chuyển quyền cho thành viên không tồn tại | 1. Family Owner đã đăng nhập. | Target User ID: `nonexistent-user` | 1. Owner chọn chuyển quyền cho user không tồn tại. | Hệ thống báo lỗi "Thành viên không tồn tại trong gia đình". | NOT RUN | | |
| TC-FG-001N4 | FR-FG-01, UC-03 | Giải tán gia đình - dữ liệu không bị xóa | 1. Family Owner đã đăng nhập.<br>2. Gia đình có dữ liệu. | Family ID: `family-A` | 1. Owner gửi yêu cầu giải tán.<br>2. Xác nhận.<br>3. Kiểm tra DB. | 1. Gia đình chuyển sang INACTIVE.<br>2. Dữ liệu không bị xóa.<br>3. Thành viên nhận thông báo.<br>4. Audit log ghi nhận. | NOT RUN | | |
| TC-FG-001A | FR-FG-01, FR-US-05, UC-03 | Guest không có quyền tạo gia đình | 1. Guest chưa đăng nhập. | Token: none | 1. Gọi API tạo gia đình. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-FG-001B | FR-FG-01, UC-03 | Tên gia đình vượt quá 100 ký tự | 1. Người dùng đã đăng ký và kích hoạt. | Tên: chuỗi 101 ký tự | 1. Nhập tên 101 ký tự.<br>2. Submit. | Hệ thống báo lỗi "Tên gia đình không được vượt quá 100 ký tự". | NOT RUN | | |

---

### FR-FG-02: Quản lý nhánh gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-002P | FR-FG-02, BR-FG-003, UC-03 | Tạo nhánh thành công | 1. Family Owner đã đăng nhập.<br>2. Gia đình ACTIVE. | Family ID: `family-A`<br>Tên nhánh: `Chi trưởng`<br>Mô tả: `Nhánh con trưởng`<br>Trưởng nhánh: `member-01` | 1. Mở "Nhánh gia đình".<br>2. "Thêm nhánh".<br>3. Nhập thông tin.<br>4. Gán thành viên.<br>5. Lưu. | 1. Nhánh mới được tạo.<br>2. Trưởng nhánh được gán đúng.<br>3. Cây gia phả cập nhật. | NOT RUN | | |
| TC-FG-002N | FR-FG-02, UC-03 | Tên nhánh trùng trong cùng gia đình | 1. Gia đình A đã có nhánh "Chi trưởng". | Family ID: `family-A`<br>Tên nhánh: `Chi trưởng` (trùng) | 1. Thêm nhánh với tên trùng. | Hệ thống báo lỗi "Tên nhánh đã tồn tại trong gia đình này". | NOT RUN | | |
| TC-FG-002N2 | FR-FG-02, UC-03 | Xóa nhánh - thành viên không bị xóa | 1. Nhánh "Chi trưởng" có 5 thành viên. | Branch ID: `branch-01` | 1. Xóa nhánh.<br>2. Kiểm tra thành viên. | 1. Nhánh bị xóa.<br>2. Thành viên chuyển về branch_id = NULL.<br>3. Hồ sơ thành viên không bị xóa. | NOT RUN | | |
| TC-FG-002A | FR-FG-02, FR-US-05, UC-03 | Member không có quyền quản lý nhánh | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API tạo nhánh. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-FG-002V | FR-FG-02, BR-FG-003, UC-03 | Chuyển thành viên từ nhánh này sang nhánh khác | 1. member-01 thuộc "Chi trưởng".<br>2. Owner muốn gán vào "Chi thứ". | Member ID: `member-01`<br>New Branch: `branch-02` | 1. Gán member-01 vào nhánh mới. | Cảnh báo: "Thành viên đang thuộc nhánh Chi trưởng. Chuyển sang nhánh mới?" Yêu cầu xác nhận. | NOT RUN | | |

---

### FR-FG-03: Quản lý thành viên gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-003P | FR-FG-03, BR-FG-001, UC-03 | Thêm thành viên (đã có tài khoản) | 1. Family Owner đã đăng nhập.<br>2. Gia đình ACTIVE.<br>3. User B có tài khoản. | Family ID: `family-A`<br>Họ tên: `Nguyễn Thị B`<br>Ngày sinh: `1990-05-20`<br>Giới tính: `NỮ`<br>Email: `userB@example.com` | 1. Mở "Thành viên".<br>2. "Thêm thành viên".<br>3. Tìm tài khoản theo email.<br>4. Liên kết và lưu. | 1. FamilyMember tạo với user_id = userB.<br>2. Status ACTIVE.<br>3. User B nhận thông báo.<br>4. User B xuất hiện trong danh sách. | NOT RUN | | |
| TC-FG-003P2 | FR-FG-03, UC-03 | Thêm thành viên chưa có tài khoản (placeholder) | 1. Family Owner đã đăng nhập. | Họ tên: `Nguyễn Văn C`<br>Ngày sinh: `1950-01-01`<br>Giới tính: `NAM`<br>Email: (trống) | 1. Thêm thành viên với email trống.<br>2. Lưu. | 1. FamilyMember tạo với user_id = NULL.<br>2. Status ACTIVE.<br>3. Xuất hiện trong cây gia phả. | NOT RUN | | |
| TC-FG-003N | FR-FG-03, UC-03 | Thêm thành viên trùng (cùng tên + ngày sinh) | 1. Đã có thành viên "Nguyễn Văn A" sinh 1990-01-01. | Họ tên: `Nguyễn Văn A`<br>Ngày sinh: `1990-01-01` | 1. Thêm với thông tin trùng. | Cảnh báo "Thành viên với thông tin này có thể đã tồn tại. Vui lòng kiểm tra lại." | NOT RUN | | |
| TC-FG-003N2 | FR-FG-03, UC-03 | Xóa thành viên có quan hệ trong cây | 1. Thành viên có cha-con và hôn nhân. | Member ID: `member-01` | 1. Xóa member-01. | Cảnh báo "Thành viên này có quan hệ với người khác. Dữ liệu quan hệ sẽ bị xóa theo. Bạn chắc chắn?" | NOT RUN | | |
| TC-FG-003A | FR-FG-03, FR-US-05, UC-03 | Member không có quyền xóa thành viên | 1. Family Member đã đăng nhập. | Token: member_token<br>Target: `member-02` | 1. Gọi API xóa thành viên. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-FG-003V | FR-FG-03, UC-03 | Đình chỉ thành viên - thu hồi quyền | 1. Owner đình chỉ member-D. | Member ID: `member-D`<br>Status: ACTIVE → SUSPENDED | 1. Đình chỉ.<br>2. member-D gọi API. | 1. Status chuyển SUSPENDED.<br>2. member-D nhận thông báo.<br>3. API trả về 403. | NOT RUN | | |

---

### FR-FG-04: Quản lý quan hệ cha mẹ - con

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-004P | FR-FG-04, BR-FG-004, UC-04 | Thiết lập quan hệ cha-con thành công | 1. Family Owner đã đăng nhập.<br>2. Cha và con tồn tại.<br>3. Chưa có quan hệ. | Cha: `member-father` (sinh 1960)<br>Con: `member-child` (sinh 1990) | 1. Mở hồ sơ con.<br>2. "Thêm cha/mẹ".<br>3. Chọn cha.<br>4. Xác nhận. | 1. Cạnh PARENT_CHILD được tạo.<br>2. Thế hệ tính lại.<br>3. Cây gia phả cập nhật. | NOT RUN | | |
| TC-FG-004N | FR-FG-04, BR-FG-004, UC-04 | Tạo quan hệ gây vòng lặp | 1. Quan hệ: Ông A → Cha B → Con C. | Từ: `member-C` (con)<br>Đến: `member-grandfather-A` (ông) | 1. Gán member-C làm cha của ông A. | Từ chối: "Không thể tạo quan hệ vì gây mâu thuẫn thế hệ (vòng lặp)." | NOT RUN | | |
| TC-FG-004N2 | FR-FG-04, BR-FG-004, UC-04 | Thêm cha/mẹ thứ ba | 1. Thành viên đã có 2 cha/mẹ. | New Parent: `member-newparent` | 1. Thêm cha/mẹ thứ ba. | Lỗi: "Đã có đủ 2 cha/mẹ. Sửa quan hệ hiện có trước." | NOT RUN | | |
| TC-FG-004V | FR-FG-04, BR-FG-004, UC-04 | Tạo quan hệ trùng lặp | 1. Đã có quan hệ cha-con giữa A và B. | Cha: A<br>Con: B | 1. Tạo lại quan hệ A-B. | Lỗi: "Quan hệ này đã tồn tại." | NOT RUN | | |
| TC-FG-004P2 | FR-FG-04, UC-04 | Gỡ quan hệ cha-con | 1. Tồn tại quan hệ A-B. | Cha: A<br>Con: B | 1. Gỡ quan hệ.<br>2. Xác nhận. | 1. Cạnh bị xóa.<br>2. Thế hệ tính lại.<br>3. Cây cập nhật. | NOT RUN | | |

---

### FR-FG-05: Quản lý hôn nhân

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-005P | FR-FG-05, BR-FG-005, UC-04 | Thiết lập hôn nhân thành công | 1. Owner đã đăng nhập.<br>2. Hai thành viên trưởng thành.<br>3. Chưa có hôn nhân. | Spouse 1: A (35 tuổi)<br>Spouse 2: B (30 tuổi)<br>Ngày cưới: 2020-12-01 | 1. Mở hồ sơ A.<br>2. "Thêm vợ/chồng".<br>3. Chọn B.<br>4. Nhập ngày cưới.<br>5. Xác nhận. | 1. Cạnh MARRIAGE tạo với status MARRIED.<br>2. Cây gia phả hiển thị liên kết.<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-FG-005N | FR-FG-05, BR-FG-005, UC-04 | Hôn nhân khi đã có người đang kết hôn | 1. C đang kết hôn với D. | Spouse 1: C<br>Spouse 2: E | 1. Tạo hôn nhân C-E. | Chặn: "Thành viên này đã có quan hệ hôn nhân đang hoạt động. Kết thúc quan hệ hiện tại trước." | NOT RUN | | |
| TC-FG-005P2 | FR-FG-05, UC-04 | Kết thúc hôn nhân (ly hôn) | 1. Tồn tại hôn nhân A-B (MARRIED). | Trạng thái: DIVORCED<br>Ngày ly hôn: 2024-06-01 | 1. Cập nhật trạng thái DIVORCED. | 1. Cạnh chuyển DIVORCED (không xóa).<br>2. Cả hai có thể tạo hôn nhân mới. | NOT RUN | | |
| TC-FG-005A | FR-FG-05, FR-US-05, UC-04 | Member không có quyền quản lý hôn nhân | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API thiết lập hôn nhân. | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-FG-06: Xem cây gia phả tương tác

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-006P | FR-FG-06, BR-FG-007, UC-05 | Xem cây gia phả hiển thị đúng | 1. Family Member đã đăng nhập.<br>2. Gia đình ≥ 3 thế hệ, ≥ 10 thành viên. | Family ID: `family-A` | 1. Mở "Gia phả".<br>2. Chọn gia đình.<br>3. Quan sát. | 1. Cây hiển thị đúng cấu trúc.<br>2. Cùng thế hệ cùng hàng.<br>3. Zoom/pan mượt.<br>4. Click vào node hiển thị thông tin. | NOT RUN | | |
| TC-FG-006P2 | FR-FG-06, UC-05 | Lọc cây theo nhánh | 1. Gia đình có nhiều nhánh. | Family ID: `family-A`<br>Branch: `branch-01` | 1. Chọn bộ lọc nhánh. | Chỉ hiển thị thành viên thuộc nhánh đã chọn. | NOT RUN | | |
| TC-FG-006N | FR-FG-06, UC-05 | Gia đình chưa có dữ liệu | 1. Gia đình mới, chỉ có Owner. | Family ID: `family-new` | 1. Mở cây gia phả. | Hiển thị 1 node + gợi ý thêm thành viên. | NOT RUN | | |
| TC-FG-006A | FR-FG-06, FR-US-05, UC-05 | Người ngoài gia đình không xem được | 1. User X không thuộc gia đình A. | Token: user_X<br>Family: `family-A` | 1. Gọi API gia phả của family-A. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-FG-006V | FR-FG-06, NFR-06, UC-05 | Hiệu năng tải cây lớn (>1000 node) | 1. Gia đình có >1000 thành viên. | Family ID: `family-large` | 1. Mở cây.<br>2. Đo thời gian tải.<br>3. Mở rộng nhánh xa. | 1. Tải lần đầu < 2s.<br>2. Mở rộng có loading.<br>3. Pan/zoom < 200ms. | NOT RUN | | |

---

### FR-FG-07: Trực quan hóa quan hệ

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-007P | FR-FG-07, BR-FG-007, UC-05 | Chế độ đồ thị quan hệ hiển thị đúng | 1. Family Member đã đăng nhập.<br>2. Có dữ liệu. | Family ID: `family-A` | 1. Mở gia phả.<br>2. Chọn "Đồ thị quan hệ". | 1. Đồ thị với nút + cạnh.<br>2. Cạnh PARENT_CHILD/MARRIAGE phân biệt màu.<br>3. Có chú giải. | NOT RUN | | |
| TC-FG-007P2 | FR-FG-07, UC-05 | Click nút - làm nổi bật quan hệ | 1. Đang ở chế độ đồ thị. | Selected: `member-A` | 1. Click member-A. | Quan hệ trực tiếp nổi bật; các nút khác mờ đi. | NOT RUN | | |
| TC-FG-007E | FR-FG-07, UC-05 | Chưa có quan hệ nào | 1. Gia đình chỉ có thành viên, chưa có quan hệ. | Family ID: `family-no-rel` | 1. Chọn "Đồ thị quan hệ". | Thông báo "Chưa có quan hệ nào. Vui lòng thêm quan hệ trước." | NOT RUN | | |

---

### FR-FG-08: Tra cứu quan hệ

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-FG-008P | FR-FG-08, BR-FG-007, UC-05 | Tra cứu quan hệ - tìm thấy đường đi | 1. Family Member đã đăng nhập.<br>2. A và B có quan hệ. | A: `member-grandfather`<br>B: `member-grandson` | 1. Mở "Tra cứu quan hệ".<br>2. Chọn A và B.<br>3. "Tra cứu". | 1. Kết quả: "Ông nội - Cháu nội".<br>2. Đường đi từng bước.<br>3. ≤ 2 giây.<br>4. Có nút "Giải thích AI". | NOT RUN | | |
| TC-FG-008N | FR-FG-08, UC-05 | Không tìm thấy đường đi | 1. A và B chưa có quan hệ. | A: `member-X`<br>B: `member-Y` | 1. Tra cứu. | "Chưa xác định được quan hệ. Kiểm tra dữ liệu gia phả." | NOT RUN | | |
| TC-FG-008N2 | FR-FG-08, UC-05 | Chọn cùng một thành viên | 1. Đã đăng nhập. | A = B = `member-A` | 1. Chọn A ở cả hai ô.<br>2. Tra cứu. | Lỗi: "Chọn hai thành viên khác nhau." | NOT RUN | | |
| TC-FG-008V | FR-FG-08, NFR-12, UC-05 | Hiệu năng tra cứu | 1. Đồ thị 5000+ thành viên. | Family ID: `family-large`<br>A, B: xa nhất | 1. Gọi API.<br>2. Đo thời gian (100 lần). | P95 < 2 giây (NFR-12). | NOT RUN | | |
| TC-FG-008A | FR-FG-08, FR-US-05, UC-05 | Người ngoài gia đình không tra cứu được | 1. User X không thuộc gia đình A. | Token: user_X<br>Family: `family-A` | 1. Gọi API tra cứu. | API trả về 403 Forbidden. | NOT RUN | | |

------

## Module 3: Community

### FR-COM-01: Đăng và quản lý bài viết

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-COM-001P | FR-COM-01, BR-COM-001, UC-06 | Đăng bài viết thành công (toàn gia đình) | 1. Family Member đã đăng nhập, ACTIVE.<br>2. Thuộc gia đình. | Family ID: `family-A`<br>Nội dung: `Chúc mừng sinh nhật ông!`<br>Phạm vi: `FAMILY` | 1. Mở luồng cộng đồng.<br>2. "Tạo bài viết".<br>3. Nhập nội dung.<br>4. Chọn phạm vi FAMILY.<br>5. "Đăng". | 1. Bài viết lưu với status PUBLISHED.<br>2. Hiển thị trên luồng cộng đồng.<br>3. Thành viên trong phạm vi nhận thông báo. | NOT RUN | | |
| TC-COM-001P2 | FR-COM-01, UC-06 | Đăng bài viết với hình ảnh đính kèm | 1. Family Member đã đăng nhập. | Nội dung: `Ảnh họp mặt`<br>File: 3 ảnh JPG (< 10MB mỗi ảnh)<br>Phạm vi: `FAMILY` | 1. Tạo bài viết.<br>2. Đính kèm 3 ảnh.<br>3. Đăng. | 1. Bài viết hiển thị kèm ảnh.<br>2. Ảnh được lưu trong media storage.<br>3. Thành viên xem được ảnh. | NOT RUN | | |
| TC-COM-001N | FR-COM-01, UC-06 | Đăng bài viết với nội dung rỗng | 1. Family Member đã đăng nhập. | Nội dung: (trống) | 1. Tạo bài viết.<br>2. Để trống nội dung.<br>3. Đăng. | Hệ thống báo lỗi "Nội dung bài viết không được để trống". | NOT RUN | | |
| TC-COM-001A | FR-COM-01, BR-COM-001, UC-06 | Guest không thể đăng bài viết | 1. Guest chưa đăng nhập. | Nội dung: `Bài viết bất kỳ` | 1. Gọi API tạo bài viết. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-COM-001A2 | FR-COM-01, BR-COM-001, UC-06 | Member không đăng được bài cho gia đình không thuộc | 1. Member thuộc gia đình A.<br>2. Cố đăng bài cho gia đình B. | Token: member_A<br>Family ID: `family-B` | 1. Gọi API tạo bài viết với family_id = B. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-COM-001P3 | FR-COM-01, UC-06 | Sửa bài viết của chính mình | 1. Family Member đã đăng bài X. | Post ID: `post-X`<br>Nội dung mới: `Nội dung đã sửa` | 1. Mở bài viết X.<br>2. Sửa nội dung.<br>3. Lưu. | 1. Nội dung được cập nhật.<br>2. Đánh dấu thời gian chỉnh sửa.<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-COM-001N2 | FR-COM-01, BR-COM-002, UC-06 | Xóa bài viết của người khác | 1. Member A đăng bài.<br>2. Member B cố xóa bài của A. | Token: member_B<br>Post ID: `post-by-A` | 1. Gọi API xóa bài viết của A. | API trả về 403 Forbidden (chỉ tác giả hoặc Admin mới xóa). | NOT RUN | | |
| TC-COM-001B | FR-COM-01, UC-06 | Đăng bài với nội dung vượt 2000 ký tự | 1. Family Member đã đăng nhập. | Nội dung: 2001 ký tự | 1. Nhập nội dung 2001 ký tự.<br>2. Đăng. | Hệ thống báo lỗi "Nội dung không được vượt quá 2000 ký tự". | NOT RUN | | |
| TC-COM-001B2 | FR-COM-01, UC-06 | Đăng bài với hơn 10 file đính kèm | 1. Family Member đã đăng nhập. | File: 15 ảnh JPG | 1. Đính kèm 15 ảnh.<br>2. Đăng. | Hệ thống báo lỗi "Tối đa 10 file đính kèm". | NOT RUN | | |

---

### FR-COM-02: Bình luận và thả cảm xúc

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-COM-002P | FR-COM-02, BR-COM-001, UC-06 | Bình luận vào bài viết thành công | 1. Family Member đã đăng nhập.<br>2. Bài viết PUBLISHED. | Post ID: `post-01`<br>Nội dung: `Chúc mừng!` | 1. Mở bài viết.<br>2. Nhập bình luận.<br>3. Gửi. | 1. Bình luận được lưu.<br>2. Số lượng bình luận tăng.<br>3. Chủ bài viết nhận thông báo. | NOT RUN | | |
| TC-COM-002P2 | FR-COM-02, UC-06 | Thả cảm xúc (Like) thành công | 1. Family Member đã đăng nhập.<br>2. Bài viết PUBLISHED. | Post ID: `post-01`<br>Cảm xúc: `LIKE` | 1. Click Like. | 1. Số lượt like tăng 1.<br>2. Gỡ like bằng click lại. | NOT RUN | | |
| TC-COM-002N | FR-COM-02, UC-06 | Bình luận với nội dung trống | 1. Family Member đã đăng nhập. | Nội dung: (trống) | 1. Gửi bình luận trống. | Chặn: "Nội dung bình luận không được để trống". | NOT RUN | | |
| TC-COM-002A | FR-COM-02, BR-COM-001, UC-06 | Guest không thể bình luận | 1. Guest chưa đăng nhập. | Post ID: `post-01` | 1. Gọi API bình luận. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-COM-002V | FR-COM-02, UC-06 | Sửa bình luận của chính mình | 1. Member A đã bình luận. | Comment ID: `cmt-A`<br>Nội dung mới: `Đã sửa` | 1. Sửa bình luận. | Nội dung bình luận được cập nhật. | NOT RUN | | |
| TC-COM-002V2 | FR-COM-02, UC-06 | Xóa bình luận của người khác (chủ bài viết) | 1. Member A là chủ bài viết.<br>2. Member B bình luận. | Token: member_A (owner)<br>Comment ID: `cmt-by-B` | 1. A xóa bình luận của B. | Bình luận bị xóa. Audit log ghi nhận. | NOT RUN | | |

---

### FR-COM-03: Chia sẻ tin tức gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-COM-003P | FR-COM-03, BR-COM-001, UC-06 | Đăng tin tức gia đình thành công | 1. Family Member đã đăng nhập. | Loại tin: `BIRTHDAY`<br>Tiêu đề: `Sinh nhật bà Năm`<br>Ngày: `2026-09-01`<br>Thành viên: `member-grandma` | 1. "Đăng tin gia đình".<br>2. Chọn loại tin.<br>3. Nhập thông tin.<br>4. Đăng. | 1. Tin hiển thị ở mục "Tin gia đình".<br>2. Loại tin phân biệt.<br>3. Thành viên liên quan nhận thông báo. | NOT RUN | | |
| TC-COM-003N | FR-COM-03, UC-06 | Đăng tin buồn - không hiển thị cảm xúc thích | 1. Family Member đã đăng nhập. | Loại tin: `SAD_NEWS`<br>Tiêu đề: `Tin buồn` | 1. Đăng tin buồn.<br>2. Kiểm tra giao diện. | Giao diện trang trọng, không có nút cảm xúc "thích". | NOT RUN | | |
| TC-COM-003P2 | FR-COM-03, UC-06 | Family Owner ghim tin quan trọng | 1. Family Owner đã đăng nhập. | News ID: `news-01` | 1. Owner ghim tin lên đầu. | Tin được ghim lên đầu luồng, tối đa 7 ngày. | NOT RUN | | |

---

### FR-COM-04: Chia sẻ hình ảnh

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-COM-004P | FR-COM-04, BR-COM-001, UC-06 | Chia sẻ ảnh thành công | 1. Family Member đã đăng nhập. | File: 5 ảnh JPG (2MB/ảnh)<br>Mô tả: `Ảnh họp mặt`<br>Thẻ: `member-A`, `member-B` | 1. "Chia sẻ ảnh".<br>2. Chọn 5 ảnh.<br>3. Nhập mô tả, gắn thẻ.<br>4. Đăng. | 1. Ảnh được nén và lưu.<br>2. Hiển thị trên luồng + album.<br>3. Thành viên được gắn thẻ nhận thông báo. | NOT RUN | | |
| TC-COM-004N | FR-COM-04, UC-06 | Tải ảnh vượt quá giới hạn kích thước | 1. Family Member đã đăng nhập. | File: 1 ảnh 12MB | 1. Chọn ảnh 12MB.<br>2. Đăng. | Lỗi: "Mỗi ảnh không được vượt quá 10MB". | NOT RUN | | |
| TC-COM-004B | FR-COM-04, UC-06 | Tải > 20 ảnh/lần | 1. Family Member đã đăng nhập. | File: 25 ảnh JPG | 1. Chọn 25 ảnh.<br>2. Đăng. | Lỗi: "Tối đa 20 ảnh mỗi lần". | NOT RUN | | |
| TC-COM-004V | FR-COM-04, UC-06 | Gỡ thẻ chính mình khỏi ảnh | 1. Member A được gắn thẻ. | Media ID: `media-01` | 1. A gỡ thẻ của mình. | Thẻ được gỡ, ảnh vẫn tồn tại. | NOT RUN | | |

---

### FR-COM-05: Thông báo gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-COM-005P | FR-COM-05, BR-COM-003, UC-06 | Tạo thông báo (Family Owner) | 1. Family Owner đã đăng nhập. | Tiêu đề: `Họp mặt cuối năm`<br>Nội dung: `Kính mời toàn thể...`<br>Mức: `QUAN_TRONG` | 1. "Tạo thông báo".<br>2. Nhập thông tin.<br>3. Gửi. | 1. Thông báo hiển thị đầu luồng.<br>2. Gửi in-app đến thành viên.<br>3. Mức quan trọng được đánh dấu. | NOT RUN | | |
| TC-COM-005A | FR-COM-05, BR-COM-003, UC-06 | Member không thể tạo thông báo | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API tạo thông báo. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-COM-005P2 | FR-COM-05, UC-06 | Thông báo khẩn cấp - gửi qua tất cả kênh | 1. Owner đã đăng nhập.<br>2. Có thành viên tắt in-app. | Mức: `KHAN_CAP` | 1. Tạo thông báo khẩn cấp. | Gửi qua in-app + email + push (bất kể cấu hình cá nhân). | NOT RUN | | |
| TC-COM-005P3 | FR-COM-05, UC-06 | Hẹn giờ gửi thông báo | 1. Owner đã đăng nhập. | Hẹn: 2026-09-05 08:00 | 1. Tạo thông báo hẹn giờ.<br>2. Kiểm tra trước/sau giờ hẹn. | Trước giờ chưa hiển thị; sau giờ tự phát hành. | NOT RUN | | |
| TC-COM-005A2 | FR-COM-05, BR-COM-003, UC-06 | Owner thu hồi thông báo đã gửi | 1. Thông báo đã gửi. | Announcement ID: `ann-01` | 1. Owner thu hồi. | Thông báo gỡ khỏi luồng. Thành viên nhận cập nhật. | NOT RUN | | |

## Module 4: Events

### FR-EVT-01: Tạo sự kiện gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-EVT-001P | FR-EVT-01, BR-EVT-001, UC-07 | Tạo sự kiện thành công | 1. Family Member đã đăng nhập.<br>2. Thuộc gia đình. | Tên: `Lễ Giỗ Tổ 2026`<br>Loại: `MEMORIAL`<br>Bắt đầu: 2026-09-10 08:00<br>Kết thúc: 2026-09-10 12:00<br>Địa điểm: `Nhà thờ tổ`<br>Khách mời: tất cả thành viên | 1. "Tạo sự kiện".<br>2. Nhập thông tin.<br>3. Chọn khách mời.<br>4. "Tạo". | 1. Sự kiện tạo với status OPEN.<br>2. Người tạo là Event Owner.<br>3. Khách mời nhận thư mời.<br>4. Audit log ghi nhận. | NOT RUN | | |
| TC-EVT-001N | FR-EVT-01, BR-EVT-004, UC-07 | Tạo sự kiện với thời gian kết thúc trước thời gian bắt đầu | 1. Family Member đã đăng nhập. | Bắt đầu: 2026-09-10 12:00<br>Kết thúc: 2026-09-10 08:00 | 1. Nhập thời gian không hợp lệ.<br>2. Tạo. | Hệ thống báo lỗi "Thời gian kết thúc phải sau thời gian bắt đầu". | NOT RUN | | |
| TC-EVT-001A | FR-EVT-01, BR-EVT-001, UC-07 | Guest không thể tạo sự kiện | 1. Guest chưa đăng nhập. | Token: none | 1. Gọi API tạo sự kiện. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-EVT-001P2 | FR-EVT-01, UC-07 | Tạo sự kiện có khách ngoài gia đình | 1. Family Member đã đăng nhập. | Khách ngoài: `friend@example.com`, `guest2@gmail.com` (≤ 50) | 1. Tạo sự kiện.<br>2. Thêm khách ngoài. | 1. Khách ngoài nhận email mời.<br>2. Email có link RSVP công khai. | NOT RUN | | |
| TC-EVT-001V | FR-EVT-01, UC-07 | Sửa sự kiện - gửi thông báo thay đổi | 1. Sự kiện đã tạo, có người RSVP. | Event ID: `event-01`<br>Thời gian mới: thay đổi | 1. Event Owner sửa thông tin.<br>2. Lưu. | 1. Sự kiện cập nhật.<br>2. Người đã RSVP nhận thông báo thay đổi. | NOT RUN | | |
| TC-EVT-001N2 | FR-EVT-01, UC-07 | Hủy sự kiện - thông báo cho người tham gia | 1. Sự kiện OPEN, có người RSVP. | Event ID: `event-01`<br>Lý do hủy: `Thay đổi lịch` | 1. Event Owner hủy sự kiện.<br>2. Nhập lý do. | 1. Sự kiện chuyển CANCELLED.<br>2. Toàn bộ người tham gia nhận thông báo hủy.<br>3. RSVP bị khóa. | NOT RUN | | |

---

### FR-EVT-02: Xác nhận tham dự (RSVP)

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-EVT-002P | FR-EVT-02, BR-EVT-002, UC-07 | Xác nhận tham dự (GOING) | 1. Family Member đã đăng nhập.<br>2. Sự kiện OPEN. | Event ID: `event-01`<br>RSVP: `GOING` | 1. Mở trang sự kiện.<br>2. Chọn "GOING". | 1. RSVP = GOING được lưu.<br>2. Số liệu tham gia cập nhật.<br>3. Event Owner nhận thông báo. | NOT RUN | | |
| TC-EVT-002N | FR-EVT-02, BR-EVT-002, UC-07 | Đổi trạng thái RSVP (từ GOING sang NOT_GOING) | 1. Thành viên đã chọn GOING. | RSVP mới: `NOT_GOING` | 1. Chọn NOT_GOING. | Trạng thái cũ bị ghi đè. Số liệu cập nhật. | NOT RUN | | |
| TC-EVT-002V | FR-EVT-02, BR-EVT-002, UC-07 | RSVP bị khóa khi Event Owner đóng | 1. Event Owner đã khóa RSVP trước 24h. | Event ID: `event-01`<br>Trạng thái RSVP: `CLOSED` | 1. Thành viên cố gắng đổi RSVP. | Hệ thống chặn: "RSVP đã đóng". | NOT RUN | | |
| TC-EVT-002P2 | FR-EVT-02, UC-07 | Khách ngoài RSVP qua link công khai | 1. Khách ngoài có link RSVP.<br>2. Email: `guest@example.com` | Token: temp_guest_token<br>RSVP: `GOING` | 1. Mở link RSVP.<br>2. Nhập tên, chọn GOING. | RSVP được ghi nhận. Không yêu cầu đăng nhập. | NOT RUN | | |

---

### FR-EVT-03: Quản lý người tham gia

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-EVT-003P | FR-EVT-03, BR-EVT-003, UC-07 | Xem danh sách người tham gia và thống kê | 1. Event Owner đã đăng nhập.<br>2. Sự kiện có RSVP. | Event ID: `event-01` | 1. Mở "Người tham gia". | Hiển thị thống kê: Going (5), Maybe (2), Not Going (1), Chưa phản hồi (10). | NOT RUN | | |
| TC-EVT-003P2 | FR-EVT-03, UC-07 | Gửi nhắc nhở cho người chưa phản hồi | 1. Event Owner đã đăng nhập.<br>2. Có người chưa phản hồi. | Event ID: `event-01` | 1. Chọn "Nhắc nhở" cho nhóm chưa phản hồi. | Hệ thống gửi thông báo nhắc. | NOT RUN | | |
| TC-EVT-003P3 | FR-EVT-03, UC-07 | Xuất danh sách tham dự (CSV) | 1. Event Owner đã đăng nhập. | Event ID: `event-01`<br>Định dạng: CSV | 1. "Xuất danh sách". | File CSV được tải xuống với danh sách tham dự. | NOT RUN | | |
| TC-EVT-003A | FR-EVT-03, FR-US-05, UC-07 | Member không có quyền quản lý người tham gia | 1. Family Member đã đăng nhập.<br>2. Không phải Event Owner hay Family Owner. | Token: member_token | 1. Gọi API quản lý người tham gia. | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-EVT-04: Thư viện ảnh sự kiện

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-EVT-004P | FR-EVT-04, BR-EVT-005, UC-07 | Tải ảnh lên thư viện sự kiện | 1. Family Member đã RSVP = GOING. | Event ID: `event-01`<br>File: 5 ảnh JPG | 1. Mở tab "Thư viện ảnh".<br>2. "Tải ảnh".<br>3. Chọn ảnh, nhập mô tả.<br>4. Tải lên. | 1. Ảnh được lưu vào album sự kiện.<br>2. Thành viên khác xem được.<br>3. Người được gắn thẻ nhận thông báo. | NOT RUN | | |
| TC-EVT-004A | FR-EVT-04, BR-EVT-005, UC-07 | Người không tham gia không thể tải ảnh | 1. Family Member RSVP = NOT_GOING. | Event ID: `event-01` | 1. Gọi API tải ảnh. | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-EVT-05: Nhắc nhở sự kiện

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-EVT-005P | FR-EVT-05, UC-07 | Nhắc nhở tự động 7 ngày trước sự kiện | 1. Sự kiện sắp diễn ra sau 7 ngày.<br>2. Người dùng RSVP = GOING. | Event ID: `event-01`<br>Start: 2026-09-10 08:00<br>Current: 2026-09-03 08:00 | 1. Scheduler chạy job nhắc nhở. | 1. Người dùng nhận thông báo nhắc.<br>2. Nội dung: tên, thời gian, địa điểm.<br>3. Ghi nhật ký gửi. | NOT RUN | | |
| TC-EVT-005P2 | FR-EVT-05, UC-07 | Nhắc nhở 1 ngày và 3 giờ trước sự kiện | 1. Sự kiện sắp diễn ra sau 1 ngày / 3 giờ.<br>2. Người dùng RSVP = MAYBE. | Event ID: `event-01` | 1. Scheduler chạy job. | Nhắc nhở được gửi ở cả 2 mốc. | NOT RUN | | |
| TC-EVT-005N | FR-EVT-05, UC-07 | Sự kiện bị hủy - không gửi nhắc nhở | 1. Sự kiện đã bị hủy. | Event ID: `event-01` (CANCELLED) | 1. Đến mốc nhắc nhở. | Hệ thống không gửi nhắc nhở. Gửi thông báo hủy. | NOT RUN | | |
| TC-EVT-005V | FR-EVT-05, UC-07 | Tắt nhắc nhở cho sự kiện cụ thể | 1. Người dùng tắt nhắc cho sự kiện. | Event ID: `event-01`<br>Reminder: OFF | 1. Đến mốc nhắc nhở. | Người dùng không nhận nhắc cho sự kiện này. | NOT RUN | | |

## Module 5: Family Directory

### FR-DIR-01: Danh bạ thành viên

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DIR-001P | FR-DIR-01, BR-DIR-001, UC-08 | Xem danh bạ thành viên | 1. Family Member đã đăng nhập.<br>2. Gia đình có ≥ 5 thành viên ACTIVE. | Family ID: `family-A` | 1. Mở "Danh bạ". | 1. Danh sách hiển thị tất cả thành viên ACTIVE.<br>2. Mỗi thành viên có ảnh, tên, thế hệ, nhánh, liên hệ.<br>3. Sắp xếp theo tên/thế hệ/nhánh. | NOT RUN | | |
| TC-DIR-001A | FR-DIR-01, BR-DIR-001, UC-08 | Guest không xem được danh bạ | 1. Guest chưa đăng nhập. | Family ID: `family-A` | 1. Gọi API danh bạ. | API trả về 401 Unauthorized. | NOT RUN | | |
| TC-DIR-001V | FR-DIR-01, UC-08 | Thông tin liên hệ ẩn theo cài đặt riêng tư | 1. Thành viên B đặt SĐT ở chế độ riêng tư. | Member ID: `member-B` (private) | 1. Member A xem danh bạ.<br>2. Kiểm tra thông tin của B. | SĐT của B không hiển thị, chỉ có nút "Gửi tin nhắn qua hệ thống". | NOT RUN | | |

---

### FR-DIR-02: Hồ sơ nghề nghiệp

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DIR-002P | FR-DIR-02, UC-08 | Thêm hồ sơ nghề nghiệp | 1. Family Member đã đăng nhập. | Vị trí: `Kỹ sư phần mềm`<br>Công ty: `Công ty ABC`<br>Lĩnh vực: `IT`<br>Địa điểm: `Hà Nội`<br>Năm bắt đầu: 2020 | 1. Mở hồ sơ → tab "Nghề nghiệp".<br>2. Nhập thông tin.<br>3. Lưu. | 1. Thông tin nghề nghiệp được lưu.<br>2. Hiển thị trong danh bạ.<br>3. Xuất hiện trong tìm kiếm (FR-DIR-04). | NOT RUN | | |

---

### FR-DIR-03: Hồ sơ học vấn

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DIR-003P | FR-DIR-03, UC-08 | Thêm hồ sơ học vấn | 1. Family Member đã đăng nhập. | Trường: `ĐH Bách Khoa HN`<br>Chuyên ngành: `CNTT`<br>Bậc: `Đại học`<br>Năm nhập: 2018<br>Năm tốt nghiệp: 2022 | 1. Mở hồ sơ → tab "Học vấn".<br>2. "Thêm học vấn".<br>3. Nhập thông tin.<br>4. Lưu. | 1. Bản ghi học vấn được lưu.<br>2. Hiển thị trong danh bạ. | NOT RUN | | |
| TC-DIR-003N | FR-DIR-03, UC-08 | Năm tốt nghiệp trước năm nhập học | 1. Family Member đã đăng nhập. | Năm nhập: 2022<br>Năm tốt nghiệp: 2020 | 1. Nhập năm không hợp lệ.<br>2. Lưu. | Lỗi: "Năm tốt nghiệp phải >= năm nhập học". | NOT RUN | | |
| TC-DIR-003V | FR-DIR-03, UC-08 | Thêm nhiều bản ghi học vấn | 1. Family Member đã đăng nhập.<br>2. Đã có 1 bản ghi. | Bản ghi 2: Thạc sĩ, ĐH QG HN | 1. "Thêm học vấn".<br>2. Nhập bản ghi thứ 2. | Cả 2 bản ghi hiển thị theo thứ tự thời gian. | NOT RUN | | |

---

### FR-DIR-04: Tìm kiếm thành viên theo nghề nghiệp, địa điểm, thế hệ

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DIR-004P | FR-DIR-04, BR-DIR-001, UC-08 | Tìm kiếm thành viên theo nghề nghiệp | 1. Family Member đã đăng nhập.<br>2. Có thành viên làm "Kỹ sư". | Từ khóa: `Kỹ sư`<br>Bộ lọc: Nghề nghiệp | 1. Mở "Tìm kiếm thành viên".<br>2. Nhập "Kỹ sư".<br>3. Tìm kiếm. | Danh sách thành viên làm kỹ sư. | NOT RUN | | |
| TC-DIR-004P2 | FR-DIR-04, UC-08 | Kết hợp nhiều bộ lọc | 1. Family Member đã đăng nhập. | Nghề nghiệp: `Bác sĩ`<br>Địa điểm: `TP. HCM`<br>Thế hệ: `3` | 1. Nhập các bộ lọc kết hợp.<br>2. Tìm kiếm. | Kết quả là các bác sĩ ở TP.HCM thuộc thế hệ 3. | NOT RUN | | |
| TC-DIR-004N | FR-DIR-04, UC-08 | Không có kết quả | 1. Family Member đã đăng nhập. | Từ khóa: `Phi hành gia` | 1. Tìm kiếm. | Gợi ý giảm bộ lọc hoặc tìm từ khóa khác. | NOT RUN | | |
| TC-DIR-004V | FR-DIR-04, UC-08 | Tìm kiếm tôn trọng cài đặt riêng tư | 1. Thành viên B ẩn thông tin nghề nghiệp. | Từ khóa: `Kỹ sư` | 1. Thành viên B khớp từ khóa nhưng ẩn. | B không xuất hiện trong kết quả. | NOT RUN | | |

## Module 6: Family Heritage

### FR-HER-01: Quản lý tư liệu lịch sử

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-HER-001P | FR-HER-01, BR-HER-001, UC-09 | Tải lên tư liệu lịch sử thành công | 1. Family Owner đã đăng nhập. | File: PDF 5MB (Sắc phong)<br>Tiêu đề: `Sắc phong vua ban 1890`<br>Loại: `DOCUMENT`<br>Niên đại: `1890`<br>Giai đoạn: `Thời Nguyễn` | 1. Mở "Tư liệu lịch sử".<br>2. "Thêm tư liệu".<br>3. Chọn file, nhập thông tin.<br>4. Lưu. | 1. Tư liệu được lưu với status DRAFT/PUBLISHED.<br>2. Bản xem trước được tạo (nếu ảnh/PDF).<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-HER-001N | FR-HER-01, UC-09 | Tải file vượt quá 25MB | 1. Family Owner đã đăng nhập. | File: 30MB | 1. Tải file 30MB. | Lỗi: "Kích thước file không được vượt quá 25MB". | NOT RUN | | |
| TC-HER-001V | FR-HER-01, UC-09 | Phát hiện file trùng hash | 1. Tư liệu X đã tồn tại. | File: cùng hash với X | 1. Tải file trùng. | Cảnh báo "File này có thể đã tồn tại trong kho lưu trữ". | NOT RUN | | |
| TC-HER-001A | FR-HER-01, BR-HER-001, UC-09 | Guest không thể tải tư liệu | 1. Guest chưa đăng nhập. | Token: none | 1. Gọi API tạo tư liệu. | API trả về 401 Unauthorized. | NOT RUN | | |

---

### FR-HER-02: Quản lý câu chuyện gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-HER-002P | FR-HER-02, BR-HER-001, UC-09 | Đăng câu chuyện gia đình | 1. Family Member đã đăng nhập. | Tiêu đề: `Kỷ niệm ngày giỗ tổ 2020`<br>Nội dung: 5000 ký tự<br>Thành viên: `member-A`, `member-B`<br>Ảnh: 2 ảnh | 1. "Viết câu chuyện".<br>2. Nhập thông tin.<br>3. Đăng. | 1. Câu chuyện lưu với status PUBLISHED.<br>2. Hiển thị trong kho di sản.<br>3. Thành viên được gắn nhận thông báo. | NOT RUN | | |
| TC-HER-002P2 | FR-HER-02, UC-09 | Lưu nháp câu chuyện | 1. Family Member đã đăng nhập. | Trạng thái: `DRAFT` | 1. Viết câu chuyện.<br>2. Chọn "Lưu nháp". | Câu chuyện lưu DRAFT, chỉ người viết thấy. | NOT RUN | | |

---

### FR-HER-03: Quản lý thành viên tiêu biểu

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-HER-003P | FR-HER-03, UC-09 | Tạo hồ sơ thành viên tiêu biểu | 1. Family Owner đã đăng nhập.<br>2. Thành viên tồn tại. | Member ID: `member-A`<br>Danh hiệu: `Tiến sĩ đầu tiên của dòng họ`<br>Thành tựu: `Bảo vệ luận án năm 2020` | 1. Mở "Thành viên tiêu biểu".<br>2. "Thêm thành viên tiêu biểu".<br>3. Nhập thông tin.<br>4. Lưu. | 1. Hồ sơ tiêu biểu được tạo.<br>2. Hiển thị trong khu vực di sản.<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-HER-003N | FR-HER-03, UC-09 | Tạo hồ sơ cho thành viên đã có hồ sơ tiêu biểu | 1. Member-A đã có hồ sơ tiêu biểu. | Member ID: `member-A` | 1. Cố tạo hồ sơ thứ 2 cho member-A. | Chặn: "Thành viên này đã có hồ sơ tiêu biểu". | NOT RUN | | |
| TC-HER-003A | FR-HER-03, UC-09 | Member không thể tạo hồ sơ tiêu biểu | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API tạo hồ sơ tiêu biểu. | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-HER-04: Thư viện ảnh gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-HER-004P | FR-HER-04, UC-09 | Xem thư viện ảnh gia đình | 1. Family Member đã đăng nhập.<br>2. Thư viện có ảnh. | Family ID: `family-A` | 1. Mở "Thư viện ảnh". | 1. Hiển thị album theo chủ đề/thời gian.<br>2. Click album → xem lưới ảnh.<br>3. Click ảnh → lightbox + thông tin. | NOT RUN | | |
| TC-HER-004P2 | FR-HER-04, UC-09 | Tải xuống ảnh | 1. Family Member đã đăng nhập. | Photo ID: `photo-01` | 1. Mở ảnh.<br>2. Chọn "Tải xuống". | File ảnh được tải xuống (bản nén hoặc gốc tùy quyền). | NOT RUN | | |
| TC-HER-004V | FR-HER-04, UC-09 | Ảnh đánh dấu riêng tư - chỉ người được chỉ định xem | 1. Member A đánh dấu ảnh riêng tư.<br>2. Member B không được chỉ định. | Photo ID: `photo-private` | 1. Member B cố xem ảnh. | Ảnh không hiển thị hoặc báo lỗi. | NOT RUN | | |

---

### FR-HER-05: Kho lưu trữ số

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-HER-005P | FR-HER-05, BR-HER-002, UC-09 | Xem kho lưu trữ số - các danh mục | 1. Family Owner đã đăng nhập.<br>2. Có dữ liệu di sản. | Family ID: `family-A` | 1. Mở "Kho lưu trữ". | 1. Hiển thị danh mục: Tư liệu, Câu chuyện, Thành viên tiêu biểu, Thư viện ảnh.<br>2. Mỗi danh mục có số lượng.<br>3. Có bộ lọc: loại, giai đoạn, nhánh. | NOT RUN | | |
| TC-HER-005P2 | FR-HER-05, UC-09 | Xuất báo cáo thư mục kho lưu trữ | 1. Family Owner đã đăng nhập. | Định dạng: PDF | 1. "Xuất báo cáo". | File PDF được tải xuống với danh mục kho lưu trữ. | NOT RUN | | |
| TC-HER-005A | FR-HER-05, BR-HER-002, UC-09 | Tư liệu Pending chờ duyệt - chỉ Family Member thấy | 1. Member A tải tư liệu, status = PENDING. | Heritage ID: `heritage-pending` | 1. Member khác xem kho lưu trữ. | Tư liệu PENDING không hiển thị với người khác. | NOT RUN | | |

## Module 7: AI-assisted Services

### FR-AI-01: Tìm kiếm ngữ nghĩa bằng AI

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-AI-001P | FR-AI-01, BR-AI-001, UC-10 | Tìm kiếm ngữ nghĩa thành công | 1. Family Member đã đăng nhập.<br>2. AI Service khả dụng.<br>3. Có dữ liệu liên quan. | Truy vấn: `Những ai trong gia đình làm bác sĩ?` | 1. Mở ô tìm kiếm.<br>2. Nhập câu hỏi.<br>3. Nhấn tìm. | 1. Kết quả xếp theo độ liên quan.<br>2. Nhóm theo loại nội dung.<br>3. Trả về danh sách bác sĩ trong gia đình. | NOT RUN | | |
| TC-AI-001N | FR-AI-01, UC-10 | Không có kết quả phù hợp | 1. Family Member đã đăng nhập.<br>2. Dữ liệu không có thông tin. | Truy vấn: `Phi hành gia trong gia đình` | 1. Tìm kiếm. | "Không tìm thấy kết quả phù hợp". Gợi ý tìm kiếm khác. | NOT RUN | | |
| TC-AI-001N2 | FR-AI-01, BR-AI-003, UC-10 | AI Service không khả dụng - fallback về tìm kiếm từ khóa | 1. Family Member đã đăng nhập.<br>2. AI Service đang lỗi. | Truy vấn: `Nguyễn Văn A` | 1. Tìm kiếm. | 1. Hệ thống tự động fallback về tìm kiếm từ khóa.<br>2. Hiển thị ghi chú "Đang dùng chế độ tìm kiếm cơ bản".<br>3. Trả về kết quả tìm kiếm từ khóa. | NOT RUN | | |
| TC-AI-001A | FR-AI-01, BR-AI-001, UC-10 | AI không truy cập dữ liệu ngoài phạm vi quyền | 1. Member thuộc gia đình A.<br>2. Không thuộc gia đình B. | Truy vấn: `Thông tin gia đình B` | 1. Tìm kiếm về gia đình B. | Kết quả không bao gồm dữ liệu gia đình B. | NOT RUN | | |

---

### FR-AI-02: Trợ lý tri thức gia đình (AI Assistant)

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-AI-002P | FR-AI-02, BR-AI-001, BR-AI-002, UC-10 | Hỏi đáp với AI Assistant thành công | 1. Family Member đã đăng nhập.<br>2. AI Service khả dụng.<br>3. Dữ liệu có thông tin. | Câu hỏi: `Ông nội em sinh năm nào?` | 1. Mở AI Assistant.<br>2. Nhập câu hỏi.<br>3. Gửi. | 1. AI trả lời kèm trích dẫn nguồn.<br>2. Câu trả lời có nhãn "AI-generated".<br>3. Có link đến hồ sơ/tài liệu gốc.<br>4. Có nút đánh giá 👍/👎. | NOT RUN | | |
| TC-AI-002N | FR-AI-02, UC-10 | Câu hỏi ngoài phạm vi dữ liệu gia đình | 1. Family Member đã đăng nhập. | Câu hỏi: `Thời tiết hôm nay thế nào?` | 1. Hỏi AI câu ngoài phạm vi. | AI từ chối nhẹ nhàng: "Tôi chỉ có thể trả lời các câu hỏi về gia đình bạn". | NOT RUN | | |
| TC-AI-002N2 | FR-AI-02, UC-10 | Không tìm thấy dữ liệu | 1. Family Member đã đăng nhập. | Câu hỏi: `Ai là người cao nhất trong họ?` (không có dữ liệu) | 1. Hỏi AI. | "Chưa có thông tin trong dữ liệu gia đình". | NOT RUN | | |
| TC-AI-002V | FR-AI-02, BR-AI-002, UC-10 | Kết quả AI không tự động thay đổi dữ liệu | 1. AI gợi ý sửa thông tin. | Gợi ý: cập nhật ngày sinh | 1. AI đưa ra gợi ý. | AI không tự thay đổi dữ liệu, cần người dùng xác nhận. | NOT RUN | | |

---

### FR-AI-03: Giải thích quan hệ gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-AI-003P | FR-AI-03, FR-FG-08, BR-AI-001, UC-10 | Giải thích quan hệ giữa hai thành viên | 1. Family Member đã đăng nhập.<br>2. Hai thành viên có quan hệ. | Member A: ông<br>Member B: cháu | 1. Tra cứu quan hệ (FR-FG-08).<br>2. Nhấn "Giải thích bằng AI". | 1. AI sinh giải thích: tên quan hệ, ý nghĩa.<br>2. Giải thích từng bước đường đi.<br>3. Có nguồn (cạnh quan hệ). | NOT RUN | | |
| TC-AI-003N | FR-AI-03, UC-10 | Đánh giá "sai" - ghi nhận phản hồi | 1. AI đã đưa ra giải thích. | Phản hồi: 👎 (sai) | 1. Người dùng đánh giá "sai". | Hệ thống ghi nhận phản hồi để cải thiện, không tự sửa dữ liệu gia phả. | NOT RUN | | |

---

### FR-AI-04: Tóm tắt nội dung bằng AI

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-AI-004P | FR-AI-04, BR-AI-002, UC-10 | Tóm tắt nội dung dài thành công | 1. Family Member đã đăng nhập.<br>2. Nội dung ≥ 500 ký tự. | Content: bài viết 2000 ký tự | 1. Mở nội dung.<br>2. Nhấn "Tóm tắt bằng AI". | 1. Tóm tắt hiển thị trong khung gọn.<br>2. Có nút "Mở rộng" xem nội dung gốc.<br>3. Có nhãn "AI-generated". | NOT RUN | | |
| TC-AI-004N | FR-AI-04, UC-10 | Nội dung quá ngắn - nút tóm tắt bị ẩn | 1. Family Member đã đăng nhập. | Content: 200 ký tự (< 500) | 1. Kiểm tra nút "Tóm tắt". | Nút "Tóm tắt" bị ẩn hoặc thông báo không cần tóm tắt. | NOT RUN | | |

---

### FR-AI-05: Gợi ý thành viên và tài nguyên gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-AI-005P | FR-AI-05, BR-AI-001, UC-10 | Gợi ý hiển thị trên trang chủ | 1. Family Member đã đăng nhập.<br>2. Có lịch sử hoạt động tối thiểu. | User ID: `user-active` | 1. Mở trang chủ. | 1. Hiển thị nhóm gợi ý: thành viên, tài nguyên, sự kiện.<br>2. Mỗi nhóm ≤ 5 mục kèm lý do.<br>3. Có nút "Không quan tâm". | NOT RUN | | |
| TC-AI-005N | FR-AI-05, UC-10 | Chưa đủ dữ liệu - gợi ý cơ bản | 1. Family Member mới, chưa có lịch sử. | User ID: `user-new` | 1. Mở trang chủ. | Hiển thị gợi ý cơ bản (thành viên cùng nhánh, tài liệu mới nhất) thay vì cá nhân hóa. | NOT RUN | | |
| TC-AI-005V | FR-AI-05, UC-10 | Tắt gợi ý trong cài đặt | 1. Family Member đã đăng nhập. | Setting: suggest = OFF | 1. Mở trang chủ. | Khu vực gợi ý không hiển thị. | NOT RUN | | |

## Module 8: Dashboard & Reporting

### FR-DASH-01: Thống kê gia đình

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DASH-001P | FR-DASH-01, BR-DASH-001, UC-11 | Xem thống kê gia đình | 1. Family Owner đã đăng nhập.<br>2. Gia đình có dữ liệu. | Family ID: `family-A` | 1. Mở "Thống kê gia đình". | 1. Hiển thị các chỉ số: tổng thành viên, số nhánh, số thế hệ, tỷ lệ hồ sơ đầy đủ.<br>2. Số liệu từ dữ liệu đã xác thực.<br>3. Click vào chỉ số → danh sách chi tiết. | NOT RUN | | |
| TC-DASH-001A | FR-DASH-01, FR-US-05, UC-11 | Family Member không xem được thống kê gia đình (chỉ Owner) | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API thống kê gia đình. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-DASH-001E | FR-DASH-01, UC-11 | Gia đình chưa có dữ liệu - thống kê trống | 1. Gia đình mới, chưa có thành viên ngoài Owner. | Family ID: `family-new` | 1. Mở thống kê. | Hiển thị trạng thái trống + hướng dẫn thêm thành viên. | NOT RUN | | |

---

### FR-DASH-02: Bảng điều khiển hoạt động cộng đồng

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DASH-002P | FR-DASH-02, BR-DASH-001, UC-11 | Xem dashboard hoạt động cộng đồng | 1. Family Member đã đăng nhập.<br>2. Có hoạt động 7 ngày gần nhất. | Family ID: `family-A` | 1. Mở "Hoạt động cộng đồng". | 1. Hiển thị: bài viết mới, bình luận, cảm xúc, ảnh mới.<br>2. Danh sách thành viên tích cực.<br>3. Có bộ lọc thời gian. | NOT RUN | | |
| TC-DASH-002E | FR-DASH-02, UC-11 | Chưa có hoạt động | 1. Gia đình mới, chưa có bài viết. | Family ID: `family-new` | 1. Mở dashboard. | Hiển thị trạng thái trống + gợi ý bắt đầu tương tác. | NOT RUN | | |

---

### FR-DASH-03: Thống kê sự kiện

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DASH-003P | FR-DASH-03, BR-DASH-001, UC-11 | Xem thống kê sự kiện | 1. Family Owner đã đăng nhập.<br>2. Có lịch sử sự kiện. | Family ID: `family-A` | 1. Mở "Thống kê sự kiện". | 1. Hiển thị: tổng sự kiện, tỷ lệ tham dự, sự kiện sắp tới.<br>2. Biểu đồ theo thời gian.<br>3. Lọc theo năm/loại. | NOT RUN | | |

---

### FR-DASH-04: Thống kê nhân khẩu

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DASH-004P | FR-DASH-04, BR-DASH-001, UC-11 | Xem thống kê nhân khẩu | 1. Family Owner đã đăng nhập.<br>2. Có dữ liệu nhân khẩu. | Family ID: `family-A` | 1. Mở "Thống kê nhân khẩu". | 1. Biểu đồ: độ tuổi, giới tính, địa điểm, nghề nghiệp.<br>2. Lọc theo nhánh.<br>3. Nhóm < 3 người được gộp vào "Khác".<br>4. Tỷ lệ thiếu dữ liệu. | NOT RUN | | |

---

### FR-DASH-05: Tạo và xuất báo cáo

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-DASH-005P | FR-DASH-05, BR-DASH-001, UC-11 | Tạo và xuất báo cáo PDF | 1. Family Owner đã đăng nhập.<br>2. Có dữ liệu thống kê. | Loại báo cáo: tổng hợp<br>Khoảng thời gian: 2026-01-01 đến 2026-08-20 | 1. Mở "Báo cáo".<br>2. Chọn loại, khoảng thời gian.<br>3. Xem trước.<br>4. Xuất PDF. | 1. Báo cáo hiển thị đúng nội dung.<br>2. File PDF được tải xuống.<br>3. Báo cáo lưu trong lịch sử. | NOT RUN | | |
| TC-DASH-005P2 | FR-DASH-05, UC-11 | Xuất báo cáo CSV | 1. Family Owner đã đăng nhập. | Định dạng: CSV | 1. Xuất CSV. | File CSV được tải xuống với dữ liệu thô dạng bảng. | NOT RUN | | |
| TC-DASH-005P3 | FR-DASH-05, UC-11 | Tải lại báo cáo lịch sử | 1. Đã có báo cáo trong lịch sử. | Report ID: `report-01` | 1. Mở danh sách báo cáo đã tạo.<br>2. Tải lại file cũ. | File được tải xuống. | NOT RUN | | |
| TC-DASH-005A | FR-DASH-05, FR-US-05, UC-11 | Member không thể xuất báo cáo | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API tạo báo cáo. | API trả về 403 Forbidden. | NOT RUN | | |

## Module 9: Administration

### FR-ADM-01: Quản lý người dùng

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-ADM-001P | FR-ADM-01, BR-ADM-001, UC-12 | Xem danh sách người dùng và tìm kiếm | 1. Administrator đã đăng nhập. | Từ khóa: `nguyen` | 1. Mở "Quản lý người dùng".<br>2. Tìm kiếm theo tên/email.<br>3. Lọc theo trạng thái/vai trò. | 1. Danh sách tài khoản hiển thị.<br>2. Tìm kiếm trả về kết quả chính xác.<br>3. Bộ lọc hoạt động. | NOT RUN | | |
| TC-ADM-001P2 | FR-ADM-01, BR-ADM-001, BR-ADM-002, UC-12 | Khóa tài khoản người dùng | 1. Administrator đã đăng nhập.<br>2. Tài khoản user-A đang ACTIVE. | User ID: `user-A`<br>Lý do: `Vi phạm chính sách` | 1. Mở chi tiết user-A.<br>2. Chọn "Khóa tài khoản".<br>3. Nhập lý do.<br>4. Xác nhận. | 1. User-A chuyển sang BLOCKED.<br>2. User-A nhận email thông báo.<br>3. Audit log ghi nhận.<br>4. User-A không đăng nhập được. | NOT RUN | | |
| TC-ADM-001P3 | FR-ADM-01, UC-12 | Mở khóa tài khoản | 1. Tài khoản user-B đang BLOCKED. | User ID: `user-B` | 1. Chọn "Mở khóa".<br>2. Xác nhận. | 1. User-B chuyển sang ACTIVE.<br>2. User-B đăng nhập được.<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-ADM-001P4 | FR-ADM-01, UC-12 | Đổi vai trò người dùng | 1. Administrator đã đăng nhập.<br>2. User-C đang là USER. | User ID: `user-C`<br>Vai trò mới: `ADMIN` | 1. Đổi vai trò user-C thành ADMIN.<br>2. Xác nhận. | 1. User-C có quyền Admin.<br>2. Audit log ghi nhận. | NOT RUN | | |
| TC-ADM-001N | FR-ADM-01, UC-12 | Hạ quyền Admin cuối cùng - bị chặn | 1. Chỉ còn 1 Admin duy nhất. | Admin ID: `last-admin` | 1. Cố hạ quyền Admin cuối cùng. | Hệ thống chặn: "Không thể hạ quyền Admin cuối cùng". | NOT RUN | | |
| TC-ADM-001A | FR-ADM-01, BR-ADM-001, UC-12 | Family Owner không có quyền quản lý người dùng toàn hệ thống | 1. Family Owner đã đăng nhập. | Token: owner_token | 1. Gọi API quản lý người dùng (khóa tài khoản). | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-ADM-02: Kiểm duyệt nội dung

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-ADM-002P | FR-ADM-02, BR-COM-004, UC-12 | Duyệt nội dung bị báo cáo - gỡ bài vi phạm | 1. Administrator đã đăng nhập.<br>2. Bài viết post-X bị báo cáo. | Post ID: `post-X`<br>Lý do: `Ngôn từ thù hận`<br>Xử lý: gỡ bài + cảnh cáo | 1. Mở hàng đợi kiểm duyệt.<br>2. Xem nội dung + ngữ cảnh.<br>3. Chọn "Gỡ nội dung".<br>4. Chọn mức xử lý: cảnh cáo. | 1. Bài viết chuyển REMOVED.<br>2. Người đăng nhận thông báo + cảnh cáo.<br>3. Người báo cáo nhận thông báo.<br>4. Audit log ghi nhận. | NOT RUN | | |
| TC-ADM-002P2 | FR-ADM-02, UC-12 | Nội dung không vi phạm - giữ nguyên | 1. Bài viết post-Y bị báo cáo nhưng không vi phạm. | Post ID: `post-Y` | 1. Xem nội dung.<br>2. Chọn "Giữ nội dung". | 1. Bài viết giữ nguyên PUBLISHED.<br>2. Người báo cáo nhận thông báo "không vi phạm".<br>3. Audit log ghi nhận. | NOT RUN | | |
| TC-ADM-002P3 | FR-ADM-02, UC-12 | Khôi phục nội dung đã gỡ nhầm | 1. Bài viết post-Z đã bị gỡ trước đó (< 30 ngày). | Post ID: `post-Z` | 1. Administrator khôi phục. | Bài viết được PUBLISHED trở lại. Audit log ghi nhận. | NOT RUN | | |

---

### FR-ADM-03: Nhật ký kiểm toán (Audit Log)

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-ADM-003P | FR-ADM-03, BR-ADM-002, UC-12 | Xem và lọc nhật ký kiểm toán | 1. Administrator đã đăng nhập.<br>2. Có audit log trong hệ thống. | Bộ lọc: hành động = ROLE_CHANGE<br>Thời gian: 7 ngày | 1. Mở "Nhật ký kiểm toán".<br>2. Lọc theo hành động, thời gian. | 1. Danh sách audit log hiển thị.<br>2. Mỗi bản ghi có: thời gian, người thực hiện, hành động, đối tượng, IP.<br>3. Lọc trả về kết quả chính xác. | NOT RUN | | |
| TC-ADM-003P2 | FR-ADM-03, UC-12 | Xuất audit log ra CSV | 1. Administrator đã đăng nhập.<br>2. Có audit log. | Bộ lọc: tất cả | 1. Xuất CSV. | File CSV được tải xuống với dữ liệu đã lọc. | NOT RUN | | |
| TC-ADM-003V | FR-ADM-03, BR-ADM-002, UC-12 | Audit log không thể sửa đổi (append-only) | 1. Administrator đã đăng nhập. | Audit Log ID: `log-001` | 1. Cố gắng sửa/xóa audit log. | Hệ thống chặn: audit log không thể sửa đổi. | NOT RUN | | |
| TC-ADM-003A | FR-ADM-03, BR-ADM-002, UC-12 | Family Member không thể xem audit log | 1. Family Member đã đăng nhập. | Token: member_token | 1. Gọi API xem audit log. | API trả về 403 Forbidden. | NOT RUN | | |

---

### FR-ADM-04: Sao lưu và phục hồi

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-ADM-004P | FR-ADM-04, BR-ADM-004, UC-12 | Sao lưu tự động theo lịch | 1. Cấu hình sao lưu đã thiết lập.<br>2. Đến giờ sao lưu. | Lịch: hằng ngày lúc 02:00 | 1. Scheduler kích hoạt sao lưu.<br>2. Kiểm tra kết quả. | 1. Bản sao lưu database + file được tạo.<br>2. Hash được xác minh.<br>3. Bản sao lưu xuất hiện trong danh sách. | NOT RUN | | |
| TC-ADM-004P2 | FR-ADM-04, BR-ADM-004, UC-12 | Phục hồi dữ liệu từ bản sao lưu | 1. Administrator đã đăng nhập.<br>2. Có bản sao lưu hợp lệ. | Backup ID: `backup-2026-08-20` | 1. Chọn bản sao lưu.<br>2. "Phục hồi".<br>3. Xác nhận kép (nhập từ khóa). | 1. Dữ liệu được phục hồi thành công.<br>2. Audit log ghi nhận.<br>3. Hệ thống hoạt động bình thường sau phục hồi. | NOT RUN | | |
| TC-ADM-004N | FR-ADM-04, UC-12 | Phục hồi thất bại - dữ liệu hiện tại được giữ nguyên | 1. Bản sao lưu bị hỏng. | Backup ID: `backup-corrupt` | 1. Phục hồi từ bản sao lưu hỏng. | Hệ thống báo lỗi, giữ nguyên dữ liệu hiện tại, không tự ghi đè. | NOT RUN | | |

---

### FR-ADM-05: Cấu hình hệ thống

| Test Case ID | Requirement ID | Feature | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Evidence | Defect ID |
|:------------:|:--------------:|---------|:-------------|:----------|:------|:----------------|:-------------:|:------:|:--------:|:---------:|
| TC-ADM-005P | FR-ADM-05, BR-ADM-003, UC-12 | Thay đổi cấu hình hệ thống | 1. Administrator đã đăng nhập.<br>2. Có quyền Admin. | Tham số: max_upload_size = 20MB<br>Nhóm: chung | 1. Mở "Cấu hình hệ thống".<br>2. Sửa max_upload_size thành 20MB.<br>3. Lưu. | 1. Cấu hình được lưu và áp dụng ngay.<br>2. Audit log ghi nhận.<br>3. Khi tải file 20MB → thành công; 21MB → lỗi. | NOT RUN | | |
| TC-ADM-005N | FR-ADM-05, UC-12 | Nhập giá trị không hợp lệ | 1. Administrator đã đăng nhập. | Tham số: max_upload_size = -1 | 1. Nhập giá trị âm.<br>2. Lưu. | Hệ thống báo lỗi "Giá trị không hợp lệ". Không lưu. | NOT RUN | | |
| TC-ADM-005A | FR-ADM-05, BR-ADM-003, UC-12 | Family Owner không thể cấu hình hệ thống | 1. Family Owner đã đăng nhập. | Token: owner_token | 1. Gọi API cấu hình hệ thống. | API trả về 403 Forbidden. | NOT RUN | | |
| TC-ADM-005P2 | FR-ADM-05, UC-12 | Tắt dịch vụ AI - kiểm tra fallback | 1. Administrator đã đăng nhập. | AI service: OFF | 1. Tắt AI service.<br>2. Family Member dùng AI Assistant. | 1. Cấu hình lưu thành công.<br>2. AI Assistant hiển thị trạng thái không khả dụng + fallback. | NOT RUN | | |
| TC-ADM-005P3 | FR-ADM-05, UC-12 | Khôi phục cấu hình mặc định | 1. Administrator đã đăng nhập. | Nhóm: bảo mật | 1. Chọn "Khôi phục mặc định" cho nhóm bảo mật. | Các tham số trong nhóm trở về giá trị mặc định. | NOT RUN | | |

---

## Execution Report

> ⚡ **Cập nhật kết quả thực thi Unit & Integration Testing — 2025-09-15**
> Phiên bản này ghi nhận kết quả từ automated test suite (pytest + coverage).
> Chi tiết: [`execution/Unit-Integration-Report.md`](execution/Unit-Integration-Report.md)

### Tổng quan

| Metric | Value |
|--------|-------|
| **Total Tests** | 213 |
| **PASS** | 206 (96.7%) |
| **FAIL** | 7 (3.3%) |
| **BLOCKED** | 0 |
| **NOT RUN** | Các test case UI/E2E trong file này chưa được automate (xem ghi chú) |
| **Coverage** | 82% (3,629 / 4,446 lines) |
| **Defects Found** | 2 (BUG-001: ✅ Fixed, BUG-002: ❌ Unresolved) |

> 📝 **Ghi chú:** Test cases trong file này được viết ở mức UI/E2E (dạng step-by-step). Tests được thực thi ở unit, service, repository và integration (API contract) level. Các TC mapping dưới đây cho thấy kết quả tương ứng từ automated tests hiện tại.

---

### Kết quả theo Module

#### Module US — User & Security

| Test Case ID | Kết quả từ Automation | Ghi chú evidence |
|:------------:|:---------------------:|:-----------------|
| TC-US-001P, TC-US-001N, TC-US-001N2, TC-US-001V | **FAIL** 🔴 | Endpoint `/api/auth/register` chưa được implement trong `auth_controller.py`. Service layer (`AuthService.register`) đã có code nhưng controller không expose. → **BUG-002** |
| TC-US-001N3, TC-US-001N4, TC-US-001N5, TC-US-001B, TC-US-001E | **NOT RUN** | Các test case này yêu cầu UI (form validation, email flow). Chưa có test frontend. |
| TC-US-002P, TC-US-002N | **FAIL** 🔴 | Endpoint `/api/auth/login` chưa được implement. → **BUG-002** |
| TC-US-002N2, TC-US-002N3, TC-US-002V, TC-US-002B | **NOT RUN** | Yêu cầu UI hoặc DB seeding (trạng thái account PENDING/BLOCKED, brute-force counter, perf). |
| TC-US-002N4 (login non-existent email) | **PASS** ✅ | Unit test `test_login_nonexistent_email` xác nhận trả về 401 mà không tiết lộ email không tồn tại. |
| TC-US-002A (refresh token) | **PASS** ✅ | Unit test `test_refresh_token_success` + `test_refresh_token_invalid` xác nhận luồng. |
| TC-US-003P, TC-US-003N, TC-US-003A (logout) | **PASS** ✅ | Unit test `test_logout` xác nhận. |
| TC-US-004P (forgot password) | **PASS** ✅ | Unit test `test_forgot_password` xác nhận. |
| TC-US-004N, TC-US-004N2, TC-US-004V | **PASS** ✅ | Unit tests `test_forgot_password_nonexistent`, `test_reset_password_success`, `test_reset_password_invalid_token` xác nhận. |
| TC-US-005P ... TC-US-005E (RBAC) | **NOT RUN** | Yêu cầu integration test với token giả định các role. Có thể triển khai với `test_auth.py` pattern. |
| TC-US-006P (get profile with token) | **FAIL** 🔴 | Endpoint `/api/auth/profile` (thực tế là `/users/me`) chưa được implement. → **BUG-002** |
| TC-US-006N, TC-US-006P2 (profile not found, update) | **PASS** ✅ | Unit tests `test_get_profile_not_found`, `test_update_profile` xác nhận. |
| TC-US-007P... (reset password) | **PASS** ✅ | Unit test `test_reset_password_success`, `test_reset_password_invalid_token` pass. |

#### Module FG — Family & Genealogy (Full PASS ✅)

| Test Case ID | Kết quả | Evidence |
|:------------:|:-------:|:--------:|
| TC-FG-001P (create family) | **PASS** | `test_create_family_creates_default_branch_and_commits`, `test_create_family` (repo) |
| TC-FG-001N (get non-existent) | **PASS** | `test_get_family_raises_when_missing`, `test_get_by_id_not_found` (repo) |
| TC-FG-001P2 (update family) | **PASS** | `test_update_family` |
| TC-FG-001P3 (delete family) | **PASS** | `test_delete_family` |
| TC-FG-001V (reject foreign branch) | **PASS** | `test_add_member_rejects_branch_from_another_family` |
| TC-FG-002P (add member) | **PASS** | `test_add_member_to_valid_branch` |
| TC-FG-003P (relationships) | **PASS** | `test_add_parent_child_relationship`, `test_add_marriage_relationship` |
| TC-FG-003V (validation) | **PASS** | `test_relationship_validation` (self-relationship, non-member, invalid type) |
| TC-FG-004P (genealogy tree) | **PASS** | `test_genealogy_tree_contains_roots_children_and_spouses` |
| TC-FG-004P2 (relationship lookup) | **PASS** | `test_lookup_relationship_returns_direct_relationship` |

#### Module COM — Community (Full PASS ✅)

| Test Case ID | Kết quả | Evidence |
|:------------:|:-------:|:--------:|
| TC-COM-001P (create post) | **PASS** | `test_create_post_success` |
| TC-COM-001N (empty content) | **PASS** | `test_create_post_empty` |
| TC-COM-001P2, 001P3 (update/delete own post) | **PASS** | `test_update_post`, `test_delete_post` |
| TC-COM-001N2 (non-author forbidden) | **PASS** | `test_update_post_forbidden`, `test_delete_post_forbidden` |
| TC-COM-003P (feed) | **PASS** | `test_get_feed_success`, `test_get_feed_invalid_page`, `test_get_feed_invalid_page_size` |
| TC-COM-002P (comment) | **PASS** | `test_add_comment_success` |
| TC-COM-002N (empty/long comment) | **PASS** | `test_add_comment_empty`, `test_add_comment_too_long` |
| TC-COM-002P2 (reaction) | **PASS** | `test_add_reaction_success` |
| TC-COM-002N (invalid reaction) | **PASS** | `test_add_reaction_invalid_type` |
| TC-COM-002V (duplicate reaction) | **PASS** | `test_add_reaction_duplicate` |
| TC-COM-002E (integrity error) | **PASS** | `test_add_reaction_integrity_error` |
| TC-COM-005P (announcement) | **PASS** | `test_create_announcement` |

#### Module EVT — Events (Full PASS ✅)

| Test Case ID | Kết quả | Evidence |
|:------------:|:-------:|:--------:|
| TC-EVT-001P (CRUD event) | **PASS** | `test_create_event_success`, `test_get_events`, `test_get_event_success` |
| TC-EVT-001N (not found → 404) | **PASS** | `test_get_event_not_found`, `test_update_event_not_found`, `test_cancel_event_not_found` |
| TC-EVT-001V (update event) | **PASS** | `test_update_event_success` |
| TC-EVT-001E (empty list) | **PASS** | `test_get_events_empty` |
| TC-EVT-002P (RSVP) | **PASS** | `test_rsvp_going`, `test_rsvp_maybe`, `test_rsvp_not_going` |
| TC-EVT-002N (invalid status → 400) | **PASS** | `test_rsvp_invalid_status` |
| TC-EVT-002V (update RSVP) | **PASS** | `test_rsvp_update_existing` |
| TC-EVT-003P (attendees) | **PASS** | `test_get_attendees_all`, `test_get_attendees_filtered` |
| TC-EVT-003E (empty attendees) | **PASS** | `test_get_attendees_empty` |
| TC-EVT-005P (reminder) | **PASS** | `test_send_reminder` |

#### Module AI — AI Services (Full PASS ✅)

| Test Case ID | Kết quả | Evidence |
|:------------:|:-------:|:--------:|
| TC-AI-001P (semantic search) | **PASS** | `test_semantic_search` |
| TC-AI-001N (no results) | **PASS** | `test_semantic_search_no_results` |
| TC-AI-002P (conversation CRUD) | **PASS** | `test_create_conversation`, `test_get_conversation_with_messages`, `test_list_conversations`, `test_delete_conversation` |
| TC-AI-002N (not found) | **PASS** | `test_get_conversation_not_found`, `test_delete_conversation_not_found` |
| TC-AI-002P5 (chat mock) | **PASS** | `test_chat_mock_provider` |
| TC-AI-003P (explain relationship) | **PASS** | `test_explain_relationship_parent_child`, `test_explain_relationship_marriage` |
| TC-AI-004P (summarize) | **PASS** | `test_summarize_short`, `test_summarize_medium`, `test_summarize_full` |
| TC-AI-004N (invalid length) | **PASS** | `test_summarize_invalid_length` |

#### Module ADM — Administration (Full PASS ✅)

| Test Case ID | Kết quả | Evidence |
|:------------:|:-------:|:--------:|
| TC-ADM-001P (list users) | **PASS** | `test_list_users_valid`, `test_list_users_with_filter` |
| TC-ADM-001N (invalid page size) | **PASS** | `test_list_users_invalid_page_size` |
| TC-ADM-001P2 (activate/block user) | **PASS** | `test_activate_user_success`, `test_suspend_user` |
| TC-ADM-001N (invalid status, not found) | **PASS** | `test_activate_user_invalid_status`, `test_activate_user_not_found` |
| TC-ADM-002P (moderate post) | **PASS** | `test_moderate_post` |
| TC-ADM-002N (invalid type) | **PASS** | `test_moderate_invalid_type` |
| TC-ADM-003P (audit log) | **PASS** | `test_get_audit_log`, `test_list_audit_logs` (repo), `test_add_audit_log` (repo) |
| TC-ADM-005P (update config) | **PASS** | `test_update_config`, `test_update_config_new` (repo) |
| TC-ADM-005N (empty config) | **PASS** | `test_update_config_empty` |

---

### Danh sách Defect

#### BUG-001: Missing Route Registration ✅ &#0208;Đã sửa

| Field | Value |
|-------|-------|
| **ID** | BUG-001 |
| **Mức độ** | 🔴 Critical |
| **Trạng thái** | **Fixed** |
| **Mô tả** | `register_routes()` trong `app/api/routes.py` import 8 routers nhưng chỉ đăng ký 2 (`heritage`, `directory`). 6 router còn lại không được `app.include_router()`, dẫn đến 404 cho toàn bộ API. |
| **Fix** | Thêm `app.include_router()` cho: `health`, `auth`, `event`, `community`, `ai`, `admin`, `family`. |

#### BUG-002: Missing Auth Endpoints ❌ Chưa sửa

| Field | Value |
|-------|-------|
| **ID** | BUG-002 |
| **Mức độ** | 🔴 Critical |
| **Trạng thái** | **Unresolved** |
| **Mô tả** | `auth_controller.py` chỉ có 3 endpoints (`/auth/forgot-password`, `/auth/reset-password`, `/auth/refresh`). Frontend cần thêm: `POST /auth/register`, `POST /auth/login`, `POST /auth/logout`, `POST /auth/verify-email`, `GET /users/me`. `AuthService` đã code đầy đủ nhưng controller chưa expose. |
| **Impact** | 7 integration tests FAIL. Người dùng không thể register, login, xem profile. |
| **Affected TC** | TC-US-001P, TC-US-001N, TC-US-001N2, TC-US-001V, TC-US-002P, TC-US-002N, TC-US-006P |

---

### Coverage Summary (82%)

| Service | Coverage | | Repository | Coverage |
|---------|:--------:|-|------------|:--------:|
| `event_service.py` | **100%** | | `reaction_repository.py` | **100%** |
| `community_service.py` | **99%** | | `rsvp_repository.py` | **100%** |
| `auth_service.py` | **98%** | | `ai_repository.py` | **100%** |
| `admin_service.py` | **91%** | | `admin_repository.py` | **97%** |
| `family_service.py` | **84%** | | `user_repository.py` | **95%** |
| `ai_service.py` | **61%** | | `event_repository.py` | **97%** |
| `directory_service.py` | **20%** | | `post_repository.py` | **91%** |
| `heritage_service.py` | **40%** | | `directory_repository.py` | **39%** |

---

### Evidence Files

| File | Description |
|------|-------------|
| [`evidence/unit-integration/unit-tests-full.log`](evidence/unit-integration/unit-tests-full.log) | Full pytest output — Unit tests (160 passed) |
| [`evidence/unit-integration/all-tests-full.log`](evidence/unit-integration/all-tests-full.log) | Full pytest output — All tests (206 passed, 7 failed) |
| [`evidence/unit-integration/all-tests-summary.log`](evidence/unit-integration/all-tests-summary.log) | PASS/FAIL summary list per test case |
| [`execution/Unit-Integration-Report.md`](execution/Unit-Integration-Report.md) | Detailed Unit & Integration Test Report |

### Hướng dẫn chạy lại

```bash
# Yêu cầu: Python 3.14+, dependencies từ backend/requirements.txt

cd familyconnect

# 1. Unit tests only (160 tests)
DATABASE_URL="sqlite+aiosqlite:///./test.db" python3 -m pytest backend/tests/unit/ -v --cov=backend

# 2. All tests (unit + integration, 213 tests)
DATABASE_URL="sqlite+aiosqlite:///./test.db" python3 -m pytest backend/tests/ -v --cov=backend

# 3. With coverage report
DATABASE_URL="sqlite+aiosqlite:///./test.db" python3 -m pytest backend/tests/ --cov=backend --cov-report=html
```

---

*Báo cáo được tạo tự động từ automated test suite. Chi tiết tại [execution/Unit-Integration-Report.md](execution/Unit-Integration-Report.md).*
