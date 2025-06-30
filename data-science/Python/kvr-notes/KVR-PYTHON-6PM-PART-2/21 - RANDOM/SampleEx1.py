#program for generating random RTA Values
#SampleEx1.py
import random as r
alphs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
lst1=["TS","AP"]
lst2=["08","09","39","07"]
for i in range(1,11):
	print(r.sample(lst1,1)+r.sample(lst2,1)+r.sample(alphs,2)+r.sample(digits,4))