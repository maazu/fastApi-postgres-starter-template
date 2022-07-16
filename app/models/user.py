from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from app.models.base import Base


class User(Base):
    
    __tablename__ = "users"
    id: int = Column(
        "id", Integer(), autoincrement=True, nullable=False, unique=True, primary_key=True
    )
    name:str = Column("name", String(length=256), nullable=False)
    email:str =  Column("email", String(length=64), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())