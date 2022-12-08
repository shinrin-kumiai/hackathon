from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_sample():
    a = 1
    b = 2
    assert 2*a == b