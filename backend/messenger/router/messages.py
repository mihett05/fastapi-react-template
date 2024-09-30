from typing import Annotated

from fastapi import APIRouter, Depends

from auth.deps import get_current_user
from messenger.deps import get_chats_repository, get_messages_repository
from messenger.models import Message, Chat
from messenger.repository import ChatsRepository, MessagesRepository
from messenger.schemas import (
    MessageRead,
    MessageCreate,
    MessageUpdate,
)
from messenger.usecases import get_chat
from messenger.usecases.messages import (
    create_message,
    get_message,
    update_message,
    delete_message,
    send_message_notifications,
)
from users.models import User
from ws.schemas import EventTypeResponse
from ws.usecases.updates import get_message_ws, get_response

router = APIRouter()


async def send_mess_update_ws(
    chat: Chat, user: User, message: Message, *, event: EventTypeResponse
):
    message_ws = await get_message_ws(message)
    response_ws = await get_response(message_ws, event)

    await send_message_notifications(chat, user, response=response_ws)


@router.post("/", response_model=MessageRead)
async def create_message_handler(
    dto: MessageCreate,
    user: Annotated[User, Depends(get_current_user)],
    mess_repository: Annotated[MessagesRepository, Depends(get_messages_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(dto.chat_id, user, repository=chats_repository)
    message = await create_message(dto, user, repository=mess_repository)

    await send_mess_update_ws(chat, user, message, event=EventTypeResponse.NEW_MESSAGE)

    return message


@router.get("/{chat_id}/{message_id}", response_model=MessageRead)
async def get_message_handler(
    chat_id: int,
    message_id: int,
    user: Annotated[User, Depends(get_current_user)],
    mess_repository: Annotated[MessagesRepository, Depends(get_messages_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(chat_id, user, repository=chats_repository)
    return await get_message(message_id, chat.id, repository=mess_repository)


@router.patch("/{chat_id}/{message_id}", response_model=MessageRead)
async def update_message_handler(
    chat_id: int,
    message_id: int,
    dto: MessageUpdate,
    user: Annotated[User, Depends(get_current_user)],
    mess_repository: Annotated[MessagesRepository, Depends(get_messages_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(chat_id, user, repository=chats_repository)
    message = await get_message(message_id, chat.id, repository=mess_repository)

    await send_mess_update_ws(
        chat, user, message, event=EventTypeResponse.UPDATED_MESSAGE
    )

    return await update_message(message, dto, user, repository=mess_repository)


@router.delete("/{chat_id}/{message_id}", response_model=MessageRead)
async def delete_message_handler(
    chat_id: int,
    message_id: int,
    user: Annotated[User, Depends(get_current_user)],
    mess_repository: Annotated[MessagesRepository, Depends(get_messages_repository)],
    chats_repository: Annotated[ChatsRepository, Depends(get_chats_repository)],
):
    chat = await get_chat(chat_id, user, repository=chats_repository)
    mess = await get_message(message_id, chat.id, repository=mess_repository)

    message = await delete_message(mess, user, repository=mess_repository)
    await send_mess_update_ws(
        chat, user, message, event=EventTypeResponse.DELETED_MESSAGE
    )

    return message
