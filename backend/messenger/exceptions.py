from core.exceptions import EntityNotFound

from .models import Message, Chat


class MessageNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(Message)


class ChatNotFound(EntityNotFound):

    def __init__(self):
        super().__init__(Chat)