#program for generating random RTA Values
#SampleEx2.py

import random as r
alphs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
lst1=["TS","AP"]
lst2=["08","09","39","07"]
for i in range(1,11):
	s=" "
	l1=r.sample(lst1,1)
	l2=r.sample(lst2,1)
	l3=r.sample(alphs,2)
	l4=r.sample(digits,4)
	rta=l1+l2+l3+l4
	s=s.join(rta)
	print(s)

	