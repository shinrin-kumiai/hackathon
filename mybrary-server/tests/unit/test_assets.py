import os
import dotenv
from fastapi.testclient import TestClient

from src.main import app
from src import models

from tests.conftest import engine

client = TestClient(app)
dotenv.load_dotenv(override=True)


def test_isbnコードが9784798167206である本の書影が正しく取得できる():
    """正常形(/assets/thumbnails)
    1. isbnコードが9784798167206である本を登録
    2. 登録した本の書影を正しく取得できることを確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        response = client.post("/user/books/register/?isbn=9784798167206")
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["isbn"] == "9784798167206"
        
        response = client.get("/assets/thumbnails/9784798167206")
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/jpeg"
        assert response.headers["content-length"] == "22351"
    else:
        pass


def test_isbnコードが9784785300019である書影がない本の書影が正しく取得できる():
    """正常形(/assets/thumbnails)
    1. isbnコードが9784785300019である本を登録
    2. 登録した本の書影を正しく取得できることを確認

    Note:
        .env > NDLAPI_RELATED_TEST_EXECUTE_IS == "true"の場合のみテスト実行
    """
    if os.environ.get('NDLAPI_RELATED_TEST_EXECUTE_IS') == "true":
        response = client.post("/user/books/register/?isbn=9784785300019")
        res_json = response.json()
        assert response.status_code == 200
        assert res_json["isbn"] == "9784785300019"
        
        response = client.get("/assets/thumbnails/9784785300019")
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/jpeg"
        assert response.headers["content-length"] == "53416"
    else:
        pass