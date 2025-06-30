#Program for Demonstarting reduce()
#reduceex1.py
import functools
def  addop(a,b):  # Normal Function
	return a+b


# main program
lst=[10,20,30,40,50]
res=functools.reduce(addop,lst)
print("sum({})={}".format(lst,res))