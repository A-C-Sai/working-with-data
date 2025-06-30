#Program for generating Mul Tables for Differ Values and accept them from KBD
#RandomMulTables.py
n=int(input("How Many Mul Tables  u want:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=[]
	print("Enter {} Values:".format(n))
	for i in range(1,n+1):
		lst.append(int(input()))
	else:
		print("Given List of Values:{}".format(lst)) # [19, 0, 18, -4, 12]
		#Code for Generating Table for random values
		for num in lst:  # Outer For Loop
			if(num<=0):
				print("\t{} is invalid Input".format(num))
			else:
				print("-"*50)
				print("\tMul table for:{}".format(num))
				print("-"*50)
				i=1
				while(i<=10):#Inner while Loop
					print("\t{} x {} = {}".format(num,i,num*i))
					i=i+1
				else:
					print("-"*50)

