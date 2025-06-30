#Program for deciding wether the given number is prime or not
#PrimeEx3.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break

    if(res):
        print("{} is Prime".format(n))
    else:
        print("{} is Not Prime".format(n))