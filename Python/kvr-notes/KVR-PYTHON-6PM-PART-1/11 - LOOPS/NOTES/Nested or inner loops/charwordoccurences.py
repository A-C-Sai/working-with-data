#Program for finding all the occurences of a given word
#charwordoccurences.py
s=input("Enter word:")
d={}
for ch in s:
	if ch not in d:
		d[ch]=1
	else:
		d[ch]=d[ch]+1
else:
	print("-"*50)
	print("Given Word:{}".format(s))
	print("-"*50)
	for ch,noc in d.items():
		print("\t{}--->{}".format(ch,noc))
	print("-"*50)
