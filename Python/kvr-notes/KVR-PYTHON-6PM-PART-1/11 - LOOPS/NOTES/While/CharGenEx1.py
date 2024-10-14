#program for accepting a line of text and display char by char
#CharGenEx1.py
import time
line=input("Enter a Line of text:")
print("-"*50)
print("Given Line:{}".format(line))
print("-"*50)
i=0
while(i<len(line)):
	print("\t{}".format(line[i]))
	i=i+1
	time.sleep(1)
else:
	print("-"*50)