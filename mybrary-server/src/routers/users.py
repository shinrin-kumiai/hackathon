from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies import get_db

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get("/all")
async def get_users(db: Session = Depends(get_db)):
    return {"message": "This end-point is in the user.py!"}

@router.get("/{id}")
async def get_users(db: Session = Depends(get_db)):
    return {"message": "This end-point is in the user.py!"}
