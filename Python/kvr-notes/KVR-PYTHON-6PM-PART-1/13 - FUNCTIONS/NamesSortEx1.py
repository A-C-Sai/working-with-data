#Program for accepting list of names and sort them in both Ascending and Decending
#NamesSortEx1.py
def   readnames():
	lst=[] # empty list
	n=int(input("Enter How Many Names u want to Sort:"))#n=-4
	if(n<=0):
		return lst  # returning empty list
	else:
		print("Enter {} Names:".format(n))
		for i in range(1,n+1):
			val=input()
			lst.append(val)
		return lst		# returning non-empty list

def  sortNamesAscendingOrder(lstobj):
	print("-"*50)
	print("List of Original Names:")
	print("-"*50)
	for val in lstobj:
		print("\t{}".format(val))
	else:
		lstobj.sort()  # OR lstobj.sort(reverse=False)
		print("List of  Names in Ascending:")
		print("-"*50)
		for val in lstobj:
			print("\t{}".format(val))
		else:
			print("-"*50)

def sortNamesDecendingOrder(kvrlist):
	print("-"*50)
	print("List of Original Names:")
	print("-"*50)
	for val in kvrlist:
		print("\t{}".format(val))
	else:
		kvrlist.sort(reverse=True) #  kvrlist.sort()  kvrlist.reverse() OR kvrlist[::-1]
		print("List of  Names in Ascending:")
		print("-"*50)
		for val in kvrlist:
			print("\t{}".format(val))
		else:
			print("-"*50)



#main program
lst=readnames()
if(len(lst)==0):
	print("List is empty, can't sort Names")
else:
	while(True):
		opt=int(input("Do u want to sort names in\n Ascending Order (Press-1)\n Decending Order (Press-2) \n exit press-3:"))
		match(opt):
			case 1:
				sortNamesAscendingOrder(lst)
			case 2:
				sortNamesDecendingOrder(lst)
			case 3:
				print("Thx for using this Program")
				break
			case _:
				print("Ur Selection of Operation is wrong--try again")
