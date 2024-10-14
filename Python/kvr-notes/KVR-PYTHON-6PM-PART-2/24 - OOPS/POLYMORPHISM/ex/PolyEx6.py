#PolyEx6.py
class Circle:
	def  area(self):  # Orioginal Method (One Form)
		self.r=float(input("Enter Radious:"))
		self.ac=3.14*self.r**2
		print("Area of Circle:{}".format(self.ac))
class Square(Circle):
	def  area(self): # Overridden Methods (Multiple Forms)
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square:{}".format(self.sa))
class Rect(Square):
	def  area(self): # Overridden Methods (Multiple Forms)
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		self.ar=self.l*self.b
		print("Area of Rect:{}".format(self.ar))
		print("-"*50)
		Circle.area(self)
		print("-"*50)
		super().area()
#main program
r=Rect()
r.area()