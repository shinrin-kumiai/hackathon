from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_community(engine) -> None:
    """CommunityテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.Community(
            id = "comm0001-0000-0000-0000-000000000000",
            name = "コミュニティ1",
            owner_id = "user0003-0000-0000-0000-000000000000"
        ))
        db.add(models.Community(
            id = "comm0002-0000-0000-0000-000000000000",
            name = "コミュニティ2",
            owner_id = "user0005-0000-0000-0000-000000000000"
        ))
        db.add(models.Community(
            id = "comm0003-0000-0000-0000-000000000000",
            name = "コミュニティ3",
            owner_id = "user0007-0000-0000-0000-000000000000"
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_community(engine)