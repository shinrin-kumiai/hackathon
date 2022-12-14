from pydantic import BaseModel, Field

from src import models


class UserBookInfo(BaseModel):
    """ユーザー所有の本のレスポンスモデル

    BaseClass:
        BaseModel: pydanticの基盤クラス
    """
    id: str = Field(..., description="所有id")
    book_id: str = Field(..., description="本のid")
    user_id: str = Field(..., description="所有者id")
    title: str = Field(..., description="本のタイトル")
    publisher: str = Field(..., description="出版社")
    creator: str = Field(..., description="著者")
    isbn: str = Field(..., description="isbn13")

    def mapping_to_dict(user_book: models.UserBook) -> dict:
        """UserBook型のオブジェクトをUserBookInfo型のdictにマッピングする関数

        Args:
            user_book (models.UserBook): UserBookテーブルから取得したレコードオブジェクト

        Returns:
            dict: UserBookInfo型のdict
        """
        return dict(
            id = user_book.id,
            book_id = user_book.book_id,
            user_id = user_book.user_id,
            title = user_book.book.title,
            publisher = user_book.book.publisher,
            creator = user_book.book.creator,
            isbn = user_book.book.isbn
        )
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id":"usbk0001-0000-0000-0000-000000000000",
                "book_id": "book0001-0000-0000-0000-000000000000",
                "user_id": "user0001-0000-0000-0000-000000000000",
                "title": "Pythonの本",
                "publisher": "森林書房",
                "creator": "森田 林",
                "isbn": "9780000000000"
            }
        }