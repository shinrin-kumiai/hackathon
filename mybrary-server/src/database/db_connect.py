import os
import dotenv
import urllib
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship,Session

dotenv.load_dotenv(override=True)


# if os.environ.get("IS_LOCAL_DB")=="true":
#     SQLALCHEMY_DATABASE_URL = "sqlite:///mybrary.sqlite3"

#     engine = create_engine(
#         SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#     )
# else:
#     ###Azureへの接続################################
#     server=os.environ.get("SERVER")
#     database=os.environ.get("DATABASE")
#     username=os.environ.get("USERNAME")
#     password=os.environ.get("PASSWORD")
def azure_db_connect(server,database,username,password):

    odbc_connect=urllib.parse.quote_plus(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)

    with engine.connect() as conn:
        #print(vars(conn.engine))
        rs = conn.execute('SELECT @@VERSION as version')
        for row in rs:
            print(row['version'])

    print(row['version'])
    print("接続に成功しました")

    return engine

# if __name__ == "__main__":
#     azure_db_connect(server=os.environ.get("SERVER"),
#                     database=os.environ.get("DATABASE"),
#                     username=os.environ.get("USERNAME"),
#                     password=os.environ.get("PASSWORD"))

################################################

####testテーブルの作成#####
# Base=declarative_base()
# #生徒テーブル
# class Student(Base):
#     __tablename__ = "students_test"
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     name = Column(String(255))
#     class_name=Column(String(14))
#     tall=Column(Integer)
#     weight=Column(Integer)
#     test=relationship("Test",back_populates="students")

# #テーブル科目と点数テーブル
# class Test(Base):
#     __tablename__ = "test_subject_data"
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     student_id=Column(Integer,ForeignKey("students_test.id"))
#     students=relationship("Student",back_populates="test")
#     test_score=Column(Integer)
#     test_subject=Column(String(255))

# print("DBにテーブルを追加")


# Base.metadata.create_all(engine)
#SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

# session=Session()
# def get_db() -> SessionLocal:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#db=Depends(get_db)

# Session = sessionmaker(bind=engine)
# session = Session()
# print(f"engineの中身を確認{engine}")

# with Session(bind=engine) as db:
#     add_student_data=(Student(
#                         name = "mori",
#                         class_name="2",
#                         tall=173,
#                         weight=60,))

#     db.add(add_student_data)
#     db.commit()


        #subjects=["math","english","science"]
        # add_subject=Test(test_subject="math")
        # db.add(add_subject)

        # add_test_score=Test(test_score=100)
        # db.add(add_test_score)
        
    

#print("DBに要素を追加しました")
#conn.close()
# for subject in subjects:
#     print(subject)
#     session.add(Test(test=subject))
#     session.commit
