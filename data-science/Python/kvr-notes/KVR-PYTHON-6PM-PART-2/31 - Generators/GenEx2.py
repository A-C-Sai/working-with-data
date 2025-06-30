#Program for demonstrating generators--decided toi generate 0 to 5(6-1)
#GenEx2.py
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
while True:
	try:
		print(next(kr))
	except StopIteration:
		print("=========================")
		break
