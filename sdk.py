import requests


class TradingSDK:
    """
    Lightweight Python SDK that wraps Trading REST APIs
    """

    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")

    def get_instruments(self):
        """
        Fetch list of tradable instruments
        """
        response = requests.get(f"{self.base_url}/api/v1/instruments")
        response.raise_for_status()
        return response.json()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place a BUY or SELL order (MARKET or LIMIT)
        """
        payload = {
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "quantity": quantity
        }

        if price is not None:
            payload["price"] = price

        response = requests.post(
            f"{self.base_url}/api/v1/orders",
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def get_order_status(self, order_id):
        """
        Fetch status of an order by orderId
        """
        response = requests.get(
            f"{self.base_url}/api/v1/orders/{order_id}"
        )
        response.raise_for_status()
        return response.json()

    def get_trades(self):
        """
        Fetch list of executed trades
        """
        response = requests.get(f"{self.base_url}/api/v1/trades")
        response.raise_for_status()
        return response.json()

    def get_portfolio(self):
        """
        Fetch current portfolio holdings
        """
        response = requests.get(f"{self.base_url}/api/v1/portfolio")
        response.raise_for_status()
        return response.json()
