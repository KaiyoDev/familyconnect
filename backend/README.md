# FamilyConnect Backend

Backend API for FamilyConnect platform built with FastAPI and Clean Architecture.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL with SQLAlchemy (async)
- **Migrations:** Alembic
- **Config:** pydantic-settings

## Architecture

4-layer Clean Architecture:

```
backend/
├── app/
│   ├── api/              # Presentation layer (controllers, schemas, middleware)
│   ├── services/         # Application/Business logic layer
│   ├── domain/           # Domain layer (models, interfaces, exceptions)
│   └── infrastructure/   # Infrastructure layer (databases, repositories)
├── migrations/           # Alembic migrations
├── config.py             # Configuration
└── main.py               # App factory
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Update `.env` with your database credentials.

5. Run migrations:
```bash
alembic upgrade head
```

6. Start server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Migrations

Create new migration:
```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback one migration:
```bash
alembic downgrade -1
```

## Health Check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "healthy", "database": "connected"}
```
