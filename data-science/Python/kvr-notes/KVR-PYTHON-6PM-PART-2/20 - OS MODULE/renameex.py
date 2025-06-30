#Rename a Folder--rename()
#renameex.py
import os
try:
	os.rename("D:\HYD","D:\KVRPACK")
	print("Folder Renamed--verify")
except FileNotFoundError:
	print("Old Folder Name does not exist")