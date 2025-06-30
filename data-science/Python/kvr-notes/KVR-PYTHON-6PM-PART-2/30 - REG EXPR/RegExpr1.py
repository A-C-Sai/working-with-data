#RegExpr1.py---findall()
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sp="Python"
result=re.findall(sp,gd) # here result is of type <class,list>
noc=0
for val in result:
	noc=noc+1
	print("\t{}".format(val))
else:
	print("'{}' found {} Times:".format(sp,noc))