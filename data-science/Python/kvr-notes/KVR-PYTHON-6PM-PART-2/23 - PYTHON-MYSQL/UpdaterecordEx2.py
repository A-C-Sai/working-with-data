#UpdaterecordEx2.py
import mysql.connector
def updaterecord():
	while(True):
		try:
			con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
			cur=con.cursor()
			#accept the employee number and company name
			empno=int(input("Enter Employee Number:"))
			cmpname=input("Enter Company name for updation:")
			#prepare and execute the query
			uq="update employee set sal=sal+sal*20/100,cname='%s' where eno=%d"
			cur.execute(uq %(cmpname,empno))
			con.commit()
			if(cur.rowcount!=0):
				print("{} Record(s) Updated--Verify".format(cur.rowcount))
			else:
				print("Employee Record Does not exist")
			print("-"*50)
			ch=input("Do u want to Update another Record(yes/no):")
			if(ch.lower()=="no"):
				break
		except mysql.connector.DatabaseError as db:
			print("Problem in DB:",db)
		except ValueError:
			print("Don't enter alnums,strs and symbols for employee Number:")
		except:
			print("Some thing went wrong!!!")

#main program
updaterecord()
