#Program for cal Factorial of a given number
#FactEx1.py
def  fact(n):
	if(n<0):
		print("{} is invalid Input:".format(n))
	else:
		f=1
		for i in range(1,n+1):
			f=f*i
		else:
			print("Fact({})={}".format(n,f))

#main program
n=int(input("Enter any value:"))
fact(n)#Function Call