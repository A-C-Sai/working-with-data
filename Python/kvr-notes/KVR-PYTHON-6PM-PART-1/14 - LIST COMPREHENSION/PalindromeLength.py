#PalindromeLength.py
print("Enter List of words separed space:")
paldowrds=[word for word in input().split() if word==word[::-1] ]
print("List of Palindrome words:{}".format(paldowrds))
#Code for finding max length palindrome word
dictobj=dict([ (word,len(word))  for word in paldowrds ])
print("-"*50)
print("Palindrome Word\tLength")
print("-"*50)
for pn,pl in dictobj.items():
	print("{}\t{}".format(pn,pl))
print("-"*50)
ml=max(dictobj.values())
kvr=[  k for  k,v in dictobj.items()  if ml==v]
print("Max Length Palindrom word={} and its length={}".format(kvr,ml))
for val in kvr:
	print(val,end=" ")
