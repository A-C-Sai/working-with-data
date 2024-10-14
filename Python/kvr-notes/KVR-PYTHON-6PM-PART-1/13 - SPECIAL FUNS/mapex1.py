#Program for demonstrating map()
#mapex1.py
def   square(n):
	return n**2

#main program
lst=[2,3,5,12,15,-4,25]
mapobj=map(square,lst) # Here mapobj is an object of <class,'map'>
sqlist=list(mapobj)
print("-"*50)
print("Given Element\t\tSquares")
print("-"*50)
for gn,sn in zip(lst,sqlist):
	print("\t{}\t\t{}".format(gn,sn))
print("-"*50)
print("===============OR===============")
print("Given Element\t\tSquares")
print("-"*50)
d=dict(zip(lst,sqlist))
for gn,sn in d.items():
	print("\t{}\t\t{}".format(gn,sn))
print("-"*50)