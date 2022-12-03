from sqlalchemy.orm import Session

from src import models
from src.database.database import engine




def seeding_to_user_community(engine):
    """user_communityテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        community = db.query(models.Community).filter(models.Community.id == "comm0001-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0003-0000-0000-0000-000000000000").first()
        community.user.append(user)
        
        community = db.query(models.Community).filter(models.Community.id == "comm0001-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0004-0000-0000-0000-000000000000").first()
        community.user.append(user)
        
        community = db.query(models.Community).filter(models.Community.id == "comm0002-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0005-0000-0000-0000-000000000000").first()
        community.user.append(user)

        community = db.query(models.Community).filter(models.Community.id == "comm0002-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0006-0000-0000-0000-000000000000").first()
        community.user.append(user)

        community = db.query(models.Community).filter(models.Community.id == "comm0002-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0008-0000-0000-0000-000000000000").first()
        community.user.append(user)

        community = db.query(models.Community).filter(models.Community.id == "comm0003-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0007-0000-0000-0000-000000000000").first()
        community.user.append(user)

        community = db.query(models.Community).filter(models.Community.id == "comm0003-0000-0000-0000-000000000000").first()
        user = db.query(models.User).filter(models.User.id == "user0008-0000-0000-0000-000000000000").first()
        community.user.append(user)

        db.commit()


if __name__ == "__main__":
    seeding_to_user_community(engine)