from fastapi import APIRouter
from .user import user_route

api_routes = APIRouter(prefix="/v1")
api_routes.include_router(user_route,tags=["Users"])