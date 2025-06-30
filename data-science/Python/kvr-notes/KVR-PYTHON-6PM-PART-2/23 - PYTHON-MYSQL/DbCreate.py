#program for getting connection from mysql database
#DbCreate.py
import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",user="root",passwd="root")
    cur=con.cursor()
    dc="create database hyd"
    cur.execute(dc)
    print("Database Created Sucessfully in MYSQL")
except mysql.connector.DatabaseError as db:
	print("Problem in Db:",db)