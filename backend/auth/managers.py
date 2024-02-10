from typing import Optional, AsyncGenerator

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users.db import BeanieUserDatabase, ObjectIDIDMixin

from auth.schemas import User, get_user_db
from config import get_config


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = get_config().secret
    verification_token_secret = get_config().secret

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)) -> UserManager:
    yield UserManager(user_db)
