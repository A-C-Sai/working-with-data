#PolyEx11.py
class Circle:
	def  area(self,r):  # Original Constructor (One Form)
		self.ac=3.14*r**2
		print("Area of Circle:{}".format(self.ac))
class Square:
	def  __init__(self,s): # Original Constructor (One Form)
		self.sa=s**2
		print("Area of Square:{}".format(self.sa))
class Rect(Square,Circle):
	def  __init__(self,l,b): # Overriddent Constructor
		self.ar=l*b
		print("Area of Rect:{}".format(self.ar))
		print("------------------------------------------------------")
		super().__init__(float(input("Enter Side:")))
		print("------------------------------------------------------")
		Circle.area(self,float(input("Enter Radious:")))
#main program
l=float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
r=Rect(l,b)

