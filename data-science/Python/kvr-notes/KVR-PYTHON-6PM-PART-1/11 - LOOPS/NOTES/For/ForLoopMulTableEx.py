#program for generating mul table for +ve integer value
#ForLoopMulTableEx.py
n=int(input("Enter a Value for generting mul table:"))
if(n<=0):
	print("{} is invalid inputy:".format(n))
else:
	print("-"*50)
	print("Mul Table for {}".format(n))
	print("-"*50)
	for i in range(1,11):
		print("\t{} x {}={}".format(n,i,n*i))
	else:
		print("-"*50)
