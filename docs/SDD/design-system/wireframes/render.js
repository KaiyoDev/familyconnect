// FT8-33 wireframe renderer — puppeteer-core + local Brave, 3 breakpoints per screen
const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");
const screens = require("./screens.js");

const BRAVE = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe";
const OUT = path.join(__dirname, "out");
const CHROME = "#3B82F6", GREEN = "#10B981", AMBER = "#F59E0B", RED = "#EF4444", SLATE = "#64748B";
const LIGHT = "#F1F5F9", BORDER = "#CBD5E1", INK = "#0F172A", GRAY = "#94A3B8";
const PAD = 6; // px between blocks (scale-invariant)

function box(t, x, y, w, h, label, opts = {}) {
  const b = { t, x, y, w, h };
  if (label) b.label = label;
  if (opts.color) b.color = opts.color;
  if (opts.strip) b.strip = opts.strip; // colored strip on left
  if (opts.labelRight) b.labelRight = opts.labelRight;
  if (opts.center) b.center = true;
  if (opts.topLeft) b.topLeft = true;
  return b;
}

function layout(s) {
  const blocks = [];
  const W = { s: 1440, t: 768, m: 375 }[s.size];

  // Sidebars (portal has no header — logo row inside sidebar; admin has top header)
  const PORTAL_SIDEBAR = { logo: true, nav: ["Tổng quan", "Gia phả", "Gia đình", "Cộng đồng", "Sự kiện", "Danh bạ", "Di sản", "Trợ lý AI", "Báo cáo"] };
  const ADMIN_SIDEBAR = { logo: true, nav: ["Dashboard", "Người dùng", "Kiểm duyệt", "Nhật ký", "Sao lưu", "Cấu hình"] };
  const useSidebar = s.layout === "portal" ? PORTAL_SIDEBAR : s.layout === "admin" ? ADMIN_SIDEBAR : null;
  const sbW = s.size === "m" ? 0 : 220;
  const topBar = s.layout === "admin" || s.size === "m";

  let x = 0, y = 0, availW, availH;
  if (topBar) {
    blocks.push(box(s, 0, 0, W, 48, "Logo · Tìm kiếm · Avatar · …", { labelRight: true }));
    blocks.push(box(s, 0, 48, sbW, 0, "", { color: "rgba(2,6,23,.06)" }));
    x = sbW; y = 48; availW = W - sbW; availH = s.h - 48 - PAD;
  } else if (useSidebar) {
    blocks.push(box(s, 0, 0, sbW, s.h, "", { color: "rgba(2,6,23,.06)" }));
    const nav = useSidebar.nav;
    nav.forEach((n, i) => blocks.push(box(s, 10, 16 + i * 30, sbW - 20, 22, n, { strip: i === 0 ? CHROME : null })));
    x = sbW; availW = W - sbW; availH = s.h - PAD;
  } else if (s.layout === "auth") {
    blocks.push(box(s, 0, 0, W, s.h, "", { color: "rgba(59,130,246,.07)" }));
  } else {
    blocks.push(box(s, 0, 0, W, 48, "Logo · Tìm kiếm · Đăng nhập / Đăng ký", { labelRight: true }));
    y = 48; availW = W; availH = s.h - 48 - PAD;
  }

  // Content area — single column, stacked, clamped at bottom
  const cx = x, cw = availW, ch = availH - PAD;

  for (const b of s.blocks) {
    if (b === "sidebar-portal" || b === "sidebar-admin") continue;
    const def = DEFS[b];
    if (!def) continue;
    if (y + def.h > ch) y = Math.max(0, ch - def.h);
    blocks.push(box(s, cx, y, cw, def.h, def.label, def.opts));
    y += def.h + PAD;
  }
  return blocks;
}

