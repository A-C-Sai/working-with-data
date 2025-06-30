#BigThreeEx2.py
a=int(input("Enter Value of a:")) # a=10
b=int(input("Enter Value of b:")) # b=50
c=int(input("Enter Value of c:")) # c=4
if (a>=b) and (a>c):
    print("big({},{},{})={}".format(a,b,c,a))
else:
    if(b>a) and (b>=c):
        print("big({},{},{})={}".format(a, b, c, b))
    else:
        if(c>=a) and (c>b):
            print("big({},{},{})={}".format(a, b, c, c))
        else:
            print("ALL ARE EQUAL")
print("Program execution completed")