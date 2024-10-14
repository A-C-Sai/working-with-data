#ConstEx1.py
class Student:
	def  __init__(self):  # default constructor
		print("i am from constructor")
		self.sno=10
		self.sname="lalit"
		self.marks=45.66



#main program
s=Student() # Object Creation-----PVM--calls Constructor Automatically / Implcitly for placing our own data                                                       data without leaving object empty
print("Content of s=",s.__dict__)