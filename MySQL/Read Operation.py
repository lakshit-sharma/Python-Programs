import mysql.connector

# Connect Database
db = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='lakshit')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Create query
sql = 'select * from income'

try:
    cursor.execute(sql)
    result= cursor.fetchall()           # fetches all the rows
    for i in result:
        print(i)
    cursor.execute(sql)
    r = cursor.fetchone()               # fetches only one row
    for i in r:
        print(i)
except:
    print('Unable to fetch the data')

# Disconnect Server
db.close()