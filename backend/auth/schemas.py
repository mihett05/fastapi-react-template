from pydantic import EmailStr

from core.pydantic import PydanticModel
from users.schemas import UserRead


class UserWithToken(PydanticModel):
    access_token: str
    user: UserRead


class UserAuthenticate(PydanticModel):
    email: EmailStr
    password: str
