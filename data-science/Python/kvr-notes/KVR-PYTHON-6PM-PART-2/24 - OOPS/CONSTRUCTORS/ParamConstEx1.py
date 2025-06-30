#program for demonstrating Parametrized Constructor
#ParamConstEx1.py
class Test:
	def __init__(self,k,v):
		print("i am from Parametrized constructor:")
		self.a=k
		self.b=v
		print("\ta={}\tb={}".format(self.a,self.b))

#main program
t1=Test(10,20)# Object creation calls Parametrized Constructor
t2=Test(100,200)# Object creation calls Parametrized Constructor
t3=Test(1000,2000)# Object creation calls Parametrized Constructor