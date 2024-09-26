from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
Base = declarative_base()

class MessageStore(Base):
    __tablename__ = 'message_store'

    id = Column(Integer, primary_key=True)
    session_id = Column(Text, nullable=False)
    message = Column(Text, nullable=False)


