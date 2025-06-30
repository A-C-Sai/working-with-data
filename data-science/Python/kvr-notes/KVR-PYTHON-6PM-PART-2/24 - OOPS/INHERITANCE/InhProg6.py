#Wrt a Python program wch will implement the following
#let us assume there exist a university wch contains University name and it's location, accept and display University details. Let us assume there exist a college wch contains College name and it's location, accept and display college details along with University details. Let us assume there exist a student wch contains student number,Student name and course persuing, accept and display students details along with University and college details
#InhProg6.py
class Univ:
	def getUnivDet(self):
		self.uname=input("Enter University Name:")
		self.uloc=input("Enter University Location:")
	def dispUnivDet(self):
		print("-"*50)
		print("University Name:{}".format(self.uname))
		print("University Location:{}".format(self.uloc))
		print("-"*50)
class College(Univ):
	def getCollDet(self):
		self.cname=input("Enter College Name:")
		self.cloc=input("Enter College Location:")
	def dispCollDet(self):
		print("College Name:{}".format(self.cname))
		print("College Location:{}".format(self.cloc))
		print("-"*50)

class Student(College):
	def getStudDet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
	def dispStudDet(self):
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)

#main program
so=Student()
so.getStudDet()
so.getCollDet()
so.getUnivDet()
so.dispUnivDet()
so.dispCollDet()
so.dispStudDet()
