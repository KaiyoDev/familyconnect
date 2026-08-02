# FamilyConnect

Nền tảng kết nối gia đình — giúp các thành viên duy trì liên lạc, chia sẻ khoảnh khắc và quản lý thông tin gia đình.

## Công nghệ

| Tầng | Stack |
|------|-------|
| Backend | Python, FastAPI, PostgreSQL |
| Frontend | React, TypeScript |
| Mobile | React Native |
| Infra | Docker, GitHub Actions |

## Cấu trúc thư mục

```
familyconnect
├── backend/       # API server (FastAPI)
├── frontend/      # Web app (React)
├── docs/          # Tài liệu dự án
├── .github/       # CI/CD templates
└── README.md
```

## Cài đặt

### Yêu cầu hệ thống
- Python 3.11+
- Node.js 20+
- Docker & Docker Compose
- Git

### Clone

```bash
git clone https://github.com/KaiyoDev/familyconnect.git
cd familyconnect
```

### Chạy Backend

```bash
cd backend
# Cài đặt dependencies
pip install -r requirements.txt
# Chạy dev server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Chạy Frontend

```bash
cd frontend
# Cài đặt dependencies
npm install
# Chạy dev server
npm run dev
```

## Branch Strategy

| Branch | Mục đích |
|--------|----------|
| `main` | Production-ready, bảo vệ bởi branch protection |
| `develop` | Tích hợp tính năng mới |
| `feature/*` | Tính năng mới |
| `bugfix/*` | Sửa lỗi |
| `release/*` | Chuẩn bị release |
| `hotfix/*` | Sửa lỗi khẩn cấp trên production |

## Đóng góp

1. Tạo branch từ `develop`: `git checkout -b feature/ten-tinh-nang develop`
2. Commit theo quy ước Conventional Commits
3. Tạo Pull Request vào `develop`
4. Cần tối thiểu 1 approval trước khi merge

## Nhóm phát triển

- Đặng Hoàng Ân
- Lê Kha Bình
- Rcom Chiến
- Bùi Cao Thiên Phước
- Phan Đình Phúc

## License

MIT — xem [LICENSE](LICENSE)
