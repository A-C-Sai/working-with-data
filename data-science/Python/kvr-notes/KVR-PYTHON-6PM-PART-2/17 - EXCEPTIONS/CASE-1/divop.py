#Program cal diviion of any two integer values and HIT the programmer-exception
#divop.py------File Name and acts as module name
from hyd import HydDivisionError
def  division(a,b):   # a=10   b=0
	if (b==0):
		raise HydDivisionError  # Hiiting or Raising or Generating exception
	else:
		return (a/b)


#Phase-2:  here division() is a common function which is hitting the Programmer-defined excepotion