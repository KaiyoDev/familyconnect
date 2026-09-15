# Phân tích Kiến trúc Module (NFR-05)

> **Dự án:** FamilyConnect
> **Ngày:** 2026-08-20
> **Chiến lược:** Automated dependency analysis bằng AST parsing + manual review

---

## Layer Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      API Layer                            │
│   (controllers, middleware, routes, dependencies)         │
├──────────────────────────────────────────────────────────┤
│                    Services Layer                         │
│   auth_service, admin_service, family_service,           │
│   community_service, event_service, ai_service           │
├──────────────────────────────────────────────────────────┤
│                Infrastructure Layer                       │
│   repositories, models, databases, mappers, types        │
├──────────────────────────────────────────────────────────┤
│                   Domain Layer                            │
│   interfaces, models, utils, exceptions                  │
├──────────────────────────────────────────────────────────┤
│                   Data Layer (PostgreSQL)                 │
└──────────────────────────────────────────────────────────┘
```

## Dependency Rules

| Từ \ Đến | Domain | Services | Infrastructure | API |
|:---------:|:------:|:--------:|:--------------:|:---:|
| **Domain** | ✅ | ❌ | ❌ | ❌ |
| **Services** | ✅ | ✅ | ✅ | ❌ |
| **Infrastructure** | ✅ | ❌ | ✅ | ❌ |
| **API** | ✅ | ✅ | ✅ | ✅ |

**Nguyên tắc:**
- Domain không import gì từ tầng khác (pure business logic)
- Services được phép import Domain + Infrastructure
- Infrastructure được phép import Domain (IO interfaces)
- API layer được phép import tất cả tầng dưới

---

## Kết quả Phân tích

**✅ Không phát hiện circular imports**
**✅ Không phát hiện forbidden cross-layer dependencies**

### Cross-Layer Dependencies chi tiết

| Source Layer | Target Layer | Số imports | Ví dụ |
|:-----------:||:----------:|:---------:|:-----:|
| `services` | `domain` | 8 | `auth_service → domain.utils.jwt`, `auth_service → domain.utils.password`, `family_service → domain.interfaces.*` |
| `services` | `infrastructure` | 9 | `community_service → infrastructure.models.community`, `event_service → infrastructure.repositories.*` |
| `services` | `schemas` | 1 | `auth_service → schemas.auth` |
| `infrastructure.repositories` | `domain` | 5 | `family_repository → domain.interfaces.family_repository` (Dependency Injection) |
| `api.controllers` | `services` | 4 | `auth_controller → services.auth_service` |
| `api.controllers` | `infrastructure` | 7 | `ai_controller → infrastructure.databases.database` |
| `api.middleware` | `domain` | 1 | `middleware → domain.exceptions` |
| `api.middleware` | `infrastructure` | 2 | `middleware → infrastructure.databases.database` |

### Domain Layer Isolation

Domain layer (7 modules) hoàn toàn **không phụ thuộc** vào bất kỳ tầng nào khác:
- `domain.exceptions` — pure Python
- `domain.interfaces.*` — only `RepositoryBase`
- `domain.utils.*` — `passlib`, `jose` (external)
- `domain.models.*` — pure Pydantic/ORM models

Lớp domain đảm bảo có thể được test và thay thế độc lập.

---

## Module Graph

```
api.controllers ──→ services ──→ infrastructure.repositories
    │                             │       └──→ infrastructure.models
    │                             │
    │                             └──→ infrastructure.databases
    │
    └──→ api.middleware ──→ infrastructure.databases
                          └──→ infrastructure.models.admin (Notification)

services ──→ domain.utils (jwt, password)
          ──→ domain.interfaces.* (DI contracts)
          ──→ domain.exceptions

infrastructure.repositories ──→ domain.interfaces.* (IO contracts)

infrastructure.models ──→ infrastructure.databases.base (Base, mixins)
```

---

## Đánh giá

| Tiêu chí | Kết quả | Ghi chú |
|:---------|:-------:|:--------|
| **Separation of Concerns** | ✅ | 4 tầng rõ ràng |
| **Domain Isolation** | ✅ | Domain không phụ thuộc tầng khác |
| **Dependency Rule** | ✅ | Không có domain → services/infrastructure |
| **Circular Imports** | ✅ | Không phát hiện |
| **Repository Pattern** | ✅ | Repositories implement domain interfaces |
| **DI Readiness** | ✅ | Tất cả service đều inject repository |
| **Testability** | ✅ | Services test được bằng mock repositories |

**Kết luận:** Kiến trúc module FamilyConnect tuân thủ đúng nguyên tắc phân tách tầng. Không có vi phạm nào về luồng dependency. Tất cả module có thể được unit test độc lập thông qua mock interfaces.

---

## Khuyến nghị

1. **Giảm Infrastructure coupling trong API Controllers:** Một số controller (`ai_controller`, `auth_controller`) gọi trực tiếp `infrastructure.databases.database` thay vì thông qua service nên được tái cấu trúc.
2. **Repository interfaces:** `CommentRepository`, `ReactionRepository`, `PostRepository` hiện không implement interface chung — nên thêm `ICommentRepository` vào `domain.interfaces`.
3. **Domain exception normalization:** `family_service` dùng `NotFoundException`/`ValidationException` từ `domain.exceptions`, nhưng `community_service` và `admin_service` tự define exception riêng — nên chuẩn hóa.