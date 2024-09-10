from typing import Optional

from pydantic import EmailStr

from core.pydantic import PydanticModel


class UserRead(PydanticModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool

    # profile: Optional['ProfileRead'] = None


class UserCreate(PydanticModel):
    email: EmailStr
    password: str


class UserUpdate(PydanticModel):
    email: EmailStr
    password: str


class ProfileCreate(PydanticModel):
    org_name: str
    contact_phone: str
    ceo_fullname: str
    inn: str
    kpp: str
    ogrn: str


class ProfileRead(PydanticModel):
    id: int
    user_id: int
    org_name: str
    contact_phone: str
    ceo_fullname: str
    inn: str
    kpp: str
    ogrn: str


class ProfileUpdate(PydanticModel):
    id: int
    org_name: Optional[str]
    contact_phone: Optional[str]
    ceo_fullname: Optional[str]
    inn: Optional[str]
    kpp: Optional[str]
    ogrn: Optional[str]


class ProfileDelete(PydanticModel):
    id: int
