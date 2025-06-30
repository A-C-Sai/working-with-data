#Program for demonstrating globals()
#globalsfunEx1.py
a=10
b=20
c=30  # here a,b,c are called Global Variables
def  operations():
	p=100
	q=200
	r=300   # Here p,q,r are called local Variables
	res=a+b+c+p+q+r
	print(res)

	
#main program
operations()

#Note: In the above function, we have Different local varaibles and different global Varaibles