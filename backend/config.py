from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_PATH = Path(__file__).parent
PROJECT_PATH = Path(__file__).parent.parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_PATH / ".env",
        secrets_dir=BACKEND_PATH / "secrets",
    )

    secret: str
    mongodb_user: str
    mongodb_password: str


@lru_cache
def get_config() -> Config:
    return Config()
