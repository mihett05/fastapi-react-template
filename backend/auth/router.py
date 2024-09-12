from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import consts
from auth.deps import get_tokens, extract_refresh_token
from auth.schemas import UserWithToken, UserAuthenticate
from auth.tokens import TokensGateway
from auth.tokens.dtos import TokenInfo
from auth.usecases import authenticate_user, authorize_user, create_token_pair
from users.deps import get_security, get_users_repository
from users.mappers import user_mapper
from users.repository import UsersRepository
from users.schemas import UserCreate
from users.security import SecurityGateway

router = APIRouter()


@router.post("/login", response_model=UserWithToken)
async def login_user(
    auth_data: UserAuthenticate,
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    security_gateway: Annotated[SecurityGateway, Depends(get_security)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
):
    user = await authenticate_user(
        auth_data,
        users_repository=users_repository,
        security_gateway=security_gateway,
    )

    tokens_pair = await create_token_pair(user, tokens_gateway=tokens_gateway)

    response = JSONResponse(
        content=UserWithToken(
            user=user_mapper(user), access_token=tokens_pair.access_token
        ).model_dump(by_alias=True),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens_pair.refresh_token)
    return response


@router.post("/register", response_model=UserWithToken)
async def register_user(
    dto: UserCreate,
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
):
    # TODO вынести в usecases
    user = await users_repository.add(dto)
    tokens_pair = await create_token_pair(user, tokens_gateway=tokens_gateway)

    response = JSONResponse(
        content=UserWithToken(
            user=user_mapper(user), access_token=tokens_pair.access_token
        ).model_dump(by_alias=True),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens_pair.refresh_token)
    return response


@router.post("/refresh", response_model=UserWithToken)
async def refresh_token(
    users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
    tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
    token_info: Annotated[TokenInfo, Depends(extract_refresh_token)],
):
    user = await authorize_user(
        token_info,
        users_repository=users_repository,
    )
    tokens_pair = await create_token_pair(user, tokens_gateway=tokens_gateway)

    response = JSONResponse(
        content=UserWithToken(
            user=user_mapper(user), access_token=tokens_pair.access_token
        ).model_dump(by_alias=True),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens_pair.refresh_token)
    return response
