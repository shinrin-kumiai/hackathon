from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_user_book(engine):
    """UserBookテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.UserBook(
            id = "usbk0001-0000-0000-0000-000000000000",
            book_id = "book0001-0000-0000-0000-000000000000",
            user_id = "user0002-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0002-0000-0000-0000-000000000000",
            book_id = "book0002-0000-0000-0000-000000000000",
            user_id = "user0002-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0003-0000-0000-0000-000000000000",
            book_id = "book0003-0000-0000-0000-000000000000",
            user_id = "user0002-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0004-0000-0000-0000-000000000000",
            book_id = "book0004-0000-0000-0000-000000000000",
            user_id = "user0003-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0005-0000-0000-0000-000000000000",
            book_id = "book0005-0000-0000-0000-000000000000",
            user_id = "user0003-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0006-0000-0000-0000-000000000000",
            book_id = "book0006-0000-0000-0000-000000000000",
            user_id = "user0003-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0007-0000-0000-0000-000000000000",
            book_id = "book0007-0000-0000-0000-000000000000",
            user_id = "user0005-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0008-0000-0000-0000-000000000000",
            book_id = "book0008-0000-0000-0000-000000000000",
            user_id = "user0005-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0009-0000-0000-0000-000000000000",
            book_id = "book0009-0000-0000-0000-000000000000",
            user_id = "user0005-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0010-0000-0000-0000-000000000000",
            book_id = "book0010-0000-0000-0000-000000000000",
            user_id = "user0006-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0011-0000-0000-0000-000000000000",
            book_id = "book0001-0000-0000-0000-000000000000",
            user_id = "user0006-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0012-0000-0000-0000-000000000000",
            book_id = "book0002-0000-0000-0000-000000000000",
            user_id = "user0006-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0013-0000-0000-0000-000000000000",
            book_id = "book0006-0000-0000-0000-000000000000",
            user_id = "user0007-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0014-0000-0000-0000-000000000000",
            book_id = "book0007-0000-0000-0000-000000000000",
            user_id = "user0007-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0015-0000-0000-0000-000000000000",
            book_id = "book0008-0000-0000-0000-000000000000",
            user_id = "user0007-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0016-0000-0000-0000-000000000000",
            book_id = "book0003-0000-0000-0000-000000000000",
            user_id = "user0008-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0017-0000-0000-0000-000000000000",
            book_id = "book0004-0000-0000-0000-000000000000",
            user_id = "user0008-0000-0000-0000-000000000000"
        ))
        db.add(models.UserBook(
            id = "usbk0018-0000-0000-0000-000000000000",
            book_id = "book0005-0000-0000-0000-000000000000",
            user_id = "user0008-0000-0000-0000-000000000000"
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_user_book(engine)