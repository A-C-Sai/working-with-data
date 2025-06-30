#maxminvalue.py
n=int(input("Enter How Many values Sum and Avg u want to find:"))
if(n<=0):
    print("{} is invalid:".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("Given List ={}".format(lst))# [100.0, 15.0, 34.0, -2.0, 150.0]
        print("-" * 50)
        lst.sort()
        print("min=",lst[0])
        print("max=",lst[-1])
