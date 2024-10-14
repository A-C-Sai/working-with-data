#Read the data from csv file by using csv module
#ReadcsvEx5.py
import csv
try:
	with open("stud.csv","r") as fp:
		dictrd=csv.DictReader(fp)
		for rec in dictrd:
			print("-"*50)
			for kn,kv in rec.items():
				print("\t{}-->{}".format(kn,kv))
			print()
			print("-"*50)
except FileNotFoundError:
	print("File does not exist:")