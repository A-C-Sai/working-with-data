#Program for cal area of Different Figures by using OOPs 
#PloyEx3.py
class Circle:
	def area(self,r):
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))

class Square:
	def area(self,s): # Overridden Method
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		
		
class Rect(Circle,Square):
	def area(self,l,b): # Overridden Method
		self.ra=l*b
		print("Area of Rect={}".format(self.ra))
		print("-"*50)
		super().area(float(input("Enter Radious:")))
		print("-"*50)
		Square.area(self,float(input("Enter Side:")))
		
		
#main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter breadth:")))