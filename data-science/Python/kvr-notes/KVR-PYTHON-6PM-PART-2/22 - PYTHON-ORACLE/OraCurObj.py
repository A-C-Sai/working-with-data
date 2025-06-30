#Program for creating cursor object
#OraCurObj.py
import cx_Oracle
try:
	con=cx_Oracle.connect("system/manager@localhost/xe")
	print("\nConnection  Sucessful")
	cur=con.cursor()
	print("\ntype of cur=",type(cur)) # <class 'cx_Oracle.Cursor'>
	print("Cursor object  created")
except cx_Oracle.DatabaseError as db:
	print("Problem in DB:",db)
