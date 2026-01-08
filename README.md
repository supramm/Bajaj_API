
# Trading Platform – Backend API, SDK & UI

This project is a **simplified trading platform** built using **Python and FastAPI**.  
It provides REST APIs for placing trades, tracking orders, viewing portfolios, and includes:
- A **wrapper SDK**
- A **web-based UI**
- **Swagger API documentation**

This project is designed as a **campus hiring assignment submission**.

---

## Features

- 📈 List available trading instruments
- 🛒 Place BUY / SELL orders
- ⚡ Immediate order execution (simulated)
- 📊 Trade history tracking
- 💼 Portfolio management
- 🌐 Web UI dashboard
- 📘 Swagger API documentation
- 📦 Python SDK wrapper

---

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Jinja2 (HTML templates)
- Requests (SDK)

---

## Project Structure

```

trading-platform/
│
├── app.py                 # FastAPI backend
├── templates/
│   └── index.html         # Web UI
├── static/
│   └── style.css          # UI styling
├── sdk/
│   └── client.py          # Python SDK
├── test_sdk.py            # SDK test script
├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd trading-platform
````

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present:

```bash
pip install fastapi uvicorn jinja2 requests
```

---

## Running the Application

```bash
uvicorn app:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## Access Points

* 🌐 **Web UI**
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* 📘 **Swagger API Docs**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

| Method | Endpoint                    | Description       |
| ------ | --------------------------- | ----------------- |
| GET    | `/api/v1/instruments`       | List instruments  |
| POST   | `/api/v1/orders`            | Place an order    |
| GET    | `/api/v1/orders/{order_id}` | Order status      |
| GET    | `/api/v1/trades`            | Trade history     |
| GET    | `/api/v1/portfolio`         | Portfolio summary |

---

## SDK Usage Example

```python
from sdk.client import TradingClient

client = TradingClient("http://127.0.0.1:8000")

print(client.get_instruments())
print(client.place_order("TCS", "BUY", "MARKET", 10))
print(client.get_portfolio())
```

Run SDK test:

```bash
python test_sdk.py
```

---

## Assumptions & Simplifications

* Single user system
* In-memory storage (no database)
* Orders are executed immediately
* No real market data integration
* No authentication

---

## Future Enhancements

* Limit order execution logic
* Database integration
* Authentication & authorization
* Advanced UI (React / charts)
* Order matching engine

---

## Author

**Supram Kumar**
Computer Science Undergraduate
AI & ML Specialization

---

## License

This project is for **educational and evaluation purposes only**.

```
