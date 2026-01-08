from pydantic import BaseModel
from typing import Optional


class OrderRequest(BaseModel):
    symbol: str
    side: str            # BUY or SELL
    orderType: str       # MARKET or LIMIT
    quantity: int
    price: Optional[float] = None
