#Program accepting the list of values dynamically  and  display the values
#ReadListValuesEx1.py
n=int(input("Enter How Many values u have:")) # n=5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	#crate an empty list
	lst=list()
	for i in range(1,n+1):
		val=int(input("Enter {} Value:".format(i)))
		lst.append(val)
	else:
		print("-"*50)
		print("content of list={}".format(lst))
		print("-"*50)







