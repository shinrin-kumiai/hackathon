import dotenv
import urllib
from sqlalchemy import create_engine

dotenv.load_dotenv(override=True)

def azure_db_connect(server,database,username,password):

    odbc_connect=urllib.parse.quote_plus(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)

    with engine.connect() as conn:
        rs = conn.execute('SELECT @@VERSION as version')
        for row in rs:
            print(row['version'])

    print(row['version'])
    print("接続に成功しました")

    return engine