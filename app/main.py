import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from pydantic import AnyHttpUrl
from app.api import api_routes
from fastapi.responses import JSONResponse


app = FastAPI(title=settings.PROJECT_NAME,version=settings.VERSION,description=settings.DESCRIPTION)
app.include_router(api_routes)


BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/", include_in_schema=False)
async def health_check() -> JSONResponse:
    return JSONResponse({"message": "service status online"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

