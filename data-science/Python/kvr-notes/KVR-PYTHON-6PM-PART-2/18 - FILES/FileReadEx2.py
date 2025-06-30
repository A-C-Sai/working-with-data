#Porogram for reading the data of the file
#FileReadEx2.py
filename=input("Enter File Name:")
try:
	with open(filename,"r") as fp:
		filelines=fp.readlines()
		print("content of file")
		print("---------------------------------------")
		for line in filelines:
			print(line,end="")
		print("---------------------------------------")
except FileNotFoundError:
	print("File does not exist:")