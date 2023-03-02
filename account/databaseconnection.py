from dotenv import load_dotenv
import os
import mysql.connector 
load_dotenv()

def mysqlPoolConnect(host, user, port, password, database):
    try:
      conPool = mysql.connector.connect(
        host=host,
        port = port,
        user = user,
        password = password,
        database = database,
       )
    except mysql.Error as e:
      print(e)
      return e
    return conPool
dbconnection={ 
  "sql":mysqlPoolConnect(os.environ["host"],os.environ["USER"],os.environ["port"],os.environ["password"],os.environ["database"])
 }