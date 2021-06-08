import mysql.connector
# Connect to Database
db = mysql.connector.connect(host='localhost',user='root',passwd='admin')

cursor = db.cursor()            # Initialise cursor

sql = 'show databases'          # Write query here

cursor.execute(sql)             # Execute query

for i in cursor:
    print(i)
