#Student.py---File Name and module name
import College as c
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