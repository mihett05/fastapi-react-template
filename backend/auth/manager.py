from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from config import get_config
from .models import User


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = get_config().secret
    verification_token_secret = get_config().secret

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
