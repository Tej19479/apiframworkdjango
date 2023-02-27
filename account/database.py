import mysql.connector
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

connection =mysql.connector.connect(
  host="localhost",
  port=3309,
  user="tej",
  password="Tej@123",
  database="fair2"
)

def selectdata(self):
   res = pd.read_sql(self,connection)
   return res


