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
            isbn = "9784798067278",
            jan = "jan",
            title = "Python実践データ分析100本ノック",
            author = "下山 輝昌",
            publisher = "秀和システム",
            price = 2400,
            language = "ja",
            page_count = 367,
            size = 21
        ))
        db.add(models.Book(
            id = "book0002-0000-0000-0000-000000000000",
            isbn = "9784774142043",
            jan = "jan",
            title = "Webを支える技術",
            author = "山本 陽平",
            publisher = "技術評論社",
            price = 2570,
            language = "ja",
            page_count = 377,
            size = 21
        ))
        db.add(models.Book(
            id = "book0003-0000-0000-0000-000000000000",
            isbn = "9784774142357",
            jan = "jan",
            title = "プロになるためのWeb技術入門 : なぜ,あなたはWebシステムを開発できないのか",
            author = "小森 裕介",
            publisher = "技術評論社",
            price = 2280,
            language = "ja",
            page_count = 277,
            size = 23
        ))
        db.add(models.Book(
            id = "book0004-0000-0000-0000-000000000000",
            isbn = "9784873115658",
            jan = "jan",
            title = "リーダブルコード : より良いコードを書くためのシンプルで実践的なテクニック",
            author = "角 征典",
            publisher = "オライリー・ジャパン",
            price = 2400,
            language = "ja",
            page_count = 237,
            size = 21
        ))
        db.add(models.Book(
            id = "book0005-0000-0000-0000-000000000000",
            isbn = "9784873116860",
            jan = "jan",
            title = "Web API : the good parts",
            author = "水野 貴明",
            publisher = "オライリー・ジャパン",
            price = 2200,
            language = "ja",
            page_count = 208,
            size = 24
        ))
        db.add(models.Book(
            id = "book0006-0000-0000-0000-000000000000",
            isbn = "9784774184111",
            jan = "jan",
            title = "JavaScript本格入門 : モダンスタイルによる基礎から現場での応用まで",
            author = "山田 祥寛",
            publisher = "技術評論社",
            price = 2980,
            language = "ja",
            page_count = 455,
            size = 23
        ))
        db.add(models.Book(
            id = "book0007-0000-0000-0000-000000000000",
            isbn = "9784797398892",
            jan = "jan",
            title = "1冊ですべて身につくHTML&CSSとWebデザイン入門講座",
            author = "Mana",
            publisher = "SBクリエイティブ",
            price = 2260,
            language = "ja",
            page_count = 279,
            size = 24
        ))
        db.add(models.Book(
            id = "book0008-0000-0000-0000-000000000000",
            isbn = "9784798169101",
            jan = "jan",
            title = "IT用語図鑑",
            author = "増井 敏克",
            publisher = "翔泳社",
            price = 1800,
            language = "ja",
            page_count = 295,
            size = 21
        ))
        db.add(models.Book(
            id = "book0009-0000-0000-0000-000000000000",
            isbn = "9784815601577",
            jan = "jan",
            title = "確かな力が身につくJavaScript「超」入門",
            author = "狩野 祐東",
            publisher = "SBクリエイティブ",
            price = 2480,
            language = "ja",
            page_count = 325,
            size = 24
        ))
        db.add(models.Book(
            id = "book0010-0000-0000-0000-000000000000",
            isbn = "9784863543591",
            jan = "jan",
            title = "基礎から学ぶReact/React Hooks : 実践入門 : つまずきポイントを確認しながらすすめる!",
            author = "asakohattori",
            publisher = "シーアンドアール研究所",
            price = 3420,
            language = "ja",
            page_count = 375,
            size = 21
        ))
        db.commit()


if __name__ == "__main__":
    seeding_to_book(engine)