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


def test_user0002が所有している本usbk0001に対してuser0001が貸し出し申請を行い正常に処理される():
    """正常形テスト([post]/user/{user_book_id}/rental-request)
    1. usbk0001を指定して貸し出し申請をリクエスト
    2. レスポンスのステータスコードとメッセージを確認
    3. 正常に申請処理が行われていることの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 1

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 2


def test_user0002が所有している本usbk0001に対してuser0002が貸し出し申請を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-request)
    1. ログイン中のユーザーをuser0002に変更
    2. usbk0001を指定して貸し出し申請をリクエスト
    3. レスポンスのステータスコードとメッセージを確認
    4. usbk0001の最新ステータスが変更されていないことの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 1

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "自分の本に対して貸出申請を行うことは出来ません."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 1


def test_ステータスが貸出可能ではないusbk0001に対してuser0002が貸し出し申請を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-request)
    1. usbk0001を指定して貸し出し申請を2度リクエスト
    2. レスポンスのステータスコードとメッセージを確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "この本は現在貸出不可状態です."