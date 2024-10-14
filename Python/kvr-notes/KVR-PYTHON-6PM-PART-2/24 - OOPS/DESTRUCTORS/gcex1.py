#gcex1.py
import gc
print("Program execution started")
print("Initially, Is GC Running:",gc.isenabled())
a=10
b=20
c=a+b
gc.disable()
print("Is GC Running after disable:",gc.isenabled())
d=a-b
e=a*b
print("Val of a=",a)
print("Val of b=",b)
print("sum=",c)
gc.enable()
print("sub=",d)
print("Mul=",e)
print("Is GC Running after enable:",gc.isenabled())
print("Program execution Ended")

