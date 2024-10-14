# Python program to demonstrate to write single record
# writing single record to CSV file
#csvwriteex2.py
import csv

# data record of csv file
row = ['KVR', 'CSE', '2', '9.0']
	
# name of csv file
filename = "univ1.csv"
# writing to csv file
with open(filename, 'a') as fp:
	# creating a csv writer object
	cw = csv.writer(fp)
	# writing the data row to the csv file
	cw.writerow(row)
	print("\nSingle Record Written to the CSV File:")

	