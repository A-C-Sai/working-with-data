#Program for demonstrating globals()
#globalsfunEx2.py
a=10
b=20
c=30  # here a,b,c are called Global Variables
def  operations():
	a=100
	b=200
	c=300   # Here a,b,c are called local Variables
	res=a+b+c+globals()['a']+globals()['b']+globals()['c']
	print(res)
	

	
#main program
operations()

#Note: In the above function, we have  local varaibles and  global Varaibles on same name