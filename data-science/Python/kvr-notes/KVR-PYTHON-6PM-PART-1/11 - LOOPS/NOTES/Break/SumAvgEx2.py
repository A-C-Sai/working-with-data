#SumAvgEx2.py
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
        s=0.0
        for val in lst:
            s=s+val
        else:
            print("-" * 50)
            print("sum=",s)
            print("Avg=%0.2f" %(s/len(lst)))
            print("-" * 50)





