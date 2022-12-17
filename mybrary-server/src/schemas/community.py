from pydantic import BaseModel, Field

from src import models


class CommunitySetupInfo(BaseModel):
    """コミュニティ作成時に使用するスキーマ

    BaseClass:
        BaseModel: pydanticの基盤クラス
    """
    name: str = Field(..., description="コミュニティ名", max_length=30)
    description: str | None = Field(default=None, description="コミュニティの説明文", max_length=150)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "森林組合",
                "description": "森林組合のコミュニティです."
            }
        }


class CommunityInfo(CommunitySetupInfo):
    """コミュニティ情報を返すレスポンスモデル

    BaseClass:
        CommunitySetupInfo: コミュニティ作成時に使用するスキーマ
    """
    id:str = Field(..., description="コミュニティid")
    owner_id: str = Field(..., description="コミュニティ所有者のユーザーid")
    has_permission: bool = Field(..., description="アクセスユーザー=コミュニティオーナーの場合True")

    def mapping_to_dict(target_community: models.Community, user_id: str) -> dict:
        """Community型のオブジェクトをCommunityInfo型のdictにマッピングする関数

        Args:
            target_community (models.Community): Communityテーブルから取得したレコードオブジェクト
            user_id (str): ログイン中のユーザー

        Returns:
            dict: CommunityInfo型のdict
        """
        return dict(
            id = target_community.id,
            name = target_community.name,
            description = target_community.description,
            owner_id = target_community.owner_id,
            has_permission = True if target_community.owner_id == user_id else False
        )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "森林組合",
                "description": "森林組合のコミュニティです.",
                "id": "comm0000-0000-0000-0000-000000000000",
                "owner_id": "user0001-0000-0000-0000-000000000000",
                "has_permission": "false"
            }
        }