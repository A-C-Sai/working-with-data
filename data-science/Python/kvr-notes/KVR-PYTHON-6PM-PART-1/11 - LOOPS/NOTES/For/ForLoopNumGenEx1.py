#program for displaying 1 to n where n is +ve 
#ForLoopNumGenEx1.py
n=int(input("Enter Value of n:")) # n=5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	print("-"*50)
	print("Numbers within:{}".format(n))
	print("-"*50)
	for val in range(1,n+1):
		print("\t{}".format(val))
	else:
		print("-"*50)