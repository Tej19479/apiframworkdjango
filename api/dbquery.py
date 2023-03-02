from collections import namedtuple
from django.db import connection
import mysql.connector



def getsingledata(self):
    with connection.cursor() as cursor:
        cursor.execute(self)
        row = cursor.fetchone()
        print("return one data query",row[0]) 
    return row[0]

def getselectdata(self):
    with connection.cursor() as cursor:
        cursor.execute(self)
        from_db = []
        result = cursor.fetchall()
        print("result7777777777",result)

        for results in result:
            print("result",results)
            from_db.append(result)
        print ("from_db33333",from_db)  
        return from_db
 