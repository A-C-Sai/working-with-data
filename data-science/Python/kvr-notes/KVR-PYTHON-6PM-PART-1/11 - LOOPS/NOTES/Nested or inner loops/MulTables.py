#Program for generating Mul Tables for 1 to n where n is +ve
#MulTables.py
nt=int(input("Enter How Many Mul Tables u want:"))
if(nt<=0):
	print("{} is invalid Input".format(nt))
else:
	for i in range(1,nt+1): # Outer for loop supply number 1  2  3  4  ...n
		print("-"*50)
		print("\tMul table for {}".format(i))
		print("-"*50)
		for j in range(1,11):
			print("\t{} x {} = {}".format(i,j,i*j))
		else:
			print("-"*50)





