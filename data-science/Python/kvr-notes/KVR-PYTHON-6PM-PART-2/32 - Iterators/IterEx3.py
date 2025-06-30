#IterEx3.py
lst=(10,"Rossum",34.56,True,2+3j,"Python") # Iterable Object--tuple
lstiter=iter(lst) #iter() converts any Iterable objects into Iterator object type
print("type of lst=",type(lst))
print("Type lstiter=",type(lstiter))
print("content of listiter=",lstiter)
print("-------------------------------")
while(True):
	try:
		print(next(lstiter))
	except StopIteration:
		break
