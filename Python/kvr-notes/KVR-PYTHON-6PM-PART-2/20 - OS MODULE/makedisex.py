#Creating Folders Hierarchy---makedirs()
#makedisex.py
import os
try:
	os.makedirs("c:\\KVR")
	print("Folder Hierarchy Created Sucessfully")
except FileExistsError:
	print("Folder Hierarchy alerady created:")