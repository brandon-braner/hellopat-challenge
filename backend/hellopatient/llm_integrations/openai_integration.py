import os

from langchain_openai import ChatOpenAI

from hellopatient.config import get_settings

settings = get_settings()

os.environ["OPENAI_API_KEY"] = f"{settings.openai_api_key}"



def open_ai_integration(model: str):
    valid_models = ["gpt-4o-mini"]

    if model not in valid_models:
        raise ValueError(f"Invalid model. Choose from: {', '.join(valid_models)}")
    
    return ChatOpenAI(
            model=model,
            temperature=0.0,
            max_tokens=1000
    )
