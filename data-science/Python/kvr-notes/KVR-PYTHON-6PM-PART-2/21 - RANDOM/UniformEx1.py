#program for generating random floating  Values berween 0.0 to 1.0 by using uniform()
#UniformEx1.py
import random as r
for i in range(1,10):
	print(r.uniform(10.56,20.67))
print("----------------------------------")
for i in range(1,10):
	print(round(r.uniform(10,20),2))
print("----------------------------------")
for i in range(1,10):
	print("%0.2f" %r.uniform(100.67,200))
