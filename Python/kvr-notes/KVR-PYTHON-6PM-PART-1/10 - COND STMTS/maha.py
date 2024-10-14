#maha.py
print("Enter a line of text:")
line=input()
up=[]
for ch in line:
	if ch.islower():
		up.append(ch)

print(up)
