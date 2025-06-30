#Program extrating names from given text
#NamesMarksListEx1.py
import re
gd="Rossum is the developer of python an got 44 marks , Ritche is dev of c lang got 66 marks, Travis is the dev of numpy  got 99 marks and Kinney is the dev of pandas and gor 45 and Suresh got 11 marks and he is student and Rajesh marks 333"
print("List of Names")
namesmatches=re.findall("[A-Z][a-z]+",gd)
for names in namesmatches:
	print("\t{}".format(names))
#-----------------------------------------------------------------
print("List of Marks")
markslist=re.findall("[0-9]{2,4}",gd)   #  \d{2,4}  or \d+  or [0,9]{2}
for marks in markslist:
	print("\t{}".format(marks))
#-----------------------------------------------------------------
print("----------------------------------------------------")
print("\tNames\tMarks")
print("----------------------------------------------------")
for names, marks in zip(namesmatches,markslist):
	print("\t{}\t{}".format(names,marks))
print("----------------------------------------------------")




