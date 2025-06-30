#Program for deciding wether the given number is prime or not
#PrimeEx2.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    res=0
    for i in range(2,n):
        if(n%i==0):
            res=1
            break

    if(res==0):
        print("{} is Prime".format(n))
    else:
        print("{} is Not Prime".format(n))