#Program extrating names from given text
#NamesListEx1.py
import re
gd="Rossum is the developer of python , Ritche is dev of c lang, Travis is the dev of numpy and Kinney is the dev of pandas"
namesmatches=re.finditer("[A-Z][a-z]+",gd)
for names in namesmatches:
	print("Start Index:{}  End Index:{} and Name:{}".format(names.start(),names.end(),names.group()))
