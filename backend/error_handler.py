"""Global error handlers (mirror of teacher's src/error_handler.py).

Responsibility: translate uncaught exceptions / domain errors into uniform
HTTP responses.
Teacher used `app.register_error_handler`. FastAPI adaptation: exception
handlers are registered via `app.add_exception_handler` / `@app.exception_handler`
and are currently set up in `app/api/middleware.py` (DomainException handler +
generic handler). This module is reserved per the teacher architecture.

NOTE: implementation deferred to the wire-up step.
"""
