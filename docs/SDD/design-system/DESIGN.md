# FamilyConnect — Web Portal Design Specification (Google Stitch)

> Input spec cho Google Stitch: paste file này vào Stitch để generate design system `.gdd`, 48 hi-fi UI và prototype.
> Nguồn: `docs/SDD/03_UIUXDesign.md` (FT8-33), SRS (FT8-2..FT8-13), SAD (FT8-30).

## 1. Product Overview

FamilyConnect là nền tảng cộng đồng gia đình số, kết nối các thế hệ qua cây gia phả, sự kiện, di sản và trợ lý AI. Web Portal phục vụ 4 vai trò: Guest, Family Member, Family Owner, Administrator. Responsive 3 breakpoints: Desktop 1440 / Tablet 768 / Mobile 375.

## 2. Design Principles

1. **Gia đình trước tiên:** mọi màn hình lấy gia đình và quan hệ thân tộc làm trung tâm; dùng ngôn ngữ xưng hô Việt Nam (ông, bà, bác, cô, chú, anh, chị...).
2. **Đơn giản cho mọi lứa tuổi:** chữ to (16px base), tương phản cao (AA), thao tác tối giản; đối tượng có người lớn tuổi.
3. **Nhất quán:** toàn bộ màn hình dùng chung design system (color tokens, typography, components).
4. **RBAC-driven:** menu và thao tác hiển thị theo vai trò; Admin có khu vực riêng.
5. **Responsive-first:** từ Mobile 375 lên Desktop 1440; form nặng tối ưu Desktop, core thao tác (xem cây, feed, RSVP) đầy đủ trên Mobile.
6. **AI là trợ lý:** phản hồi AI kèm trích dẫn nguồn + trạng thái fallback khi AI không khả dụng.

## 3. Design System

### 3.1 Color Tokens

| Token | Giá trị | Dùng cho |
|---|---|---|
| `primary` | `#0D9488` (Teal 600) | Nút chính, liên kết, trạng thái active |
| `primary-dark` | `#0F766E` (Teal 700) | Hover, sidebar, header |
| `primary-light` | `#CCFBF1` (Teal 100) | Nền active, badge nhạt |
| `accent` | `#F59E0B` (Amber 500) | Sự kiện, nhấn mạnh, RSVP |
| `success` | `#16A34A` | Trạng thái thành công, đã duyệt |
| `warning` | `#D97706` | Cảnh báo, chờ duyệt |
| `danger` | `#DC2626` | Lỗi, từ chối, xóa |
| `info` | `#0284C7` | Thông tin, AI |
| `neutral-0` | `#FFFFFF` | Nền, thẻ |
| `neutral-50` | `#F8FAFC` | Nền trang |
| `neutral-100` | `#F1F5F9` | Nền khối, hover |
| `neutral-200` | `#E2E8F0` | Border nhạt |
| `neutral-300` | `#CBD5E1` | Border, divider |
| `neutral-500` | `#64748B` | Text phụ |
| `neutral-700` | `#334155` | Text chính |
| `neutral-900` | `#0F172A` | Header, tiêu đề |
| `text-on-primary` | `#FFFFFF` | Text trên nút primary |
| `danger-bg` | `#FEF2F2` | Nền alert danger |

### 3.2 Typography

- Font: **Be Vietnam Pro** (hỗ trợ tiếng Việt đầy đủ), fallback `Inter, Segoe UI, sans-serif`.
- Thang kích thước: 12 / 14 / 16 (base) / 18 / 20 / 24 / 32 / 40.
- Line-height: heading 1.2, body 1.5.
- Weight: 400 regular, 500 medium, 600 semibold, 700 bold.

### 3.3 Spacing & Radius

- Grid 4px: 4 / 8 / 12 / 16 / 24 / 32 / 48.
- Radius: `sm` 4px (input), `md` 8px (card, button), `lg` 12px (modal, drawer), `full` 999px (avatar, chip).
- Shadow: `card` `0 1px 3px rgba(15,23,42,.08)`, `modal` `0 8px 24px rgba(15,23,42,.15)`.

