#FilterReduceEx1.py
import functools
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
# lst=[10,-23,40,25,-10,-30]--->pslist=[10,40,25]---sum=75--nnlist=[-23,-10,-30]=sum=-63
if(len(lst)==0):
	print("List is empty and can't find sum of +Ve and _ve Values")
else:
	#apply filter for obtaining +Ve and -Ve Values
	pslist=list(filter(lambda val:val>0, lst))
	nslist=list(filter(lambda val:val<0,lst))
	#apply reduce for getting +Ve Values sum and -Ve Vals sum
	pslistsum=functools.reduce(lambda a,b:a+b,pslist)
	nslistsum=functools.reduce(lambda a,b: a+b,nslist)
	print("-"*50)
	print("Given Elements:{}".format(lst))
	print("Possitive Elements:{}".format(pslist))
	print("Negative Elements:{}".format(nslist))
	print("-"*50)
	print("PosSum({})={}".format(pslist,pslistsum))
	print("NegSum({})={}".format(nslist,nslistsum))
	print("-"*50)