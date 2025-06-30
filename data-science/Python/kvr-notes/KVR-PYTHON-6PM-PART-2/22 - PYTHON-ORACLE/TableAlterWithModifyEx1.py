#Program for altering the column sizes of Employee Table
#TableAlterWithModifyEx1.py
import cx_Oracle
def tablealterwithmodify():
	try:
		con=cx_Oracle.connect("system/manager@127.0.0.1/xe")
		cur=con.cursor()
		aq="alter table employee modify(eno  number(4),name varchar2(15))"
		cur.execute(aq)
		print("Employee Table altered--verify")
	except  cx_Oracle.DatabaseError as db:
		print("Problem in DB:",db)

#main program
tablealterwithmodify()