from pydantic import BaseModel

class ProductRecommendationRequest(BaseModel):
    user_input: str

class ProductRecommendationResponse(BaseModel):
    recommendation: str
