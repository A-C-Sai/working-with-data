#Program for demionstrating filter() 
#FilterEx2.py

posfun=lambda n: n>0 # Anonymous Fun
negfun=lambda n: n<0 # Anonymous Fun

#main program
lst=[10,-23,0,34,56,-57,-37,45,-5]
poslist=list(filter(posfun,lst)) # Here filterobj is an object whose type is <class, 'filter'>
neglist=tuple(filter(negfun,lst))
print("Given List List of Values:",lst)
print("List of +VE Elements=",poslist)
print("List of -VE Elements=",neglist)