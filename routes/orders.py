from fastapi import APIRouter, HTTPException
from models.order import OrderRequest
from data.store import INSTRUMENTS, ORDERS
from services.order_service import execute_order
import uuid

router = APIRouter()


@router.post("/api/v1/orders")
def place_order(order: OrderRequest):

    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    symbols = [i["symbol"] for i in INSTRUMENTS]
    if order.symbol not in symbols:
        raise HTTPException(status_code=404, detail="Instrument not found")

    if order.orderType == "LIMIT" and order.price is None:
        raise HTTPException(status_code=400, detail="Price required for LIMIT order")

    order_id = str(uuid.uuid4())

    ORDERS[order_id] = {
        "orderId": order_id,
        "symbol": order.symbol,
        "side": order.side,
        "orderType": order.orderType,
        "quantity": order.quantity,
        "price": order.price,
        "status": "PLACED"
    }


    
    trade = execute_order(ORDERS[order_id])

    if trade:
        ORDERS[order_id]["status"] = "EXECUTED"

    return ORDERS[order_id]
