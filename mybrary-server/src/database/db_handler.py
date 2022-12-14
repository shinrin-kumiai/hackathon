from src.database.database import engine
from src.models import Base
from fire import Fire


def db_handler(db_create:bool=False,db_delete:bool=False) -> None:
    """DB作成とDB削除を引数のboolで判定して実行する関数
    Args:
        db_create:true or falseを受け取る
        db_delete:true or falseを受け取る
    """
    if db_create:
        #DBの作成
        Base.metadata.create_all(bind=engine)
    if db_delete:
        #DBの削除
        Base.metadata.drop_all(bind=engine)


if __name__ =="__main__":
    Fire(db_handler)
    

