from fastapi import APIRouter

from .chats import router as chat_router
from .messages import router as mess_router

router = APIRouter()

router.include_router(chat_router, prefix="/chat", tags=["chats"])
router.include_router(mess_router, prefix="/mess", tags=["messages"])
