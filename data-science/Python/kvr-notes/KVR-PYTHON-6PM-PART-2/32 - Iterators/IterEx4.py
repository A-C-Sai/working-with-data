#IterEx4.py
d={10:"Apple",20:"Mango",30:"kiwi"} # Iterable Object--dict
dictiter=iter(d) #iter() converts any Iterable objects into Iterator object type
print("type of d=",type(d))
print("Type dictiter=",type(dictiter))
print("content of dictiter=",dictiter)
print("-------------------------------")
while(True):
	try:
		k=next(dictiter)
		print(k,d.get(k))
	except StopIteration:
		break
