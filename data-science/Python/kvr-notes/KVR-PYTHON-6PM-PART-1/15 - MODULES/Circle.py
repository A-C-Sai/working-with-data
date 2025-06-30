#Circle.py---File Name and Module Name
def area():
    r=float(input("Enter Radious:"))
    if(r<0):
        print("{} is invalid Radious".format(r))
    else:
        ac=3.14*r**2
        print("Area of Circle={}".format(ac))
