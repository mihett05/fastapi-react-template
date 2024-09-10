from sqlalchemy.orm import Mapped, mapped_column

from core.sqlalchemy import Base

from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    salt: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(foreign_key=True)
    message_text: Mapped[str]
    user_from_id: Mapped[int] = mapped_column(foreign_key=True)
    user_to_id: Mapped[int] = mapped_column(foreign_key=True)
    created_at: Mapped[datetime]


class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    contract_id: Mapped[int] = mapped_column(unique=True)