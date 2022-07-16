import logging
from typing import AsyncIterator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import scoped_session

from app.core.config import settings

logger = logging.getLogger(__name__)

async_engine = create_async_engine(
    settings.DB_URI,
    pool_pre_ping=True,
    echo=settings.ECHO_SQL,
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, autoflush=False, expire_on_commit=False,  class_=AsyncSession
)
Session = scoped_session(AsyncSessionLocal)

async def get_session():
    try:
        yield Session
    except SQLAlchemyError as e:
        logger.exception(e)