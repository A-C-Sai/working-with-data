#PolyEx7.py
class Circle:
	def  area(self):  # Orioginal Method (One Form)
		self.r=float(input("Enter Radious:"))
		self.ac=3.14*self.r**2
		print("Area of Circle:{}".format(self.ac))
class Square:
	def  area(self): # Orioginal Method (One Form)
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square:{}".format(self.sa))
class Rect(Square,Circle):
	def  area(self): # Overriddent Method
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		self.ar=self.l*self.b
		print("Area of Rect:{}".format(self.ar))
		print("------------------------------------------------------")
		Square.area(self)#    OR   super().area()
		Circle.area(self)

#main program
r=Rect()
r.area()
