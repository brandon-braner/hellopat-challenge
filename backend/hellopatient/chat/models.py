from pydantic import BaseModel

class ProductRecommendationRequest(BaseModel):
    user_input: str
    session_id: str

class ProductRecommendationResponse(BaseModel):
    recommendation: str
    session_id: str
