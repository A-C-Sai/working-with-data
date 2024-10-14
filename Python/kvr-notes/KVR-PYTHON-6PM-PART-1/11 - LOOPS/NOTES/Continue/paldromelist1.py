#Program for accepting list of words and display only palindromes
#paldromelist1.py
print("Enter List of words separated by space")
lst=[word for word in input().split()]
plist=[]
nplist=[]
for word in lst:
	if(word!=word[::-1]):
		nplist.append(word)
		continue
	plist.append(word)	
else:
	print("content of list={}".format(lst))
	print("Palindrom List={}".format(plist))
	print("Non-Palindrom List={}".format(nplist))