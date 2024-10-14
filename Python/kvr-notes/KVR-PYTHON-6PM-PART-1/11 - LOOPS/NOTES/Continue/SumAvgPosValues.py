#SumAvgPosValues.py
#Program for accepting list of values and find sum and avg .
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
        print("Given List ={}".format(lst)) #[10,-20,30,-40,15]
        print("-" * 50)
        #logic for finding sum of +VE vals
        pos=0
        nop=0
        for val in lst:
            if(val<0):
                continue
            print("\t{}".format(val))# printing +ve Vals
            pos=pos+val # Accumulating Pos Values
            nop=nop+1 # Counting Number of Pos Values
        else:
            print("Sum={}".format(pos))
            print("Pos Avg=%0.2f" %(pos/nop))



