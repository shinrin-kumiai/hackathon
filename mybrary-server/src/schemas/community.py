from pydantic import BaseModel, Field

from src import models


class CommunitySetupInfo(BaseModel):
    """コミュニティ作成時に使用するスキーマ

    BaseClass:
        BaseModel: pydanticの基盤クラス
    """
    name: str = Field(..., description="コミュニティ名", max_length=30)
    description: str | None = Field(default=None, description="コミュニティの説明文", max_length=100)

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
    owner_id: str = Field(..., description="コミュニティ所有者のユーザーid")

    def mapping_to_dict(target_community: models.Community) -> dict:
        """Community型のオブジェクトをCommunityInfo型のdictにマッピングする関数

        Args:
            target_community (models.Community): Communityテーブルから取得したレコードオブジェクト

        Returns:
            dict: CommunityInfo型のdict
        """
        pass

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "森林組合",
                "description": "森林組合のコミュニティです.",
                "owner_id": "user0001-0000-0000-0000-000000000000"
            }
        }