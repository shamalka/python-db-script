#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
import MySQLdb
import sys
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "ptest1")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()
# execute the SQL query using execute() method.
cursor.execute ("select * from ward order by a limit 1")
# fetch all of the rows from the query
data = cursor.fetchall ()
# print the rows
print data

con = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "ptest2")
cursor2 = con.cursor ()
cursor2.execute ("select * from ward2 order by e limit 1")
data2 = cursor2.fetchall ()
print data2
if (data[0][0]!=data2[0][0]):
    print "true"
    cursor2.execute ("INSERT INTO ward2(e,f,g,h) VALUES(%s,%s,%s,%s)",(data[0][0],data[0][1],data[0][2],data[0][3]))
    con.commit()
else:
    print "false"

# close the cursor object
cursor.close ()
cursor2.close()
con.close()
# close the connection
connection.close ()
# exit the program

