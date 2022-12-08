from fastapi.testclient import TestClient

from src.main import app

from tests.conftest import engine

client = TestClient(app)

