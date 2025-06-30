#program for accepting a line of text and display char by char
#VowelsGenEx1.py
import time
line=input("Enter a Line of text:")  # Apple
print("-"*50)
print("Given Line:{}".format(line))
print("-"*50)
i=0
while(i<len(line)):
	if line[i] in ['a','e','i','o','u','A','E','I','O','U']:
		print("\t{}".format(line[i]))
	i=i+1
print("-"*50)