import os
import dotenv
from src.database.database import SessionLocal

dotenv.load_dotenv(override=True)


def get_db() -> SessionLocal:
    """DBへのセッションを返す関数

    Returns:
        SessionLocal: セッションを作成するためのクラスオブジェクト

    Yields:
        Iterator[SessionLocal]: DB接続の為のセッション
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user() -> str:
    """ログイン中ユーザーのユーザーidを返す関数

    Returns:
        str: user_id (uuid4)
    """
    return "user0005-0000-0000-0000-000000000000"


def get_thumbnail_save_path() -> str:
    """書影の保存先パスを返す関数

    Returns:
        str: .envから取得した書影の保存先パス
    """
    return os.environ.get("THUMBNAIL_SAVE_PATH")