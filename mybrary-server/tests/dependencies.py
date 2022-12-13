from src.dependencies import *
from src.main import app

from tests.conftest import TestingSessionLocal


def override_get_db() -> TestingSessionLocal:
    """セッションをテストDB用に上書きする関数

    Returns:
        TestingSessionLocal: テスト用セッションを生成するクラスオブジェクト

    Yields:
        Iterator[TestingSessionLocal]: テスト毎にテスト用セッションを返す
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_get_thumbnail_save_path() -> str:
    """書影の保存先パスを上書きする関数

    Returns:
        str: テスト時の書影の保存先パス
    """
    return "tests/tmp"


def override_get_current_user0001() -> str:
    """ログイン中ユーザーを"user0001"に上書きする関数

    Returns:
        str: user_id (uuid4)
    """
    return "user0001-0000-0000-0000-000000000000"


def override_get_current_user0002() -> str:
    """ログイン中ユーザーを"user0002"に上書きする関数

    Returns:
        str: user_id (uuid4)
    """
    return "user0002-0000-0000-0000-000000000000"

def all_dependency_overrides() -> None:
    """全てのDependsのoverrideを実行する関数
    """
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_thumbnail_save_path] = override_get_thumbnail_save_path
    app.dependency_overrides[get_current_user] = override_get_current_user0001