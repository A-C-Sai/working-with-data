#program adding twoi values by using Classes and objects with Instance Methods
#SumExInstanceMethod1.py
class Sum:
	def readvals(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
	def addop(self):
		self.c=self.a+self.b

	def disp(self):
		self.readvals()
		self.addop()
		print("sum({},{})={}".format(self.a,self.b,self.c))

#main program,
s=Sum()
s.disp()
