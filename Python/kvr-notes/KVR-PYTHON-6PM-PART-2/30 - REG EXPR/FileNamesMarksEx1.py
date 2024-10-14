#Program for extracting student name and marks from student.data file by reg expr
#FileNamesMarksEx1.py
import re
try:
	with open("D:\KVR-PYTHON-6PM\REG EXPR/notes\student.data","r") as fp:
		filedata=fp.read()
		names=re.findall("[A-Z][a-z]+",filedata)
		markslist=re.findall("\d{2,3}",filedata)
		print("==============================")
		print("\tNames\tMarks")
		print("==============================")
		for name,marks in zip(names,markslist):
			print("\t{}\t{}".format(name,marks))
		print("==============================")
except FileNotFoundError:
	print("File does not exist")
