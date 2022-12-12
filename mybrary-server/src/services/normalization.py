from fastapi import HTTPException

def isbn_normalize(isbn: str) -> str:
    """ハイフン区切りのisbnコードを正規化(ハイフン削除)する関数

    Args:
        isbn (str): isbnコード

    Returns:
        str: 正規化後のisbnコード
    """
    return "".join(list(map(str, isbn.split("-"))))


def toggle_isbn10_and_isbn13(isbn: str) -> str:
    """isbn10とisbn13を入れ替える関数

    Args:
        isbn (str): isbn10 or isbn13

    Raises:
        HTTPException: isbnコードが規定の形式以外だった場合にエラーを吐く

    Returns:
        str: isbn10 or isbn13
    """
    if len(isbn) == 10:
        return f"978{isbn}"
    elif len(isbn) == 13:
        return isbn[3:]
    else:
        raise HTTPException(
            status_code=400,
            detail="The isbn code contains some mistake."
        )