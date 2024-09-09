from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyCookie
from sqlalchemy.ext.asyncio import AsyncSession

from auth import consts
from auth.tokens.dtos import TokenInfo
from auth.tokens.gateway import TokensGateway
from config import get_config
from core.deps import get_session
from .models import User
from .repository import UsersRepository
from .security.bcrypt import BcryptSecurityGateway, SecurityGateway
from .tokens.jwt import JwtTokensGateway, TokenConfig
from .usecases import authorize_user

cookie_scheme = APIKeyCookie(name=consts.REFRESH_COOKIE)
oauth2_scheme = OAuth2PasswordBearer("/auth/token")


async def get_tokens() -> TokensGateway:
    return JwtTokensGateway(TokenConfig(secret_key=get_config().secret))


async def get_security() -> SecurityGateway:
    return BcryptSecurityGateway()


async def get_users_repository(
        session: Annotated[AsyncSession, Depends(get_session)],
        security_gateway: Annotated[SecurityGateway, Depends(get_security)],
) -> UsersRepository:
    return UsersRepository(session, security_gateway=security_gateway)


async def extract_access_token(
        token: Annotated[str, Depends(oauth2_scheme)],
        tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(token)


async def extract_refresh_token(
        token: Annotated[str, Depends(oauth2_scheme)],
        tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(token)


async def get_current_user(
        token: Annotated[TokenInfo, Depends(extract_access_token)],
        users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
) -> User:
    return await authorize_user(token, users_repository=users_repository)
