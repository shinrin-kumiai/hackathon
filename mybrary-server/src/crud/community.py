from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import uuid4

from src import models, services, schemas


def create_new_community(
    db: Session,
    user_id: str,
    community_setup_info: schemas.CommunitySetupInfo
    ) -> str:
    """コミュニティを新規作成する関数

    Args:
        db (Session): DB接続用セッション
        user_id (str): コミュニティを作成したユーザーのid
        community_setup_info (schemas.CommunitySetupInfo): POSTで受け取ったコミュニティ情報

    Returns:
        str: 作成したコミュニティの id
    """
    community_id = str(uuid4())
    db.add(models.Community(
        id = community_id,
        name = community_setup_info.name,
        owner_id = user_id,
        description = community_setup_info.description
    ))
    db.commit()
    db.flush()
    return community_id


def search_community_by_id(
    db: Session,
    community_id: str
    ) -> models.Community:
    """コミュニティ情報をコミュニティidで取得する関数

    Args:
        db (Session): DB接続用セッション
        community_id (str): 取得対象コミュニティのid

    Returns:
        models.Community: 取得されたコミュニティ情報
    """
    try:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        if target_community is None:
            raise HTTPException(
                status_code=404,
                detail="指定されたidのコミュニティが見つかりませんでした."
            )
        else:
            return target_community
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")


def add_commynity_member(
    db: Session,
    community_id: str,
    target_user_id: str
) -> None:
    """community_idで指定されたコミュニティにtarget_user_idで指定されたユーザーを登録する関数

    Args:
        db (Session): DB接続用セッション
        community_id (str): 登録対象コミュニティid
        target_user_id (str): 登録対象ユーザーid
    """
    community = db.query(models.Community).filter(models.Community.id == community_id).first()
    user = db.query(models.User).filter(models.User.id == target_user_id).first()
    if user is None:
        raise HTTPException(
            status_code = 404,
            detail = "指定されたidのユーザーが見つかりませんでした."
        )
    community.user.append(user)
    db.commit()