#Program for generating Mul Table for a given +ve Number
#MulTableEx1.py
n=int(input("Enter a value for Generating Mul Table:")) # n=-5  0  9
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("Mul Table for :{}".format(n))
	print("-"*50)
	i=1
	while(i<=10):
		print('\t{} x {}={}'.format(n,i,n*i))
		i=i+1
	else:
		print("-"*50)