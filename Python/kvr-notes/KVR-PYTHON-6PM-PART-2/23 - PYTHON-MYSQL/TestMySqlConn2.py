#program for getting connection from mysql database
#TestMySqlConn2.py
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",
													user="root",
													passwd="root")
print("Python program obtains connection from mysql")
print("Type of con=",type(con))
