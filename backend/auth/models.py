from fastapi_users import schemas


class UserCreate(schemas.BaseUserCreate):
    """pydantic model for create user"""
    pass


class UserUpdate(schemas.BaseUserUpdate):
    """pydantic model for update user profile *"""
    pass
