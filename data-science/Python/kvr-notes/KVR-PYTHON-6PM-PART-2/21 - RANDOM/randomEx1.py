#program for generating random floating  Values berween 0.0 to 1.0 by using random()
#randomEx1.py
import random as r
for i in range(1,10):
	print(r.random())
print("----------------------------------")
for i in range(1,10):
	print(round(r.random(),2))
print("----------------------------------")
for i in range(1,10):
	print("%0.2f" %r.random())
