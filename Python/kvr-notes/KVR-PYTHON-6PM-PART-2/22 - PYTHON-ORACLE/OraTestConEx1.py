#Program for obtaining the connection from Oracle database.
#OraTestConEx1.py
import cx_Oracle # Step-1
try:
	con=cx_Oracle.connect("system/manager1@127.0.0.1/XE")
	print("type of con=",type(con))
	print("Python Progrm got connection from Oracle DB")

except cx_Oracle.DatabaseError as db:
	print("Problem in DB:",db)
