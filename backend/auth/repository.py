from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.schemas import UserCreate

from .exceptions import UserNotFound
from .security import SecurityGateway


class UsersRepository:
    def __init__(self, session: AsyncSession, security_gateway: SecurityGateway):
        self.session = session
        self.security_gateway = security_gateway

    async def get(self, user_id: int) -> User:
        if user := await self.session.get(User, user_id):
            return user
        raise UserNotFound()

    async def get_by_email(self, email: str) -> User:
        if user := await self.session.scalar(select(User).where(User.email == email)):
            return user
        raise UserNotFound()

    async def add(self, user_create: UserCreate) -> User:
        password_with_salt = self.security_gateway.create_hashed_password(
            user_create.password
        )
        model = User(
            email=user_create.email,
            hashed_password=password_with_salt.hashed_password,
            salt=password_with_salt.salt,
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, user: User):
        self.session.add(user)
        await self.session.commit()
        # TODO: мб рефреш ещё сделать?

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.commit()
