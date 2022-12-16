import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models
from src.dependencies import get_current_user

from tests.conftest import engine
from tests.dependencies import override_get_current_user0002

client = TestClient(app)
dotenv.load_dotenv(override=True)


def test_isbnコードが9784798067278である登録済みの本のユーザー紐づけ処理が正常に行われる():
    """正常形テスト(/user/books/register/)
    1. テストDBにおいて本の数が10冊であることの確認
    2. ユーザー1の所有している本の冊数が0冊であることの確認
    3. テスト対象エンドポイントを叩き、レスポンスを取得
    4. レスポンスのステータスコードとメッセージを確認
    5. テストDBにおいて本の冊数が10冊で増えていないことの確認
    6. ユーザー1の所有している本の冊数が1冊になっていることの確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 10
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 0

        response = client.post("/user/books/register/?isbn=9784798067278")
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["isbn"] == "9784798067278"

        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 10
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 1
    else:
        pass


def test_isbnコードが9784798167206である未登録の本の登録とユーザー紐づけ処理が正常に行われる():
    """正常形テスト(/user/books/register/)
    1. テストDBにおいて本の数が10冊であることの確認
    2. ユーザー1の所有している本の冊数が0冊であることの確認
    3. テスト対象エンドポイントを叩き、レスポンスを取得
    4. レスポンスのステータスコードとメッセージを確認
    5. tests/tmp/9784798167206.jpgが保存されていることの確認
    6. テストDBにおいて本の冊数が11冊になっていることの確認
    7. ユーザー1の所有している本の冊数が1冊になっていることの確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 10
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 0

        response = client.post("/user/books/register/?isbn=9784798167206")
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["isbn"] == "9784798167206"
        assert len(glob.glob("tests/tmp/9784798167206.jpg")) == 1

        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 11
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 1
    else:
        pass


def test_書影が登録されていない本のisbnコードである9784785300019を指定してPOSTし正常に登録される():
    """正常形テスト(/user/books/register/)
    1. テストDBにおいて本の数が10冊であることの確認
    2. ユーザー1の所有している本の冊数が0冊であることの確認
    3. テスト対象エンドポイントを叩き、レスポンスを取得
    4. レスポンスのステータスコードとメッセージを確認
    5. tests/tmp/9784798167206.jpgが保存されていないことの確認
    6. テストDBにおいて本の冊数が11冊になっていることの確認
    7. ユーザー1の所有している本の冊数が1冊になっていることの確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 10
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 0

        response = client.post("/user/books/register/?isbn=9784785300019")
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["isbn"] == "9784785300019"
        assert len(glob.glob("tests/tmp/9784785300019.jpg")) == 0

        with Session(bind=engine) as db:
            all_books = db.query(models.Book).all()
            assert len(all_books) == 11
            all_user1_books = db.query(models.UserBook)\
                .filter(models.UserBook.user_id == "user0001-0000-0000-0000-000000000000")\
                    .all()
            assert len(all_user1_books) == 1
    else:
        pass


def test_情報がNDLに登録されていない本のisbnコードである9784785300029を指定してPOSTし404エラーを吐く():
    """異常系テスト(/user/books/register/)
    1. NDLに未登録の本のisbnコードである9784785300029を指定してPOST
    2. レスポンスのステータスコードと詳細を確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        response = client.post("/user/books/register/?isbn=9784785300029")
        res_json = response.json()
        assert response.status_code == 404
        assert res_json["detail"] == "指定されたisbnコードの本は見つかりませんでした."
    else:
        pass


def test_存在しない14桁のisbnコードである12345678901234を指定してPOSTし400エラーを吐く():
    """異常系テスト(/user/books/register/)
    1. 存在しない14桁のisbnコードである12345678901234を指定しPOST
    2. レスポンスのステータスコードとメッセージを確認
    """
    response = client.post("/user/books/register/?isbn=12345678901234")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "isbnコードの桁数が正しくありません."



def test_user0001が所有している本の一覧が正常に取得できる():
    """正常系テスト(/user/books)
    1. ログインユーザーを"user0001"に変更
    2. "user0001"が所有している本の一覧をリクエスト
    3. "user0001"が所有している本が3冊取得されることを確認
    """
    response = client.get("/user/books?page=1&size=50")
    res_json = response.json()
    assert response.status_code == 200
    assert len(res_json["items"]) == 0


def test_user0002が所有している本の一覧が正常に取得できる():
    """正常系テスト(/user/books)
    1. ログインユーザーを"user0002"に変更
    2. "user0002"が所有している本の一覧をリクエスト
    3. "user0002"が所有している本が3冊取得されることを確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    response = client.get("/user/books?page=1&size=50")
    res_json = response.json()
    assert response.status_code == 200
    assert len(res_json["items"]) == 3
    assert res_json["items"][0]["book_id"] == "book0001-0000-0000-0000-000000000000"
    assert res_json["items"][1]["book_id"] == "book0002-0000-0000-0000-000000000000"
    assert res_json["items"][2]["book_id"] == "book0003-0000-0000-0000-000000000000"


def test_本の所有idがusbk0001の本の情報を正常に取得できる():
    """正常系テスト(/user/books/{book_id})
    2. book_idが"usbk0001"の本の情報をリクエスト
    3. book_idが"usbk0001"の本の情報が正常に取得されることを確認
    """
    response = client.get("/user/books/usbk0001-0000-0000-0000-000000000000")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["book_id"] == "book0001-0000-0000-0000-000000000000"


def test_本の所有idがusbk0000である存在しない本の情報をリクエストして404エラーを吐く():
    """異常系テスト(/user/books/{book_id})
    2. book_idが"usbk0000"の本の情報をリクエスト
    3. 404エラーが吐かれることを確認
    """
    response = client.get("/user/books/usbk0000-0000-0000-0000-000000000000")
    res_json = response.json()
    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidの本が見つかりませんでした."