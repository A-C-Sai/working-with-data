#Program for demonstrating generators--decided toi generate 0 to 5(6-1)
#GenEx1.py
def  kvrrange(val):
	k=0
	while(k<val):
		yield k
		k=k+1

#main program
kr=kvrrange(6) # 
print("Type of kvrrange=",type(kvrrange))
print("Type of kr=",type(kr))
print("content of kr=",kr)
print("=========================")
#To get the value from generator, we use a function called next()
#Syntax:    next(generatorobject)
print(next(kr)) # 0
print(next(kr)) # 1
print(next(kr)) # 2
print(next(kr)) # 3
print(next(kr)) # 4
print(next(kr)) # 5
print(next(kr)) # StopIteration--exception




