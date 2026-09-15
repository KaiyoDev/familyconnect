---
version: alpha
name: FamilyConnect-design
description: FamilyConnect presents itself as an AI-powered digital family community platform through a calm, minimalist-modern brand voice (shadcncraft reference) — anchored by a teal primary (#0D9488) used with restraint, a neutral-dominant palette, and Inter typography across every UI surface. The system targets family users of all ages (seniors included): large type (16px base), AA contrast, generous spacing on a 4px grid, soft shadows, sober radius (input 6px, card/button 10px, modal 12px). Coverage spans the Web Portal: 48 hi-fi UI screens x 3 breakpoints (Desktop 1440 / Tablet 768 / Mobile 375), 4 roles (Guest, Member, Owner, Admin), RBAC-driven menus.

colors:
  primary: "#0D9488"
  primary-dark: "#0F766E"
  primary-light: "#CCFBF1"
  on-primary: "#FFFFFF"
  accent: "#F59E0B"
  accent-light: "#FEF3C7"
  success: "#16A34A"
  success-bg: "#F0FDF4"
  warning: "#D97706"
  warning-bg: "#FFFBEB"
  danger: "#DC2626"
  danger-bg: "#FEF2F2"
  info: "#0284C7"
  info-bg: "#F0F9FF"
  neutral-0: "#FFFFFF"
  neutral-50: "#F8FAFC"
  neutral-100: "#F1F5F9"
  neutral-200: "#E2E8F0"
  neutral-300: "#CBD5E1"
  neutral-500: "#64748B"
  neutral-700: "#334155"
  neutral-900: "#0F172A"
  text-on-primary: "#FFFFFF"
  pink: "#DB2777"
  pink-light: "#FDF2F8"

typography:
  display-1:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.20
  display-2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
  heading-1:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.30
  heading-2:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
  heading-3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.40
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
  body-md-medium:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  label:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.40
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30

rounded:
  xs: 4px
  sm: 6px
  md: 10px
  lg: 12px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-primary-hover:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-700}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
    border: "1px solid {colors.neutral-300}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-700}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  text-input:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-900}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    border: "1px solid {colors.neutral-300}"
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-900}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-900}"
    border: "2px solid {colors.danger}"
  card-base:
    backgroundColor: "{colors.neutral-0}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.neutral-200}"
  card-feature:
    backgroundColor: "{colors.neutral-0}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.neutral-200}"
  tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm-medium}"
    border: "0 0 2px {colors.primary} solid"
  tab-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-500}"
    typography: "{typography.body-sm-medium}"
    border: "0 0 2px transparent solid"
  table-header:
    backgroundColor: "{colors.neutral-100}"
    textColor: "{colors.neutral-700}"
    typography: "{typography.body-sm-medium}"
    padding: "12px 16px"
  table-row:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-700}"
    typography: "{typography.body-sm}"
    padding: "12px 16px"
    border: "0 0 1px {colors.neutral-200} solid"
  modal:
    backgroundColor: "{colors.neutral-0}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    shadow: "rgba(15, 23, 42, 0.15) 0px 8px 24px 0px"
  drawer:
    backgroundColor: "{colors.neutral-0}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    shadow: "rgba(15, 23, 42, 0.15) 0px 8px 24px 0px"
  overlay:
    backgroundColor: "rgba(15, 23, 42, 0.40)"
  toast-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  toast-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
  toast-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
  toast-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info}"
  badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
  badge-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning}"
  badge-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger}"
  avatar:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-dark}"
    rounded: "{rounded.full}"
  tree-node-male:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-900}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
  tree-node-female:
    backgroundColor: "{colors.neutral-0}"
    textColor: "{colors.neutral-900}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.pink}"
  tree-node-founder:
    backgroundColor: "{colors.accent-light}"
    textColor: "{colors.neutral-900}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.accent}"
  skeleton:
    backgroundColor: "{colors.neutral-200}"
    rounded: "{rounded.xs}"
  empty-state:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-500}"
    padding: "{spacing.xxl}"
---

## Overview

