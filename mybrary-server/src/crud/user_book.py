from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from src import models


def associate_book_to_user(db: Session, user_id: str, book_id: str) -> None:
    """本をユーザーに紐づける(所有させる)関数

    Args:
        db (Session): DB接続用セッション
        user_id (str): ユーザーid
        book_id (str): 本id
    """
    db.add(models.UserBook(
        id = str(uuid4()),
        user_id = user_id,
        book_id = book_id
    ))
    db.commit()
    db.flush()


def get_all_user_book(db: Session, user_id: str):
    """ログイン中のユーザーが所有している全ての本を配列で取得する関数

    Args:
        db (Session): DB接続用セッション
        user_id (str): ユーザーid

    Returns:
        <models.UserBook>: ログイン中のユーザーが所有している本の一覧
    """
    return db.query(models.UserBook)\
        .filter(models.UserBook.user_id == user_id)\
            .join(models.Book, models.UserBook.book_id == models.Book.id)\
                .all()


def search_user_book_by_id(db: Session, book_id: str) -> models.UserBook:
    """ユーザー所有の本をidで情報取得する関数

    Args:
        db (Session): DB接続用セッション
        book_id (str): 取得対象の本のid

    Returns:
        models.UserBook: UserBookテーブルのレコードオブジェクト
    """
    target_book = db.query(models.UserBook)\
        .filter(models.UserBook.id == book_id)\
            .join(models.Book, models.UserBook.book_id == models.Book.id)\
                .first()
    if target_book is None:
        raise HTTPException(
            status_code=404,
            detail="指定されたidの本が見つかりませんでした."
        )
    return target_book


def delete_user_book_by_id(db: Session, book_id: str) -> None:
    """idで指定されたユーザー所有の本を削除する関数

    Args:
        db (Session): DB接続用セッション
        book_id (str): 削除対象の本のid

    Returns:
        models.UserBook: UserBookテーブルのレコードオブジェクト
    """
    try:
        db.query(models.UserBook)\
            .filter(models.UserBook.id == book_id)\
                .delete()
        db.commit()
    except:
        raise HTTPException(
            status_code=500,
            detail="本の削除に失敗しました"
        )