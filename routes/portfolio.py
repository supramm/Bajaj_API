from fastapi import APIRouter
from data.store import PORTFOLIO, INSTRUMENTS

router = APIRouter()


@router.get("/api/v1/portfolio")
def get_portfolio():
    response = []

    for symbol, holding in PORTFOLIO.items():
        instrument = next(i for i in INSTRUMENTS if i["symbol"] == symbol)
        ltp = instrument["lastTradedPrice"]

        response.append({
            "symbol": symbol,
            "quantity": holding["quantity"],
            "averagePrice": holding["averagePrice"],
            "currentValue": holding["quantity"] * ltp
        })

    return response
