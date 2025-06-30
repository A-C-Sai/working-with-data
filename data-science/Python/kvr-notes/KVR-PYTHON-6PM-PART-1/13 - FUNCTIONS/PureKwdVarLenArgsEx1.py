#Program for demonstrating Keyword Variable Length arguments
#PureKwdVarLenArgsEx1.py
def   dispinfo( **param): # here ** param if calle Kwd Var len argment and type dict
	print(param,type(param),len(param))


#PureKwdVarLenArgsEx1.py
#main program
dispinfo(eno=10,ename="Parveen",sal=4.5,dsg="SE")#Function Call-1
dispinfo(sno=20,sname="Rossum",marks=44.44)#Function Call-2
dispinfo(tno=20,tname="KVR",Exp=24,place="HYD",subject="Python")#Function Call-3
dispinfo(a=10,b=20)#Function Call-4
dispinfo(m=100)#Function Call-5
dispinfo()# #Function Call-6