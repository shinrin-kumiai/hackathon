from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_community_book(engine):
    """CommunityBookテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.CommunityBook(
            id = "cmbk0001-0000-0000-0000-000000000000",
            book_id = "book0001-0000-0000-0000-000000000000",
            community_id = "comm0002-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0002-0000-0000-0000-000000000000",
            book_id = "book0002-0000-0000-0000-000000000000",
            community_id = "comm0002-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0003-0000-0000-0000-000000000000",
            book_id = "book0003-0000-0000-0000-000000000000",
            community_id = "comm0002-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0004-0000-0000-0000-000000000000",
            book_id = "book0004-0000-0000-0000-000000000000",
            community_id = "comm0002-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0005-0000-0000-0000-000000000000",
            book_id = "book0005-0000-0000-0000-000000000000",
            community_id = "comm0003-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0006-0000-0000-0000-000000000000",
            book_id = "book0006-0000-0000-0000-000000000000",
            community_id = "comm0003-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0007-0000-0000-0000-000000000000",
            book_id = "book0007-0000-0000-0000-000000000000",
            community_id = "comm0003-0000-0000-0000-000000000000"
        ))
        db.add(models.CommunityBook(
            id = "cmbk0008-0000-0000-0000-000000000000",
            book_id = "book0008-0000-0000-0000-000000000000",
            community_id = "comm0003-0000-0000-0000-000000000000"
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_community_book(engine)