from typing import Set

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.sqlalchemy import Base

from datetime import datetime

from users.models import User


class Association(Base):
    __tablename__ = "chat_to_user"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), primary_key=True)


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    message_text: Mapped[str]
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    members: Mapped[Set[User]] = relationship(
        secondary=Association.__table__, collection_class=set
    )
    messages: Mapped[list[Message]] = relationship(cascade="all, delete-orphan")
