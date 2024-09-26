from fastapi import APIRouter

from ws.router import router as ws_router
from auth.router import router as auth_router
from users.router import router as users_router
from messenger.router import router as messenger_router

api = APIRouter()
api.include_router(ws_router, prefix="/ws", tags=["ws"])
api.include_router(auth_router, prefix="/auth", tags=["auth"])
api.include_router(users_router, prefix="/users", tags=["users"])
api.include_router(messenger_router, prefix="/messenger")
