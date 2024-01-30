from fastapi import APIRouter

from auth.router import router as auth_router

api = APIRouter()
api.include_router(auth_router)

# Далее также подключать и добавлять роутеры из других приложений
