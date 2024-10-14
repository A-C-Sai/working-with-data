#Program for inserting the records in employee table in Oracle
#InsertRecordEx1.py
import cx_Oracle
def   insertrecord():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		iq="insert into employee values(50,'RT',6.6,'TCS')"
		cur.execute(iq)
		con.commit()
		print("{} Record inserted Sucessfully".format(cur.rowcount))
	except cx_Oracle.DatabaseError as kv:
		print("Problem in Db:",kv)

#main program
insertrecord()