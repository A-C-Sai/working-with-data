#Removing a Folder----rmdir()
#rmdirex.py
import os
try:
	os.rmdir("C:\INDIA\HYD\PYTHON\AMPT")
	print("Folder Removed--verify")
except FileNotFoundError:
	print("Folder does not exist")
except OSError :
	print("Folder is non-empty")
