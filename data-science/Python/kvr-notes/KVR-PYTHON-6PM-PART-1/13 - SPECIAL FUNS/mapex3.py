#Program for demonstrating map()
#mapex3.py
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
	print("List is empty and nothing is to map")
else:
	sqlist=list(map(lambda k:k**2,lst))
	print("-"*50)
	print("Given Element\t\tSquares")
	print("-"*50)
	for gn,sn in zip(lst,sqlist):
		print("\t{}\t\t{}".format(gn,sn))
	print("-"*50)
	print("===============OR===============")
	print("-"*50)
	d=dict(zip(lst,sqlist))
	for gn,sn in d.items():
		print("\tSquare({})\t\t{}".format(gn,sn))
	print("-"*50)