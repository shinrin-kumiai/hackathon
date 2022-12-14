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
    community_setup_info: schemas.CommunitySetupInfo,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
) -> None:
    try:
        created_community_id = crud.create_new_community(
                db=db,
                user_id=user_id, 
                community_setup_info=community_setup_info
            )
        created_community = crud.search_community_by_id(
                db=db,
                community_id=created_community_id
            )
        return schemas.CommunityInfo.mapping_to_dict(target_community=created_community)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")