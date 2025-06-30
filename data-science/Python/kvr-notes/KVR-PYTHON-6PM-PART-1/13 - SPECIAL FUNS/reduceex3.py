#Program for Demonstarting reduce()
#reduceex3.py
import functools
lst=[10,2000,130,240,50,-150]
maxv=functools.reduce(lambda a,b: a if a>b else b,lst)
minv=functools.reduce(lambda a,b: a if a<b else b, lst)
print("max({})={}".format(lst,maxv))
print("min({})={}".format(lst,minv))
