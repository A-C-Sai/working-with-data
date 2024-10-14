#Rect.py---File Name and Module Name
def area():
    l=float(input("Enter Length:"))
    b = float(input("Enter Breadth:"))
    if(l<0) or (b<0):
        print("Invalid Measurements")
    else:
        ar=l*b
        print("Area of Rect={}".format(ar))