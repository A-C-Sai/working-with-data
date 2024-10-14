#listcompre.py
print("Enter List of values separated by space:")  # [10,2,222,50,10,4,55,-3,0,22]
lst=  [float(val)  for val  in input().split() ]
print("content of lst",lst)
print("============OR================")
ls=[]
n=int(input("Enter how many values u want to be list:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("Enter {} values:".format(n))
	for i in range(1,n+1):
		val=int(input())
		ls.append(val)
	else:
		print("content of lst",ls)

