#Program for cal area of Different Figures by using OOPs 
#PloyEx4.py
class Circle:
	def __init__(self,r):
		self.ac=3.14*r**2
		print("Area of Circle={}".format(self.ac))

class Square:
	def __init__(self,s): # Overridden Constructors
		self.sa=s**2
		print("Area of Square={}".format(self.sa))
		
		
class Rect(Circle,Square):
	def __init__(self,l,b): # Overridden Constructors
		self.ra=l*b
		print("Area of Rect={}".format(self.ra))
		print("-"*50)
		super().__init__(float(input("Enter Radious:")))
		print("-"*50)
		Square.__init__(self,float(input("Enter Side:")))
		
		
#main program
r=Rect(float(input("Enter Length:")),float(input("Enter breadth:")))
