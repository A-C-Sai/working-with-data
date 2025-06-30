#Program for accepting list of values and find sum and avg
#SumAvg.py
def   readvalues():
	lst=[] # empty list
	n=int(input("Enter How Many Number sum and avg u want to find:"))#n=-4
	if(n<=0):
		return lst  # returning empty list
	else:
		print("Enter {} Values:".format(n))
		for i in range(1,n+1):
			val=float(input())
			lst.append(val)
		return lst		

def   findsumavg(lstobj):
	s=0
	print("-"*50)
	print("List of Values:")
	print("-"*50)
	for val in lstobj:
		print("\t{}".format(val))
		s=s+val
	else:
		print("Sum={}".format(s))
		print("Avg={}".format(s/len(lstobj)))
		print("-"*50)

#main program
lst=readvalues() # Function Call
if(len(lst)==0):
	print("List is empty, can't find sum and avg:")
else:
	findsumavg(lst)