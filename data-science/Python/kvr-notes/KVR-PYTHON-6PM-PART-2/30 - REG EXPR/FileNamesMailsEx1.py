#Program for extracting student name and marks from student.data file by reg expr
#FileNamesMailsEx1.py
import re
try:
	with open("D:\KVR-PYTHON-6PM\REG EXPR/notes\mails.info","r") as fp:
		filedata=fp.read()
		names=re.findall("[A-Z][a-z]+",filedata)
		mails=re.findall("\S+@\S+",filedata)
		print("==============================")
		print("\tNames\tMails")
		print("==============================")
		for name,mail in zip(names,mails):
			print("\t{}\t{}".format(name,mail))
		print("==============================")
except FileNotFoundError:
	print("File does not exist")