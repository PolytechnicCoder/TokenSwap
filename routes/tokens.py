from fastapi import APIRouter
from services.tokens import get_supported_tokens

router = APIRouter()

@router.get("/tokens")
def get_tokens():
    return get_supported_tokens()
