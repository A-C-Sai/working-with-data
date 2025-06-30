lst=[10,12,45,6,23]
sqlist=[]
for val in lst:
    res=val**2
    sqlist.append(res)
print("Original list={}".format(lst))
print("Square list={}".format(sqlist))
print("==========OR================")
sqlist1=[val**2 for val in lst ]
print("Original list={}".format(lst))
print("Square list={}".format(sqlist))