FamilyConnect là nền tảng Cộng đồng Gia đình số tích hợp Trí tuệ nhân tạo: kết nối các thế hệ phân tán địa lý qua cây gia phả, giao tiếp, sự kiện, di sản và trợ lý AI trong một hệ sinh thái thống nhất. Web Portal phục vụ 4 vai trò (Guest, Member, Owner, Admin), responsive 3 breakpoint (Desktop 1440 / Tablet 768 / Mobile 375), 48 hi-fi UI màn hình.

Phong cách: **minimalist modern** (tham chiếu shadcncraft). UI gọn, không trang trí thừa, nội dung là trọng tâm. Màu neutral chiếm phần lớn giao diện, primary teal dùng có chủ đích (CTA, link, active state). Spacing rộng trên grid 4px, shadow nhẹ, radius vừa phải. Không gradient nặng, không hiệu ứng thừa.

**Key Characteristics:**
- Teal primary ({colors.primary}) dành cho hành động chính, link, trạng thái active; không tràn lan
- Neutral scale ({colors.neutral-50..900}) là xương sống giao diện: nền, surface, border, text
- Semantic màu riêng (success/warning/danger/info) kèm nền nhạt (bg) cho alert/badge/toast
- Inter trên mọi surface (fallback Be Vietnam Pro cho tiếng Việt)
- Radius: input 6px ({rounded.sm}), card/button 10px ({rounded.md}), modal 12px ({rounded.lg})
- Tree node gia phả mã màu theo giới tính: nam primary, nữ pink ({colors.pink}), ông tổ highlight accent
- 16px base text (phù hợp người lớn tuổi), contrast AA

## Colors

> Nguồn: spec FamilyConnect (03_UIUXDesign.md), tông teal, thang neutral shadcn/ui.

### Brand & Primary
- **Primary Teal** ({colors.primary}): Hành động chính, link, active state. Dùng có chủ đích, không tràn lan.
- **Primary Dark** ({colors.primary-dark}): Hover, sidebar, header.
- **Primary Light** ({colors.primary-light}): Nền active, badge nhạt, avatar fallback.
- **Accent Amber** ({colors.accent}): Sự kiện, nhấn mạnh, RSVP, highlight ông tổ.
- **Pink** ({colors.pink}): Màu nữ trong tree node (thân tộc).

### Semantic
- **Success** ({colors.success}): Thành công, đã duyệt. Nền {colors.success-bg}.
- **Warning** ({colors.warning}): Cảnh báo, chờ duyệt. Nền {colors.warning-bg}.
- **Danger** ({colors.danger}): Lỗi, từ chối, xóa. Nền {colors.danger-bg}.
- **Info** ({colors.info}): Thông tin, AI. Nền {colors.info-bg}.

### Neutral Scale
- **Neutral 0** ({colors.neutral-0}): Nền trang, thẻ, canvas.
- **Neutral 50** ({colors.neutral-50}): Nền trang đậm hơn, section.
- **Neutral 100** ({colors.neutral-100}): Nền khối, table header, hover.
- **Neutral 200** ({colors.neutral-200}): Border nhạt, divider.
- **Neutral 300** ({colors.neutral-300}): Border, input border.
- **Neutral 500** ({colors.neutral-500}): Text phụ, placeholder.
- **Neutral 700** ({colors.neutral-700}): Text chính.
- **Neutral 900** ({colors.neutral-900}): Header, tiêu đề.

## Typography

### Font Family
**Inter** (font chính shadcncraft). Fallback: Be Vietnam Pro, Segoe UI, sans-serif (Be Vietnam Pro dùng khi cần hỗ trợ tiếng Việt tốt hơn).

### Hierarchy

| Token | Size | Weight | Line Height | Use |
|---|---|---|---|---|
| `{typography.display-1}` | 40px | 700 | 1.20 | Landing hero, trang công khai |
| `{typography.display-2}` | 32px | 700 | 1.25 | Section mở đầu |
| `{typography.heading-1}` | 24px | 600 | 1.30 | Tiêu đề trang |
| `{typography.heading-2}` | 20px | 600 | 1.35 | Tiêu đề section, card |
| `{typography.heading-3}` | 18px | 600 | 1.40 | Card title |
| `{typography.body-md}` | 16px | 400 | 1.50 | Body chính (base) |
| `{typography.body-md-medium}` | 16px | 500 | 1.50 | Body nhấn |
| `{typography.body-sm}` | 14px | 400 | 1.50 | Body phụ, table |
| `{typography.body-sm-medium}` | 14px | 500 | 1.50 | Menu active, tab |
| `{typography.label}` | 14px | 600 | 1.40 | Form label |
| `{typography.caption}` | 12px | 400 | 1.40 | Badge, meta |
| `{typography.button-md}` | 14px | 500 | 1.30 | Button label |

