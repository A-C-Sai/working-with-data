#Program for accepting list of words and display only palindromes
#paldromelist.py
n=int(input("Enter How Many Words u Have:"))
if(n<=0):
    print("{} is invalid:".format(n))
else:
	lst=[]
	for i in range(1,n+1):
		val=input("Enter {} Word: ".format(i))
		lst.append(val)
	else:
		print("content of list={}".format(lst))
		for word in lst:
			if(word!=word[::-1]):
				continue
			print("\t{}".format(word))