// Block definitions — default: full-width (w=1), h in px, optional w2 (right-column variant)
const DEFS = {
  "nav-public":        { w: 1, h: 48, label: "Điều hướng: Giới thiệu · Tính năng · Gia phả · Liên hệ", opts: { labelRight: true } },
  "hero":              { w: 1, h: 220, label: "Hero: Kết nối các thế hệ gia đình — tiêu đề + CTA + ảnh minh họa", opts: { center: true } },
  "stats-strip":       { w: 1, h: 72, label: "4 số liệu: 500+ gia đình · 12.000 thành viên · 48 tỉnh · 3 thế hệ", opts: { center: true } },
  "feature-cards":     { w: 1, h: 150, label: "6 ô tính năng: Cây gia phả · Sự kiện · Di sản · Trợ lý AI · …", opts: { center: true } },
  "testimonial":       { w: 1, h: 100, label: "Trải nghiệm người dùng (testimonial)", opts: { center: true } },
  "cta":               { w: 1, h: 90, label: "CTA: Tạo gia đình miễn phí — bắt đầu ngay", opts: { center: true } },
  "footer":            { w: 1, h: 90, label: "Footer: liên kết, liên hệ, bản quyền", opts: { color: "rgba(2,6,23,.06)", center: true } },

  "auth-card":         { w: 1, h: 420, label: "Thẻ đăng nhập — form xác thực trung tâm", opts: { center: true, strip: CHROME } },

  "sidebar-portal":    { w: 1, h: 0, label: "" },
  "sidebar-admin":     { w: 1, h: 0, label: "" },
  "breadcrumb":        { w: 1, h: 30, label: "Breadcrumb: Tổng quan / Gia phả / …" },
  "tabs":              { w: 1, h: 36, label: "Tabs: Thành viên · Quan hệ · Tư liệu · Sự kiện", opts: { strip: CHROME } },
  "sample-content":    { w: 1, h: 200, label: "Vùng nội dung chính (placeholder)", opts: { color: "rgba(2,6,23,.05)", center: true } },

  "welcome":           { w: 1, h: 72, label: "Chào mừng, [Tên] — lời chúc + nút hành động nhanh", opts: { strip: CHROME } },
  "quick-stats":       { w: 1, h: 76, label: "3 thẻ số: Thành viên · Sự kiện sắp tới · Tư liệu mới", opts: { center: true } },
  "recent-activities": { w: 1, h: 120, label: "Hoạt động gần đây: 4 dòng sự kiện", opts: {} },
  "upcoming-events":   { w: 1, h: 120, label: "Sự kiện sắp tới", opts: {} },
  "birthday-list":     { w: 1, h: 120, label: "Sinh nhật tháng này", opts: {} },

  "search-bar":        { w: 1, h: 52, label: "Tìm kiếm: Ô nhập + nút Tìm", opts: { center: true } },
  "filter-chips":      { w: 1, h: 36, label: "Chip lọc: Thành viên · Bài viết · Sự kiện · Tư liệu · Tất cả", opts: { center: true } },
  "search-results":    { w: 1, h: 300, label: "Kết quả tìm kiếm: danh sách 4 mục", opts: {} },

  "toolbar":           { w: 1, h: 40, label: "Thanh công cụ: Tìm kiếm · Lọc · Sắp xếp · Thêm mới (+)", opts: { center: true } },
  "tree":              { w: 1, h: 320, label: "Cây gia phả: các node thế hệ 1-2-3 nối bằng đường", opts: { color: "rgba(16,185,129,.10)", center: true } },
  "graph":             { w: 1, h: 320, label: "Đồ thị quan hệ: node + cạnh", opts: { color: "rgba(16,185,129,.10)", center: true } },
  "relation-form":     { w: 1, h: 110, label: "Chọn A · Chọn B · Kiểm tra quan hệ", opts: { center: true } },
  "relation-result":   { w: 1, h: 150, label: "Kết quả: quan hệ giữa A và B (mô tả + đường ngắn nhất)", opts: {} },
  "profile-header":    { w: 1, h: 96, label: "Avatar · Họ tên · Ngày sinh · Quan hệ gốc · Nút Chỉnh sửa", opts: { strip: GREEN } },
  "profile-tabs":      { w: 1, h: 36, label: "Tabs: Tổng quan · Nghề nghiệp · Tư liệu · Câu chuyện", opts: { strip: CHROME } },
  "profile-detail":    { w: 1, h: 240, label: "Chi tiết hồ sơ: 2 cột thông tin", opts: { center: true } },
  "form":              { w: 1, h: 300, label: "Form nhập liệu (placeholder)", opts: { center: true } },
  "relation-preview":  { w: 1, h: 150, label: "Xem trước quan hệ: node gợi ý trước khi lưu", opts: { color: "rgba(16,185,129,.10)", center: true } },

  "family-header":     { w: 1, h: 96, label: "Ảnh bìa · Tên gia đình · Khu vực · Nút: Thêm thành viên", opts: { strip: GREEN } },
  "family-stats":      { w: 1, h: 76, label: "4 thẻ số: Thành viên · Nhánh · Tư liệu · Sự kiện", opts: { center: true } },
  "family-detail":     { w: 1, h: 240, label: "Thông tin chi tiết: 2 cột", opts: { center: true } },
  "branch-tree":       { w: 1, h: 260, label: "Cây nhánh: sơ đồ phân nhánh", opts: { color: "rgba(16,185,129,.10)", center: true } },
  "branch-actions":    { w: 1, h: 100, label: "Hành động nhánh: Đổi tên · Sáp nhập · Xóa · Tạo nhánh mới", opts: { center: true } },
  "member-table":      { w: 1, h: 280, label: "Bảng thành viên: Tên · Ngày sinh · Quan hệ · Vai trò · Trạng thái", opts: {} },
  "request-list":      { w: 1, h: 280, label: "Danh sách yêu cầu tham gia: Hồ sơ · Quan hệ khai báo · Nút Duyệt / Từ chối", opts: {} },

  "composer":          { w: 1, h: 84, label: "Ô soạn bài: Đang nghĩ gì? + nút Đăng", opts: { center: true } },
  "feed":              { w: 1, h: 320, label: "Luồng bài viết: 3 bài (avatar · nội dung · like/comment/share)", opts: {} },
  "post-detail":       { w: 1, h: 240, label: "Chi tiết bài viết: nội dung + ảnh", opts: {} },
  "comments":          { w: 1, h: 180, label: "Bình luận: 3 comment + ô nhập", opts: {} },
  "post-form":         { w: 1, h: 260, label: "Form tạo bài viết: tiêu đề · nội dung · ảnh · tệp", opts: { center: true } },
  "news-list":         { w: 1, h: 300, label: "Tin gia đình: danh sách 4 tin", opts: {} },
  "announce-form":     { w: 1, h: 260, label: "Form tạo thông báo: tiêu đề · nội dung · đối tượng", opts: { center: true } },
  "preview-pane":      { w: 1, h: 200, label: "Xem trước thông báo", opts: { color: "rgba(2,6,23,.05)", center: true } },

  "calendar":          { w: 1, h: 300, label: "Lịch tháng: 6 dòng x 7 cột, đánh dấu ngày có sự kiện", opts: { color: "rgba(245,158,11,.10)", center: true } },
  "event-list":        { w: 1, h: 300, label: "Danh sách sự kiện: 4 mục (tên · ngày · địa điểm · trạng thái)", opts: {} },
  "event-header":      { w: 1, h: 120, label: "Ảnh bìa sự kiện · Tên · Thời gian · Địa điểm", opts: { strip: AMBER } },
  "rsvp-actions":      { w: 1, h: 64, label: "RSVP: [Sẽ tham dự] [Có thể] [Không tham dự]", opts: { center: true } },
  "event-info":        { w: 1, h: 120, label: "Thông tin sự kiện: mô tả · chủ trì · liên hệ", opts: {} },
  "attendee-list":     { w: 1, h: 120, label: "Người tham gia: Going (12) · Maybe (4)", opts: {} },
  "invite-pane":       { w: 1, h: 160, label: "Chọn khách mời + mẫu thư mời", opts: { color: "rgba(245,158,11,.08)", center: true } },
  "attendee-table":    { w: 1, h: 260, label: "Bảng người tham gia: Tên · Trạng thái RSVP · Phản hồi", opts: {} },
  "status-chart":      { w: 1, h: 150, label: "Biểu đồ RSVP: Going/Maybe/Not Going", opts: { center: true } },
  "album-toolbar":     { w: 1, h: 40, label: "Thanh công cụ: Upload · Sắp xếp · Chế độ xem", opts: { center: true } },
  "photo-grid":        { w: 1, h: 260, label: "Lưới ảnh 3 cột (placeholder ảnh)", opts: { color: "rgba(2,6,23,.05)", center: true } },

  "directory-grid":    { w: 1, h: 300, label: "Lưới danh bạ: 6 thẻ thành viên (avatar · tên · quan hệ)", opts: {} },
  "career-timeline":   { w: 1, h: 260, label: "Timeline nghề nghiệp / học vấn", opts: {} },
  "adv-search":        { w: 1, h: 120, label: "Form tìm kiếm nâng cao: tên · tuổi · nghề · khu vực · quan hệ", opts: { center: true } },

  "archive-cards":     { w: 1, h: 300, label: "Kho lưu trữ: 6 thẻ (tư liệu · ảnh · câu chuyện · kỷ vật)", opts: {} },
  "doc-list":          { w: 1, h: 300, label: "Danh sách tư liệu: 4 mục (tên · loại · năm · người đóng góp)", opts: {} },
  "story-cards":       { w: 1, h: 260, label: "Câu chuyện gia đình: 4 thẻ", opts: {} },
  "honor-list":        { w: 1, h: 260, label: "Thành viên tiêu biểu: danh sách xếp hạng + khen thưởng", opts: {} },
  "timeline":          { w: 1, h: 120, label: "Dòng thời gian ảnh", opts: { color: "rgba(2,6,23,.05)", center: true } },

  "chat":              { w: 1, h: 360, label: "Trợ lý AI: hội thoại (hỏi — đáp kèm trích dẫn nguồn)", opts: { color: "rgba(59,130,246,.08)", center: true } },
  "semantic-results":  { w: 1, h: 200, label: "Kết quả ngữ nghĩa: các mục nổi bật", opts: {} },
  "source-cards":      { w: 1, h: 120, label: "Thẻ nguồn: hồ sơ · tư liệu liên quan", opts: {} },

  "stats-cards":       { w: 1, h: 90, label: "4 thẻ KPI: Tổng · Tăng trưởng · …", opts: { center: true } },
  "chart-line":        { w: 1, h: 180, label: "Biểu đồ đường: xu hướng (placeholder)", opts: { color: "rgba(59,130,246,.08)", center: true } },
  "chart-bar":         { w: 1, h: 180, label: "Biểu đồ cột: phân bố (placeholder)", opts: { color: "rgba(59,130,246,.08)", center: true } },
  "chart-donut":       { w: 1, h: 180, label: "Biểu đồ tròn: cơ cấu (placeholder)", opts: { color: "rgba(59,130,246,.08)", center: true } },
  "event-stats":       { w: 1, h: 160, label: "Thống kê sự kiện: tham dự · hủy · nhắc nhở", opts: {} },
  "report-form":       { w: 1, h: 180, label: "Form báo cáo: loại · phạm vi · kỳ", opts: { center: true } },
  "report-preview":    { w: 1, h: 180, label: "Xem trước báo cáo", opts: { color: "rgba(2,6,23,.05)", center: true } },
  "export-actions":    { w: 1, h: 60, label: "Xuất: PDF · CSV · Lên lịch tự động", opts: { center: true } },

  "admin-table":       { w: 1, h: 240, label: "Bảng dữ liệu admin (placeholder)", opts: {} },
  "user-table":        { w: 1, h: 280, label: "Bảng người dùng: Tên · Email · Vai trò · Trạng thái · Thao tác", opts: {} },
  "moderation-list":   { w: 1, h: 300, label: "Hàng chờ kiểm duyệt: bài viết · ảnh · hồ sơ — Duyệt / Từ chối", opts: {} },
  "filter-bar":        { w: 1, h: 44, label: "Lọc: thời gian · loại · người thực hiện", opts: { center: true } },
  "audit-list":        { w: 1, h: 300, label: "Nhật ký kiểm toán: thời gian · người · hành động · IP", opts: {} },
  "backup-list":       { w: 1, h: 160, label: "Danh sách bản sao lưu: thời điểm · kích thước · trạng thái", opts: {} },
  "backup-schedule":   { w: 1, h: 100, label: "Lịch sao lưu tự động + nút: Sao lưu ngay · Khôi phục", opts: { center: true } },
  "settings-form":     { w: 1, h: 280, label: "Form cấu hình: chung · thông báo · bảo mật · giới hạn", opts: { center: true } },
};

