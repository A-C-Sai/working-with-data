#program for generating 1 to n where n must be +Ve Integer values
#NumGenEx1.py
n=int(input("Enter How Many values u want to generate:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("\tNumbers within:{}".format(n))
	print("-"*50)
	i=1 # Initlization part
	while(i<=n):  # Cond Part
		print("\t{}".format(i))
		i=i+1 #Incrementation Part
	print("-"*50)
	