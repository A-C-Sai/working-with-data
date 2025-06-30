#Read the data from csv file by using csv module
#ReadcsvEx3.py
import csv
try:
	with open("univ2.csv","r") as fp:
		csvreader=csv.reader(fp)
		for record in csvreader:
			for val in record:
				print("\t{}".format(val),end="")
			print()
		
except FileNotFoundError:
	print("File does not exist:")