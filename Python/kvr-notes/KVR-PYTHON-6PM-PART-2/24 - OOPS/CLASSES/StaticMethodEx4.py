#Program for all types of Arithmetic Operations by using Class and objects with Static Method
#StaticMethodEx4.py
class Aop:
	def readvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
		self.op=input("Enter Arithmetic Operator:")
		self.cal()	#calling Static Method By using self
	@staticmethod
	def  cal():
		match(a.op):
			case "+":
				print("sum({},{})={}".format(a.a,a.b,a.a+a.b))
			case "-":
				print("sub({},{})={}".format(a.a,a.b,a.a-a.b))
			case "*":
				print("mul({},{})={}".format(a.a,a.b,a.a*a.b))
			case '/':
				print("div({},{})={}".format(a.a,a.b,a.a/a.b))
			case """//""":
				print("Floor Div({},{})={}".format(a.a,a.b,a.a//a.b))
			case "%":
				print("Mod({},{})={}".format(a.a,a.b,a.a%a.b))
			case "**":
				print("pow({},{})={}".format(a.a,a.b,a.a**a.b))
			case _:
				print("{} is not an Arithmetic Operator:".format(a.op))

#main program
a=Aop()
a.readvalues()