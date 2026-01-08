from pydantic import BaseModel


class PortfolioItem(BaseModel):
    symbol: str
    quantity: int
    averagePrice: float
    currentValue: float
