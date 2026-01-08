from fastapi import APIRouter
from data.store import TRADES

router = APIRouter()


@router.get("/api/v1/trades")
def get_trades():
    return TRADES
