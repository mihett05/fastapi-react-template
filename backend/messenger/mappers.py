from messenger.models import Message, Chat
from messenger.schemas import MessageRead, ChatRead
from core.mappers import sqlalchemy_retort

retort = sqlalchemy_retort.extend(recipe=[])

messages_mapper = retort

message_mapper = retort.get_converter(Message, MessageRead)

chats_mapper = retort

chat_mapper = retort.get_converter(Chat, ChatRead)
