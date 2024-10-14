#Program for reading from CSV file by using csv module
#CSVDictReaderEx2.py
import csv
try:
	with open("univ2.csv","r") as fp:
		csr=csv.reader(fp) # Here csdr is an object of <class, _csv.reader>
		for record in csr:
			for val  in record:
				print("\t{}".format(val),end="")
			print()
except FileNotFoundError:
	print("CSV File does not exist")