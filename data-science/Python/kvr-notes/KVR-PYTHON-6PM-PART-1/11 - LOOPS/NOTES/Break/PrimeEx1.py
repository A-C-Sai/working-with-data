#Program for deciding wether the given number is prime or not
#PrimeEx1.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    ass="Prime"
    for i in range(2,n): 
        if(n%i==0):
            ass="NOT PRIME"
            break

    if(ass=="Prime"):
        print("{} is {}".format(n,ass))
    else:
        print("{} is {}".format(n,ass))