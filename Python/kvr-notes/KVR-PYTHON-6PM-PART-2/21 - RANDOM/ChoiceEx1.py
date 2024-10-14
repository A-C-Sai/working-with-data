#program for generating random char data from given word
#ChoiceEx1.py
import random as r
s="PYTHON"
for i in range(1,5):
	print("\t{}".format(r.choice(s)))