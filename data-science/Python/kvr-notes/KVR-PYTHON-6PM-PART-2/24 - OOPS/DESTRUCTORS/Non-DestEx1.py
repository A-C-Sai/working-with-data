#Non-DestEx1.py
import sys
class Employee:
	def  __init__(self,eno,ename):
		print("\n\ti am Constructor")
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))

#main program
print("Program Execution Started:")
e1=Employee(10,"Rossum") # Object creation
print("Size of e1=",sys.getsizeof(e1))
e2=Employee(20,"Travis") # Object creation
print("Size of e2=",sys.getsizeof(e2))
print("\nProgram Execution Ended:")
