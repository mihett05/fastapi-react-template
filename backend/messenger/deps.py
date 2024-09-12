from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from messenger.repository import ChatsRepository


async def get_chats_repository(
        session: Annotated[AsyncSession, Depends(get_session)],
) -> ChatsRepository:
    return ChatsRepository(session)
