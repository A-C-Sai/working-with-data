#Program for deleting records in employee table in Oracle based employee number
#DeleteRecordEx1.py
import cx_Oracle
def   deleterecord():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		dq="delete from employee where eno=40"
		cur.execute(dq)
		con.commit()
		if(cur.rowcount==0):
			print("Record Does not exist:")
		else:
			print("{} record deleted sucessfully".format(cur.rowcount))
	except cx_Oracle.DatabaseError as kv:
		print("Problem in Db:",kv)

#main program
deleterecord()