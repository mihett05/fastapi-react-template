from core.exceptions import EntityNotFound

from .models import User, Message, Chat


class InvalidCredentials(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid credentials were provided")


class UserNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(User)


class MessageNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(Message)


class ChatNotFound(EntityNotFound):

    def __init__(self):
        super().__init__(Chat)