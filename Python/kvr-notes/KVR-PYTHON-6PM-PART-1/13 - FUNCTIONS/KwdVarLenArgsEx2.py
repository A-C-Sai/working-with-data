#Program for demonstrating Keyword Variable Length arguments
#KwdVarLenArgsEx2.py---This Program will  execute as it is .
def dispinfo(eno,ename,sal,dsg): # Function Def-1
	print("\t{}\t{}\t{}\t{}".format(eno,ename,sal,dsg))

dispinfo(eno=10,ename="Parveen",sal=4.5,dsg="SE")#Function Call-1
#---------------------------------------------------------------------------
def  dispinfo(sno,sname,marks):# Function Def-2
	print("\t{}\t{}\t{}".format(sno,sname,marks))

dispinfo(sno=20,sname="Rossum",marks=44.44)#Function Call-2
#---------------------------------------------------------------------------
def dispinfo(tno,tname,Exp,place,subject): # Function Def-3
	print("\t{}\t{}\t{}\t{}\t{}".format(tno,tname,Exp,place,subject))

dispinfo(tno=20,tname="KVR",Exp=24,place="HYD",subject="Python")#Function Call-3
#---------------------------------------------------------------------------
def dispinfo(a,b): # Function Def-4
	print("\t{}\t{}".format(a,b))

dispinfo(a=10,b=20)#Function Call-4
#---------------------------------------------------------------------------
def dispinfo(m): # Function Def-5
	print("\t{}".format(m))

dispinfo(m=100)#Function Call-5

#---------------------------------------------------------------------------
def dispinfo(): # Function Def-6
	print("No taking any Key word arguments")

dispinfo()# #Function Call-6
#---------------------------------------------------------------------------

#100  familiy of similar  function calls---we need to define 100 function Def--Waste of Time and this Type of Procedure is not recommended
