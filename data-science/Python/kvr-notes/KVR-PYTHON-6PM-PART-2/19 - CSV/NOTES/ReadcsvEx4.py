#Read the data from csv file by using csv module
#ReadcsvEx4.py
import csv
try:
	with open("univ2.csv","r") as fp:
		dictrd=csv.DictReader(fp)
		for rec in dictrd:
			print("-"*50)
			for kn,kv in rec.items():
				print("\t{}-->{}".format(kn,kv))
			print()
			print("-"*50)
except FileNotFoundError:
	print("File does not exist:")