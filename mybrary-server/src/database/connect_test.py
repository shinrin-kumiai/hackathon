import urllib
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

server="sinrin.database.windows.net"
database="sinrindb"
username="sinrin"
password="sonken625@@"

print("test")
odbc_connect=urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD=' + password)
print("test")
engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)
print("test")

with engine.connect() as conn:
    print("test")
    rs = conn.execute('SELECT @@VERSION as version')
    for row in rs:
        print(row['version'])

Base=declarative_base()

class Test(Base):
    __tablename__ = "testｓ"
    id = Column(Integer,primary_key=True,autoincrement=True)
    test=Column(String(14))
    test_score=Column(Integer)

Base.metadata.create_all(engine)
print("DBにカラムを追加しました")

Session=sessionmaker(bind=engine)
session=Session()

subjects=["math","english","science"]

for subject in subjects:
    session.add(Test(test=subject))
session.commit

print("DBに要素を追加する")