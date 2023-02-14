from collections import namedtuple
from django.db import connection



def getsingledata(self):
    with connection.cursor() as cursor:
        cursor.execute(self)
        row = cursor.fetchone()
        print("return one data query",row[0]) 
    return row[0]
 