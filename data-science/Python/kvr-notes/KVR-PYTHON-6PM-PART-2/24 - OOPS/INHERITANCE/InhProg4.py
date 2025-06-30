#InhProg4.py
class Father:
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
		fp1=self.fatherprop()
		mp1=self.motherprop()
		totprop=fp1+mp1+self.cp
		print("="*50)
		print("Parent Property:{}".format(fp1))
		print("Mother Property:{}".format(mp1))
		print("Child Property:{}".format(self.cp))
		print("Total Property of child:{}".format(totprop))
		print("="*50)

#main program
co=Child()
co.totprop()
print("================OR===================")
Child().totprop() # here Child() is called Name-Less object
