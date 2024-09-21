from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from messenger.models import Message, Chat
from messenger.schemas import MessageCreate, ChatCreate
from .exceptions import MessageNotFound, ChatNotFound

import time

from datetime import datetime


class MessagesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, message_id: int) -> Message:
        if message := await self.session.get(Message, message_id):
            return message  # type: ignore
        raise MessageNotFound()

    async def get_by_chat(self, chat_id: int) -> list[Message]:
        if messages := await self.session.scalars(
            select(Message).where(Message.chat_id == chat_id)  # type: ignore
        ):
            return messages  # type: ignore
        raise MessageNotFound()

    async def get_by_user(self, user_id: int) -> list[Message]:
        if messages := await self.session.scalars(
            select(Message).where(
                or_(
                    Message.receiver_id == user_id,  # type: ignore
                    Message.sender_id == user_id,
                )
            )
        ):
            return messages  # type: ignore
        raise MessageNotFound()

    async def add(self, message: MessageCreate) -> Message:
        model = Message(
            chat_id=message.chat_id,
            sender_id=message.sender_id,
            message_text=message.message_text,
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def delete(self, message: Message):
        await self.session.delete(message)
        await self.session.commit()


class ChatsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, chat_id: int) -> Chat:
        if chat := await self.session.get(
            Chat, chat_id, options=[selectinload(Chat.messages), selectinload()]
        ):
            return chat  # type: ignore
        raise ChatNotFound()

    async def add(self, dto: ChatCreate) -> Chat:
        model = Chat(name=dto.name, messages=[], members=dto.members)

        self.session.add(model)
        await self.session.commit()

        return model

    async def delete(self, chat: Chat):
        await self.session.delete(chat)
        await self.session.commit()
