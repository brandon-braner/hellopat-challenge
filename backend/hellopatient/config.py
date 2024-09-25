import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

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




@lru_cache
def get_settings():
    return Settings()