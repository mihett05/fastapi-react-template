import uuid

from beanie import PydanticObjectId
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: PydanticObjectId


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass

