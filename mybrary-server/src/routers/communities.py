from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from src.dependencies import get_db, get_current_user, get_thumbnail_save_path
from src import crud, services, schemas

router = APIRouter(
    prefix='/community',
    tags=['community']
)


@router.post("/create", response_model=schemas.CommunityInfo)
async def create_community(
    community_setup_info: schemas.CommunitySetupInfo
) -> None:
    try:
        return {
                    "name": "森林組合",
                    "description": "森林組合のコミュニティです.",
                    "owner_id": "user0001-0000-0000-0000-000000000000"
                }
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")