### Principles
- 16px base (tối thiểu body), phù hợp người lớn tuổi
- Heading 600-700, button 500, body 400
- Line-height heading 1.2-1.4, body 1.5
- Không chữ toàn uppercase (trừ micro-label nếu cần)

## Layout

### Spacing System
- **Base unit**: 4px. Tokens: `{spacing.xxs}` (4px) → `{spacing.section}` (64px).
- Card padding: 16-24px. Form gap: 16px. Section gap: 32-48px.

### Grid & Container
| Breakpoint | Width | Hành vi |
|---|---|---|
| Desktop | ≥ 1024 (base 1440) | Sidebar cố định 220px, multi-column, table |
| Tablet | 768 | Sidebar thu icon 64px hoặc drawer |
| Mobile | 375 | Drawer menu + bottom nav 5 tab: Trang chủ, Gia phả, Sự kiện, Di sản, Cá nhân |

### Whitespace Philosophy
Spacing rộng rãi, thở; form nặng tối ưu Desktop, core thao tác (xem cây, feed, RSVP) đầy đủ Mobile.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | Không shadow; border `{colors.neutral-200}` | Card mặc định, table |
| 1 (card) | `rgba(15, 23, 42, 0.08) 0px 1px 3px 0px` | Card, thẻ nhẹ |
| 2 (modal) | `rgba(15, 23, 42, 0.15) 0px 8px 24px 0px` | Modal, drawer, dropdown |

Shadow nhẹ, không đổ bóng mạnh (minimalist).

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Skeleton, chip nhỏ |
| `{rounded.sm}` | 6px | Input, select, textarea |
| `{rounded.md}` | 10px | Card, button, toast, table |
| `{rounded.lg}` | 12px | Modal, drawer |
| `{rounded.full}` | 9999px | Avatar, badge, chip, bottom nav |

## Components

> Spec đầy đủ từng component: `docs/SDD/03_UIUXDesign.md` mục 7. Tại đây ghi token-binding bản chuẩn.

### Buttons
- **`button-primary`**: nền `{colors.primary}`, text `{colors.on-primary}`, radius `{rounded.md}`, padding 10px 18px, weight 500. Hover: `{colors.primary-dark}`.
- **`button-secondary`**: trong suốt, viền `1px {colors.neutral-300}`, text `{colors.neutral-700}`.
- **`button-ghost`**: trong suốt, text `{colors.neutral-700}`.
- **`button-danger`**: nền `{colors.danger}`, text trắng.
- Kích thước: sm 32 / md 40 / lg 48. Disabled: nền neutral-200, text neutral-500. Min touch target 44px.

### Inputs & Forms
- **`text-input`**: nền trắng, viền `{colors.neutral-300}`, radius `{rounded.sm}` (6px), height 44px.
- Focus: viền 2px `{colors.primary}`. Error: viền 2px `{colors.danger}` + message danger.
- Label: `{typography.label}` 14px 600. Placeholder: `{colors.neutral-500}`.
- Select/Textarea: cùng hệ input. Checkbox/Radio: focus ring primary.

### Tabs
- Underline: active `{colors.primary}` 2px dưới, height 40px. Inactive: text `{colors.neutral-500}`.
- Segment: pill active nền `{colors.primary}`, text trắng.

### Table
- Header: nền `{colors.neutral-100}`, text 600. Row: zebra neutral-50, hover neutral-50, border `{colors.neutral-200}`.
- Sticky header, đủ 3 breakpoint (mobile: card transform nếu cần).

### Card
- Radius `{rounded.md}` 10px, shadow card nhẹ, padding 16-24, nền trắng trên nền trang neutral-50.

### Modal / Drawer
- Radius `{rounded.lg}` 12px, overlay `{colors.overlay}` (rgba 15,23,42 40%), đóng Esc, focus trap.

