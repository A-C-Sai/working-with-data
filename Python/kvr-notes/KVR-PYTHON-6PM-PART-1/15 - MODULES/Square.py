#Square.py---File Name and Module Name
def area():
    s=float(input("Enter Side Value:"))
    if(s<0):
        print("Invalid Side Value")
    else:
        sa=s**2
        print("Area of Square={}".format(sa))