### 3.4 Components

| Component | Mô tả |
|---|---|
| Button | 4 variants: primary, secondary (outline), ghost, danger; 3 sizes: sm 32 / md 40 / lg 48; disabled state; min touch target 44px |
| Input / Select / Textarea | Border `neutral-300`, focus ring primary 2px, error state danger, label 14px semibold |
| Checkbox / Radio | Vòng chọn, focus visible |
| Tabs | Underline primary, 40px height |
| Table | Header `neutral-100` 600, row hover `neutral-50`, zebra, sticky header |
| Card | Radius `md`, shadow `card`, padding 16-24 |
| Modal / Drawer | Radius `lg`, overlay `rgba(15,23,42,.4)`, đóng bằng Esc |
| Toast | 4 loại success/warning/danger/info, auto-dismiss 4s |
| Badge / Tag | Radius full, 20px height, semantic màu |
| Avatar | Circle, size 24/32/40/48/64, fallback initials |
| Tree Node (gia phả) | Node thế hệ: card 96px, nối bằng đường; màu theo giới tính (nam primary, nữ pink `#DB2777`), ông tổ highlight accent |
| Chart | Line/bar/donut, legend, tooltip |
| Empty state | Icon + title + description + CTA |
| Skeleton | Loading, shimmer |

### 3.5 Iconography

- Bộ icon 24px stroke 1.5 (Material Symbols), thống nhất toàn portal; icon menu phụ trợ không thay thế nhãn text.

### 3.6 Breakpoints

| Breakpoint | Width | Hành vi |
|---|---|---|
| Desktop | ≥ 1024 (base 1440) | Sidebar cố định 220px, multi-column |
| Tablet | 768 | Sidebar thu icon 64px hoặc drawer |
| Mobile | 375 | Drawer menu + bottom nav 5 tab: Trang chủ, Gia phả, Sự kiện, Di sản, Cá nhân |

### 3.7 Accessibility

- Contrast ≥ WCAG AA (4.5:1 text, 3:1 UI).
- Touch target ≥ 44px.
- Focus visible ring primary.
- ARIA labels cho icon buttons, form fields.

## 4. Screens (48 hi-fi UI)

> Wireframe tham chiếu: `wireframes/out/{desktop,tablet,mobile}/{CODE}.png`. Mỗi screen render 3 breakpoint.

### Public & Auth (PUB-01..05)

- **PUB-01 Landing page:** header logo + nav + CTA; hero (slogan "Kết nối các thế hệ gia đình" + CTA "Tạo gia đình miễn phí" + ảnh gia đình); strip 4 số liệu; 6 feature cards (Cây gia phả, Sự kiện, Di sản, Danh bạ, Trợ lý AI, An toàn dữ liệu); testimonial; CTA cuối; footer.
- **PUB-02 Đăng nhập:** form trung tâm (email, password, show/hide, "Quên mật khẩu?", nút Đăng nhập, chia link Đăng ký, social? — không dùng social, chỉ email/OTP). Tích hợp OTP khi cần 2FA.
- **PUB-03 Đăng ký:** họ tên, email, SĐT, mật khẩu + xác nhận; đồng ý điều khoản; gửi mã kích hoạt.
- **PUB-04 Quên mật khẩu:** nhập email → gửi OTP → nhập OTP → đặt mật khẩu mới.
- **PUB-05 Kích hoạt tài khoản:** nhập OTP 6 số, đếm ngược gửi lại.

### App Shell (SHL-01..03)

- **SHL-01 Layout chính:** sidebar (logo, 9 menu, bottom user), breadcrumb, tabs, nội dung; mobile: drawer + bottom nav.
- **SHL-02 Trang chủ tổng quan:** welcome card + hành động nhanh (Thêm thành viên, Tạo sự kiện, Đăng bài), 3 thẻ số (Thành viên, Sự kiện sắp tới, Tư liệu mới), hoạt động gần đây, sự kiện sắp tới, sinh nhật tháng.
- **SHL-03 Tìm kiếm toàn cục:** thanh tìm kiếm lớn, chip lọc (Tất cả/Thành viên/Bài viết/Sự kiện/Tư liệu), kết quả grouped.

