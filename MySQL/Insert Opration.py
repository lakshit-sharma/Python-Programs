import mysql.connector

# Open database connection
db = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='lakshit')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# SQL query to INSERT a record into the database
#sql = '''insert into people values
#(27,"Martin","Sommer",67,"Madrid","Business"),(28,"Elizabeth","Brown",47,"London","Service")'''

try:
    # Execute sql command
    cursor.execute(sql)
    # Commit Changes n Database
    db.commit()
except:
    # Rollback if any error occured
    cursor.rollback()

cursor.execute('select * from people')
for i in cursor:
    print(i)

# disconnect from Server
db.close()