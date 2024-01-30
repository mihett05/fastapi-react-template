from beanie import PydanticObjectId
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from auth.schemas import User
from auth.managers import get_user_manager
from config import get_config


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=get_config().secret, lifetime_seconds=3600)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
auth_backend = AuthenticationBackend(name="jwt", transport=bearer_transport, get_strategy=get_jwt_strategy)
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)
