#listcompre1.py
print("Enter List of values separated by space:")  # [10,2,222,50,10,4,55,-3,0,22]
lst=  [float(val)  for val  in input().split() ]
print("content of lst",lst) # [3.0, 5.0, 2.0, 7.0, 3.0, 9.0, 6.0]
print("-"*40)
newlst=[]
for val in lst:
	newlst.append(val*2)
else:
	print("new list=",newlst)
print("-"*40)
print("==============OR=================")
newlst=[ val*2  for val  in lst]
print("new list=",newlst)
