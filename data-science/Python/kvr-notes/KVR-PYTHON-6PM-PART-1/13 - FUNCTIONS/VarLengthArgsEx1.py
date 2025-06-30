#program for demonstarting Variable length arguments
#This Program will not execute as it is bcoz PVM is an interpreter and it can remember only latest Function Definiton but not able to remember all the definition bcoz function name is same.
#VarLengthArgsEx1.py
def disp(a): # Function Def-1
	print(a)
def  disp(a,b): # Function Def-2
	print(a,b)
def  disp(a,b,c): # Function Def-3
	print(a,b,c)
def  disp(a,b,c,d): # Function Def-4
	print(a,b,c,d)

#main program
disp(10)  # Function Call-1
disp(10,20) # Function Call-2
disp(10,20,30) # Function Call-3
disp(10,20,30,40) # Function Call-4
disp() # Function Call-5

