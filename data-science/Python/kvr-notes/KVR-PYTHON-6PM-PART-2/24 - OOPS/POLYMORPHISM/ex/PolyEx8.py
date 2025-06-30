#PolyEx8.py
class Circle:
	def  __init__(self):  # Original Constructor (One Form)
		self.r=float(input("Enter Radious:"))
		self.ac=3.14*self.r**2
		print("Area of Circle:{}".format(self.ac))
class Square:
	def  __init__(self): # Original Constructor (One Form)
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square:{}".format(self.sa))
class Rect(Square,Circle):
	def  __init__(self): # Overriddent Constructor
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		self.ar=self.l*self.b
		print("Area of Rect:{}".format(self.ar))
		print("------------------------------------------------------")
		Square.__init__(self)
		Circle.__init__(self)
#main program
r=Rect()
