#ConstOverrideEx.py
class Circle:
	def __init__(self): # Original  Const
		print("Drawing--Circle")

class Rect(Circle):
	def __init__(self): # Ovveridden Const
		print("Drawing--Rect")
		#super().__init__()

class Square(Rect):
	def __init__(self): # Ovveridden Const
		print("Drawing--Square")
		Rect.__init__(self)
		Circle.__init__(self)


#main program
s=Square() # Object creartion----


