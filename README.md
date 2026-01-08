
# Trading Backend API (Simulated Broker System)

## Overview

This project is a **Python-based backend trading system** built using **FastAPI**.  
It simulates core functionalities of an online stock broking platform such as:

- Viewing tradable instruments  
- Placing buy and sell orders (Market and Limit)  
- Executing orders  
- Viewing executed trades  
- Viewing portfolio holdings  

The system uses **in-memory storage** and does **not connect to real markets**.  
The focus of this project is on **API design, backend structure, and trading logic simulation**.

---

## Technology Stack

- **Language:** Python 3  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Data Storage:** In-memory (Python dictionaries and lists)  
- **API Format:** JSON  

---

## Project Structure

```

trading_api/
│
├── app.py
│
├── data/
│   └── store.py
│
├── models/
│   ├── order.py
│   ├── trade.py
│   └── portfolio.py
│
├── routes/
│   ├── instruments.py
│   ├── orders.py
│   ├── trades.py
│   └── portfolio.py
│
├── services/
│   └── order_service.py
│
├── requirements.txt
└── README.md

````

---

## Setup and Run Instructions

### Prerequisites
- Python 3.9 or higher
- pip

### Install Dependencies
```bash
pip install fastapi uvicorn
````

### Run the Application

```bash
uvicorn app:app --reload
```

### Access the API

* Base URL: `http://127.0.0.1:8000`
* Swagger UI (API documentation): `http://127.0.0.1:8000/docs`

---

## API Details

### Health Check

```
GET /
```

Response:

```json
{
  "status": "API is running"
}
```

---

### Fetch Instruments

```
GET /api/v1/instruments
```

Response:

```json
[
  {
    "symbol": "TCS",
    "exchange": "NSE",
    "instrumentType": "EQUITY",
    "lastTradedPrice": 3850.0
  }
]
```

---

### Place Order

```
POST /api/v1/orders
```

Request Body:

```json
{
  "symbol": "TCS",
  "side": "BUY",
  "orderType": "MARKET",
  "quantity": 5
}
```

Response:

```json
{
  "orderId": "...",
  "symbol": "TCS",
  "side": "BUY",
  "orderType": "MARKET",
  "quantity": 5,
  "price": null,
  "status": "EXECUTED"
}
```

Validations:

* Quantity must be greater than 0
* Symbol must exist
* Price is mandatory for LIMIT orders

---

### Get Order Status

```
GET /api/v1/orders/{orderId}
```

Response:

```json
{
  "orderId": "...",
  "status": "EXECUTED",
  "symbol": "TCS",
  "side": "BUY",
  "quantity": 5
}
```

---

### Fetch Trades

```
GET /api/v1/trades
```

Response:

```json
[
  {
    "tradeId": "...",
    "orderId": "...",
    "symbol": "TCS",
    "quantity": 5,
    "price": 3850.0
  }
]
```

---

### Fetch Portfolio

```
GET /api/v1/portfolio
```

Response:

```json
[
  {
    "symbol": "TCS",
    "quantity": 5,
    "averagePrice": 3850.0,
    "currentValue": 19250.0
  }
]
```

---

## Order Execution Logic

* **Market Orders:** Execute immediately at the last traded price
* **Limit Orders:**

  * BUY orders execute only if limit price is greater than or equal to market price
  * SELL orders execute only if limit price is less than or equal to market price
* Executed orders generate trades
* Trades update portfolio holdings
* Portfolio average price is calculated using weighted average pricing

---

## Assumptions Made

* Single hardcoded user (no authentication)
* No real market connectivity
* In-memory data storage (data resets on server restart)
* No order cancellation functionality
* No partial order fills
* Immediate execution simulation
* Portfolio is a derived, read-only view

---

## Design Decisions

* Separation of concerns using routes, services, models, and data layers
* Business logic isolated in the service layer
* RESTful API design principles followed
* Clean and readable code for ease of evaluation and explanation

---

## Notes

This project is designed for **demonstration and evaluation purposes only**.
It focuses on backend design, API structure, and trading workflow simulation rather than production readiness.

```
