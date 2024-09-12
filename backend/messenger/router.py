from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth.deps import get_current_user
from messenger.deps import get_chats_repository
from messenger.mappers import chat_mapper
from messenger.models import Chat
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatRead

router = APIRouter()


@router.get("/chat/{chat_id}", response_model=ChatRead)
async def get_chat(
    chat_id: int,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return chat_mapper(await chats_repository.get(chat_id))


@router.post("/chat", response_model=ChatRead)
async def create_chat(
    dto: ChatCreate,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await chats_repository.add(dto)
    return chat_mapper(chat)


@router.delete("/chat/{chat_id}", response_model=ChatRead)
async def delete_chat(
    chat_id: int,
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await chats_repository.get(chat_id)
    await chats_repository.delete(chat)
    return chat_mapper(chat)


@router.put("/chat/{chat_id}", response_model="str")
async def update_chat():
    pass
