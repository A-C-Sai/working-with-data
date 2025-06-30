#Program for deleting records in employee table in Oracle based employee number
#DeleteRecordEx2.py
import mysql.connector
def   deleterecord():
	while(True):
		try:
			con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="batch6pm")
			cur=con.cursor()
			#accpet the emp number from KBD
			empno=int(input("Enter Employee Number:"))
			cur.execute("delete from employee where eno=%d" %empno)
			con.commit()
			if(cur.rowcount==0):
				print("Record Does not exist:")
			else:
				print("{} record deleted sucessfully".format(cur.rowcount))
			print("-"*50)
			ch=input("Do u want to delete another record(yes/no):")
			if(ch.lower()=="no"):
				print("\nThx for using this program")
				break
		except mysql.connector.DatabaseError as kv:
			print("Problem in Db:",kv)
		except ValueError:
				print("Don't Enter alnums,strs,symbols for empno")
		except:
				print("Oooops ,wome thing went wrong")

#main program
deleterecord()