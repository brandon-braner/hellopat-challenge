from langchain_community.chat_message_histories.sql import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from hellopatient.config import get_settings
from hellopatient.llm_integrations.openai_integration import open_ai_integration

settings = get_settings()


def get_llm_with_chat_history() -> RunnableWithMessageHistory:
    llm = settings.llm
    model_name = settings.llm_model
    model = None

    match llm:
        case "open_ai":
            model = _get_openai_integration(model_name)
        case _:
            raise NotImplementedError(f"LLM {llm} not implemented")

    return RunnableWithMessageHistory(
        model, _get_session_history_postgres
    )

def _get_session_history_postgres(session_id: str):
    connection_string = f"postgresql://{settings.pg_username}:{settings.pg_password}@{settings.pg_host}:{settings.pg_port}/{settings.pg_database}"
    
    return SQLChatMessageHistory(session_id, connection_string)


def _get_openai_integration(model):
    return open_ai_integration(model)
