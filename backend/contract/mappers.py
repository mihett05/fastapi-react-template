from adaptix.conversion import coercer

from contract.models import Contract
from contract.schemas import ContractRead
from core.mappers import sqlalchemy_retort
from messenger.mappers import chat_mapper
from messenger.models import Chat
from messenger.schemas import ChatRead
from users.mappers import user_mapper
from users.models import User
from users.schemas import UserRead

retort = sqlalchemy_retort.extend(recipe=[])

contract_mapper = retort.get_converter(Contract, ContractRead, recipe=[coercer(Chat, ChatRead, chat_mapper),
                                                                       coercer(User, UserRead, user_mapper)])


