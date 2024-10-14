#Program for altering  Employee Table by adding new col name
#TableAlterWithAddEx1.py
import cx_Oracle
def  tablealteradd():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		aq="alter table employee add (cname varchar2(10))"
		cur.execute(aq)
		#OR cur.execute("alter table employee add (cname varchar2(10))")
		print("Employee Table altered--verify")
	except cx_Oracle.DatabaseError as k:
		print("Problem in Db:",k)


#main program
tablealteradd() # Function Call