### Toast
- 4 loại semantic kèm nền nhạt + text màu đậm tương ứng, auto-dismiss 4s.

### Badge / Tag
- Radius `{rounded.full}`, height 20px, semantic màu, nền nhạt + text đậm.

### Avatar
- Circle `{rounded.full}`, size 24/32/40/48/64, fallback initials nền primary-light text primary-dark.

### Tree Node (gia phả)
- Node thẻ: width ~96px, radius `{rounded.md}`, viền 2px theo giới tính (nam `{colors.primary}`, nữ `{colors.pink}`), ông tổ nền `{colors.accent-light}` viền `{colors.accent}`.
- Nối bằng đường thẳng, pan/zoom, mở rộng nhánh.

### Chart
- Line/bar/donut: primary + neutral, legend, tooltip. Dùng cho dashboard/báo cáo.

### Empty State
- Icon + title + description + CTA, text `{colors.neutral-500}`, padding `{spacing.xxl}`.

### Skeleton
- Loading shimmer: nền `{colors.neutral-200}`, radius `{rounded.xs}`, animation pulse.

## Do's and Don'ts

### Do
- Dùng `{colors.primary}` (teal) cho CTA, link, active state — nhưng tiết chế, neutral là chủ đạo
- Dùng neutral scale làm xương sống: nền, surface, border, text
- Semantic màu kèm nền nhạt (bg) cho alert/badge/toast
- Áp `{rounded.sm}` (6px) cho input, `{rounded.md}` (10px) cho card/button, `{rounded.lg}` (12px) cho modal
- Giữ Inter trên mọi surface, 16px base
- Cây gia phả: mã màu giới tính (nam teal, nữ pink, ông tổ accent)

### Don't
- Không dùng primary cho body text, nền lớn, hoặc trang trí tràn lan
- Không gradient nặng, không đổ bóng mạnh, không hiệu ứng thừa
- Không dùng icon thay nhãn text menu (icon phụ trợ)
- Không trộn style: một component = một cách dùng nhất quán
- Không thiết kế mobile trước khi chốt desktop (responsive-first từ 375 nhưng desktop là chuẩn form nặng)

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Desktop | 1440 (base, ≥1024) | Sidebar 220px, multi-column, table đầy đủ |
| Tablet | 768 | Sidebar thu icon 64px hoặc drawer, 2-column |
| Mobile | 375 | Drawer menu + bottom nav 5 tab, 1-column, form xếp dọc |

### Touch Targets
- Button/input height ≥ 44px (tối thiểu 40 trên desktop)
- Touch target ≥ 44px, focus visible ring primary
- Text ≥ 14px (body 16px), contrast AA (4.5:1 text, 3:1 UI)

### Collapsing Strategy
- **Sidebar**: 220px → icon 64px (tablet) → drawer (mobile) + bottom nav
- **Table**: desktop table → mobile card transform hoặc horizontal scroll
- **Grid card**: multi-column → 2-column tablet → 1-column mobile
- **Form**: 2-column desktop → 1-column mobile
- **Bottom nav**: 5 tab cố định (Trang chủ, Gia phả, Sự kiện, Di sản, Cá nhân)

## Nguồn thiết kế

- Design system token: frontmatter file này (chuyển từ Google Stitch `.gdd`, giữ tham khảo tại `design-system/design-system.gdd`).
- Kit tham chiếu: shadcncraft (https://shadcncraft.com/).
- Hi-fi tham chiếu: `screens/{CODE}-{breakpoint}.png` (desktop / tablet / mobile), render từ Google Stitch.

## Iteration Guide

1. Focus một component/lần
2. Reference component names + tokens trực tiếp
3. Đổi token → cập nhật frontmatter + design tokens cùng lúc
4. Thêm variant → entry riêng trong `components:`
5. Mặc định `{typography.body-md}` cho body
6. Giữ `{colors.primary}` teal là primary CTA, không trộn với semantic
7. Kiểm tra: contrast AA, touch ≥ 44px, focus visible trước khi chốt

## Known Gaps

- Dark mode chưa đặc tả token (chưa trong scope FT8-33)
- Animation/transition chưa đặc tả; đề xuất 150-200ms ease
- Form validation success state chưa đặc tả (error đã có)
- Thang chart color (donut multi-color) chưa chốt đầy đủ
