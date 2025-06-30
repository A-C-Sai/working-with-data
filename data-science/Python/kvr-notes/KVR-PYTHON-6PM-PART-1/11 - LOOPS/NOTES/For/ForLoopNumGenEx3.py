#program for displaying all even numbers from n to 1
#ForLoopNumGenEx3.py
n=int(input("Enter Value of n:")) # n=10
if(n<=0):
	print("{} is invalid input".format(n))
else:
	print("-"*50)
	print("Numbers within {} to 1".format(n))
	print("-"*50)
	for v in range(n,0,-2):
		if(v%2==0):
			print("\t{}".format(v))
		

	