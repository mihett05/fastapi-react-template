from core.pydantic import PydanticModel


class UserRead(PydanticModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool


class UserWithToken(PydanticModel):
    access_token: str
    user: UserRead


class UserCreate(PydanticModel):
    email: str
    password: str


class UserUpdate(PydanticModel):
    email: str
    password: str


class UserAuthenticate(PydanticModel):
    email: str
    password: str