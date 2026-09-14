"""FastAPI application entry point.

Uses create_app() factory from create_app.py with Windows event loop policy.
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
