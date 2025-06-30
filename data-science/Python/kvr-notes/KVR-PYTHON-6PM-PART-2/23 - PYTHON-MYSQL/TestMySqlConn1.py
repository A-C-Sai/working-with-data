#program for getting connection from mysql database
#TestMySqlConn1.py
import mysql.connector
con=mysql.connector.connect(host="localhost",
													user="root",
													passwd="root")
print("Python program obtains connection from mysql")
print("Type of con=",type(con))
