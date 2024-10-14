#maxminvaluewithlogicex1..py
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
        print("Given List ={}".format(lst))
        print("-" * 50)
        maxv=lst[0]
        minv=lst[0]
        for i in range(1,len(lst)):
            if(lst[i]>maxv):
                maxv=lst[i]
            if(lst[i]<minv):
                minv=lst[i]
        else:
            print("Max=",maxv)
            print("Min=",minv)
