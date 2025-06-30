#Creating a Folder-----mkdir()
#mkdirex.py
import os
try:
	os.mkdir("C:\\HYDERABAD")
	print("Folder Created Successfully")
except FileNotFoundError:
	print("Folders Hierarchy can't be created")
except FileExistsError: 
	print("Folder already exist")