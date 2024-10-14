#MethodOverrideEx1.py
class Circle:  # Base Class
	def  draw(self): # Original Method--One Form
		print("Drawing Circle:")
		#super().draw() error

class Rect(Circle):  # Derived Class
	def draw(self): # Overridden Method---Multiple Form
		print("Drawing Rect")
		super().draw()

class Square(Rect):
	def draw(self): # Overridden Method---Multiple Form
		print("Drawing Square")
		super().draw()


#main program
print("w.r.t Square Class Object")
s=Square()
s.draw()
