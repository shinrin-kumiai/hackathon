from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from typing import List
from functools import partial
from uuid import uuid4
from datetime import datetime, date, timedelta

from src.dependencies import get_db, get_current_user, get_thumbnail_save_path
from src import crud, services, schemas

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post("/signup", response_model=schemas.UserInfo)
async def create_user(
    user_setup_info: schemas.UserSetupInfo,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
    ):
    try:
        user_id = str(uuid4()) #現在は仮でuuid直入れしてます.認証機能の実装後修正します.

        try:
            crud.search_user_by_id(db=db, user_id=user_id)
        except HTTPException as e:
            if e.detail == "指定されたidのユーザーが見つかりませんでした.":
                registered_user_id = crud.create_user(
                    db=db,
                    user_id=user_id,
                    user_setup_info=user_setup_info
                )
                return schemas.UserInfo.mapping_to_dict(
                    target_user=crud.search_user_by_id(db=db, user_id=registered_user_id),
                    user_id=registered_user_id
                )
            else:
                raise HTTPException(
                    status_code=e.status_code,
                    detail=e.detail
                )
        raise HTTPException(
            status_code=400,
            detail="既にユーザー登録されています."
        )

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/books/register/", response_model=schemas.UserBookInfo)
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

        registered_user_book_id = crud.associate_book_to_user(
            db=db,
            user_id=user_id,
            book_id=target_book.id
        )
        crud.set_state_to_lendable(
            user_book_id=registered_user_book_id,
            user_id=user_id,
            db=db
        )
        return schemas.UserBookInfo.mapping_to_dict(
            user_book=crud.search_user_book_by_id(db=db, user_book_id=registered_user_book_id),
            user_id=user_id,
            db=db
        )

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/books", response_model=Page[schemas.UserBookInfo])
async def get_user_books(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):  
    try:
        user_book = crud.get_all_user_book(db=db, user_id=user_id)
        return paginate(list(map(partial(schemas.UserBookInfo.mapping_to_dict, user_id=user_id, db=db), user_book)))
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{target_user_id}/books", response_model=Page[schemas.UserBookInfo])
async def get_user_books(
    target_user_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):  
    try:
        user_book = crud.get_all_user_book(db=db, user_id=target_user_id)
        return paginate(list(map(partial(schemas.UserBookInfo.mapping_to_dict, user_id=user_id, db=db), user_book)))
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/books/{user_book_id}", response_model=schemas.UserBookInfo)
async def search_book_by_id(
    user_book_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
) -> schemas.UserBookInfo:
    try:
        return schemas.UserBookInfo.mapping_to_dict(
            user_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id),
            user_id = user_id,
            db=db
        )

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.delete("/books/{user_book_id}")
async def delete_book_by_id(
    user_book_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
) -> schemas.UserBookInfo:
    try:
        target_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id)
        if target_book.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="この本の削除機能へのアクセス権限がありません."
            )
        crud.delete_user_book_by_id(db=db, book_id=user_book_id)
        return {"message": f"id:{user_book_id}の本を削除しました."}

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/communities", response_model=List[schemas.CommunityInfo])
async def get_belong_communities(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
) -> str:
    try:
        belong_communities = crud.search_user_by_id(db=db, user_id=user_id).community
        return list(map(partial(schemas.CommunityInfo.mapping_to_dict, user_id=user_id), belong_communities))

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{target_user_id}")
async def get_user_info(
    target_user_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user = crud.search_user_by_id(db=db, user_id=target_user_id)
        return schemas.UserInfo.mapping_to_dict(target_user, user_id)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{target_user_id}")
async def get_user_info(
    target_user_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user = crud.search_user_by_id(db=db, user_id=target_user_id)
        return schemas.UserInfo.mapping_to_dict(target_user, user_id)

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/{user_book_id}/rental-request")
async def send_rental_request(
    user_book_id: str,
    return_due_date: date = Query(default=date.today()+timedelta(days=7), description="返却予定日を指定:YYYY-MM-DD"),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id)

        if target_user_book.user_id == user_id:
            raise HTTPException(
                status_code=400,
                detail="自分の本に対して貸出申請を行うことは出来ません."
            )

        latest_state = crud.get_latest_state_by_user_book_id(db=db, user_book_id=user_book_id)

        if latest_state.state_id != 1:
            raise HTTPException(
                status_code=400,
                detail="この本は現在貸出不可状態です."
            )

        crud.set_state_lendable_to_applying(
            user_book_id = user_book_id,
            user_id = user_id,
            return_due_date = return_due_date,
            db = db
        )
        return {"message": "貸出申請を正常に送信しました."}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/{user_book_id}/rental-permit")
async def send_rental_request(
    user_book_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id)

        if target_user_book.user_id != user_id:
            raise HTTPException(
                status_code=400,
                detail="自分の本ではない本に対して貸出許可を行うことは出来ません."
            )

        latest_state = crud.get_latest_state_by_user_book_id(db=db, user_book_id=user_book_id)

        if latest_state.state_id != 2:
            raise HTTPException(
                status_code=400,
                detail="この本は現在貸出許可対象ではありません."
            )

        crud.set_state_applying_to_allowed(
            user_book_id = user_book_id,
            user_id = latest_state.relation_user_id,
            return_due_date = latest_state.return_due_date,
            db = db
        )
        return {"message": "正常に貸出許可が行われました."}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/{user_book_id}/rental-confirm")
async def send_rental_request(
    user_book_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id)

        if target_user_book.user_id == user_id:
            raise HTTPException(
                status_code=400,
                detail="自分の本に対して貸出確認を行うことは出来ません."
            )

        latest_state = crud.get_latest_state_by_user_book_id(db=db, user_book_id=user_book_id)

        if latest_state.relation_user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="この処理へのアクセス権がありません."
            )

        if latest_state.state_id != 3:
            raise HTTPException(
                status_code=400,
                detail="この本は現在貸出確認対象ではありません."
            )

        crud.set_state_allowed_to_confirmed(
            user_book_id = user_book_id,
            user_id = user_id,
            return_due_date = latest_state.return_due_date,
            db = db
        )
        return {"message": "正常に貸出確認処理が行われました."}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/{user_book_id}/return-confirm")
async def send_rental_request(
    user_book_id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        target_user_book = crud.search_user_book_by_id(db=db, user_book_id=user_book_id)

        if target_user_book.user_id != user_id:
            raise HTTPException(
                status_code=400,
                detail="自分の本ではない本に対して返却確認を行うことは出来ません."
            )

        latest_state = crud.get_latest_state_by_user_book_id(db=db, user_book_id=user_book_id)

        if latest_state.state_id != 4:
            raise HTTPException(
                status_code=400,
                detail="この本は現在返却対象ではありません."
            )

        crud.set_state_back_to_lendable(
            user_book_id = user_book_id,
            user_id = latest_state.relation_user_id,
            db = db
        )
        return {"message": "正常に返却処理が行われました."}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)