#Program for obtaining Col names
#SelectColNamesEx.py
import cx_Oracle
def  colnames():
	try:
		con=cx_Oracle.connect("system/manager@localhost/xe")
		cur=con.cursor()
		cur.execute("select * from employee")
		#Obtains Col Names
		coldata=cur.description
		print("-"*50)
		for cols in coldata:
			print(cols[0],end="\t")
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
colnames()