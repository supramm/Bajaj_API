import uuid
from data.store import INSTRUMENTS, TRADES, PORTFOLIO


def execute_order(order: dict):
    symbol = order["symbol"]
    quantity = order["quantity"]
    side = order["side"]
    order_type = order["orderType"]
    limit_price = order["price"]

    instrument = next(i for i in INSTRUMENTS if i["symbol"] == symbol)
    market_price = instrument["lastTradedPrice"]

    execution_price = market_price

    if order_type == "LIMIT":
        if side == "BUY" and limit_price < market_price:
            return False
        if side == "SELL" and limit_price > market_price:
            return False
        execution_price = limit_price

    trade = {
        "tradeId": str(uuid.uuid4()),
        "orderId": order["orderId"],
        "symbol": symbol,
        "quantity": quantity,
        "price": execution_price
    }

    TRADES.append(trade)

    holding = PORTFOLIO.get(symbol, {"quantity": 0, "averagePrice": 0})

    if side == "BUY":
        total_cost = holding["quantity"] * holding["averagePrice"] + quantity * execution_price
        new_qty = holding["quantity"] + quantity
        avg_price = total_cost / new_qty
        PORTFOLIO[symbol] = {
            "quantity": new_qty,
            "averagePrice": avg_price
        }
    else:
        PORTFOLIO[symbol]["quantity"] -= quantity

    return trade
