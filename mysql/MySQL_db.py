#!/usr/bin/python

import MySQLdb
import getpass

pw = getpass.getpass('Pls. input DB password: ')

db_conn = MySQLdb.connect(host='localhost',user='root',passwd=pw,db='company')

cursor = db_conn.cursor()

line = cursor.execute('select * from employee_info')
print line

table_content = cursor.fetchall()

for l in table_content:
    print l

cursor.close()

db_conn.commit()
db_conn.close()
