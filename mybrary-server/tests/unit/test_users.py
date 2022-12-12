import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models

from tests.conftest import engine

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
        assert res_json["message"] == "本が正常に登録されました."

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
        assert res_json["message"] == "本が正常に登録されました."
        assert glob.glob("/tests/tmp/9784798167206.jpg") is not None

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


def test_書影が登録されていない本のisbnコードである9784785300012を指定してPOSTし404エラーを吐く():
    """異常系テスト(/user/books/register/)
    1. NDLに書影が未登録の本のisbnコードである9784785300012を指定してPOST
    2. レスポンスのステータスコードと詳細を確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        response = client.post("/user/books/register/?isbn=9784785300012")
        res_json = response.json()
        assert response.status_code == 404
        assert res_json["detail"] == "書影が見つかりませんでした."
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
    assert res_json["detail"] == "isbnコードは10桁or13桁で指定してください."