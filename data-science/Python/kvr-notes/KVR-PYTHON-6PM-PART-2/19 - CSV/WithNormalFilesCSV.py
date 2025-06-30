#Program for reading from CSV file by using Normal Files--Functions
#WithNormalFilesCSV.py
try:
	with open("D:\KVR-PYTHON-6PM\FILES\student.csv","r") as fp:
		csvdata=fp.read()
		print("CSV File Data:")
		print("------------------------------")
		print(csvdata)
		print("------------------------------")
except FileNotFoundError:
	print("File does not exist")