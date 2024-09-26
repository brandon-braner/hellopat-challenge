from fastapi import APIRouter, HTTPException

from hellopatient.chat.schmea import ProductRecommendationRequest, ProductRecommendationResponse
from hellopatient.chat.service import ProductRecommendationService
from hellopatient.chat.chat_history_service import ChatHistoryService

router = APIRouter(prefix='/chat')



@router.post("/product_recommendation")
async def product_recommendation_chat(request: ProductRecommendationRequest) -> ProductRecommendationResponse:
    service = ProductRecommendationService()
    recommendation = await service.get_recommendation(
        request.user_input, request.session_id
    )

    return ProductRecommendationResponse(
        response=recommendation,
        session_id=request.session_id
    )

@router.get("/get_chat_history/{session_id}")
async def get_chat_history(session_id: str):
   service = ChatHistoryService()
   return await service.get_chat_history(session_id)