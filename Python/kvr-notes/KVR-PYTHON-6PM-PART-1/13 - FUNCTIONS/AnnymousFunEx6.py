#Program for finding biggest and smallest from three numbers
#AnnymousFunEx6.py
big=lambda a,b,c: a if b<a>=c else b if a<=b>c else c if a<c>=b  else "ALL Values are Equal:"
small=lambda k,v,r: k if v>k<=r else v if k>=v<r else r if k>r<=v else "ALL Values are Equal:"

#main program
a=int(input("Enter Val of a:"))
b=int(input("Enter Val of b:"))
c=int(input("Enter Val of c:"))
print("Big({},{},{})={}".format(a,b,c,big(a,b,c)))
print("Small({},{},{})={}".format(a,b,c,small(a,b,c)))