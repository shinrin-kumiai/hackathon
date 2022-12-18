from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from src import models, crud


class BookInfo(BaseModel):
    """Bookテーブルデータのレスポンスモデル

    BaseClass:
        BaseModel: pydanticの基盤クラス
    """
    id: str = Field(..., description="本のid")
    isbn: str = Field(..., description="isbn13")
    title: str = Field(..., description="本のタイトル")
    creator: str = Field(..., description="著者")
    publisher: str = Field(..., description="出版社")

    def mapping_to_dict(target_book: models.Book) -> dict:
        """Book型のオブジェクトをBookInfo型にマッピングする関数

        Args:
            target_book (models.Book): Bookテーブルから取得したレコードオブジェクト

        Returns:
            dict: BookInfo型のdict
        """
        return dict(
            id = target_book.id,
            isbn = target_book.isbn,
            title = target_book.title,
            creator = target_book.creator,
            publisher = target_book.publisher
        )
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "book-0000-0000-0000-000000000000",
                "isbn": "9780000000000",
                "title": "Pythonの本",
                "creator": "森田 林",
                "publisher": "森林書房"
            }
        }


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
    has_permission: bool = Field(..., description="アクセスユーザー=所有者の場合True")
    latest_state_id: int = Field(..., description="最新のステータスidを返す")

    def mapping_to_dict(user_book: models.UserBook, user_id: str, db: Session) -> dict:
        """UserBook型のオブジェクトをUserBookInfo型のdictにマッピングする関数

        Args:
            user_book (models.UserBook): UserBookテーブルから取得したレコードオブジェクト
            user_id (str): ログイン中のユーザーid

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
            isbn = user_book.book.isbn,
            has_permission = True if user_book.user_id == user_id else False,
            latest_state_id = crud.get_latest_state_by_user_book_id(user_book_id=user_book.id, db=db).state_id,
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
                "isbn": "9780000000000",
                "has_permission": "false",
                "latest_state_id": 1
            }
        }