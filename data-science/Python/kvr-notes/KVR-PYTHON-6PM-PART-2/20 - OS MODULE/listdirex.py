#Listing the files in folder-listdir()
#listdirex.py
import os
try:
	dirname=input("Enter Folder Name:")
	files=os.listdir(dirname)
	print("-"*50)
	print("Number of Files={}".format(len(files)))
	print("-"*50)
	for filename in files:
		if(filename[-3:]==".py"):  #   NamesMarksListEx1.py
			print("\t{}".format(filename))
	print("-"*50)
except FileNotFoundError:
	print("Folder does not exist")
