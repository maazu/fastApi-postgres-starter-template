import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from app.core.config import settings
from pydantic import AnyHttpUrl
from app.api import api_router
from app.db.base import Base
from app.db.session import engine
app = FastAPI(title=settings.PROJECT_NAME,version=settings.VERSION,description=settings.DESCRIPTION)

Base.metadata.create_all(bind=engine)
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
 
#["http://localhost", "http://localhost:4200"]'
BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []


if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

