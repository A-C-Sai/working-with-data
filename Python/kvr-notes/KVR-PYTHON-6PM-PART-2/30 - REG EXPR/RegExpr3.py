#RegExpr3.py---findaiter()
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sp="Python"
matres=re.finditer(sp,gd) # here matres is of type <class,callable_Ityerator>
noc=0
print("-"*50)
for row in matres:
	noc=noc+1
	print("\tStart Index:{}   End Index:{}  Value:{}".format(row.start(),row.end(),row.group()))
print("-"*50)
print("'{}' found {} times".format(sp,noc))
