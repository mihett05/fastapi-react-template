from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from auth import consts
from auth.deps import get_security, get_tokens, get_users_repository, extract_access_token, extract_refresh_token
from auth.mappers import user_mapper
from auth.repository import UsersRepository
from auth.schemas import UserAuthenticate, UserCreate, UserRead, UserWithToken
from auth.security import SecurityGateway
from auth.tokens import TokensGateway
from auth.tokens.dtos import TokenInfo
from auth.usecases import authenticate_user, authorize_user, create_token_pair

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_user(
        users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
        token_info: TokenInfo = Depends(extract_access_token),
):
    user = await authorize_user(
        token_info,
        users_repository=users_repository,
    )
    return JSONResponse(content=user_mapper(user).model_dump())


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
            user=user_mapper(user),
            access_token=tokens_pair.access_token
        ).model_dump(),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens_pair.refresh_token)
    return response


@router.post("/register", response_model=UserWithToken)
async def register_user(register_data: UserCreate):
    pass


@router.post("/refresh", response_model=str)
async def refresh_token(
        users_repository: Annotated[UsersRepository, Depends(get_users_repository)],
        tokens_gateway: Annotated[TokensGateway, Depends(get_tokens)],
        token_info: TokenInfo = Depends(extract_refresh_token)):
    user = await authenticate_user_by_access_token(
        token_info,
        users_repository=users_repository,
    )
    tokens_pair = await create_token_pair(user, tokens_gateway=tokens_gateway)

    response = JSONResponse(
        content=UserWithToken(
            user=user_mapper(user),
            access_token=tokens_pair.access_token
        ).model_dump(),
    )
    response.set_cookie(consts.REFRESH_COOKIE, tokens_pair.refresh_token)
    return response
