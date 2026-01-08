from pydantic import BaseModel


class Trade(BaseModel):
    tradeId: str
    orderId: str
    symbol: str
    quantity: int
    price: float
