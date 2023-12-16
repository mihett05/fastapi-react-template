from fastapi_users import schemas
from pydantic import BaseModel


class SignUpForm(schemas.BaseUserCreate):
    """pydantic model for create user"""
    pass


class SignInForm(BaseModel):
    """pydantic model for update user profile *"""
    username: str
    password: str
