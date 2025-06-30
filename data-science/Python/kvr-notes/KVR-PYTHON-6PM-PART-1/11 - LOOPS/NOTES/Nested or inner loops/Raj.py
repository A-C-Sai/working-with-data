#Program for generating Mul Tables for Differ Values and accept them from KBD
#Raj.py
n=int(input("How Values u have:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=[]
	print("Enter {} Values:".format(n))
	for i in range(1,n+1):
		lst.append(input())
	else:
		print("Given List of Values:{}".format(lst)) # [19, 0, 18, -4, 12]