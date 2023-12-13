from fastapi import APIRouter

from auth.models import LoginForm
from users.schemas import User

router = APIRouter()


@router.post("/login")
async def login_user(body: LoginForm):
    user = await User.find_one(
        User.username == body.username, User.hashed_password == body.password
    )

# https://fastapi-users.github.io/ - готовая либа
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ - сам jwt аутентификацию пишешь
