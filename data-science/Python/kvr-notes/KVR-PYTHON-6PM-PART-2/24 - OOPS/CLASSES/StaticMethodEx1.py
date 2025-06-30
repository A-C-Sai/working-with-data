#Program for demonstrating Static Methods
#StaticMethodEx1.py
class Student: 
	def  readstuddata(self):
		self.sno=int(input("Enter Student Number:"))
		self.name=input("Enter Student Name:")
		self.cname=input("Enter Student College Name:")
	
class Employee:
	def readempdata(self):
		self.sno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.cname=input("Enter Employee Comp Name:")
		self.esal=float(input("Enter Employee Salary:"))
	
class Teacher:
	def readteacherdata(self):
		self.tno=int(input("Enter Teacher Number:"))
		self.tname=input("Enter Teacher Name:")
		self.subname=input("Enter Teacher Subject:")

class Hyd:
	@staticmethod
	def  dispobjectdata(obj):
		print("-"*50)
		for k,v in obj.__dict__.items():
			print("\t{}\t{}".format(k,v))
		print("-"*50)	

#main program
s=Student()  # Student Object Creation
e=Employee() # Employee Object Creation
t=Teacher() # Teacher Object creation
#read stdent object data
s.readstuddata() # calling Instance Method
#read employee object data
e.readempdata() # calling Instance Method
#read teacher object data
t.readteacherdata() # calling Instance Method
#display student data
print("Student details")
Hyd.dispobjectdata(s)
#isplay emp data
print("Employee details")
Hyd.dispobjectdata(e)
#isplay teacher data
print("Teacher details")
Hyd.dispobjectdata(t)