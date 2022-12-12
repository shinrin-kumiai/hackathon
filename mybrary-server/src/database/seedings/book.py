from sqlalchemy.orm import Session

from src import models
from src.database.database import engine


def seeding_to_book(engine) -> None:
    """BookテーブルへのSeeding
    
    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
    """
    with Session(bind=engine) as db:
        db.add(models.Book(
            id = "book0001-0000-0000-0000-000000000000",
            link = "http://iss.ndl.go.jp/books/R100000096-I012781940-00",
            isbn = "9784798067278",
            title = "Python実践データ分析100本ノック",
            creator = "下山, 輝昌",
            publisher = "秀和システム",
        ))
        db.add(models.Book(
            id = "book0002-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000074-I000580639-00",
            isbn= "9784774142043",
            title= "Webを支える技術",
            creator= "山本, 陽平(1975-)",
            publisher= "技術評論社"
        ))
        db.add(models.Book(
            id = "book0003-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000096-I010615692-00",
            isbn= "9784774142357",
            title= "プロになるためのWeb技術入門 : なぜ,あなたはWebシステムを開発できないのか",
            creator= "小森, 裕介",
            publisher= "技術評論社"
        ))
        db.add(models.Book(
            id = "book0004-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000074-I000709259-00",
            isbn= "9784873115658",
            title= "リーダブルコード",
            creator= "Boswell, Dustin",
            publisher= "オライリー・ジャパン"
        ))
        db.add(models.Book(
            id = "book0005-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000002-I025901139-00",
            isbn= "9784873116860",
            title= "Web API:The Good Parts",
            creator= "水野, 貴明, 1973-",
            publisher= "オライリー・ジャパン"
        ))
        db.add(models.Book(
            id = "book0006-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000074-I000686013-00",
            isbn= "9784873117386",
            title= "入門Python3",
            creator= "Lubanovic, Bill",
            publisher= "オライリー・ジャパン"
        ))
        db.add(models.Book(
            id = "book0007-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000096-I000289981-00",
            isbn= "9784774184111",
            title= "JavaScript本格入門 : モダンスタイルによる基礎から現場での応用まで : \"なんとなく書ける\"で終わらせず、変わりゆくスタイルを本質から理解して、効率的なモノ作りを実現するために。",
            creator= "山田, 祥寛",
            publisher= "技術評論社"
        ))
        db.add(models.Book(
            id = "book0008-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000002-I031633004-00",
            isbn= "9784798169101",
            title= "IT用語図鑑",
            creator= "増井, 敏克, 1979-",
            publisher= "翔泳社"
        ))
        db.add(models.Book(
            id = "book0009-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000002-I029945915-00",
            isbn= "9784815601577",
            title= "確かな力が身につくJavaScript「超」入門",
            creator= "狩野, 祐東",
            publisher= "SBクリエイティブ"
        ))
        db.add(models.Book(
            id = "book0010-0000-0000-0000-000000000000",
            link= "http://iss.ndl.go.jp/books/R100000096-I012583582-00",
            isbn= "9784863543591",
            title= "基礎から学ぶReact/React Hooks : 実践入門 : つまずきポイントを確認しながらすすめる!",
            creator= "asakohattori",
            publisher= "シーアンドアール研究所"
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_book(engine)