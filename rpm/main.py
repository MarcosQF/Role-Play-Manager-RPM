from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

from .core.errors import ApiException
from .core.main_router import api_router

app = FastAPI()
app.include_router(api_router)


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "error_code": exc.headers.get("X-Error-Code", "UNKNOWN_ERROR"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
