#Program for demionstrating filter() 
#FilterEx1.py
def  posfun(n):  # Normal Function
	if n>0:
		return True
	else:
		return False
 
def negfun(n):   # Normal Function
	if(n<0):
		return True
	else:
		return False

#main program
lst=[10,-23,0,34,56,-57,-37,45,-5]
filterobj1=filter(posfun,lst) # Here filterobj is an object whose type is <class, 'filter'>
filterobj2=filter(negfun,lst)
poslist=list(filterobj1)
neglist=tuple(filterobj2)

print("Given List List of Values:",lst)
print("List of +VE Elements=",poslist)
print("List of -VE Elements=",neglist)