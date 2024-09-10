from auth.models import User
from auth.schemas import UserRead
from core.mappers import sqlalchemy_retort

users_mapper = sqlalchemy_retort.extend(recipe=[])

user_mapper = users_mapper.get_converter(User, UserRead)
