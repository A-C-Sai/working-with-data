#program for shuffling the values
#ShuffleEx2.py
import random as r
s="MISSISSIPPI"
lst=list(s)

for i in range(1,len(s)):
	r.shuffle(lst)
	s=" "
	s=s.join(lst)
	print("\t{}".format(s))