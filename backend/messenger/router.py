from typing import Annotated

from fastapi import APIRouter, Depends

from messenger.deps import get_chats_repository
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatRead

router = APIRouter()


@router.get("/chat/{chat_id}", response_model=ChatRead)
async def get_chat(
    chat_id: int,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    pass


@router.post("/chat", response_model=ChatRead)
async def create_chat(
    dto: ChatCreate,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    pass


@router.delete("/chat/{chat_id}", response_model=ChatRead)
async def delete_chat(
    chat_id: int,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    pass


@router.put("/chat/{chat_id}", response_model="str")
async def update_chat():
    pass
