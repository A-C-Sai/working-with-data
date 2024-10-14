#Program for finding max and min from list of values by using Functions
#indexvalue.py
def  readvalues():
	print("\nEnter List of values separated by space:") 
	lst=[ int (val)  for val in input().split() ]  
	return lst

def   findindex():
	lst=readvalues()
	indval=-1
	sk=int(input("Enter which value u want to search:"))
	for i in range(0,len(lst)):
		if(sk==lst[i]):
			indval=i
			break
	
	if(indval>-1):
		print("{} Found at {} Index:".format(sk,indval))
	else:
		print("{} does not exist in list".format(sk))

#main program
findindex()