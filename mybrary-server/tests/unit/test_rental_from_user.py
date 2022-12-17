import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models
from src.dependencies import get_current_user

from tests.conftest import engine
from tests.dependencies import override_get_current_user0001, override_get_current_user0002, override_get_current_user0003

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


def test_usbk0001への貸し出し申請に対して貸し出し許可を行い正常に処理される():
    """正常形テスト([post]/user/{user_book_id}/rental-permit)
    1. usbk0001を指定して貸し出し申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. レスポンスのステータスコードとメッセージを確認
    5. 正常に申請処理が行われていることの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 3


def test_user0002が所有している本usbk0001への貸出申請に対してuser0003が貸出許可を行い403エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-permit)
    1. usbk0001を指定して貸出申請をリクエスト
    2. ログイン中のユーザーをuser0003に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. レスポンスのステータスコードとメッセージを確認
    5. usbk0001の最新ステータスが変更されていないことの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0003

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "自分の本ではない本に対して貸出許可を行うことは出来ません."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 2


def test_ステータスが貸出可能ではないusbk0001に対してuser0002が貸し出し許可申請を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-permit)
    1. usbk0001を指定して貸し出し許可申請をリクエスト
    2. レスポンスのステータスコードとメッセージを確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "この本は現在貸出許可対象ではありません."


def test_usbk0001への貸し出し許可に対して貸し出し確認を行い正常に処理される():
    """正常形テスト([post]/user/{user_book_id}/rental-confirm)
    1. usbk0001を指定して貸し出し申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. ログイン中のユーザーをuser0001に戻す
    5. 貸出受取を行う
    6. レスポンスのステータスコードとメッセージを確認
    7. 正常に申請処理が行われていることの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0001
    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出確認処理が行われました."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 4


def test_user0002が所有している本usbk0001への貸出許可に対して自分で貸出許可を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-confirm)
    1. usbk0001を指定して貸出申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. user0002のまま貸出許可に対して貸出確認処理を行う
    4. レスポンスのステータスコードとメッセージを確認
    5. usbk0001の最新ステータスが変更されていないことの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."


    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "自分の本に対して貸出確認を行うことは出来ません."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 3


def test_user0002が所有している本usbk0001へのuser0001からの貸出許可に対してuser0003で貸出許可を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-confirm)
    1. usbk0001を指定して貸出申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. 貸出許可に対して貸出確認処理を行う
    4. レスポンスのステータスコードとメッセージを確認
    5. usbk0001の最新ステータスが変更されていないことの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0003

    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 403
    assert res_json["detail"] == "この処理へのアクセス権がありません."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 3


def test_ステータスが貸出許可中ではないusbk0001に対してuser0001が貸し出し確認処理を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-confirm)
    1. usbk0001を指定して貸し出し許可申請をリクエスト
    2. レスポンスのステータスコードとメッセージを確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0001

    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "この本は現在貸出確認対象ではありません."


def test_usbk0001への貸出確認に対して返却確認を行い正常に処理される():
    """正常形テスト([post]/user/{user_book_id}/return-confirm)
    1. usbk0001を指定して貸し出し申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. ログイン中のユーザーをuser0001に変更
    5. 貸出許可に対して貸出確認を行う
    6. レスポンスのステータスコードとメッセージを確認
    5. 正常に申請処理が行われていることの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0001

    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出確認処理が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/return-confirm")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に返却処理が行われました."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 1


def test_usbk0001への貸出確認に対してuser0003が返却確認を行い400エラーを吐く():
    """正常形テスト([post]/user/{user_book_id}/return-confirm)
    1. usbk0001を指定して貸し出し申請をリクエスト
    2. ログイン中のユーザーをuser0002に変更
    3. 貸し出し申請に対して貸し出し許可を行う
    4. ログイン中のユーザーをuser0003に変更
    5. 貸出許可に対して貸出確認を行う
    6. レスポンスのステータスコードとメッセージを確認
    5. 正常に申請処理が行われていないことの確認
    """
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/rental-request")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "貸出申請を正常に送信しました."

    app.dependency_overrides[get_current_user] = override_get_current_user0002

    response = client.post(f"/user/{user_book_id}/rental-permit")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出許可が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0001

    response = client.post(f"/user/{user_book_id}/rental-confirm")
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["message"] == "正常に貸出確認処理が行われました."

    app.dependency_overrides[get_current_user] = override_get_current_user0003

    response = client.post(f"/user/{user_book_id}/return-confirm")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "自分の本ではない本に対して返却確認を行うことは出来ません."

    with Session(bind=engine) as db:
        target_user_book_state = db.query(
            models.UserBookStateLog
        )\
            .filter(models.UserBookStateLog.user_book_id == user_book_id)\
                .order_by(models.UserBookStateLog.register_date.desc())\
                    .first()
        assert target_user_book_state.state_id == 4


def test_ステータスが貸出確認ではないusbk0001に対してuser0002が返却確認処理を行い400エラーを吐く():
    """異常系テスト([post]/user/{user_book_id}/rental-permit)
    1. usbk0001を指定して貸し出し許可申請をリクエスト
    2. レスポンスのステータスコードとメッセージを確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    user_book_id = "usbk0001-0000-0000-0000-000000000000"

    response = client.post(f"/user/{user_book_id}/return-confirm")
    res_json = response.json()
    assert response.status_code == 400
    assert res_json["detail"] == "この本は現在返却対象ではありません."