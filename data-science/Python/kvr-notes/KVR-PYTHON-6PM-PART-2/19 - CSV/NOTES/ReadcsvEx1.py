#Read the data from csv file by using csv module
#ReadcsvEx1.py
import csv
try:
	with open("stud.csv","r") as fp:
		csvreader=csv.reader(fp)
		for record in csvreader:
			for val in record:
				print("\t{}".format(val),end=" ")
			print()
		
except FileNotFoundError:
	print("File does not exist:")
