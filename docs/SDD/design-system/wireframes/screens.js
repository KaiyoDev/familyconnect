// FT8-33 wireframe specs — 48 screens, 3 breakpoints (1440/768/375)
// Block types rendered by render.js. Fields override defaults for key forms.
module.exports = [
  // ── PUBLIC & AUTH ────────────────────────────────────────────────
  { code: "PUB-01", title: "Landing page", layout: "public", blocks: ["nav-public", "hero", "stats-strip", "feature-cards", "testimonial", "cta", "footer"] },
  { code: "PUB-02", title: "Đăng nhập", layout: "auth", blocks: ["auth-card"], fields: { email: "Email", password: "Mật khẩu" }, actions: ["Đăng nhập", "Quên mật khẩu?", "Đăng ký tài khoản"] },
  { code: "PUB-03", title: "Đăng ký", layout: "auth", blocks: ["auth-card"], fields: { fullname: "Họ và tên", email: "Email", phone: "Số điện thoại", password: "Mật khẩu", confirm: "Xác nhận mật khẩu" }, actions: ["Đăng ký", "Đã có tài khoản? Đăng nhập"] },
  { code: "PUB-04", title: "Quên / đặt lại mật khẩu", layout: "auth", blocks: ["auth-card"], fields: { email: "Email" }, actions: ["Gửi mã xác thực"] },
  { code: "PUB-05", title: "Kích hoạt tài khoản", layout: "auth", blocks: ["auth-card"], fields: { otp: "Mã xác thực 6 chữ số" }, actions: ["Xác nhận", "Gửi lại mã (00:59)"] },
  // ── SHELL ────────────────────────────────────────────────────────
  { code: "SHL-01", title: "Layout chính (shell)", layout: "portal", blocks: ["sidebar-portal", "breadcrumb", "tabs", "sample-content"] },
  { code: "SHL-02", title: "Trang chủ tổng quan", layout: "portal", blocks: ["sidebar-portal", "welcome", "quick-stats", "recent-activities", "upcoming-events", "birthday-list"] },
  { code: "SHL-03", title: "Tìm kiếm toàn cục", layout: "portal", blocks: ["sidebar-portal", "search-bar", "filter-chips", "search-results"] },
  // ── GENEALOGY ────────────────────────────────────────────────────
  { code: "GEN-01", title: "Cây gia phả (thế hệ)", layout: "portal", blocks: ["sidebar-portal", "toolbar", "tree"] },
  { code: "GEN-02", title: "Đồ thị quan hệ", layout: "portal", blocks: ["sidebar-portal", "toolbar", "graph"] },
  { code: "GEN-03", title: "Tra cứu quan hệ", layout: "portal", blocks: ["sidebar-portal", "relation-form", "relation-result"] },
  { code: "GEN-04", title: "Hồ sơ thành viên", layout: "portal", blocks: ["sidebar-portal", "profile-header", "profile-tabs", "profile-detail"] },
  { code: "GEN-05/06", title: "Thêm thành viên & thiết lập quan hệ", layout: "portal", blocks: ["sidebar-portal", "form", "relation-preview"] },
  // ── FAMILY ───────────────────────────────────────────────────────
  { code: "FAM-01", title: "Tạo gia đình", layout: "portal", blocks: ["sidebar-portal", "form"], fields: { familyName: "Họ gia đình", displayName: "Tên hiển thị", region: "Khu vực / quê quán", desc: "Mô tả gia đình" }, actions: ["Tạo gia đình"] },
  { code: "FAM-02", title: "Thông tin gia đình", layout: "portal", blocks: ["sidebar-portal", "family-header", "family-stats", "family-detail"] },
  { code: "FAM-03", title: "Quản lý nhánh", layout: "portal", blocks: ["sidebar-portal", "branch-tree", "branch-actions"] },
  { code: "FAM-04", title: "Danh sách thành viên", layout: "portal", blocks: ["sidebar-portal", "toolbar", "member-table"] },
  { code: "FAM-05", title: "Xác thực yêu cầu tham gia", layout: "portal", blocks: ["sidebar-portal", "request-list"] },
  // ── COMMUNITY ────────────────────────────────────────────────────
  { code: "COM-01", title: "Luồng cộng đồng", layout: "portal", blocks: ["sidebar-portal", "composer", "feed"] },
  { code: "COM-02", title: "Chi tiết bài viết", layout: "portal", blocks: ["sidebar-portal", "post-detail", "comments"] },
  { code: "COM-03", title: "Tạo bài viết", layout: "portal", blocks: ["sidebar-portal", "post-form"] },
  { code: "COM-04", title: "Tin gia đình", layout: "portal", blocks: ["sidebar-portal", "news-list"] },
  { code: "COM-05", title: "Tạo thông báo", layout: "portal", blocks: ["sidebar-portal", "announce-form", "preview-pane"] },
  // ── EVENT ────────────────────────────────────────────────────────
  { code: "EVT-01", title: "Danh sách sự kiện + lịch", layout: "portal", blocks: ["sidebar-portal", "calendar", "event-list"] },
  { code: "EVT-02", title: "Chi tiết sự kiện + RSVP", layout: "portal", blocks: ["sidebar-portal", "event-header", "rsvp-actions", "event-info", "attendee-list"] },
  { code: "EVT-03", title: "Tạo / sửa sự kiện", layout: "portal", blocks: ["sidebar-portal", "form", "invite-pane"], fields: { title: "Tên sự kiện", time: "Thời gian", place: "Địa điểm", desc: "Mô tả" }, actions: ["Lưu & gửi thư mời"] },
  { code: "EVT-04", title: "Quản lý người tham gia", layout: "portal", blocks: ["sidebar-portal", "attendee-table", "status-chart"] },
  { code: "EVT-05", title: "Thư viện ảnh sự kiện", layout: "portal", blocks: ["sidebar-portal", "album-toolbar", "photo-grid"] },
  // ── DIRECTORY ────────────────────────────────────────────────────
  { code: "DIR-01", title: "Danh bạ thành viên", layout: "portal", blocks: ["sidebar-portal", "directory-grid"] },
  { code: "DIR-02", title: "Hồ sơ nghề nghiệp / học vấn", layout: "portal", blocks: ["sidebar-portal", "profile-header", "career-timeline"] },
  { code: "DIR-03", title: "Tìm kiếm nâng cao", layout: "portal", blocks: ["sidebar-portal", "adv-search", "directory-grid"] },
  // ── HERITAGE ─────────────────────────────────────────────────────
  { code: "HER-01", title: "Kho lưu trữ số", layout: "portal", blocks: ["sidebar-portal", "archive-cards"] },
  { code: "HER-02", title: "Tư liệu lịch sử", layout: "portal", blocks: ["sidebar-portal", "doc-list"] },
  { code: "HER-03", title: "Câu chuyện gia đình", layout: "portal", blocks: ["sidebar-portal", "story-cards"] },
  { code: "HER-04", title: "Thành viên tiêu biểu", layout: "portal", blocks: ["sidebar-portal", "honor-list"] },
  { code: "HER-05", title: "Thư viện ảnh gia đình", layout: "portal", blocks: ["sidebar-portal", "photo-grid", "timeline"] },
  // ── AI ───────────────────────────────────────────────────────────
  { code: "AI-01", title: "Trợ lý tri thức gia đình", layout: "portal", blocks: ["sidebar-portal", "chat"] },
  { code: "AI-02", title: "Kết quả tìm kiếm ngữ nghĩa", layout: "portal", blocks: ["sidebar-portal", "search-bar", "semantic-results", "source-cards"] },
  // ── DASHBOARD ────────────────────────────────────────────────────
  { code: "DSH-01", title: "Thống kê gia đình", layout: "portal", blocks: ["sidebar-portal", "stats-cards", "chart-line", "chart-bar"] },
  { code: "DSH-02", title: "Nhân khẩu + sự kiện", layout: "portal", blocks: ["sidebar-portal", "chart-donut", "chart-bar", "event-stats"] },
  { code: "DSH-03", title: "Tạo / xuất báo cáo", layout: "portal", blocks: ["sidebar-portal", "report-form", "report-preview", "export-actions"] },
  // ── ADMIN ────────────────────────────────────────────────────────
  { code: "ADM-01", title: "Admin dashboard", layout: "admin", blocks: ["sidebar-admin", "stats-cards", "chart-line", "admin-table"] },
  { code: "ADM-02", title: "Quản lý người dùng", layout: "admin", blocks: ["sidebar-admin", "toolbar", "user-table"] },
  { code: "ADM-03", title: "Kiểm duyệt nội dung", layout: "admin", blocks: ["sidebar-admin", "moderation-list"] },
  { code: "ADM-04", title: "Nhật ký kiểm toán", layout: "admin", blocks: ["sidebar-admin", "filter-bar", "audit-list"] },
  { code: "ADM-05", title: "Sao lưu & phục hồi", layout: "admin", blocks: ["sidebar-admin", "backup-list", "backup-schedule"] },
  { code: "ADM-06", title: "Cấu hình hệ thống", layout: "admin", blocks: ["sidebar-admin", "settings-form"] },
  // ── PROFILE ──────────────────────────────────────────────────────
  { code: "PRF-01/02/03", title: "Hồ sơ cá nhân · Thông báo · Lịch sử", layout: "portal", blocks: ["sidebar-portal", "profile-tabs", "profile-detail"] },
];
