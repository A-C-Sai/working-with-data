#InhProg5.py
class GrandParent:
	def grandparentprop(self):
		self.gpp=float(input("Enter Grand Parent Property:"))
		return self.gpp
class Father(GrandParent):
	def fatherprop(self):
		self.fp=float(input("Enter father Property:"))
		return self.fp
class Mother:
	def motherprop(self):
		self.mp=float(input("Enter Mother Property:"))
		return self.mp
class Child(Father,Mother):
	def totprop(self):
		self.cp=float(input("Enter Child Property:"))
		gp1=self.grandparentprop()
		fp1=self.fatherprop()
		mp1=self.motherprop()
		totprop=fp1+mp1+self.cp+gp1
		print("="*50)
		print("Grand Parent Property:{}".format(gp1))
		print("Parent Property:{}".format(fp1))
		print("Mother Property:{}".format(mp1))
		print("Child Property:{}".format(self.cp))
		print("Total Property of child:{}".format(totprop))
		print("="*50)

#main program
Child().totprop() # here Child() is called Name-Less object
