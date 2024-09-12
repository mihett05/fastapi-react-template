from auth.exceptions import InvalidCredentials
from users.models import User
from auth.schemas import UserAuthenticate
from auth.tokens.dtos import TokenInfo
from users.exceptions import UserNotFound
from users.repository import UsersRepository
from users.security import SecurityGateway
from users.security.dtos import PasswordDto


async def authenticate_user(
    dto: UserAuthenticate,
    *,
    users_repository: UsersRepository,
    security_gateway: SecurityGateway,
) -> User:
    try:
        user = await users_repository.get_by_email(dto.email)
        is_password_valid = security_gateway.verify_passwords(
            dto.password, PasswordDto(hashed_password=user.hashed_password, salt=user.salt)
        )
        if not is_password_valid:
            raise InvalidCredentials()
        return user
    except UserNotFound:
        raise InvalidCredentials()


async def authorize_user(
    dto: TokenInfo,
    *,
    users_repository: UsersRepository,
) -> User:
    try:
        return await users_repository.get_by_email(dto.subject)
    except UserNotFound:
        raise InvalidCredentials()
