from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())