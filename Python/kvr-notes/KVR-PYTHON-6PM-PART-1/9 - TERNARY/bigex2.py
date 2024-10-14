#program for finding biggest of two numbers
#bigex2.py
a=int(input("Enter Value of a:")) # a=100
b=int(input("Enter Value of b:"))# b=100
#Find Big Logic and check for equality
res=a if a>b else b if b>a else "Values are Equal"
print("big({},{})={}".format(a,b,res))
