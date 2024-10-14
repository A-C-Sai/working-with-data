# Removing File Name----remove()
#removeex.py
import os
try:
	os.remove("C:\KVR-HYD\\emp.csv")
	print("File Removed--Verify")
except FileNotFoundError:
	print("file does not exist")