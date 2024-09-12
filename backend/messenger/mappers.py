from messenger.models import Message, Chat
from messenger.schemas import MessageRead, ChatRead
from core.mappers import sqlalchemy_retort

retort = sqlalchemy_retort.extend(recipe=[])

message_mapper = retort.get_converter(Message, MessageRead)

chat_mapper = retort.get_converter(Chat, ChatRead)
