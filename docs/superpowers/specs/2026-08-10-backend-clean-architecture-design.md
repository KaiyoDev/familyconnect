# Backend Clean Architecture Design

**Date:** 2026-08-10
**Status:** Approved
**Scope:** Sprint 2 Backend Scaffolding (Skeleton Only)

## Overview

Create a clean backend scaffolding for FamilyConnect using FastAPI with a 4-layer Clean Architecture pattern. The backend will be empty of business features—only structure, config, database connection, Alembic migrations, and a health check endpoint.

## Architecture Overview

**4-layer Clean Architecture** based on the Flask-CleanArchitecture template, adapted for FastAPI with improvements.

```
backend/
├── app/
│   ├── api/              # Presentation layer
│   │   ├── controllers/  # Route handlers (FastAPI routers)
│   │   ├── schemas/      # Pydantic request/response models
│   │   ├── middleware.py # CORS, logging, error handling
│   │   └── dependencies.py # FastAPI DI providers
│   │
│   ├── services/         # Application/Business logic layer
│   │   └── ...           # Use case orchestrators
│   │
│   ├── domain/           # Domain layer (core)
│   │   ├── models/       # Business entities (Pydantic/dataclass)
│   │   ├── interfaces/   # Repository interfaces (ABC)
│   │   ├── constants.py  # Business constants
│   │   └── exceptions.py # Domain exceptions
│   │
│   └── infrastructure/   # Infrastructure layer
│       ├── databases/    # DB engine, session, adapters
│       ├── models/       # SQLAlchemy ORM models
│       └── repositories/ # Repository implementations
│
├── migrations/           # Alembic migrations
├── config.py             # pydantic-settings config
├── main.py               # FastAPI app factory + uvicorn
├── requirements.txt
└── .env
```

### Key Improvements Over Template

| Template (Flask) | FamilyConnect (FastAPI) |
|---|---|
| Flask Blueprints | FastAPI APIRouter |
| Marshmallow schemas | Pydantic v2 models |
| Manual session.close() mỗi method | Context manager session |
| DI container khai báo không dùng | FastAPI Depends() DI |
| `create_all()` | Alembic migrations |
| Hardcoded credentials | pydantic-settings + .env |
| flasgger swagger | FastAPI auto OpenAPI |
| `app.run()` | uvicorn runner |

## Layer Responsibilities

### API Layer (Presentation)

Handles HTTP requests, validation, and response formatting.

- **Controllers:** FastAPI APIRouter instances with route handlers
- **Schemas:** Pydantic v2 models for request/response validation
- **Middleware:** CORS, request logging, exception handling
- **Dependencies:** FastAPI Depends() providers (DB session injection)

### Services Layer (Application Logic)

Orchestrates use cases and business workflows. Empty in scaffolding.

- Calls domain interfaces (not infrastructure directly)
- Implements application-specific business rules
- Transaction boundaries for multi-step operations

### Domain Layer (Core)

Business entities and contracts. No framework dependencies.

- **Models:** Pure business entities (Pydantic dataclasses or BaseModels)
- **Interfaces:** ABC contracts for repositories (e.g., `IUserRepository`)
- **Constants:** Business rules (`MAX_FAMILY_MEMBERS = 20`)
- **Exceptions:** Domain-specific errors (`FamilyNotFoundException`)

### Infrastructure Layer (External Concerns)

Implements domain interfaces and external integrations.

- **Databases:** SQLAlchemy async engine, session management
- **Models:** SQLAlchemy ORM models (table definitions)
- **Repositories:** Implement domain interfaces with actual DB queries

### Data Flow

```
Controller → Service → Domain Interface (ABC) → Repository (impl) → DB
   ↑                                              ↑
   API layer                                   Infra layer
```

## Config & Environment

### pydantic-settings Configuration

```python
# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FamilyConnect API"
    debug: bool = False
    database_url: str  # required in .env
    secret_key: str
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"

settings = Settings()
```

### Environment File

```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/familyconnect
SECRET_KEY=dev-secret-change-in-prod
DEBUG=true
```

### Async Database

Uses `asyncpg` + SQLAlchemy async. FastAPI is natively async, no thread blocking.

## Database & Migration

### SQLAlchemy Async Setup

```python
# infrastructure/databases/database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from infrastructure.databases.base import Base
from config import settings

engine = create_async_engine(settings.database_url, echo=settings.debug)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
```

### Base Model with Timestamps

```python
# infrastructure/databases/base.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
```

### Alembic Migration

```bash
alembic init migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
```

## Middleware & Error Handling

### Middleware Registration

```python
# api/middleware.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from domain.exceptions import DomainException
import time

def register_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = round((time.time() - start) * 1000, 2)
        app.logger.info(f"{request.method} {request.url.path} — {response.status_code} ({duration}ms)")
        return response

    @app.exception_handler(DomainException)
    async def domain_exception_handler(request: Request, exc: DomainException):
        return JSONResponse(status_code=exc.status_code, content={"error": exc.message})
```

### Domain Exceptions

```python
# domain/exceptions.py
class DomainException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class NotFoundException(DomainException):
    def __init__(self, message="Resource not found"):
        super().__init__(message, 404)
```

## App Factory

```python
# main.py
from fastapi import FastAPI
from api.controllers.health_controller import router as health_router
from api.middleware import register_middleware

def create_app() -> FastAPI:
    app = FastAPI(title="FamilyConnect API", version="0.1.0")
    register_middleware(app)
    app.include_router(health_router, tags=["Health"])
    return app

app = create_app()
```

## Health Check Endpoint

```python
# api/controllers/health_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from api.dependencies import get_db

router = APIRouter()

@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "healthy", "database": "connected"}
```

## Dependencies

```txt
# requirements.txt
fastapi>=0.110
uvicorn>=0.29
sqlalchemy>=2.0
asyncpg>=0.29
pydantic-settings>=2.2
alembic>=1.13
python-dotenv>=1.0
```

## Final Folder Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── controllers/
│   │   │   └── health_controller.py
│   │   ├── schemas/
│   │   │   └── .gitkeep
│   │   ├── middleware.py
│   │   └── dependencies.py
│   ├── services/
│   │   └── .gitkeep
│   ├── domain/
│   │   ├── models/
│   │   │   └── .gitkeep
│   │   ├── interfaces/
│   │   │   └── .gitkeep
│   │   ├── constants.py
│   │   └── exceptions.py
│   └── infrastructure/
│       ├── databases/
│       │   ├── database.py
│       │   └── base.py
│       ├── models/
│       │   └── .gitkeep
│       └── repositories/
│           └── .gitkeep
├── migrations/
│   └── (alembic init)
├── config.py
├── main.py
├── requirements.txt
└── .env
```

## Run Command

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Next Steps

After scaffolding is complete, add features incrementally:
1. Auth module (JWT + User entity)
2. Family module (Family + Member entities)
3. Check-in module
4. Feed module
5. Notifications module

Each feature follows the same pattern: domain interface → infrastructure repository → service → API controller.
