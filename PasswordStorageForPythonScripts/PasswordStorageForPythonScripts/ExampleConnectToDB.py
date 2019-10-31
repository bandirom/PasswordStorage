import socket
from Client import SuperCacher


## Also you can add another data in virtual storage using:
#  cacher.set('Key', 'Value'))  #return True
## And get data from storage using:
#  cacher.get('Key') # return 'Value'

PORT = 4000 # Must be equal with PORT in Storage.py

def get_ip():  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP  # return your IP adress

cacher = SuperCacher(get_ip(), PORT)

server = 'localhost'
username = 'YourUserName'
password = cacher.get(username)
database = 'YourDB'

#### Connect to MS SQL server ### 

import pymssql
conn = pymssql.connect(host=server,user=username,password=password,database=database)

### Connect to PostgresSQL server ###

import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor
from psycopg2 import sql, Error

def Connect():
    return psycopg2.connect(dbname = database,
                            user = username, 
                            password = password,
                            host = server)

conn = Connect()
cursor = conn.cursor()