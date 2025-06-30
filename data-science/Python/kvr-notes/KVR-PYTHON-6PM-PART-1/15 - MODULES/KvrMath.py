#Program for cal Factorial of a given number 
#KvrMath.py-----File Name and acts as module 
def   fact(n):
	if(n<0):
		print("factorial not defined for negative values")
	else:
		f=1
		for i in range(1,n+1):
			f=f*i
		else:
			print("fact({})={}".format(n,f))

		
