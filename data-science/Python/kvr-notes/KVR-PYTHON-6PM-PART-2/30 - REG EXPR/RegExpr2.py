#RegExpr2.py---search()
import re
gd="Python is an oop Lang.Python is al Fun Prog Lang"
sp="Python"
result=re.search(sp,gd)  
if(result==None):
	print("Type of res=",type(result))  #<class NoneType>
	print("Search is un-successful")
	print("'{}' Value  does not exist".format(sp))
else:
	print("Type of res=",type(result))  #<class re.Match>
	print("Search is Successful")
	print("Starting Index={}".format(result.start()))
	print("End Index={}".format(result.end()))
	print("Match Value={}".format(result.group()))
