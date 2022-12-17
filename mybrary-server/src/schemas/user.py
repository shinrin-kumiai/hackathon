from pydantic import BaseModel, Field

from src import models


class UserSetupInfo(BaseModel):
    name: str = Field(..., description="ニックネーム", max_length=30)
    mail_adress: str | None = Field(default=None, description="メールアドレス")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "森林 太郎",
                "mail_adress": "sample@example.com",
            }
        }


class UserInfo(UserSetupInfo):
    id: str = Field(..., description="ユーザーid")
    has_permission: bool = Field(..., description="アクセスユーザー=所有者の場合True")

    def mapping_to_dict(target_user: models.User, user_id: str):
        """User型のオブジェクトをUserInfo型のdictにマッピングする関数

        Args:
            target_user (models.User): Userテーブルから取得したレコードオブジェクト
            user_id (str): ログイン中のユーザー

        Returns:
            dict: UserInfo型のdict
        """
        return dict(
            id = target_user.id,
            name = target_user.name,
            mail_adress = target_user.mail_adress,
            has_permission = True if target_user.id == user_id else False
        )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id":"user0001-0000-0000-0000-000000000000",
                "name": "佐藤",
                "mail_adress": "sample@example.com",
                "has_permission": "false"
            }
        }

