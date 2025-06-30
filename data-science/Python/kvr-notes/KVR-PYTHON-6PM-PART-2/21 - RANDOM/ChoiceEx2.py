#program for generating random catcha code data from given word
#ChoiceEx2.py
import random as r
alphs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
ss="!@#%^&*()_!~"
for i in range(1,6):
	print(r.choice(alphs)+r.choice(digits)+r.choice(alphs)+r.choice(ss))

