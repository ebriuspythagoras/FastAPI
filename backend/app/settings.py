from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    DEBUG: bool = False
    APP_NAME: str = "MyShop"


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    @property
    def DATABASE_ASYNC_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@"
            f"{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"
        )


class Settings(CoreSettings, PostgresSettings):
    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
