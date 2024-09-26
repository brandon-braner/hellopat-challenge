from pydantic import BaseModel

class ProductRecommendationRequest(BaseModel):
    user_input: str
    session_id: str

class ProductRecommendationResponse(BaseModel):
    response: str
    session_id: str

class MessageStore(BaseModel):
    id: int
    session_id: str
    message: str