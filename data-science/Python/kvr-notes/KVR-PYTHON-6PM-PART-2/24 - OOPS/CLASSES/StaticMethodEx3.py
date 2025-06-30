#Program for all types of Arithmetic Operations by using Class and objects with Static Method
#StaticMethodEx3.py
class Aop:
	def readvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
		self.op=input("Enter Arithmetic Operator:")

class Operations:
	@staticmethod
	def  cal(obj):
		match(obj.op):
			case "+":
				print("sum({},{})={}".format(obj.a,obj.b,obj.a+obj.b))
			case "-":
				print("sub({},{})={}".format(obj.a,obj.b,obj.a-obj.b))
			case "*":
				print("mul({},{})={}".format(obj.a,obj.b,obj.a*obj.b))
			case '/':
				print("div({},{})={}".format(obj.a,obj.b,obj.a/obj.b))
			case """//""":
				print("Floor Div({},{})={}".format(obj.a,obj.b,obj.a//obj.b))
			case "%":
				print("Mod({},{})={}".format(obj.a,obj.b,obj.a%obj.b))
			case "**":
				print("pow({},{})={}".format(obj.a,obj.b,obj.a**obj.b))
			case _:
				print("{} is not an Arithmetic Operator:".format(obj.op))

#main program
a=Aop() # object creation
a.readvalues()
Operations.cal(a) # calling static method by using class name
