#Non-MethodOverrideEx1.py
class Circle:  # Base Class
	def  draw1(self): 
		print("Drawing Circle:")

class Rect(Circle):  # Derived Class
	def draw2(self):
		print("Drawing Rect")
		self.draw1()
		

#main program
print("w.r.t Rect Class Object")
r=Rect()
r.draw2()