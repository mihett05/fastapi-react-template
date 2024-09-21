from auth.exceptions import InvalidCredentials
from users.models import User
from auth.schemas import UserAuthenticate
from auth.tokens.dtos import TokenInfo
from users.exceptions import UserNotFound
from users.repository import UsersRepository
from users.schemas import UserCreate
from users.security import SecurityGateway
from users.security.dtos import PasswordDto


async def authenticate_user_uc(
    dto: UserAuthenticate, *, repo: UsersRepository, gateway: SecurityGateway
) -> User:
    try:
        user = await repo.get_by_email(dto.email)
        is_password_valid = gateway.verify_passwords(
            dto.password,
            PasswordDto(hashed_password=user.hashed_password, salt=user.salt),
        )
        if not is_password_valid:
            raise InvalidCredentials()
        return user
    except UserNotFound:
        raise InvalidCredentials()


async def authorize_user_uc(dto: TokenInfo, *, repo: UsersRepository) -> User:
    try:
        return await repo.get_by_email(dto.subject)
    except UserNotFound:
        raise InvalidCredentials()


async def create_user_uc(dto: UserCreate, *, repo: UsersRepository) -> User:
    return await repo.add(dto)
