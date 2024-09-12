from typing import Annotated

from fastapi import Depends, Cookie
from fastapi.security import (
    OAuth2PasswordBearer,
    APIKeyCookie,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from auth import consts
from auth.tokens.dtos import TokenInfo
from auth.tokens.gateway import TokensGateway
from config import get_config

from users.deps import get_users_repository
from users.models import User
from users.repository import UsersRepository
from auth.tokens.jwt import JwtTokensGateway, TokenConfig
from auth.usecases import authorize_user

cookie_scheme = APIKeyCookie(name=consts.REFRESH_COOKIE)
oauth2_scheme = OAuth2PasswordBearer("/auth/token")
http_scheme = HTTPBearer()


async def get_tokens() -> TokensGateway:
    return JwtTokensGateway(TokenConfig(secret_key=get_config().secret))


async def extract_access_token(
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_scheme)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(token.credentials)


async def extract_refresh_token(
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
    cookie: Annotated[str | None, Cookie(alias=consts.REFRESH_COOKIE)],
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(cookie)


async def get_current_user(
    token: Annotated[TokenInfo, Depends(extract_access_token)],
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
) -> User:
    return await authorize_user(token, users_repository=users_repository)
