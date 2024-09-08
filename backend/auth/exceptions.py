from core.exceptions import EntityNotFound

from .models import User


class InvalidCredentials(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid credentials were provided")


class UserNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(User)
