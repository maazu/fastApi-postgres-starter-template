from fastapi import APIRouter
from .user import user_route

v1_routes = APIRouter(prefix="/v1")
v1_routes.include_router(user_route)
