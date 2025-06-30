# Python program to write the dict data to JSON to a file
#JsonWrite.py
import json
dictionary ={"rollno" : 56,"name" : "Rossum","cgpa" : 8.6} #  dict object
with open("kvr.json", "w") as fp:
	json.dump(dictionary, fp)
	print("Data written to file--verify")