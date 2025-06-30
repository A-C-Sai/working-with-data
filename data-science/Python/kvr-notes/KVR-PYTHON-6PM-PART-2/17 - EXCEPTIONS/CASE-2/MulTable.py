#MulTable.py---FILE NAME AND MODULE NAME
from MulExceptions import ZeroError,NegativeNumberError
def  table(n):
	if(n==0):
		raise  ZeroError  # Hitting the exception
	elif(n<0):
		raise NegativeNumberError # # Hitting the exception
	elif(n>0):
		print("="*50)
		print("Mul Table for :{}".format(n))
		print("="*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		else:
			print("="*50)