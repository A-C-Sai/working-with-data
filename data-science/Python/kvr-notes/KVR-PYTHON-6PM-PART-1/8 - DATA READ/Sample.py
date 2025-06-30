#Program cal area of circle
#Sample.py
try:
	r=float(input("Enter radious:"))
	if(r<0):
		print("Invalid Input:")
	else:
		area=3.14*r*r
		print("------------------------------")
		print("Radious={}".format(r))
		print("Area of Circle={}".format(area))
		print("------------------------------")
except ValueError:
	print("Don't enter String, Alnums, and symbols")