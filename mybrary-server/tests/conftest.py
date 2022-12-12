import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pytest

from src.models import Base
from src.database.master_seeding import main

test_db_path = "sqlite:///mybrary_test.sqlite3"
engine = sqlalchemy.create_engine(test_db_path,connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from tests.dependencies import all_dependency_overrides


@pytest.fixture(
    scope="function",
    autouse=True
)
def setup_and_teardown():
    Base.metadata.create_all(bind=engine)
    main(engine=engine, all = True)
    all_dependency_overrides()
    yield
    os.remove("mybrary_test.sqlite3")
