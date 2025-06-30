#Program for demionstrating filter() 
#FilterEx4.py
print("Enter list of values separated bny space")
lst=[int(val) for val in input().split()]
poslist=list(filter(lambda n: n>0,lst))
neglist=tuple(filter(lambda k: k<0,lst))
print("Given List List of Values:",lst)
print("List of +VE Elements=",poslist)
print("List of -VE Elements=",neglist)