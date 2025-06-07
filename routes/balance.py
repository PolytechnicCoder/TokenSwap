import asyncio
from fastapi import APIRouter, Query, HTTPException
from services.solana_service import get_balance

router = APIRouter()

@router.get("/balance")
async def get_user_balance(address: str = Query(..., description="User's public wallet address")):
    try:
        balance = await asyncio.to_thread(get_balance, address)
        return {"address": address, "balance": balance}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

