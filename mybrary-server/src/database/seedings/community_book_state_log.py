from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta

from src import models
from src.database.database import engine


def seeding_to_community_book_state_log(engine) -> None:
    """CommunityBookStateLogテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0001-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0002-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0003-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0004-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0005-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0006-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0007-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.add(models.CommunityBookStateLog(
            community_book_id = "cmbk0008-0000-0000-0000-000000000000",
            state_id = 1,
            relation_user_id = None,
            return_due_date = date.today() + timedelta(days=7),
            register_date = datetime.now()
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_community_book_state_log(engine)