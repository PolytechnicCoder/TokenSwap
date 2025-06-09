import asyncio
from fastapi import APIRouter, Query, HTTPException
from services.solana_service import get_balance, get_spl_token_balance
import traceback

router = APIRouter()


@router.get("/balance")
async def get_user_balance(
    address: str = Query(..., description="Public ключ гаманця"),
    mint: str = Query(None, description="Mint-адреса SPL токена (опційно)")
):
    """
    Отримує баланс SOL або SPL токена по гаманцю.
    Якщо mint не вказаний — повертає баланс SOL.
    """
    try:
        if mint:
            balance = await asyncio.to_thread(get_spl_token_balance, address, mint)
        else:
            balance = await asyncio.to_thread(get_balance, address)

        return {
            "address": address,
            "balance": balance,
            "mint": mint or "SOL"
        }

    except Exception as e:
        # Виводимо повний стек помилки для дебагу
        print("[ERROR]:", traceback.format_exc())
        raise HTTPException(
            status_code=400,
            detail=f"{type(e).__name__}: {str(e)}"
        )
