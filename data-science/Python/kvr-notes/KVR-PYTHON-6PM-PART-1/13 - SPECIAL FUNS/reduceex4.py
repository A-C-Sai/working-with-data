#Program for Demonstarting reduce()
#reduceex4.py
import functools
tpl=("Rossum","is","the","father", "of","python")
res=functools.reduce(lambda a,b: a+" "+b, tpl)
print("Result=",res)
