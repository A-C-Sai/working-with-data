#Program for reading from CSV file by using csv module
#CSVDictReaderEx1.py
import csv
try:
	with open("univ2.csv","r") as fp:
		csdr=csv.DictReader(fp) # Here csdr is an object of <class, _csv.DictReader>
		for record in csdr:
			for k,v in record.items():
				print("\t{}-->{}".format(k,v))
			print()
except FileNotFoundError:
	print("CSV File does not exist")