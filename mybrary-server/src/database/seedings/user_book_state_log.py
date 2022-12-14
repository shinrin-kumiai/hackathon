from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta

from src import models
from src.database.database import engine


def seeding_to_user_book_state_log(engine) -> None:
    """UserBookStateLogテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0001-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0002-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0003-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0004-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0005-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0006-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0007-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0008-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0009-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0010-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0011-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0012-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0013-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0014-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0015-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0016-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0017-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.UserBookStateLog(
            user_book_id = "usbk0018-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_user_book_state_log(engine)