
import email
from fastapi import APIRouter, Depends
from app.models.user import User 
from app.schema.user import User as UserSchema
from fastapi_sqlalchemy import db

user_route = APIRouter()

@user_route.get('/users/')
def get_users():
    users = db.session.query(User).all()
    return users


@user_route.post("/add-user/", response_model=UserSchema)
def add_user(user: UserSchema):
    db_user = User(name=user.name, email=user.email)
    db.session.add(db_user)
    db.session.commit()
    return db_user