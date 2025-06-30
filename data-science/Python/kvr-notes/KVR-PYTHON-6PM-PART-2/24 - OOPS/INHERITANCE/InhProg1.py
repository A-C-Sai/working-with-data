#Program demonstrating Inheritance
#InhProg1.py
class C1:
	def  getA(self):
		self.a=10
class C2(C1): # Single Inheritance
	def getB(self):
		self.b=20
	def operate(self):
		c=self.a+self.b
		print("sum({},{})={}".format(self.a,self.b,c))
	
#main program
o2=C2()
print("content of o2=",o2.__dict__)
o2.getB()
print("content of o2=",o2.__dict__)
o2.getA()
print("content of o2=",o2.__dict__)
o2.operate()
print("content of o2=",o2.__dict__)