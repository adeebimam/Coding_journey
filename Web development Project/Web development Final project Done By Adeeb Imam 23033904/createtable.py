import mysql.connector, database
conn = database.getConnection()   #connection to DB
DB_NAME = 'WH_BOOKING'
TABLE_NAME = 'Guest'

TABLE_DESCRIPTION = f"""CREATE TABLE {TABLE_NAME} (
    Guest_ID INT PRIMARY KEY,
    Guest_FirstName VARCHAR(255),
    Guest_LastName VARCHAR(255),
    Guest_Email VARCHAR(255),
    Guest_Password VARCHAR(255)
)"""

     

if conn != None:    #Checking if connection is None
    if conn.is_connected(): #Checking if connection is established
        print('MySQL Connection is established')                          
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(DB_NAME)) #use database        
        dbcursor.execute(TABLE_DESCRIPTION) 
        print('Table {} created successfully.'.format(TABLE_NAME))               
        conn.close() #Connection must be closed
    else:
        print('DB connection error')
else:
    print('DBFunc error')



