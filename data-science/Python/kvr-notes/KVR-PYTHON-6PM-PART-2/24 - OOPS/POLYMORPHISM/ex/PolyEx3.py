#PolyEx3.py
class Circle:
	def   __init__(self): # Original default Constructor
		print("Drawing Circle--DC")

class Rect(Circle):
	def __init__(self): # Overriddent default constructor
		print("Drawing Rect--DC")
		super().__init__()


#main program
ro=Rect() # Object Creation and calls Default Constructor
