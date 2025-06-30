#Student.py---File Name and module name
import College as c
import mysql.connector
class Student(c.College):
	def getStudDet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
		self.getCollDet()

	def dispStudDet(self):
		self.dispUnivDet()
		self.dispCollDet()
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)
	def  storeStudCollUnivData(self):
		try:
			con=mysql.connector.connect(host="localhost", user="root",passwd="root",database="batch6pm")
			cur=con.cursor()
			iq="insert into univstu values(%d,'%s','%s','%s','%s','%s','%s' ) "
			cur.execute(iq %(self.sno,self.sname,self.crs,self.cname,self.cloc,self.uname,self.uloc))
			con.commit()
			print("{} Student Record Inserted Sucessfully".format(cur.rowcount))
		except mysql.connector.DatabaseError as db:
			print("Problem in DB:",db)


