#program for cal division of Two Numebrs
#DivOpDemo.py----Main program--Specific Program
from divop import division
from hyd import HydDivisionError
try:
	a=int(input("Enter Value of a:"))
	b=int(input("Enter Value of b:"))
	res=division(a,b) # Function Call---gives either Result or Exception
except HydDivisionError:
	print("Don't Enter Zero For Den..")
except ValueError:
	print("Don't enter alnums, strs and special symbols for integer values")
except :
	print("ooooooooooooooops some thing went wrong!!!!")
else:
	print("Div({},{})={}".format(a,b,res))
finally:
	print("I am finally block")
