from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from src.dependencies import get_db, get_current_user, get_thumbnail_save_path
from src import crud, services, schemas

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post("/books/register/")
async def register_book(
    isbn: str = Query(..., description = "登録したい本のisbnコード"),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
    thumbnail_save_path: str = Depends(get_thumbnail_save_path)
) -> None:
    try:
        isbn = services.isbn_normalize(isbn)
        isbn = services.toggle_isbn10_and_isbn13(isbn) if len(isbn) != 13 else isbn
        target_book = crud.search_book_by_isbn(db=db, isbn=isbn)

        if target_book is None:
            xml_data = services.get_xml_data_from_ndl(isbn)
            res_json = services.xml_to_json(xml_data=xml_data)
            if res_json is None:
                raise HTTPException(
                    status_code=404,
                    detail="指定されたisbnコードの本は見つかりませんでした."
                )
            services.get_thumbnail_from_ndl(
                isbn=isbn,
                thumbnail_save_path=thumbnail_save_path
            )
            registered_isbn = crud.register_book(db=db, book_data_json=res_json)
            isbn = registered_isbn if isbn != registered_isbn else isbn
            target_book = crud.search_book_by_isbn(db=db, isbn=isbn)

        crud.associate_book_to_user(
            db=db,
            user_id=user_id,
            book_id=target_book.id
        )
        return {"message": "本が正常に登録されました."}

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/books", response_model=Page[schemas.UserBookInfo])
async def get_user_books(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):  
    try:
        user_book = crud.get_all_user_book(db=db, user_id=user_id)
        return paginate(list(map(schemas.UserBookInfo.mapping_to_dict, user_book)))
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")