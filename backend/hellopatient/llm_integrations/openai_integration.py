import os
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_community.chat_message_histories import SQLChatMessageHistory



os.environ["OPENAI_API_KEY"] = ""

from langchain_openai import ChatOpenAI

def open_ai_integration(model):
    valid_models = ["gpt-4o-mini"]
    if model not in valid_models:
        raise ValueError(f"Invalid model. Choose from: {', '.join(valid_models)}")
    return ChatOpenAI(
            model=model,
            temperature=0.0,
            max_tokens=1000
    )



