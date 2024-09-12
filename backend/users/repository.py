from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from users.models import User, Profile
from users.schemas import UserCreate, ProfileCreate, ProfileUpdate
from .exceptions import UserNotFound, ProfileNotFound
from .security import SecurityGateway


class UsersRepository:
    def __init__(self, session: AsyncSession, security_gateway: SecurityGateway):
        self.session = session
        self.security_gateway = security_gateway

    async def get(self, user_id: int) -> User:
        if user := await self.session.get(
            User, user_id, options=[selectinload(User.profile)]
        ):
            return user
        raise UserNotFound()

    async def get_by_email(self, email: str) -> User:
        query = (
            select(User).where(User.email == email).options(selectinload(User.profile))
        )

        if user := await self.session.scalar(query):
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
            profile=None,
        )
        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, user: User):
        self.session.add(user)
        await self.session.commit()

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.commit()


class ProfilesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    async def get_by_user(user: User) -> Profile:
        if profile := user.profile:
            return profile
        raise ProfileNotFound()

    async def get(self, profile_id: int) -> Profile:
        if profile := await self.session.get(Profile, profile_id):
            return profile
        raise ProfileNotFound()

    async def add(self, dto: ProfileCreate, user: User) -> Profile:
        model = Profile(
            user_id=user.id,
            org_name=dto.org_name,
            contact_phone=dto.contact_phone,
            ceo_fullname=dto.ceo_fullname,
            inn=dto.inn,
            kpp=dto.kpp,
            ogrn=dto.ogrn,
        )

        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, dto: ProfileUpdate, user: User) -> Profile:
        model = user.profile

        attrs = dto.model_dump().keys()
        for attr in attrs:
            setattr(model, attr, getattr(dto, attr) or getattr(model, attr))

        await self.session.commit()
        return model

    async def delete(self, user: User):
        profile = user.profile
        await self.session.delete(user.profile)
        await self.session.commit()

        return profile
