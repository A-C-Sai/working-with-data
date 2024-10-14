#DestEx1.py
import time
class Employee:
	def  __init__(self,eno,ename): # Constructor
		print("\n\ti am Constructor")
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
	
	def __del__(self): # Destructor 
		print("GC Calls __del__() during object destruction")

#main program
print("Program Execution Started:")
e1=Employee(10,"Rossum") # Object creation
e2=Employee(20,"Travis") # Object creation
print("\nProgram Execution Ended:")
time.sleep(10)
#At the end of the program, GC calls detsructor for removing the removing the memory current program objects and This type Gc Collection is called Automatic Garbage Collection.
