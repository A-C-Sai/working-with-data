#MethodOverEx2.py
class Circle:
	def    draw(self):  # Original Method
		print("Drawing Circle")

class Rect(Circle):
	def draw(self):  # Overridden Method
		print("Drawing Rect")
		super().draw()

class Square(Rect):
	def  draw(self): # Overridden Method
		print("Drawing Square:")
		super().draw()
		


#main program
print("w.r.t Square")
s=Square()
s.draw()
