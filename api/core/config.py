from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT / ".env",
        env_file_encoding="utf-8",
    )

    database_url: str = ""
    app_title: str = "API de Livros"
    app_description: str = "CRUD de livros com FastAPI + SQLModel"
    app_version: str = "1.0.0"
    db_echo: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()