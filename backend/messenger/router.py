from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from messenger.deps import get_chats_repository
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatRead, ChatUpdate
from messenger.usecases import (
    get_chat,
    create_chat,
    get_chats,
    update_chat_attrs,
    update_chat_members,
    delete_chat,
)
from users.deps import get_users_repository
from users.models import User
from users.repository import UsersRepository
from users.usecases import get_users

router = APIRouter()


@router.get("/chat", response_model=list[ChatRead])
async def get_chats_handler(
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await get_chats(user, repository=chats_repository)


@router.post("/chat", response_model=ChatRead)
async def create_chat_handler(
    dto: ChatCreate,
    user: Annotated[User, Depends(get_current_user)],  # noqa
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await create_chat(
        dto, repository=chats_repository, users_repository=users_repository
    )


@router.get("/chat/{chat_id}", response_model=ChatRead)
async def get_chat_handler(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await get_chat(chat_id, user, repository=chats_repository)


@router.patch("/chat/{chat_id}/attrs", response_model=ChatRead)
async def update_chat_handler(
    chat_id: int,
    dto: ChatUpdate,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(chat_id, user, repository=chats_repository)
    return await update_chat_attrs(chat, dto, repository=chats_repository)


@router.patch("/chat/{chat_id}/members", response_model=ChatRead)
async def update_chat_handler(
    chat_id: int,
    dto: ChatUpdate,
    user: Annotated[User, Depends(get_current_user)],
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(chat_id, user, repository=chats_repository)
    include = await get_users(dto.include, repository=users_repository)
    exclude = await get_users(dto.exclude, repository=users_repository)

    return await update_chat_members(
        chat, include, exclude, repository=chats_repository
    )


@router.delete("/chat/{chat_id}", response_model=ChatRead)
async def delete_chat_handler(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await delete_chat(chat_id, user, repository=chats_repository)
