from core.mappers import sqlalchemy_retort
from messenger.models import Message
from messenger.schemas import MessageRead

retort = sqlalchemy_retort.extend(recipe=[])

message_mapper = retort.get_converter(Message, MessageRead)
