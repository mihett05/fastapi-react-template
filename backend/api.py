from fastapi import APIRouter

from auth.router import router as auth_router
from users.router import router as users_router

api = APIRouter()
api.include_router(auth_router, prefix="/auth", tags=["auth"])
api.include_router(users_router, prefix="/users", tags=["users"])

# Далее также подключать и добавлять роутеры из других приложений
