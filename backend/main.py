"""FastAPI application entry point (mirror of teacher's src/app.py).

Responsibility: create app instance and run the server.
Teacher used `create_app()` from `create_app.py` and ran on port 9999.
"""
import sys
if sys.platform == "win32":
    import selectors
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from create_app import create_app

app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
