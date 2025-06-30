#program for demonstrating Parametrized Constructor
#ParamDefualtConstEx1.py
class Test:
	def __init__(self,k=1,v=2): # default and parameterized
		print("i am from default / Parametrized constructor:")
		self.a=k
		self.b=v
		print("\ta={}\tb={}".format(self.a,self.b))

#main program
t1=Test()# Object creation calls default Constructor
t2=Test(10,20)# Object creation calls Parametrized Constructor
