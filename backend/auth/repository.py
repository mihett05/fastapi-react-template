from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User, Message, Chat
from auth.schemas import UserCreate

from .exceptions import UserNotFound, MessageNotFound
from .security import SecurityGateway

import time

from datetime import datetime


class UsersRepository:
    def __init__(self, session: AsyncSession, security_gateway: SecurityGateway):
        self.session = session
        self.security_gateway = security_gateway

    async def get(self, user_id: int) -> User:
        if user := await self.session.get(User, user_id):
            return user
        raise UserNotFound()

    async def get_by_email(self, email: str) -> User:
        if user := await self.session.scalar(select(User).where(User.email == email)):
            return user
        raise UserNotFound()

    async def add(self, user_create: UserCreate) -> User:
        password_with_salt = self.security_gateway.create_hashed_password(
            user_create.password
        )
        model = User(
            email=user_create.email,
            hashed_password=password_with_salt.hashed_password,
            salt=password_with_salt.salt,
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, user: User):
        self.session.add(user)
        await self.session.commit()
        # TODO: мб рефреш ещё сделать?

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.commit()


class MessagesRepository:

    def __init__(self, session: AsyncSession, security_gateway: SecurityGateway):
        self.session = session
        self.security_gateway = security_gateway

    async def get(self, message_id: int) -> Message:
        if message := await self.session.get(Message, message_id):
            return message
        raise MessageNotFound()

    async def get_by_chat(self, chat_id: int) -> list[Message]:
        if messages := await self.session.get(select(Message).where(Message.chat_id == chat_id)):
            return messages
        raise MessageNotFound()

    async def get_by_user(self, user_id: int) -> list[Message]:
        if messages := await self.session.get(select(Message).where(Message.user_to_id == user_id or Message.user_to_id == user_id)):
            return messages
        raise MessageNotFound()

    async def add(self, chat_id: int, user_to_id: int, user_from_id: int, message_text: str) -> Message:
        model = Message(
            chat_id=chat_id,
            user_to_id=user_to_id,
            user_from_id=user_from_id,
            message_text=message_text,
            created_at=datetime.fromtimestamp(time.time())
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def delete(self, message: Message):
        await self.session.delete(message)
        await self.session.commit()


class ChatsRepository:

    def __init__(self, session: AsyncSession, security_gateway: SecurityGateway):
        self.session = session
        self.security_gateway = security_gateway

    async def get(self, chat_id: int) -> Chat:
        if chat := await self.session.get(Chat, chat_id):
            return chat
        raise MessageNotFound()

    async def add(self, contract_id: int) -> Chat:
        model = Chat(
            contract_id=contract_id
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def delete(self, chat: Chat):
        await self.session.delete(select(Message).where(Message.chat_id == chat.id))
        await self.session.delete(chat)
        await self.session.commit()
