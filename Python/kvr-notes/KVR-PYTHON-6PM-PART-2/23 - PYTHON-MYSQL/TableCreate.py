#program for creating employee table in MYSQL
#TableCreate.py
import mysql.connector
def createtable():
	try:
		con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
		cur=con.cursor()
		tq="create table employee (eno int primary key,name varchar(10) not null ,sal float not null,cname varchar(10) not null)"
		cur.execute(tq)
		print("table created successfully in mysal")
	except mysql.connector.DatabaseError as db:
		print("Problem in Db:",db)

#main program
createtable()

#NOTE:  u do altering  table with modify and add options