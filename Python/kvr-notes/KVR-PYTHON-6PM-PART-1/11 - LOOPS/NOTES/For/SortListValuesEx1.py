#Program accepting the list of values dynamically  and sort them
#SortListValuesEx1.py
n=int(input("Enter How Many values u want to sort:")) # n=-5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	#create an empty list
	lst=[]
	for i in range(1,n+1):
		val=float(input("Enter {} Value:".format(i)))
		lst.append(val)
	else:
		print("-"*50)
		print("Original  list of Values={}".format(lst))
		print("-"*50)
		#Code for sorting--ASC Order
		lst.sort()
		print("Sorted Values of list in Ascending Order={}".format(lst))
		lst.sort(reverse=True) # lst.reverse() #or  or   lst=lst[::-1]
		print("Sorted Values of list in Decending Order={}".format(lst))
