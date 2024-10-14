
#AopOp.py----File Name and Module Name
class Aop:
	def readvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
		self.op=input("Enter Arithmetic Operator:")
		# self.cal(self)	#calling Static Method By using self
		#OR
		Aop.cal(self)   # Calling static method by using Class Name
	@staticmethod
	def  cal(a):
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

