from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # --------------------------------------------------
    # PROJECT
    # --------------------------------------------------

    PROJECT_NAME: str = "NOVA"
    VERSION: str = "1.0.0"

    DEBUG: bool = False

    API_PREFIX: str = "/api"

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    JWT_ALGORITHM: str = "HS256"

    # --------------------------------------------------
    # DATABASE
    # --------------------------------------------------

    POSTGRES_HOST: str

    POSTGRES_PORT: int = 5432

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    POSTGRES_DB: str

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    # --------------------------------------------------
    # REDIS
    # --------------------------------------------------

    REDIS_HOST: str

    REDIS_PORT: int = 6379

    REDIS_DB: int = 0

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        return (
            f"redis://"
            f"{self.REDIS_HOST}:"
            f"{self.REDIS_PORT}/"
            f"{self.REDIS_DB}"
        )

    # --------------------------------------------------
    # TELEGRAM
    # --------------------------------------------------

    TELEGRAM_BOT_TOKEN: str

    TELEGRAM_BOT_USERNAME: str

    TELEGRAM_WEBHOOK_SECRET: str

    # --------------------------------------------------
    # AI
    # --------------------------------------------------

    OPENAI_API_KEY: str = ""

    OPENAI_MODEL: str = "gpt-5"

    # --------------------------------------------------
    # CORS
    # --------------------------------------------------

    ALLOWED_ORIGINS: List[AnyHttpUrl] = []

    # --------------------------------------------------
    # RATE LIMIT
    # --------------------------------------------------

    RATE_LIMIT_PER_MINUTE: int = 120

    # --------------------------------------------------
    # FILE STORAGE
    # --------------------------------------------------

    STORAGE_PATH: str = "storage"

    MAX_UPLOAD_SIZE: int = 25 * 1024 * 1024


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
