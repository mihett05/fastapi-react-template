from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        secrets_dir=Path(__file__).parent / "secrets",
    )

    secret: str
    mongodb_user: str
    mongodb_password: str


@lru_cache
def get_config() -> Config:
    return Config()
