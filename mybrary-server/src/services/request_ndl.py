from fastapi import HTTPException
import xml.etree.ElementTree as ET
import requests


def get_xml_data_from_ndl(isbn: str) -> str:
    """国立国会図書館APIから書誌情報をxmlで取得してくる関数

    Args:
        isbn (str): isbn10 or isbn13

    Returns:
        str: xmlデータ
    """
    opensearch_url = 'https://iss.ndl.go.jp/api/opensearch'
    params = {
        'dataset': 'opac-ISBN',
        'isbn': isbn,
        'format': 'xml'
    }
    xml_data = requests.get(url=opensearch_url, params=params).text
    return xml_data


def xml_to_json(xml_data: str) -> str | None:
    """xmlデータを渡すことで書誌情報をjsonで返す関数

    Args:
        xml_data (str): 国立国会図書館APIから取得したxmlデータ

    Returns:
        str: json形式で書誌情報を返す
    """
    root = ET.fromstring(xml_data)
    try:
        link = root.findall('channel')[0].findall('item')[0].findall('link')[0].text
        res_json = requests.get(f"{link}.json")
        return res_json.json()
    except:
        return None


def get_thumbnail_from_ndl(isbn: str, thumbnail_save_path: str) -> None:
    """国立国会図書館の書影APIからisbn13で指定された本の書影を取得し保存する関数

    Args:
        isbn (str): 書影を取得したい本のisbn13コード
        thumbnail_save_path (str): 書影の保存先パス

    Returns:
        str: 画像ファイルの保存先パス
    """
    try:
        thumbnail_url = "https://iss.ndl.go.jp/thumbnail"
        res = requests.get(f"{thumbnail_url}/{isbn}")

        if res.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="書影が見つかりませんでした."
            )

        img_data = res.content
        img_path = f"{thumbnail_save_path}/{isbn}.jpg"

        with open(img_path, "wb") as img:
            img.write(img_data)
        
        return img_path

    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail
        )
    except:
        raise HTTPException(
            status_code=400,
            detail="書影の取得・保存に失敗しました."
        )