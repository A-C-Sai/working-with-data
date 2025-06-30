#Program for cal area of Different Figures by using OOPs 
#PloyEx1.py
class Circle:
	def area(self):
		self.r=float(input("Enter radious:"))
		self.ac=3.14*self.r**2
		print("Area of Circle={}".format(self.ac))
class Square(Circle):
	def area(self): # Overridden Method
		self.s=float(input("Enter Side:"))
		self.sa=self.s**2
		print("Area of Square={}".format(self.sa))
		print("-"*50)
		super().area()

class Rect(Square):
	def area(self): # Overridden Method
		self.l,self.b=float(input("Enter Length:")),float(input("Enter breadth:"))
		self.ra=self.l*self.b
		print("Area of Rect={}".format(self.ra))
		print("-"*50)
		super().area()


#main program
r=Rect()
r.area()
