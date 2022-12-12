from sqlalchemy.orm import Session
from uuid import uuid4

from src import models, services


def search_book_by_isbn(db: Session, isbn: str) -> models.Book | None:
    """Bookテーブルからisbnコードで本を検索する関数

    Args:
        db (Session): DB接続用セッション
        isbn (str): isbnコード

    Returns:
        models.Book | None: models.bookオブジェクト or 該当無しならNoneが返る
    """
    return db.query(models.Book)\
        .filter(models.Book.isbn == isbn)\
            .first()


def register_book(db: Session, book_data_json: str) -> None:
    """bookテーブルに本を新規登録する関数

    Args:
        db (Session): DB接続用セッション
        book_data_json (str): 国立国会図書館APIから取得した書誌jsonデータ
    
    Return:
        isbn (str): DBに登録したisbn13を返す
            →リクエストとレスポンスでisbnが異なる場合があるため
    """
    isbn = services.isbn_normalize(book_data_json["identifier"]["ISBN"][0])
    if len(isbn) == 10: 
        isbn = services.toggle_isbn10_and_isbn13(isbn)

    db.add(models.Book(
        id = str(uuid4()),
        link = book_data_json['link'],
        isbn = isbn,
        title = book_data_json["title"][0]["value"],
        creator = book_data_json["dc_creator"][0]["name"].replace("著", ""),
        publisher = book_data_json["publisher"][0]["name"]
    ))
    db.commit()
    db.flush()
    return isbn