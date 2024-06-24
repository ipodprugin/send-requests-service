from typing import Optional
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: SecretStr
    BASE_URL: str
    TIMEOUT: int = 10
    MAX_THREADS: int = 5 

settings = Settings()

