import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.database.db_connect import azure_db_connect
import dotenv
dotenv.load_dotenv(override=True)

if os.environ.get("IS_LOCAL_DB")=="true":
    SQLALCHEMY_DATABASE_URL = "sqlite:///mybrary.sqlite3"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    ###Azureへの接続################################
    server=os.environ.get("SERVER")
    database=os.environ.get("DATABASE")
    username=os.environ.get("USERNAME")
    password=os.environ.get("PASSWORD")
    
    engine=azure_db_connect(server,database,username,password)
    print(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()