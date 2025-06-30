#ConstEx2.py
class Student:
	def  __init__(self): # # default constructor
		print("i am from constructor")
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))

#main program
s=Student() # Object Creation-----PVM--calls Constructor Automatically / Implcitly for placing our own data   data without leaving object empty
print("Content of s=",s.__dict__)