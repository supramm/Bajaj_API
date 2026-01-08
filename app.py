from fastapi import FastAPI
from routes.instruments import router as instruments_router
from routes.orders import router as orders_router
from routes.trades import router as trades_router
from routes.portfolio import router as portfolio_router

app = FastAPI(title="Trading Backend API")


@app.get("/")
def health_check():
    return {"status": "API is running"}


app.include_router(instruments_router)
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(portfolio_router)