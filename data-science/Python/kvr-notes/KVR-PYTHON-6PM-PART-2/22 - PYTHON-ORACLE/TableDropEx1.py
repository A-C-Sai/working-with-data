#Program for altering  Employee Table by adding new col name
#TableDropEx1.py
import cx_Oracle
def  tabledrop():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		cur.execute("drop table student")
		print("Student Table droped--verify")
	except cx_Oracle.DatabaseError as k:
		print("Problem in Db:",k)


#main program
tabledrop() # Function Call