from sqlalchemy.orm import Session
from fire import Fire

from src import models
from src.database.database import engine


def delete_target_table_records(engine, models_obj) -> None:
    """models_objで受け取ったテーブルオブジェクトの全レコードを削除する関数

    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
        models_obj (<class 'sqlalchemy.sql.schema.Table'>): 削除対象テーブルのオブジェクト
        ※中間テーブルは<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>型
    """
    with Session(bind=engine) as db:
        db.query(models_obj).delete()
        db.commit()


def main(
        engine = engine, 
        book: bool = False,
        user: bool = False,
        community: bool = False,
        user_community: bool = False,
        user_book: bool = False,
        community_book: bool = False,
        user_book_state_log: bool = False,
        community_book_state_log: bool = False,
        state: bool = False,
        all: bool = False
        ) -> None:
    """引数でTrueを受け取ったテーブルに対してdelete_target_table_records関数を呼び出す関数

    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine. Defaults to engine.
        book (bool, optional): Defaults to False.
        user (bool, optional): Defaults to False.
        community (bool, optional): Defaults to False.
        user_community (bool, optional): Defaults to False.
        user_book (bool, optional): Defaults to False.
        community_book (bool, optional): Defaults to False.
        user_book_state_log (bool, optional): Defaults to False.
        community_book_state_log (bool, optional): Defaults to False.
        state (bool, optional): Defaults to False.
        all (bool, optional): 全テーブルの全レコードの削除. Defaults to False.
    """
    if book or all: delete_target_table_records(engine = engine, models_obj = models.Book)
    if user or all: delete_target_table_records(engine = engine, models_obj = models.User)
    if community or all: delete_target_table_records(engine = engine, models_obj = models.Community)
    if user_community or all: delete_target_table_records(engine = engine, models_obj = models.user_community_table)
    if user_book or all: delete_target_table_records(engine = engine, models_obj = models.UserBook)
    if community_book or all: delete_target_table_records(engine = engine, models_obj = models.CommunityBook)
    if user_book_state_log or all: delete_target_table_records(engine = engine, models_obj = models.UserBookStateLog)
    if community_book_state_log or all: delete_target_table_records(engine = engine, models_obj = models.CommunityBookStateLog)
    if state or all: delete_target_table_records(engine = engine, models_obj = models.State)


if __name__ == "__main__":
    Fire(main)