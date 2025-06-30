#Program for reading the records of employee table--fetchone()
#SelectRecordsEx1.py
import cx_Oracle
def  selectrecords():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		sq="select * from employee"
		cur.execute(sq)
		#Process the records
		print("-"*50)
		while(True):
			record=cur.fetchone()
			if(record!=None):
				for val in record:
					print("\t{}".format(val),end=" ")
				print()
			else:
				print("-"*50)
				break
	
	except cx_Oracle.DatabaseError as db:
			print("Problem in DB:",db)

#main program
selectrecords()