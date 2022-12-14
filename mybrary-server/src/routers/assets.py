import os
import dotenv
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from src import services

dotenv.load_dotenv(override=True)


router = APIRouter(
    prefix='/assets',
    tags=['assets']
)


@router.get('/thumbnails/{isbn}')
async def get_image(
    isbn: str
):
    try:
        isbn = services.isbn_normalize(isbn)
        file_path = f"{os.environ.get('THUMBNAIL_SAVE_PATH')}/{isbn}.jpg"
        if os.path.exists(file_path):
            return FileResponse(file_path)
        else:
            return FileResponse("src/assets/default/thumbnail_not_found.jpg")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")
