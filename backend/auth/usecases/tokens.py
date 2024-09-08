from typing import Annotated

from fastapi import Depends

from auth import consts
from auth.models import User
from auth.tokens.dtos import TokenPairDto, TokenInfo
from auth.tokens.gateway import TokensGateway
from fastapi.security import OAuth2PasswordBearer, APIKeyCookie

cookie_scheme = APIKeyCookie(name=consts.REFRESH_COOKIE)
oauth2_scheme = OAuth2PasswordBearer("/auth/token")


async def create_token_pair(
        user: User, *, tokens_gateway: TokensGateway
) -> TokenPairDto:
    return await tokens_gateway.create_token_pair(user.email)


async def extract_access_token(
        token: Annotated[str, Depends(oauth2_scheme)], *, tokens_gateway: TokensGateway
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(token)


async def extract_refresh_token(
        token: Annotated[str, Depends(oauth2_scheme)], *, tokens_gateway: TokensGateway
) -> TokenInfo:
    return await tokens_gateway.extract_token_info(token)
