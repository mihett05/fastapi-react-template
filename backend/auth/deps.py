from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import get_config
from core.deps import get_session

from .repository import UsersRepository
from .security.bcrypt import BcryptSecurityGateway, SecurityGateway
from .tokens.jwt import JwtTokensGateway, TokenConfig, TokensGateway


async def get_tokens() -> TokensGateway:
    return JwtTokensGateway(TokenConfig(secret_key=get_config().secret))


async def get_security() -> SecurityGateway:
    return BcryptSecurityGateway()


async def get_users_repository(
    session: Annotated[AsyncSession, Depends(get_session)],
    security_gateway: Annotated[SecurityGateway, Depends(get_security)],
) -> UsersRepository:
    return UsersRepository(session, security_gateway=security_gateway)
