#program for demonstrating Default Constructor
#DefaultConstEx1.py
class Test:
	def __init__(self):
		print("i am from default constructor:")
		self.a=10
		self.b=20
		print("\ta={}\tb={}".format(self.a,self.b))

#main program
t1=Test()# Object creation calls default constructor
t2=Test()# Object creation calls default constructor
t3=Test()# Object creation calls default constructor