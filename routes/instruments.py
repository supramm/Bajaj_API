from fastapi import APIRouter
from data.store import INSTRUMENTS

router = APIRouter()


@router.get("/api/v1/instruments")
def get_instruments():
    return INSTRUMENTS
