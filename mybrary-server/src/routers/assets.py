import os
import dotenv
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import FileResponse

from src import services
from src.dependencies import get_thumbnail_save_path

dotenv.load_dotenv(override=True)


router = APIRouter(
    prefix='/assets',
    tags=['assets']
)


@router.get('/thumbnails/{isbn}/')
async def get_image(
    isbn: str,
    thumbnail_save_path: str = Depends(get_thumbnail_save_path)
):
    try:
        isbn = services.isbn_normalize(isbn)
        file_path = f"{thumbnail_save_path}/{isbn}.jpg"
        if os.path.exists(file_path):
            return FileResponse(file_path)
        else:
            return FileResponse("src/assets/default/thumbnail_not_found.jpg")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)