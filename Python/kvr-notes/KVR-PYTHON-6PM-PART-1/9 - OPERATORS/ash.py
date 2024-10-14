#ash.py
lst=['abc', 'xyz', 'aba', '1221']
cnt=0
for word in lst:
	if(word[0]==word[-1]):
		print(word)
		cnt=cnt+1
print("Result=",cnt)