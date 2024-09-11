from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.sqlalchemy import Base

from datetime import datetime


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    contract_id: Mapped[int] = mapped_column(unique=True)
    messages: Mapped[list["Message"]] = relationship('Message', cascade='all, delete-orphan')


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    message_text: Mapped[str]
    user_from_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user_to_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime]
