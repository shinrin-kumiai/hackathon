from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import uuid4

from src import models, services, schemas


def search_user_by_id(
    db: Session,
    user_id: str
) -> models.User:
    """ユーザーidからユーザー情報を取得する関数

    Args:
        db (Session): DB接続用セッション
        user_id (str): 検索対象ユーザーid

    Returns:
        models.User: ユーザーテーブルのレコードオブジェクト
    """
    return db.query(models.User)\
        .filter(models.User.id == user_id)\
            .first()
