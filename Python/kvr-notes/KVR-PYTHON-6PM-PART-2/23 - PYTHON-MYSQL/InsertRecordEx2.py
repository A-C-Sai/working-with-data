#Program for inserting the records in employee table in MYSQL by reading employee values fromk Key board
#InsertRecordEx2.py
import mysql.connector
def   insertrecord():
	try:
		con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
		cur=con.cursor()
		#Accept employee values
		empno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		sal=float(input("Enter Employee Salary:"))
		cname=input("Enter Employee Comp Name:")
		#Design  and execute the query
		dq="insert into employee values(%d,'%s',%f,'%s')"
		cur.execute(dq %(empno,ename,sal,cname))
		#OR cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,ename,sal,cname))
		con.commit()
		print("%d Employee Record Inserted Sucessfully" %cur.rowcount)
	except mysql.connector.DatabaseError as kv:
		print("Problem in Db:",kv)
	except ValueError:
		print("Don't Enter alnums,strs,symbols for empno and salary")
	except:
		print("Oooops ,wome thing went wrong")
#main program
insertrecord()