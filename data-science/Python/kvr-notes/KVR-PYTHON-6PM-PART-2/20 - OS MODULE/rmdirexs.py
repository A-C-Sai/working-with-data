#Removing a Folders----removedirs()
#rmdirexs.py
import os
try:
	os.removedirs("C:\KVR-HYD")
	print("Folders Removed--verify")
except FileNotFoundError:
	print("Folder does not exist")
except OSError :
	print("Folder is non-empty")
