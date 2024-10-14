# importing the csv module
#csvdictwriteex2.py
import csv
	
# my data rows as dictionary objects
mydict =[ {'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}   ]
	
# field names
csvfields = ['name', 'branch', 'year', 'cgpa']
	
# name of csv file
filename = "univ2.csv"
	
# writing to csv file
with open(filename, 'w') as fp:
	# creating a csv dict writer object
	dictwriter = csv.DictWriter(fp, fieldnames = csvfields)
	# writing headers (field names)
	dictwriter.writeheader()
	# writing data rows
	dictwriter.writerows(mydict)
	print("\nDict Data Written to the csv file--verify")
