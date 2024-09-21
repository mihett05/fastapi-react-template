from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from messenger.deps import get_chats_repository
from messenger.mappers import chat_mapper
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatRead
from messenger.usecases.chats import get_chat_uc, create_chat_uc, get_chats_uc
from users.models import User

router = APIRouter()


@router.get("/chat", response_model=ChatRead)
async def get_chats(
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chats_uc(user, repo=chats_repository)
    return chat_mapper(chat)


@router.post("/chat", response_model=ChatRead)
async def create_chat(
    dto: ChatCreate,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await create_chat_uc(dto, repo=chats_repository)
    return chat_mapper(chat)


@router.get("/chat/{chat_id}", response_model=ChatRead)
async def get_chat(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat_uc(chat_id, user, repo=chats_repository)
    return chat_mapper(chat)


@router.patch("/chat/{chat_id}", response_model=ChatRead)
async def update_chat(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    pass


@router.delete("/chat/{chat_id}", response_model=ChatRead)
async def delete_chat(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    pass
