from typing import Annotated, AsyncGenerator

from fastapi import Depends
from fastapi_users.authentication import JWTStrategy

from fastapi_users.db import SQLAlchemyUserDatabase


from sqlalchemy.ext.asyncio import AsyncSession

from config import get_config
from core.deps import get_session
from .manager import UserManager

from .models import User


async def get_user_db(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(
    user_db: Annotated[SQLAlchemyUserDatabase, Depends(get_user_db)],
) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=get_config().secret,
        lifetime_seconds=int(get_config().access_token_lifetime.total_seconds()),
    )


def get_jwt_refresh_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=get_config().secret,
        lifetime_seconds=int(get_config().refresh_token_lifetime.total_seconds()),
    )
