#Non-ConstEx.py
class Student:
	def readstudvalues(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))

#main program
s=Student() # Object Creation--{}
print("Content of s = ",s.__dict__)
s.readstudvalues() # calling the instance method explicitly 
print("Content of s = ",s.__dict__)