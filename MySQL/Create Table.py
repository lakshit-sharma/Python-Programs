import mysql.connector

# Open database connection
db=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='lakshit')

# prepare a cursor object using cursor() method
cursor=db.cursor()

# Create table as per requirement
sql='''create table people
(First_Name varchar(20), Last_name varchar(20), 
Age int(5), Address varchar(20), Occupation varchar(20)'''

# Execute sql command
cursor.execute(sql)

# disconnect from Server
db.close()