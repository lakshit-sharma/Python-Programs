import mysql.connector

# Connect Database
db = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='lakshit')

# Prepare a Cursor Object
cursor = db.cursor()

# Create Query
sql = '''update Income
set Balance = 48904.65
where Serial_Number=15'''

try:
    cursor.execute(sql)         # Execute Query
    db.commit()                 # Commit your changes

except:
    print("Error")
    db.rollback()               # Rollback in case of any error

cursor.execute("select * from income")
for i in cursor:
    print(i)