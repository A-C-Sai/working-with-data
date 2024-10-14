#program for displaying 1 to n where n is +ve 
#ForLoopNumGenEx2.py
n=int(input("Enter Value of n:")) # n=5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	print("-"*50)
	print("Numbers within {} to 1".format(n))
	print("-"*50)
	for i in range(n,0,-1):
		print("\t{}".format(i))
	else:
		print("-"*50)

	