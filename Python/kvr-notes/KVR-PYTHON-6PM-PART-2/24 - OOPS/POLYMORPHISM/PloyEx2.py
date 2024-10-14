#Program for cal area of Different Figures by using OOPs 
#PloyEx2.py
class Circle:
	def area(self,r):
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))
class Square(Circle):
	def area(self,s): # Overridden Method
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		print("-"*50)
		super().area(float(input("Enter Radious:")))
		
class Rect(Square):
	def area(self,l,b): # Overridden Method
		self.ra=l*b
		print("Area of Rect={}".format(self.ra))
		print("-"*50)
		super().area(float(input("Enter Side:")))
		
#main program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter breadth:")))
