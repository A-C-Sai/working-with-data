# Python program to demonstrate writing to CSV File---csv.writer--->writer()
#csvwriteex1.py
import csv
# field / header names 
recfields = ['Name', 'Branch', 'Year', 'CGPA']
# data rows of csv file
rows = [ ['Nikhil', 'CSE', '2', '9.0'],
		['Sanchit', 'CSE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']    ]
# name of csv file
csvfilename = "univ1.csv"
# writing  data to csv file
with open(csvfilename, 'w') as fp:
	# creating a csv writer object
	csvwriter = csv.writer(fp)
	# writing the fields / header name
	csvwriter.writerow(recfields)
	# writing the data rows
	csvwriter.writerows(rows)
	print("\nCSV file Created  and Verify")
