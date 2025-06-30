#program for shuffling the values
#ShuffleEx1.py
import random as r
lst=[10,"RS",34.56,"Python",True]
for i in range(1,6):
	r.shuffle(lst)
	print(lst)