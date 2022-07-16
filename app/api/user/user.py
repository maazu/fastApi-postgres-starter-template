from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session

from app.models.user import User 
from app.schema.user import User as UserSchema


user_route = APIRouter()


async def get_users(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    return result.scalars().all()


@user_route.get("/users/", response_model=list[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await get_users(session)
    return [UserSchema(name=user.name, email=user.email) for user in users]




   
    
