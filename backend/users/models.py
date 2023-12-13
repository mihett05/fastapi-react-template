from fastapi_users import schemas
from pydantic import BaseModel


class User(BaseModel):
    """pydantic model for get single/list user profile"""
    email: str
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    """pydantic model for update user profile"""
    pass
