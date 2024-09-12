from typing import Optional

from messenger.models import Message, Chat
from messenger.schemas import MessageRead, ChatRead
from core.mappers import sqlalchemy_retort

from adaptix.conversion import coercer

retort = sqlalchemy_retort.extend(recipe=[])

message_mapper = retort.get_converter(Message, MessageRead)

chat_mapper = retort.get_converter(
    Chat, ChatRead, recipe=[coercer(Message, MessageRead, message_mapper)]
)
chat_mapper_nullable = retort.get_converter(
    Optional[Chat],
    Optional[ChatRead],
    recipe=[coercer(Message, MessageRead, message_mapper)],
)
