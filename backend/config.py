from functools import lru_cache
from pathlib import Path
from datetime import timedelta

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_PATH = Path(__file__).parent
PROJECT_PATH = Path(__file__).parent.parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_PATH / ".env",
    )

    secret: str
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str

    access_token_lifetime: timedelta = timedelta(hours=1)
    refresh_token_lifetime: timedelta = timedelta(days=7)

    @computed_field
    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


@lru_cache
def get_config() -> Config:
    return Config()
