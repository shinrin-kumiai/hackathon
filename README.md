# Mybrary
ハックツハッカソン用リポジトリです。


# Skills
[![Our Skills](https://skillicons.dev/icons?i=html,css,react,vite,mui,fastapi,sqlite,azure&theme=light)](#Skills)


# 環境変数について
- 本アプリで使用する環境変数は`.env`ファイルから取得される.
- Github上には`.env.sample`としてアップロードしてあるためコピーして`.env`ファイルを作成し、必要な内容を記述すること.

#### .envの中身
```
#IS_LOCAL_PC=trueでsqlite3にfalseでAzureに接続される
IS_LOCAL_DB=false
SERVER=Azureのサーバー名.database.windows.net
DATABASE=データベース名
USERNAME=ユーザー名
PASSWORD=パスワード
#サーバー関連設定
THUMBNAIL_SAVE_PATH = 
#テスト関連設定
NDLAPI_RELATED_TEST_EXECUTE_IS = true
```

# 作成が必要なディレクトリについて
- `src`ディレクトリ直下に以下のような構成で`thumbnails`という空ディレクトリを作成すること.
```
src
└ assets/
　 ├ default/
　 └ thumbnails/ <-
```

# DB操作（SQLite and Azure DB）
## DB作成
以下のコマンドを`mybrary-server`ディレクトリ内で実行する
```bash
py -m src.database.db_handler --db_create=True
```
## DB削除
以下のコマンドを`mybrary-server`ディレクトリ内で実行する
```bash
py -m src.database.db_handler --db_delete=True
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
py -m src.database.master_seeding --book=True
```
- userテーブルとcommunityテーブルにseedingをする場合
```bash
py -m src.database.master_seeding --user=True --community=True
```
- 全テーブルに対してseedingを行う場合
```bash
py -m src.database.master_seeding --all=True
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

## record handler
### - delete all records
以下のコマンドを`mybrary-server`ディレクトリ内で実行すると、指定したテーブルの全レコードが削除される
```bash
py -m src.database.record_handler --Option=Param

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
py -m src.database.master_seeding --book=True
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
>### - [post] /user/books/register/
>- ユーザー所有の本を登録するエンドポイント
>#### -- クエリパラメータ
>|Query-param|detail|
>|:----:|:----|
>|isbn|登録対象の本のisbn13を指定|
>#### --レスポンスモデル
>`schemas.UserBookInfo`
>#### -- テスト
>国立国会図書館APIへの開発時のアクセス数を最低限に抑えるため、このエンドポイントへのテストは`.env`ファイル内の>`NDLAPI_RELATED_TEST_EXECUTE_IS`をtrue(小文字に注意)にした場合にのみ実行される.


>### - [get] /user/books
>- ユーザー所有本の一覧を取得するエンドポイント
>#### -- クエリパラメータ
>|Query-param|detail|
>|:----:|:----|
>|page|取得したいページ数|
>|size|1ページで取得したい要素数|
>#### --レスポンスモデル
>`list[schemas.UserBookInfo]`


>### - [get] /user/books/{book_id}
>- 本の所有idによって指定された本の情報を返すエンドポイント
>#### --パスパラメータ
>|Path-param|detail|
>|:----:|:----|
>|book_id|取得対象の本のid|
>#### --レスポンスモデル
>`schemas.UserBookInfo`


>### - [delete] /user/books/{book_id}
>- 本の所有idによって指定された本の削除を行うエンドポイント
>#### --パスパラメータ
>|Path-param|detail|
>|:----:|:----|
>|book_id|削除対象の本のid|
>#### 制限
> - 指定された本の所有者のみがこのエンドポイントへのアクセス権限を有する.


> ### - [get] /user/communities
> - ログイン中のユーザーが所属しているコミュニティの情報を配列で返すエンドポイント
> #### --レスポンスモデル
> `schemas.CommunityInfo`


## communityカテゴリ
>### - [post] /community/create
>- 新規コミュニティを作成するエンドポイント
>#### リクエストボディモデル
>`schemas.CommunitySetupInfo`
>#### レスポンスモデル
>`schemas.CommunityInfo`

>### - [post] /communities/{community_id}/add/{target_user_id}
>- コミュニティにユーザーを登録するエンドポイント
>#### -- パスパラメータ
>|Path-param|detail|
>|:----:|:----|
>|community_id|登録対象コミュニティのid|
>|target_user_id|登録対象ユーザーのid|

>### - [get] /communities/{community_id}
>- コミュニティidで指定したコミュニティの情報を取得するエンドポイント
>#### レスポンスモデル
>`schemas.CommunityInfo`


## assetsカテゴリ
>### - [get] /assets/thumbnails/{isbn}
>- isbn13によって指定された本の書影を取得するエンドポイント
>- 指定されたisbnコードの書影が存在しなかった場合はThumbnail-No-Found画像がレスポンスされる.
>#### -- パスパラメータ
>|Path-param|detail|
>|:----:|:----|
>|isbn|取得対象の本のisbn13|
>#### -- テスト
>国立国会図書館APIへの開発時のアクセス数を最低限に抑えるため、このエンドポイントへのテストは`.env`ファイル内の`NDLAPI_RELATED_TEST_EXECUTE_IS`をtrue(小文字に注意)にした場合にのみ実行される.