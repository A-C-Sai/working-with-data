
#AopOp1.py----File Name and Module Name
class Aop:
	def readvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
		self.op=input("Enter Arithmetic Operator:")
		Aop.getresult(self)   # Calling static method by using Class Name
	@classmethod
	def  getresult(cls,obj):
		cls.cal(obj) # Calling Static method w.r.t cls.
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
		
