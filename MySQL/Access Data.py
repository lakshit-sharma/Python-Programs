import mysql.connector


class people:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='lakshit')
        print('created')

    def access_elements(self):
        query = '''select ID,First_Name,Age from people'''
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print('Sr.No. - ', row[0])
            print('Name - ', row[1])
            print('age - ', row[2])
            print('\n------')
        return row


show = people()
show.access_elements()
