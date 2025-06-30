#Program for reading the records of employee table--fetchmany(no. of records)
#SelectRecordsEx2.py
import cx_Oracle
def  selectrecords():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		cur.execute("select * from employee")
		#Process the records
		records=cur.fetchmany(4)
		for record in records:
			for val in record:
				print("\t{}".format(val),end=" ")
			print()
	except cx_Oracle.DatabaseError as db:
			print("Problem in DB:",db)

#main program
selectrecords()