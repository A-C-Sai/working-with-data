#Program for demionstrating filter() 
#FilterEx3.py
def  readvalues():
	lst=[]
	n=int(input("Enter How Many values u Have:"))
	if(n<=0):
		return lst
	else:
		print("Enter {} Values:".format(n))
		for i in range(1,n+1):
			lst.append(int(input()))
		return lst
#main program
lst=readvalues()
if(len(lst)==0):
	print("List is empty and nothing is filtering")
else:
	poslist=list(filter(lambda n: n>0,lst))
	neglist=tuple(filter(lambda k: k<0,lst))
	print("Given List List of Values:",lst)
	print("List of +VE Elements=",poslist)
	print("List of -VE Elements=",neglist)