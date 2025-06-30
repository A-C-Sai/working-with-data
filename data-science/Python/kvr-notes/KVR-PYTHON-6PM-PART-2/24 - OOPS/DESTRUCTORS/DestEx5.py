#DestEx5.py
import time,sys
class Employee:
	def  __init__(self,eno,ename): # Constructor
		print("\n\ti am Constructor")
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
	
	def __del__(self): # Destructor 
		print("GC Calls __del__() during object destruction")
		#global totmemspace
		#totmemspace=totmemspace-sys.getsizeof(self)
		#print("Available Memory Space={}".format(totmemspace))

#main program
print("Program Execution Started:")
e1=Employee(10,"Rossum") # Object creation
e2=e1 # Deep Copy
e3=e2 # Deep Copy
print(e1.__dict__,id(e1))
print(e2.__dict__,id(e2))
print(e3.__dict__,id(e3))
print("-----------------------------------------------------------------------")
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory Space at Line No-18:{}".format(totmemspace))
time.sleep(5)
print("\nProgram Execution Ended:")

