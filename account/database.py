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
     
