from messenger.models import Message, Chat
from messenger.schemas import MessageRead, ChatRead
from core.mappers import sqlalchemy_retort

messages_mapper = sqlalchemy_retort.extend(recipe=[])

message_mapper = messages_mapper.get_converter(Message, MessageRead)

chats_mapper = sqlalchemy_retort.extend(recipe=[])

chat_mapper = messages_mapper.get_converter(Chat, ChatRead)
