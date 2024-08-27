from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Cookie, HTTPException, status
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication.transport.bearer import BearerResponse

from config import get_config
from .backend import auth_backend
from .deps import get_jwt_strategy, get_jwt_refresh_strategy, get_user_manager
from .manager import UserManager
from .schemas import UserRead, UserCreate, UserUpdate
from .backend import fastapi_users


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# TODO: сделать добавление refresh cookie в response для login
# TODO: сделать logout который удаляет refresh cookie


@router.post("/jwt/refresh", tags=["auth"], response_model=BearerResponse)
async def refresh_token(
    strategy: Annotated[JWTStrategy, Depends(get_jwt_strategy)],
    refresh_strategy: Annotated[JWTStrategy, Depends(get_jwt_refresh_strategy)],
    refresh: Annotated[str | None, Cookie()],
    user_manager: Annotated[UserManager, Depends(get_user_manager)],
):
    if not refresh:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token required"
        )

    user = await refresh_strategy.read_token(refresh, user_manager)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired"
        )

    new_refresh = await refresh_strategy.write_token(user)

    response = await auth_backend.login(strategy, user)
    response.set_cookie(
        "refresh",
        new_refresh,
        httponly=True,
        expires=datetime.utcnow() + get_config().refresh_token_lifetime,
    )

    return response
