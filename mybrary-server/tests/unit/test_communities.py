import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models, schemas
from src.dependencies import get_current_user

from tests.conftest import engine
from tests.dependencies import override_get_current_user0002

client = TestClient(app)
dotenv.load_dotenv(override=True)


def test_user0001が新規コミュニティを正常に作成できる():
    """正常形テスト(/community/create)
    1. テストDBにおいてコミュニティの数が3つであることの確認
    2. コミュニティ作成エンドポイントを叩く
    3. レスポンスのステータスコードとメッセージを確認
    4. テストDBにおいてコミュニティの数が4つに増えていることの確認
    """
    with Session(bind=engine) as db:
        all_communities = db.query(models.Community).all()
        assert len(all_communities) == 3

    response = client.post("/community/create", json={
        "name": "森林組合",
        "description": "森林組合のコミュニティです."
    })
    res_json = response.json()
    assert response.status_code == 200
    assert res_json["name"] == "森林組合"
    assert res_json["description"] == "森林組合のコミュニティです."
    assert res_json["owner_id"] == "user0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        all_communities = db.query(models.Community).all()
        assert len(all_communities) == 4