### Gia phả (GEN-01..06)

- **GEN-01 Cây gia phả thế hệ:** tree interactive (pan/zoom, mở rộng nhánh), node thẻ họ tên + năm sinh, màu theo giới, ông tổ highlight; toolbar (tìm, thêm, xem dạng).
- **GEN-02 Đồ thị quan hệ:** graph quan hệ với filter (trực tiếp/gián tiếp, mức độ), click node → hồ sơ.
- **GEN-03 Tra cứu quan hệ:** chọn A, chọn B → kết quả quan hệ + giải thích AI + đường ngắn nhất trên đồ thị.
- **GEN-04 Hồ sơ thành viên:** header (avatar, tên, ngày sinh, quan hệ gốc, nút Sửa), tabs (Tổng quan, Nghề nghiệp, Tư liệu, Câu chuyện), 2 cột detail.
- **GEN-05/06 Form thêm thành viên & quan hệ:** form (họ tên, giới tính, ngày sinh, ảnh, ghi chú) + panel chọn quan hệ (cha/mẹ/vợ/chồng/con, chọn thành viên hiện có hoặc tạo mới) + preview quan hệ + kiểm tra ràng buộc (vòng lặp, >2 cha mẹ).

### Gia đình (FAM-01..05)

- **FAM-01 Tạo gia đình:** form (họ gia đình, tên hiển thị, khu vực/quê quán, mô tả, ảnh bìa) → tạo + trở thành Owner.
- **FAM-02 Thông tin gia đình:** bìa + tên + khu vực, 4 thẻ số, detail 2 cột, nút chỉnh sửa (Owner).
- **FAM-03 Quản lý nhánh:** cây nhánh, hành động (tạo nhánh mới, đổi tên, sáp nhập, xóa — Owner).
- **FAM-04 Danh sách thành viên:** bảng (avatar, tên, ngày sinh, quan hệ, vai trò, trạng thái), lọc theo nhánh/trạng thái, thêm thành viên.
- **FAM-05 Xác thực yêu cầu tham gia:** danh sách pending (hồ sơ, quan hệ khai báo, lời nhắn), Duyệt/Từ chối kèm lý do.

### Cộng đồng (COM-01..05)

- **COM-01 Luồng cộng đồng:** composer (đăng bài), feed (avatar, nội dung, ảnh, like/comment/share), filter (Tất cả/Gia đình tôi/Đã đăng).
- **COM-02 Chi tiết bài viết:** nội dung + ảnh, like/comment/share, bình luận + ô nhập.
- **COM-03 Tạo bài viết:** tiêu đề, nội dung (rich text), đính kèm ảnh/tệp, phạm vi hiển thị, đăng.
- **COM-04 Tin gia đình:** danh sách tin/thông báo chính thức (badge "Tin gia đình"), phân loại.
- **COM-05 Tạo thông báo:** form (tiêu đề, nội dung, đối tượng: toàn gia đình/nhánh) + preview + gửi.

### Sự kiện (EVT-01..05)

- **EVT-01 Danh sách sự kiện + lịch:** lịch tháng (đánh dấu sự kiện accent) + danh sách sắp tới, lọc trạng thái.
- **EVT-02 Chi tiết sự kiện + RSVP:** bìa, tên, thời gian, địa điểm, mô tả; RSVP (Sẽ tham dự/Có thể/Không), danh sách tham gia.
- **EVT-03 Tạo/sửa sự kiện:** form (tên, thời gian, địa điểm, mô tả, ảnh) + chọn khách mời + mẫu thư mời → lưu & gửi.
- **EVT-04 Quản lý người tham gia:** bảng RSVP + biểu đồ Going/Maybe/Not Going, nhắc nhở chưa phản hồi, xuất CSV/PDF.
- **EVT-05 Thư viện ảnh sự kiện:** grid ảnh, upload, sort, slideshow.

