from typing import Optional

from adaptix.conversion import coercer

from users.models import User, Profile
from auth.schemas import UserRead
from core.mappers import sqlalchemy_retort
from users.schemas import ProfileRead

retort = sqlalchemy_retort.extend(recipe=[])

profile_mapper_default = retort.get_converter(Profile, ProfileRead)
profile_mapper_nullable = retort.get_converter(Optional[Profile], Optional[ProfileRead])

user_mapper = retort.get_converter(
    User,
    UserRead,
    recipe=[
        coercer(Profile, ProfileRead, profile_mapper_default),
        coercer(Optional[Profile], Optional[ProfileRead], profile_mapper_nullable),
    ]
)
