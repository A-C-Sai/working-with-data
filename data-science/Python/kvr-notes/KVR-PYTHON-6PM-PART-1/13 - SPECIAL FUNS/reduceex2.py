#Program for Demonstarting reduce()
#reduceex2.py
import functools
lst=[10,20,30,40,50,-150]
res=functools.reduce(lambda a,b:a+b,lst)
print("sum({})={}".format(lst,res))