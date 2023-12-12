from fastapi import APIRouter

from auth.schemas import User
from auth.models import LoginForm


router = APIRouter()


@router.get(
    "/",
    response_class=list[User],
    response_description="Возвращает всех пользователей",
)
async def get_users():
    return await User.find_all().to_list()


@router.get("/")
async def login_user(body: LoginForm):
    user = await User.find_one(
        User.username == body.username, User.hashed_password == body.password
    )


# https://fastapi-users.github.io/ - готовая либа
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ - сам jwt аутентификацию пишешь
