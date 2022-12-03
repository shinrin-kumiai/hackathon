from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_state(engine):
    """StateテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.State(state="貸出可能"))
        db.add(models.State(state="貸出申請中"))
        db.add(models.State(state="貸出中"))
        db.add(models.State(state="返却申請中"))
        db.add(models.State(state="貸出停止"))
        db.commit()


if __name__ == "__main__":
    seeding_to_state(engine)