#BigThreeEx1.py
a=int(input("Enter Value of a:")) # a=10
b=int(input("Enter Value of b:")) # b=100
c=int(input("Enter Value of c:")) # c=1
if(a==b==c):
    print("All are equal")
else:
    if(b<=a>c):
        print("Big={}".format(a))
    else:
        if(a<b>=c):
            print("big={}".format(b))
        else:
            print("Big={}".format(c))

