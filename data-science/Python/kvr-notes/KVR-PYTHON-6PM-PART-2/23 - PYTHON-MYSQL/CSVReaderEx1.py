#Program for reading from CSV file by using csv module
#CSVReaderEx1.py
import csv
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
	cur=con.cursor()
	dq="insert into employee values(%d,'%s',%f,'%s')"
	with open("student.csv","r") as fp:
		csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>

		for record in csvr:
			eno=int(record[0])
			ename=record[1]
			sal=float(record[2])
			cname=record[3]
			cur.execute(dq %(eno,ename,sal,cname))
			con.commit()
			print("Row Inserted")
except FileNotFoundError:
	print("CSV File does not exist")
except mysql.connector.DatabaseError as kv:
			print("Problem in Db:",kv)
except ValueError:
			print("Don't Enter alnums,strs,symbols for empno and salary")

"""
for val in record:
				print("\t{}".format(val),end="")
			print()
"""