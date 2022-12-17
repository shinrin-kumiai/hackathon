from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import uuid4
from datetime import datetime, date

from src import models, services, schemas


def get_latest_state_by_user_book_id(
    user_book_id: str,
    db: Session,
) -> int:
    """本の所有idによって指定された本の最新のステータスを取得する関数

    Args:
        user_book_id (str): ユーザー所有本の所有id
        db (Session): DB接続用セッション

    Returns:
        int: 指定された本の最初ステータスid
    """
    target_user_book_state = db.query(
        models.UserBookStateLog
    )\
        .filter(models.UserBookStateLog.user_book_id == user_book_id)\
            .order_by(models.UserBookStateLog.register_date.desc())\
                .first()

    if target_user_book_state is None:
        raise HTTPException(
            status_code = 404,
            detail = "指定された本が見つかりませんでした."
        )

    return target_user_book_state


def set_state_lendable_to_applying(
    db: Session,
    user_book_id: str,
    user_id: str,
    return_due_date: date
) -> None:
    """本の最新ステートを貸出可能から貸出申請中に変更

    Args:
        user_book_id (str): ユーザー所有本の所有id
        user_id (str): 貸出申請元のユーザーid
        return_due_date (date): 返却予定日
        db (Session): DB接続用セッション
    """
    db.add(models.UserBookStateLog(
        user_book_id = user_book_id,
        state_id = 2,
        relation_user_id = user_id,
        return_due_date = return_due_date,
        register_date = datetime.now()
    ))
    db.commit()
    db.flush()


def set_state_applying_to_allowed(
    db: Session,
    user_book_id: str,
    user_id: str,
    return_due_date: date
) -> None:
    """本の最新ステートを貸出申請中から貸出許可中に変更

    Args:
        user_book_id (str): ユーザー所有本の所有id
        user_id (str): 貸出申請元のユーザーid
        return_due_date (date): 返却予定日
        db (Session): DB接続用セッション
    """
    db.add(models.UserBookStateLog(
        user_book_id = user_book_id,
        state_id = 3,
        relation_user_id = user_id,
        return_due_date = return_due_date,
        register_date = datetime.now()
    ))
    db.commit()
    db.flush()


def set_state_allowed_to_confirmed(
    db: Session,
    user_book_id: str,
    user_id: str,
    return_due_date: date
) -> None:
    """本の最新ステートを貸出許可中から貸出中に変更

    Args:
        user_book_id (str): ユーザー所有本の所有id
        user_id (str): 貸出申請元のユーザーid
        return_due_date (date): 返却予定日
        db (Session): DB接続用セッション
    """
    db.add(models.UserBookStateLog(
        user_book_id = user_book_id,
        state_id = 4,
        relation_user_id = user_id,
        return_due_date = return_due_date,
        register_date = datetime.now()
    ))
    db.commit()
    db.flush()


def set_state_back_to_lendable(
    db: Session,
    user_book_id: str,
    user_id: str,
) -> None:
    """本の最新ステートを貸出中から貸出可能に変更

    Args:
        user_book_id (str): ユーザー所有本の所有id
        user_id (str): 貸出申請元のユーザーid
        db (Session): DB接続用セッション
    """
    db.add(models.UserBookStateLog(
        user_book_id = user_book_id,
        state_id = 1,
        relation_user_id = user_id,
        return_due_date = None,
        register_date = datetime.now()
    ))
    db.commit()
    db.flush()
