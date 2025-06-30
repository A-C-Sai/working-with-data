#PolyEx2.py
class Circle:
	def   draw(self): # Original Method
		print("Drawing Circle")

class Rect(Circle):
	def draw(self):   # Overridden Method
		print("Drawing Rect")
class Square(Rect):
	def draw(self): # Overridden method
		print("Dawing Square")
		Circle.draw(self)
		Rect.draw(self)

#main program
s=Square()
s.draw()
	