// Fields override (screens.js `fields`) injected into form-like blocks
const FORM_BLOCKS = ["auth-card", "form", "announce-form", "post-form", "report-form", "settings-form", "adv-search"];

function applyFields(blocks, s) {
  if (!s.fields) return;
  for (const b of blocks) {
    if (FORM_BLOCKS.includes(b.t)) b.fields = Object.entries(s.fields);
  }
}

const CARD_W = 30, CARD_H = 44, CARD_X = 30, CARD_Y = 30; // page interior offset
const PAGE_W = 794, PAGE_H = 1123, HEADER_H = 56;

function svgBlock(s, b) {
  const f = [];
  const color = b.color || (b.strip ? "#ffffff" : "#ffffff");
  f.push(`<rect x="${b.x}" y="${b.y}" width="${b.w}" height="${b.h}" rx="4" fill="${color}" stroke="${BORDER}" stroke-width="1"/>`);
  if (b.strip) f.push(`<rect x="${b.x}" y="${b.y}" width="4" height="${b.h}" rx="2" fill="${b.strip}"/>`);
  if (b.labelRight) {
    f.push(`<rect x="${b.x + 10}" y="${b.y + 8}" width="26" height="12" rx="3" fill="${CHROME}"/><rect x="${b.x + 42}" y="${b.y + 13}" width="${Math.max(40, b.w - 140)}" height="3" rx="1.5" fill="${LIGHT}"/><rect x="${b.x + Math.max(40, b.w - 140) + 52}" y="${b.y + 8}" width="22" height="12" rx="3" fill="${LIGHT}"/>`);
    return f.join("");
  }
  if (b.center) {
    const lines = wrap(b.label || "", Math.max(2, Math.floor(b.w / 92)));
    lines.forEach((ln, i) => f.push(`<text x="${b.x + b.w / 2}" y="${b.y + b.h / 2 - ((lines.length - 1) * 7) / 2 + i * 14}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="${GRAY}">${esc(ln)}</text>`));
    return f.join("");
  }
  const lx = b.x + 12, ly = b.y + 18;
  f.push(`<text x="${lx}" y="${ly}" font-family="Segoe UI, Arial, sans-serif" font-size="11.5" fill="${SLATE}">${esc(b.label)}</text>`);
  const rows = b.h >= 60 ? Math.max(1, Math.floor((b.h - 34) / 14)) : 0;
  for (let i = 0; i < rows; i++) {
    const ry = ly + 18 + i * 14;
    const rw = b.w - (i % 2 === 0 ? 70 : 120);
    if (rw > 60) f.push(`<rect x="${lx}" y="${ry}" width="${rw}" height="3" rx="1.5" fill="${LIGHT}"/>`);
  }
  if (b.fields) {
    const fy = ly + 8;
    b.fields.forEach(([k, lbl], i) => {
      if (fy + i * 40 > b.y + b.h - 20) return;
      const rowY = fy + i * 40;
      f.push(`<text x="${lx}" y="${rowY}" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="${SLATE}">${esc(lbl)}</text>`);
      f.push(`<rect x="${lx}" y="${rowY + 6}" width="${b.w - 60}" height="18" rx="3" fill="#F8FAFC" stroke="${BORDER}" stroke-width="1"/>`);
    });
  }
  return f.join("");
}

