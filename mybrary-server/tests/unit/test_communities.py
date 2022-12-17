import os
import dotenv
import glob
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.main import app
from src import models, schemas
from src.dependencies import get_current_user

from tests.conftest import engine
from tests.dependencies import override_get_current_user0002, override_get_current_user0003

client = TestClient(app)
dotenv.load_dotenv(override=True)


def test_user0001が新規コミュニティを正常に作成できる():
    """正常形テスト([post]/community/create)
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


def test_user0003がcomm0001にuser0001を新規追加しようとして正常に成功する():
    """正常形テスト([post]/communities/{community_id}/add/{target_user_id})
    1. コミュニティ1に"佐藤"がいないことの確認
    2. コミュニティ1の権限者であるuser0003がuser0001(佐藤)をコミュニティ1に登録するエンドポイントを叩く
    3. レスポンスのステータスコードとメッセージの確認
    4. コミュニティ1に"佐藤"が正常に追加されていることの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0001-0000-0000-0000-000000000000"
    target_user_id = "user0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "佐藤" not in target_community_users

    response = client.post(f"/communities/{community_id}/add/{target_user_id}")
    res_json = response.json()

    assert response.status_code == 200
    assert res_json["message"] == "佐藤さんがコミュニティ1に参加しました！"

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "佐藤" in target_community_users


def test_user0002がcomm0001にuser0001を新規追加しようとして403エラーを吐く():
    """異常形テスト([post]/communities/{community_id}/add/{target_user_id})
    1. コミュニティ1に"佐藤"がいないことの確認
    2. コミュニティ1の権限がないuser0002がuser0001(佐藤)をコミュニティ1に登録するエンドポイントを叩く
    3. レスポンスのステータスコードとメッセージの確認
    4. コミュニティ1に"佐藤"が追加されていないことの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0002
    community_id = "comm0001-0000-0000-0000-000000000000"
    target_user_id = "user0001-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "佐藤" not in target_community_users

    response = client.post(f"/communities/{community_id}/add/{target_user_id}")
    res_json = response.json()

    assert response.status_code == 403
    assert res_json["detail"] == "コミュニティに対してオーナー権限がありません."

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "佐藤" not in target_community_users


def test_user0003がcomm0001にuser0004を新規追加しようとして400エラーを吐く():
    """異常形テスト([post]/communities/{community_id}/add/{target_user_id})
    1. コミュニティ1に"田中"がいることの確認
    2. コミュニティ1の権限者であるuser0003がuser0004(田中)をコミュニティ1に登録するエンドポイントを叩く
    3. レスポンスのステータスコードとメッセージの確認
    4. コミュニティ1に"田中"が追加されていないことの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0001-0000-0000-0000-000000000000"
    target_user_id = "user0004-0000-0000-0000-000000000000"

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "田中" in target_community_users
        assert target_community_users.count("田中") == 1

    response = client.post(f"/communities/{community_id}/add/{target_user_id}")
    res_json = response.json()

    assert response.status_code == 400
    assert res_json["detail"] == "このユーザーは既にメンバー登録済みです."

    with Session(bind=engine) as db:
        target_community = db.query(models.Community)\
            .filter(models.Community.id == community_id)\
                .first()
        target_community_users = list(map(lambda x: x.name, target_community.user))
        assert "田中" in target_community_users
        assert target_community_users.count("田中") == 1


