#Program for demonstrating Keyword Variable Length arguments
#KwdVarLenArgsEx1.py---This Program will not execute as it is .
def dispinfo(eno,ename,sal,dsg): # Function Def-1
	print("\t{}\t{}\t{}\t{}".format(eno,ename,sal,dsg))

def  dispinfo(sno,sname,marks):# Function Def-2
	print("\t{}\t{}\t{}".format(sno,sname,marks))

def dispinfo(tno,tname,Exp,place,subject): # Function Def-3
	print("\t{}\t{}\t{}\t{}\t{}".format(tno,tname,Exp,place,subject))

def dispinfo(a,b): # Function Def-4
	print("\t{}\t{}".format(a,b))

def dispinfo(m): # Function Def-5
	print("\t{}".format(m))

def dispinfo(): # Function Def-6
	print("No taking any Key word arguments")

#main program--having family of similar Function Calls with keyword Variable length  arguments 
dispinfo(eno=10,ename="Parveen",sal=4.5,dsg="SE")#Function Call-1
dispinfo(sno=20,sname="Rossum",marks=44.44)#Function Call-2
dispinfo(tno=20,tname="KVR",Exp=24,place="HYD",subject="Python")#Function Call-3
dispinfo(a=10,b=20)#Function Call-4
dispinfo(m=100)#Function Call-5
dispinfo()# #Function Call-6