import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models
from src.dependencies import get_current_user

from tests.conftest import engine
from tests.dependencies import override_get_current_user0002, override_get_current_user0003

client = TestClient(app)
dotenv.load_dotenv(override=True)


def test_ユーザー登録が正常に実行される():
    """正常形テスト([post]/user/signup)
    1. 現在のユーザーの人数が8人であることの確認
    2. ユーザー登録処理
    3. ユーザーが正常に登録されていることの確認
    """
    with Session(bind=engine) as db:
        all_users = db.query(models.User).all()
        assert len(all_users) == 8

        response = client.post("/user/signup", json={
            "name": "森林 太郎",
            "mail_adress": "sample@example.com",
        })
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["name"] == "森林 太郎"

    with Session(bind=engine) as db:
        all_users = db.query(models.User).all()
        assert len(all_users) == 9


def test_ユーザー名が未入力でユーザー登録リクエストを送り422エラーを吐く():
    """異常形テスト([post]/user/signup)
    1. 現在のユーザーの人数が8人であることの確認
    2. ユーザー登録処理
    3. レスポンスの確認
    4. ユーザー人数が変化していないことの確認
    """
    with Session(bind=engine) as db:
        all_users = db.query(models.User).all()
        assert len(all_users) == 8

        response = client.post("/user/signup", json={
            "name": "森林 太郎",
            "mail_adress": "sample@example.com",
        })
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["name"] == "森林 太郎"

    with Session(bind=engine) as db:
        all_users = db.query(models.User).all()
        assert len(all_users) == 9


def test_isbnコードが9784798067278である登録済みの本のユーザー紐づけ処理が正常に行われる():
    """正常形テスト([post]/user/books/register/)
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
    """正常形テスト([post]/user/books/register/)
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
    """正常形テスト([post]/user/books/register/)
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
    """異常系テスト([post]/user/books/register/)
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
    """異常系テスト([post]/user/books/register/)
    1. 存在しない14桁のisbnコードである12345678901234を指定しPOST
    2. レスポンスのステータスコードとメッセージを確認
    """
    response = client.post("/user/books/register/?isbn=12345678901234")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "isbnコードの桁数が正しくありません."



def test_user0001が所有している本の一覧が正常に取得できる():
    """正常系テスト([get]/user/books)
    1. ログインユーザーを"user0001"に変更
    2. "user0001"が所有している本の一覧をリクエスト
    3. "user0001"が所有している本が3冊取得されることを確認
    """
    response = client.get("/user/books?page=1&size=50")
    res_json = response.json()
    assert response.status_code == 200
    assert len(res_json["items"]) == 0


def test_user0002が所有している本の一覧が正常に取得できる():
    """正常系テスト([get]/user/books)
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
    """正常系テスト([get]/user/books/{book_id})
    2. book_idが"usbk0001"の本の情報をリクエスト
    3. book_idが"usbk0001"の本の情報が正常に取得されることを確認
    """
    response = client.get("/user/books/usbk0001-0000-0000-0000-000000000000")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["book_id"] == "book0001-0000-0000-0000-000000000000"


def test_本の所有idがusbk0000である存在しない本の情報をリクエストして404エラーを吐く():
    """異常系テスト([get]/user/books/{book_id})
    2. book_idが"usbk0000"の本の情報をリクエスト
    3. 404エラーが吐かれることを確認
    """
    response = client.get("/user/books/usbk0000-0000-0000-0000-000000000000")
    res_json = response.json()
    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidの本が見つかりませんでした."


def test_user0002が所有しているusbk0001という所有idの本を正常に削除できる():
    """正常系テスト([delete]/user/books/{book_id})
    1. ログイン中のユーザーをuser0002に変更
    2. usbk0001をuser0002が所有していることの確認
    3. user0002の所有本からusbk0001を削除するリクエストを送る
    4. user0002の所有本にusbk0001が無くなっていることを確認する
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    book_ownership_id = "usbk0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_book = db.query(models.UserBook)\
            .filter(models.UserBook.id == book_ownership_id)\
                .first()
        target_book is not None

    response = client.delete(f"/user/books/{book_ownership_id}")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == f"id:{book_ownership_id}の本を削除しました."

    with Session(bind=engine) as db:
        target_book = db.query(models.UserBook)\
            .filter(models.UserBook.id == book_ownership_id)\
                .first()
        target_book is None


def test_user0001がuser0002が所有しているusbk0001という所有idの本を削除しようとして403エラーを吐く():
    """異常系テスト([delete]/user/books/{book_id})
    1. usbk0001をuser0002が所有していることの確認
    2. user0001でログイン中だがuser0002の所有本からusbk0001を削除するリクエストを送る
    3. user0002の所有本にusbk0001が無くなっていないことを確認する
    """
    book_ownership_id = "usbk0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_book = db.query(models.UserBook)\
            .filter(models.UserBook.id == book_ownership_id)\
                .first()
        target_book is not None

    response = client.delete(f"/user/books/{book_ownership_id}")
    res_json = response.json()
    assert response.status_code == 403
    assert res_json["detail"] == "この本の削除機能へのアクセス権限がありません."

    with Session(bind=engine) as db:
        target_book = db.query(models.UserBook)\
            .filter(models.UserBook.id == book_ownership_id)\
                .first()
        target_book is not None


def test_user0003が所属しているコミュニティの一覧を正常に取得できる():
    """正常形テスト([get]/user/communities)
    1. ログイン中のユーザーをuser0003に変更
    2. user0003が所属しているコミュニティ情報の一覧をリクエスト
    3. レスポンスを確認し、正常に取得できていることを確認する
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    
    response = client.get("/user/communities")
    res_json = response.json()
    assert response.status_code == 200
    assert len(res_json) == 1
    assert res_json[0]["name"] == "コミュニティ1"
