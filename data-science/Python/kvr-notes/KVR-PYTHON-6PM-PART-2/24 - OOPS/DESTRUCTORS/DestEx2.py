#DestEx2.py
import time,sys
class Employee:
	def  __init__(self,eno,ename): # Constructor
		print("\n\ti am Constructor")
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
	
	def __del__(self): # Destructor 
		print("GC Calls __del__() during object destruction")
		global totmemspace
		totmemspace=totmemspace-sys.getsizeof(self)
		print("Available Memory Space={}".format(totmemspace))

#main program
print("Program Execution Started:")
e1=Employee(10,"Rossum") # Object creation
e2=Employee(20,"Travis") # Object creation
e3=Employee(20,"Travis") # Object creation
totmemspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory Space at Line No-18:{}".format(totmemspace))
print("\nProgram Execution Ended:")
time.sleep(10)
#At the end of the program, GC calls its detsructor for removing the  memory current program objects and This type of Gc Collection is called Automatic Garbage Collection.
