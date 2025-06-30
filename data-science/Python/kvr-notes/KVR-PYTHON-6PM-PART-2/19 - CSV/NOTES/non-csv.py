#read the data from csv files 
#non-csv.py
try:
	with open("stud.csv","r") as fp:
		filedata=fp.read()
		print(filedata)
except FileNotFoundError:
	print("File does not exist:")