from hellopatient.llm_integrations.llm_factory import get_llm_with_chat_history
from langchain_core.messages import HumanMessage

class ProductRecommendationService:

    async def get_recommendation(self, user_input: str, session_id: str) -> str:
        llm = get_llm_with_chat_history()

        human_message = HumanMessage(user_input)
        llm_response = llm.invoke(
            [human_message],
            config={"configurable": {"session_id": session_id}},
        )

        return llm_response.content
