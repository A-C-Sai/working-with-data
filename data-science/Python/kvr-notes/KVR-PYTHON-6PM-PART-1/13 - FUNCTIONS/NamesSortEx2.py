#Program for accepting list of names and sort them in both Ascending and Decending
#NamesSortEx2.py
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

def  sortNamesAscendingOrder():
	lst=readnames()
	if(len(lst)==0):
		print("List is empty, we can't sort the names in Ascending Order:")
	else:
		print("-"*50)
		print("List of Original Names:")
		print("-"*50)
		for val in lst:
			print("\t{}".format(val))
		else:
			lst.sort()  # OR lstobj.sort(reverse=False)
			print("List of  Names in Ascending:")
			print("-"*50)
			for val in lst:
				print("\t{}".format(val))
			else:
				print("-"*50)

def sortNamesDecendingOrder():
	kvrlist=readnames()
	if(len(kvrlist)==0):
		print("List is empty, we can't sort the names in Decending Order:")
	else:
		print("-"*50)
		print("List of Original Names:")
		print("-"*50)
		for val in kvrlist:
			print("\t{}".format(val))
		else:
			kvrlist.sort(reverse=True) #  kvrlist.sort()  kvrlist.reverse() OR kvrlist[::-1]
			print("List of  Names in Decending Order:")
			print("-"*50)
			for val in kvrlist:
				print("\t{}".format(val))
			else:
				print("-"*50)

#main program
while(True):
		opt=int(input("Do u want to sort names in\n Ascending Order (Press-1)\n Decending Order (Press-2) \n exit press-3:"))
		match(opt):
			case 1:
				sortNamesAscendingOrder()
			case 2:
				sortNamesDecendingOrder()
			case 3:
				print("Thx for using this Program")
				break
			case _:
				print("Ur Selection of Operation is wrong--try again")


