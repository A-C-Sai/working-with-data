#Program for adding Two Numbers
#AnnymousFunEx1.py
def  addop(a,b):
	c=a+b
	return c

sumop=lambda x,y:x+y  # Anonymous Function

#main program
print("type of addop=",type(addop))  # <class 'function'>
res=addop(10,20)
print("sum by using Normal Function={}".format(res))
print("---------------------------------------------------------------------")
print("type of sumop=",type(sumop))  # <class 'function'>
res=sumop(100.2,200.4)
print("sum by using Anonymous Function={}".format(res))


