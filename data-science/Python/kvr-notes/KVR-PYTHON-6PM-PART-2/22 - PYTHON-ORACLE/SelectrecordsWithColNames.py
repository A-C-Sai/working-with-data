#Program for obtaining Col names
#SelectrecordsWithColNames.py
import cx_Oracle
def  tabledata():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		tname=input("Enter the table name:")
		cur.execute("select * from %s" %tname)
		#Obtains Col Names
		coldata=cur.description
		print("-"*50)
		for cname in [cols[0] for cols in cur.description]:
			print(cname,end="\t")
		print()
		print("-"*50)
		#Obtain records
		records=cur.fetchall()
		for record in records:
			for val in record:
				print("{}".format(val),end="\t")
			print()
		print("-"*50)

	except cx_Oracle.DatabaseError as db:
			print("Problem in DB:",db)

#main program
tabledata()