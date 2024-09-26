from fastapi import APIRouter, HTTPException

from hellopatient.chat.models import ProductRecommendationRequest, ProductRecommendationResponse
from hellopatient.chat.service import ProductRecommendationService

router = APIRouter(prefix='/chat')



@router.post("/product_recommendation")
async def product_recommendation_chat(request: ProductRecommendationRequest) -> ProductRecommendationResponse:
    service = ProductRecommendationService()
    recommendation = await service.get_recommendation(
        request.user_input, request.session_id
    )

    return ProductRecommendationResponse(
        recommendation=recommendation,
        session_id=request.session_id
    )