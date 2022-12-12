from src.database.database import SessionLocal

def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()def get_thumbnail_save_path() -> str:
    """書影の保存先パスを返す関数

    Returns:
        str: .envから取得した書影の保存先パス
    """
    return os.environ.get("THUMBNAIL_SAVE_PATH")