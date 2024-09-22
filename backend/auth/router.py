from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import consts
from auth.deps import get_tokens, extract_refresh_token
from auth.schemas import UserWithToken, UserAuthenticate
from auth.tokens import TokensGateway
from auth.tokens.dtos import TokenInfo, TokenPairDto
from auth.usecases import (
    authenticate_user,
    authorize_user,
    create_token_pair,
    create_user,
)

from users.deps import get_security, get_users_repository
from users.mappers import user_mapper
from users.models import User
from users.repository import UsersRepository
from users.schemas import UserCreate
from users.security import SecurityGateway

router = APIRouter()


def get_auth_response(user: User, tokens: TokenPairDto) -> JSONResponse:
    response = JSONResponse(
        content=UserWithToken(
            user=user_mapper(user), access_token=tokens.access_token
        ).model_dump(by_alias=True),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens.refresh_token)
    return response


@router.post("/login", response_model=UserWithToken)
async def login_user_handler(
    dto: UserAuthenticate,
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    security_gateway: Annotated[SecurityGateway, Depends(get_security)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
):
    user = await authenticate_user(
        dto,
        repository=users_repository,
        gateway=security_gateway,
    )
    tokens_pair = await create_token_pair(user, gateway=tokens_gateway)

    return get_auth_response(user, tokens_pair)


@router.post("/register", response_model=UserWithToken)
async def register_user_handler(
    dto: UserCreate,
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
):
    user = await create_user(dto, repository=users_repository)
    tokens_pair = await create_token_pair(user, gateway=tokens_gateway)

    return get_auth_response(user, tokens_pair)


@router.post("/refresh", response_model=UserWithToken)
async def refresh_token_handler(
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
    token_info: Annotated[TokenInfo, Depends(extract_refresh_token)],
):
    user = await authorize_user(token_info, repository=users_repository)
    tokens_pair = await create_token_pair(user, gateway=tokens_gateway)

    return get_auth_response(user, tokens_pair)
