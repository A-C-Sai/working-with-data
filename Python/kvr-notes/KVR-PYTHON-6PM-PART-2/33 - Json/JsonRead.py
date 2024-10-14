# Python program to read json file
#JsonRead.py
import json
try:
	fp = open('kvr.json')
	dictobj = json.load(fp) # returns JSON object as  a dictionary
	# Iterating through the json  list
	for k,v in dictobj.items():
		print("{}--->{}".format(k,v))
except FileNotFoundError:
	print("Json File does not exist")