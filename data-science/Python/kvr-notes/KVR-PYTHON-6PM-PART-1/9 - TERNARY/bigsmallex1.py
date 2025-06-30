#program for finding biggest and smallest of Three numbers
#bigsmallex1.py
a=int(input("Enter Value of a:")) # a=10
b=int(input("Enter Value of b:"))# b=30
c=int(input("Enter Value of c:"))# b=30
#Find Big logic
big=a  if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>=a) and (c>b) else "ALL VALS ARE EQUAL"
print("big({},{},{})={}".format(a,b,c,big))
#Find small logic
sma=a if (a<=b) and (a<c) else b if (b<a) and (b<=c) else c if (c<=a) and (c<b) else "ALL VALS ARE EQUAL"
print("small({},{},{})={}".format(a,b,c,sma))



