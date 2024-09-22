from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from messenger.deps import get_chats_repository
from messenger.repository import ChatsRepository
from messenger.schemas import ChatCreate, ChatRead, ChatUpdate, ChatDelete
from messenger.usecases.chats import (
    get_chat_uc,
    create_chat_uc,
    get_chats_uc,
    update_chat_uc,
    delete_chat_uc,
)
from users.deps import get_users_repository
from users.models import User
from users.repository import UsersRepository

router = APIRouter()


@router.get("/chat", response_model=list[ChatRead])
async def get_chats(
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await get_chats_uc(user, repo=chats_repository)


@router.post("/chat", response_model=ChatRead)
async def create_chat(
    dto: ChatCreate,
    user: Annotated[User, Depends(get_current_user)],  # noqa
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await create_chat_uc(dto, repo=chats_repository, users_repo=users_repository)


@router.get("/chat/{chat_id}", response_model=ChatRead)
async def get_chat(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await get_chat_uc(chat_id, user, repo=chats_repository)


@router.patch("/chat/{chat_id}", response_model=ChatRead)
async def update_chat(
    chat_id: int,
    dto: ChatUpdate,
    user: Annotated[User, Depends(get_current_user)],
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await update_chat_uc(
        chat_id, dto, user, repo=chats_repository, users_repo=users_repository
    )


@router.delete("/chat/{chat_id}", response_model=ChatRead)
async def delete_chat(
    chat_id: int,
    user: Annotated[User, Depends(get_current_user)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    return await delete_chat_uc(chat_id, user, repo=chats_repository)
