from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.dependencies import get_db

router = APIRouter(
    prefix='/community',
    tags=['community']
)

@router.get("/communities")
async def get_communities(db: Session = Depends(get_db)):
    return {"message": "This end-point is in the community.py!"}