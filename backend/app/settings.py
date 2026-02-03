from functools import lru_cache

from pydantic_settings import BaseSettings

class CoreSettings(BaseSettings):
    DEBUG: bool = False
    APP_NAME: str = "MyShop"

class Settings(CoreSettings):
    pass

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()