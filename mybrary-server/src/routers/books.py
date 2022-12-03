from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies import get_db

router = APIRouter(
    prefix='/book',
    tags=['book']
)


@router.get("/books")
async def get_books(db: Session = Depends(get_db)) -> dict:
    return {"message": "This end-point is in the book.py!"}