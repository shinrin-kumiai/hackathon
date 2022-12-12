import os
import shutil
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
    os.makedirs("tests/tmp", exist_ok=True)
    main(engine=engine, all = True)
    all_dependency_overrides()
    yield
    shutil.rmtree('tests/tmp/')
    os.remove("mybrary_test.sqlite3")
