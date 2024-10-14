#IterEx1.py
lst=[10,"Rossum",34.56,True,2+3j,"Python"] # Iterable Object--List
lstiter=iter(lst)
print("type of lst=",type(lst))
print("Type lstiter=",type(lstiter))
print("content of listiter=",lstiter)
print("-------------------------------")
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))
print(next(lstiter))