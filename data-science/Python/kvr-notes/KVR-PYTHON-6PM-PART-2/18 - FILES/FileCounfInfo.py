#Porogram for finding number of lines, words and chars from the file
#FileCounfInfo.py
filename=input("Enter File Name:")
nol,nowd,noc=0,0,0
try:
	with open(filename,"r" ) as fp:
		filelines=fp.readlines()
		for line in filelines:
			nol=nol+1
			nowd=nowd+len(line.split())
			noc=noc+len(line)
			#Code
		else:
			print("-"*50)
			print("Number of Lines=",nol)
			print("Number of Words=",nowd)
			print("Number of Chars=",noc)
			print("-"*50)
except FileNotFoundError:
	print("File does not exist")
