"""Startup wrapper — sets Windows event loop policy BEFORE any asyncio code runs."""
import sys

if sys.platform == "win32":
    import selectors
    import asyncio
    # Must be called BEFORE asyncio.run() or uvicorn creates its loop
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # Also set the default policy for any subprocess/spawned processes
    import os
    os.environ["PYTHONASYNCIODEBUG"] = "0"

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7777,
        log_level="info",
        loop="asyncio",  # Force asyncio loop (not uvloop)
    )
