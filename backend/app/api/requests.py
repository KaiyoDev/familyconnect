"""API request helpers (mirror of teacher's src/api/requests.py).

Responsibility: extract / validate inbound request data before it reaches a
controller or service. Teacher validated Marshmallow schemas here.
FastAPI adaptation: request validation is handled declaratively by Pydantic
schemas in `api/schemas/` plus FastAPI `Depends`, so this module is reserved
for cross-cutting request helpers.

NOTE: implementation deferred to the Business Logic / API step.
"""
