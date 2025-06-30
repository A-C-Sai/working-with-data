#Program for cal area and perimeter of Cirtcle
#AreaPeriCircle.py
def   area():
	r=float(input("Enter Radious for cal area of Circle:"))
	if(r<0):
		print("{} is invalid Input:".format(r))
	else:
		ac=3.14*r**2
		print("Area of Circle:{}".format(ac))

def peri():
	r=float(input("\nEnter Radious for cal Perimeter of Circle:"))
	if(r>=0):
		cp=2*3.14*r
		print("Perimneter of Circle:{}".format(cp))
	else:
		print("{} is Invalid Input:".format(r))
#main program
area() # Function Call
peri() # Function Call

