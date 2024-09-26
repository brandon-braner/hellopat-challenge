import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from models import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine


current_dir = Path(__file__).parent.resolve()
env_file = current_dir.parent / ".env"


if env_file.exists():
    load_dotenv(env_file)


class Settings(BaseSettings):
    app_name: str = "HelloPatient"
    pg_username: str = os.environ.get("HELLO_PATIENT_PG_USERNAME", "postgres")
    pg_password: str = os.environ.get("HELLO_PATIENT_PG_PASSWORD", "postgres")
    pg_host: str = os.environ.get("HELLO_PATIENT_PG_HOST", "localhost")
    pg_port: int = os.environ.get("HELLO_PATIENT_PG_PORT", 5432)
    pg_database: str = os.environ.get("HELLO_PATIENT_PG_DATABASE", "postgres")
    
    llm: str = os.environ.get("HELLO_PATIENT_LLM", "")
    llm_model: str = os.environ.get("HELLO_PATIENT_LLM_MODEL", "")
    openai_api_key: str = os.environ.get("OPENAI_API_KEY", "")



def get_db_engine():
    settings = get_settings()
    _main_uri = (
    f"{settings.pg_username}:{settings.pg_password}@"
    f"{settings.pg_host}:{settings.pg_port}/{settings.pg_database}"
)

    _async_uri = f"postgresql+asyncpg://{_main_uri}"

    async_engine = create_async_engine(_async_uri)

    return async_engine

@lru_cache
def get_settings():
    return Settings()