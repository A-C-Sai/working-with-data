#DestEx6.py
import time,sys
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
e2=e1 # Deep Copy
e3=e2 # Deep Copy
print(e1.__dict__,id(e1))
print(e2.__dict__,id(e2))
print(e3.__dict__,id(e3))
print("-----------------------------------------------------------------------")
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory Space at Line No-18:{}".format(totmemspace))
print("-----------------------------------------------------------------------")
print("No Longer Interested to maintain the memory space e1 object")
time.sleep(5)
totmemspace=totmemspace-sys.getsizeof(e1)
del e1 # Forcelly GC can't call its Destructor bcoz e2 and e3 points same memory space
print("Available Memory Space--Line No:29={}".format(totmemspace))
print("No Longer Interested to maintain the memory space e2 object")
time.sleep(5)
totmemspace=totmemspace-sys.getsizeof(e2)
e2=None # Forcelly GC can't call its Destructor bcoz  e3 points same memory space
print("Available Memory Space--Line No:34={}".format(totmemspace))
print("No Longer Interested to maintain the memory space e3 object")
time.sleep(5)
totmemspace=totmemspace-sys.getsizeof(e3)
del e3 # Forcelly GC  call its Destructor No objects Points object memory space
time.sleep(5)
print("Available Memory Space--Line No:40={}".format(totmemspace))
print("\nProgram Execution Ended:")
