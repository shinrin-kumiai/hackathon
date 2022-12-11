from src.main import app, get_db
from sqlalchemy.orm import sessionmaker

from tests.conftest import TestingSessionLocal


def override_get_db() -> TestingSessionLocal:
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()




def all_dependency_overrides() -> None:
    app.dependency_overrides[get_db] = override_get_db