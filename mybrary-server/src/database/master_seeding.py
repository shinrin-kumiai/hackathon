from fire import Fire

from src.database.database import engine
from src.database.seedings.book import seeding_to_book
from src.database.seedings.user import seeding_to_user
from src.database.seedings.community import seeding_to_community
from src.database.seedings.user_community import seeding_to_user_community
from src.database.seedings.user_book import seeding_to_user_book
from src.database.seedings.community_book import seeding_to_community_book
from src.database.seedings.user_book_state_log import seeding_to_user_book_state_log
from src.database.seedings.community_book_state_log import seeding_to_community_book_state_log
from src.database.seedings.state import seeding_to_state


def main(
            engine = engine, 
            book: bool = True,
            user: bool = True,
            community: bool = True,
            user_community: bool = True,
            user_book: bool = True,
            community_book: bool = True,
            user_book_state_log: bool = True,
            community_book_state_log: bool = True,
            state: bool = True,
        ) -> None:
    """引数でTrueと指定されたテーブルに対するseedingファイルを実行する

    Args:
        engine (<class 'sqlalchemy.engine.base.Engine'>): databaseからimportしたengine
        book (bool, optional): Defaults to True.
        user (bool, optional): Defaults to True.
        community (bool, optional): Defaults to True.
        user_community (bool, optional): Defaults to True.
        user_book (bool, optional): Defaults to True.
        community_book (bool, optional): Defaults to True.
        user_book_state_log (bool, optional): Defaults to True.
        community_book_state_log (bool, optional): Defaults to True.
        state (bool, optional): Defaults to True.
    """
    if book: seeding_to_book(engine = engine)
    if user: seeding_to_user(engine = engine)
    if community: seeding_to_community(engine = engine)
    if user_community: seeding_to_user_community(engine = engine)
    if user_book: seeding_to_user_book(engine = engine)
    if community_book: seeding_to_community_book(engine = engine)
    if user_book_state_log: seeding_to_user_book_state_log(engine = engine)
    if community_book_state_log: seeding_to_community_book_state_log(engine = engine)
    if state: seeding_to_state(engine = engine)


if __name__ == "__main__":
    Fire(main)