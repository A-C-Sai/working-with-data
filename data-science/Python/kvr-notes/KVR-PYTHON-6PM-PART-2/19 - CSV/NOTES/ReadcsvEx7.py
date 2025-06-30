#Read the data from csv file by using csv module
#ReadcsvEx7.py
import csv
try:
	with open("studentmarks1.csv","r") as fp:
		csvreader=csv.reader(fp)
		for record in csvreader:
			for val in record:
				print("{}".format(val),end="\t")
			print()
		
except FileNotFoundError:
	print("File does not exist:")