def test_user0003が存在しないコミュニティcomm0004にuser0001を新規追加しようとして404エラーを吐く():
    """異常形テスト([post]/communities/{community_id}/add/{target_user_id})
    1. user0003がuser0004(田中)を存在しないコミュニティcomm0004に登録するエンドポイントを叩く
    2. レスポンスのステータスコードとメッセージの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0004-0000-0000-0000-000000000000"
    target_user_id = "user0001-0000-0000-0000-000000000000"

    response = client.post(f"/communities/{community_id}/add/{target_user_id}")
    res_json = response.json()

    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidのコミュニティが見つかりませんでした."


def test_user0003がcomm0004に存在しないユーザーuser0000を新規追加しようとして404エラーを吐く():
    """異常形テスト([post]/communities/{community_id}/add/{target_user_id})
    1. user0003が存在しないユーザーuser0000をcomm0001に登録するエンドポイントを叩く
    2. レスポンスのステータスコードとメッセージの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0001-0000-0000-0000-000000000000"
    target_user_id = "user0000-0000-0000-0000-000000000000"

    response = client.post(f"/communities/{community_id}/add/{target_user_id}")
    res_json = response.json()

    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidのユーザーが見つかりませんでした."


def test_comm0001のオーナーであるユーザーuser0003がcomm0001の情報を正常に取得できる():
    """正常形テスト([get]/communities/{community_id})
    1. ログイン中のユーザーをuser0003に変更する
    2. コミュニティ1の情報をリクエストする
    3. レスポンスのステータスコードとメッセージの確認
    4. has_permissionがTrueであることの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0001-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}")
    res_json = response.json()

    assert response.status_code == 200
    assert res_json["name"] == "コミュニティ1"
    assert res_json["has_permission"] == True


def test_ユーザーuser0001がcomm0001の情報を正常に取得できる():
    """正常形テスト([get]/communities/{community_id})
    1. コミュニティ1の情報をリクエストする
    2. レスポンスのステータスコードとメッセージの確認
    3. has_permissionがFalseであることの確認
    """
    community_id = "comm0001-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}")
    res_json = response.json()

    assert response.status_code == 200
    assert res_json["name"] == "コミュニティ1"
    assert res_json["has_permission"] == False


def test_ユーザーuser0001が存在しないコミュニティcomm0000の情報をリクエストして404エラーを吐く():
    """正常形テスト([get]/communities/{community_id})
    1. コミュニティ1の情報をリクエストする
    2. レスポンスのステータスコードとメッセージの確認
    3. has_permissionがFalseであることの確認
    """
    community_id = "comm0000-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}")
    res_json = response.json()

    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidのコミュニティが見つかりませんでした."


def test_comm0001に属しているユーザーuser0003が同コミュニティでのアクセス可能本一覧を正常に取得できる():
    """正常形テスト([get]/communities/{community_id}/books)
    1. ログイン中のユーザーをuser0003に変更する
    2. コミュニティ1のアクセス可能本一覧情報をリクエストする
    3. レスポンスのステータスコードとメッセージの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0001-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}/books")
    res_json = response.json()

    assert response.status_code == 200
    assert len(res_json) == 3


def test_user0003が存在しないコミュニティucomm0000でのアクセス可能本一覧をリクエストして404エラーを吐く():
    """正常形テスト([get]/communities/{community_id}/books)
    1. ログイン中のユーザーをuser0003に変更する
    2. コミュニティ1のアクセス可能本一覧情報をリクエストする
    3. レスポンスのステータスコードとメッセージの確認
    """
    app.dependency_overrides[get_current_user] = override_get_current_user0003
    community_id = "comm0000-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}/books")
    res_json = response.json()

    assert response.status_code == 404
    assert res_json["detail"] == "指定されたidのコミュニティが見つかりませんでした."


def test_comm0001に属していないユーザーuser0001が同コミュニティでのアクセス可能本一覧をリクエストして403エラーを吐く():
    """正常形テスト([get]/communities/{community_id}/books)
    1. コミュニティ1のアクセス可能本一覧情報をリクエストする
    2. レスポンスのステータスコードとメッセージの確認
    """
    community_id = "comm0001-0000-0000-0000-000000000000"

    response = client.get(f"/communities/{community_id}/books")
    res_json = response.json()

    assert response.status_code == 403
    assert res_json["detail"] == "このコミュニティに対してアクセス権限がありません."