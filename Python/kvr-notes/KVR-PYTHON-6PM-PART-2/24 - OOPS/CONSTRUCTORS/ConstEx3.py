#ConstEx3.py
class Student:
	def  __init__(self,sno,sname): # parameterized constructor
		print("i am from constructor")
		self.sno=sno
		self.sname=sname


#main program
s1=Student(10,"Rossum") #object creation
print("content of s1=",s1.__dict__)
s2=Student(20,"Travis") # Object creation
print("content of s2=",s2.__dict__)
s3=Student(30,"dennis") # Object creation
print("content of s2=",s3.__dict__)