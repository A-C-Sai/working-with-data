#Program for obtaining Col names
#SelectrecordsWithColNames.py
import mysql.connector
def  tabledata():
	try:
		con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
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

	except mysql.connector.DatabaseError as db:
			print("Problem in DB:",db)

#main program
tabledata()