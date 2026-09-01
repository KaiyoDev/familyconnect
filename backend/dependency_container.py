"""Dependency injection container (mirror of teacher's src/dependency_container.py).

Responsibility: compose / wire infrastructure (db session, repositories,
services) and expose them for injection into controllers.
Teacher used the `dependency_injector` library (containers.DeclarativeContainer).
FastAPI adaptation: dependency wiring is done with `fastapi.Depends` and the
helpers in `app/api/dependencies.py` (e.g. `get_db`). This module is reserved
for a centralized container if one is introduced later.

NOTE: implementation deferred to the DI / Business Logic step.
"""
