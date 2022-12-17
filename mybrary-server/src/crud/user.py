from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import uuid4

from src import models, services, schemas


def create_user(
    db: Session,
    user_id: str,
    user_setup_info: schemas.UserSetupInfo
):
    """Userユーザーを登録する関数

    Args:
        db (Session): DB接続用セッション
        user_id (str): ユーザーid
        user_setup_info (schemas.UserSetupInfo): 受け取ったユーザー情報

    Returns:
        str: 登録したユーザーのuser_id
    """
    try:
        db.add(models.User(
            id = user_id,
            name = user_setup_info.name,
            mail_adress = user_setup_info.mail_adress
        ))
        db.commit()
        db.flush()

        return user_id
    except:
        raise HTTPException(status_code=500, detail="DB登録に失敗しました.")


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
    try:
        target_user = db.query(models.User)\
            .filter(models.User.id == user_id)\
                .first()
        if target_user is None:
            raise HTTPException(
                status_code=404,
                detail="指定されたidのユーザーが見つかりませんでした."
            )
        return target_user
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")