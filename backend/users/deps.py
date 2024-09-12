from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from users.security import SecurityGateway
from users.security.bcrypt import BcryptSecurityGateway
from core.deps import get_session
from .repository import UsersRepository, ProfilesRepository


async def get_security() -> SecurityGateway:
    return BcryptSecurityGateway()


async def get_users_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
    security_gateway: Annotated[SecurityGateway, Depends(get_security)],
) -> UsersRepository:
    return UsersRepository(session, security_gateway=security_gateway)


async def get_profiles_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ProfilesRepository:
    return ProfilesRepository(session)
