from typing import Optional

from pydantic import EmailStr

from core.pydantic import PydanticModel


class ProfileCreate(PydanticModel):
    org_name: str
    contact_phone: str
    ceo_fullname: str
    inn: str
    kpp: str
    ogrn: str


class ProfileRead(PydanticModel):
    user_id: int
    org_name: str
    contact_phone: str
    ceo_fullname: str
    inn: str
    kpp: str
    ogrn: str


class ProfileUpdate(PydanticModel):
    org_name: Optional[str] = None
    contact_phone: Optional[str] = None
    ceo_fullname: Optional[str] = None
    inn: Optional[str] = None
    kpp: Optional[str] = None
    ogrn: Optional[str] = None


class ProfileDelete(PydanticModel):
    user_id: int


class UserRead(PydanticModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool

    profile: Optional[ProfileCreate]


class UserCreate(PydanticModel):
    email: EmailStr
    password: str


class UserUpdate(PydanticModel):
    email: EmailStr
    password: str
