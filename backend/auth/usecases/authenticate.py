from auth.exceptions import InvalidCredentials, UserNotFound
from auth.models import User
from auth.repository import UsersRepository
from auth.schemas import UserAuthenticate
from auth.security import SecurityGateway
from auth.security.dtos import PasswordDto
from auth.tokens.dtos import TokenInfo


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


async def authenticate_user_by_access_token(
        dto: TokenInfo,
        *,
        users_repository: UsersRepository,
) -> User:
    try:
        return await users_repository.get_by_email(dto.subject)
    except UserNotFound:
        raise InvalidCredentials()
