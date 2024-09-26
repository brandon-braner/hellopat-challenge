from hellopatient.config import get_db_engine
from hellopatient.chat.models import MessageStore
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class ChatHistoryService:
    async def get_chat_history(self, session_id: str):
        engine = get_db_engine()
        async with AsyncSession(engine) as session:
            async with session.begin():
                stmt = select(MessageStore).where(MessageStore.session_id == session_id)
                sessions = [row.__dict__ for row in await session.scalars(stmt)]
        
        return sessions