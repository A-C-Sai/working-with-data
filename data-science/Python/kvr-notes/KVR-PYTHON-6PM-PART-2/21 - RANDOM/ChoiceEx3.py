#program for generating random RTA Values
#ChoiceEx3.py
import random as r
alphs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
lst1=["TS","AP"]
lst2=["08","09","39","07"]
for i in range(1,11):
	print(r.choice(lst1)+r.choice(lst2)+r.choice(alphs)+r.choice(alphs)+r.choice(digits)+r.choice(digits)+r.choice(digits)+r.choice(digits))