from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SwapRequest(BaseModel):
    user_address: str
    amount: float
    from_token: str
    to_token: str

@router.post("/swap")
async def swap_tokens(request: SwapRequest):
    # Поки що лише симуляція
    return {
        "status": "success",
        "message": f"Swapped {request.amount} {request.from_token} → {request.to_token} for user {request.user_address}"
    }
