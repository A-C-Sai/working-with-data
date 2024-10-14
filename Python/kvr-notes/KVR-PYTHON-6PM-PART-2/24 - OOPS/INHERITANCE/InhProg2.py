#InhProg2.py
class Parent:
	def parentprop(self):
		self.pp=float(input("Enter Parent Property:"))
		return self.pp
class Child(Parent):
	def childprop(self):
		self.cp=float(input("Enter Child Property:"))
		return self.cp
	def totprop(self):
		pp1=self.parentprop()
		cp1=self.childprop()
		totprop=pp1+cp1
		print("="*50)
		print("Parent Property:{}".format(pp1))
		print("Child Property:{}".format(cp1))
		print("Total Property of child:{}".format(totprop))
		print("="*50)

#main programs
co=Child()
co.totprop()
