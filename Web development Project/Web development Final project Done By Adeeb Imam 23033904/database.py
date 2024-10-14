import mysql.connector
from mysql.connector import errorcode

# MYSQL CONFIG VARIABLES
hostname = "localhost"
username = "root"
passwd = "12345678"
database = "WH_BOOKING"

def getConnection():
    try:
        conn = mysql.connector.connect(
            host=hostname,
            user=username,
            password=passwd,
            database=database
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Username or password is incorrect')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)
    else:
        return conn
