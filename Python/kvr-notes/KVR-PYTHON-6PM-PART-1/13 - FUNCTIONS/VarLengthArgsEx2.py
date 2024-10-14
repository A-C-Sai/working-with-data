#program for demonstarting Variable length arguments
#This Program will  execute bcoz we are Defining a Function and calling that Function Immediately.
#VarLengthArgsEx2.py
def disp(a): # Function Def-1
	print(a)

disp(10)  # Function Call-1
#--------------------------------------------------------------------
def  disp(a,b): # Function Def-2
	print(a,b)
disp(10,20) # Function Call-2
#--------------------------------------------------------------------
def  disp(a,b,c): # Function Def-3
	print(a,b,c)

disp(10,20,30) # Function Call-3
#--------------------------------------------------------------------
def  disp(a,b,c,d): # Function Def-4
	print(a,b,c,d)
disp(10,20,30,40) # Function Call-4
#--------------------------------------------------------------------
def  disp(): # Function Def-5
	print("Not Taking any Values")
disp() # Function Call-5
#--------------------------------------------------------------------
#NOTE:   In the above Program, We have 5 Function Calls and 5 Function Def..
					# 1000 Function Calls----- 1000 Function Defs--Time Consuming Process
					#Today with Var length args concept
					# we have n-Multiple Function calls of same family------  we define
					                                           # 1 Function Definition 
