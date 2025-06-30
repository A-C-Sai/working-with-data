#Program accepting the (key,value) from KBD and put them dict
#ReadDictValuesEx.py
n=int(input("Enter How Many (Key,Value) values u have:")) # n=5
if(n<=0):
	print("{} is invalid input".format(n))
else:
	#crate an empty list
	d=dict()
	for i in range(1,n+1):
		k=input("Enter {}  Value of Key:".format(i))
		v=input("Enter {} Key Value of Value:".format(i))
		d[k]=v # Adding (Key,value) to dict
	else:
		print("-"*50)
		print("content of dict")
		print("-"*50)
		for k,v in d.items():
			print("\t{}--->{}".format(k,v))
		else:
			print("-"*50)