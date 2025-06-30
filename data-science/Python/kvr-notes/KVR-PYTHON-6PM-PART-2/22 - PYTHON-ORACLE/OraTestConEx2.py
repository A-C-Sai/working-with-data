#Program for obtaining the connection from Oracle database.
#OraTestConEx2.py
import cx_Oracle # Step-1
try:
	con=cx_Oracle.connect("system/manager@localhost/XE")
	print("type of con=",type(con))
	print("Python Progrm got connection from Oracle DB")

except cx_Oracle.DatabaseError as db:
	print("Problem in DB:",db)
