from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from hellopatient.config import get_settings
from models import Base

settings = get_settings()

_main_uri = f"""{settings.pg_username}:{settings.pg_password}@{settings.pg_host}:{settings.pg_port}/{settings.pg_database}"""
_sync_uri = f"postgresql://{_main_uri}"
_async_uri = f"postgresql+asyncpg://{_main_uri}"

sync_engine = create_engine(_sync_uri)

Base.metadata.create_all(sync_engine)

engine = create_async_engine(_async_uri)
