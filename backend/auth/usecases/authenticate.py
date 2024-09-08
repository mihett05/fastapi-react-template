from auth.exceptions import InvalidCredentials, UserNotFound
from auth.models import User
from auth.repository import UsersRepository
from auth.security import SecurityGateway
from auth.security.dtos import PasswordDto


async def authenticate_user(
    email: str,
    password: str,
    *,
    users_repository: UsersRepository,
    security_gateway: SecurityGateway,
) -> User:
    try:
        user = await users_repository.get_by_email(email)
        is_password_valid = security_gateway.verify_passwords(
            password, PasswordDto(hashed_password=user.hashed_password, salt=user.salt)
        )
        if not is_password_valid:
            raise InvalidCredentials()
        return user
    except UserNotFound:
        raise InvalidCredentials()
