#Program for generating n to 1  where n must be +ve
#NumGenEx3.py
n=int(input("Enter value of n:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	print("-"*50)
	print("Number from {} to 1:".format(n))
	print("-"*50)
	while(n>=1):
		print("\t{}".format(n))
		n=n-1
	else:
		print("-"*50)

	