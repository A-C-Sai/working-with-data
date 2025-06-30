#Program extrating names from given text
#NamesListEx2.py
import re
gd="Rossum is the developer of python , Ritche is dev of c lang, Travis is the dev of numpy and Kinney is the dev of pandas"
namesmatches=re.findall("[A-Z][a-z]+",gd)
for names in namesmatches:
	print("\t{}".format(names))

