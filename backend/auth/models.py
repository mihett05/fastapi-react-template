from typing import Optional

from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class RegistrationForm(BaseModel):
    email: str
    username: str
    password: str

    last_name: Optional[str]
    first_name: Optional[str]