function buildPage(s) {
  const W = { s: 1440, t: 768, m: 375 }[s.size];
  const H = { s: 900, t: 800, m: 700 }[s.size];
  const blocks = layout({ ...s, W: undefined, size: s.size, h: H, w: W });
  applyFields(blocks, s);
  return { W, H, blocks };
}

function svgFor(s) {
  const { W, H, blocks } = buildPage(s);
  const header = `<rect x="0" y="0" width="${W}" height="${HEADER_H}" fill="#0F172A"/><text x="28" y="36" font-family="Segoe UI, Arial, sans-serif" font-size="19" font-weight="600" fill="#fff">${esc("W·" + s.code + " " + s.title)}</text>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">${header}${blocks.map(b => svgBlock(s, b)).join("")}</svg>`;
}

function esc(t) { return (t || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function wrap(t, n) {
  const words = t.split(" ");
  const lines = []; let cur = "";
  for (const w of words) { if ((cur + " " + w).trim().length > n && cur) { lines.push(cur); cur = w; } else cur = (cur + " " + w).trim(); }
  if (cur) lines.push(cur);
  return lines;
}

const SIZE_NAMES = { s: "desktop", t: "tablet", m: "mobile" };
(async () => {
  const browser = await puppeteer.launch({ executablePath: BRAVE, args: ["--no-sandbox", "--disable-gpu"] });
  const page = await browser.newPage();
  const dirs = ["desktop", "tablet", "mobile"];
  for (const d of dirs) fs.mkdirSync(path.join(OUT, d), { recursive: true });

  for (const s of screens) {
    for (const size of Object.keys(SIZE_NAMES)) {
      const svg = svgFor({ ...s, size });
      await page.setContent(`<!doctype html><style>body{margin:0}</style>${svg}`);
      const el = await page.$("svg");
      const box = await el.boundingBox();
      const scale = Math.min(2, 2000 / box.width);
      await page.setViewport({ width: Math.ceil(box.width * scale), height: Math.ceil(box.height * scale) });
      await el.screenshot({ path: path.join(OUT, SIZE_NAMES[size], `${s.code.replaceAll("/", "-")}.png`) });
    }
    console.log(s.code);
  }
  await browser.close();
  console.log("DONE");
})().catch(e => { console.error(e); process.exit(1); });
