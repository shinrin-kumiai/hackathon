from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_user(engine) -> None:
    """UserテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.User(
            id = "user0001-0000-0000-0000-000000000000",
            name = "佐藤",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0002-0000-0000-0000-000000000000",
            name = "鈴木",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0003-0000-0000-0000-000000000000",
            name = "高橋",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0004-0000-0000-0000-000000000000",
            name = "田中",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0005-0000-0000-0000-000000000000",
            name = "伊藤",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0006-0000-0000-0000-000000000000",
            name = "渡辺",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0007-0000-0000-0000-000000000000",
            name = "山本",
            mail_adress = "sample@example.com"
        ))
        db.add(models.User(
            id = "user0008-0000-0000-0000-000000000000",
            name = "中村",
            mail_adress = "sample@example.com"
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_user(engine)