### Danh bạ (DIR-01..03)

- **DIR-01 Danh bạ thành viên:** grid thẻ (avatar, tên, quan hệ, nghề), tìm nhanh, lọc nhánh.
- **DIR-02 Hồ sơ nghề nghiệp/học vấn:** header hồ sơ + timeline nghề nghiệp & học vấn.
- **DIR-03 Tìm kiếm nâng cao:** form (tên, giới tính, tuổi, nghề, khu vực, quan hệ, nhánh) + kết quả grid.

### Di sản (HER-01..05)

- **HER-01 Kho lưu trữ số:** thẻ phân loại (Tư liệu, Ảnh, Câu chuyện, Kỷ vật), lọc năm/thập niên.
- **HER-02 Tư liệu lịch sử:** danh sách (tên, loại, năm, người đóng góp, trạng thái duyệt) + xem tài liệu.
- **HER-03 Câu chuyện gia đình:** thẻ story (tác giả, thập niên, ảnh), viết story mới.
- **HER-04 Thành viên tiêu biểu:** danh sách xếp hạng đóng góp + khen thưởng.
- **HER-05 Thư viện ảnh gia đình:** grid ảnh + timeline, tag thành viên, upload.

### Trợ lý AI (AI-01..02)

- **AI-01 Trợ lý tri thức gia đình:** chat (hỏi đáp về lịch sử gia đình, quan hệ), trả lời kèm trích dẫn nguồn (link hồ sơ/tư liệu), đánh giá 👍/👎, trạng thái fallback khi AI tắt.
- **AI-02 Kết quả tìm kiếm ngữ nghĩa:** thanh tìm + kết quả ngữ nghĩa nổi bật + thẻ nguồn (hồ sơ, tư liệu liên quan).

### Báo cáo (DSH-01..03)

- **DSH-01 Thống kê gia đình:** 4 KPI + chart line (tăng trưởng thành viên) + chart bar (phân bố nhánh).
- **DSH-02 Nhân khẩu + sự kiện:** donut (giới tính/độ tuổi) + bar (sự kiện theo tháng) + thống kê tham dự.
- **DSH-03 Tạo/xuất báo cáo:** form (loại, phạm vi, kỳ) + preview + xuất PDF/CSV + lịch tự động.

### Admin (ADM-01..06)

- **ADM-01 Admin dashboard:** sidebar admin (6 menu), KPI toàn hệ thống, chart, bảng mới nhất.
- **ADM-02 Quản lý người dùng:** bảng (tên, email, vai trò, trạng thái, thao tác), lọc, cấm/kích hoạt, reset mật khẩu.
- **ADM-03 Kiểm duyệt nội dung:** hàng chờ (bài viết, ảnh, hồ sơ, tư liệu) — Duyệt/Từ chối kèm lý do, xem trước.
- **ADM-04 Nhật ký kiểm toán:** filter (thời gian, loại, người, IP) + danh sách log.
- **ADM-05 Sao lưu & phục hồi:** danh sách backup (thời điểm, kích thước, trạng thái), lịch tự động, sao lưu ngay, khôi phục.
- **ADM-06 Cấu hình hệ thống:** form cấu hình chung, thông báo, bảo mật (2FA, session), giới hạn.

### Cá nhân (PRF-01..03)

- **PRF-01/02/03 Hồ sơ cá nhân · Thông báo · Lịch sử:** tabs (Tổng quan: thông tin + ảnh đại diện + đổi mật khẩu; Thông báo: danh sách đọc/chưa đọc, cài đặt kênh; Lịch sử: hoạt động của tôi).

## 5. Prototype

- Prototype tương tác: từ DESIGN.md này, Stitch generate prototype nối 48 màn hình.
- Luồng demo chính: Landing → Đăng ký → Kích hoạt → Đăng nhập → Tạo gia đình → Cây gia phả → Đăng bài → Tạo sự kiện → RSVP → Trợ lý AI.
