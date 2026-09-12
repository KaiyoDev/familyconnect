"""API response helpers (mirror of teacher's src/api/responses.py).

Responsibility: centralize HTTP response envelopes returned by controllers.
Teacher used Flask `jsonify` (success_response, error_response, ...).
FastAPI adaptation: replace `jsonify` with `fastapi.responses.JSONResponse`
or Pydantic response models defined in `api/schemas/`.

NOTE: implementation deferred to the Business Logic / API step.
"""
