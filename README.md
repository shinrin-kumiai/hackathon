# Mybrary
ハックツハッカソン用リポジトリです。


# 環境変数について
- 本アプリで使用する環境変数は`.env`ファイルから取得される.
- Github上には`.env.sample`としてアップロードしてあるためコピーして`.env`ファイルを作成し、必要な内容を記述すること.


# DB作成（仮DB:SQLite）
## SQLiteファイル(Table)作成
以下のコマンドを`mybrary-server`ディレクトリ内で実行する
```bash
py -m src.models
```
## Seedings
### - **commands**
以下のコマンドを`mybrary-server`ディレクトリ内で実行する
```bash
py -m src.seeding.master_seeding --Option=Param

#Option: 既定のOption属性値
#Param: bool
```
### - Option属性設定
seeding実行時のOption属性のDefault値は以下の通り
|Option|Default Params|Details|
|:----|:----:|:----|
|all|False|全テーブルへのseeding|
|book|False|本が10冊登録されます|
|user|False|ユーザーが8名登録されます|
|community|False|コミュニティが3グループ作成されます|
|user_community|False|ユーザーとコミュニティが紐づきます|
|user_book|False|ユーザーと本が紐づきます|
|community_book|False|コミュニティと本が紐づきます|
|user_book_state_log|False|ユーザー所有の本が全て"貸出可能"状態になります|
|community_book_state_log|False|コミュニティ所有の本が全て"貸出可能"状態になります|
|state|False|本のステータス一覧が登録されます|

### - Option属性設定の例
- bookテーブルにのみseedingをする場合
```bash
py -m src.master_seeding --book=True
```
- userテーブルとcommunityテーブルにseedingをする場合
```bash
py -m src.master_seeding --user=True --community=True
```
- 全テーブルに対してseedingを行う場合
```bash
py -m src.master_seeding --all=True
```

### - サンプルデータにおけるuuid
以下のテーブルでは固有idにuuid4を使用するため、サンプルデータでは頭8桁で判断できるようにしている\
uuid4では、"00000000-0000-0000-0000-000000000000"のような36桁のidが割り振られる
|テーブル名|表記|
|:----|:----|
|book|book0000-...|
|user|user0000-...|
|community|comm0000-...|
|user_book|usbk0000-...|
|community_book|cmbk0000-...|


### - Seedingによって作られるデータ構造
全テーブルSeeding後のデータ構造は以下の通り
#### @ **ユーザーとコミュニティ**
|ユーザー|コミュニティ1|コミュニティ2|
|:----:|:----:|:----:|
|user0001|-|-|
|user0002|-|-|
|user0003|comm0001|-|
|user0004|comm0001|-|
|user0005|comm0002|-|
|user0006|comm0002|-|
|user0007|comm0003|-|
|user0008|comm0002|comm0003|

#### @ **ユーザーと本**
|ユーザー|本1|本2|本3|
|:----:|:----:|:----:|:----:|
|user0001|-|-|-|
|user0002|book0001|book0002|book0003|
|user0003|book0004|book0005|book0006|
|user0004|-|-|-|
|user0005|book0007|book0008|book0009|
|user0006|book0010|book0001|book0002|
|user0007|book0006|book0007|book0008|
|user0008|book0003|comm0004|book0005|

#### @ **コミュニティと本**
|コミュニティ|本1|本2|本3|本4|
|:----:|:----:|:----:|:----:|:----:|
|comm0001|-|-|-|-|
|comm0002|book0001|book0002|book0003|book0004|
|comm0003|book0005|book0006|book0007|book0008|

#### @ **コミュニティごとのアクセス可能冊数**
|コミュニティ|所属ユーザー|book0001|book0002|book0003|book0004|book0005|book0006|book0007|book0008|book0009|book0010|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|comm0001|user0003, user0004|0|0|0|1|1|1|0|0|0|0|
|comm0002|user0005, user0006, user0008|2|2|2|2|1|0|1|1|1|0|
|comm0003|user0007, user0008|0|0|1|1|2|2|2|2|0|0|

## database handler
### - delete all records
以下のコマンドを`mybrary-server`ディレクトリ内で実行すると、指定したテーブルの全レコードが削除される
```bash
py -m src.seeding.db_handler --Option=Param

#Option: 既定のOption属性値
#Param: bool
```

### - Option属性設定
db_handler実行時のOption属性のDefault値は以下の通り
|Option|Default Params|Details|
|:----|:----:|:----|
|all|False|全テーブルを指定|
|book|False|bookテーブルを指定|
|user|False|userテーブルを指定|
|community|False|communityテーブルを指定|
|user_community|False|user_communityテーブルを指定|
|user_book|False|user_bookテーブルを指定|
|community_book|False|community_bookテーブルを指定|
|user_book_state_log|False|user_book_state_logテーブルを指定|
|community_book_state_log|False|community_book_state_logテーブルを指定|
|state|False|stateテーブルを指定|

### - Option属性設定の例
- 本のみ登録
```bash
py -m src.master_seeding --book=True
```


# フロントエンドサーバーの起動
#### 【開発時】
以下のコマンドを`mybrary-front`ディレクトリ内で実行する
```bash
npm run dev
```

# バックエンドサーバーの起動
#### 【開発時】
以下のコマンドを`mybrary-server`ディレクトリ内で実行する
```bash
py -m uvicorn src.main:app --reload
```

# テストの実行
#### 【ディレクトリ構成】
- `pytest`によるテスト環境を構築している
- 以下のようなディレクトリ構成になっている
```
tests/
├ integration/
│ ├ __init__.py
│ └ //integration test files
├ unit/
│ ├ __init__.py
│ └ //unit test files
├ __init__.py
├ conftest.py
└ dependencies.py
```
- `integration`ディレクトリは統合テストを記述
- `unit`ディレクトリは単体テストを記述
- `dependencies.py`にはテスト時にoverrideする関数を記述

#### 【テストの実行】
- テストコードは以下のコマンドで実行できる

`tests`ディレクトリ内の全てのテスト実行
```bash
py -m pytest tests/
```

`tests/integration`ディレクトリ内の全てのテスト実行
```bash
py -m pytest tests/integration/
```

`tests/integration/test_sample.py`ファイル内の全てのテスト実行
```bash
py -m pytest tests/integration/test_sample.py
```


# エンドポイント一覧
## userカテゴリ
### - /user/books/register/
- ユーザー所有の本を登録するエンドポイント

#### -- クエリパラメータ
|Query-param|detail|
|:----:|:----|
|isbn|登録対象の本のisbn13を指定|

#### -- テスト
国立国会図書館APIへの開発時のアクセス数を最低限に抑えるため、このエンドポイントへのテストは`.env`ファイル内の`NDLAPI_RELATED_TEST_EXECUTE_IS`をtrue(小文字に注意)にした場合にのみ実行される.