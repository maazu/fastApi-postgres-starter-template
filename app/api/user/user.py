from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import DuplicatedEntryError
from app.db.session import get_session
from sqlalchemy.exc import IntegrityError
from app.models.user import User 
from app.schema.user import User as UserSchema, UserInDBBase

user_route = APIRouter()

async def get_users(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    return result.scalars().all()


@user_route.get("/users/", response_model=list[UserInDBBase])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await get_users(session)
    return [UserInDBBase(id=user.id,name=user.name, email=user.email) for user in users]


def add_user(session: AsyncSession, name: str, email: str):
    new_user = User(name=name, email=email)
    session.add(new_user)
    return new_user


@user_route.post("/users/")
async def new_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    user = add_user(session, user.name, user.email)
    try:
        await session.commit()
        return user
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("User already exist")
    
