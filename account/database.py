import mysql.connector
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
from mysql.connector import MySQLConnection, Error
from account.databaseconnection import dbconnection


def selectdata(self):
   print("ffffffnf")
   res = pd.read_sql(self,dbconnection["sql"])
   return res
 
def getsingledata(self):
        cursor = dbconnection["sql"].cursor()
        cursor.execute(self)
        row = cursor.fetchone()
        print("return one data query",row[0]) 
        return row[0]


def insertQuery(table, fields, data): 
   query= f"INSERT INTO {table} {fields} VALUES {data}"
   print("insert query",query)
   cursor = dbconnection["sql"].cursor()
   cursor.execute(query)
   dbconnection["sql"].commit()
   res1=cursor.lastrowid
   return res1

def getGenralQueryData(query):
    try:
      cursor = dbconnection["sql"].cursor()
      cursor.execute(query)
      rows =cursor.fetchall()
      a=[]
      cursor.close()
      return rows
    except:
       return False