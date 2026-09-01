"""CORS configuration (mirror of teacher's src/cors.py).

Responsibility: configure Cross-Origin Resource Sharing for the API.
Teacher used `flask_cors.CORS`. FastAPI adaptation: `fastapi.middleware.cors.CORSMiddleware`
is currently registered in `app/api/middleware.py` (register_middleware).
This module is reserved per the teacher architecture.

NOTE: implementation deferred to the wire-up step.
"""
